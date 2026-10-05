---
description: Analyze crawler activity with requests over time charts, referrer breakdowns, and configurable filters with data export capabilities
title: Enhanced AI Crawl Control metrics with new drilldowns and filters
image: https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/og.png?v=56d02ce69e810645
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 14, 2025

## Enhanced AI Crawl Control metrics with new drilldowns and filters

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.

#### What's new

#### Track crawler requests over time

Visualize crawler activity patterns over time, and group data by different dimensions:

- **By Crawler** — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)
- **By Category** — Analyze crawler purpose or type
- **By Operator** — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site
- **By Host** — Break down activity across multiple subdomains
- **By Status Code** — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)

![AI Crawl Control requests over time chart with grouping tabs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1293,height=666,format=webp/_astro/ai-crawl-control-requests-over-time.BtRyz0OT.png "Interactive chart showing crawler requests over time with filterable dimensions")

*Interactive chart showing crawler requests over time with filterable dimensions*

#### Analyze referrer data (Paid plans)

Identify traffic sources with referrer analytics:

- View top referrers driving traffic to your site
- Understand discovery patterns and content popularity from AI operators

![AI Crawl Control top referrers breakdown](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1291,height=656,format=webp/_astro/ai-crawl-control-top-referrers.CEUAwpd8.png "Bar chart showing top referrers and their respective traffic volumes")

*Bar chart showing top referrers and their respective traffic volumes*

#### Export data

Download your filtered view as a CSV:

- Includes all applied filters and groupings
- Useful for custom reporting and deeper analysis

#### Get started

1. Log in to the Cloudflare dashboard, and select your account and domain.
2. Go to **AI Crawl Control** > **Metrics**.
3. Use the grouping tabs to explore different views of your data.
4. Apply filters to focus on specific crawlers, time ranges, or response codes.
5. Select **Download CSV** to export your filtered data for further analysis.

Learn more about [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/#page","headline":"Enhanced AI Crawl Control metrics with new drilldowns and filters","description":"Analyze crawler activity with requests over time charts, referrer breakdowns, and configurable filters with data export capabilities","url":"https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/og.png?v=56d02ce69e810645","dateModified":"2025-10-14","datePublished":"2025-10-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
