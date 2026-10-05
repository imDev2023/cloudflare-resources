---
description: Fail synchronous inference requests when capacity is unavailable.
title: Reject busy requests
image: https://developers.cloudflare.com/workers-ai/features/reject-if-busy/og.png?v=bb6cf5fefc74a740
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers-ai/llms.txt  
> Use this file to discover all available pages before exploring further.

# Reject busy requests

Last updated Sep 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/features/reject-if-busy/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Set `rejectIfBusy` when your application should not wait in a capacity queue. Workers AI rejects the synchronous inference request if capacity is unavailable.

## Send a REST request

For the native REST API, add `rejectIfBusy` to the request `options` object:

```bash
curl --request POST \
  --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "messages": [
      {
        "role": "user",
        "content": "Explain what a capacity queue is."
      }
    ],
    "options": {
      "rejectIfBusy": true
    }
  }'
```

## Use the Workers binding

For the Workers AI binding, pass `rejectIfBusy` in the third argument to `env.AI.run()`:

```js
const response = await env.AI.run(
	"@cf/google/gemma-4-26b-a4b-it",
	{
		messages: [
			{
				role: "user",
				content: "Explain what a capacity queue is.",
			},
		],
	},
	{ rejectIfBusy: true },
);
```

```ts
const response = await env.AI.run(
	"@cf/google/gemma-4-26b-a4b-it",
	{
		messages: [
			{
				role: "user",
				content: "Explain what a capacity queue is.",
			},
		],
	},
	{ rejectIfBusy: true },
);
```

Do not add `rejectIfBusy` to the model input object. The binding only applies this option from the third argument.

## Call Chat Completions

For OpenAI-compatible Chat Completions, add `options` at the top level of the request body:

```bash
curl --request POST \
  --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/v1/chat/completions" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "@cf/google/gemma-4-26b-a4b-it",
    "messages": [
      {
        "role": "user",
        "content": "Explain what a capacity queue is."
      }
    ],
    "options": {
      "rejectIfBusy": true
    }
  }'
```

OpenAI clients that preserve custom fields can send this option. Clients that remove unknown fields do not apply it, so requests proceed normally.

## Handle capacity errors

Rejected requests return HTTP status `429` and internal error code `3040`. The error message is `Capacity temporarily exceeded, please try again.`

Refer to [Workers AI errors](https://developers.cloudflare.com/workers-ai/platform/errors/) for error details.
