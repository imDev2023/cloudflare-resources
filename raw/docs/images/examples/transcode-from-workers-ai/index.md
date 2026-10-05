---
description: Transcode an image from Workers AI before uploading to R2
title: Transcode images
image: https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/og.png?v=fe0232bbfa16400d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Transcode images

Transcode an image from Workers AI before uploading to R2

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

```js
const stream = await env.AI.run("@cf/bytedance/stable-diffusion-xl-lightning", {
	prompt: YOUR_PROMPT_HERE,
});

// Convert to AVIF
const image = (
	await env.IMAGES.input(stream).output({ format: "image/avif" })
).response();

const fileName = "image.avif";

// Upload to R2
await env.R2.put(fileName, image.body);
```
