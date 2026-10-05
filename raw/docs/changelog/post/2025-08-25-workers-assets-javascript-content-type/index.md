---
description: Updated JavaScript asset responses to use the standardized text/javascript Content-Type header (previously `application/javascript`) for better alignment with the HTML spec and browser expectations.
title: Content type returned in Workers Assets for Javascript files is now `text/javascript`
image: https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/og.png?v=bf133a86d86d8b7a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2025

## Content type returned in Workers Assets for Javascript files is now \`text/javascript\`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

JavaScript asset responses have been updated to use the `text/javascript` Content-Type header instead of `application/javascript`. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends `text/javascript` as the preferred type going forward.

This change improves:

- Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.
- Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.
- Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.
- Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.

Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.

Users will see this change on the next deployment of their assets.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/#page","headline":"Content type returned in Workers Assets for Javascript files is now `text/javascript`","description":"Updated JavaScript asset responses to use the standardized text/javascript Content-Type header (previously application/javascript) for better alignment with the HTML spec and browser expectations.","url":"https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/og.png?v=bf133a86d86d8b7a","dateModified":"2025-08-25","datePublished":"2025-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
