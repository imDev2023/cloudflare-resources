---
description: Send logs directly from edge with low latency.
title: Edge Log Delivery
image: https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/og.png?v=95bfbf216e12fe49
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Edge Log Delivery

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Edge Log Delivery allows customers to send logs directly from Cloudflare’s edge to their destination of choice. You can configure the maximum interval for your log batches between 30 seconds and five minutes. However, you cannot specify a minimum interval for log batches, meaning that log files may be sent in shorter intervals than the maximum specified. Compared to Logpush, Edge Log Delivery sends logs with lower latency, more frequently, and in smaller batches.

Edge Log Delivery is only available for HTTP request logs. Refer to the [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#kind) page for steps on how to configure a job to use Edge Log Delivery.
