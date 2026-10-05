---
description: In HTTP request logs, cacheResponseBytes reflects the uncompressed response size from cache or origin. edgeResponseBytes reflects the final compressed response size sent to the client. Because Cloudflare applies compression (gzip, Brotli) before delivering to the client, edgeResponseBytes is typically smaller than cacheResponseBytes.
title: edgeResponseBytes and cacheResponseBytes discrepancy
image: https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/og.png?v=7cfd5e1933c19659
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# edgeResponseBytes and cacheResponseBytes discrepancy

Last updated Jun 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [HTTP request logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/), `cacheResponseBytes` reflects the uncompressed response size from cache or origin. `edgeResponseBytes` reflects the final compressed response size sent to the client. Because Cloudflare applies compression (gzip, Brotli) before delivering to the client, `edgeResponseBytes` is typically smaller than `cacheResponseBytes`.
