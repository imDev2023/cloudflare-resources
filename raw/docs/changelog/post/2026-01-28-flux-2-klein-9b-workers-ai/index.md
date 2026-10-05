---
description: New ultra-fast FLUX.2 [klein] 9B model on Workers AI
title: Launching FLUX.2 [klein] 9B on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/og.png?v=9b2d1d1e2c5a78cb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 28, 2026

## Launching FLUX.2 \[klein] 9B on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 \[klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.

Read the [BFL blog ↗︎](https://bfl.ai/blog) to learn more about the model itself, or try it out yourself on our [multi modal playground ↗︎](https://multi-modal.ai.cloudflare.com/).

Pricing documentation is available on the [model page](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Workers AI platform specifics

The model hosted on Workers AI is optimized for speed with a **fixed 4-step inference process** and supports up to 4 image inputs. Since this is a distilled model, the `steps` parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 \[dev] and FLUX.2 \[klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.

With the REST API, the multipart form data input looks like this:

```bash
curl --request POST \
  --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'prompt=a sunset at the alps' \
  --form width=1024 \
  --form height=1024
```

With the Workers AI binding, you can use it as such:

```javascript
const form = new FormData();
form.append("prompt", "a sunset with a dog");
form.append("width", "1024");
form.append("height", "1024");

// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');

const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-9b", {
	multipart: {
		body: formStream,
		contentType: formContentType,
	},
});
```

The parameters you can send to the model are detailed here:

<details>

<summary>JSON Schema for Model</summary>



**Required Parameters**

- <code>prompt</code> (string) - Text description of the image to generate

**Optional Parameters**

- <code>input_image_0</code> (string) - Binary image
- <code>input_image_1</code> (string) - Binary image
- <code>input_image_2</code> (string) - Binary image
- <code>input_image_3</code> (string) - Binary image
- <code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely
- <code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920
- <code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920
- <code>seed</code> (integer) - Seed for reproducibility

**Note:** Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.

</details>

#### Multi-reference images

The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 \[dev] and FLUX.2 \[klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.

For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.

You must name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.

```bash
curl --request POST \
  --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'prompt=take the subject of image 1 and style it like image 0' \
  --form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \
  --form input_image_1=@/Users/johndoe/Desktop/me.png \
  --form width=1024 \
  --form height=1024
```

Through Workers AI Binding:

```javascript
//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
  const reader = stream.getReader();
  const chunks = [];

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
  }

  return new Blob(chunks, { type: contentType });
}

const image0 = await fetch("http://image-url");
const image1 = await fetch("http://image-url");
const form = new FormData();

const image_blob0 = await streamToBlob(image0.body, "image/png");
const image_blob1 = await streamToBlob(image1.body, "image/png");
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')

// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');

const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-9b", {
    multipart: {
        body: formStream,
        contentType: formContentType
    }
})
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/#page","headline":"Launching FLUX.2 [klein] 9B on Workers AI","description":"New ultra-fast FLUX.2 [klein] 9B model on Workers AI","url":"https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/og.png?v=9b2d1d1e2c5a78cb","dateModified":"2026-01-28","datePublished":"2026-01-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
