---
description: New browser support detection for PQ encryption on Radar
title: Browser Support Detection for PQ Encryption on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/og.png?v=b2de3a6f3513ab11
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 6, 2025

## Browser Support Detection for PQ Encryption on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes browser detection for Post-quantum (PQ) encryption. The [Post-quantum encryption card ↗︎](https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption) now checks whether a user’s browser supports post-quantum encryption. If support is detected, information about the key agreement in use is displayed.

![Screenshot of the PQ encryption browser support test on the Adoption \& Usage page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=872,height=109,format=webp/_astro/pq-encryption-test.gx_uoaMX.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/#page","headline":"Browser Support Detection for PQ Encryption on Cloudflare Radar","description":"New browser support detection for PQ encryption on Radar","url":"https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/og.png?v=b2de3a6f3513ab11","dateModified":"2025-10-06","datePublished":"2025-10-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
