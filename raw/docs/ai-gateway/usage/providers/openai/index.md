---
description: Route OpenAI API requests through AI Gateway for observability and control.
title: OpenAI
image: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/og.png?v=95bdf250d8970561
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# OpenAI

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[OpenAI ↗︎](https://openai.com/about/) helps you build with GPT models.

## Endpoint

**Base URL**

```plaintext
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai
```

When making requests to OpenAI, replace `https://api.openai.com/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai`.

**Chat completions endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions`

**Responses endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses`

## Examples

### OpenAI SDK

<details>

<summary>

With Key in Request

</summary>

```js
import OpenAI from "openai";

const client = new OpenAI({
	apiKey: "YOUR_OPENAI_API_KEY",
	defaultHeaders: {
		"cf-aig-authorization": `Bearer {cf_api_token}`,
	},
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
});

const response = await client.chat.completions.create({
	model: "gpt-4o-mini",
	messages: [{ role: "user", content: "Hello, world!" }],
});
```

```js
import OpenAI from "openai";

const client = new OpenAI({
	apiKey: "YOUR_OPENAI_API_KEY",
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
});

const response = await client.chat.completions.create({
	model: "gpt-4o-mini",
	messages: [{ role: "user", content: "Hello, world!" }],
});
```

</details>

<details>

<summary>

With Stored Keys (BYOK) / Unified Billing

</summary>

```js
import OpenAI from "openai";

const client = new OpenAI({
	apiKey: "{cf_api_token}",
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
});

// Ensure your OpenAI API key is stored with BYOK
// or Unified Billing has credits
const response = await client.chat.completions.create({
	model: "gpt-4o-mini",
	messages: [{ role: "user", content: "Hello, world!" }],
});
```

</details>

### cURL

<details>

<summary>

Responses API with API Key in Request

</summary>

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
  --header 'Authorization: Bearer {OPENAI_API_KEY}' \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
  	"model": "gpt-5.1",
  	"input": [
    	{
      	"role": "user",
      	"content": "Write a one-sentence bedtime story about a unicorn."
    	}
  	]
  }'
```

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
  --header 'Authorization: Bearer {OPENAI_API_KEY}' \
  --header 'Content-Type: application/json' \
  --data '{
  	"model": "gpt-5.1",
  	"input": [
    	{
      	"role": "user",
      	"content": "Write a one-sentence bedtime story about a unicorn."
    	}
  	]
  }'
```

</details>

<details>

<summary>

Chat Completions with API Key in Request

</summary>

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
  --header 'Authorization: Bearer {OPENAI_API_KEY}' \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
  --header 'Authorization: Bearer {OPENAI_API_KEY}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```

</details>

<details>

<summary>

Responses API with Stored Keys (BYOK) / Unified Billing

</summary>

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
  	"model": "gpt-5.1",
  	"input": [
    	{
      	"role": "user",
      	"content": "Write a one-sentence bedtime story about a unicorn."
    	}
  	]
  }'
```

</details>

<details>

<summary>

Chat Completions with Stored Keys (BYOK) / Unified Billing

</summary>

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```

</details>
