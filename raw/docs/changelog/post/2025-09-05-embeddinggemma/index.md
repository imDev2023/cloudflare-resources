---
description: Partnering with Google to bring to you EmbeddingGemma best-in-class embedding performance for RAG and semantic search
title: Introducing EmbeddingGemma from Google on Workers AI
image: https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/og.png?v=e38f665e7b57d1bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 5, 2025

## Introducing EmbeddingGemma from Google on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to be a launch partner alongside [Google ↗︎](https://developers.googleblog.com/en/introducing-embeddinggemma/) to bring their newest embedding model, **EmbeddingGemma**, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.

[`@cf/google/embeddinggemma-300m`](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/) is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.

**Using EmbeddingGemma in AI Search:** Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.

To use EmbeddingGemma for your AI Search projects:

1. Go to **Create** in the [AI Search dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
2. Follow the setup flow for your new RAG instance
3. In the **Generate Index** step, open up **More embedding models** and select `@cf/google/embeddinggemma-300m` as your embedding model
4. Complete the setup to create an AI Search

Try it out and let us know what you think!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/#page","headline":"Introducing EmbeddingGemma from Google on Workers AI","description":"Partnering with Google to bring to you EmbeddingGemma best-in-class embedding performance for RAG and semantic search","url":"https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/og.png?v=e38f665e7b57d1bb","dateModified":"2025-09-05","datePublished":"2025-09-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
