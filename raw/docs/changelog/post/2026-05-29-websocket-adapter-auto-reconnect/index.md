---
description: Realtime SFU WebSocket adapters now automatically reconnect and buffer media after brief endpoint disconnects or restarts when using Stream mode.
title: Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media
image: https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/og.png?v=5d288e00f6b01d0f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 29, 2026

## Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is a [WebRTC Selective Forwarding Unit that runs on Cloudflare's global network](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/), so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.

When you use the [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.

#### Streaming WebRTC media to WebSocket endpoints

Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including [Durable Objects](https://developers.cloudflare.com/durable-objects/), [Workers](https://developers.cloudflare.com/workers/), [Containers](https://developers.cloudflare.com/containers/), or external services, without running a WebRTC client themselves.

The [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: [PCM audio frames and JPEG video frames](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#media-formats).

#### What changed

When you use the WebSocket adapter in [Stream mode (egress)](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#stream-mode-egress) to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now [automatically reconnects](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming) after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.

Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.

The reconnect behavior also includes [live-first media buffering](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect), so brief interruptions reduce media loss without replaying stale video.

#### Reconnect behavior

During reconnect:

- Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.
- Video resumes from the [latest available JPEG frame](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#video-jpeg) instead of replaying stale frames.
- Recovery is best effort and does not guarantee gapless or exactly-once delivery.

If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.

#### Learn more

- [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)
- [Automatic reconnection for streaming](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming)
- [Get started with Realtime SFU](https://developers.cloudflare.com/realtime/sfu/get-started/)
- [Realtime SFU example architecture](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)
- [Realtime vs Regular SFUs](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)
- [Global SFU Network Visualization ↗︎](https://realtime-sfu.dev-demos.workers.dev/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/#page","headline":"Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media","description":"Realtime SFU WebSocket adapters now automatically reconnect and buffer media after brief endpoint disconnects or restarts when using Stream mode.","url":"https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/og.png?v=5d288e00f6b01d0f","dateModified":"2026-05-29","datePublished":"2026-05-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
