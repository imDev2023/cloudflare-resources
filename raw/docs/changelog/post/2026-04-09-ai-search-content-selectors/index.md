---
description: Control which parts of crawled pages are indexed using CSS selectors.
title: Website Source CSS content selectors for precise content extraction in AI Search
image: https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/og.png?v=ec30e7cc6729db27
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2026

## Website Source CSS content selectors for precise content extraction in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [CSS content selectors](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/) for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.

Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.

Configure content selectors via the dashboard or API:

```bash
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "my-ai-search",
    "source": "https://example.com",
    "type": "web-crawler",
    "source_params": {
      "web_crawler": {
        "parse_options": {
          "content_selector": [
            {
              "path": "**/blog/**",
              "selector": "article .post-body"
            }
          ]
        }
      }
    }
  }'
```

Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.

For configuration details and examples, refer to the [content selectors documentation](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/#page","headline":"Website Source CSS content selectors for precise content extraction in AI Search","description":"Control which parts of crawled pages are indexed using CSS selectors.","url":"https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/og.png?v=ec30e7cc6729db27","dateModified":"2026-04-08","datePublished":"2026-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
