---
description: Improved connection metric insights in the Cloud Observatory, with new provider-level, region-level, and percentile views
title: Cloud Observatory connection metrics improvements
image: https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/og.png?v=200e1361beeaa053
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## Cloud Observatory connection metrics improvements

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloud Observatory ↗︎](https://radar.cloudflare.com/cloud-observatory) on [**Radar**](https://developers.cloudflare.com/radar/) now provides improved connection metric insights, offering new ways to explore TCP round-trip time, TCP handshake duration, TLS handshake duration, and response header receive duration across cloud provider origin servers.

The [Cloud Observatory overview ↗︎](https://radar.cloudflare.com/cloud-observatory#connection-metrics) now shows connection metrics broken down by cloud provider, making it easy to compare connection performance across Amazon Web Services, Google Cloud, Microsoft Azure, and Oracle Cloud.

![Screenshot of Cloud Observatory connection metrics broken down by cloud provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2338,height=1408,format=webp/_astro/cloud-observatory-connection-metrics-by-provider.Bk9nSitV.png)

Each [provider page ↗︎](https://radar.cloudflare.com/cloud-observatory/amazon#connection-metrics) now shows connection metrics for the top five regions, with a selector to rank by lowest or highest values.

![Screenshot of Cloud Observatory connection metrics broken down by region for a provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2338,height=1414,format=webp/_astro/cloud-observatory-connection-metrics-by-region.CbHAKXoc.png)

Each [region page ↗︎](https://radar.cloudflare.com/cloud-observatory/amazon/us-east-1#connection-metrics) now displays connection metrics as percentile distributions (25th percentile, median, and 75th percentile), providing insight into the range and variability of connection times.

![Screenshot of Cloud Observatory connection metrics with percentile distribution for a region](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2340,height=1288,format=webp/_astro/cloud-observatory-connection-metrics-percentiles.DJ9eAE0-.png)

These views are also available through the [`Origins` API](https://developers.cloudflare.com/api/resources/radar/subresources/origins/), using the `timeseries_groups` endpoint with the `ORIGIN`, `REGION`, or `PERCENTILE` dimension.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/#page","headline":"Cloud Observatory connection metrics improvements","description":"Improved connection metric insights in the Cloud Observatory, with new provider-level, region-level, and percentile views","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/og.png?v=200e1361beeaa053","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
