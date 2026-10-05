---
description: Pages now skips a queued build when a newer build for the same project, branch, and deployment target is queued.
title: Pages now skips superseded queued builds
image: https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/og.png?v=c7efe57736e05176
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 11, 2026

## Pages now skips superseded queued builds

[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/#page","headline":"Pages now skips superseded queued builds","description":"Pages now skips a queued build when a newer build for the same project, branch, and deployment target is queued.","url":"https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/og.png?v=c7efe57736e05176","dateModified":"2026-08-11","datePublished":"2026-08-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
