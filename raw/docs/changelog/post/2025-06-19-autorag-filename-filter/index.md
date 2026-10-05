---
description: You can now filter AutoRAG search queries by file name, allowing you to control which files can be retrieved for a given query.
title: Filter your AutoRAG search by file name
image: https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/og.png?v=2b75bae2da6b83c5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2025

## Filter your AutoRAG search by file name

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [AutoRAG](https://developers.cloudflare.com/ai-search/), you can now [filter](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) by an object's file name using the `filename` attribute, giving you more control over which files are searched for a given query.

This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.

For example, your search query may look like:

```js
const response = await env.AI.autorag("my-autorag").search({
	query: "what is the project deadline?",
	filters: {
		type: "eq",
		key: "filename",
		value: "project-alpha-roadmap.md",
	},
});
```

This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.

Learn more in AutoRAG's [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/#page","headline":"Filter your AutoRAG search by file name","description":"You can now filter AutoRAG search queries by file name, allowing you to control which files can be retrieved for a given query.","url":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/og.png?v=2b75bae2da6b83c5","dateModified":"2025-06-19","datePublished":"2025-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
