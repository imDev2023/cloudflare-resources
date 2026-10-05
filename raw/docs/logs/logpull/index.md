---
description: Pull request logs via the Logpull REST API.
title: Logpull
image: https://developers.cloudflare.com/logs/logpull/og.png?v=cd522fed058f576e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Logpull

Last updated Aug 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpull/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpull is a REST API for consuming request logs over HTTP. These logs contain data related to the connecting client, the request path through the Cloudflare network, and the response from the origin web server. This data is useful for enriching existing logs on an origin server. Logpull is available to customers on the Enterprise plan.

Caution

Logpull is considered a legacy feature and we recommend using [Logpush](https://developers.cloudflare.com/logs/logpush/) or [Logs Engine](https://developers.cloudflare.com/logs/r2-log-retrieval/) instead for better performance and functionality.

Review the following content to learn more about Logpull.

- [Understanding the basics](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/)
- [Enabling log retention](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/)
- [Requesting logs](https://developers.cloudflare.com/logs/logpull/requesting-logs/)
- [Additional details](https://developers.cloudflare.com/logs/logpull/additional-details/)

## Availability

|  | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Availability | No | No | No | Yes |

### Limitation

Logpull is unavailable when the Customer Metadata Boundary (CMB) is set outside the US region. Specifically, it does not work when CMB is restricted to the EU-only setting. For more details, refer to the [Cloudflare Data Localization](https://developers.cloudflare.com/data-localization/) documentation.
