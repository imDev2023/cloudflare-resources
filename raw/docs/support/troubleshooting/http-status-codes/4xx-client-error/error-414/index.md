---
description: Troubleshoot HTTP 414 error responses.
title: Error 414
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/og.png?v=6d470e9710031225
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 414

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 414 URI Too Long

The `414 URI Too Long` status code indicates that the server refuses to process the request because the URI provided by the client is excessively long.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.15).

### Common use cases

For example, if a client is attempting a `GET` request with an unusually long URI, such as one containing an excessive number of query parameters, after a `POST`, this could be seen as a security risk and a `414` is generated.

### Cloudflare-specific information

Cloudflare will generate a `414` response if the URI length exceeds 32KB.
