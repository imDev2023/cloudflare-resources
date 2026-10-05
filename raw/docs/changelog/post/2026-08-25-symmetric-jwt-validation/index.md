---
description: Validate JSON Web Tokens signed with HS256, HS384, or HS512 symmetric keys.
title: Symmetric key support for JWT validation
image: https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/og.png?v=39970e07740e5b70
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## Symmetric key support for JWT validation

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports symmetric keys that use the `HS256`, `HS384`, and `HS512` algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.

Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#credentials) for supported key formats and credential requirements.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/#page","headline":"Symmetric key support for JWT validation","description":"Validate JSON Web Tokens signed with HS256, HS384, or HS512 symmetric keys.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/og.png?v=39970e07740e5b70","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
