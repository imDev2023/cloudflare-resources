---
description: Worker startup time limit has been increased from 400 ms to 1s
title: Worker startup time limit increased to 1 second
image: https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/og.png?v=7ceba3898fcf9ddb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 10, 2025

## Worker startup time limit increased to 1 second

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.

This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.

For more information, see the documentation on [Workers startup limits](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/#page","headline":"Worker startup time limit increased to 1 second","description":"Worker startup time limit has been increased from 400 ms to 1s","url":"https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/og.png?v=7ceba3898fcf9ddb","dateModified":"2025-10-10","datePublished":"2025-10-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
