---
description: The list items endpoint now accepts a key query parameter to return the item matching an exact object key.
title: Filter AI Search list items by exact object key
image: https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/og.png?v=ba79439d2ec14042
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2026

## Filter AI Search list items by exact object key

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [AI Search](https://developers.cloudflare.com/ai-search/), you can upload files to an instance, or connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) such as an R2 bucket, to make your content searchable with natural language. Each file becomes an **item** identified by an object **key** (its filename or path). The [list items endpoint](https://developers.cloudflare.com/ai-search/api/items/rest-api/) returns the items in an instance.

That endpoint now accepts a `key` query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing `item_id` filter for when you know the key but not the ID.

```bash
curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/instances/<INSTANCE_NAME>/items?key=docs/readme.md" \
  -H "Authorization: Bearer <API_TOKEN>"
```

Keys are unique per data source, so combine `key` with `source` (for example, `source=builtin`) to disambiguate when the same key exists across multiple sources.

For more information, refer to [managing items](https://developers.cloudflare.com/ai-search/api/items/rest-api/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/#page","headline":"Filter AI Search list items by exact object key","description":"The list items endpoint now accepts a key query parameter to return the item matching an exact object key.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/og.png?v=ba79439d2ec14042","dateModified":"2026-07-08","datePublished":"2026-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
