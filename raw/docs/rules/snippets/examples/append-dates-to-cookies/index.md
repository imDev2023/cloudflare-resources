---
description: Dynamically set a cookie expiration and test group.
title: Append dates to cookies to use with A/B testing
image: https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/og.png?v=72b4197b81f549c5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Append dates to cookies to use with A/B testing

Dynamically set a cookie expiration and test group.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
export default {
	async fetch(request) {
		const response = await fetch(request);

		// Clone the response so that it is no longer immutable
		const newResponse = new Response(response.body, response);

		// Define the dynamic expiry time. 24 h * 60 m * 60 s * 1000 ms = 86,400,000 ms
		const expiry = new Date(Date.now() + 7 * 86400000).toUTCString();
		// Define the group variable. "A" if the request header "userGroup" is "premium", "B" if otherwise.
		const group = request.headers.get("userGroup") == "premium" ? "A" : "B";

		// Append the custom header with the values
		newResponse.headers.append(
			"Set-Cookie",
			`testGroup=${group}; Expires=${expiry}; Path=/`,
		);

		return newResponse;
	},
};
```
