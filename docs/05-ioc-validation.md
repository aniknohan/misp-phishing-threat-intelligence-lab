# 05 — IOC Validation and Search

## Overview

After the simulated phishing indicators were entered and structured within MISP, each primary IOC was searched individually to verify that it had been successfully recorded and was available for analyst retrieval and correlation.

The validation process covered four indicator types:

- Domain
- Destination IP address
- SHA-256 file hash
- URL

This step demonstrates a common threat-intelligence workflow in which analysts pivot on an observed indicator to identify matching intelligence records and associated investigation context.

---

## Validation Methodology

Each IOC was entered into the MISP attribute search interface.

The validation workflow was:

```text
Observed IOC
     |
     v
MISP Attribute Search
     |
     v
Matching Attribute
     |
     v
Associated Event
     |
     v
Investigation Context
```

A successful result confirmed that the indicator was stored within MISP and could be retrieved during subsequent investigations or threat-hunting activities.

---

# 1. Domain IOC Validation

## Search Value

```text
secure-login-support.com
```

## Expected Attribute Type

```text
domain
```

## Result

MISP successfully returned records associated with the simulated phishing investigation.

![MISP domain IOC search results](../evidence/screenshots/misp-ioc-domain-search-results.png)

**Figure 1 — Domain IOC search results for `secure-login-support.com`.**

Two matching domain records are visible because the domain was represented both as an individual IOC attribute and as an attribute within the structured `domain-ip` object.

This demonstrates the distinction between independently searchable indicators and structured MISP object relationships.

### Analyst Finding

**Validation Status:** Successful

The domain was successfully indexed and retrievable through MISP attribute search.

---

# 2. Destination IP IOC Validation

## Search Value

```text
198.51.100.23
```

## Expected Attribute Type

```text
ip-dst
```

## Result

MISP returned the destination-IP records associated with the investigation.

![MISP IP IOC search results](../evidence/screenshots/misp-ioc-ip-search-results.png)

**Figure 2 — Destination IP IOC search results for `198.51.100.23`.**

As with the domain, two matching records are expected because the destination IP exists both as an individual attribute and within the `domain-ip` object.

The address belongs to a documentation range and was intentionally used for the simulated investigation.

### Analyst Finding

**Validation Status:** Successful

The destination IP was successfully indexed and available for correlation and analyst search.

---

# 3. SHA-256 IOC Validation

## Search Value

```text
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

## Expected Attribute Type

```text
sha256
```

## Result

MISP returned a single matching SHA-256 attribute associated with the simulated phishing investigation.

![MISP SHA-256 IOC search results](../evidence/screenshots/misp-ioc-sha256-search-results.png)

**Figure 3 — SHA-256 IOC search result for the simulated attachment indicator.**

Unlike the domain and destination IP, the SHA-256 indicator was not duplicated within the `domain-ip` object. Therefore, one result was expected.

### Analyst Finding

**Validation Status:** Successful

The file-based IOC was successfully recorded as a `sha256` attribute and could be retrieved through MISP search.

---

# 4. URL IOC Validation

## Search Value

```text
http://secure-login-support.com/account/verify
```

## Expected Attribute Type

```text
url
```

## Result

MISP successfully returned the complete simulated credential-harvesting URL.

![MISP URL IOC search results](../evidence/screenshots/misp-ioc-url-search-results.png)

**Figure 4 — URL IOC search result for the simulated credential-harvesting endpoint.**

The URL was stored independently from the domain, allowing analysts to search for the complete network indicator rather than relying only on domain-level matching.

### Analyst Finding

**Validation Status:** Successful

The complete URL was successfully indexed and retrievable within MISP.

---

# Validation Summary

| IOC | Type | Expected Results | Validation |
|---|---|---:|---|
| `secure-login-support.com` | `domain` | 2 | Successful |
| `198.51.100.23` | `ip-dst` | 2 | Successful |
| SHA-256 attachment indicator | `sha256` | 1 | Successful |
| Credential-harvesting URL | `url` | 1 | Successful |

The two-result behavior for the domain and destination IP is expected because both indicators were maintained as standalone attributes and incorporated into the `domain-ip` object.

---

## SOC Analyst Relevance

IOC search and validation are important capabilities in operational security environments.

An analyst receiving a suspicious domain, IP address, URL, or file hash could use a threat-intelligence platform to determine whether the indicator:

- has been previously observed;
- appears in another investigation;
- is associated with known infrastructure;
- has relationships with additional indicators;
- belongs to an existing campaign or event; or
- provides context for a current alert.

This allows threat intelligence to support incident triage rather than functioning only as static documentation.

---

## Example SOC Pivot Workflow

A practical investigation could follow this process:

```text
SIEM / EDR / Email Alert
          |
          v
     Extract IOC
          |
          v
     Search MISP
          |
          +---- No Match ---> Continue Enrichment
          |
          |
          +---- Match
                 |
                 v
          Review MISP Event
                 |
                 v
        Identify Related IOCs
                 |
                 v
       Hunt Across Telemetry
```

For example, an analyst investigating a phishing alert could search the observed domain in MISP, identify the related destination IP and URL, and then pivot into DNS, proxy, firewall, email, or endpoint telemetry.

---

## Investigation Outcome

All four primary IOC types were successfully validated through MISP search.

The results confirm that the investigation data was structured in a way that supports:

- analyst retrieval;
- IOC correlation;
- threat hunting;
- investigation pivoting;
- infrastructure analysis; and
- future incident triage.

The validation phase therefore confirms that the indicators were not merely documented—they were made searchable and reusable as threat-intelligence artifacts.

---

## Next Section

Continue to:

[06 — Analyst Conclusion](06-analyst-conclusion.md)
