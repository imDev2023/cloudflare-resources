---
description: Troubleshoot HTTP 409 error responses.
title: Error 409
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/og.png?v=065990829e22861f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 409

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 409 Conflict

The `409 Conflict` status code indicates that the request could not be completed due to a conflict with the current state of the target resource.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.10).

### Common use cases

This error typically happens with a `PUT` request when multiple clients are attempting to edit the same resource. To solve this issue:

- The server should generate a payload that includes enough information for the client to recognize the source of the conflict.
- Clients should retry the request again after resolving the conflict.

### Cloudflare-specific information

Cloudflare will return a 409 response for a [Error 1001: DNS Resolution Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/).
