---
description: New RPKI ASPA insights on Cloudflare Radar, including ASPA deployment trends, per-ASN ASPA content, and API access
title: RPKI ASPA Deployment Insights on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/og.png?v=c99829e3ef3f230b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2026

## RPKI ASPA Deployment Insights on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes [Autonomous System Provider Authorization (ASPA) ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.

#### New API endpoints

The new [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API provides the following endpoints:

- [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) - Retrieves current or historical ASPA objects.
- [`/bgp/rpki/aspa/changes`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/) - Retrieves changes to ASPA objects over time.
- [`/bgp/rpki/aspa/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/) - Retrieves ASPA object counts over time as a timeseries.

#### New Radar widgets

The [global routing page ↗︎](https://radar.cloudflare.com/routing) now shows the ASPA deployment trend over time by counting daily ASPA objects.

![Screenshot of the ASPA deployment trend chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-global-trend.CXGWGFL4.png)

The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.

![Screenshot of the ASPA objects table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1852,format=webp/_astro/aspa-global-table.vHUyNoTh.png)

On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.

![Screenshot of the ASPA deployment trent chart for Germany](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-germany-trend.DIH6CESC.png)

On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.

![Screenshot of the ASPA changes timeline on an AS routing page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2198,height=1212,format=webp/_astro/aspa-asn-timeline.Bnl6upJs.png)

Check out the [Radar routing page ↗︎](https://radar.cloudflare.com/routing) to explore the data.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/#page","headline":"RPKI ASPA Deployment Insights on Cloudflare Radar","description":"New RPKI ASPA insights on Cloudflare Radar, including ASPA deployment trends, per-ASN ASPA content, and API access","url":"https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/og.png?v=c99829e3ef3f230b","dateModified":"2026-02-25","datePublished":"2026-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
