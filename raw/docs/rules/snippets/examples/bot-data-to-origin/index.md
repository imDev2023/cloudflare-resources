---
description: Send [Bots](/bots/) information to your origin. Refer to [Bot Management variables](/bots/reference/bot-management-variables/) for a full list of available fields.
title: Send Bot Management information to origin
image: https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/og.png?v=5ee1a94c309481d8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Send Bot Management information to origin

Send [Bots](https://developers.cloudflare.com/bots/) information to your origin. Refer to [Bot Management variables](https://developers.cloudflare.com/bots/reference/bot-management-variables/) for a full list of available fields.

Last updated Mar 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
export default {
	async fetch(request) {
		// Clone the original request to construct a new request
		const newRequest = new Request(request);
		// Set Bot Management headers on a new request to the origin: https://developers.cloudflare.com/bots/reference/bot-management-variables/#workers-variables
		newRequest.headers.set("bot-score", request.cf.botManagement.score); // bot score (integer)
		newRequest.headers.set(
			"verified-bot",
			request.cf.botManagement.verifiedBot,
		); // verified bot (boolean)
		newRequest.headers.set("ja4", request.cf.botManagement.ja4); // JA4 fingerprint hash (string)
		// Serve response to the new request from the origin
		return await fetch(newRequest);
	},
};
```
