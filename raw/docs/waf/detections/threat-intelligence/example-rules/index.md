---
description: Mitigate high-risk traffic using threat intelligence fields in WAF rules.
title: Example rules
image: https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/og.png?v=4b3ad8e9c93eb313
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Example rules

Last updated Jun 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom rule](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/) examples using [threat intelligence fields](https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/). All fields are arrays — use [`any()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#any) with `[*]`.

Caution

Test rules with *Log* before enforcing. IP-based threat intelligence is a seven-day lookback over shared infrastructure — combine with other signals such as [attack score](https://developers.cloudflare.com/waf/detections/attack-score/) before you block.

## Log matches before blocking

Deploy with *Log* (Enterprise plans) to review matches before enforcing:

- **Expression:**  
  `any(cf.intel.ip.attacker_names[*] != "")`
- **Action:** *Log*

Review matches in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/), then change the action to *Block* or *Managed Challenge*.

## Block DDoS participants targeting your region

- **Expression:**  
  `any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")`
- **Action:** *Block*

## Challenge a threat actor targeting the finance sector

- **Expression:**  
  `any(cf.intel.ip.target_industries[*] == "Banking & Financial Services") and any(cf.intel.ip.attacker_names[*] == "BLACKBASTA")`
- **Action:** *Managed Challenge*

## Filter by attacker country

- **Expression:**  
  `any(cf.intel.ip.attacker_countries[*] == "CN")`
- **Action:** *Block*

## Combine with attack score

Block requests flagged by the WAF threat intelligence dataset that also have a low [attack score](https://developers.cloudflare.com/waf/detections/attack-score/):

- **Expression:**  
  `any(cf.intel.ip.datasets[*] == "waf") and cf.waf.score lt 20`
- **Action:** *Block*

## Rate limit threat actors on API paths

[Rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/) applying a stricter rate to flagged IPs on your API:

- **Expression:**  
  `any(cf.intel.ip.datasets[*] == "ddos") and starts_with(http.request.uri.path, "/api/")`
- **Action:** *Block* when the rate is exceeded.
