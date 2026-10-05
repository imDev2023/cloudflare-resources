---
description: Transform videos directly in Workers without requiring public URL access to source files.
title: Media Transformations binding for Workers
image: https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/og.png?v=e12f723f21105709
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2026

## Media Transformations binding for Workers

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use a Workers binding to transform videos with Media Transformations. This allows you to resize, crop, extract frames, and extract audio from videos stored anywhere, even in private locations like R2 buckets.

The Media Transformations binding is useful when you want to:

- Transform videos stored in private or protected sources
- Optimize videos and store the output directly back to R2 for re-use
- Extract still frames for classification or description with Workers AI
- Extract audio tracks for transcription using Workers AI

To get started, add the Media binding to your Wrangler configuration:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "media": {
    "binding": "MEDIA"
  }
}
```

```toml
[media]
binding = "MEDIA"
```

Then use the binding in your Worker to transform videos:

```js
export default {
	async fetch(request, env) {
		const video = await env.R2_BUCKET.get("input.mp4");

		const result = env.MEDIA.input(video.body)
			.transform({ width: 480, height: 270 })
			.output({ mode: "video", duration: "5s" });

		return await result.response();
	},
};
```

```ts
export default {
	async fetch(request, env) {
		const video = await env.R2_BUCKET.get("input.mp4");

		const result = env.MEDIA.input(video.body)
			.transform({ width: 480, height: 270 })
			.output({ mode: "video", duration: "5s" });

		return await result.response();
	},
};
```

Output modes include `video` for optimized MP4 clips, `frame` for still images, `spritesheet` for multiple frames, and `audio` for M4A extraction.

For more information, refer to the [Media Transformations binding documentation](https://developers.cloudflare.com/stream/transform-videos/bindings/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/#page","headline":"Media Transformations binding for Workers","description":"Transform videos directly in Workers without requiring public URL access to source files.","url":"https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/og.png?v=e12f723f21105709","dateModified":"2026-03-18","datePublished":"2026-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
