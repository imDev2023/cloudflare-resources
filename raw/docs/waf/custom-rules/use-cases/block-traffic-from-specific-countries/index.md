---
description: Block traffic from specific countries with a custom rule.
title: Block traffic from specific countries
image: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/og.png?v=46cfeba865d34afb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Block traffic from specific countries

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests based on country code using the [`ip.src.country`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/) field.

- **When incoming requests match**:

  | Field | Operator | Value |
  | --- | --- | --- |
  | Country | is in | `Korea, North` |

  If you are using the expression editor:  
  `(ip.src.country in {"KP"})`
- **Then take action**: *Block*

## Other resources

- [Use case: Block traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/)
- [Use case: Allow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)
