---
description: Preview high-performance multimodal video generation and editing model with conversational controls and generated audio.
title: Gemini Omni Flash
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini Omni Flash

Text-to-Video • Google

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/gemini-omni-flash`

- Third-party

Preview high-performance multimodal video generation and editing model with conversational controls and generated audio.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://ai.google.dev/gemini-api/terms) |
| Pricing | <ul><li>Input text (per 1M tokens)$1.50</li><li>Input image (per 1M tokens)$1.50</li><li>Input audio (per 1M tokens)$1.50</li><li>Input video (per 1M tokens)$1.50</li><li>Output text (per 1M tokens)$9.00</li><li>Reasoning (per 1M tokens)$9.00</li><li>Output video (per 1M tokens)$17.50</li><li>Default (per second)$1.50</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'google/gemini-omni-flash',
  {
    text: 'A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.',
    aspect_ratio: '16:9',
    resolution: '720p',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/gemini-omni-flash",
  "input": {
    "text": "A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.",
    "aspect_ratio": "16:9",
    "resolution": "720p"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/underwater-reef.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Breakfast robot** — Generate a portrait-format character scene</summary>



```ts
const response = await env.AI.run(
  'google/gemini-omni-flash',
  {
    text: 'A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.',
    aspect_ratio: '9:16',
    resolution: '720p',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/gemini-omni-flash",
  "input": {
    "text": "A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.",
    "aspect_ratio": "9:16",
    "resolution": "720p"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/breakfast-robot.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Desert train** — Generate a high-resolution desert scene</summary>



```ts
const response = await env.AI.run(
  'google/gemini-omni-flash',
  {
    text: 'A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.',
    aspect_ratio: '16:9',
    resolution: '1080p',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/gemini-omni-flash",
  "input": {
    "text": "A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.",
    "aspect_ratio": "16:9",
    "resolution": "1080p"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/desert-train.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Northern lights** — Generate a low-resolution night landscape</summary>



```ts
const response = await env.AI.run(
  'google/gemini-omni-flash',
  {
    text: 'Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.',
    aspect_ratio: '16:9',
    resolution: '360p',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/gemini-omni-flash",
  "input": {
    "text": "Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.",
    "aspect_ratio": "16:9",
    "resolution": "360p"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/northern-lights.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

## Parameters

text

`string`Text prompt or editing instruction

image

`string`First-frame or primary reference image

last\_frame

`string`Last-frame reference image

▶reference\_images\[]

`array`maxItems: 10

video

`string`Reference video for editing or extension

audio

`string`Reference audio input

previous\_interaction\_id

`string`

aspect\_ratio

`string`enum: 16:9, 9:16

resolution

`string`enum: 360p, 720p, 1080p, 4k

▶video

`one of`

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-output.json)
