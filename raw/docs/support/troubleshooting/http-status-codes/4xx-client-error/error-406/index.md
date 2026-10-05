---
description: Troubleshoot HTTP 406 error responses.
title: Error 406
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-406/og.png?v=903bf554b5b947c7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 406

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-406/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 406 Not Acceptable

The `406 Not Acceptable` status code indicates that the requested resource is not available in a format that adheres to the content negotiation headers specified by the client (for example, `Accept-Charset` or `Accept-Language`).

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.7).

### Common use cases

For example, if a client requests content in a specific language or character set that the server does not support, this error will be generated. To avoid returning a `406` error, the server can instead serve the less preferred method to the client's User-Agent, rather than rejecting the request.

### Cloudflare-specific information

Cloudflare does not generate `406` errors directly but can proxy these responses from the origin server. If content negotiation issues occur, they are typically related to configurations at the origin server, such as language or character set settings.
