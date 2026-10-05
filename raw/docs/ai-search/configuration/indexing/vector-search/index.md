---
description: Configure vector search in AI Search to find semantically similar content using embeddings.
title: Vector search
image: https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/og.png?v=ca22d998ce486798
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-search/llms.txt  
> Use this file to discover all available pages before exploring further.

# Vector search

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-search/configuration/indexing/vector-search/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Vector search converts your query into a vector embedding and finds chunks with similar meaning. It is enabled by default on all AI Search instances. For an overview of search modes, refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/).

## Built-in vector index

AI Search instances include a built-in vector index powered by [Vectorize](https://developers.cloudflare.com/vectorize/). The vector index stores embeddings generated from your content and is created and maintained automatically. You do not need to create or manage a Vectorize index yourself.

## Embedding model

The [embedding model](https://developers.cloudflare.com/ai-search/configuration/models/) determines the vector dimensions for the vector index. The embedding model is set when creating an instance and cannot be changed after creation.

## Disable vector search

Vector search is enabled by default. To use [keyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/) only, set `index_method.vector` to `false`. At least one of `vector` or `keyword` must be `true`.

```ts
const instance = await env.AI_SEARCH.create({
	id: "my-instance",
	index_method: {
		vector: false,
		keyword: true,
	},
});
```

## Per-request overrides

You can force vector-only search on a per-request basis using `ai_search_options.retrieval.retrieval_type`, even if keyword search is also enabled on the instance.

```ts
const instance = env.AI_SEARCH.get("my-instance");

const results = await instance.search({
	messages: [{ role: "user", content: "What is Cloudflare?" }],
	ai_search_options: {
		retrieval: {
			retrieval_type: "vector",
		},
	},
});
```

## Scoring details

When using vector search, each chunk includes a `scoring_details` object:

| Field | Type | Description |
| --- | --- | --- |
| `vector_score` | number | Vector similarity score (0 to 1). |
| `vector_rank` | number | Rank position in the result set. |

## Limits

For vector index limits, refer to [Limits and pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/).
