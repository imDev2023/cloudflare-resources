---
description: MeloTTS is a high-quality multi-lingual text-to-speech library by MyShell.ai.
title: melotts
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![MyShell logo](https://developers.cloudflare.com/_astro/myshell.6ROagMV2.svg)

# melotts

Text-to-Speech • MyShell

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/myshell-ai/melotts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/myshell-ai/melotts`

- Cloudflare-hosted

MeloTTS is a high-quality multi-lingual text-to-speech library by MyShell.ai.

| Model Info | |
| --- | --- |
| Unit Pricing | $0.000205 per audio minute |

## Parameters

prompt

`string`requiredminLength: 1A text description of the audio you want to generate

lang

`string`default: enThe speech language (e.g., 'en' for English, 'fr' for French). Defaults to 'en' if not specified

▶Option 1{}

objectcontentType: application/json

Option 2

stringcontentType: audio/mpegformat: binary

The generated audio in MP3 format

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/@cf/myshell-ai/melotts/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/@cf/myshell-ai/melotts/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/@cf/myshell-ai/melotts/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/@cf/myshell-ai/melotts/schema-output.json)
