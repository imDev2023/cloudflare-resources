---
description: Interact with Cloudflare Stream videos directly from Workers without API tokens or HTTP requests.
title: Introducing Stream Bindings for Workers
image: https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/og.png?v=e8a0cd8dbe733c81
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## Introducing Stream Bindings for Workers

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.

Use the Stream binding when you want to:

- Upload videos from URLs or create basic direct upload links for end users
- Generate signed playback tokens without managing signing keys
- Manage video metadata, captions, downloads, and watermarks
- Build video pipelines entirely within Workers

To get started, add the Stream binding to your Wrangler configuration:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "stream": {
    "binding": "STREAM"
  }
}
```

```toml
[stream]
binding = "STREAM"
```

**Generate a video with AI and upload directly to Stream** or send a URL of a file you already have:

```js
const aiResponse = await env.AI.run(
	"google/veo-3.1",
	{
		prompt: "A dog walking next to a river",
		duration: "10s",
		aspect_ratio: "16:9",
		resolution: "1080p",
		generate_audio: true,
	},
	{
		gateway: { id: "experiments" },
	},
);

// Veo will return a URL of the generated asset.
const videoUrl = aiResponse.result.video;

// Alternative option: a video of the Austin Office mobile
// const videoUrl = 'https://pub-d9fcbc1abcd244c1821f38b99017347f.r2.dev/aus-mobile.mp4';

// Upload to Stream by providing a URL
const streamVideo = await env.STREAM.upload(videoUrl);

// The streamVideo response will include the video ID, playback and manifest
// URLs, and other information, just like the REST API.
```

```ts
const aiResponse = await env.AI.run(
	'google/veo-3.1',
	{
		prompt: 'A dog walking next to a river',
		duration: '10s',
		aspect_ratio: '16:9',
		resolution: '1080p',
		generate_audio: true,
	},
	{
		gateway: { id: 'experiments' },
	},
);

// Veo will return a URL of the generated asset.
const videoUrl = aiResponse.result.video;

// Alternative option: a video of the Austin Office mobile
// const videoUrl = 'https://pub-d9fcbc1abcd244c1821f38b99017347f.r2.dev/aus-mobile.mp4';

// Upload to Stream by providing a URL
const streamVideo = await env.STREAM.upload(videoUrl);

// The streamVideo response will include the video ID, playback and manifest
// URLs, and other information, just like the REST API.
```

**Generate a signed URL without using a signing key** or an API call:

```js
const video_id = "ce800be43a9772f4bb02f35b860fb516";
const token = await env.STREAM.video(video_id).generateToken();

// Use the "token" in an iframe embed code, manifest URL, or thumbnail:
const embedUrl = `https://customer-igynxd2rwhmuoxw8.cloudflarestream.com/${token}/iframe`;
```

```ts
const video_id = 'ce800be43a9772f4bb02f35b860fb516';
const token = await env.STREAM.video(video_id).generateToken();

// Use the "token" in an iframe embed code, manifest URL, or thumbnail:
const embedUrl = `https://customer-igynxd2rwhmuoxw8.cloudflarestream.com/${token}/iframe`;
```

**Get and set video properties** easily:

```js
const video_id = "46c8b7f480d410840758c1cb14a72e47";
const result = await env.STREAM.video(video_id).details();

await env.STREAM.video(video_id).update({
	meta: { name: "sample video" },
});
```

```ts
const video_id = '46c8b7f480d410840758c1cb14a72e47';
const result = await env.STREAM.video(video_id).details();

await env.STREAM.video(video_id).update({
  meta: { name: 'sample video' }
});
```

For setup instructions and the full API reference, refer to [Bind to Workers API](https://developers.cloudflare.com/stream/manage-video-library/bindings/).

#### Get started with your Agent

> Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the Stream binding to get info based on the ID, and leverage video.meta.name as the page title.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/#page","headline":"Introducing Stream Bindings for Workers","description":"Interact with Cloudflare Stream videos directly from Workers without API tokens or HTTP requests.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/og.png?v=e8a0cd8dbe733c81","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
