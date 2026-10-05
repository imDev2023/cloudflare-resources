---
description: xAI's Grok Imagine image model. Generates and edits images from text and reference-image inputs with configurable aspect ratio and resolution.
title: Grok Imagine Image
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Imagine Image

Text-to-Image • xAI

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-imagine-image`

- Third-party
- Zero data retention

xAI's Grok Imagine image model. Generates and edits images from text and reference-image inputs with configurable aspect ratio and resolution.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://x.ai/legal/terms-of-service) |
| More information | [link ↗](https://docs.x.ai/developers/models/grok-imagine-image) |
| Zero data retention | Yes |
| Pricing | <ul><li>Per image$0.02</li><li>Per input image$0.002</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'xai/grok-imagine-image',
  { prompt: 'A golden retriever puppy playing in autumn leaves' },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "xai/grok-imagine-image",
  "input": {
    "prompt": "A golden retriever puppy playing in autumn leaves"
  }
}'
```

![Simple Generation](https://examples.aig.cloudflare.com/xai/grok-imagine-image/simple-generation.jpeg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image/simple-generation.jpeg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Custom Aspect Ratio** — Portrait orientation render at 2K resolution</summary>



```ts
const response = await env.AI.run(
  'xai/grok-imagine-image',
  {
    prompt:
      'A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures',
    aspect_ratio: '3:4',
    resolution: '2k',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "xai/grok-imagine-image",
  "input": {
    "prompt": "A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures",
    "aspect_ratio": "3:4",
    "resolution": "2k"
  }
}'
```

![Custom Aspect Ratio](https://examples.aig.cloudflare.com/xai/grok-imagine-image/custom-aspect-ratio.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image/custom-aspect-ratio.png"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Cinematic Landscape** — Widescreen landscape at 2K resolution</summary>



```ts
const response = await env.AI.run(
  'xai/grok-imagine-image',
  {
    prompt:
      'A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting',
    aspect_ratio: '16:9',
    resolution: '2k',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "xai/grok-imagine-image",
  "input": {
    "prompt": "A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting",
    "aspect_ratio": "16:9",
    "resolution": "2k"
  }
}'
```

![Cinematic Landscape](https://examples.aig.cloudflare.com/xai/grok-imagine-image/cinematic-landscape.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image/cinematic-landscape.png"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

## Parameters

prompt

`string`required

n

`integer`minimum: 1maximum: 10

aspect\_ratio

`string`enum: 1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, auto

quality

`string`enum: low, medium, high

resolution

`string`enum: 1k, 2k

response\_format

`string`enum: url, b64\_json

user

`string`

▶image{}

`object`

▶images\[]

`array`maxItems: 10

▶mask{}

`object`

image

`string`

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image/schema-output.json)
