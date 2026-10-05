---
description: Monitor robots.txt file health, track crawler violations, and gain visibility into how AI crawlers interact with your directives.
title: New Robots.txt tab for tracking crawler compliance
image: https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/og.png?v=e4317c181f38cd53
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 21, 2025

## New Robots.txt tab for tracking crawler compliance

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control now includes a **Robots.txt** tab that provides insights into how AI crawlers interact with your `robots.txt` files.

#### What's new

The Robots.txt tab allows you to:

- Monitor the health status of `robots.txt` files across all your hostnames, including HTTP status codes, and identify hostnames that need a `robots.txt` file.
- Track the total number of requests to each `robots.txt` file, with breakdowns of successful versus unsuccessful requests.
- Check whether your `robots.txt` files contain [Content Signals ↗︎](https://contentsignals.org/) directives for AI training, search, and AI input.
- Identify crawlers that request paths explicitly disallowed by your `robots.txt` directives, including the crawler name, operator, violated path, specific directive, and violation count.
- Filter `robots.txt` request data by crawler, operator, category, and custom time ranges.

#### Take action

When you identify non-compliant crawlers, you can:

- Block the crawler in the [Crawlers tab](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- Create custom [WAF rules](https://developers.cloudflare.com/waf/) for path-specific security
- Use [Redirect Rules](https://developers.cloudflare.com/rules/url-forwarding/) to guide crawlers to appropriate areas of your site

To get started, go to **AI Crawl Control** > **Robots.txt** in the Cloudflare dashboard. Learn more in the [Track robots.txt documentation](https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/#page","headline":"New Robots.txt tab for tracking crawler compliance","description":"Monitor robots.txt file health, track crawler violations, and gain visibility into how AI crawlers interact with your directives.","url":"https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/og.png?v=e4317c181f38cd53","dateModified":"2025-10-21","datePublished":"2025-10-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
