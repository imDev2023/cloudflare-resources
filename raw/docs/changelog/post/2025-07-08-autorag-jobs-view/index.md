---
description: Track your indexing pipeline in real time with 3–5× faster indexing and a new Jobs dashboard.
title: Faster indexing and new Jobs view in AutoRAG
image: https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/og.png?v=079c49e5d78b7106
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2025

## Faster indexing and new Jobs view in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now expect **3-5× faster indexing** in AutoRAG, and with it, a brand new **Jobs view** to help you monitor indexing progress.

With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the [Sync API](https://developers.cloudflare.com/api/resources/ai-search/subresources/rags/) or by clicking “Sync index” in the dashboard.

With the new jobs observability, you can now:

- View the status, job ID, source, start time, duration and last sync time for each indexing job
- Inspect real-time logs of job events (e.g. `Starting indexing data source...`)
- See a history of past indexing jobs under the Jobs tab of your AutoRAG

This makes it easier to understand what’s happening behind the scenes.

**Coming soon:** We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.

Try it out today on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/autorag).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/#page","headline":"Faster indexing and new Jobs view in AutoRAG","description":"Track your indexing pipeline in real time with 3–5× faster indexing and a new Jobs dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/og.png?v=079c49e5d78b7106","dateModified":"2025-07-08","datePublished":"2025-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
