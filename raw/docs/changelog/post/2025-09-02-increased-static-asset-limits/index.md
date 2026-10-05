---
description: Paid and Workers for Platforms users can now upload up to 100,000 static assets per Worker version, up from the previous limit of 20,000.
title: Increased static asset limits for Workers
image: https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/og.png?v=4983c3a1fd32747f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2025

## Increased static asset limits for Workers

[Workers](https://developers.cloudflare.com/workers/) [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now upload up to **100,000 static assets** per Worker version

- Paid and Workers for Platforms users can now upload up to **100,000 static assets** per Worker version, a 5x increase from the previous limit of 20,000.
- Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker
- The individual file size limit of 25 MiB remains unchanged for all customers.

This increase allows you to build larger applications with more static assets without hitting limits.

#### Wrangler

To take advantage of the increased limits, you must use **Wrangler version 4.34.0 or higher**. Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.

#### Learn more

For more information about Workers static assets, see the [Static Assets documentation](https://developers.cloudflare.com/workers/static-assets/) and [Platform Limits](https://developers.cloudflare.com/workers/platform/limits/#static-assets).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/#page","headline":"Increased static asset limits for Workers","description":"Paid and Workers for Platforms users can now upload up to 100,000 static assets per Worker version, up from the previous limit of 20,000.","url":"https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/og.png?v=4983c3a1fd32747f","dateModified":"2025-09-04","datePublished":"2025-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
