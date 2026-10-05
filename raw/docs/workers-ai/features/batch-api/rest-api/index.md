---
description: Send and retrieve batch inference requests using the Workers AI REST API.
title: REST API
image: https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/og.png?v=5b1fb19ca805e26f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers-ai/llms.txt  
> Use this file to discover all available pages before exploring further.

# REST API

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you prefer to work directly with the REST API instead of a [Cloudflare Worker](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/), below are the steps on how to do it:

## 1. Sending a Batch Request

Make a POST request using the following pattern. You can pass `external_reference` as a unique ID per-request that will be returned in the response.

*Sending a batch requestbash*

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/baai/bge-m3?queueRequest=true" \
 --header "Authorization: Bearer $API_TOKEN" \
 --header 'Content-Type: application/json' \
 --json '{
    "requests": [
        {
            "query": "This is a story about Cloudflare",
            "contexts": [
                {
                    "text": "This is a story about an orange cloud"
                },
                {
                    "text": "This is a story about a llama"
                },
                {
                    "text": "This is a story about a hugging emoji"
                }
            ],
            "external_reference": "reference-1"
        }
    ]
  }'
```

```json
{
	"result": {
		"status": "queued",
		"request_id": "768f15b7-4fd6-4498-906e-ad94ffc7f8d2",
		"model": "@cf/baai/bge-m3"
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

## 2. Retrieving the Batch Response

After receiving a `request_id` from your initial POST, you can poll for or retrieve the results with another POST request:

*Retrieving a responsebash*

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/baai/bge-m3?queueRequest=true" \
 --header "Authorization: Bearer $API_TOKEN" \
 --header 'Content-Type: application/json' \
 --json '{
    "request_id": "<uuid>"
  }'
```

```json
{
	"result": {
		"responses": [
			{
				"id": 0,
				"result": {
					"response": [
						{ "id": 0, "score": 0.73974609375 },
						{ "id": 1, "score": 0.642578125 },
						{ "id": 2, "score": 0.6220703125 }
					]
				},
				"success": true,
				"external_reference": "reference-1"
			}
		],
		"usage": { "prompt_tokens": 12, "completion_tokens": 0, "total_tokens": 12 }
	},
	"success": true,
	"errors": [],
	"messages": []
}
```
