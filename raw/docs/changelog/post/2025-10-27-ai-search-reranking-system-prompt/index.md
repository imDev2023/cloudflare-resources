---
description: Improve result accuracy with reranking and dynamically control AI Search responses by setting system prompts in API requests.
title: Reranking and API-based system prompt configuration in AI Search
image: https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/og.png?v=fbb5debd9f9e0e63
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 28, 2025

## Reranking and API-based system prompt configuration in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.

#### Rerank for more relevant results

You can now enable [reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.

You can enable and configure reranking in the dashboard or directly in your API requests:

```javascript
const answer = await env.AI.autorag("my-autorag").aiSearch({
	query: "How do I train a llama to deliver coffee?",
	model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
	reranking: {
		enabled: true,
		model: "@cf/baai/bge-reranker-base",
	},
});
```

#### Set system prompts in API

Previously, [system prompts](https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/) could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:

```javascript
// Dynamically set query and system prompt in AI Search
async function getAnswer(query, tone) {
	const systemPrompt = `You are a ${tone} assistant.`;

	const response = await env.AI.autorag("my-autorag").aiSearch({
		query: query,
		system_prompt: systemPrompt,
	});

	return response;
}

// Example usage
const query = "What is Cloudflare?";
const tone = "friendly";

const answer = await getAnswer(query, tone);
console.log(answer);
```

Learn more about [Reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) and [System Prompt](https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/) in AI Search.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/#page","headline":"Reranking and API-based system prompt configuration in AI Search","description":"Improve result accuracy with reranking and dynamically control AI Search responses by setting system prompts in API requests.","url":"https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/og.png?v=fbb5debd9f9e0e63","dateModified":"2025-10-28","datePublished":"2025-10-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
