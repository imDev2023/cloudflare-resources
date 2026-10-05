---
description: Generate detailed, production-ready SVG vector graphics from text prompts with fine geometry, scalable to any size for print and design work.
title: Recraft V4 Pro SVG
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4 Pro SVG

Text-to-Image • Recraft

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-pro-vector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-pro-vector`

- Third-party
- Zero data retention

Generate detailed, production-ready SVG vector graphics from text prompts with fine geometry, scalable to any size for print and design work.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://www.recraft.ai/terms) |
| More information | [link ↗](https://www.recraft.ai/) |
| Zero data retention | Yes |
| Pricing | <ul><li>Per image$0.30</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'recraft/recraftv4-pro-vector',
  { prompt: 'A modern minimalist logo for a cloud computing company, clean geometric shapes' },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-pro-vector",
  "input": {
    "prompt": "A modern minimalist logo for a cloud computing company, clean geometric shapes"
  }
}'
```

![Logo Design](https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/logo-design.svg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/logo-design.svg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Examples

<details>

<summary>**Icon Set** — Generate a vector icon</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-pro-vector',
  {
    prompt: 'A flat design icon of a rocket launching, suitable for a mobile app',
    size: '2048x2048',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-pro-vector",
  "input": {
    "prompt": "A flat design icon of a rocket launching, suitable for a mobile app",
    "size": "2048x2048"
  }
}'
```

![Icon Set](https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/icon-set.svg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/icon-set.svg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Print-Ready Vector** — High-resolution vector for large-format print</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-pro-vector',
  {
    prompt:
      'An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical',
    size: '2048x2048',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-pro-vector",
  "input": {
    "prompt": "An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical",
    "size": "2048x2048"
  }
}'
```

![Print-Ready Vector](https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/print-ready-vector.svg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/print-ready-vector.svg"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

</details>

<details>

<summary>**Brand Illustration** — Vector illustration with brand colors</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-pro-vector',
  {
    prompt: 'A vector illustration of a cityscape skyline at sunset with clean lines and flat colors',
    controls: { colors: [{ rgb: [255, 87, 51] }, { rgb: [41, 50, 65] }, { rgb: [239, 239, 239] }] },
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-pro-vector",
  "input": {
    "prompt": "A vector illustration of a cityscape skyline at sunset with clean lines and flat colors",
    "controls": {
      "colors": [
        {
          "rgb": [
            255,
            87,
            51
          ]
        },
        {
          "rgb": [
            41,
            50,
            65
          ]
        },
        {
          "rgb": [
            239,
            239,
            239
          ]
        }
      ]
    }
  }
}'
```

![Brand Illustration](https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/brand-illustration.svg)

```json
{
  "state": "Completed",
  "result": {
    "image": "https://examples.aig.cloudflare.com/recraft/recraftv4-pro-vector/brand-illustration.svg"
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

size

`string`

style

`string`

substyle

`string`

▶controls{}

`object`

image

`string`

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-pro-vector/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-pro-vector/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-pro-vector/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-pro-vector/schema-output.json)
