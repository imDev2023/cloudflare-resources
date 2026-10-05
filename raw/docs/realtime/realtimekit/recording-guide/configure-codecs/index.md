---
description: Configure video codecs, resolution, and container formats for RealtimeKit recordings.
title: Configure Video Settings
image: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/og.png?v=be02e7f7d1c1a21e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure Video Settings

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Video codecs are software programs that compress and decompress digital video data for transmission, storage, or playback. Configuring the appropriate video codec can help reduce file size, enhance video quality, and ensure compatibility with different playback devices.

## Configure Codecs

You can modify the codec which is used for recording the videos. We currently support the following codecs:

- **H264 (default)**: Records video using the H.264 codec with 1280px × 720px resolution, and 384 kbps AAC audio in MP4 container.
- **VP8**: Records video using the VP8 codec with 1280px × 720px resolution, and Vorbis codec audio in WebM container.

You can change the codec by specifying the codec in the `video_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:

```json
{
  "video_config": {
    "codec": "H264"
  }
}
```

## Download Video Files

The video file for your recording is generated only if you passed the `video_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `downloadUrl` provided in the response body of the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/) to download and export the video file.
