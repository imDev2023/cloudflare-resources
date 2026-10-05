---
description: OAuth consent screens now show publisher verification details inline, so users can more easily understand who owns an application before granting access.
title: Improved publisher verification details on OAuth consent screens
image: https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/og.png?v=e5d61eeda30d1b4c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 5, 2026

## Improved publisher verification details on OAuth consent screens

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

OAuth consent screens now display a shield icon with explanatory text beneath the consent screen title. Each shield icon indicates who owns the application and whether its domain ownership is verified.

- **Green filled shield**: Cloudflare owns and manages the application.
- **Blue outlined shield**: A third-party application with verified ownership of its domain.
- **Amber filled shield**: A third-party application without verified ownership of a domain.

Domain verification only confirms that the application owner controls the displayed domain.

For more information, refer to [Authorizing an application](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/#page","headline":"Improved publisher verification details on OAuth consent screens","description":"OAuth consent screens now show publisher verification details inline, so users can more easily understand who owns an application before granting access.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/og.png?v=e5d61eeda30d1b4c","dateModified":"2026-08-05","datePublished":"2026-08-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
