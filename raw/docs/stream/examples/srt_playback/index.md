---
description: Example of sub 1s latency video playback using SRT and ffplay
title: SRT playback
image: https://developers.cloudflare.com/stream/examples/srt_playback/og.png?v=2fa12ac6c5c30aa7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/stream/llms.txt  
> Use this file to discover all available pages before exploring further.

# SRT playback

Example of sub 1s latency video playback using SRT and ffplay

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/stream/examples/srt_playback/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Before you can play live video, you must first be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live/start-stream-live).

Copy the SRT Playback URL for your live input from either:

- The **Live inputs** page of the Cloudflare dashboard. [Go to **Live inputs** ↗](https://dash.cloudflare.com/?to=/:account/stream/inputs)
- The [Stream API](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#use-the-api)

Paste it into the URL below, replacing `<SRT_PLAYBACK_URL>`:

*SRT playback with ffplaysh*

```sh
ffplay -analyzeduration 1 -fflags -nobuffer -probesize 32 -sync ext '<SRT_PLAYBACK_URL>'
```

For more, refer to [Play live video in native apps with less than one second latency](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/#play-live-video-in-native-apps-with-less-than-1-second-latency).
