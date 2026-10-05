---
description: Redirect a response based on the country code in the header of a visitor.
title: Country code redirect
image: https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/og.png?v=59e4cb9f41a7e592
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Country code redirect

Redirect a response based on the country code in the header of a visitor.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
export default {
	async fetch(request) {
		/**
		 * A map of the URLs to redirect to
		 * @param {Object} countryMap
		 */
		const countryMap = {
			// Replace the country codes and target URLs with ones that apply to your case.
			US: "https://example.com/us",
			EU: "https://example.com/eu",
		};

		// Use the cf object to obtain the country of the request
		// more on the cf object: https://developers.cloudflare.com/workers/runtime-apis/request#incomingrequestcfproperties
		const country = request.cf.country;

		// If country is not null and is defined in the country map above, redirect.
		if (country != null && country in countryMap) {
			const url = countryMap[country];
			// Remove this logging statement from your final output.
			console.log(
				`Based on ${country}-based request, your user would go to ${url}.`,
			);
			return Response.redirect(url);

			// If request country not in map, return another page.
		} else {
			return fetch("https://example.com", request);
		}
	},
};
```
