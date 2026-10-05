---
description: AI Search adds six Workers AI models for text generation.
title: New Workers AI text generation models in AI Search
image: https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/og.png?v=33d3cd6a2d044a5c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## New Workers AI text generation models in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports six additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models for text generation:

| Model | Context window (tokens) |
| --- | --- |
| `@cf/deepseek-ai/deepseek-v4-flash-0731` | 1,048,576 |
| `@cf/deepseek-ai/deepseek-v4-pro-0813` | 1,048,576 |
| `@cf/openai/gpt-oss-120b` | 128,000 |
| `@cf/openai/gpt-oss-20b` | 128,000 |
| `@cf/qwen/qwen3.8-27b` | 262,144 |
| `@cf/moonshotai/kimi-k2.7-code` | 262,144 |

These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/#page","headline":"New Workers AI text generation models in AI Search","description":"AI Search adds six Workers AI models for text generation.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/og.png?v=33d3cd6a2d044a5c","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
