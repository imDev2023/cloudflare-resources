---
title: RTKAi
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/og.png?v=b1298b09dfb684a8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKAi

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This module consists of the `ai` object which is used to interface with product's AI features. You can obtain the live meeting transcript and use other meeting AI features such as summary, and agenda using this object.

### meeting.ai.onTranscript(transcript)

**Kind**: instance method of [`RTKAi`](#module_RTKAi)

| Param | Type | Description |
| --- | --- | --- |
| transcript | `TranscriptionData` | Transcript data received for a participant. |
