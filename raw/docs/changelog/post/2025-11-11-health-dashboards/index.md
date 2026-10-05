---
description: Introducing Logpush Health Dashboards
title: Logpush Health Dashboards
image: https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/og.png?v=bb929f1ca305ee9a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 11, 2025

## Logpush Health Dashboards

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’re excited to introduce **Logpush Health Dashboards**, giving customers real-time visibility into the status, reliability, and performance of their [Logpush](https://developers.cloudflare.com/logs/logpush/) jobs. Health dashboards make it easier to detect delivery issues, monitor job stability, and track performance across destinations. The dashboards are divided into two sections:

- **Upload Health**: See how much data was successfully uploaded, where drops occurred, and how your jobs are performing overall. This includes data completeness, success rate, and upload volume.
- **Upload Reliability** – Diagnose issues impacting stability, retries, or latency, and monitor key metrics such as retry counts, upload duration, and destination availability.

![Health Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1333,height=334,format=webp/_astro/Health-Dashboard.CP0mV0IW.gif)

Health Dashboards can be accessed from the Logpush page in the Cloudflare dashboard at the account or zone level, under the Health tab. For more details, refer to our [**Logpush Health Dashboards**](https://developers.cloudflare.com/logs/logpush/logpush-health) documentation, which includes a comprehensive troubleshooting guide to help interpret and resolve common issues.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/#page","headline":"Logpush Health Dashboards","description":"Introducing Logpush Health Dashboards","url":"https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/og.png?v=bb929f1ca305ee9a","dateModified":"2025-11-11","datePublished":"2025-11-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
