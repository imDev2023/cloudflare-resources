---
description: Define custom metadata fields and filter search results by category, version, or any custom attribute.
title: Custom metadata filtering for AI Search
image: https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/og.png?v=546d8c0828f09571
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 23, 2026

## Custom metadata filtering for AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.

#### Define a custom metadata schema

You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (`text`, `number`, or `boolean`):

```bash
curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {API_TOKEN}" \
  -d '{
    "id": "my-instance",
    "type": "r2",
    "source": "my-bucket",
    "custom_metadata": [
      { "field_name": "category", "data_type": "text" },
      { "field_name": "version", "data_type": "number" },
      { "field_name": "is_public", "data_type": "boolean" }
    ]
  }'
```

#### Add metadata to your documents

How you attach metadata depends on your data source:

- **R2 bucket**: Set metadata using S3-compatible custom headers ( `x-amz-meta-*`) when uploading objects. Refer to [R2 custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#custom-metadata) for examples.
- **Website**: Add `<meta>` tags to your HTML pages. Refer to [Website custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/) for details.

#### Filter search results

Use custom metadata fields in your search queries alongside built-in attributes like `folder` and `timestamp`:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {API_TOKEN}" \
  -d '{
    "messages": [
      {
        "content": "How do I configure authentication?",
        "role": "user"
      }
    ],
    "ai_search_options": {
      "retrieval": {
        "filters": {
          "category": "documentation",
          "version": { "$gte": 2.0 }
        }
      }
    }
  }'
```

Learn more in the [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/#page","headline":"Custom metadata filtering for AI Search","description":"Define custom metadata fields and filter search results by category, version, or any custom attribute.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/og.png?v=546d8c0828f09571","dateModified":"2026-03-23","datePublished":"2026-03-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
