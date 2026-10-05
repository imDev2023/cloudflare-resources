---
description: Magic Transit and Magic WAN customers that enable the CMB EU setting can access their health check data in the Cloudflare dashboard.
title: Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.
image: https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/og.png?v=0a366a537f407e69
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 30, 2025

## Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU ([Customer Metadata Boundary - Europe](https://developers.cloudflare.com/data-localization/metadata-boundary/)) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.

This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.

Specifically, these two GraphQL endpoints are now compatible with CMB EU:

- `magicTransitTunnelHealthChecksAdaptiveGroups`
- `magicTransitTunnelTrafficAdaptiveGroups`

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/#page","headline":"Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.","description":"Magic Transit and Magic WAN customers that enable the CMB EU setting can access their health check data in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/og.png?v=0a366a537f407e69","dateModified":"2025-07-30","datePublished":"2025-07-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
