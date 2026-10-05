---
description: Workers Builds now skips a queued build when a newer build for the same build trigger is queued.
title: Workers Builds now skips superseded queued builds
image: https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/og.png?v=deb9d404ff063654
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 24, 2026

## Workers Builds now skips superseded queued builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Builds now automatically skips a queued build when a newer build for the same build trigger is also queued.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/#page","headline":"Workers Builds now skips superseded queued builds","description":"Workers Builds now skips a queued build when a newer build for the same build trigger is queued.","url":"https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/og.png?v=deb9d404ff063654","dateModified":"2026-07-24","datePublished":"2026-07-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
