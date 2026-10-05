---
description: Drill down into individual crawler behavior with status code charts and export data for use in WAF rules, Redirect Rules, and robots.txt files.
title: Crawler drilldowns with extended actions menu
image: https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/og.png?v=3aab9deb3dc3deed
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 10, 2025

## Crawler drilldowns with extended actions menu

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/), [Redirect Rules](https://developers.cloudflare.com/rules/url-forwarding/), and robots.txt files.

#### What's new

#### Status code distribution chart

The **Metrics** tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.

![AI Crawl Control status code distribution chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1712,height=1104,format=webp/_astro/ai-crawl-control-status-codes.DESJcAiK.png)

#### Extended actions menu

Each crawler row includes a three-dot menu with per-crawler actions:

- **View Metrics** — Filter the AI Crawl Control Metrics page to the selected crawler.
- **View on Cloudflare Radar** — Access verified crawler details on Cloudflare Radar.
- **Copy User Agent** — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.
- **View in Security Analytics** — Filter Security Analytics by detection IDs (Bot Management customers).
- **Copy Detection ID** — Copy detection IDs for use in WAF custom rules (Bot Management customers).

![AI Crawl Control crawler actions menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2040,height=762,format=webp/_astro/ai-crawl-control-crawler-info.Dwc39LqI.png)

#### Get started

1. Log in to the Cloudflare dashboard, and select your account and domain.
2. Go to **AI Crawl Control** > **Metrics** to access the status code distribution chart.
3. Go to **AI Crawl Control** > **Crawlers** and select the three-dot menu for any crawler to access per-crawler actions.
4. Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.

Learn more about [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/#page","headline":"Crawler drilldowns with extended actions menu","description":"Drill down into individual crawler behavior with status code charts and export data for use in WAF rules, Redirect Rules, and robots.txt files.","url":"https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/og.png?v=3aab9deb3dc3deed","dateModified":"2025-11-10","datePublished":"2025-11-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
