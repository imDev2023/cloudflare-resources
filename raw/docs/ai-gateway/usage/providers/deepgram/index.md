---
description: Route Deepgram speech-to-text and text-to-speech requests through AI Gateway for observability and control.
title: Deepgram
image: https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/og.png?v=1f9191c3744b3eb4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Deepgram

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Deepgram ↗︎](https://developers.deepgram.com/home) provides Voice AI APIs for speech-to-text, text-to-speech, and voice agents.

Note

Deepgram is also available through Workers AI, see [Deepgram Workers AI](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/#deepgram-workers-ai).

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram
```

## URL Structure

When making requests to Deepgram, replace `https://api.deepgram.com/` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/`.

## Prerequisites

When making requests to Deepgram, ensure you have the following:

- Your AI Gateway Account ID.
- Your AI Gateway gateway name.
- An active Deepgram API token.

## Example

### SDK

*TSts*

```ts
import { createClient, LiveTranscriptionEvents } from "@deepgram/sdk";


const deepgram = createClient("{deepgram_api_key}", {
    global: {
      websocket: {
        options: {
          url: "wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/",
          _nodeOnlyHeaders: {
            "cf-aig-authorization": "Bearer {CF_AIG_TOKEN}"
          }
        }
      }
    }
});


const connection = deepgram.listen.live({
    model: "nova-3",
    language: "en-US",
    smart_format: true,
});

connection.send(...);
```
