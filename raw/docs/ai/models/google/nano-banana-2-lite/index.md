---
description: Google's fastest Gemini image generation model for rapid image creation and iteration.
title: Nano Banana 2 Lite
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Nano Banana 2 Lite

Text-to-Image • Google

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/nano-banana-2-lite`

- Third-party
- Zero data retention

Google's fastest Gemini image generation model for rapid image creation and iteration.

| Model Info | |
| --- | --- |
| Context Window [ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/) | 65,536 tokens |
| Terms and License | [link ↗](https://ai.google.dev/gemini-api/terms) |
| More information | [link ↗](https://deepmind.google/technologies/imagen/) |
| Zero data retention | Yes |
| Pricing | <ul><li>Input (per 1M tokens)$0.25</li><li>Output (per 1M tokens)$30.00</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'google/nano-banana-2-lite',
  {
    prompt:
      'A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design',
    aspect_ratio: '16:9',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/nano-banana-2-lite",
  "input": {
    "prompt": "A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design",
    "aspect_ratio": "16:9"
  }
}'
```

![Concept Sketch](https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Product Render** — Create a square PNG product image</summary>



```ts
const response = await env.AI.run(
  'google/nano-banana-2-lite',
  {
    prompt:
      'A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style',
    aspect_ratio: '1:1',
    output_format: 'png',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "google/nano-banana-2-lite",
  "input": {
    "prompt": "A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style",
    "aspect_ratio": "1:1",
    "output_format": "png"
  }
}'
```

![Product Render](https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png"
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

▶image\_input\[]

`array`maxItems: 3

aspect\_ratio

`string`enum: match\_input\_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

output\_format

`string`enum: jpg, png

resolution

`string`enum: 1K, 2K, 4K

image

`string`format: uri

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-output.json)
