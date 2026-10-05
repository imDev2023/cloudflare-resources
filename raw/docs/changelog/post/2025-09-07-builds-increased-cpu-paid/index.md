---
description: Increased the available vCPU for Workers Builds from 2 to 4 vCPUs for paid plans, improving build performance and parallel processing capabilities. - workers
title: Increased vCPU for Workers Builds on paid plans
image: https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/og.png?v=f828ea4a486e75e3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 18, 2025

## Increased vCPU for Workers Builds on paid plans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We recently [increased the available disk space](https://developers.cloudflare.com/changelog/2025-08-04-builds-increased-disk-size/) from 8 GB to 20 GB for **all** plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to **4 vCPU**.

These changes continue our focus on making [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) faster and more reliable.

| Metric | Free Plan | Paid Plans |
| --- | --- | --- |
| CPU | 2 vCPU | **4 vCPU** |

#### Performance Improvements

- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs
- **2x faster multi-threaded builds**: Tools like [esbuild ↗︎](https://esbuild.github.io/) and [webpack ↗︎](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling

All other [build limits](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) — including memory, build minutes, and timeout remain unchanged.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/#page","headline":"Increased vCPU for Workers Builds on paid plans","description":"Increased the available vCPU for Workers Builds from 2 to 4 vCPUs for paid plans, improving build performance and parallel processing capabilities. - workers","url":"https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/og.png?v=f828ea4a486e75e3","dateModified":"2025-09-18","datePublished":"2025-09-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
