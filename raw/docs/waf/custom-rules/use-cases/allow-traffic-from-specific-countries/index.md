---
description: Allow traffic only from specific countries.
title: Allow traffic from specific countries only
image: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/og.png?v=fe155ea220236639
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Allow traffic from specific countries only

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests based on country code using the [`ip.src.country`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/) field, only allowing requests from two countries: United States and Mexico.

- **When incoming requests match**:

  | Field | Operator | Value |
  | --- | --- | --- |
  | Country | is not in | `Mexico`, `United States` |

  If you are using the expression editor:  
  `(not ip.src.country in {"US" "MX"})`
- **Then take action**: *Block*

## Other resources

- [Use case: Block traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)
- [Use case: Block traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/)
