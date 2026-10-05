---
description: Learn more about calculating bytes served by the origin and bandwidth usage.
title: Common calculations FAQ
image: https://developers.cloudflare.com/logs/faq/common-calculations/og.png?v=492033517cc31575
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Common calculations FAQ

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/faq/common-calculations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[❮ Back to FAQ](https://developers.cloudflare.com/logs/faq/)

### How can I calculate bytes served by the origin from Cloudflare Logs?

The best way to calculate bytes served by the origin is to use the `CacheResponseBytes` field in Cloudflare Logs, and to filter only requests that come from the origin. Make sure to filter out `OriginResponseStatus` values `0` and `304`, which indicate a revalidated response.

### How do I calculate bandwidth usage for my zone?

Bandwidth (or data transfer) can be calculated by adding the `EdgeResponseBytes` field in HTTP request logs. There are some types of requests that are not factored into bandwidth calculations. In order to only include relevant requests in calculations, add the filter `ClientRequestSource = 'eyeball'`.
