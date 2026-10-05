---
description: Troubleshoot HTTP 415 error responses.
title: Error 415
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/og.png?v=b449da8a535b091a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 415

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 415 Unsupported Media Type

The `415 Unsupported Media Type` status code indicates that the server refuses to process the request because the format of the payload is not supported. One way to identify and fix this issue would be to look at the `Content-Type` or `Content-Encoding` headers sent in the client's request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.16).

### Common use cases

This may be triggered by submitting a file type or format that the server is not configured to handle, such as uploading an unsupported image or document format, may also trigger this error.

### Cloudflare-specific information

Cloudflare typically passes this response from the origin server if it encounters an unsupported media type in the client's request payload.
