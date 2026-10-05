---
description: "The Images binding now follows the same unique-transformation billing model as URL-based transformations, and calls to `.info()` are free.\n"
title: Images binding is now billed per unique transformation
image: https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/og.png?v=92ab4f00bfeafe21
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Images binding is now billed per unique transformation

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Images binding](https://developers.cloudflare.com/images/optimization/binding/) is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.

Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.

Calls to [`.info()`](https://developers.cloudflare.com/images/optimization/binding/#infostream) are no longer billed.

For more information, refer to [Images pricing](https://developers.cloudflare.com/images/pricing/#images-transformed) and the [Images binding documentation](https://developers.cloudflare.com/images/optimization/binding/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/#page","headline":"Images binding is now billed per unique transformation","description":"The Images binding now follows the same unique-transformation billing model as URL-based transformations, and calls to .info() are free.","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/og.png?v=92ab4f00bfeafe21","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
