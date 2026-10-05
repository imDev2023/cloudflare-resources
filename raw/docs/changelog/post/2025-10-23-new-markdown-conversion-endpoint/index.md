---
description: You can now programmatically get a list of all supported file formats that can be converted by our Markdown Conversion utility.
title: "Workers AI Markdown Conversion: New endpoint to list supported formats"
image: https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/og.png?v=88adf33d4e277fdd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 23, 2025

## Workers AI Markdown Conversion: New endpoint to list supported formats

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Developers can now programmatically retrieve a list of all file formats supported by the [Markdown Conversion utility](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) in Workers AI.

You can use the [`env.AI`](https://developers.cloudflare.com/workers-ai/configuration/bindings/) binding:

```typescript
await env.AI.toMarkdown().supported()
```

Or call the REST API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \
  -H 'Authorization: Bearer {API_TOKEN}'
```

Both return a list of file formats that users can convert into Markdown:

```json
[
	{
		"extension": ".pdf",
		"mimeType": "application/pdf",
	},
	{
		"extension": ".jpeg",
		"mimeType": "image/jpeg",
	},
	...
]
```

Learn more about our [Markdown Conversion utility](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/#page","headline":"Workers AI Markdown Conversion: New endpoint to list supported formats","description":"You can now programmatically get a list of all supported file formats that can be converted by our Markdown Conversion utility.","url":"https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/og.png?v=88adf33d4e277fdd","dateModified":"2025-10-23","datePublished":"2025-10-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
