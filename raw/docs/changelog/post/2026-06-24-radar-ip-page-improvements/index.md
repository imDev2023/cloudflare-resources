---
description: The Cloudflare Radar IP page now pinpoints your IPv4 and IPv6 locations alongside the Cloudflare data centers you connect to, and the AS card shows more network details.
title: Precise IP location and richer AS details on the Cloudflare Radar IP page
image: https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/og.png?v=3db8ab7195352a2a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 24, 2026

## Precise IP location and richer AS details on the Cloudflare Radar IP page

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now plots your IPv4 and IPv6 locations on the [IP page ↗︎](https://radar.cloudflare.com/ip), shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.

#### Your IP location on the map

The map of your connection now shows:

- **IP location markers** — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.
- **Cloudflare data center markers** — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.
- **Data center connectors** — Each line connects your IP markers to their respective data centers.

![Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3136,height=1305,format=webp/_astro/ip-page-geolocation.BJ53oUtj.png)

Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.

#### Extended AS information

The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.

Visit the [Cloudflare Radar IP page ↗︎](https://radar.cloudflare.com/ip) to explore more details about your IP.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/#page","headline":"Precise IP location and richer AS details on the Cloudflare Radar IP page","description":"The Cloudflare Radar IP page now pinpoints your IPv4 and IPv6 locations alongside the Cloudflare data centers you connect to, and the AS card shows more network details.","url":"https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/og.png?v=3db8ab7195352a2a","dateModified":"2026-06-24","datePublished":"2026-06-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
