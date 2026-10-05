---
description: "You can now interact with the Images API directly in your Worker with Image Bindings.\n"
title: Bind the Images API to your Worker
image: https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/og.png?v=ffaa53faa11a82de
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2025

## Bind the Images API to your Worker

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now [interact with the Images API](https://developers.cloudflare.com/images/optimization/binding/) directly in your Worker.

This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.

The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:

```jsonc
{
	"images": {
		"binding": "IMAGES", // i.e. available in your Worker on env.IMAGES
	},
}
```

```toml
[images]
binding = "IMAGES"
```

Within your Worker code, you can interact with this binding by using `env.IMAGES`.

Here's how you can rotate, resize, and blur an image, then output the image as AVIF:

```ts
const info = await env.IMAGES.info(stream);
// stream contains a valid image, and width/height is available on the info object

const response = (
	await env.IMAGES.input(stream)
		.transform({ rotate: 90 })
		.transform({ width: 128 })
		.transform({ blur: 20 })
		.output({ format: "image/avif" })
).response();

return response;
```

For more information, refer to [Images Bindings](https://developers.cloudflare.com/images/optimization/binding/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/#page","headline":"Bind the Images API to your Worker","description":"You can now interact with the Images API directly in your Worker with Image Bindings.","url":"https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/og.png?v=ffaa53faa11a82de","dateModified":"2025-02-24","datePublished":"2025-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
