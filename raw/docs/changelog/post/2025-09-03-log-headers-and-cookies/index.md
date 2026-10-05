---
description: Log Explorer now supports logging and querying header and cookie fields
title: Logging headers and cookies using custom fields
image: https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/og.png?v=b84d2a9985d08a82
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 3, 2025

## Logging headers and cookies using custom fields

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) now supports logging and filtering on header or cookie fields in the [`http_requests` dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/).

Create a custom field to log desired header or cookie values into the `http_requests` dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.

![Edit Custom fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1790,height=404,format=webp/_astro/edit-custom-fields.Cy4qXSpL.png)

For more details, refer to [Headers and cookies](https://developers.cloudflare.com/log-explorer/log-search/#headers-and-cookies).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/#page","headline":"Logging headers and cookies using custom fields","description":"Log Explorer now supports logging and querying header and cookie fields","url":"https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/og.png?v=b84d2a9985d08a82","dateModified":"2025-09-03","datePublished":"2025-09-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
