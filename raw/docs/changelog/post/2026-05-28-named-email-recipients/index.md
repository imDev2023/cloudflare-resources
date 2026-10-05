---
description: You can now include display names on to, cc, bcc, and from addresses when sending emails via the Workers binding or REST API.
title: Send emails with named recipient addresses
image: https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/og.png?v=5b4fc73edafc3c9a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## Send emails with named recipient addresses

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send emails with display names on recipient addresses in addition to the existing `from` support. Pass an object with `email` and an optional `name` field for `to`, `cc`, `bcc`, `replyTo`, or `from`:

*src/index.jsjs*

```js
export default {
	async fetch(request, env) {
		const response = await env.EMAIL.send({
			from: { email: "support@example.com", name: "Support Team" },
			to: { email: "jane@example.com", name: "Jane Doe" },
			cc: [
				"manager@company.com",
				{ email: "team@company.com", name: "Engineering Team" },
			],
			subject: "Welcome!",
			html: "<h1>Thanks for joining!</h1>",
			text: "Thanks for joining!",
		});

		return Response.json({ messageId: response.messageId });
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request, env): Promise<Response> {
		const response = await env.EMAIL.send({
			from: { email: "support@example.com", name: "Support Team" },
			to: { email: "jane@example.com", name: "Jane Doe" },
			cc: [
				"manager@company.com",
				{ email: "team@company.com", name: "Engineering Team" },
			],
			subject: "Welcome!",
			html: "<h1>Thanks for joining!</h1>",
			text: "Thanks for joining!",
		});

		return Response.json({ messageId: response.messageId });
	},
} satisfies ExportedHandler<Env>;
```

Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.

Refer to the [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) and [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) documentation for full request examples.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/#page","headline":"Send emails with named recipient addresses","description":"You can now include display names on to, cc, bcc, and from addresses when sending emails via the Workers binding or REST API.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/og.png?v=5b4fc73edafc3c9a","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
