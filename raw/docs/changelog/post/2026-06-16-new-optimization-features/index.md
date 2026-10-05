---
description: "New composite modes, percentage-based overlay dimensions, fit modes, and AI upscaling.\n"
title: New optimization features in Images
image: https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/og.png?v=267daedab564767f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2026

## New optimization features in Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

These updates introduce new features for optimizing and manipulating with Images:

- **New `composite` option:** Control how [overlays are blended](https://developers.cloudflare.com/images/optimization/draw-overlays/#composite) with the base image.
- **Percentage widths:** Set the dimensions of an overlay as [a fraction of the dimensions](https://developers.cloudflare.com/images/optimization/draw-overlays/#width-and-height) of the base image.
- **New `fit` modes:** Use [`aspect-crop`](https://developers.cloudflare.com/images/optimization/features/#aspect-crop) to always preserve the target aspect ratio or [`scale-up`](https://developers.cloudflare.com/images/optimization/features/#scale-up) to always enlarge images.
- **New `upscale` parameter:** Apply [AI upscaling](https://developers.cloudflare.com/images/optimization/features/#upscale) to produce sharper, more detailed results when enlarging images.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/#page","headline":"New optimization features in Images","description":"New composite modes, percentage-based overlay dimensions, fit modes, and AI upscaling.","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/og.png?v=267daedab564767f","dateModified":"2026-06-16","datePublished":"2026-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
