---
description: New traffic charts showing HTTP response content type distribution and API-related dynamic traffic share
title: Content type distribution and API traffic share on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/og.png?v=2ef32f56264ef494
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 20, 2026

## Content type distribution and API traffic share on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes two new charts on the [traffic page ↗︎](https://radar.cloudflare.com/traffic) that provide deeper insights into the composition of HTTP traffic: a content type distribution chart and an API traffic share chart.

#### Content type distribution

The new [**Content type** ↗︎](https://radar.cloudflare.com/traffic#content-type) chart displays the distribution of HTTP response content types, grouped into high-level categories. A traffic type selector allows filtering by human, bot, or all traffic. The existing [**Bot vs. Human** ↗︎](https://radar.cloudflare.com/traffic#bot-vs-human) chart also gained a content type category filter, allowing users to see the bot/human split for specific content categories.

![Screenshot of the content type distribution chart on the Radar traffic page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/content-type-distribution.Dz2q1n6W.png)

Content type categories:

- **HTML** — Web pages ( `text/html`)
- **Images** — All image formats ( `image/*`)
- **JSON** — JSON data and API responses ( `application/json`, `*+json`)
- **JavaScript** — Scripts ( `application/javascript`, `text/javascript`)
- **CSS** — Stylesheets ( `text/css`)
- **Plain Text** — Unformatted text ( `text/plain`)
- **Fonts** — Web fonts ( `font/*`, `application/font-*`)
- **XML** — XML documents and feeds ( `text/xml`, `application/xml`, `application/rss+xml`, `application/atom+xml`)
- **YAML** — Configuration files ( `text/yaml`, `application/yaml`)
- **Video** — Video content and streaming ( `video/*`, `application/ogg`, `*mpegurl`)
- **Audio** — Audio content ( `audio/*`)
- **Markdown** — Markdown documents ( `text/markdown`)
- **Documents** — PDFs, Office documents, ePub, CSV ( `application/pdf`, `application/msword`, `text/csv`)
- **Binary** — Executables, archives, WebAssembly ( `application/octet-stream`, `application/zip`, `application/wasm`)
- **Serialization** — Binary API formats ( `application/protobuf`, `application/grpc`, `application/msgpack`)
- **Other** — All other content types

The `CONTENT_TYPE` dimension and `contentType` filter are available on the HTTP [summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2/), [timeseries groups](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2/), and [timeseries](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries/) endpoints.

#### API traffic share

The new [**API traffic** ↗︎](https://radar.cloudflare.com/traffic#api-traffic) chart shows the percentage of dynamic (non-cacheable) HTTP request traffic that is API-related. API traffic is identified by JSON or XML response content types (`application/json`, `application/xml`, `text/xml`) on HTTP requests that returned a 200 status code. A traffic type selector allows switching between human traffic, bot traffic, or all traffic.

![Screenshot of the API traffic share chart on the Radar traffic page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1006,format=webp/_astro/api-traffic-share._xl0TThn.png)

The `API_TRAFFIC` dimension is available on the existing HTTP [summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2/) and [timeseries groups](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2/) endpoints. An `apiTraffic` filter (`API` or `NON_API`) can also be applied to [HTTP timeseries](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries/) requests to retrieve raw request counts for API-only or non-API traffic.

Visit the [Radar traffic page ↗︎](https://radar.cloudflare.com/traffic) to explore these new charts.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/#page","headline":"Content type distribution and API traffic share on Cloudflare Radar","description":"New traffic charts showing HTTP response content type distribution and API-related dynamic traffic share","url":"https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/og.png?v=2ef32f56264ef494","dateModified":"2026-05-20","datePublished":"2026-05-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
