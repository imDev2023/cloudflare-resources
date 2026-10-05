---
description: New Regional traffic insights, bringing a more localized perspective to the traffic trends shown on Radar
title: Regional Data in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/og.png?v=683d4d0d748cc64f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 29, 2025

## Regional Data in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.

The following API endpoints are now available:

- [`Get Geolocation`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/get/) - Retrieves geolocation by `geoId`.
- [`List Geolocations`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/list/) - Lists geolocations.
- [`NetFlows Summary By Dimension`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary_v2/) - Retrieves NetFlows summary by dimension.

All `summary` and `timeseries_groups` endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/) now include an `adm1` dimension for grouping data by first level administrative division (for example, state, province, etc.)

A new filter `geoId` was also added to all endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/), allowing filtering by a specific administrative division.

Check out the new Regional traffic insights on a country specific traffic page [new Radar page ↗︎](https://radar.cloudflare.com/traffic/pt).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/#page","headline":"Regional Data in Cloudflare Radar","description":"New Regional traffic insights, bringing a more localized perspective to the traffic trends shown on Radar","url":"https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/og.png?v=683d4d0d748cc64f","dateModified":"2025-09-29","datePublished":"2025-09-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
