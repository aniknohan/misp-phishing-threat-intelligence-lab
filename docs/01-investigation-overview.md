# 01 — Investigation Overview

## Executive Summary

This project documents a simulated phishing threat-intelligence investigation conducted in MISP (Malware Information Sharing Platform).

The investigation models a credential-harvesting phishing scenario in which multiple indicators of compromise (IOCs) were collected, structured, correlated, and mapped to the MITRE ATT&CK framework.

The primary objective was to demonstrate how a SOC or Cyber Threat Intelligence (CTI) analyst can transform isolated technical indicators into structured and actionable threat intelligence.

> **Lab Safety Notice:** All indicators used in this project are simulated or documentation-range artifacts created exclusively for defensive cybersecurity training. No live malicious infrastructure was used.

---

## Investigation Scenario

A simulated phishing investigation identified infrastructure consistent with a credential-harvesting campaign.

The investigation focused on four primary indicators:

| Indicator Type | Value | Analytical Purpose |
|---|---|---|
| Domain | `secure-login-support.com` | Simulated phishing infrastructure |
| Destination IP | `198.51.100.23` | Documentation-range infrastructure address |
| URL | `http://secure-login-support.com/account/verify` | Simulated credential-harvesting endpoint |
| SHA-256 | `275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f` | Simulated malicious attachment indicator |

These indicators were entered into MISP and analyzed as components of the same phishing investigation.

---

## Investigation Objectives

The investigation was designed to demonstrate the following analyst capabilities:

- Create and manage a structured MISP event.
- Record network and file-based indicators of compromise.
- Model relationships between a domain and IP address using a MISP object.
- Enable correlation for relevant indicators.
- Search MISP for existing IOC occurrences.
- Validate individual domain, IP, URL, and SHA-256 indicators.
- Associate phishing activity with MITRE ATT&CK.
- Interpret relationships between indicators rather than treating each IOC independently.
- Document analyst findings in a reproducible investigation workflow.

---

## Investigation Workflow

The investigation followed this process:

1. Create a dedicated MISP event for the simulated phishing investigation.
2. Add the suspicious domain, destination IP address, phishing URL, and SHA-256 hash.
3. Configure the indicators for correlation where appropriate.
4. Create a `domain-ip` MISP object to represent the relationship between the domain and infrastructure IP.
5. Associate the event with the Enterprise ATT&CK phishing technique.
6. Search individual IOC values to validate their presence and relationships within MISP.
7. Review the resulting correlation information.
8. Document the findings and analyst assessment.

---

## Threat Intelligence Model

The investigation models the following relationship:

```text
Simulated Phishing Campaign
        |
        +-- Domain
        |     secure-login-support.com
        |
        +-- Destination IP
        |     198.51.100.23
        |
        +-- Credential-Harvesting URL
        |     http://secure-login-support.com/account/verify
        |
        +-- File Indicator
        |     SHA-256
        |     275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
        |
        +-- ATT&CK Mapping
              Spearphishing Link
