---
description: Access logs will now respect the CMB.
title: Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)
image: https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/og.png?v=bdf386521b0c65b1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2025

## Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access logs now support the [Customer Metadata Boundary (CMB)](https://developers.cloudflare.com/data-localization/metadata-boundary/). If you have configured the CMB for your account, all Access logging will respect that configuration.

Note

For EU CMB customers, the logs will not be stored by Access and will appear as empty in the dashboard. EU CMB customers should utilize [Logpush](https://developers.cloudflare.com/logs/logpush/) to retain their Access logging, if desired.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/#page","headline":"Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)","description":"Access logs will now respect the CMB.","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/og.png?v=bdf386521b0c65b1","dateModified":"2025-08-14","datePublished":"2025-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
