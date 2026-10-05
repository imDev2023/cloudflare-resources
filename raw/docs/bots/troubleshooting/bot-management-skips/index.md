---
description: Understand why Bot Management does not score certain requests.
title: Bot Management skips
image: https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/og.png?v=bed86772ba84c636
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Bot Management skips

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

There are instances in which Bot Management does not run and certain fields, such as the [JA3/JA4 field](https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/), are not populated because it has been determined that running Bot Management would not be necessary.

Refer to [bot scores](https://developers.cloudflare.com/bots/concepts/bot-score/#not-computed) for more information about why a request is not scored.

## Common reasons for Bot Management to not score a request

### Requests to internal endpoints

Requests such as `/cdn-cgi/` are handled individually and will never receive a Bot Management score. Email Obfuscation, Web Analytics, Trace Requests, Challenge Pages, and JavaScript Detections do not receive bot scores. Refer to the table below for some examples of internal endpoints.

| Route |
| --- |
| `/cdn-cgi/rum` |
| `/cdn-cgi/script_monitor/report` |
| `/cdn-cgi/trace` |
| `/cdn-cgi/challenge-platform/…` |
| `/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js` |

### Purge requests

All HTTP purge requests will not receive a bot score.

### Early hints cache requests

Early hints cache requests will not receive a bot score.
