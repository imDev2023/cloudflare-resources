---
description: Configure up to 32 token configurations per zone, with up to 16 keys in each configuration.
title: Increased limits for JWT validation configurations
image: https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/og.png?v=36120e6ec99489b0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 27, 2026

## Increased limits for JWT validation configurations

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports 32 token configurations per zone by default. Each token configuration can contain up to 16 keys.

These increased limits support more JWT configurations and provide additional capacity for key rotation.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) for configuration details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/#page","headline":"Increased limits for JWT validation configurations","description":"Configure up to 32 token configurations per zone, with up to 16 keys in each configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/og.png?v=36120e6ec99489b0","dateModified":"2026-08-27","datePublished":"2026-08-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
