# MISP Phishing Threat Intelligence Investigation

## Overview

This project demonstrates a simulated Security Operations Center (SOC) threat intelligence investigation using **MISP (Malware Information Sharing Platform)**.

The investigation focuses on suspicious phishing infrastructure associated with a simulated credential-harvesting campaign. Indicators of Compromise (IOCs) were documented, structured, correlated, mapped to MITRE ATT&CK, and validated using MISP.

The objective was to demonstrate how a SOC analyst can transform raw indicators into structured and searchable threat intelligence that can support detection, correlation, threat hunting, and incident response.

> **Lab Safety Notice**
>
> All indicators used in this project are simulated or documentation-range values created for educational purposes. They should not be interpreted as active malicious infrastructure.

---

## Investigation Scenario

A SOC investigation identified infrastructure associated with a simulated phishing campaign designed to direct a victim to a credential-harvesting page.

The investigation identified several artifacts requiring threat-intelligence documentation:

- Suspicious domain
- Destination IP address
- Credential-harvesting URL
- SHA-256 attachment hash

These indicators were entered into MISP and correlated within a structured investigation event.

---

## Investigation Objectives

The objectives of this lab were to:

- Create and manage a MISP investigation event
- Document Indicators of Compromise
- Categorize indicators using appropriate MISP attribute types
- Enable IOC correlation
- Model relationships between infrastructure indicators
- Map observed behavior to MITRE ATT&CK
- Validate indicators using MISP search functionality
- Produce analyst-ready threat intelligence documentation

---

## Lab Environment

| Component | Purpose |
|---|---|
| MISP | Threat intelligence and IOC management |
| Web Browser | MISP administration and investigation |
| MITRE ATT&CK | Adversary behavior classification |
| Isolated Lab Environment | Safe investigation environment |

---

## Indicators of Compromise

| Indicator | Type | MISP Category | Purpose |
|---|---|---|---|
| `secure-login-support.com` | Domain | Network activity | Simulated phishing infrastructure |
| `198.51.100.23` | Destination IP | Network activity | Documentation-range destination address |
| `http://secure-login-support.com/account/verify` | URL | Network activity | Simulated credential-harvesting URL |
| `275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f` | SHA-256 | Payload delivery | Simulated malicious attachment hash |

The IP address `198.51.100.23` belongs to the TEST-NET-2 documentation range and is used here strictly for laboratory purposes.

---

## Investigation Workflow

```text
Suspicious Phishing Activity
          │
          ▼
   Artifact Collection
          │
          ▼
   IOC Identification
          │
          ├── Domain
          ├── Destination IP
          ├── URL
          └── SHA-256
          │
          ▼
      MISP Event
          │
          ▼
   IOC Classification
          │
          ▼
 Domain ↔ IP Relationship
          │
          ▼
 MITRE ATT&CK Mapping
          │
          ▼
 Correlation + IOC Search
          │
          ▼
 Investigation Completed
```

---

# 1. MISP Event Creation

A dedicated MISP event was created to document the investigation.

**Event Name**

`SOC Investigation - Suspicious Phishing Infrastructure`

The event provides a centralized intelligence record containing the indicators, relationships, ATT&CK mapping, and analyst context associated with the investigation.

![MISP Event](evidence/screenshots/01-event-creation.png)

---

# 2. IOC Collection and Classification

Four primary indicators were identified and entered into MISP.

### Domain

```text
secure-login-support.com
```

MISP classification:

```text
Category: Network activity
Type: domain
```

The domain represents the simulated phishing infrastructure.

![Domain IOC](evidence/screenshots/02-domain-ioc.png)

### Destination IP

```text
198.51.100.23
```

MISP classification:

```text
Category: Network activity
Type: ip-dst
```

The address is part of a documentation range and represents the simulated destination infrastructure.

![IP IOC](evidence/screenshots/03-ip-ioc.png)

### Credential-Harvesting URL

```text
http://secure-login-support.com/account/verify
```

MISP classification:

```text
Category: Network activity
Type: url
```

The URL represents the simulated phishing landing page associated with the investigation.

![URL IOC](evidence/screenshots/04-url-ioc.png)

### Attachment Hash

```text
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

MISP classification:

```text
Category: Payload delivery
Type: sha256
```

The hash represents a simulated malicious attachment associated with the phishing scenario.

![SHA-256 IOC](evidence/screenshots/05-sha256-ioc.png)

---

# 3. IOC Correlation

Correlation was enabled for the investigation indicators.

Correlation allows MISP to identify instances where the same indicator appears across other events or intelligence records.

From a SOC perspective, this capability can help analysts identify:

- Reused infrastructure
- Recurring phishing campaigns
- Shared malicious indicators
- Connections between investigations
- Potential campaign relationships

---

# 4. Infrastructure Relationship Modeling

Instead of treating the domain and destination IP as completely independent indicators, a MISP `domain-ip` object was created.

Relationship:

```text
secure-login-support.com
        │
        ▼
198.51.100.23
```

This models the relationship between the suspicious domain and its associated simulated destination infrastructure.

![Domain-IP Object](evidence/screenshots/07-domain-ip-object.png)

Using structured MISP objects improves the intelligence model because related artifacts can be represented together rather than only as isolated attributes.

---

# 5. MITRE ATT&CK Mapping

The phishing activity was mapped to the ATT&CK entry available in the lab's MISP galaxy:

```text
Spearphishing Link - T1192
```

![MITRE ATT&CK Mapping](evidence/screenshots/06-attack-mapping.png)

This associates the threat intelligence with the adversary behavior represented by the phishing link.

> **Version note:** The MISP galaxy used in this lab displays the legacy ATT&CK identifier `T1192`. Current ATT&CK versions represent spearphishing links under the Phishing technique as `T1566.002`.

This distinction is documented to preserve the evidence exactly as displayed by the lab environment while recognizing the current ATT&CK taxonomy.

---

# 6. IOC Validation

After documenting the indicators, MISP search functionality was used to verify that each IOC was successfully indexed and retrievable.

### Domain Validation

The suspicious domain was searched within MISP and returned the corresponding investigation records.

![Domain Search](evidence/screenshots/09-domain-search-validation.png)

### IP Validation

The destination IP was successfully retrieved through MISP IOC search.

![IP Search](evidence/screenshots/10-ip-search-validation.png)

### SHA-256 Validation

The simulated attachment hash returned the expected investigation record.

![SHA256 Search](evidence/screenshots/11-sha256-search-validation.png)

### URL Validation

The credential-harvesting URL returned the associated network activity attribute.

![URL Search](evidence/screenshots/12-url-search-validation.png)

This confirmed that the indicators were available for future intelligence searches and correlation.

---

# 7. Investigation Completion

After IOC documentation, object creation, ATT&CK mapping, correlation, and validation were completed, the MISP event analysis state was changed to:

```text
Completed
```

![Completed Investigation](evidence/screenshots/08-completed-investigation.png)

This represents the closure of the intelligence documentation phase of the investigation.

---

# Analyst Assessment

The collected indicators support a simulated phishing scenario involving a credential-harvesting URL and associated network infrastructure.

The investigation established relationships between:

```text
Phishing Technique
        │
        ▼
Credential-Harvesting URL
        │
        ▼
Suspicious Domain
        │
        ▼
Destination IP
```

A simulated malicious attachment hash was also documented as a payload-delivery indicator associated with the investigation.

Structuring these artifacts in MISP makes them available for correlation, intelligence searches, detection engineering, threat hunting, and future incident investigations.

---

# SOC Relevance

This lab demonstrates practical skills relevant to SOC and threat intelligence operations, including:

- Indicator of Compromise management
- Threat intelligence documentation
- MISP event management
- Indicator classification
- Infrastructure analysis
- IOC correlation
- MISP object modeling
- MITRE ATT&CK mapping
- Threat intelligence validation
- Phishing investigation
- Analyst documentation

---

# Key Takeaways

This investigation demonstrated that effective threat intelligence involves more than collecting indicators.

Raw artifacts become more useful when they are:

1. Correctly classified
2. Given investigative context
3. Correlated with related indicators
4. Structured into meaningful relationships
5. Mapped to adversary behavior
6. Made searchable for future investigations

MISP provides a structured mechanism for transforming investigation artifacts into reusable threat intelligence.

---

# Disclaimer

This project was created exclusively for cybersecurity education and defensive security portfolio development.

The infrastructure, indicators, and investigation scenario are simulated. Documentation-range addressing and controlled lab artifacts were intentionally used to avoid interaction with real malicious infrastructure.

No real organization, user, or production system was targeted.

---

## Author

**Anik Nohan**

Cybersecurity | SOC Analysis | Blue Team | Threat Intelligence
