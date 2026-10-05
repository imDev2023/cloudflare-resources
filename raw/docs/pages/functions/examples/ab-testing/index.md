---
description: Set up an A/B test by controlling what page is served based on cookies. This version supports passing the request through to test and control on the origin.
title: A/B testing with middleware
image: https://developers.cloudflare.com/pages/functions/examples/ab-testing/og.png?v=4e99f7cbe7eeb7b9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/pages/llms.txt  
> Use this file to discover all available pages before exploring further.

# A/B testing with middleware

Set up an A/B test by controlling what page is served based on cookies. This version supports passing the request through to test and control on the origin.

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/pages/functions/examples/ab-testing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
const cookieName = "ab-test-cookie";
const newHomepagePathName = "/test";

const abTest = async (context) => {
	const url = new URL(context.request.url);
	// if homepage
	if (url.pathname === "/") {
		// if cookie ab-test-cookie=new then change the request to go to /test
		// if no cookie set, pass x% of traffic and set a cookie value to "current" or "new"

		let cookie = request.headers.get("cookie");
		// is cookie set?
		if (cookie && cookie.includes(`${cookieName}=new`)) {
			// pass the request to /test
			url.pathname = newHomepagePathName;
			return context.env.ASSETS.fetch(url);
		} else {
			const percentage = Math.floor(Math.random() * 100);
			let version = "current"; // default version
			// change pathname and version name for 50% of traffic
			if (percentage < 50) {
				url.pathname = newHomepagePathName;
				version = "new";
			}
			// get the static file from ASSETS, and attach a cookie
			const asset = await context.env.ASSETS.fetch(url);
			let response = new Response(asset.body, asset);
			response.headers.append("Set-Cookie", `${cookieName}=${version}; path=/`);
			return response;
		}
	}
	return context.next();
};

export const onRequest = [abTest];
```
