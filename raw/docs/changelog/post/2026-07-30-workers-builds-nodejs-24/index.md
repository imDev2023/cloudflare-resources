---
description: Workers Builds now uses Node.js 24.18.0 by default while retaining support for explicit Node.js version overrides.
title: Node.js 24 is now the default for Workers Builds
image: https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/og.png?v=8df0d9306f18b27e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 30, 2026

## Node.js 24 is now the default for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Builds now uses Node.js 24.18.0 by default. The build image preinstalls Node.js 22.23.2 and 24.18.0.

You can continue to override the default with the `NODE_VERSION` environment variable, an `.nvmrc` file, or a `.node-version` file. For more information, refer to [Override default versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#overriding-default-versions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/#page","headline":"Node.js 24 is now the default for Workers Builds","description":"Workers Builds now uses Node.js 24.18.0 by default while retaining support for explicit Node.js version overrides.","url":"https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/og.png?v=8df0d9306f18b27e","dateModified":"2026-07-30","datePublished":"2026-07-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
