---
description: AI Crawl Control analytics now include path pattern grouping, enhanced referral analytics, data transfer metrics, and image exports.
title: Analytics enhancements
image: https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/og.png?v=ef1c3e1845a11c73
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 9, 2026

## Analytics enhancements

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.

![AI Crawl Control path patterns](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2256,height=1262,format=webp/_astro/ai-crawl-control-path-patterns.0xT_lucE.png)

**Path pattern grouping**

- In the **Metrics** tab > **Most popular paths** table, use the new **Patterns** tab that groups requests by URI pattern ( `/blog/*`, `/api/v1/*`, `/docs/*`) to identify which site areas crawlers target most. Refer to the screenshot above.

**Enhanced referral analytics**

- Destination patterns show which site areas receive AI-driven referral traffic.
- In the **Metrics** tab, a new **Referrals over time** chart shows trends by operator or source.

**Data transfer metrics**

- In the **Metrics** tab > **Allowed requests over time** chart, toggle **Bytes** to show bandwidth consumption.
- In the **Crawlers** tab, a new **Bytes Transferred** column shows bandwidth per crawler.

**Image exports**

- Export charts and tables as images for reports and presentations.

Learn more about [analyzing AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/#page","headline":"Analytics enhancements","description":"AI Crawl Control analytics now include path pattern grouping, enhanced referral analytics, data transfer metrics, and image exports.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/og.png?v=ef1c3e1845a11c73","dateModified":"2026-02-09","datePublished":"2026-02-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
