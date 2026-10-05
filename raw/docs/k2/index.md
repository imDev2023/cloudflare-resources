---
description: Serverless durable logs
title: K2
image: https://developers.cloudflare.com/k2/og.png?v=9d8a9f5bbb2b5535
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/k2/llms.txt  
> Use this file to discover all available pages before exploring further.

# K2

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/k2/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Decouple event producers and consumers with a durable log

Available on Workers Paid plan

Note

K2 is in **public beta**, and any developer with a [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) can start using it. During the beta, each account can store up to 10 GB. To request a higher limit, refer to [Limits](https://developers.cloudflare.com/k2/platform/limits/#account-limits).

Cloudflare K2 is a durable log. Produce records to a log, store them for a configurable retention period, and consume them from one or more independent consumers.

[Get started](https://developers.cloudflare.com/k2/get-started/)

---

## Features

[Create a K2 stream](https://developers.cloudflare.com/k2/get-started/)

Create a K2 stream, produce records to it, and consume them through a subscription.

Use Create a K2 stream

[Produce with a Workers binding or HTTP](https://developers.cloudflare.com/k2/features/produce/)

Produce records to a K2 stream with a Workers binding or the HTTP API.

Produce to K2

[Configure retention period](https://developers.cloudflare.com/k2/configuration/#retention)

Records in K2 can be stored for up to 30 days, with longer retention available by request.

Use Configure retention period

[Create a subscription to consume](https://developers.cloudflare.com/k2/features/consume/)

Share records across a group of consumers, or deliver every record to multiple independent consumers, with subscriptions.

Create a subscription

---

## Related products

[Workers](https://developers.cloudflare.com/workers/)

Build serverless applications and deploy instantly across the globe for exceptional performance, reliability, and scale.

[Queues](https://developers.cloudflare.com/queues/)

Complete asynchronous tasks with guaranteed delivery and pull-based Worker consumers.

---
