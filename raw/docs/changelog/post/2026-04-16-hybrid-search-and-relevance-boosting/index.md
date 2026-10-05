---
description: Combine vector and keyword search in a single query, and boost results by metadata fields like timestamp or priority.
title: AI Search now has hybrid search and relevance boosting
image: https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/og.png?v=7a19804bf00d361b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 16, 2026

## AI Search now has hybrid search and relevance boosting

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.

#### Hybrid search

Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.

You can configure the tokenizer (`porter` for natural language, `trigram` for code), keyword match mode (`and` for precision, `or` for recall), and fusion method (`rrf` or `max`) per instance:

```ts
const instance = await env.AI_SEARCH.create({
	id: "my-instance",
	index_method: { vector: true, keyword: true },
	fusion_method: "rrf",
	indexing_options: { keyword_tokenizer: "porter" },
	retrieval_options: { keyword_match_mode: "and" },
});
```

Refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/) for an overview and [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for configuration details.

#### Relevance boosting

Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on `timestamp`, or surface high-priority content by boosting on a custom metadata field like `priority`.

Configure up to 3 boost fields per instance or override them per request:

```ts
const results = await env.AI_SEARCH.get("my-instance").search({
	messages: [{ role: "user", content: "deployment guide" }],
	ai_search_options: {
		retrieval: {
			boost_by: [
				{ field: "timestamp", direction: "desc" },
				{ field: "priority", direction: "desc" },
			],
		},
	},
});
```

Refer to [Relevance boosting](https://developers.cloudflare.com/ai-search/configuration/retrieval/boosting/) for configuration details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/#page","headline":"AI Search now has hybrid search and relevance boosting","description":"Combine vector and keyword search in a single query, and boost results by metadata fields like timestamp or priority.","url":"https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/og.png?v=7a19804bf00d361b","dateModified":"2026-04-16","datePublished":"2026-04-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
