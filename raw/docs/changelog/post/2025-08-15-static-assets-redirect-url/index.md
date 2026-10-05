---
description: Corrected handling of double slashes in redirect rule paths
title: "Workers Static Assets: Corrected handling of double slashes in redirect rule paths"
image: https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/og.png?v=2e554a69baebf448
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 15, 2025

## Workers Static Assets: Corrected handling of double slashes in redirect rule paths

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Static Assets](https://developers.cloudflare.com/workers/static-assets/): Fixed a bug in how [redirect rules ↗︎](https://developers.cloudflare.com/workers/static-assets/redirects/) defined in your Worker's `_redirects` file are processed.

If you're serving Static Assets with a `_redirects` file containing a rule like `/ja/* /:splat`, paths with double slashes were previously misinterpreted as external URLs. For example, visiting `/ja//example.com` would incorrectly redirect to `https://example.com` instead of `/example.com` on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: [Cloudflare Pages](https://developers.cloudflare.com/pages/) was not affected by this issue.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/#page","headline":"Workers Static Assets: Corrected handling of double slashes in redirect rule paths","description":"Corrected handling of double slashes in redirect rule paths","url":"https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/og.png?v=2e554a69baebf448","dateModified":"2025-08-15","datePublished":"2025-08-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
