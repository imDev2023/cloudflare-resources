---
description: "Rasterize text, sign private image URLs, create Direct Creator Upload links, filter hosted images by custom metadata, and set response headers directly from a Worker.\n"
title: "New in Images: text rasterization and updates to the binding"
image: https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/og.png?v=e859610fe8e84c0c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## New in Images: text rasterization and updates to the binding

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've added more ways to manage and manipulate images with the [Images binding](https://developers.cloudflare.com/images/optimization/binding/). Here's what's new:

**Render text into an image.** Output a string of text into its own image or draw it over another image.

- Use the [`.text()`](https://developers.cloudflare.com/images/optimization/binding/#textcontent-options) method to rasterize text with the Images binding.
- Style content using the `font`, `size`, and `color` options.
- The [`draw`](https://developers.cloudflare.com/images/optimization/draw-overlays/#draw-with-cfimage) array in `cf.image` now accepts a `text` key.

**Manage hosted images without an API token.**

- **Metadata filtering:** Pass `filter.metadata` to [`.list()`](https://developers.cloudflare.com/images/storage/binding/#listoptions) to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, `priority: { gte: 2, lte: 5 }`.
- **Server-side signing:** Get a signed URL for a private image with [`.signedUrl()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidsignedurloptions).
- **User uploads:** Create a Direct Creator Upload link with [`.createDirectUpload()`](https://developers.cloudflare.com/images/storage/binding/#createdirectuploadoptions) so that a client can upload an image to your storage.

**Set headers in a single call.**

- Pass a `headers` option to [`.response()`](https://developers.cloudflare.com/images/optimization/binding/#responseoptions) to set headers without rebuilding the `Response`.
- `Content-Type` is always taken from the optimized image and can't be overridden by a specified header.
- Set `Cache-Control` with [Workers Cache](https://developers.cloudflare.com/workers/cache/) to cache your optimized image at the edge.

For more information, refer to [Optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/), [Draw overlays and watermarks](https://developers.cloudflare.com/images/optimization/draw-overlays/), and [Manage hosted images with Workers](https://developers.cloudflare.com/images/storage/binding/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/#page","headline":"New in Images: text rasterization and updates to the binding","description":"Rasterize text, sign private image URLs, create Direct Creator Upload links, filter hosted images by custom metadata, and set response headers directly from a Worker.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/og.png?v=e859610fe8e84c0c","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
