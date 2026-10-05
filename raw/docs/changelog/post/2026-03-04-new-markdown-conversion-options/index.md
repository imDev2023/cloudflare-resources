---
description: Control how images, HTML, and PDFs are processed when converting to Markdown
title: New conversion options for Markdown Conversion
image: https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/og.png?v=5d64f9e20f876537
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 4, 2026

## New conversion options for Markdown Conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now customize how the [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service processes different file types by passing a `conversionOptions` object.

Available options:

- **Images**: Set the language for AI-generated image descriptions
- **HTML**: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links
- **PDF**: Exclude metadata from the output

Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:

```js
await env.AI.toMarkdown(
	{ name: "page.html", blob: new Blob([html]) },
	{
		conversionOptions: {
			html: { cssSelector: "article.content" },
			image: { descriptionLanguage: "es" },
		},
	},
);
```

```typescript
await env.AI.toMarkdown(
	{ name: "page.html", blob: new Blob([html]) },
	{
		conversionOptions: {
			html: { cssSelector: "article.content" },
			image: { descriptionLanguage: "es" },
		},
	},
);
```

Or call the REST API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
  -H 'Authorization: Bearer {API_TOKEN}' \
  -F 'files=@index.html' \
  -F 'conversionOptions={"html": {"cssSelector": "article.content"}}'
```

For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/#page","headline":"New conversion options for Markdown Conversion","description":"Control how images, HTML, and PDFs are processed when converting to Markdown","url":"https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/og.png?v=5d64f9e20f876537","dateModified":"2026-03-04","datePublished":"2026-03-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
