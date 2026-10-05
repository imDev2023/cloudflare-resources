---
description: Distilled BERT model that was finetuned on SST-2 for sentiment classification
title: distilbert-sst-2-int8
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![HuggingFace logo](https://developers.cloudflare.com/_astro/huggingface.DMS-v5TA.svg)

# distilbert-sst-2-int8

Text Classification • HuggingFace

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/huggingface/distilbert-sst-2-int8/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/huggingface/distilbert-sst-2-int8`

- Cloudflare-hosted

Distilled BERT model that was finetuned on SST-2 for sentiment classification

| Model Info | |
| --- | --- |
| More information | [link ↗](https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static) |
| Unit Pricing | $0.0263 per M input tokens |

## Usage

```ts
export interface Env {
  AI: Ai;
}

export default {
  async fetch(request, env): Promise<Response> {

    const response = await env.AI.run(
      "@cf/huggingface/distilbert-sst-2-int8",
      {
        text: "This pizza is great!",
      }
    );

    return Response.json(response);
  },
} satisfies ExportedHandler<Env>;
```

```py
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
headers = {"Authorization": "Bearer {API_KEY}"}

def run(model, input):
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

output = run("@cf/huggingface/distilbert-sst-2-int8", { "text": "This pizza is great!" })
print(output)
```

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/huggingface/distilbert-sst-2-int8  \
  -X POST  \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
  -d '{ "text": "This pizza is great!" }'
```

## Parameters

text

`string`requiredminLength: 1The text that you want to classify

type

`array`

contentType

`application/json`

description

`An array of classification results for the input text`

items

`[object Object]`

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/@cf/huggingface/distilbert-sst-2-int8/schema-output.json)
