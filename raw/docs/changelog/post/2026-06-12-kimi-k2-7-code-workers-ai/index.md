---
description: Kimi K2.7 Code is now available on Workers AI, a code-optimized 1T MoE model with 262.1k context, vision, and agentic capabilities.
title: Moonshot AI Kimi K2.7 Code now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/og.png?v=2e4695d90206dd87
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 12, 2026

## Moonshot AI Kimi K2.7 Code now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.

#### Improved coding and agent performance

K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:

- **+21.8%** on Kimi Code Bench v2
- **+11.0%** on Program Bench
- **+31.5%** on MLS Bench Lite

#### Reasoning efficiency

K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.

#### Key capabilities

- **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
- **Long-horizon coding** with improved instruction following and higher end-to-end coding task success rates
- **Vision inputs** for processing images alongside text
- **Thinking mode** with configurable reasoning depth via `chat_template_kwargs.thinking`
- **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns
- **Structured outputs** with JSON schema support

#### Differences from Kimi K2.6

If you are migrating from Kimi K2.6, note the following:

- K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency
- Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)
- API usage is identical — no parameter changes required

#### Get started

Use Kimi K2.7 Code through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.7 Code model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/#page","headline":"Moonshot AI Kimi K2.7 Code now available on Workers AI","description":"Kimi K2.7 Code is now available on Workers AI, a code-optimized 1T MoE model with 262.1k context, vision, and agentic capabilities.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/og.png?v=2e4695d90206dd87","dateModified":"2026-06-12","datePublished":"2026-06-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
