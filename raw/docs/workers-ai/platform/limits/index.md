---
description: Rate limits for Workers AI inference requests, organized by task type and model.
title: Limits
image: https://developers.cloudflare.com/workers-ai/platform/limits/og.png?v=f48e357380e3ed94
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers-ai/llms.txt  
> Use this file to discover all available pages before exploring further.

# Limits

Last updated Sep 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/platform/limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI is now Generally Available. We've updated our rate limits to reflect this.

Note that model inferences in local mode using Wrangler will also count towards these limits. Beta models may have lower rate limits while we work on performance and scale.

Custom requirements

If you have custom requirements like private custom models or higher limits, complete the [Custom Requirements Form ↗︎](https://forms.gle/axnnpGDb6xrmR31T6). Cloudflare will contact you with next steps.

Rate limits are default per task type, with some per-model limits defined as follows:

## Rate limits by task type

### [Automatic Speech Recognition](https://developers.cloudflare.com/workers-ai/models/)

- 720 requests per minute

### [Image Classification](https://developers.cloudflare.com/workers-ai/models/)

- 3000 requests per minute

### [Image-to-Text](https://developers.cloudflare.com/workers-ai/models/)

- 720 requests per minute

### [Object Detection](https://developers.cloudflare.com/workers-ai/models/)

- 3000 requests per minute

### [Summarization](https://developers.cloudflare.com/workers-ai/models/)

- 1500 requests per minute

### [Text Classification](https://developers.cloudflare.com/workers-ai/models/)

- 2000 requests per minute

### [Text Embeddings](https://developers.cloudflare.com/workers-ai/models/)

- 3000 requests per minute
- [@cf/baai/bge-large-en-v1.5](https://developers.cloudflare.com/workers-ai/models/bge-large-en-v1.5/) is 1500 requests per minute

### [Text Generation](https://developers.cloudflare.com/workers-ai/models/)

- 300 requests per minute, unless the model requires the Workers Paid plan

#### Paid models

The following limits apply per account, per model to any model that requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) — each model page states whether it does. These models are the only models that do not receive the default limit:

| Billing | Rate limit |
| --- | --- |
| Standard Workers AI billing | 20 requests per minute |
| Prepaid AI Gateway credits | 50 requests per minute |

To receive the elevated limit, load [prepaid AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing**. These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.

### [Text-to-Image](https://developers.cloudflare.com/workers-ai/models/)

- 720 requests per minute
- [@cf/runwayml/stable-diffusion-v1-5-img2img](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-v1-5-img2img/) is 1500 requests per minute

### [Translation](https://developers.cloudflare.com/workers-ai/models/)

- 720 requests per minute
