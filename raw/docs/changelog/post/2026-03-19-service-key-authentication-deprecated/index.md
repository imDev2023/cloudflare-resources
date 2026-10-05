---
description: Service Key authentication for the Cloudflare API is deprecated and will be removed on September 30, 2026. Migrate to API Tokens.
title: Service Key authentication deprecated
image: https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/og.png?v=9a0a07dcc0b03d26
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 19, 2026

## Service Key authentication deprecated

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.

[API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) replace Service Keys with fine-grained permissions, expiration, and revocation.

#### What you need to do

Replace any use of the `X-Auth-User-Service-Key` header with an [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) scoped to the permissions your integration requires.

If you use `cloudflared`, update to a version from November 2022 or later. These versions already use API Tokens.

If you use [origin-ca-issuer ↗︎](https://github.com/cloudflare/origin-ca-issuer), update to a version that supports API Token authentication.

For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/#page","headline":"Service Key authentication deprecated","description":"Service Key authentication for the Cloudflare API is deprecated and will be removed on September 30, 2026. Migrate to API Tokens.","url":"https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/og.png?v=9a0a07dcc0b03d26","dateModified":"2026-03-19","datePublished":"2026-03-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
