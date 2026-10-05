---
description: Troubleshoot Cloudflare 1037 error code.
title: Error 1037
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/og.png?v=1882b3982ca618d7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1037

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1037: Invalid rewrite rule (failed to evaluate expression)

This error indicates that the rewrite rule expression could not be evaluated.

### Common cause

There are several causes for this error, but it can mean that one expression element contained an undefined value when it was evaluated.

For example, you get a 1037 error when using the following URL rewrite dynamic expression and the `X-Source` header is not included in the request:

`http.request.headers["x-source"][0]`

### Resolution

Make sure that all the elements of your rewrite expression are defined. For example, if you are referring to a header value, ensure the header is set.
