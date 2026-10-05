---
description: Expanded visibility into crawler, referral, and bot activity with new Radar API endpoints
title: Bot &amp; Crawler Insights in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/og.png?v=21039691dd130beb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2025

## Bot & Crawler Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Web crawlers insights

[**Radar**](https://developers.cloudflare.com/radar/) now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.

We have introduced the following endpoints:

- [`/bots/crawlers/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/): Returns an overview of crawler HTTP request distributions across key dimensions.
- [`/bots/crawlers/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/): Provides time-series data on crawler request distributions across the same dimensions.

These endpoints allow analysis across the following dimensions:

- `user_agent`: Parsed data from the `User-Agent` header.
- `referer`: Parsed data from the `Referer` header.
- `crawl_refer_ratio`: Ratio of HTML page crawl requests to HTML page referrals by platform.

#### Broader bot insights

In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:

- [`/bots/`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/): Lists all bots.
- [`/bots/{bot_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get/): Returns detailed metadata for a specific bot.
- [`/bots/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries/): Time-series data for bot activity.
- [`/bots/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/summary/): Returns an overview of bot HTTP request distributions across key dimensions.
- [`/bots/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries_groups/): Provides time-series data on bot request distributions across the same dimensions.

These endpoints support filtering and breakdowns by:

- `bot`: Bot name.
- `bot_operator`: The organization or entity operating the bot.
- `bot_category`: Classification of bot type.

The previously available `verified_bots` endpoints have now been deprecated in favor of this set of bot insights APIs. While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.

Learn more about the new Radar bot and crawler insights in our [blog post ↗︎](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/#page","headline":"Bot & Crawler Insights in Cloudflare Radar","description":"Expanded visibility into crawler, referral, and bot activity with new Radar API endpoints","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/og.png?v=21039691dd130beb","dateModified":"2025-07-01","datePublished":"2025-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
