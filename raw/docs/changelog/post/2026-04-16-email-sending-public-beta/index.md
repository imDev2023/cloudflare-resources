---
description: Send transactional emails at scale directly from Cloudflare Workers or the REST API. Email Sending joins Email Routing under the new Cloudflare Email Service.
title: Email Sending now in public beta
image: https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/og.png?v=59b0d9c91043c5dd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 16, 2026

## Email Sending now in public beta

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/)** is now in public beta. Send transactional emails directly from Workers (`env.EMAIL.send()`) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins [Email Routing ↗︎](https://blog.cloudflare.com/introducing-email-routing/) under the new **Cloudflare Email Service** — a single service for sending and receiving email on the Cloudflare developer platform.

Send an email from a Worker in a few lines of code:

*src/index.jsjs*

```js
export default {
	async fetch(request, env) {
		const response = await env.EMAIL.send({
			from: "notifications@yourdomain.com",
			to: "user@example.com",
			subject: "Order confirmed",
			html: "<h1>Your order has been confirmed</h1>",
			text: "Your order has been confirmed.",
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
			from: "notifications@yourdomain.com",
			to: "user@example.com",
			subject: "Order confirmed",
			html: "<h1>Your order has been confirmed</h1>",
			text: "Your order has been confirmed.",
		});

		return Response.json({ messageId: response.messageId });
	},
} satisfies ExportedHandler<Env>;
```

Email Service also integrates with the [Agents SDK](https://developers.cloudflare.com/agents/), giving your agents a native `onEmail` hook to receive, process, and reply to emails. Combined with the new [Email MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare) and Wrangler CLI email commands, any agent can send email regardless of where it runs.

Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the [Email Service documentation](https://developers.cloudflare.com/email-service/) to get started.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/#page","headline":"Email Sending now in public beta","description":"Send transactional emails at scale directly from Cloudflare Workers or the REST API. Email Sending joins Email Routing under the new Cloudflare Email Service.","url":"https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/og.png?v=59b0d9c91043c5dd","dateModified":"2026-04-16","datePublished":"2026-04-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
