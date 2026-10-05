---
description: Pruna's P-Video-Replace takes a source video and one or more identity reference images, then places the referenced person or people into the video while preserving the source motion and audio.
title: P-Video-Replace
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Video-Replace

Image-to-Video • Pruna AI

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-video-replace/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-video-replace`

- Third-party

Pruna's P-Video-Replace takes a source video and one or more identity reference images, then places the referenced person or people into the video while preserving the source motion and audio.

| Model Info | |
| --- | --- |
| More information | [link ↗](https://docs.api.pruna.ai/guides/quickstart) |
| Pricing | <ul><li>Default (per second)$0.03</li><li>@720p (per second)$0.03</li><li>@1080p (per second)$0.06</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'pruna/p-video-replace',
  {
    video: 'https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4',
    images: ['https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg'],
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
  "model": "pruna/p-video-replace",
  "input": {
    "video": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    "images": [
      "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg"
    ],
    "resolution": "720p",
    "target_fps": "original"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/pruna/p-video-replace/character-swap.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Parameters

video

`string`requiredSource RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI.

▶images\[]

`array`requiredminItems: 1maxItems: 3Identity reference image(s), 1 to 3, to place into the video. Each entry is an HTTP(S) URL or a data URI.

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

`string`requireddefault: Further instruction on how to place people from the reference images into the scene.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable\_safety\_checker

`boolean`requireddefault: falseDisable safety checker for generated videos.

video

`string`format: uriPresigned URL for the replacement video.

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/pruna/p-video-replace/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/pruna/p-video-replace/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/pruna/p-video-replace/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/pruna/p-video-replace/schema-output.json)
