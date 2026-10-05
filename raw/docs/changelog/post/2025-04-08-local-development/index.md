---
description: Developers can now use wrangler to do local development for Email Workers.
title: Local development support for Email Workers
image: https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/og.png?v=ad8a745c953237fc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2025

## Local development support for Email Workers

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Email Workers enables developers to programmatically take action on anything that hits their email inbox. If you're building with Email Workers, you can now test the behavior of an Email Worker script, receiving, replying and sending emails in your local environment using `wrangler dev`.

Below is an example that shows you how you can receive messages using the `email()` handler and parse them using [postal-mime ↗︎](https://www.npmjs.com/package/postal-mime):

```ts
import * as PostalMime from "postal-mime";

export default {
	async email(message, env, ctx) {
		const parser = new PostalMime.default();
		const rawEmail = new Response(message.raw);
		const email = await parser.parse(await rawEmail.arrayBuffer());
		console.log(email);
	},
};
```

Now when you run `npx wrangler dev`, wrangler will expose a local `/cdn-cgi/local/email` endpoint that you can `POST` email messages to and trigger your Worker's `email()` handler:

```bash
curl -X POST 'http://localhost:8787/cdn-cgi/local/email' \
  --url-query 'from=sender@example.com' \
  --url-query 'to=recipient@example.com' \
  --header 'Content-Type: application/json' \
  --data-raw 'Received: from smtp.example.com (127.0.0.1)
        by cloudflare-email.com (unknown) id 4fwwffRXOpyR
        for <recipient@example.com>; Tue, 27 Aug 2024 15:50:20 +0000
From: "John" <sender@example.com>
Reply-To: sender@example.com
To: recipient@example.com
Subject: Testing Email Workers Local Dev
Content-Type: text/html; charset="windows-1252"
X-Mailer: Curl
Date: Tue, 27 Aug 2024 08:49:44 -0700
Message-ID: <6114391943504294873000@ZSH-GHOSTTY>

Hi there'
```

This is what you get in the console:

```json
{
	"headers": [
		{
			"key": "received",
			"value": "from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for <recipient@example.com>; Tue, 27 Aug 2024 15:50:20 +0000"
		},
		{ "key": "from", "value": "\"John\" <sender@example.com>" },
		{ "key": "reply-to", "value": "sender@example.com" },
		{ "key": "to", "value": "recipient@example.com" },
		{ "key": "subject", "value": "Testing Email Workers Local Dev" },
		{ "key": "content-type", "value": "text/html; charset=\"windows-1252\"" },
		{ "key": "x-mailer", "value": "Curl" },
		{ "key": "date", "value": "Tue, 27 Aug 2024 08:49:44 -0700" },
		{
			"key": "message-id",
			"value": "<6114391943504294873000@ZSH-GHOSTTY>"
		}
	],
	"from": { "address": "sender@example.com", "name": "John" },
	"to": [{ "address": "recipient@example.com", "name": "" }],
	"replyTo": [{ "address": "sender@example.com", "name": "" }],
	"subject": "Testing Email Workers Local Dev",
	"messageId": "<6114391943504294873000@ZSH-GHOSTTY>",
	"date": "2024-08-27T15:49:44.000Z",
	"html": "Hi there\n",
	"attachments": []
}
```

Local development is a critical part of the development flow, and also works for sending, replying and forwarding emails. See [our documentation](https://developers.cloudflare.com/email-service/local-development/routing/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/#page","headline":"Local development support for Email Workers","description":"Developers can now use wrangler to do local development for Email Workers.","url":"https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/og.png?v=ad8a745c953237fc","dateModified":"2025-04-08","datePublished":"2025-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
