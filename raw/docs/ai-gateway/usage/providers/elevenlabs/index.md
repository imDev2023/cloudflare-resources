---
description: Route ElevenLabs text-to-speech requests through AI Gateway for observability and control.
title: ElevenLabs
image: https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/og.png?v=9969223ef571665a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# ElevenLabs

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[ElevenLabs ↗︎](https://elevenlabs.io/) offers advanced text-to-speech services, enabling high-quality voice synthesis in multiple languages.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs
```

## Prerequisites

When making requests to ElevenLabs, ensure you have the following:

- Your AI Gateway Account ID.
- Your AI Gateway gateway name.
- An active ElevenLabs API token.
- The model ID of the ElevenLabs voice model you want to use.

## Example

### cURL

*Requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128 \
  --header 'Content-Type: application/json' \
  --header 'xi-api-key: {elevenlabs_api_token}' \
  --data '{
    "text": "Welcome to Cloudflare - AI Gateway!",
    "model_id": "eleven_multilingual_v2"
}'
```
