# 03 — MISP Object Modeling

## Overview

Individual MISP attributes are useful for recording indicators of compromise (IOCs), but structured objects provide additional analytical context by representing relationships between related indicators.

During this investigation, the simulated phishing domain and destination IP address were modeled using a MISP `domain-ip` object.

This allowed the investigation to represent the relationship between the phishing infrastructure components rather than treating the domain and IP address only as independent indicators.

---

## Domain-to-IP Relationship

The following indicators were associated during the investigation:

| Object Component | Value | MISP Type |
|---|---|---|
| Domain | `secure-login-support.com` | `domain` |
| Destination IP | `198.51.100.23` | `ip-dst` |

The relationship can be represented conceptually as:

```text
secure-login-support.com
          |
          v
    198.51.100.23
```

Within the simulated investigation, this represents a phishing domain associated with destination infrastructure.

> **Lab Safety Notice:** `198.51.100.23` belongs to an IPv4 documentation range and is used here intentionally for defensive cybersecurity training. The infrastructure represented in this project is simulated.

---

## Why Use a MISP Object?

Recording the domain and IP as separate attributes preserves both indicators, but it does not inherently describe their relationship.

A `domain-ip` object provides structured context by grouping related attributes within the same analytical object.

This approach improves the quality of threat intelligence because analysts can understand not only **what indicators exist**, but also **how those indicators relate to one another**.

The object therefore models the relationship:

```text
Phishing Infrastructure
        |
        +-- Domain
        |     |
        |     +-- secure-login-support.com
        |
        +-- Destination IP
              |
              +-- 198.51.100.23
```

---

## MISP Object Configuration

The `domain-ip` object was configured with the following primary fields:

### Domain

```text
secure-login-support.com
```

MISP attribute type:

```text
domain
```

Category:

```text
Network activity
```

Correlation was enabled so the indicator could participate in MISP correlation workflows.

### Destination IP

```text
198.51.100.23
```

MISP attribute type:

```text
ip-dst
```

Category:

```text
Network activity
```

Correlation was also enabled for the destination IP.

### Object Comment

The relationship was documented with the analyst comment:

```text
Domain-to-IP relationship observed during simulated phishing investigation.
```

This provides investigative context for analysts reviewing the object.

---

## Object-Level Analysis

The completed object groups the domain and destination IP under a single `domain-ip` structure.

This is analytically stronger than maintaining only disconnected IOC records because it preserves the infrastructure relationship discovered during the investigation.

For a SOC or Cyber Threat Intelligence workflow, structured object modeling can assist with:

- infrastructure analysis;
- IOC correlation;
- threat hunting;
- campaign tracking;
- incident scoping;
- detection engineering; and
- intelligence sharing.

---

## Relationship to the Phishing Scenario

The domain-IP relationship forms part of the larger simulated attack chain:

```text
Phishing Activity
       |
       v
secure-login-support.com
       |
       +--------------------+
       |                    |
       v                    v
198.51.100.23        /account/verify
                            |
                            v
                 Credential-Harvesting
                       Endpoint
```

The SHA-256 indicator documented elsewhere in the investigation represents the file-based component of the simulated phishing activity.

Together, these indicators provide both network and payload context for the investigation.

---

## Analyst Interpretation

The creation of the `domain-ip` object demonstrates an important threat-intelligence principle:

> **Context increases the analytical value of an IOC.**

A domain by itself may be useful for detection. An IP address by itself may also support threat hunting.

When the relationship between them is preserved, however, analysts gain additional infrastructure context that can support pivoting and correlation during an investigation.

MISP objects provide a standardized mechanism for preserving these relationships.

---

## Investigation Result

The investigation successfully modeled:

- the simulated phishing domain;
- the associated destination IP;
- the relationship between the two indicators;
- their network-activity classifications; and
- their correlation properties.

The resulting object provides a structured representation of the simulated phishing infrastructure within MISP.

---

## Next Section

Continue to:

[04 — MITRE ATT&CK Mapping](04-mitre-attack-mapping.md)
