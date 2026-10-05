---
description: Route Cerebras inference requests through AI Gateway for observability and control.
title: Cerebras
image: https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/og.png?v=e1b603a5cdfec73a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cerebras

Last updated Aug 18, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cerebras ↗︎](https://inference-docs.cerebras.ai/) offers developers a low-latency solution for AI model inference.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras
```

## Prerequisites

When making requests to Cerebras, ensure you have the following:

- Your AI Gateway Account ID.
- Your AI Gateway gateway name.
- An active Cerebras API token.
- The name of the Cerebras model you want to use.

## Examples

### cURL

*Example fetch requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer CEREBRAS_TOKEN' \
 --data '{
    "model": "gpt-oss-120b",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

## OpenAI-Compatible Endpoint

You can also access Cerebras models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:

```txt
https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions
```

Specify:

```json
{
"model": "cerebras/{model}"
}
```
