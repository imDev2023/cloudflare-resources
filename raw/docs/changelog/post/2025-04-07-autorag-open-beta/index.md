---
description: AutoRAG lets you create fully-managed, retrieval-augmented generation (RAG) pipelines that continuously updates and scales on Cloudflare.
title: Create fully-managed RAG pipelines for your AI applications with AutoRAG
image: https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/og.png?v=ea520cf7226a1cf5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Create fully-managed RAG pipelines for your AI applications with AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/) [Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AutoRAG](https://developers.cloudflare.com/ai-search/) is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to [R2](https://developers.cloudflare.com/r2/get-started/), and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.

With AutoRAG, you can:

- **Customize your pipeline:** Choose from [Workers AI](https://developers.cloudflare.com/workers-ai) models, configure chunking strategies, edit system prompts, and more.
- **Instant setup:** AutoRAG provisions everything you need from [Vectorize](https://developers.cloudflare.com/vectorize), [AI gateway](https://developers.cloudflare.com/ai-gateway), to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.
- **Keep your index fresh:** AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.
- **Ask questions:** Query your data and receive grounded responses via a [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/) or [API](https://developers.cloudflare.com/ai-search/api/search/rest-api/).

Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.

Get started in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/autorag) or check out the [guide](https://developers.cloudflare.com/ai-search/get-started/) for instructions on how to build your RAG pipeline today.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/#page","headline":"Create fully-managed RAG pipelines for your AI applications with AutoRAG","description":"AutoRAG lets you create fully-managed, retrieval-augmented generation (RAG) pipelines that continuously updates and scales on Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/og.png?v=ea520cf7226a1cf5","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
