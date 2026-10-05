---
description: Kimi K2.6 is now available on Workers AI, bringing a 1T parameter MoE model with 32B active parameters, 262.1k context window, vision, and agentic capabilities to the Cloudflare Developer Platform.
title: Moonshot AI Kimi K2.6 now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/og.png?v=a5a88c2dcd1c6a34
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 20, 2026

## Moonshot AI Kimi K2.6 now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.

Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).

#### Key capabilities

- **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
- **Long-horizon coding** with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python
- **Coding-driven design** that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows
- **Agent swarm orchestration** scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks
- **Vision inputs** for processing images alongside text
- **Thinking mode** with configurable reasoning depth
- **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns

#### Differences from Kimi K2.5

If you are migrating from Kimi K2.5, note the following API changes:

- K2.6 uses `chat_template_kwargs.thinking` to control reasoning, replacing `chat_template_kwargs.enable_thinking`
- K2.6 returns reasoning content in the `reasoning` field, replacing `reasoning_content`

#### Get started

Use Kimi K2.6 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.6 model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/#page","headline":"Moonshot AI Kimi K2.6 now available on Workers AI","description":"Kimi K2.6 is now available on Workers AI, bringing a 1T parameter MoE model with 32B active parameters, 262.1k context window, vision, and agentic capabilities to the Cloudflare Developer Platform.","url":"https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/og.png?v=a5a88c2dcd1c6a34","dateModified":"2026-04-20","datePublished":"2026-04-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
