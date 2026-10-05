---
description: Updated Workers AI models with larger context windows
title: Workers AI larger context windows
image: https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/og.png?v=e9dba9dc606b0b73
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2025

## Workers AI larger context windows

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.

This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.

Our [catalog page](https://developers.cloudflare.com/workers-ai/models/) provides more information about each model's supported context window.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/#page","headline":"Workers AI larger context windows","description":"Updated Workers AI models with larger context windows","url":"https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/og.png?v=e9dba9dc606b0b73","dateModified":"2025-02-24","datePublished":"2025-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
