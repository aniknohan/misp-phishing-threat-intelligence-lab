# 04 — MITRE ATT&CK Mapping

## Overview

After documenting the indicators associated with the simulated phishing investigation, the activity was mapped to the MITRE ATT&CK framework using a MISP Galaxy.

The purpose of this step was to add behavioral context to the technical indicators and demonstrate how threat intelligence can be connected to an adversary technique.

The phishing activity was mapped in MISP to:

| Framework | Technique |
|---|---|
| MITRE ATT&CK | Spearphishing Link |
| ATT&CK ID displayed by the MISP Galaxy | `T1192` |
| Investigation Context | Credential-harvesting phishing |
| MISP Integration | Enterprise Attack - Attack Pattern Galaxy |

> **Version Note:** The MISP Galaxy used in this lab displays `Spearphishing Link - T1192`. ATT&CK technique identifiers can change as the framework evolves, so this project preserves the identifier displayed by the lab environment rather than rewriting the historical evidence.

---

## Why Spearphishing Link?

The simulated investigation centered on a phishing URL:

```text
http://secure-login-support.com/account/verify
```

The URL represents a credential-harvesting endpoint delivered as part of the simulated phishing scenario.

The attack flow can therefore be represented as:

```text
Phishing Message
       |
       v
Malicious / Suspicious Link
       |
       v
secure-login-support.com
       |
       v
/account/verify
       |
       v
Credential-Harvesting Infrastructure
```

This behavior is consistent with a spearphishing-link technique because the attack depends on directing a target to attacker-controlled or simulated malicious web infrastructure.

---

## MISP Galaxy Mapping

MISP Galaxies provide a structured mechanism for associating threat-intelligence data with standardized threat knowledge.

For this investigation, the event was associated with the:

```text
Enterprise Attack - Attack Pattern
```

Galaxy cluster.

The selected technique was:

```text
Spearphishing Link - T1192
```

This connects the technical IOC investigation with an adversary behavior represented in the MITRE ATT&CK knowledge base.

---

## ATT&CK Correlation Evidence

The following MISP correlation graph demonstrates the relationship between the investigation event and the selected ATT&CK Galaxy cluster.

![MISP correlation graph showing Spearphishing Link T1192](../evidence/screenshots/misp-correlation-graph-spearphishing-link.png)

**Figure 1 — MISP correlation graph linking the simulated phishing investigation to the Spearphishing Link ATT&CK Galaxy cluster.**

The graph provides visual confirmation that the MISP event was associated with the selected ATT&CK technique.

---

## Intelligence Context

Mapping the activity to ATT&CK adds behavioral context to the IOC data.

Without ATT&CK mapping, the investigation contains indicators such as:

```text
Domain
secure-login-support.com

Destination IP
198.51.100.23

URL
http://secure-login-support.com/account/verify

SHA-256
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

These indicators describe observable artifacts.

The ATT&CK mapping adds another analytical layer by describing the **behavior represented by those artifacts**.

Conceptually:

```text
Indicators of Compromise
        |
        v
Infrastructure Analysis
        |
        v
Behavioral Interpretation
        |
        v
MITRE ATT&CK
        |
        v
Spearphishing Link
```

---

## IOC-to-Technique Relationship

The indicators contribute different pieces of context to the investigation:

| Indicator | Analytical Role |
|---|---|
| `secure-login-support.com` | Simulated phishing infrastructure |
| `198.51.100.23` | Simulated destination infrastructure |
| `/account/verify` URL | Credential-harvesting endpoint |
| SHA-256 | Simulated malicious attachment indicator |
| Spearphishing Link | Behavioral ATT&CK mapping |

The combination of IOC analysis and ATT&CK mapping transforms a collection of technical artifacts into a more structured threat-intelligence record.

---

## Analyst Interpretation

ATT&CK mapping is valuable because SOC and Cyber Threat Intelligence analysts should not stop at identifying individual indicators.

An analyst should also determine:

- what behavior the indicators represent;
- how the infrastructure supports the attack;
- which adversary technique best describes the observed activity;
- how the intelligence can support detection or threat hunting; and
- how the findings can be communicated using a standardized framework.

In this investigation, the MISP Galaxy association provides that behavioral context.

---

## Defensive Value

Mapping phishing activity to ATT&CK can support defensive operations by helping analysts connect threat intelligence with:

- detection engineering;
- SIEM investigations;
- threat hunting;
- phishing detection;
- incident response;
- security-control validation; and
- intelligence reporting.

For example, the domain and URL could be used as search pivots in proxy, DNS, firewall, or SIEM telemetry while the ATT&CK mapping explains the adversary behavior being investigated.

---

## Investigation Result

The simulated phishing investigation was successfully associated with the MISP Enterprise Attack Galaxy and mapped to the **Spearphishing Link** attack pattern displayed by the lab environment.

This demonstrates the progression from:

```text
IOC Collection
      ↓
IOC Structuring
      ↓
Infrastructure Correlation
      ↓
Behavioral Analysis
      ↓
MITRE ATT&CK Mapping
```

The result is a more contextualized threat-intelligence record than a standalone collection of indicators.

---

## Next Section

Continue to:

[05 — IOC Validation](05-ioc-validation.md)
