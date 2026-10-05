---
description: AI Search adds four new Workers AI models including GLM, Qwen, and EmbeddingGemma.
title: New Workers AI models for text generation and embedding in AI Search
image: https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/og.png?v=03d86ded88da1593
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2026

## New Workers AI models for text generation and embedding in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports four additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models across text generation and embedding.

#### Text generation

| Model | Context window (tokens) |
| --- | --- |
| `@cf/zai-org/glm-4.7-flash` | 131,072 |
| `@cf/qwen/qwen3-30b-a3b-fp8` | 32,000 |

GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.

#### Embedding

| Model | Vector dims | Input tokens | Metric |
| --- | --- | --- | --- |
| `@cf/qwen/qwen3-embedding-0.6b` | 1,024 | 4,096 | cosine |
| `@cf/google/embeddinggemma-300m` | 768 | 512 | cosine |

Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.

All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/#page","headline":"New Workers AI models for text generation and embedding in AI Search","description":"AI Search adds four new Workers AI models including GLM, Qwen, and EmbeddingGemma.","url":"https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/og.png?v=03d86ded88da1593","dateModified":"2026-04-08","datePublished":"2026-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
