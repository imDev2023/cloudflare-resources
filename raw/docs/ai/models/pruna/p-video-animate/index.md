---
description: Pruna's P-Video-Animate takes a source video and a subject reference image, then animates the referenced subject using the motion and audio from the source video.
title: P-Video-Animate
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Video-Animate

Image-to-Video • Pruna AI

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-video-animate`

- Third-party

Pruna's P-Video-Animate takes a source video and a subject reference image, then animates the referenced subject using the motion and audio from the source video.

| Model Info | |
| --- | --- |
| More information | [link ↗](https://docs.api.pruna.ai/guides/quickstart) |
| Pricing | <ul><li>Default (per second)$0.03</li><li>@720p (per second)$0.03</li><li>@1080p (per second)$0.06</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'pruna/p-video-animate',
  {
    video: 'https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4',
    image: 'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
    resolution: '720p',
    target_fps: 'original',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "pruna/p-video-animate",
  "input": {
    "video": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    "image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
    "resolution": "720p",
    "target_fps": "original"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/pruna/p-video-animate/motion-transfer.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Parameters

video

`string`requiredSource RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI.

image

`string`requiredReference image of the subject to animate. HTTP(S) URL or data URI.

turbo

`boolean`requireddefault: falseTurbo mode: faster generation for slightly lower quality.

resolution

`string`requireddefault: 720penum: 720p, 1080pTarget resolution.

save\_audio

`boolean`requireddefault: trueSave the video with audio.

ignore\_audio

`boolean`requireddefault: falseIgnore source audio during generation.

target\_fps

`string`requireddefault: originalenum: 24, 48, originalTarget FPS for the working video.

instruction\_prompt

`string`requireddefault: Further instruction on how the reference subject should be animated.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable\_safety\_checker

`boolean`requireddefault: falseDisable safety checker for generated videos.

video

`string`format: uriPresigned URL for the animated video.

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-output.json)
