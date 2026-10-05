---
description: GLM-5.3 Flash is now available on Workers AI, a 320B MoE model with vision, reasoning, and function calling.
title: Z.ai GLM-5.3 Flash now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/og.png?v=5fac8ad624908f6f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## Z.ai GLM-5.3 Flash now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/zai-org/glm-5.3-flash`](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.

GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3 Flash requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 Flash through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/#page","headline":"Z.ai GLM-5.3 Flash now available on Workers AI","description":"GLM-5.3 Flash is now available on Workers AI, a 320B MoE model with vision, reasoning, and function calling.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/og.png?v=5fac8ad624908f6f","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
