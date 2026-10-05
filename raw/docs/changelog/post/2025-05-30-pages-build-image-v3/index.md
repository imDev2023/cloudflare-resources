---
description: A new V3 build image for Cloudflare Pages includes Node.js v22 as the default version
title: Cloudflare Pages builds now provide Node.js v22 by default
image: https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/og.png?v=dd5c0a769c9e0780
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 30, 2025

## Cloudflare Pages builds now provide Node.js v22 by default

[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you use the built-in build system that is part of [Cloudflare Pages](https://developers.cloudflare.com/pages/), the [Build Image](https://developers.cloudflare.com/pages/configuration/build-image/) now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).

If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings > Build & deployments > Build system version in the Cloudflare dashboard for a specific Pages project.

Note that you can always specify a particular version of Node.js or other built-in dependencies by [setting an environment variable](https://developers.cloudflare.com/pages/configuration/build-image/#override-default-versions).

For more, refer to the [developer docs for Cloudflare Pages builds](https://developers.cloudflare.com/pages/configuration/build-image)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/#page","headline":"Cloudflare Pages builds now provide Node.js v22 by default","description":"A new V3 build image for Cloudflare Pages includes Node.js v22 as the default version","url":"https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/og.png?v=dd5c0a769c9e0780","dateModified":"2025-05-30","datePublished":"2025-05-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
