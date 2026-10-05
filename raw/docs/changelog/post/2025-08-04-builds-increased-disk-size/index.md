---
description: Increased the available disk space for Workers Builds from 8 GB to 20 GB for all plans during the ongoing open beta. - workers
title: Increased disk space for Workers Builds
image: https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/og.png?v=edcb077552570b8f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2025

## Increased disk space for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

As part of the ongoing open beta for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), we’ve increased the available disk space for builds from **8 GB** to **20 GB** for both Free and Paid plans.

This provides more space for larger projects, dependencies, and build artifacts while improving overall build reliability.

| Metric | Free Plan | Paid Plans |
| --- | --- | --- |
| Disk Space | 20 GB | 20 GB |

All other [build limits](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) — including CPU, memory, build minutes, and timeout remain unchanged.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/#page","headline":"Increased disk space for Workers Builds","description":"Increased the available disk space for Workers Builds from 8 GB to 20 GB for all plans during the ongoing open beta. - workers","url":"https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/og.png?v=edcb077552570b8f","dateModified":"2025-08-04","datePublished":"2025-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
