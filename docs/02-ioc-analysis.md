# 02 — IOC Analysis

## Overview

The phishing investigation produced multiple indicators of compromise (IOCs) representing network infrastructure, a credential-harvesting endpoint, and a file-based artifact.

Rather than treating each indicator independently, the indicators were analyzed as components of a common simulated phishing scenario and documented within MISP for correlation and threat-intelligence analysis.

---

## IOC Summary

| IOC Type | Indicator | MISP Type | Assessment |
|---|---|---|---|
| Domain | `secure-login-support.com` | `domain` | Simulated phishing infrastructure |
| Destination IP | `198.51.100.23` | `ip-dst` | Documentation-range infrastructure |
| URL | `http://secure-login-support.com/account/verify` | `url` | Simulated credential-harvesting endpoint |
| File Hash | `275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f` | `sha256` | Simulated malicious attachment indicator |

> **Safety Note:** These indicators were created or selected for defensive lab use. They should not be interpreted as evidence of active malicious infrastructure.

---

## 1. Domain Analysis

### Indicator

`secure-login-support.com`

### MISP Classification

- Category: `Network activity`
- Type: `domain`
- Correlation: Enabled

### Analyst Assessment

The domain represents the primary simulated phishing infrastructure in this investigation.

Its naming convention is consistent with a social-engineering scenario designed to resemble an account-security or authentication service. Within this lab, the domain serves as the infrastructure component connecting the phishing URL to the associated destination IP.

A MISP attribute search was performed to verify that the domain had been recorded and was available for correlation.

### Evidence

![MISP domain IOC search results](../evidence/screenshots/misp-ioc-domain-search-results.png)

**Figure 1 — Domain IOC validation in MISP.**  
The search confirms that `secure-login-support.com` is stored as a network-activity domain attribute within the investigation.

---

## 2. Destination IP Analysis

### Indicator

`198.51.100.23`

### MISP Classification

- Category: `Network activity`
- Type: `ip-dst`
- Correlation: Enabled

### Analyst Assessment

The destination IP was modeled as infrastructure associated with the simulated phishing domain.

The address belongs to the `198.51.100.0/24` documentation range and is used here intentionally to avoid associating the lab with live infrastructure.

The domain and destination IP were additionally modeled through a MISP `domain-ip` object to represent their analytical relationship.

A MISP search was performed to verify the IP attribute and confirm its presence within the event.

### Evidence

![MISP destination IP IOC search results](../evidence/screenshots/misp-ioc-ip-search-results.png)

**Figure 2 — Destination IP IOC validation in MISP.**  
The search confirms the `198.51.100.23` destination-IP indicator recorded during the simulated investigation.

---

## 3. URL Analysis

### Indicator

`http://secure-login-support.com/account/verify`

### MISP Classification

- Category: `Network activity`
- Type: `url`
- Correlation: Enabled

### Analyst Assessment

The URL represents the simulated credential-harvesting endpoint associated with the phishing scenario.

The `/account/verify` path was used to model a common phishing workflow in which a victim is directed to an account-verification page designed to solicit credentials.

The URL was recorded separately from the domain so that analysts could search, correlate, and operationalize the complete network indicator when performing threat hunting or defensive analysis.

### Evidence

![MISP URL IOC search results](../evidence/screenshots/misp-ioc-url-search-results.png)

**Figure 3 — URL IOC validation in MISP.**  
The search verifies that the complete simulated credential-harvesting URL was recorded as a network-activity indicator.

---

## 4. SHA-256 Analysis

### Indicator

`275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f`

### MISP Classification

- Category: `Payload delivery`
- Type: `sha256`
- Correlation: Enabled

### Analyst Assessment

The SHA-256 value represents a simulated malicious attachment associated with the phishing investigation.

Cryptographic hashes provide analysts with a stable method of identifying known file artifacts without relying solely on filenames, which attackers can easily modify.

Within this lab, the hash demonstrates how file-based indicators can be documented alongside network indicators to provide broader investigative context.

### Evidence

![MISP SHA-256 IOC search results](../evidence/screenshots/misp-ioc-sha256-search-results.png)

**Figure 4 — SHA-256 IOC validation in MISP.**  
The MISP search confirms that the simulated file hash is stored as a payload-delivery indicator.

---

## IOC Relationship

The indicators collectively represent the following analytical chain:

```text
Phishing Activity
       |
       +--> secure-login-support.com
       |           |
       |           +--> 198.51.100.23
       |
       +--> /account/verify
       |
       +--> SHA-256 file indicator
