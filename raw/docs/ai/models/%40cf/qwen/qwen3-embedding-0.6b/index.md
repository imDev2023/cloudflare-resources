---
description: "The Qwen3 Embedding model series is the latest proprietary model of the Qwen family, specifically designed for text embedding and ranking tasks. "
title: qwen3-embedding-0.6b
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Qwen logo](https://developers.cloudflare.com/_astro/qwen.ByCZjtXU.svg)

# qwen3-embedding-0.6b

Text Embeddings • Qwen

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/qwen/qwen3-embedding-0.6b/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/qwen/qwen3-embedding-0.6b`

- Cloudflare-hosted

The Qwen3 Embedding model series is the latest proprietary model of the Qwen family, specifically designed for text embedding and ranking tasks.

| Model Info | |
| --- | --- |
| Context Window [ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/) | 8,192 tokens |
| Unit Pricing | $0.0118 per M input tokens |

## Usage

```ts
export interface Env {
  AI: Ai;
}

export default {
  async fetch(request, env): Promise<Response> {

    // Can be a string or array of strings]
    const stories = [
      "This is a story about an orange cloud",
      "This is a story about a llama",
      "This is a story about a hugging emoji",
    ];

    const embeddings = await env.AI.run(
      "@cf/qwen/qwen3-embedding-0.6b",
      {
        text: stories,
      }
    );

    return Response.json(embeddings);
  },
} satisfies ExportedHandler<Env>;
```

```py
import os
import requests


ACCOUNT_ID = "your-account-id"
AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")

stories = [
  'This is a story about an orange cloud',
  'This is a story about a llama',
  'This is a story about a hugging emoji'
]

response = requests.post(
  f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/qwen/qwen3-embedding-0.6b",
  headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
  json={"text": stories}
)

print(response.json())
```

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/qwen/qwen3-embedding-0.6b  \
  -X POST  \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
  -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'
```

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

## Parameters

▶queries

`one of`

instruction

`string`default: Given a web search query, retrieve relevant passages that answer the queryOptional instruction for the task

▶documents

`one of`

▶text

`one of`

▶data\[]

`array`

▶shape\[]

`array`

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-output.json)
