# 08 — Operationalizing the Intelligence

## Overview

Phases 01–07 built and correlated intelligence inside MISP. This phase takes it out of MISP and into the tools a SOC actually alerts from:

| Artifact | File | Purpose |
|---|---|---|
| IOC list | [`data/iocs.csv`](../data/iocs.csv) | The four event 1 indicators, defanged, with category and IDS flag |
| MISP lookup script | [`scripts/misp_ioc_lookup.py`](../scripts/misp_ioc_lookup.py) | Enrich indicators against MISP's REST API |
| Sigma rules | [`detections/sigma/`](../detections/sigma/) | Vendor-neutral DNS, proxy and process-hash detections |
| Splunk hunts | [`detections/splunk_ioc_hunt.spl`](../detections/splunk_ioc_hunt.spl) | DNS, web, Sysmon and lookup-based hunts |
| Suricata rules | [`detections/suricata_lab_iocs.rules`](../detections/suricata_lab_iocs.rules) | Network detections for DNS, HTTP, TLS SNI and IP |

```text
MISP event 1 ──► data/iocs.csv ──┬──► misp_ioc_lookup.py   (enrich an alert)
                                 ├──► Sigma rules          (any SIEM)
                                 ├──► Splunk hunts         (search history)
                                 └──► Suricata rules       (network sensor)
```

---

## 1. MISP IOC Lookup Script

`scripts/misp_ioc_lookup.py` implements the first step of the SOC workflow in the README: *extract IOC → search MISP*. It calls the same `/attributes/restSearch` endpoint reviewed in [phase 07](07-misp-threat-correlation.md#16-rest-api-and-automation), re-fangs defanged values, and groups matches by event with their tags.

It uses only the Python standard library, so there is nothing to install.

```bash
export MISP_URL="https://<your-misp>"
export MISP_KEY="<auth key>"            # from your MISP profile; never commit it

python3 scripts/misp_ioc_lookup.py                       # all IOCs in data/iocs.csv
python3 scripts/misp_ioc_lookup.py --ioc 5.45.86.171     # one value, e.g. from an alert
python3 scripts/misp_ioc_lookup.py --json results.json   # also save machine-readable results
python3 scripts/misp_ioc_lookup.py --insecure            # lab instance with a self-signed certificate
```

Example output (from testing against a mock MISP API that returns the same response format):

```text
[+] secure-login-support.com  ->  MATCH in 1 event(s)
      event 1: SOC Investigation - Suspicious Phishing Infrastructure  [domain]  (no tags)

[+] 5.45.86.171  ->  MATCH in 1 event(s)
      event 486: OSINT - Locky  [ip-dst]  (malware_classification:malware-category="Ransomware", tlp:white)

Summary: 2/4 indicator(s) found in MISP.
```

Error handling covers a rejected key (HTTP 401/403), an unreachable server and a non-JSON response, each with a one-line message.

---

## 2. Sigma Rules

| Rule | Log source | Detects | ATT&CK |
|---|---|---|---|
| [`dns_query_phishing_domain.yml`](../detections/sigma/dns_query_phishing_domain.yml) | `dns_query` | Resolution of the phishing domain or its subdomains | T1566.002, T1598.003 |
| [`proxy_phishing_url.yml`](../detections/sigma/proxy_phishing_url.yml) | `proxy` | Web requests to the domain or destination IP | T1566.002, T1598.003 |
| [`file_hash_lab_attachment.yml`](../detections/sigma/file_hash_lab_attachment.yml) | `process_creation` (Windows) | Execution of a file with the attachment's SHA-256 | T1566.001 |

Sigma rules can be converted to Splunk, Microsoft Sentinel, Elastic and other backends with `sigma-cli`:

```bash
pip install sigma-cli
sigma plugin install splunk
sigma convert -t splunk -p sysmon detections/sigma/file_hash_lab_attachment.yml
```

Because the hash is the **EICAR test file**, the process-hash rule can be tested safely: create the EICAR file on a lab endpoint with Sysmon installed and confirm the alert fires.

---

## 3. Splunk Hunts

[`splunk_ioc_hunt.spl`](../detections/splunk_ioc_hunt.spl) contains four independent searches:

1. **DNS:** which hosts resolved the phishing domain, with first and last seen.
2. **Web/proxy:** which users reached the domain or IP, and whether they hit `/account/verify` (the harvesting page).
3. **Endpoint:** Sysmon process creation matching the attachment hash.
4. **Lookup-based:** every IOC at once, from `data/iocs.csv` uploaded as a lookup.

Searches 1 and 2 use the CIM data models, so they work across any DNS or proxy source that is CIM-mapped.

---

## 4. Suricata Rules

[`suricata_lab_iocs.rules`](../detections/suricata_lab_iocs.rules) adds five network detections using the local SID range `9000001–9000005`:

| SID | Protocol | Match |
|---|---|---|
| 9000001 | DNS | Query for the phishing domain or any subdomain |
| 9000002 | HTTP | Host header for the phishing domain |
| 9000003 | HTTP | Host plus `/account/verify` path (credential page reached) |
| 9000004 | IP | Any traffic to `198.51.100.23` |
| 9000005 | TLS | SNI for the phishing domain (catches HTTPS) |

These complement the rules MISP generated automatically in [phase 07](07-misp-threat-correlation.md#14-suricata-detection-rule-export). The `dotprefix` + `endswith` pattern matches the domain and its subdomains without matching look-alikes such as `notsecure-login-support.com`.

Validate before deploying:

```bash
suricata -T -S detections/suricata_lab_iocs.rules -c /etc/suricata/suricata.yaml
```

---

## 5. Completing the Lab in MISP

These improvements need changes on the MISP instance itself. Each one is small and produces a strong new screenshot.

| Step | How | Why it matters |
|---|---|---|
| **Update galaxies** | *Galaxies → List Galaxies → Update Galaxies*, then remove the `T1192` cluster from event 1 and add **Spearphishing Link (T1566.002)** | The event then shows the current ATT&CK ID instead of a revoked one |
| **Add an analyst tag** | Add `tlp:green` and `misp-galaxy:mitre-attack-pattern` tags to event 1 | Shows sharing control and behaviour tagging |
| **Publish event 1** | *Publish Event* on event 1 (currently unpublished) | Completes the IOC lifecycle; published events can be shared and exported |
| **Add a sighting** | Click the thumbs-up sighting icon on the domain attribute | Records that the indicator was observed, a key CTI feedback loop |
| **Run the lookup script** | Create an auth key and run `scripts/misp_ioc_lookup.py` | Real output from your own instance |
| **Test the Suricata rules** | Load the rules into a lab sensor and replay a PCAP containing a DNS query for the domain | Proves intelligence → detection end to end |

---

## Analyst Takeaway

Intelligence only reduces risk when it reaches a control. This phase connects the MISP event to enrichment (the lookup script), search (Splunk), alerting (Sigma) and network detection (Suricata), the same path an indicator takes in a production SOC.
