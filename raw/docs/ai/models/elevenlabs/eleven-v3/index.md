---
description: ElevenLabs' latest text-to-speech model for highly expressive, natural speech generation with advanced voice control.
title: Eleven v3
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![ElevenLabs logo](https://developers.cloudflare.com/_astro/elevenlabs.0RXw7U95.svg)

# Eleven v3

Text-to-Speech • ElevenLabs

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-v3/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`elevenlabs/eleven-v3`

- Third-party

ElevenLabs' latest text-to-speech model for highly expressive, natural speech generation with advanced voice control.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://elevenlabs.io/terms) |
| More information | [link ↗](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) |
| Pricing | <ul><li>Per character$0.0001</li><li>Default (per second)$0.0001</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'elevenlabs/eleven-v3',
  {
    text: 'Welcome to Cloudflare AI Gateway. This is ElevenLabs speech synthesis with a natural, expressive delivery.',
    voice_id: 'JBFqnCBsd6RMkjVDRZzb',
    output_format: 'mp3_44100_128',
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "elevenlabs/eleven-v3",
  "input": {
    "text": "Welcome to Cloudflare AI Gateway. This is ElevenLabs speech synthesis with a natural, expressive delivery.",
    "voice_id": "JBFqnCBsd6RMkjVDRZzb",
    "output_format": "mp3_44100_128"
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "audio": "https://examples.aig.cloudflare.com/elevenlabs/eleven-v3/expressive-speech.mp3"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Parameters

text

`string`requiredminLength: 1maxLength: 10000The text to convert into speech.

voice\_id

`string`requiredminLength: 1The ElevenLabs voice ID to use for generation.

output\_format

`string`enum: mp3\_22050\_32, mp3\_24000\_48, mp3\_44100\_128, mp3\_44100\_192, mp3\_44100\_32, mp3\_44100\_64, mp3\_44100\_96, opus\_48000\_128, opus\_48000\_192, opus\_48000\_32, opus\_48000\_64, opus\_48000\_96

language\_code

`string`ISO 639-1 language code to enforce.

▶voice\_settings{}

`object`

seed

`integer`minimum: 0maximum: 4294967295

previous\_text

`string`

next\_text

`string`

apply\_text\_normalization

`string`enum: auto, on, off

audio

`string`URL to the generated audio file.

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-v3/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-v3/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-v3/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-v3/schema-output.json)
