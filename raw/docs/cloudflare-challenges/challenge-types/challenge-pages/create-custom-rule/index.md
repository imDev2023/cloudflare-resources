---
description: Create WAF custom rules that issue challenge pages based on bot scores or rate limits.
title: Implement a Challenge Page via WAF custom rules
image: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/create-custom-rule/og.png?v=aceb2d843fb69d93
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-challenges/llms.txt  
> Use this file to discover all available pages before exploring further.

# Implement a Challenge Page via WAF custom rules

Last updated May 6, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/create-custom-rule/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can implement a Challenge Page to your website or application by creating a [WAF custom rule](https://developers.cloudflare.com/waf/custom-rules/).

Challenges are triggered by a rule in the [Web Application Firewall (WAF)](https://developers.cloudflare.com/waf/), [Bot Management](https://developers.cloudflare.com/bots/), or [Rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/).

- **Bot Management**: Challenge visitors that appear automated based on their [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) or a specific [detection ID](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/).
- **Rate limiting**: Challenge visitors who exceed your configured [rate limits](https://developers.cloudflare.com/waf/rate-limiting-rules/).
