---
description: Recraft V4.1 Utility Pro is a general-purpose text-to-image model producing high-resolution 2048px+ output for a wide range of production and print use cases.
title: Recraft V4.1 Utility Pro
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Utility Pro

Text-to-Image • Recraft

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-utility-pro`

- Third-party
- Zero data retention

Recraft V4.1 Utility Pro is a general-purpose text-to-image model producing high-resolution 2048px+ output for a wide range of production and print use cases.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://www.recraft.ai/terms) |
| More information | [link ↗](https://www.recraft.ai/) |
| Zero data retention | Yes |
| Pricing | <ul><li>Per image$0.25</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro',
  {
    prompt:
      'A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-utility-pro",
  "input": {
    "prompt": "A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests"
  }
}'
```

![Print-Ready Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png"
  },
  "state": "Completed"
}
```

## Examples

<details>

<summary>**Large Format Art** — Large canvas general-purpose image</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro',
  {
    prompt:
      'A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky',
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
  "model": "recraft/recraftv4-1-utility-pro",
  "input": {
    "prompt": "A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky",
    "size": "2048x2048"
  }
}'
```

![Large Format Art](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Marketing Asset** — High-resolution marketing visual with controlled colors</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro',
  {
    prompt: 'A clean, modern banner illustration of a smartphone displaying a productivity app',
    controls: {
      background_color: { rgb: [250, 250, 255] },
      colors: [{ rgb: [100, 200, 150] }, { rgb: [20, 20, 60] }],
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
  "model": "recraft/recraftv4-1-utility-pro",
  "input": {
    "prompt": "A clean, modern banner illustration of a smartphone displaying a productivity app",
    "controls": {
      "background_color": {
        "rgb": [
          250,
          250,
          255
        ]
      },
      "colors": [
        {
          "rgb": [
            100,
            200,
            150
          ]
        },
        {
          "rgb": [
            20,
            20,
            60
          ]
        }
      ]
    },
    "size": "2048x2048"
  }
}'
```

![Marketing Asset](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png"
  },
  "state": "Completed"
}
```

</details>

<details>

<summary>**Technical Diagram** — High-resolution technical or infographic illustration</summary>



```ts
const response = await env.AI.run(
  'recraft/recraftv4-1-utility-pro',
  {
    prompt:
      'A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "recraft/recraftv4-1-utility-pro",
  "input": {
    "prompt": "A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers"
  }
}'
```

![Technical Diagram](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png)

```json
{
  "gatewayMetadata": {
    "keySource": "Unified"
  },
  "result": {
    "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png"
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

Input [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-output.json)
