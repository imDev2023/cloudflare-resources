---
description: New Multi-Threaded Routing Toolkit Explorer tool that parses MRT dump files entirely in the browser to inspect BGP messages, AS paths, community attributes, and more.
title: MRT Explorer on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/og.png?v=af79754e6292ddaf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2026

## MRT Explorer on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes an [MRT Explorer ↗︎](https://radar.cloudflare.com/routing/mrt-explorer) tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.

#### Loading a file

Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.

![Screenshot of the MRT Explorer file input form](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2428,height=898,format=webp/_astro/mrt-explorer-form.DKnzUqMC.png)

#### Inspecting events

Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.

![Screenshot of the MRT Explorer event list](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1536,format=webp/_astro/mrt-explorer-list.8fq2u5Kc.png)

#### Event details

Clicking on the "View details" action opens a modal with additional properties and the full event JSON.

![Screenshot of the MRT Explorer event details modal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=1890,format=webp/_astro/mrt-explorer-details.EMcHevWw.png)

#### Shareable URLs

When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.

Try the [MRT Explorer on Cloudflare Radar ↗︎](https://radar.cloudflare.com/routing/mrt-explorer).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/#page","headline":"MRT Explorer on Cloudflare Radar","description":"New Multi-Threaded Routing Toolkit Explorer tool that parses MRT dump files entirely in the browser to inspect BGP messages, AS paths, community attributes, and more.","url":"https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/og.png?v=af79754e6292ddaf","dateModified":"2026-05-19","datePublished":"2026-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
