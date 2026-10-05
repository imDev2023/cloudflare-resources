---
description: Track file indexing, search activity, and top retrievals to understand how your AutoRAG instance is being used.
title: New Metrics View in AutoRAG
image: https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/og.png?v=c320cf419926f231
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 19, 2025

## New Metrics View in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AutoRAG](https://developers.cloudflare.com/ai-search/) now includes a **Metrics** tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between `ai-search` and `search`, and see which files are retrieved most often.

![Metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2062,height=1765,format=webp/_astro/metrics.BBUwKIos.png)

You can find these metrics within each AutoRAG instance:

- Indexing: Track how files are ingested and see status changes over time.
- Search breakdown: Compare usage between `ai-search` and `search` endpoints.
- Top file retrievals: Identify which files are most frequently retrieved in a given period.

Try it today in [AutoRAG](https://developers.cloudflare.com/ai-search/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/#page","headline":"New Metrics View in AutoRAG","description":"Track file indexing, search activity, and top retrievals to understand how your AutoRAG instance is being used.","url":"https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/og.png?v=c320cf419926f231","dateModified":"2025-09-19","datePublished":"2025-09-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
