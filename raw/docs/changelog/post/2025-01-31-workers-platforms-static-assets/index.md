---
description: Workers for Platforms customers can now serve static assets for User Workers directly from Cloudflare's global edge
title: Workers for Platforms now supports Static Assets
image: https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/og.png?v=5c4e9c13fc3e760a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 31, 2025

## Workers for Platforms now supports Static Assets

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.

This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.

#### What you can build

**Static Sites:** Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.

**Full-Stack Applications:** Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.

*index.jsjs*

```js
export default {
	async fetch(request, env) {
		const url = new URL(request.url);

		// Check real-time inventory
		if (url.pathname === "/api/inventory/check") {
			const product = url.searchParams.get("product");
			const inventory = await env.INVENTORY_KV.get(product);
			return new Response(inventory);
		}

		// Serve static assets (HTML, CSS, images)
		return env.ASSETS.fetch(request);
	},
};
```

*index.tsts*

```ts
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Check real-time inventory
    if (url.pathname === '/api/inventory/check') {
      const product = url.searchParams.get('product');
      const inventory = await env.INVENTORY_KV.get(product);
      return new Response(inventory);
    }

    // Serve static assets (HTML, CSS, images)
    return env.ASSETS.fetch(request);
  }
};
```

**Get Started:** Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our [Workers for Platforms documentation. ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/#page","headline":"Workers for Platforms now supports Static Assets","description":"Workers for Platforms customers can now serve static assets for User Workers directly from Cloudflare's global edge","url":"https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/og.png?v=5c4e9c13fc3e760a","dateModified":"2025-01-31","datePublished":"2025-01-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
