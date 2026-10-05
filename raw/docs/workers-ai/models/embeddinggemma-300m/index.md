---
description: EmbeddingGemma is a 300M parameter, state-of-the-art for its size, open embedding model from Google, built from Gemma 3 (with T5Gemma initialization) and the same research and technology used to create Gemini models. EmbeddingGemma produces vector representations of text, making it well-suited for search and retrieval tasks, including classification, clustering, and semantic similarity search. This model was trained with data in 100+ spoken languages.
title: embeddinggemma-300m
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# embeddinggemma-300m

Beta

Text Embeddings • Google

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/google/embeddinggemma-300m`

- Cloudflare-hosted

EmbeddingGemma is a 300M parameter, state-of-the-art for its size, open embedding model from Google, built from Gemma 3 (with T5Gemma initialization) and the same research and technology used to create Gemini models. EmbeddingGemma produces vector representations of text, making it well-suited for search and retrieval tasks, including classification, clustering, and semantic similarity search. This model was trained with data in 100+ spoken languages.

| Model Info | |
| --- | --- |
| Beta | Yes |

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
      "@cf/google/embeddinggemma-300m",
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
  f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-300m",
  headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
  json={"text": stories}
)

print(response.json())
```

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/google/embeddinggemma-300m  \
  -X POST  \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
  -d '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'
```

OpenAI compatible endpoints

Workers AI also supports OpenAI compatible API endpoints for `/v1/chat/completions` and `/v1/embeddings`. For more details, refer to [Configurations](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

## Parameters

▶text

`one of`required

▶shape\[]

`array`

▶data\[]

`array`Embeddings of the requested text values

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/schema-input.json) [Download](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/schema-input.json)

Output [Open](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/schema-output.json) [Download](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/schema-output.json)
