---
description: You can now convert documents in multiple formats to Markdown using the toMarkdown utility method in Workers AI.
title: Markdown conversion in Workers AI
image: https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/og.png?v=e1c270965fbce1df
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 20, 2025

## Markdown conversion in Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the `toMarkdown` utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.

You can call this new tool using a binding by calling `env.AI.toMarkdown()` or the using the [REST API](https://developers.cloudflare.com/api/resources/ai/) endpoint.

In this example, we fetch a PDF document and an image from R2 and feed them both to `env.AI.toMarkdown()`. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.

```typescript
import { Env } from "./env";

export default {
	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf
		const pdf = await env.R2.get("somatosensory.pdf");

		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg
		const cat = await env.R2.get("cat.jpeg");

		return Response.json(
			await env.AI.toMarkdown([
				{
					name: "somatosensory.pdf",
					blob: new Blob([await pdf.arrayBuffer()], {
						type: "application/octet-stream",
					}),
				},
				{
					name: "cat.jpeg",
					blob: new Blob([await cat.arrayBuffer()], {
						type: "application/octet-stream",
					}),
				},
			]),
		);
	},
};
```

This is the result:

```json
[
	{
		"name": "somatosensory.pdf",
		"mimeType": "application/pdf",
		"format": "markdown",
		"tokens": 0,
		"data": "# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase..."
	},
	{
		"name": "cat.jpeg",
		"mimeType": "image/jpeg",
		"format": "markdown",
		"tokens": 0,
		"data": "The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat's eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat's facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people."
	}
]
```

See [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) for more information on supported formats, REST API and pricing.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/#page","headline":"Markdown conversion in Workers AI","description":"You can now convert documents in multiple formats to Markdown using the toMarkdown utility method in Workers AI.","url":"https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/og.png?v=e1c270965fbce1df","dateModified":"2025-03-20","datePublished":"2025-03-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
