---
description: FLUX.2 [pro] Preview is Black Forest Labs' recommended default for production image generation and editing — tracks the latest [pro] weights with strong multi-reference support.
title: FLUX.2 [pro]
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.2 \[pro]

Text-to-Image • Black Forest Labs

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-2-pro-preview`

- Third-party

FLUX.2 \[pro] Preview is Black Forest Labs' recommended default for production image generation and editing — tracks the latest \[pro] weights with strong multi-reference support.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://blackforestlabs.ai/terms-of-service/) |
| More information | [link ↗](https://blackforestlabs.ai/) |
| Pricing | <ul><li>First output megapixel$0.03</li><li>Per additional output megapixel$0.015</li><li>Per input megapixel$0.015</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'black-forest-labs/flux-2-pro-preview',
  {
    prompt:
      'A serene mountain landscape at golden hour, soft diffused light filtering through clouds',
    height: 1024,
    width: 1024,
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "black-forest-labs/flux-2-pro-preview",
  "input": {
    "prompt": "A serene mountain landscape at golden hour, soft diffused light filtering through clouds",
    "height": 1024,
    "width": 1024
  }
}'
```

![Simple Prompt](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Multi-Reference Editing** — Multi-reference editing — combine two reference images in a single composition</summary>



```ts
const response = await env.AI.run(
  'black-forest-labs/flux-2-pro-preview',
  {
    prompt: 'Combine the subjects of these images into a single editorial fashion scene',
    input_images: [
      'https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg',
      'https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg',
    ],
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "black-forest-labs/flux-2-pro-preview",
  "input": {
    "prompt": "Combine the subjects of these images into a single editorial fashion scene",
    "input_images": [
      "https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg",
      "https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg"
    ]
  }
}'
```

![Multi-Reference Editing](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Reproducible PNG Output** — Seeded generation with PNG output for downstream editing pipelines</summary>



```ts
const response = await env.AI.run(
  'black-forest-labs/flux-2-pro-preview',
  { prompt: 'A pastel watercolor of a koi pond at sunrise', output_format: 'png', seed: 1337 },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "black-forest-labs/flux-2-pro-preview",
  "input": {
    "prompt": "A pastel watercolor of a koi pond at sunrise",
    "output_format": "png",
    "seed": 1337
  }
}'
```

![Reproducible PNG Output](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

## Parameters

prompt

`string`requiredText prompt for image generation or editing.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Optional seed for reproducible generation.

width

`integer`minimum: 64maximum: 9007199254740991Width of the generated image in pixels (minimum 64). Omit to let BFL pick.

height

`integer`minimum: 64maximum: 9007199254740991Height of the generated image in pixels (minimum 64). Omit to let BFL pick.

safety\_tolerance

`integer`minimum: 0maximum: 5Tolerance for input/output moderation. 0 is the strictest, 5 the most permissive. Defaults to 2.

output\_format

`string`enum: jpeg, png, webpOutput image format. Defaults to jpeg.

▶input\_images\[]

`array`maxItems: 8Up to 8 reference images for editing or multi-image composition. Each entry is an HTTPS URL or a data:image/...;base64,... URI.

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-output.json)
