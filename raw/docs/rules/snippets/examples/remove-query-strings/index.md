---
description: Remove certain query strings from a request before passing to the origin.
title: Remove query strings before sending request to origin
image: https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/og.png?v=86547b76a32b7b9a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Remove query strings before sending request to origin

Remove certain query strings from a request before passing to the origin.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
export default {
	async fetch(request) {
		// Define the query strings you want to remove
		const queryStringsToRemove = ["utm_source", "utm_medium", "utm_campaign"];

		// Get the URL from the request
		const url = new URL(request.url);

		// Remove the specified query strings
		queryStringsToRemove.forEach((query) => {
			url.searchParams.delete(query);
		});

		// Create a new request with the modified URL
		const modifiedRequest = new Request(url, request);

		// Pass the modified request to the origin
		const response = await fetch(modifiedRequest);

		return response;
	},
};
```
