---
description: Monitors configured with a probe zone have been migrated to new infrastructure.
title: Improvements to Monitoring Using Zone Settings
image: https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/og.png?v=60bdff3e5eaac38c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 6, 2025

## Improvements to Monitoring Using Zone Settings

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.

All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.

#### What you can expect:

- More reliable application of zone settings to monitoring requests, including
  - Authenticated Origin Pulls
  - Aegis Egress IP Pools
  - Argo Smart Routing
  - HTTP/2 to Origin
- Improved support and bug fixes for retries, redirects, and proxied origin resolution
- Improved performance and reliability of monitoring requests within the Cloudflare network
- Unrelated CDN or WAF configuration changes should have no risk of impact to pool health

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/#page","headline":"Improvements to Monitoring Using Zone Settings","description":"Monitors configured with a probe zone have been migrated to new infrastructure.","url":"https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/og.png?v=60bdff3e5eaac38c","dateModified":"2025-08-06","datePublished":"2025-08-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
