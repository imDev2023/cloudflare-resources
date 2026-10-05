---
description: Configure dynamic pricing and URI pattern exclusions for Pay Per Crawl.
title: Pay Per Crawl advanced configuration
image: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/og.png?v=dcc56b32ff10c708
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2026

## Pay Per Crawl advanced configuration

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure advanced Pay Per Crawl settings for your zone, including:

- **Disable Pay Per Crawl by URI pattern** using [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) to offer free access to specific pages while charging for others.
- **Dynamic pricing** by having your origin return a `crawler-price` response header, or by using a [Cloudflare Worker](https://developers.cloudflare.com/workers/) to set prices based on request properties.

When dynamic pricing is enabled, Pay Per Crawl adds a `cf-pay-per-crawl` request header to origin requests so your origin or Worker can determine the appropriate price.

Refer to the [Advanced configuration documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/#page","headline":"Pay Per Crawl advanced configuration","description":"Configure dynamic pricing and URI pattern exclusions for Pay Per Crawl.","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/og.png?v=dcc56b32ff10c708","dateModified":"2026-06-16","datePublished":"2026-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
