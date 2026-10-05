---
description: Browser Rendering pricing announcement
title: Introducing pricing for the Browser Rendering API — $0.09 per browser hour
image: https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/og.png?v=243698a8538ac53d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 28, 2025

## Introducing pricing for the Browser Rendering API — $0.09 per browser hour

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve launched pricing for [Browser Rendering](https://developers.cloudflare.com/browser-run/), including a free tier and a pay-as-you-go model that scales with your needs. Starting **August 20, 2025**, Cloudflare will begin billing for Browser Rendering.

There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:

- [**REST API**](https://developers.cloudflare.com/browser-run/quick-actions/): Charged for **Duration** only ($/browser hour)
- [**Browser Sessions**](https://developers.cloudflare.com/browser-run/#integration-methods): Charged for both **Duration** and **Concurrency** ($/browser hour and # of concurrent browsers)

Included usage and pricing by plan

| Plan | Included duration | Included concurrency | Price (beyond included) |
| --- | --- | --- | --- |
| **Workers Free** | 10 minutes per day | 3 concurrent browsers | N/A |
| **Workers Paid** | 10 hours per month | 10 concurrent browsers (averaged monthly) | **1. REST API**: $0.09 per additional browser hour <br>**2. Workers Bindings**: $0.09 per additional browser hour <br> $2.00 per additional concurrent browser |

What you need to know:

- **Workers Free Plan:** 10 minutes of browser usage per day with 3 concurrent browsers at no charge.
- **Workers Paid Plan:** 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.

You can monitor usage via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run). Go to **Compute** > **Browser Run**.

![Browser Rendering dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1880,height=1080,format=webp/_astro/dashboard.BQnX87lT.png)

If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's [included usage](https://developers.cloudflare.com/browser-run/pricing/). To estimate costs, take a look at these [example pricing scenarios](https://developers.cloudflare.com/browser-run/pricing/#examples-of-workers-paid-pricing).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/#page","headline":"Introducing pricing for the Browser Rendering API — $0.09 per browser hour","description":"Browser Rendering pricing announcement","url":"https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/og.png?v=243698a8538ac53d","dateModified":"2025-07-28","datePublished":"2025-07-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
