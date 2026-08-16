# MISP Threat Correlation Analysis

## Overview

This phase of the investigation expands the analysis from individual indicators of compromise (IOCs) into broader threat-intelligence correlation using MISP.

The objective was to determine whether the Locky ransomware indicators identified during the investigation were connected to additional MISP events, infrastructure, campaigns, or threat-intelligence records.

The workflow included:

- Searching MISP for Locky-related intelligence
- Reviewing ransomware-related tags and attributes
- Pivoting between events and indicators
- Investigating related Locky campaigns
- Visualizing relationships using correlation graphs
- Reviewing related domains, URLs, IP addresses, and registry artifacts
- Exporting threat intelligence for IDS/SIEM integration
- Examining MISP REST API capabilities

---

## 1. Locky Intelligence Search

MISP's **Search Attributes** functionality was used to search the threat-intelligence database for references to Locky.

A wildcard search was performed using:

`%Locky%`

This allowed MISP to identify attributes containing the term within stored intelligence.

The search returned multiple records associated with Locky ransomware, including external-analysis reports, malicious infrastructure, registry artifacts, URLs, and other campaign information.

This demonstrates how analysts can move beyond a single phishing event and identify historical intelligence related to the same malware family.

![Locky attribute search results](../evidence/screenshots/12-locky-attribute-search.png)

---

## 2. Ransomware Tag-Based Investigation

MISP taxonomy tags were also used to identify indicators associated with ransomware.

The ransomware classification provided a way to pivot from the original Locky event into other events and attributes classified under the same malware category.

The search exposed multiple malicious domains associated with ransomware activity.

This type of taxonomy-based pivoting is useful because an analyst does not need to know every IOC beforehand. Threat classifications can be used to discover related infrastructure already present in the intelligence platform.

![Ransomware tagged attributes](../evidence/screenshots/13-ransomware-tagged-domains.png)

---

## 3. Pivoting into Related Locky Events

One of the identified related events was:

**Malspam 2016-06-23 (Locky)**

The event contained a substantially larger collection of intelligence than the initial OSINT record, including network indicators and connections to additional events.

Examples of observable types present in the event included:

- IP addresses
- Domains
- URLs
- Hostnames
- User-Agent information
- Registry-related artifacts

MISP also displayed multiple **Related Events**, demonstrating that the event shared indicators with other intelligence records.

This represents an important CTI workflow:

**IOC → MISP Event → Shared Indicator → Related Event → Additional Infrastructure**

![Related Locky event](../evidence/screenshots/17-related-locky-event.png)

---

## 4. Correlation Graph Analysis

The MISP correlation graph was used to visualize relationships between the Locky event, its attributes, and other related events.

Instead of reviewing indicators individually, the graph provides a visual representation of how threat intelligence overlaps across campaigns.

The graph displayed the investigated Locky event near the center with numerous connected attributes and related malspam events.

This visualization helps identify:

- Shared infrastructure
- Reused indicators
- Related malware campaigns
- Common domains and IP addresses
- Connections between historical threat events

Correlation graphs are especially valuable when investigating campaigns containing large numbers of indicators because relationships that may be difficult to identify in tabular data become visually apparent.

![Locky correlation graph](../evidence/screenshots/18-locky-correlation-graph.png)

---

## 5. Threat Intelligence Export

MISP provides several export formats that allow threat intelligence to be consumed by other defensive technologies.

Available formats observed during the investigation included:

- MISP XML
- MISP JSON
- OpenIOC
- CSV
- STIX XML
- STIX JSON
- STIX2
- RPZ
- Suricata rules
- Snort rules
- Bro/Zeek rules
- Plain-text attribute exports

This capability demonstrates how threat intelligence stored in MISP can move from analysis into operational detection.

![MISP export formats](../evidence/screenshots/19-misp-export-options.png)

---

## 6. Suricata Detection Rule Export

The Locky event was exported using MISP's **Suricata rules** functionality.

The resulting rule set contained network detection signatures generated from indicators stored within the event.

The exported rules included detections for observable types such as:

- Malicious IP addresses
- Domains
- Hostnames
- HTTP URLs

Example rule logic followed the general structure:

`alert → network indicator → matching IOC → generate security alert`

This demonstrates the operational value of structured threat intelligence. Indicators discovered during CTI analysis can be converted into detection content for network intrusion detection systems.

![Suricata rules generated from MISP](../evidence/screenshots/20-suricata-rule-export.png)

---

## 7. MISP REST API Investigation

MISP also exposes threat intelligence through its REST API.

The investigation reviewed MISP's `restSearch` functionality, which allows analysts and security tools to retrieve events and attributes programmatically.

The interface documented search parameters including:

- `returnFormat`
- `limit`
- `value`
- `type`
- `category`
- `tags`
- `eventid`
- `from`
- `to`
- `published`
- `to_ids`

This provides the foundation for automating threat-intelligence retrieval and integrating MISP with other security platforms.

![MISP REST API documentation](../evidence/screenshots/22-misp-rest-api.png)

---

## 8. JSON Event Retrieval

A MISP event was retrieved through the REST search functionality in JSON format.

The response contained structured event metadata and attributes, including fields describing:

- Event ID
- Threat level
- Distribution
- Attribute type
- Attribute category
- IOC value
- IDS status
- Comments
- Tags
- Related metadata

Structured JSON output makes MISP intelligence suitable for automated processing by scripts, SIEM platforms, SOAR systems, detection pipelines, and other security tooling.

![MISP JSON event response](../evidence/screenshots/21-misp-json-response.png)

---

## 9. Broader Threat Intelligence Discovery

Returning to the MISP event database demonstrated that the platform contains intelligence covering many campaigns and threat actors.

Events can include MITRE ATT&CK mappings, malware classifications, OSINT tags, threat-actor information, and large collections of correlated attributes.

This reinforces the value of MISP as more than an IOC repository. It can function as a central platform for organizing, enriching, correlating, and operationalizing cyber threat intelligence.

![MISP event intelligence database](../evidence/screenshots/23-misp-event-database.png)

---

## Analyst Findings

The correlation phase significantly expanded the scope of the original investigation.

The initial analysis focused on indicators associated with a specific Locky ransomware intelligence event. MISP correlation revealed that Locky-related indicators existed across multiple historical events and malspam campaigns.

The investigation demonstrated several important threat-intelligence concepts:

1. A single IOC can provide a pivot into broader campaign intelligence.
2. Shared indicators can reveal relationships between otherwise separate events.
3. Taxonomy tags provide an effective mechanism for discovering related threats.
4. Correlation graphs can expose infrastructure and campaign relationships visually.
5. Threat intelligence can be operationalized through IDS rule exports.
6. REST APIs allow CTI data to be incorporated into automated security workflows.

---

## SOC / Blue Team Relevance

From a SOC perspective, the workflow demonstrated here can support several operational activities.

Analysts can use MISP intelligence to enrich alerts, validate suspicious indicators, identify previously observed malicious infrastructure, discover related campaigns, and generate network detection rules.

A practical workflow could resemble:

**Phishing Alert → Extract IOC → Search MISP → Identify Threat Context → Pivot to Related Events → Validate Infrastructure → Map Adversary Behavior → Export Detection Intelligence**

This transforms an isolated phishing investigation into a broader threat-intelligence-driven detection process.

---

## Conclusion

The MISP correlation analysis demonstrated how individual indicators can be expanded into broader intelligence about malware campaigns and malicious infrastructure.

By combining attribute searches, taxonomy-based pivots, event correlation, visualization, structured exports, and REST API access, MISP provides analysts with a practical method for moving from isolated IOC analysis toward operational cyber threat intelligence.

The Locky investigation therefore progressed beyond simply identifying malicious indicators and demonstrated how those indicators could support correlation, threat hunting, detection engineering, and defensive security operations.
