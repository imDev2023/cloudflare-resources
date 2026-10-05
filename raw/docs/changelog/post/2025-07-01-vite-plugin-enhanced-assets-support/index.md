---
description: The Cloudflare Vite plugin now supports using all of Vite's static assets features in your Worker
title: Enhanced support for static assets with the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/og.png?v=5399133b6df7c824
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2025

## Enhanced support for static assets with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use any of Vite's [static asset handling ↗︎](https://vite.dev/guide/assets) features in your Worker as well as in your frontend. These include importing assets as URLs, importing as strings and importing from the `public` directory as well as inlining assets.

Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.

Here is an example that fetches an imported asset using the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding) and modifies the response.

```ts
// Import the asset URL
// This returns the resolved path in development and production
import myImage from "./my-image.png";

export default {
	async fetch(request, env) {
		// Fetch the asset using the binding
		const response = await env.ASSETS.fetch(new URL(myImage, request.url));
		// Create a new `Response` object that can be modified
		const modifiedResponse = new Response(response.body, response);
		// Add an additional header
		modifiedResponse.headers.append("my-header", "imported-asset");

		// Return the modified response
		return modifiedResponse;
	},
};
```

Refer to [Static Assets](https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/) in the Cloudflare Vite plugin docs for more info.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/#page","headline":"Enhanced support for static assets with the Cloudflare Vite plugin","description":"The Cloudflare Vite plugin now supports using all of Vite's static assets features in your Worker","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/og.png?v=5399133b6df7c824","dateModified":"2025-07-01","datePublished":"2025-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
