---
description: Troubleshoot HTTP 410 error responses.
title: Error 410
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/og.png?v=6b70815ad3cc2305
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 410

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 410 Gone

When a resource is intentionally and permanently removed, servers use the `410 Gone` status code to inform clients that the resource is no longer available. In this case:

- The server suggests that links referencing the resource should be removed.
- The server is not obligated to use this status code instead of a `404` response, nor is it required to maintain this response for any specific period of time.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.11).

### Common use cases

This status is commonly applied to deprecated content, such as outdated pages or discontinued products.

### Cloudflare-specific information

Cloudflare does not generate `410` for customer websites, we only proxy the request from the origin server. If you encounter a `410` error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.
