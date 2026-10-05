---
description: Keep the previous service token secret active while you deploy its replacement.
title: Grace periods for service token rotation
image: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/og.png?v=a6719cefca8c3bf9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## Grace periods for service token rotation

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.

The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.

For configuration instructions, refer to [Rotate service token secrets](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/#page","headline":"Grace periods for service token rotation","description":"Keep the previous service token secret active while you deploy its replacement.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/og.png?v=a6719cefca8c3bf9","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
