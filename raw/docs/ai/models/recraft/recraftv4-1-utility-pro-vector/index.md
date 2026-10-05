---
description: Generate detailed, high-resolution SVG vector graphics from text prompts with a general-purpose model, scalable to any size for print and large-scale design work.
title: Recraft V4.1 Utility Pro SVG
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Utility Pro SVG

Text-to-Image • Recraft

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro-vector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-utility-pro-vector`

- Third-party
- Zero data retention

Generate detailed, high-resolution SVG vector graphics from text prompts with a general-purpose model, scalable to any size for print and large-scale design work.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://www.recraft.ai/terms) |
| More information | [link ↗](https://www.recraft.ai/) |
| Zero data retention | Yes |
| Pricing | <ul><li>Per image$0.30</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro-vector',
  { prompt: 'A clean, versatile logo for a software company with abstract geometric shapes' },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-utility-pro-vector",
  "input": {
    "prompt": "A clean, versatile logo for a software company with abstract geometric shapes"
  }
}'
```

![Logo Design](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/logo-design.jpg)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/logo-design.jpg"
  },
  "state": "Completed"
}
```

## Examples

<details>

<summary>**Detailed Illustration** — High-resolution vector illustration</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro-vector',
  {
    prompt:
      'A detailed flat vector illustration of a city map with labeled streets, parks, and landmarks',
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
  "model": "recraft/recraftv4-1-utility-pro-vector",
  "input": {
    "prompt": "A detailed flat vector illustration of a city map with labeled streets, parks, and landmarks",
    "size": "2048x2048"
  }
}'
```

![Detailed Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/detailed-illustration.jpg)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/detailed-illustration.jpg"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Print-Ready Vector** — High-resolution vector for large-format print</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro-vector',
  {
    prompt:
      'A decorative border pattern with repeating floral and leaf motifs, suitable for certificate or diploma design',
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
  "model": "recraft/recraftv4-1-utility-pro-vector",
  "input": {
    "prompt": "A decorative border pattern with repeating floral and leaf motifs, suitable for certificate or diploma design",
    "size": "2048x2048"
  }
}'
```

![Print-Ready Vector](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/print-ready-vector.jpg)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/print-ready-vector.jpg"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Brand Illustration** — Vector illustration with brand colors</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro-vector',
  {
    prompt: 'A flat vector illustration of interconnected nodes representing a network or data flow',
    controls: { colors: [{ rgb: [0, 122, 204] }, { rgb: [255, 165, 0] }, { rgb: [240, 240, 240] }] },
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-utility-pro-vector",
  "input": {
    "prompt": "A flat vector illustration of interconnected nodes representing a network or data flow",
    "controls": {
      "colors": [
        {
          "rgb": [
            0,
            122,
            204
          ]
        },
        {
          "rgb": [
            255,
            165,
            0
          ]
        },
        {
          "rgb": [
            240,
            240,
            240
          ]
        }
      ]
    }
  }
}'
```

![Brand Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/brand-illustration.jpg)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro-vector/brand-illustration.jpg"
  },
  "state": "Completed"
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

Input [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro-vector/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro-vector/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro-vector/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro-vector/schema-output.json)
