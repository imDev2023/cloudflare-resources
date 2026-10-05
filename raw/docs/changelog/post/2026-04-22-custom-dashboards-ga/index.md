---
description: Build custom dashboards using 100+ GraphQL datasets and raw Log Explorer data.
title: Custom dashboards available to all customers
image: https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/og.png?v=4230cb0e57c2805b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 22, 2026

## Custom dashboards available to all customers

[Analytics](https://developers.cloudflare.com/analytics/) [Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.

This update significantly expands the data available for visualization. Build charts based on any of the **100+ datasets** available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.

#### Log Explorer integration

Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.

#### Key benefits

- **Unified visibility**: Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.
- **Flexible monitoring**: Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.
- **Expanded limits**: Log Explorer customers can create up to **100 dashboards** (up from 25 for standard customers).

![Custom Dashboards home page showing dashboard list and chart previews](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1079,height=793,format=webp/_astro/customdashboardshome.BIpSvImM.jpg)

To get started, refer to the [Custom Dashboards documentation](https://developers.cloudflare.com/analytics/custom-dashboards/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/#page","headline":"Custom dashboards available to all customers","description":"Build custom dashboards using 100+ GraphQL datasets and raw Log Explorer data.","url":"https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/og.png?v=4230cb0e57c2805b","dateModified":"2026-04-22","datePublished":"2026-04-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
