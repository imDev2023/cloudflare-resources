---
description: Bridge Realtime SFU tracks and external media services using WebSocket audio and JPEG frame delivery.
title: Media transport adapters
image: https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/og.png?v=d0bd7f1a594fd65b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Media transport adapters

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Media transport adapters connect WebRTC tracks to services that exchange media over another transport. The WebSocket adapter supports audio ingest, audio egress, and video egress as JPEG frames.

An external service can process or generate audio without implementing a WebRTC peer. Your backend creates the adapter and manages its lifetime.

## WebSocket adapter

The WebSocket adapter is in beta. Choose the path your external service needs; each adapter handles one direction:

| Your service | Direction | Media |
| --- | --- | --- |
| Generates audio | WebSocket → SFU → WebRTC | PCM audio published as a WebRTC audio track |
| Transcribes or processes audio | WebRTC → SFU → WebSocket | Audio delivered as PCM |
| Inspects frames or generates previews | WebRTC → SFU → WebSocket | Video delivered as JPEG frames |

**WebRTC endpoint**

Media tracks

Cloudflare**Realtime SFU**

**WebSocket adapters**

Binary media packets

**Your WebSocket service**

WebRTC endpointMedia tracks ↔Realtime SFU

Realtime SFUMedia ↔WebSocket adapters

WebSocket adaptersBinary media packets ↔Your WebSocket service

Use separate adapter instances for bidirectional audio. Video ingest over the WebSocket adapter is not supported.

[Use the WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)

## Learn with an example

The [AI audio guide](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/) shows speech generation and transcription through separate adapter paths. For video, the [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) receives frames in a Durable Object and distributes them to viewers.

Both examples are experimental and require application authentication and authorization before public use. Their repository guides describe setup and integration limitations.
