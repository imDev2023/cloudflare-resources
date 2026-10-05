---
description: Disable or delete service tokens that have not authenticated for a specified period.
title: Automatically manage inactive Access service tokens
image: https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/og.png?v=7d40c78b24edf476
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2026

## Automatically manage inactive Access service tokens

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit.

To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule. Cleanup runs gradually in the background, so eligible tokens may not be disabled or deleted immediately.

For configuration instructions, refer to [Manage inactive service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#manage-inactive-service-tokens).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/#page","headline":"Automatically manage inactive Access service tokens","description":"Disable or delete service tokens that have not authenticated for a specified period.","url":"https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/og.png?v=7d40c78b24edf476","dateModified":"2026-09-22","datePublished":"2026-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
