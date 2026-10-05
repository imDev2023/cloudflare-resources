---
description: Learn about update tls versions in this guide.
title: Update TLS versions
image: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/og.png?v=86af4a83aed36c9b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Update TLS versions

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In some circumstances - specifically when an application allows client-initiated SSL/TLS renegotiation - previous versions of SSL/TLS can be more vulnerable to DDoS attacks.

When you use an SSL/TLS certificate issued by Cloudflare<sup>[1](#user-content-fn-1)</sup>, you can reduce the impact of this vulnerability by:

- Updating the [Minimum TLS Version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/) accepted by your application.
- Allowing [TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/).

## Additional resources

For more details on this vulnerability, refer to [Secure Server- and Client-Initiated SSL Renegotiation ↗︎](https://crashtest-security.com/secure-client-initiated-ssl-renegotiation/).

## Footnotes

1. Meaning either [Universal](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) or [Advanced](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) certificates. [↩](#user-content-fnref-1)
