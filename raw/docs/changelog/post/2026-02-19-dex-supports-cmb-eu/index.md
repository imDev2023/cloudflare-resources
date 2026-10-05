---
description: Digital Experience Monitoring now fully supports the EU Customer Metadata Boundary
title: DEX Supports EU Customer Metadata Boundary
image: https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/og.png?v=1b19662c8ffc2692
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 19, 2026

## DEX Supports EU Customer Metadata Boundary

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into [WARP](https://developers.cloudflare.com/warp-client/) device connectivity and performance to any internal or external application.

Now, all DEX logs are fully compatible with Cloudflare's [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.

If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via [LogPush](https://developers.cloudflare.com/logs/logpush/), and build their own analytics and dashboards.

If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: "DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets."

![Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2143,height=1221,format=webp/_astro/dex_supports_cmb.6YOLXjHN.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/#page","headline":"DEX Supports EU Customer Metadata Boundary","description":"Digital Experience Monitoring now fully supports the EU Customer Metadata Boundary","url":"https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/og.png?v=1b19662c8ffc2692","dateModified":"2026-02-19","datePublished":"2026-02-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
