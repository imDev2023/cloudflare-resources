---
description: GLM-5.3 is now available on Workers AI, Z.ai's flagship agentic coding model with a 1M token context window, reasoning, and function calling.
title: Z.ai GLM-5.3 now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/og.png?v=629d145a00dccac8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 28, 2026

## Z.ai GLM-5.3 now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/zai-org/glm-5.3`](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.

GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: [Z.ai reports ↗︎](https://huggingface.co/zai-org/GLM-5.3) a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).

The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.

GLM-5.3 requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/#page","headline":"Z.ai GLM-5.3 now available on Workers AI","description":"GLM-5.3 is now available on Workers AI, Z.ai's flagship agentic coding model with a 1M token context window, reasoning, and function calling.","url":"https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/og.png?v=629d145a00dccac8","dateModified":"2026-08-28","datePublished":"2026-08-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
