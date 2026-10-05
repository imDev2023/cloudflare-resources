---
description: Reference for the runWithTools and autoTrimTools methods in embedded function calling.
title: API Reference
image: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/og.png?v=b717d7f8d4ddf28e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers-ai/llms.txt  
> Use this file to discover all available pages before exploring further.

# API Reference

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Learn more about the API reference for [embedded function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded).

## runWithTools

This wrapper method enables you to do embedded function calling. You pass it the AI binding, model, inputs (`messages` array and `tools` array), and optional configurations.

- `AI Binding`Ai
  - The AI binding, such as `env.AI`.
- `model`BaseAiTextGenerationModels
  - The ID of the model that supports function calling. For example, `@hf/nousresearch/hermes-2-pro-mistral-7b`.
- `input`Object
  - `messages`RoleScopedChatInput\[]
  - `tools`AiTextGenerationToolInputWithFunction\[]
- `config`Object
  - `streamFinalResponse`boolean optional
  - `maxRecursiveToolRuns`number optional
  - `strictValidation`boolean optional
  - `verbose`boolean optional
  - `trimFunction`boolean optional - For the `trimFunction`, you can pass it `autoTrimTools`, which is another helper method we've devised to automatically choose the correct tools (using an LLM) before sending it off for inference. This means that your final inference call will have fewer input tokens.

## createToolsFromOpenAPISpec

This method lets you automatically create tool schemas based on OpenAPI specs, so you don't have to manually write or hardcode the tool schemas. You can pass the OpenAPI spec for any API in JSON or YAML format.

`createToolsFromOpenAPISpec` has a config input that allows you to perform overrides if you need to provide headers like Authentication or User-Agent.

- `spec`string
  - The OpenAPI specification in either JSON or YAML format, or a URL to a remote OpenAPI specification.
- `config`Config optional - Configuration options for the createToolsFromOpenAPISpec function
  - `overrides`ConfigRule\[] optional
  - `matchPatterns`RegExp\[] optional
  - `options` Object optional { `verbose` boolean optional }
