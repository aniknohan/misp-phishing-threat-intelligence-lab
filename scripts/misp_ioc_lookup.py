#!/usr/bin/env python3
"""
MISP IOC lookup: enrich a list of indicators against a MISP instance.

Reads indicators from a CSV file (default: data/iocs.csv), re-fangs them,
queries MISP's /attributes/restSearch endpoint for each one and prints which
events already know about it. This is the "alert -> extract IOC -> search MISP"
step of the SOC workflow described in the README.

Uses only the Python standard library, so it runs anywhere Python 3.8+ does.

Usage:
    export MISP_URL="https://192.168.255.137"
    export MISP_KEY="<your auth key>"          # never commit this
    python3 scripts/misp_ioc_lookup.py                     # uses data/iocs.csv
    python3 scripts/misp_ioc_lookup.py --ioc 5.45.86.171   # single value
    python3 scripts/misp_ioc_lookup.py --json results.json # also save JSON
    python3 scripts/misp_ioc_lookup.py --insecure          # lab self-signed cert
"""

import argparse
import csv
import http.client
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from collections import defaultdict


def refang(value: str) -> str:
    """Turn a defanged indicator back into its searchable form."""
    return (
        value.strip()
        .replace("[.]", ".")
        .replace("(.)", ".")
        .replace("[:]", ":")
        .replace("hxxps://", "https://")
        .replace("hxxp://", "http://")
    )


def load_iocs(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if "value" not in (reader.fieldnames or []):
            sys.exit(f"[!] {path} must have a 'value' column")
        return [
            {"type": row.get("type", ""), "value": refang(row["value"])}
            for row in reader
            if row.get("value", "").strip()
        ]


def misp_search(base_url: str, key: str, value: str, context: ssl.SSLContext, timeout: int) -> list:
    """Query /attributes/restSearch for an exact value; return matching attributes."""
    url = base_url.rstrip("/") + "/attributes/restSearch"
    body = json.dumps({"returnFormat": "json", "value": value, "includeEventTags": True}).encode()
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, context=context, timeout=timeout) as resp:
        data = json.load(resp)
    return data.get("response", {}).get("Attribute", [])


def summarize(attributes: list) -> dict:
    """Group matching attributes by event."""
    events = defaultdict(lambda: {"info": "", "types": set(), "tags": set()})
    for attr in attributes:
        event = attr.get("Event", {})
        event_id = str(attr.get("event_id") or event.get("id", "?"))
        events[event_id]["info"] = event.get("info", events[event_id]["info"])
        events[event_id]["types"].add(attr.get("type", "?"))
        for tag in attr.get("Tag", []) + event.get("Tag", []):
            events[event_id]["tags"].add(tag.get("name", ""))
    return events


def main() -> int:
    parser = argparse.ArgumentParser(description="Look up IOCs in MISP via restSearch.")
    parser.add_argument("--csv", default="data/iocs.csv", help="CSV of indicators (needs a 'value' column)")
    parser.add_argument("--ioc", action="append", help="single indicator to look up (repeatable)")
    parser.add_argument("--json", help="write full results to this JSON file")
    parser.add_argument("--insecure", action="store_true", help="skip TLS verification (lab self-signed certs only)")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    base_url = os.environ.get("MISP_URL")
    key = os.environ.get("MISP_KEY")
    if not base_url or not key:
        sys.exit("[!] Set MISP_URL and MISP_KEY environment variables first.")

    iocs = [{"type": "", "value": refang(v)} for v in args.ioc] if args.ioc else load_iocs(args.csv)
    context = ssl._create_unverified_context() if args.insecure else ssl.create_default_context()

    results, hits = [], 0
    for ioc in iocs:
        try:
            attributes = misp_search(base_url, key, ioc["value"], context, args.timeout)
        except urllib.error.HTTPError as exc:
            if exc.code in (401, 403):
                sys.exit(f"[!] MISP rejected the auth key (HTTP {exc.code}). Check MISP_KEY.")
            print(f"[!] {ioc['value']}: HTTP {exc.code} {exc.reason}")
            continue
        except (urllib.error.URLError, ConnectionError, http.client.HTTPException) as exc:
            sys.exit(f"[!] Cannot reach MISP at {base_url}: {getattr(exc, 'reason', exc)}")
        except json.JSONDecodeError:
            sys.exit("[!] MISP returned a non-JSON response. Check MISP_URL points at the MISP root.")

        events = summarize(attributes)
        status = f"MATCH in {len(events)} event(s)" if events else "no match"
        hits += bool(events)
        print(f"\n[{'+' if events else '-'}] {ioc['value']}  ->  {status}")
        for event_id, detail in sorted(events.items(), key=lambda kv: kv[0]):
            tags = ", ".join(sorted(t for t in detail["tags"] if t)) or "no tags"
            print(f"      event {event_id}: {detail['info']}  [{', '.join(sorted(detail['types']))}]  ({tags})")
        results.append({
            "value": ioc["value"],
            "matches": [
                {"event_id": eid, "info": d["info"], "types": sorted(d["types"]), "tags": sorted(d["tags"])}
                for eid, d in events.items()
            ],
        })

    print(f"\nSummary: {hits}/{len(iocs)} indicator(s) found in MISP.")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2)
        print(f"Results written to {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
