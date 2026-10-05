---
description: A new feature which allows site owners to charge crawlers for access to their content
title: Introducing Pay Per Crawl (private beta)
image: https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/og.png?v=3b6500dda0a0dde1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2025

## Introducing Pay Per Crawl (private beta)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are introducing a new feature of [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) — Pay Per Crawl. [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/) enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.

![Pay per crawl](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2926,height=1516,format=webp/_astro/pay-per-crawl.B5bv2nwT.png)

**For Site Owners:**

- Set pricing and select which crawlers to charge for content access
- Manage payments via Stripe
- Monitor analytics on successful content deliveries

**For AI Crawler Owners:**

- Use HTTP headers to request and accept pricing
- Receive clear confirmations on charges for accessed content

Learn more in the [Pay Per Crawl documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/#page","headline":"Introducing Pay Per Crawl (private beta)","description":"A new feature which allows site owners to charge crawlers for access to their content","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/og.png?v=3b6500dda0a0dde1","dateModified":"2025-07-01","datePublished":"2025-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
