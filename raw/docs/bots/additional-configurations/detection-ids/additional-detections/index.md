---
description: Detection IDs for residential proxy traffic and other automated signals.
title: Additional detections
image: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/og.png?v=4830d6171dd453e1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Additional detections

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare bot detection includes additional signals to catch different kinds of automated traffic.

Bot management customers automatically benefit from the residential proxy detection improvement below, which lowers the [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) for matched requests. Using the detection ID in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) provides even more visibility and control over mitigating residential proxy traffic.

| Detection ID | Description |
| --- | --- |
| `50331651` | Observes traffic from residential proxy networks and similar commercial proxies. <br><br>When the ID matches a request, Bot Management sets the bot score to 29 and uses [anomaly detection](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/#anomaly-detection-enterprise) as its score source. |
