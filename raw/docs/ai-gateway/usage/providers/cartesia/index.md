---
description: Route Cartesia text-to-speech requests through AI Gateway for observability and control.
title: Cartesia
image: https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/og.png?v=5185dc82d53acfbf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cartesia

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cartesia ↗︎](https://docs.cartesia.ai/) provides advanced text-to-speech services with customizable voice models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia
```

## URL Structure

When making requests to Cartesia, replace `https://api.cartesia.ai/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia`.

## Prerequisites

When making requests to Cartesia, ensure you have the following:

- Your AI Gateway Account ID.
- Your AI Gateway gateway name.
- An active Cartesia API token.
- The model ID and voice ID for the Cartesia voice model you want to use.

## Example

### cURL

*Requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia/tts/bytes \
  --header 'Content-Type: application/json' \
  --header 'Cartesia-Version: 2024-06-10' \
  --header 'X-API-Key: {cartesia_api_token}' \
  --data '{
    "transcript": "Welcome to Cloudflare - AI Gateway!",
    "model_id": "sonic-english",
    "voice": {
        "mode": "id",
        "id": "694f9389-aac1-45b6-b726-9d9369183238"
    },
    "output_format": {
        "container": "wav",
        "encoding": "pcm_f32le",
        "sample_rate": 44100
    }
}
```
