---
description: Route Azure OpenAI requests through AI Gateway for observability and control.
title: Azure OpenAI
image: https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/og.png?v=8e2c7a0520ad1a06
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Azure OpenAI

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Azure OpenAI ↗︎](https://azure.microsoft.com/en-gb/products/ai-services/openai-service/) allows you apply natural language algorithms on your data.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}
```

## Prerequisites

When making requests to Azure OpenAI, you will need:

- AI Gateway account ID
- AI Gateway gateway name
- Azure OpenAI API key
- Azure OpenAI resource name
- Azure OpenAI deployment name (aka model name)

## URL structure

Your new base URL will use the data above in this structure: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}`. Then, you can append your endpoint and api-version at the end of the base URL, like `.../chat/completions?api-version=2023-05-15`.

## Examples

### cURL

*Example fetch requestbash*

```bash
curl 'https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/{deployment_name}/chat/completions?api-version=2023-05-15' \
  --header 'Content-Type: application/json' \
  --header 'api-key: {azure_api_key}' \
  --data '{
  "messages": [
    {
      "role": "user",
      "content": "What is Cloudflare?"
    }
  ]
}'
```

### Use `openai` JavaScript SDK

*JavaScriptjs*

```js
import { AzureOpenAI } from "openai";

const azure_openai = new AzureOpenAI({
  apiKey: "{azure_api_key}",
  baseURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/`,
  apiVersion: "2023-05-15",
  defaultHeaders: { "cf-aig-authorization": "{cf-api-token}" }, // if authenticated
});

const result = await azure_openai.chat.completions.create({
  model: '{deployment_name}',
  messages: [{ role: "user", content: "Hello" }],
});
```
