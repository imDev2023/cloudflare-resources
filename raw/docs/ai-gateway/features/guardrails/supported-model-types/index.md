---
description: Review which AI model types AI Gateway Guardrails evaluates for text generation, embeddings, and unknown models.
title: Supported model types
image: https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/og.png?v=229bda1a6dff72be
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Supported model types

Last updated Aug 27, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway's Guardrails detects the type of AI model being used and applies safety checks accordingly:

- **Text generation models**: Both prompts and responses are evaluated.
- **Embedding models**: Only the prompt is evaluated, as the response consists of numerical embeddings, which are not meaningful for moderation.
- **Unknown models**: If AI Gateway cannot determine the model type, it evaluates only the prompt and bypasses Guardrails for the response.

Note

Guardrails does not support streaming (`stream: true`) requests. For more information, refer to [Streaming behavior](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/#streaming-behavior).
