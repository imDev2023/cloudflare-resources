---
description: Quickly create and save multiple Brand Protection queries via API.
title: Save time with bulk query creation in Brand Protection
image: https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/og.png?v=bc073da937dea6fc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 15, 2025

## Save time with bulk query creation in Brand Protection

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Brand Protection](https://developers.cloudflare.com/security-center/brand-protection/) detects domains that may be impersonating your brand — from common misspellings (`cloudfalre.com`) to malicious concatenations (`cloudflare-okta.com`). Saved search queries run continuously and alert you when suspicious domains appear.

You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the [Brand Protection bulk query creation API](https://developers.cloudflare.com/api/resources/brand_protection/subresources/queries/methods/bulk/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/#page","headline":"Save time with bulk query creation in Brand Protection","description":"Quickly create and save multiple Brand Protection queries via API.","url":"https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/og.png?v=bc073da937dea6fc","dateModified":"2025-08-15","datePublished":"2025-08-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
