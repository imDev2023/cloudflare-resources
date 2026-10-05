---
description: Troubleshoot HTTP 412 error responses.
title: Error 412
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/og.png?v=2d7a1b90b6b87c95
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 412

Last updated Sep 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## 412 Precondition Failed

The `412 Precondition Failed` status code indicates that the server denies the request because the resource does not meet the conditions specified by the client.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.13).

### Common use cases

One common use case for the `412 Precondition Failed` status code is version control. For example, a client modifying an existing resource may set the `If-Unmodified-Since` header to ensure the resource has not been changed since the client downloaded it for editing. If another client edits the resource after the specified date but before the original client uploads their changes, the server will return a `412` response to prevent overwriting the newer updates.

### Cloudflare-specific information

Cloudflare may serve this response: for more information please refer to [ETag Headers](https://developers.cloudflare.com/cache/reference/etag-headers/).
