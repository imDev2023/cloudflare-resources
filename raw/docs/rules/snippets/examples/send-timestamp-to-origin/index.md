---
description: Convert timestamp to hexadecimal format and send it as a custom header to the origin.
title: Send timestamp to origin as a custom header
image: https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/og.png?v=6754ddc47fdc1662
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Send timestamp to origin as a custom header

Convert timestamp to hexadecimal format and send it as a custom header to the origin.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
export default {
	async fetch(request) {
		// Get the current timestamp
		const timestamp = Date.now();

		// Convert the timestamp to hexadecimal format
		const hexTimestamp = timestamp.toString(16);

		// Clone the request and add the custom header
		const modifiedRequest = new Request(request, {
			headers: new Headers(request.headers),
		});
		modifiedRequest.headers.set("X-Hex-Timestamp", hexTimestamp);

		// Log the custom header for debugging
		console.log(`X-Hex-Timestamp: ${hexTimestamp}`);

		// Pass the modified request to the origin
		const response = await fetch(modifiedRequest);

		return response;
	},
};
```
