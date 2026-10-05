---
description: Live screenshots, PDF and JSON export, detailed IP and file download data, and a redesigned summary layout for URL Scanner on Cloudflare Radar
title: URL Scanner improvements on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/og.png?v=f48eedd3262cec40
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2026

## URL Scanner improvements on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) ships several improvements to the [URL Scanner ↗︎](https://radar.cloudflare.com/scan) that make scan reports more informative and easier to share:

- **Live screenshots** — the summary card now includes an option to capture a live screenshot of the scanned URL on demand using the [Browser Rendering](https://developers.cloudflare.com/browser-run/) API.
- **Save as PDF** — a new button generates a print-optimized document aggregating all tab contents (Summary, Security, Network, Behavior, and Indicators) into a single file.
- **Download as JSON** — raw scan data is available as a JSON download for programmatic use.
- **Redesigned summary layout** — page information and security details are now displayed side by side with the screenshot, with a layout that adapts to narrower viewports.
- **File downloads** — downloads are separated into a dedicated card with expandable rows showing each file's source URL and SHA256 hash.
- **Detailed IP address data** — the Network tab now includes additional detail per IP address observed during the scan.

![Screenshot of the redesigned URL Scanner summary on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2424,height=2658,format=webp/_astro/url-scanner-summary-redesign.DO4wDjQ3.png)

Explore these improvements on the [Cloudflare Radar URL Scanner ↗︎](https://radar.cloudflare.com/scan).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/#page","headline":"URL Scanner improvements on Cloudflare Radar","description":"Live screenshots, PDF and JSON export, detailed IP and file download data, and a redesigned summary layout for URL Scanner on Cloudflare Radar","url":"https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/og.png?v=f48eedd3262cec40","dateModified":"2026-03-26","datePublished":"2026-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
