---
description: Configure audio codec format and channel settings for RealtimeKit recordings.
title: Set Audio Configurations
image: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/og.png?v=8c84befdbf726b42
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Set Audio Configurations

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Recording audio requires configuring the **codec** and **channel** parameters to guarantee optimal quality and compatibility with your application's demands. The codec determines the encoding format for the audio, and the channel specifies the number of audio channels for the recording. You can modify the following `audio_config` used for recording the audio:

## Codec

Codec determines the audio encoding format for recording, with MP3 and AAC being the supported formats.

- AAC (default)
- MP3

Note

If [VP8](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/) is selected for `video_config`, changing `audio_config` is not allowed. In this case, the codec in the `audio_config` is automatically set to `vorbis`.

## Channel

Audio signal pathway within an audio file that carries a specific sound source. The following channels are supported:

- stereo (default)
- mono

You can modify the configs by specifying it in the `audio_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:

```json
{
  "audio_config": {
    "codec": "AAC"
    "channel": "stereo"
  }
}
```

## Download Audio Files

The audio file for your recording is generated only if you passed the `audio_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `audio_download_url` provided in the response body of the [Fetch details of a recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/) to download and export the audio file.
