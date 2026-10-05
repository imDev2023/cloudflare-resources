---
description: How Cloudflare sets Host headers and SNI when forwarding connections to your origin.
title: Connection request details
image: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/og.png?v=d72a5f7abe38a2c6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-for-platforms/llms.txt  
> Use this file to discover all available pages before exploring further.

# Connection request details

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When forwarding connections to your origin server, Cloudflare will set request parameters according to the following:

## Host header

Cloudflare will not alter the Host header by default, and will forward exactly as sent by the client. If you wish to change the value of the Host header you can utilise [Page-Rules](https://developers.cloudflare.com/workers/configuration/workers-with-page-rules/) or [Workers](https://developers.cloudflare.com/workers/) using the steps outlined in [certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/).

## SNI

When establishing a TLS connection to your origin server, if the request is being sent to your configured Fallback Host then the value of the SNI sent by Cloudflare will match the value of the Host header sent by the client (i.e. the custom hostname).

If however the request is being forwarded to a Custom Origin, then the value of the SNI will be that of the Custom Origin.
