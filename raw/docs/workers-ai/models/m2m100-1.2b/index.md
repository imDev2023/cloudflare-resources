---
description: Multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation
title: m2m100-1.2b
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Meta logo](https://developers.cloudflare.com/_astro/meta.CTzB_ysm.svg)

# m2m100-1.2b

Translation • Meta

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/meta/m2m100-1.2b`

- Cloudflare-hosted
- Batch

Multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://github.com/facebookresearch/fairseq/blob/main/LICENSE) |
| More information | [link ↗](https://github.com/facebookresearch/fairseq/tree/main/examples/m2m_100) |
| Batch | Yes |
| Unit Pricing | $0.342 per M input tokens, $0.342 per M output tokens |

## Usage

```ts
export interface Env {
  AI: Ai;
}

export default {
  async fetch(request, env): Promise<Response> {

    const response = await env.AI.run(
      "@cf/meta/m2m100-1.2b",
      {
        text: "I'll have an order of the moule frites",
        source_lang: "english", // defaults to english
        target_lang: "french",
      }
    );

    return new Response(JSON.stringify(response));
  },
} satisfies ExportedHandler<Env>;
```

```py
import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
headers = {"Authorization": "Bearer {API_TOKEN}"}

def run(model, input):
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

output = run('@cf/meta/m2m100-1.2b', {
  "text": "I'll have an order of the moule frites",
  "source_lang": "english",
  "target_lang": "french"
})

print(output)
```

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/meta/m2m100-1.2b  \
    -X POST  \
    -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
    -d '{ "text": "Ill have an order of the moule frites", "source_lang": "english", "target_lang": "french" }'
```

## Parameters

<details>

<summary>Synchronous — Send a request and receive a complete response</summary>



text

<code>string</code>requiredminLength: 1The text to be translated

source\_lang

<code>string</code>default: enThe language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified

target\_lang

<code>string</code>requiredThe language code to translate the text into (e.g., 'es' for Spanish)

request\_id

<code>string</code>The async request id that can be used to obtain the results.

</details>

<details>

<summary>Batch — Send multiple requests in a single API call</summary>



▶requests\[]

<code>array</code>requiredBatch of the embeddings requests to run using async-queue

request\_id

<code>string</code>The async request id that can be used to obtain the results.

</details>

## API Schemas (Raw)

SynchronousInput [Open](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/sync-input.json) [Download](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/sync-input.json)

SynchronousOutput [Open](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/sync-output.json) [Download](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/sync-output.json)

BatchInput [Open](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/batch-input.json) [Download](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/batch-input.json)

BatchOutput [Open](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/batch-output.json) [Download](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/batch-output.json)
