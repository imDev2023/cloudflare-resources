---
description: Cloudflare Radar adds a Top ASes by announced IP space chart to country routing pages and a new RPKI ROA deployment timeseries widget.
title: New routing widgets on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/og.png?v=3a3c0604581b6e25
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 4, 2026

## New routing widgets on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) is expanding its [Routing section ↗︎](https://radar.cloudflare.com/routing) with two new widgets that give a deeper view into how networks announce address space and how RPKI ROA coverage evolves over time.

#### Top ASes by announced IP space on country pages

Country routing pages now include a **Top ASes by announced IP space** chart, breaking down the IPv4 and IPv6 address space announced from a country across the autonomous systems that originate it. The chart stacks the IPv4 and IPv6 views vertically, with the top contributing ASes called out by color and the remaining networks aggregated as **Other**.

![Screenshot of the top ASes by announced IP space chart on a country routing page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1322,format=webp/_astro/country-top-ases-ip-space.CoGqJB6W.png)

#### RPKI ROA deployment timeseries

The [RPKI sub-page ↗︎](https://radar.cloudflare.com/routing/rpki) adds an **RPKI ROA deployment** timeseries widget that tracks the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with separate IPv4 and IPv6 lines. A toggle switches the view between the share of covered **prefixes** and the share of covered **IP address space**. The widget is available on global, country, and AS views, so operators can monitor RPKI adoption progress and compare deployment trends across different scopes.

![Screenshot of the RPKI ROA deployment timeseries widget](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=874,format=webp/_astro/rpki-roa-deployment-timeseries.DTsP_V93.png)

#### API endpoints

The data behind these widgets is also available through two new endpoints on the [`BGP`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/) API:

- [`/bgp/ips/top/ases`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/) - Returns the top autonomous systems by announced IP space (IPv4 `/24`s or IPv6 `/48`s), globally or filtered by country, snapped to the nearest 8-hour RIB boundary.
- [`/bgp/rpki/roas/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/) - Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.

Visit the [Radar routing section ↗︎](https://radar.cloudflare.com/routing) to explore both widgets.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/#page","headline":"New routing widgets on Cloudflare Radar","description":"Cloudflare Radar adds a Top ASes by announced IP space chart to country routing pages and a new RPKI ROA deployment timeseries widget.","url":"https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/og.png?v=3a3c0604581b6e25","dateModified":"2026-05-04","datePublished":"2026-05-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
