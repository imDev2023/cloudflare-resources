---
description: Diffusion-based text-to-image generative model by Stability AI. Generates and modify images based on text prompts.
title: stable-diffusion-xl-base-1.0
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Stability.ai logo](https://developers.cloudflare.com/_astro/stabilityai.VsBx3CKv.svg)

# stable-diffusion-xl-base-1.0

Beta

Text-to-Image • Stability.ai

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/stabilityai/stable-diffusion-xl-base-1.0`

- Cloudflare-hosted

Diffusion-based text-to-image generative model by Stability AI. Generates and modify images based on text prompts.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md) |
| More information | [link ↗](https://stability.ai/stable-diffusion) |
| Beta | Yes |
| Unit Pricing | $0.00 per step |

## Parameters

prompt

`string`requiredminLength: 1A text description of the image you want to generate

negative\_prompt

`string`Text describing elements to avoid in the generated image

height

`integer`minimum: 256maximum: 2048The height of the generated image in pixels

width

`integer`minimum: 256maximum: 2048The width of the generated image in pixels

▶image\[]

`array`For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values

image\_b64

`string`For use with img2img tasks. A base64-encoded string of the input image

▶mask\[]

`array`An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values

num\_steps

`integer`default: 20maximum: 20The number of diffusion steps; higher values can improve quality but take longer

strength

`number`default: 1A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image

guidance

`number`default: 7.5Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt

seed

`integer`Random seed for reproducibility of the image generation

The binding returns a `ReadableStream` with the output (check the model's output schema).

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/schema-input.json) [Download](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/schema-input.json)

Output [Open](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/schema-output.json) [Download](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/schema-output.json)
