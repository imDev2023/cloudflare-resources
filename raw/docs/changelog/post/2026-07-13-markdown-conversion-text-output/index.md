---
description: Choose between Markdown and plain text output when converting documents
title: Plain text output for Markdown Conversion
image: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/og.png?v=d351b3e3dcdd0634
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 10, 2026

## Plain text output for Markdown Conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service now supports a new `output` conversion option that controls the format of the converted content.

Set `output.format` to `text` to receive plain text with Markdown syntax removed. The default value is `markdown`, so existing conversions are unchanged.

Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:

```js
await env.AI.toMarkdown(
	{ name: "page.html", blob: new Blob([html]) },
	{
		conversionOptions: {
			output: { format: "text" },
		},
	},
);
```

```typescript
await env.AI.toMarkdown(
	{ name: "page.html", blob: new Blob([html]) },
	{
		conversionOptions: {
			output: { format: "text" },
		},
	},
);
```

Or call the REST API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
  -H 'Authorization: Bearer {API_TOKEN}' \
  -F 'files=@index.html' \
  -F 'conversionOptions={"output": {"format": "text"}}'
```

When you request text output, the `format` field of each result is set to `text`. For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#output).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/#page","headline":"Plain text output for Markdown Conversion","description":"Choose between Markdown and plain text output when converting documents","url":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/og.png?v=d351b3e3dcdd0634","dateModified":"2026-07-10","datePublished":"2026-07-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
