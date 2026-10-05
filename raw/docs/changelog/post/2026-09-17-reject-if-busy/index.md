---
description: Fail synchronous inference requests instead of waiting for capacity.
title: Reject busy synchronous inference requests
image: https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/og.png?v=1f6e34f0b840ee85
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 17, 2026

## Reject busy synchronous inference requests

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `rejectIfBusy` option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.

Pass the option as the third argument to the Workers AI binding:

```js
const response = await env.AI.run(
	"@cf/google/gemma-4-26b-a4b-it",
	{
		messages: [{ role: "user", content: "Explain capacity queues." }],
	},
	{ rejectIfBusy: true },
);
```

```ts
const response = await env.AI.run(
	"@cf/google/gemma-4-26b-a4b-it",
	{
		messages: [{ role: "user", content: "Explain capacity queues." }],
	},
	{ rejectIfBusy: true },
);
```

For the native REST API, add the option to the request body:

```bash
curl --request POST \
  --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "messages": [{ "role": "user", "content": "Explain capacity queues." }],
    "options": { "rejectIfBusy": true }
  }'
```

Refer to [Reject busy requests](https://developers.cloudflare.com/workers-ai/features/reject-if-busy/) for OpenAI-compatible usage and error behavior.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/#page","headline":"Reject busy synchronous inference requests","description":"Fail synchronous inference requests instead of waiting for capacity.","url":"https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/og.png?v=1f6e34f0b840ee85","dateModified":"2026-09-17","datePublished":"2026-09-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
