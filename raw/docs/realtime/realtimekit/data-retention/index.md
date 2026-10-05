---
description: Review how long RealtimeKit stores meeting chat, recordings, analytics, and webhook logs.
title: Data retention
image: https://developers.cloudflare.com/realtime/realtimekit/data-retention/og.png?v=98375a02dd8e78f8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Data retention

Last updated Sep 11, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/data-retention/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

RealtimeKit retains data for the following periods:

| Data type | Retention period |
| --- | --- |
| Meeting and participant records | Indefinitely |
| Meeting chat with [`persist_chat`](<https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/#(resource)%20realtime_kit.meetings%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20persist_chat%20%3E%20(schema)>) | Indefinitely |
| Meeting chat without [`persist_chat`](<https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/#(resource)%20realtime_kit.meetings%20%3E%20(method)%20create%20%3E%20(params)%200%20%3E%20(param)%20persist_chat%20%3E%20(schema)>) | 7 days |
| Composite recordings | 7 days |
| Track recordings | 7 days |
| Transcripts | 7 days |
| Call analytics | 6 months |
| Webhook logs | 1 month |
