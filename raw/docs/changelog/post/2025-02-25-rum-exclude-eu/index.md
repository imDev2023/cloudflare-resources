---
description: Enable RUM monitoring for your website and respect privacy laws with ease.
title: Easily Exclude EU Visitors from RUM
image: https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/og.png?v=b4066c45028a09c2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 26, 2024

## Easily Exclude EU Visitors from RUM

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.

![RUM Enablement UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1101,height=1061,format=webp/_astro/2025-02-26-rum-eu.X0ZtbXWA.png)

Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.

To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.

You can learn more about what metrics are reported by Web Analytics and how it is collected [in the Web Analytics documentation](https://developers.cloudflare.com/web-analytics/data-metrics/). You can enable Web Analytics on any hostname by going to the [Web Analytics ↗︎](https://dash.cloudflare.com/?to=/:account/web-analytics/sites) section of the dashboard, selecting "Manage Site" for the hostname you want to monitor, and choosing the appropriate enablement option.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/#page","headline":"Easily Exclude EU Visitors from RUM","description":"Enable RUM monitoring for your website and respect privacy laws with ease.","url":"https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/og.png?v=b4066c45028a09c2","dateModified":"2024-02-26","datePublished":"2024-02-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
