---
description: Expanded DNS insights with new API endpoints for 1.1.1.1 resolver aggregated traffic data
title: DNS Insights in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/og.png?v=c17783fbb3777ba8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 27, 2025

## DNS Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) DNS resolver. In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.

Previously limited to the [`top`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/) locations and ASes endpoints, we have now introduced the following endpoints:

- [`/dns/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries/): Retrieves DNS query volume over time.
- [`/dns/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/): Retrieves summaries of DNS query distribution across ten different dimensions.
- [`/dns/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/): Retrieves timeseries data for DNS query distribution across ten different dimensions.

For the `summary` and `timeseries_groups` endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:

- `cache_hit`: Cache status (hit vs. miss).
- `dnsssec`: DNSSEC support status (secure, insecure, invalid or other).
- `dnsssec_aware`: DNSSEC client awareness (aware vs. not-aware).
- `dnsssec_e2e`: End-to-end security (secure vs. insecure).
- `ip_version`: IP version (IPv4 vs. IPv6).
- `matching_answer`: Matching answer status (match vs. no-match).
- `protocol`: Transport protocol (UDP, TLS, HTTPS or TCP).
- `query_type`: Query type ( `A`, `AAAA`, `PTR`, etc.).
- `response_code`: Response code ( `NOERROR`, `NXDOMAIN`, `REFUSED`, etc.).
- `response_ttl`: Response TTL.

Learn more about the new Radar DNS insights in our [blog post ↗︎](https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/), and check out the [new Radar page ↗︎](https://radar.cloudflare.com/dns).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/#page","headline":"DNS Insights in Cloudflare Radar","description":"Expanded DNS insights with new API endpoints for 1.1.1.1 resolver aggregated traffic data","url":"https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/og.png?v=c17783fbb3777ba8","dateModified":"2025-02-27","datePublished":"2025-02-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
