# MISP Phishing Threat Intelligence Investigation

![MISP](https://img.shields.io/badge/Platform-MISP-blue)
![MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-red)
![Threat Intelligence](https://img.shields.io/badge/Focus-Threat%20Intelligence-orange)
![SOC](https://img.shields.io/badge/Role-SOC%20%2F%20CTI%20Analyst-green)
![Lab](https://img.shields.io/badge/Environment-Simulated-lightgrey)

> A hands-on cyber threat intelligence investigation demonstrating phishing IOC analysis, MISP object modeling, indicator correlation, IOC validation, and MITRE ATT&CK mapping.

---

## Project Overview

This project documents a simulated phishing threat intelligence investigation conducted using MISP (Malware Information Sharing Platform).

The investigation demonstrates how a SOC or Cyber Threat Intelligence (CTI) analyst can transform isolated technical indicators into structured, correlated, and actionable threat intelligence.

The workflow includes:

- Identification and documentation of phishing-related indicators of compromise (IOCs)
- Structured IOC management within MISP
- Domain-to-IP relationship modeling using MISP objects
- IOC correlation and validation
- MITRE ATT&CK mapping
- Analyst assessment and investigation documentation

> **Lab Safety Notice:** All indicators used in this project are simulated or documentation-range artifacts created exclusively for defensive cybersecurity training. No live malicious infrastructure was used.

---
## Investigation Documentation

Detailed analysis and supporting documentation are organized into the following investigation phases:

| Phase | Documentation | Focus |
|---|---|---|
| 01 | [Investigation Overview](docs/01-investigation-overview.md) | Scenario, objectives, scope, and investigation methodology |
| 02 | [IOC Analysis](docs/02-ioc-analysis.md) | Analysis of domain, IP address, URL, and SHA-256 indicators |
| 03 | [MISP Object Modeling](docs/03-misp-object-modeling.md) | Structured domain-to-IP relationship modeling in MISP |
| 04 | [MITRE ATT&CK Mapping](docs/04-mitre-attack-mapping.md) | Mapping phishing activity to Spearphishing Link (T1192) |
| 05 | [IOC Validation](docs/05-ioc-validation.md) | MISP searches used to validate and correlate recorded indicators |
| 06 | [Analyst Conclusion](docs/06-analyst-conclusion.md) | Final assessment, findings, and defensive recommendations |

### Investigation Workflow

`Phishing Scenario` → `IOC Identification` → `MISP Event Creation` → `Object Modeling` → `IOC Correlation` → `MITRE ATT&CK Mapping` → `IOC Validation` → `Analyst Assessment`

---

## Skills Demonstrated

This project demonstrates practical skills applicable to SOC, Cyber Threat Intelligence (CTI), and Blue Team operations:

| Competency | Practical Application |
|---|---|
| Threat Intelligence Analysis | Analyzed and documented phishing-related indicators within a structured intelligence workflow |
| Indicator of Compromise (IOC) Analysis | Investigated domain, destination IP, URL, and SHA-256 indicators |
| MISP Event Management | Created and maintained a structured MISP investigation event |
| MISP Object Modeling | Modeled the relationship between phishing infrastructure using a domain-to-IP object |
| IOC Correlation | Enabled correlation to identify relationships and potential indicator reuse |
| MITRE ATT&CK Mapping | Mapped the simulated phishing activity to Spearphishing Link (T1192) |
| Threat Infrastructure Analysis | Connected domain, IP, URL, and file-hash artifacts within a unified investigation |
| IOC Validation | Queried recorded indicators to verify their presence and investigative context |
| Analyst Documentation | Produced structured investigation notes, evidence, findings, and defensive recommendations |

### Tools & Frameworks

- **MISP** — Threat intelligence management, IOC storage, object modeling, and correlation
- **MITRE ATT&CK** — Adversary technique classification and investigation context
- **GitHub** — Technical documentation, evidence management, and portfolio presentation

---


## Investigation Scenario

The simulated investigation centered on phishing infrastructure designed to represent an account-verification credential-harvesting campaign.

Four primary indicators were analyzed:

| IOC Type | Indicator | MISP Type |
|---|---|---|
| Domain | `secure-login-support.com` | `domain` |
| Destination IP | `198.51.100.23` | `ip-dst` |
| URL | `http://secure-login-support.com/account/verify` | `url` |
| File Hash | `275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f` | `sha256` |

The investigation was maintained as:

```text
Event:        SOC Investigation - Suspicious Phishing Infrastructure
Threat Level: Medium
Analysis:     Completed
```

---

## Investigation Workflow

```text
Phishing Scenario
       |
       v
IOC Identification
       |
       +--> Domain
       +--> Destination IP
       +--> URL
       +--> SHA-256
       |
       v
MISP Event Creation
       |
       v
IOC Classification
       |
       v
Correlation Enabled
       |
       v
domain-ip Object Modeling
       |
       v
MITRE ATT&CK Mapping
       |
       v
IOC Search & Validation
       |
       v
Analyst Assessment
```

---

## MISP Threat Intelligence Model

Rather than maintaining only a flat IOC list, the investigation preserved relationships between the observed artifacts.

```text
                 Phishing Activity
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
       Domain          URL         SHA-256
          |
          v
   Destination IP
```

The domain and destination IP were additionally modeled using a structured MISP `domain-ip` object.

---

## MITRE ATT&CK Mapping

The phishing behavior was associated with the MISP Enterprise ATT&CK Galaxy entry:

**Spearphishing Link — T1192**

The MISP environment used for this lab displayed the legacy `T1192` identifier. The project preserves the identifier shown by the lab environment rather than modifying historical evidence.
---

## IOC Validation

Each primary indicator was searched independently after being entered into MISP.

| Indicator Type | Search Result | Status |
|---|---:|---|
| Domain | 2 records | ✅ Validated |
| Destination IP | 2 records | ✅ Validated |
| SHA-256 | 1 record | ✅ Validated |
| URL | 1 record | ✅ Validated |

The domain and destination IP return two records because each exists both as a standalone attribute and as a component of the structured `domain-ip` object.

## Investigation Evidence

The following evidence captures key stages of the MISP investigation, including ATT&CK mapping and IOC validation.

### MITRE ATT&CK Correlation

![MISP correlation graph showing Spearphishing Link T1192](evidence/screenshots/misp-correlation-graph-spearphishing-link.png)

*MISP correlation graph associating the investigation with the MITRE ATT&CK Spearphishing Link technique (T1192).*

### IOC Validation Evidence

#### Domain

![MISP domain IOC validation](evidence/screenshots/misp-ioc-domain-search-results.png)

*Validation of the simulated phishing domain within the MISP attribute dataset.*

#### Destination IP

![MISP destination IP IOC validation](evidence/screenshots/misp-ioc-ip-search-results.png)

*Validation of the documentation-range destination IP associated with the simulated phishing infrastructure.*

#### SHA-256

![MISP SHA-256 IOC validation](evidence/screenshots/misp-ioc-sha256-search-results.png)

*Validation of the SHA-256 indicator representing the simulated malicious attachment.*

#### URL

![MISP URL IOC validation](evidence/screenshots/misp-ioc-url-search-results.png)

*Validation of the simulated credential-harvesting URL recorded during the investigation.*

> **Evidence Note:** Indicators shown in these screenshots are simulated or documentation-range artifacts used exclusively for defensive cybersecurity training.

---


## Investigation Documentation

Detailed analyst documentation is available in the `docs/` directory:

| Document | Description |
|---|---|
| [01 — Investigation Overview](docs/01-investigation-overview.md) | Scenario, scope, objectives, methodology, and intelligence model |
| [02 — IOC Analysis](docs/02-ioc-analysis.md) | Domain, destination IP, URL, and SHA-256 analysis |
| [03 — MISP Object Modeling](docs/03-misp-object-modeling.md) | Structured domain-to-IP relationship modeling |
| [04 — MITRE ATT&CK Mapping](docs/04-mitre-attack-mapping.md) | ATT&CK Galaxy association and behavioral context |
| [05 — IOC Validation](docs/05-ioc-validation.md) | IOC search, validation, and analyst pivot workflow |
| [06 — Analyst Conclusion](docs/06-analyst-conclusion.md) | Findings, limitations, defensive recommendations, and final assessment |

---

## Repository Structure

```text
misp-phishing-threat-intelligence-lab/
|
├── README.md
├── LICENSE
|
├── docs/
│   ├── 01-investigation-overview.md
│   ├── 02-ioc-analysis.md
│   ├── 03-misp-object-modeling.md
│   ├── 04-mitre-attack-mapping.md
│   ├── 05-ioc-validation.md
│   └── 06-analyst-conclusion.md
|
└── evidence/
    └── screenshots/
        ├── misp-correlation-graph-spearphishing-link.png
        ├── misp-ioc-domain-search-results.png
        ├── misp-ioc-ip-search-results.png
        ├── misp-ioc-sha256-search-results.png
        └── misp-ioc-url-search-results.png
```

---

## SOC Analyst Application

The threat-intelligence workflow demonstrated in this lab can be integrated into operational SOC investigations. Analysts can extract indicators from SIEM, EDR, or email-security alerts and pivot into MISP to identify known infrastructure, related indicators, and additional investigative context.

```text
SIEM / EDR / Email Alert
          |
          v
      Extract IOC
          |
          v
       Search MISP
          |
     +----+----+
     |         |
 No Match     Match
     |         |
     v         v
 Enrich     Review Event
               |
               v
         Related Indicators
               |
               v
         Hunt Telemetry
               |
               v
        Scope Incident
               |
               v
       Defensive Action
```

This workflow demonstrates how threat intelligence can support alert enrichment and incident scoping rather than functioning solely as an IOC repository. By correlating observed indicators with existing intelligence, analysts can pivot across related infrastructure, identify additional artifacts, hunt for associated activity in security telemetry, and make more informed defensive decisions.

---

## Key Takeaways

This investigation demonstrated that effective threat intelligence requires more than collecting technical indicators. Individual IOCs become significantly more valuable when they are enriched with context, structured into relationships, correlated with other intelligence, and mapped to adversary behavior.

Key analytical lessons from the investigation include:

1. **Classification provides structure** — correctly typed domain, IP, URL, and file-hash attributes improve searching, correlation, and downstream analysis.
2. **Context increases intelligence value** — analyst comments and event metadata explain why an indicator matters to the investigation.
3. **Relationships reveal infrastructure** — MISP objects preserve connections between related artifacts, such as the relationship between a domain and its destination IP.
4. **Correlation supports investigative pivoting** — searchable indicators allow analysts to identify related intelligence and pivot across potentially connected activity.
5. **MITRE ATT&CK adds behavioral context** — mapping the phishing activity to Spearphishing Link (T1192, as represented in the lab environment) connects technical indicators with adversary behavior.
6. **Validation improves investigative confidence** — independently searching recorded indicators verifies that the intelligence was successfully stored and remains available for future analysis.
7. **Documentation makes intelligence reusable** — structured analyst findings allow investigation results to support future SOC investigations, threat hunting, detection engineering, and incident response.

Together, these practices transform isolated technical artifacts into structured and reusable cyber threat intelligence.

---

## Project Status

**Investigation Complete ✅**

| Investigation Phase | Status |
|---|---|
| IOC Collection | ✅ Complete |
| MISP Classification | ✅ Complete |
| Object Modeling | ✅ Complete |
| IOC Correlation | ✅ Complete |
| MITRE ATT&CK Mapping | ✅ Complete |
| IOC Validation | ✅ Complete |
| Analyst Assessment | ✅ Complete |
| Documentation | ✅ Complete |

---

## Disclaimer

This repository was created exclusively for cybersecurity education, defensive-security training, and portfolio development.

All indicators and infrastructure represented in this project are simulated or documentation-range artifacts. No real organization, production environment, user, or malicious infrastructure was targeted.

---

## Author

**Anik Nohan**

Cybersecurity | SOC Analysis | Blue Team | Threat Intelligence
