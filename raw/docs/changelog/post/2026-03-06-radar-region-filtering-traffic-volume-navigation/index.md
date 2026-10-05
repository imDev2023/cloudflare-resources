---
description: New region filtering, traffic volume by top autonomous systems and locations, and breadcrumb navigation on Cloudflare Radar
title: Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/og.png?v=31c3736f5c694009
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 6, 2026

## Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) ships several new features that improve the flexibility and usability of the platform, as well as visibility into what is happening on the Internet.

#### Region filtering

All location-aware pages now support filtering by region, including continents, geographic subregions ([Middle East ↗︎](https://radar.cloudflare.com/middle-east), [Eastern Asia ↗︎](https://radar.cloudflare.com/eastern-asia), etc.), political regions ([EU ↗︎](https://radar.cloudflare.com/european-union), [African Union ↗︎](https://radar.cloudflare.com/african-union)), and US Census regions/divisions (for example, [New England ↗︎](https://radar.cloudflare.com/traffic/us-new-england), [US Northeast ↗︎](https://radar.cloudflare.com/traffic/us-northeast)).

![Screenshot of region filtering on Radar - Middle east](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1108,format=webp/_astro/region-filtering-middle-east.D__dYNBw.png)

#### Traffic volume by top autonomous systems and locations

A new traffic volume view shows the top autonomous systems and countries/territories for a given location. This is useful for quickly determining which network providers in a location may be experiencing connectivity issues, or how traffic is distributed across a region.

![Screenshot of traffic volume by top autonomous systems in US](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=928,format=webp/_astro/traffic-volume-top-as-us.DhnbB8gy.png)

The new AS and location dimensions have also been added to the [Data Explorer ↗︎](https://radar.cloudflare.com/explorer) for the HTTP, DNS, and NetFlows datasets. Combined with other available filters, this provides a powerful tool for generating unique insights.

![Screenshot of AS and location dimensions in Data Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1486,format=webp/_astro/data-explorer-top-as-pt.DAWOCd_b.png)

Finally, breadcrumb navigation is now available on most pages, allowing easier navigation between parent and related pages.

Check out these features on [Cloudflare Radar ↗︎](https://radar.cloudflare.com).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/#page","headline":"Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar","description":"New region filtering, traffic volume by top autonomous systems and locations, and breadcrumb navigation on Cloudflare Radar","url":"https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/og.png?v=31c3736f5c694009","dateModified":"2026-03-06","datePublished":"2026-03-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
