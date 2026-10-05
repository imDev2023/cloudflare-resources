---
description: Browser Rendering's new /crawl endpoint lets you submit a starting URL and automatically discover, render, and return content from an entire website as HTML, Markdown, or structured JSON.
title: Crawl entire websites with a single API call using Browser Rendering
image: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/og.png?v=06491500b776b80e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 10, 2026

## Crawl entire websites with a single API call using Browser Rendering

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

*Edit: this post has been edited to clarify crawling behavior with respect to site guidance.*

You can now crawl an entire website with a single API call using [Browser Rendering](https://developers.cloudflare.com/browser-run/)'s new [`/crawl` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/), available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a [verified bot (intermediary agent)](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) that respects robots.txt and [AI Crawl Control ↗︎](https://www.cloudflare.com/ai-crawl-control/) by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.

Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.

```sh
# Initiate a crawl
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://blog.cloudflare.com/"
  }'

# Check results
curl -X GET 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}' \
  -H 'Authorization: Bearer <apiToken>'
```

Key features:

- **Multiple output formats** - Return crawled content as HTML, Markdown, and structured JSON (powered by [Workers AI](https://developers.cloudflare.com/workers-ai/))
- **Crawl scope controls** - Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths
- **Automatic page discovery** - Discovers URLs from sitemaps, page links, or both
- **Incremental crawling** - Use `modifiedSince` and `maxAge` to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls
- **Static mode** - Set `render: false` to fetch static HTML without spinning up a browser, for faster crawling of static sites
- **Well-behaved bot** - Honors `robots.txt` directives, including `crawl-delay`

Available on both the Workers Free and Paid plans.

**Note**: the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.

To get started, refer to the [crawl endpoint documentation](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/). If you are setting up your own site to be crawled, review the [robots.txt and sitemaps best practices](https://developers.cloudflare.com/browser-run/reference/robots-txt/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/#page","headline":"Crawl entire websites with a single API call using Browser Rendering","description":"Browser Rendering's new /crawl endpoint lets you submit a starting URL and automatically discover, render, and return content from an entire website as HTML, Markdown, or structured JSON.","url":"https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/og.png?v=06491500b776b80e","dateModified":"2026-03-10","datePublished":"2026-03-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
