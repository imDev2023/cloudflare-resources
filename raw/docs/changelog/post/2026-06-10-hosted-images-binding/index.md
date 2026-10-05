---
description: "Upload, list, retrieve, update, and delete hosted images directly from a Worker using the Images binding.\n"
title: Manage hosted images with the Images binding
image: https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/og.png?v=02c4df3424a162f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2026

## Manage hosted images with the Images binding

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.

The `env.IMAGES.hosted` namespace supports the following storage and management operations:

- [`.upload(image, options)`](https://developers.cloudflare.com/images/storage/binding/#uploadimage-options) — Upload a new image to your account.
- [`.list(options)`](https://developers.cloudflare.com/images/storage/binding/#listoptions) — List images with pagination.
- [`.image(imageId).details()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddetails) — Get image metadata.
- [`.image(imageId).bytes()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidbytes) — Stream the original image bytes.
- [`.image(imageId).update(options)`](https://developers.cloudflare.com/images/storage/binding/#imageimageidupdateoptions) — Update metadata or access controls.
- [`.image(imageId).delete()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete) — Delete an image.

For example, you can upload an image from a request body and return its metadata:

```ts
const image = await env.IMAGES.hosted.upload(request.body, {
	filename: "upload.jpg",
	metadata: { source: "worker" },
});

return Response.json(image);
```

Or retrieve and serve the original bytes of a hosted image:

```ts
const bytes = await env.IMAGES.hosted.image("IMAGE_ID").bytes();
return new Response(bytes);
```

For more information, refer to the [Images binding](https://developers.cloudflare.com/images/storage/binding/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/#page","headline":"Manage hosted images with the Images binding","description":"Upload, list, retrieve, update, and delete hosted images directly from a Worker using the Images binding.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/og.png?v=02c4df3424a162f4","dateModified":"2026-06-10","datePublished":"2026-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
