---
description: Cloudflare Radar search now includes Internet events and outages, with links to relevant pages and historical context.
title: Radar search now includes Internet events
image: https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/og.png?v=ac04a1932ec42356
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 8, 2026

## Radar search now includes Internet events

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.

![Radar search results showing Internet outage events associated with locations and autonomous systems](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2512,height=1130,format=webp/_astro/radar-search-events.DpZAk59G.png)

Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through [WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/#page","headline":"Radar search now includes Internet events","description":"Cloudflare Radar search now includes Internet events and outages, with links to relevant pages and historical context.","url":"https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/og.png?v=ac04a1932ec42356","dateModified":"2026-09-08","datePublished":"2026-09-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
