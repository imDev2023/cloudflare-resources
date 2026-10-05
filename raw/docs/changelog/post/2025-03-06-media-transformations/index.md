---
description: "Dynamically optimize, clip, and resize video from any origin, no storage migration needed.\n"
title: Introducing Media Transformations from Cloudflare Stream
image: https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/og.png?v=045db946f25b8d86
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 6, 2025

## Introducing Media Transformations from Cloudflare Stream

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are thrilled to announce Media Transformations, a new service that brings the magic of [Image Transformations](https://developers.cloudflare.com/images/optimization/transformations/overview/) to *short-form video files,* wherever they are stored!

For customers with a huge volume of short video — generative AI output, e-commerce product videos, social media clips, or short marketing content — uploading those assets to Stream is not always practical. Sometimes, the greatest friction to getting started was the thought of all that migrating. Customers want a simpler solution that retains their current storage strategy to deliver small, optimized MP4 files. Now you can do that with Media Transformations.

To transform a video or image, [enable transformations](https://developers.cloudflare.com/stream/transform-videos/#getting-started) for your zone, then make a simple request with a specially formatted URL. The result is an MP4 that can be used in an HTML video element without a player library. If your zone already has Image Transformations enabled, then it is ready to optimize videos with Media Transformations, too.

*URL formattext*

```text
https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>
```

For example, we have a short video of the mobile in Austin's office. The original is nearly 30 megabytes and wider than necessary for this layout. Consider a simple width adjustment:

*Example URLtext*

```text
https://example.com/cdn-cgi/media/width=640/<SOURCE-VIDEO>
https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4
```

The result is less than 3 megabytes, properly sized, and delivered dynamically so that customers do not have to manage the creation and storage of these transformed assets.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/#page","headline":"Introducing Media Transformations from Cloudflare Stream","description":"Dynamically optimize, clip, and resize video from any origin, no storage migration needed.","url":"https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/og.png?v=045db946f25b8d86","dateModified":"2025-03-06","datePublished":"2025-03-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
