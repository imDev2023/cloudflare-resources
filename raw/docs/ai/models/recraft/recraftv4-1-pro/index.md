---
description: Recraft V4.1 Pro generates high-resolution, art-directed images at 2048px+ tuned for high aesthetics, with strong composition, text rendering, and refined design taste. Built for print and production work.
title: Recraft V4.1 Pro
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Pro

Text-to-Image • Recraft

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-pro`

- Third-party
- Zero data retention

Recraft V4.1 Pro generates high-resolution, art-directed images at 2048px+ tuned for high aesthetics, with strong composition, text rendering, and refined design taste. Built for print and production work.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://www.recraft.ai/terms) |
| More information | [link ↗](https://www.recraft.ai/) |
| Zero data retention | Yes |
| Pricing | <ul><li>Per image$0.25</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-pro',
  {
    prompt:
      'A detailed vintage botanical illustration of a rose with leaves and thorns, scientific illustration style',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-pro",
  "input": {
    "prompt": "A detailed vintage botanical illustration of a rose with leaves and thorns, scientific illustration style"
  }
}'
```

![Print-Ready Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/print-ready-illustration.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/print-ready-illustration.png"
  },
  "state": "Completed"
}
```

## Examples

<details>

<summary>**Large Format Art** — Large canvas digital art</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-pro',
  {
    prompt:
      'A sweeping fantasy landscape with floating islands, waterfalls cascading into clouds, and ancient stone bridges connecting the islands',
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
  "model": "recraft/recraftv4-1-pro",
  "input": {
    "prompt": "A sweeping fantasy landscape with floating islands, waterfalls cascading into clouds, and ancient stone bridges connecting the islands",
    "size": "2048x2048"
  }
}'
```

![Large Format Art](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/large-format-art.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/large-format-art.png"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Brand Asset** — Professional brand asset with controlled colors</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-pro',
  {
    prompt:
      'A modern, clean illustration of a shield with a checkmark inside, representing security and trust',
    controls: {
      background_color: { rgb: [15, 23, 42] },
      colors: [{ rgb: [46, 117, 182] }, { rgb: [255, 255, 255] }],
    },
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
  "model": "recraft/recraftv4-1-pro",
  "input": {
    "prompt": "A modern, clean illustration of a shield with a checkmark inside, representing security and trust",
    "controls": {
      "background_color": {
        "rgb": [
          15,
          23,
          42
        ]
      },
      "colors": [
        {
          "rgb": [
            46,
            117,
            182
          ]
        },
        {
          "rgb": [
            255,
            255,
            255
          ]
        }
      ]
    },
    "size": "2048x2048"
  }
}'
```

![Brand Asset](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/brand-asset.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/brand-asset.png"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Editorial Illustration** — Magazine-quality editorial illustration</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-pro',
  {
    prompt:
      'A conceptual illustration of artificial intelligence as a tree with circuit-board branches and glowing data leaves',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-pro",
  "input": {
    "prompt": "A conceptual illustration of artificial intelligence as a tree with circuit-board branches and glowing data leaves"
  }
}'
```

![Editorial Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/editorial-illustration.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/editorial-illustration.png"
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

Input [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/schema-output.json)
