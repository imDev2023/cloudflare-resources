---
description: Direct AI training crawlers to canonical URLs to ensure models train on authoritative content.
title: Introducing Redirects for AI Training
image: https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/og.png?v=1e3ccdedea361572
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 17, 2026

## Introducing Redirects for AI Training

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via **AI Crawl Control** > **Quick Actions**, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.

This feature leverages your existing `<link rel="canonical">` tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.

Refer to the [Redirects for AI Training documentation](https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/#page","headline":"Introducing Redirects for AI Training","description":"Direct AI training crawlers to canonical URLs to ensure models train on authoritative content.","url":"https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/og.png?v=1e3ccdedea361572","dateModified":"2026-04-17","datePublished":"2026-04-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
