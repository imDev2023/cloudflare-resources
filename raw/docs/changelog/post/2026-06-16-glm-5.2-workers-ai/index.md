---
description: Z.ai's flagship agentic coding model is now available on Workers AI
title: Introducing GLM-5.2 on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/og.png?v=ead826ea72e5b165
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2026

## Introducing GLM-5.2 on Workers AI

[Workers](https://developers.cloudflare.com/workers/) [Agents](https://developers.cloudflare.com/agents/) [Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are excited to announce **GLM-5.2** on Workers AI, Z.ai's flagship agentic coding model.

[`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.

**Key features and use cases:**

- **Agentic coding**: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows
- **Large context window**: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future
- **Function calling**: Build agents that invoke tools and APIs across multiple conversation turns
- **Reasoning**: Tackles complex problem-solving and step-by-step reasoning tasks

Use GLM-5.2 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

Pricing is available on the [model page](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/#page","headline":"Introducing GLM-5.2 on Workers AI","description":"Z.ai's flagship agentic coding model is now available on Workers AI","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/og.png?v=ead826ea72e5b165","dateModified":"2026-06-16","datePublished":"2026-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
