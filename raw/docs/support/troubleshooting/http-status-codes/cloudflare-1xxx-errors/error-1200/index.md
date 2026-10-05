---
description: Troubleshoot Cloudflare 1200 error code.
title: Error 1200
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1200/og.png?v=7e6f878087963051
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1200

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1200/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1200: Cache connection limit

This error indicates that the number of requests queued on Cloudflare's edge exceeds the limit.

### Common cause

There are too many requests queued on Cloudflare's edge that are awaiting process by your origin web server. This limit protects Cloudflare's systems.

### Resolution

Tune your origin webserver to accept incoming connections faster. Adjust your caching settings to improve cache-hit rates so that fewer requests reach your origin web server. Reach out to your hosting provider or web administrator for assistance.
