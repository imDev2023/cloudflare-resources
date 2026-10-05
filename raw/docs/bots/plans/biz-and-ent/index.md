---
description: Bot protection features included in the Business and Enterprise plans.
title: Business
image: https://developers.cloudflare.com/bots/plans/biz-and-ent/og.png?v=be5d5ff486498427
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Business

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/plans/biz-and-ent/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To learn more about features and functionality, select a plan.

[Free](https://developers.cloudflare.com/bots/plans/free/) [Pro](https://developers.cloudflare.com/bots/plans/pro/) [Business](https://developers.cloudflare.com/bots/plans/biz-and-ent/) [Bot Management for Enterprise](https://developers.cloudflare.com/bots/plans/bm-subscription/)

|  | |
| --- | --- |
| **Plan name** | Super Bot Fight Mode |
| **Availability** | All Business customers and Enterprise customers without Bot Management<sup>[1](#user-content-fn-1)</sup> |
| **Type of bots detected** | Simple bots, headless browsers, and many sophisticated bots |
| **Actions** | Customer chooses whether to allow, block, or challenge |
| **Analytics** | Dedicated Bot Analytics tool, available in **Security Analytics** |
| **Control** | Applied to all traffic across a domain |
| **Additional features** | [Block AI bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), <br> [AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), <br> [Instruct AI bot traffic with `robots.txt`](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/), <br> [Definitely and Likely automated bots](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings), <br> [Verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/), <br> [Static resource protection](https://developers.cloudflare.com/bots/additional-configurations/static-resources/), <br> [Optimize for WordPress](https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/), <br> [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/) |

## Bot settings versus custom rules

The following features are handled automatically in **Security Settings** and do not require custom rules:

| Feature | Handled by bot settings | Requires custom rules |
| --- | --- | --- |
| Block or challenge definitely automated traffic | Yes | Only for path-specific or threshold-tuned rules |
| Block or challenge likely automated traffic | Not available on Pro | Yes, with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) |
| Allow or block verified bots | Yes | No |
| Block AI crawlers | Yes | Only to target individual AI crawlers |
| Protect static resources | Yes | No |
| Optimize for WordPress | Yes | No |

For more details on when custom rules are needed, refer to [custom rules](https://developers.cloudflare.com/bots/additional-configurations/custom-rules/).

## How do I get started?

To get started, review our [setup guides](https://developers.cloudflare.com/bots/get-started/). If you have any questions, visit the [community ↗︎](https://community.cloudflare.com/) to engage with other Cloudflare users.

## Footnotes

1. When users purchase Bot Management for Enterprise, Cloudflare automatically replaces and disables other bot products to prevent overlap. [↩](#user-content-fnref-1)
