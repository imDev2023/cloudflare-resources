---
description: The pool filter in load balancing analytics now queries by pool name instead of pool ID, matching what you see in the UI dropdown.
title: Load balancing analytics now filters by pool name
image: https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/og.png?v=f4b5bbaa19b85fab
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 17, 2026

## Load balancing analytics now filters by pool name

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.

Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.

The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:

- **Requests over time**, filtering the chart series to the selected pool.
- **Pool distribution**, showing only the selected pool segment.
- **Top endpoints**, displaying cards for origins in the selected pool.
- **Latency**, showing latency data for the selected pool.

The **Logs** view and health event filtering are unchanged.

To use this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same pool filter appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

For more information about analytics filters and metrics, refer to [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/#page","headline":"Load balancing analytics now filters by pool name","description":"The pool filter in load balancing analytics now queries by pool name instead of pool ID, matching what you see in the UI dropdown.","url":"https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/og.png?v=f4b5bbaa19b85fab","dateModified":"2026-08-17","datePublished":"2026-08-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
