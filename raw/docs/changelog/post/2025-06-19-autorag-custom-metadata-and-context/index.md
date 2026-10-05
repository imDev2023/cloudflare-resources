---
description: You can now view custom metadata in AutoRAG search responses and use a context field to provide additional guidance to AI-generated answers.
title: View custom metadata in responses and guide AI-search with context in AutoRAG
image: https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/og.png?v=308f5c60e40d5a33
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2025

## View custom metadata in responses and guide AI-search with context in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [AutoRAG](https://developers.cloudflare.com/ai-search/), you can now view your object's custom metadata in the response from [`/search`](https://developers.cloudflare.com/ai-search/api/search/workers-binding/) and [`/ai-search`](https://developers.cloudflare.com/ai-search/api/search/workers-binding/), and optionally add a `context` field in the custom metadata of an object to provide additional guidance for AI-generated answers.

You can add [custom metadata](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/#r2putoptions) to an object when uploading it to your R2 bucket.

#### Object's custom metadata in search responses

When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside `attributes` then `file` , and can be used for downstream processing.

For example, the `attributes` section of your search response may look like:

```json
{
	"attributes": {
		"timestamp": 1750001460000,
		"folder": "docs/",
		"filename": "launch-checklist.md",
		"file": {
			"url": "https://wiki.company.com/docs/launch-checklist",
			"context": "A checklist for internal launch readiness, including legal, engineering, and marketing steps."
		}
	}
}
```

#### Add a `context` field to guide LLM answers

When you include a custom metadata field named `context`, AutoRAG attaches that value to each chunk of the file. When you run an `/ai-search` query, this `context` is passed to the LLM and can be used as additional input when generating an answer.

We recommend using the `context` field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the `context` string.

For example:

```json
{
	"context": "summary: 'Checklist for internal product launch readiness, including legal, engineering, and marketing steps.'; url: 'https://wiki.company.com/docs/launch-checklist'"
}
```

This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.

Learn more in AutoRAG's [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/#page","headline":"View custom metadata in responses and guide AI-search with context in AutoRAG","description":"You can now view custom metadata in AutoRAG search responses and use a context field to provide additional guidance to AI-generated answers.","url":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/og.png?v=308f5c60e40d5a33","dateModified":"2025-06-19","datePublished":"2025-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
