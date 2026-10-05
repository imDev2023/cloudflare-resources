---
description: Route DeepSeek API requests through AI Gateway for observability and control.
title: DeepSeek
image: https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/og.png?v=450c9f9ae7710409
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# DeepSeek

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[DeepSeek ↗︎](https://www.deepseek.com/) helps you build quickly with DeepSeek's advanced AI models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek
```

## Prerequisites

When making requests to DeepSeek, ensure you have the following:

- Your AI Gateway Account ID.
- Your AI Gateway gateway name.
- An active DeepSeek AI API token.
- The name of the DeepSeek AI model you want to use.

## URL structure

Your new base URL will use the data above in this structure:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/`.

You can then append the endpoint you want to hit, for example: `chat/completions`.

So your final URL will come together as:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions`.

## Examples

### cURL with a provider key

*Example fetch requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
 --data '{
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

### cURL with stored keys (BYOK)

Store your DeepSeek key with [bring your own keys (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Then omit the `Authorization` header so AI Gateway can substitute the stored key:

*Example BYOK requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
 --header 'content-type: application/json' \
 --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
 --data '{
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

### Use DeepSeek with JavaScript

If you are using the OpenAI SDK, you can set your endpoint like this:

*JavaScriptjs*

```js
import OpenAI from "openai";

const openai = new OpenAI({
	apiKey: env.DEEPSEEK_TOKEN,
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek",
});

try {
	const chatCompletion = await openai.chat.completions.create({
		model: "deepseek-chat",
		messages: [{ role: "user", content: "What is Cloudflare?" }],
	});

	const response = chatCompletion.choices[0].message;

	return new Response(JSON.stringify(response));
} catch (e) {
	return new Response(e);
}
```

## OpenAI-Compatible Endpoint

You can also access DeepSeek models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:

```txt
https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions
```

Specify:

```json
{
"model": "deepseek/{model}"
}
```
