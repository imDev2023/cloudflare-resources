---
description: Add metadata filters to AutoRAG queries to enable multitenancy and control the scope of retrieved results.
title: Metadata filtering and multitenancy support in AutoRAG
image: https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/og.png?v=418dfe8c36139ea7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 23, 2025

## Metadata filtering and multitenancy support in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now filter [AutoRAG](https://developers.cloudflare.com/ai-search/) search results by `folder` and `timestamp` using [metadata filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) to narrow down the scope of your query.

This makes it easy to build [multitenant experiences](https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/) where each user can only access their own data. By organizing your content into per-tenant folders and applying a `folder` filter at query time, you ensure that each tenant retrieves only their own documents.

**Example folder structure:**

```bash
customer-a/logs/
customer-a/contracts/
customer-b/contracts/
```

**Example query:**

```js
const response = await env.AI.autorag("my-autorag").search({
	query: "When did I sign my agreement contract?",
	filters: {
		type: "eq",
		key: "folder",
		value: "customer-a/contracts/",
	},
});
```

You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select **Sync index**. Metadata filtering is available for all data indexed on or after **April 21, 2025**.

If you are new to AutoRAG, get started with the [Get started AutoRAG guide](https://developers.cloudflare.com/ai-search/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/#page","headline":"Metadata filtering and multitenancy support in AutoRAG","description":"Add metadata filters to AutoRAG queries to enable multitenancy and control the scope of retrieved results.","url":"https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/og.png?v=418dfe8c36139ea7","dateModified":"2025-04-23","datePublished":"2025-04-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
