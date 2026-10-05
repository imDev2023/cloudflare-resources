---
description: The /crawl endpoint accepts a new contentUse parameter that enforces the `use` directive in a site's robots.txt Content Signals.
title: Crawl endpoint now respects the Content Signals `use` directive
image: https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/og.png?v=7f55b9d73c87b314
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 31, 2026

## Crawl endpoint now respects the Content Signals \`use\` directive

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`/crawl`](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) endpoint now respects the `use` directive of the [Content Signals ↗︎](https://contentsignals.org/) standard, letting site owners express the maximum level at which their content may be used.

You can declare your intended level with the new `contentUse` parameter. Allowed values, from least to most permissive, are `reference` and `full`, and the default is `full`. If a target site's `robots.txt` sets a `use` level that is more restrictive than your declared `contentUse`, the crawl request is rejected with a `400` error.

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com",
    "contentUse": "reference",
    "formats": ["markdown"]
  }'
```

For more information, refer to [Content Signals](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/#content-signals) in the `/crawl` endpoint documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/#page","headline":"Crawl endpoint now respects the Content Signals `use` directive","description":"The /crawl endpoint accepts a new contentUse parameter that enforces the use directive in a site's robots.txt Content Signals.","url":"https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/og.png?v=7f55b9d73c87b314","dateModified":"2026-08-31","datePublished":"2026-08-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
