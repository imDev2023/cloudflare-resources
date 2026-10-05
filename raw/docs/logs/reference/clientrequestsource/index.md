---
description: Understand ClientRequestSource field values in logs.
title: ClientRequestSource field
image: https://developers.cloudflare.com/logs/reference/clientrequestsource/og.png?v=62d998e4efeb04c4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# ClientRequestSource field

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/reference/clientrequestsource/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The possible values for the `ClientRequestSource` field are the following:

| Value | Request source | Description |
| --- | --- | --- |
| `0` | unknown | Should never happen. |
| `1` | eyeball | A request from an end user. If you want to count requests made the Cloudflare Edge, the query should filter on `requestSource=eyeball`. |
| `2` | purge | A request made by Cloudflare's purge system. |
| `3` | alwaysOnline | A request made by Cloudflare's Always Online crawler. |
| `4` | healthcheck | A request made by Cloudflare's Health Check system. |
| `5` | edgeWorkerFetch | A fetch request made from an edge Worker. |
| `6` | edgeWorkerCacheAPI | A cache API call made from an edge Worker. |
| `7` | edgeWorkerKV | A KV call made from an edge Worker. |
| `8` | imageResizing | Requests made by Cloudflare's Image Resizing product. |
| `9` | orangeToOrange | A request that comes from another orange clouded zone. |
| `10` | sslDetector | A request made by Cloudflare's [SSL Detector system ↗︎](https://blog.cloudflare.com/ssl-tls-recommender/). |
| `11` | earlyHintsCache | An [Early Hint request ↗︎](https://blog.cloudflare.com/early-hints/). |
| `12` | inBrowserChallenge | An end user request caused by a Cloudflare security product (Challenges, JavaScript Detections). These requests never reach the origin. |
