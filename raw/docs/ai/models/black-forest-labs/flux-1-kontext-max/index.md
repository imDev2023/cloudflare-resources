---
description: FLUX.1 Kontext [max] is Black Forest Labs' highest-quality Kontext model for text-to-image generation and context-aware image editing.
title: FLUX.1 Kontext [max]
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.1 Kontext \[max]

Text-to-Image • Black Forest Labs

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-1-kontext-max`

- Third-party

FLUX.1 Kontext \[max] is Black Forest Labs' highest-quality Kontext model for text-to-image generation and context-aware image editing.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://blackforestlabs.ai/terms-of-service/) |
| More information | [link ↗](https://docs.bfl.ml/api-reference/models/edit-or-create-an-image-with-flux1-kontext-[max]) |
| Pricing | <ul><li>Per image$0.08</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'black-forest-labs/flux-1-kontext-max',
  {
    prompt:
      'A lone warrior in bloodstained samurai armor stands before a pagoda engulfed in flames, cinematic dark fantasy realism',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "black-forest-labs/flux-1-kontext-max",
  "input": {
    "prompt": "A lone warrior in bloodstained samurai armor stands before a pagoda engulfed in flames, cinematic dark fantasy realism"
  }
}'
```

![Maximum Quality Generation](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/maximum-quality-generation.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/maximum-quality-generation.png"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Reproducible Generation** — Use a seed and PNG output for reproducible image generation.</summary>



```ts
const response = await env.AI.run(
  'black-forest-labs/flux-1-kontext-max',
  {
    prompt:
      'A detailed oil painting portrait of a Renaissance nobleman with an intricate lace collar',
    seed: 42,
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
  "model": "black-forest-labs/flux-1-kontext-max",
  "input": {
    "prompt": "A detailed oil painting portrait of a Renaissance nobleman with an intricate lace collar",
    "seed": 42,
    "output_format": "png"
  }
}'
```

![Reproducible Generation](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/reproducible-generation.png)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/reproducible-generation.png"
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

input\_image

`string`Optional base64 encoded image or URL to edit.

aspect\_ratio

`string`Output aspect ratio, from 3:7 to 7:3. Defaults to 1:1.

seed

`integer | null`Optional seed for reproducible generation.

prompt\_upsampling

`boolean`Whether to upsample the prompt. Defaults to false.

safety\_tolerance

`integer`minimum: 0maximum: 6Moderation tolerance. 0 is strictest and 6 is most permissive.

output\_format

`string`enum: jpeg, pngOutput image format. Defaults to jpeg.

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-output.json)
