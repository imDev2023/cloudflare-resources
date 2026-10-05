---
description: Regionalize traffic at the IP layer by binding a BYOIP prefix to a region.
title: Regionalized IP Bindings for Regional Services
image: https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/og.png?v=57b0715725a85065
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 23, 2026

## Regionalized IP Bindings for Regional Services

[Data Localization Suite](https://developers.cloudflare.com/data-localization/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Regional Services now supports **Regionalized IP Bindings**, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/).

Where [Regional Hostnames](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/) regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.

Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.

To get started, refer to [Regionalized IP Bindings](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/#page","headline":"Regionalized IP Bindings for Regional Services","description":"Regionalize traffic at the IP layer by binding a BYOIP prefix to a region.","url":"https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/og.png?v=57b0715725a85065","dateModified":"2026-06-23","datePublished":"2026-06-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
