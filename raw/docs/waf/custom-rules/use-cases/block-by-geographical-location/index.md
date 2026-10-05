---
description: Block traffic based on geographic location.
title: Block traffic by geographical location
image: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/og.png?v=f612818530d01734
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Block traffic by geographical location

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests by autonomous system number (ASN), continent, or country of origin.

- **When incoming requests match**:

  | Field | Operator | Value | Logic |
  | --- | --- | --- | --- |
  | AS Num | equals | `131279` | Or |
  | Continent | equals | `Asia` | Or |
  | Country | equals | `Korea, North` |  |

  If you are using the expression editor:  
  `(ip.src.asnum eq 131279) or (ip.src.continent eq "AS") or (ip.src.country eq "KP")`
- **Then take action**: *Block*

## Other resources

- [Use case: Block traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/)
- [Use case: Allow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)
- [Fields reference: Geolocation](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/?field-category=Geolocation)
