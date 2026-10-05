---
description: Route Mistral AI requests through AI Gateway for observability and control.
title: Mistral AI
image: https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/og.png?v=4b72964726904a56
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Mistral AI

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Mistral AI ↗︎](https://mistral.ai) helps you build quickly with Mistral's advanced AI models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral
```

## Prerequisites

When making requests to the Mistral AI, you will need:

- AI Gateway Account ID
- AI Gateway gateway name
- Mistral AI API token
- Mistral AI model name

## URL structure

Your new base URL will use the data above in this structure: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/`.

Then you can append the endpoint you want to hit, for example: `v1/chat/completions`

So your final URL will come together as: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions`.

## Examples

### cURL

*Example fetch requestbash*

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer MISTRAL_TOKEN' \
 --data '{
    "model": "mistral-large-latest",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

### Use `@mistralai/mistralai` package with JavaScript

If you are using the `@mistralai/mistralai` package, you can set your endpoint like this:

*JavaScript examplejs*

```js
import { Mistral } from "@mistralai/mistralai";

const client = new Mistral({
	apiKey: MISTRAL_TOKEN,
	serverURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral`,
});

await client.chat.create({
	model: "mistral-large-latest",
	messages: [
		{
			role: "user",
			content: "What is Cloudflare?",
		},
	],
});
```

## OpenAI-Compatible Endpoint

You can also access Mistral models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:

```txt
https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions
```

Specify:

```json
{
"model": "mistral/{model}"
}
```
