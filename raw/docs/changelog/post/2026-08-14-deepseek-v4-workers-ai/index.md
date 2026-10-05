---
description: DeepSeek's latest reasoning models are now on Workers AI, the first models on the platform with a full one million token context window.
title: DeepSeek V4 Flash and Pro now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/og.png?v=31f9faee27dea85e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2026

## DeepSeek V4 Flash and Pro now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/deepseek-ai/deepseek-v4-pro-0813`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/) and [`@cf/deepseek-ai/deepseek-v4-flash-0731`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) are now available on Workers AI.

DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full **one million (1,048,576) token context window**. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.

DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.

**Key capabilities:**

- **Reasoning**: Both models support thinking mode for complex, step-by-step problem-solving.
- **Function calling**: Build agents that invoke tools and APIs across multiple conversation turns.
- **Long context**: Both models support a full 1,048,576 token context window.

Both models require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use these models through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [DeepSeek V4 Pro model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/), the [DeepSeek V4 Flash model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/#page","headline":"DeepSeek V4 Flash and Pro now available on Workers AI","description":"DeepSeek's latest reasoning models are now on Workers AI, the first models on the platform with a full one million token context window.","url":"https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/og.png?v=31f9faee27dea85e","dateModified":"2026-08-14","datePublished":"2026-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
