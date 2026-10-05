---
description: The Routing page on Cloudflare Radar is now a dedicated section with separate Overview, RPKI, and Anomalies sub-pages, plus new Top 100 ASes and RPKI prefix validation widgets
title: Routing Section Expansion on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/og.png?v=463d5296b26a9b93
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 1, 2026

## Routing Section Expansion on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now features an expanded [Routing section ↗︎](https://radar.cloudflare.com/routing) with dedicated sub-pages, providing a more organized and in-depth view of the global routing ecosystem. This restructuring lays the groundwork for additional routing features and widgets coming in the near future.

#### Dedicated sub-pages

The single Routing page has been split into three focused sub-pages:

- [**Overview** ↗︎](https://radar.cloudflare.com/routing) — Routing statistics, IP address space trends, BGP announcements, and the new Top 100 ASes ranking.
- [**RPKI** ↗︎](https://radar.cloudflare.com/routing/rpki) — RPKI validation status, ASPA deployment trends, and per-ASN ASPA provider details.
- [**Anomalies** ↗︎](https://radar.cloudflare.com/routing/anomalies) — BGP route leaks, origin hijacks, and Multi-Origin AS (MOAS) conflicts.

![Screenshot of the routing section menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=574,height=342,format=webp/_astro/routing-section-menu.CEq17il_.png)

#### New widgets

The routing overview now includes a **Top 100 ASes** table ranking autonomous systems by customer cone size, IPv4 address space, or IPv6 address space. Users can switch between rankings using a segmented control.

![Screenshot of the top-100 ASes table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1426,format=webp/_astro/top-100-ases-table.ZBSReN_5.png)

The RPKI sub-page introduces a **RPKI validation** view for per-ASN pages, showing prefixes grouped by RPKI validation status (Valid, Invalid, Unknown) with visibility scores.

![Screenshot of the RPKI validation view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=978,format=webp/_astro/rpki-validation-view.D3eQih4x.png)

#### Improved IP address space chart

The [IP address space ↗︎](https://radar.cloudflare.com/routing) chart now displays both IPv4 and IPv6 trends stacked vertically and is available on global, country, and AS views.

![Screenshot of the IPv4 and IPv6 combined IP space chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1310,format=webp/_astro/combined-ipv4-ipv6-space.DQ5qc8la.png)

Check out the [Radar routing section ↗︎](https://radar.cloudflare.com/routing) to explore the data, and stay tuned for more routing insights coming soon.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/#page","headline":"Routing Section Expansion on Cloudflare Radar","description":"The Routing page on Cloudflare Radar is now a dedicated section with separate Overview, RPKI, and Anomalies sub-pages, plus new Top 100 ASes and RPKI prefix validation widgets","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/og.png?v=463d5296b26a9b93","dateModified":"2026-04-01","datePublished":"2026-04-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
