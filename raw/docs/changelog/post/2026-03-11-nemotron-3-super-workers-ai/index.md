---
description: A hybrid MoE model with 120B total parameters and 12B active, optimized for multi-agent and agentic AI workloads.
title: NVIDIA Nemotron 3 Super now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/og.png?v=18a263618381158b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 11, 2026

## NVIDIA Nemotron 3 Super now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to partner with NVIDIA to bring [`@cf/nvidia/nemotron-3-120b-a12b`](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/) to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.

The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.

**Key capabilities:**

- **Hybrid Mamba-transformer architecture** delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications
- **Tool calling** support for building AI agents that invoke tools across multiple conversation turns
- **Multi-Token Prediction (MTP)** accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass
- **32,000 token context window** for retaining conversation history and plan states across multi-step agent workflows

Prompt caching

For optimal performance with multi-turn conversations, send the `x-session-affinity` header with a unique session identifier to enable prompt caching. This routes requests to the same model instance, reducing latency and inference costs. For details, refer to [Prompt caching](https://developers.cloudflare.com/workers-ai/features/prompt-caching/).

Use Nemotron 3 Super through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

For more information, refer to the [Nemotron 3 Super model page](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/#page","headline":"NVIDIA Nemotron 3 Super now available on Workers AI","description":"A hybrid MoE model with 120B total parameters and 12B active, optimized for multi-agent and agentic AI workloads.","url":"https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/og.png?v=18a263618381158b","dateModified":"2026-03-11","datePublished":"2026-03-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
