---
description: Troubleshoot HTTP 417 error responses.
title: Error 417
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/og.png?v=f6f4378f7c5335dc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 417

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 417 Expectation Failed

The `417 Expectation Failed` status code indicates that the server could not meet the requirements specified in the `Expect` header of the client's request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.18).

### Common use cases

Some clients use the `Expect` header, such as `Expect: 100-continue`, to verify if the server is ready to receive a large payload, and if the server cannot fulfill this expectation, it returns a 417 response. Similarly, a server may reject a request with this error if the client includes an `Expect` header with unsupported or invalid values.

### Cloudflare-specific information

Cloudflare typically forwards this response from the origin server if it encounters an issue related to unsupported or unfulfilled `Expect` headers in the client's request.
