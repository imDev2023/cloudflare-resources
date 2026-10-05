---
description: Troubleshoot HTTP 501 error responses.
title: Error 501
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/og.png?v=ec50883a91e3c995
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 501

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 501: not implemented

Cloudflare Workers returns a `501` error when a request uses an HTTP method that is not supported by the Workers Runtime.

### Common causes

- A client sent a request to a Workers script using a custom or non-standard HTTP method (methods outside of `GET`, `POST`, `PUT`, etc.).
- A typo in the HTTP method (for example, `POT` instead of `POST`).

### Resolution

- Update the client to use a valid, standard [HTTP request method ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).
