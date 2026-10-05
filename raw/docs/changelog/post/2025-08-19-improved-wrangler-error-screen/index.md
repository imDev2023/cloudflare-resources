---
description: Wrangler's error screen now features light and dark themes, more reliable source map resolution, and better error cause display.
title: Easier debugging in Workers with improved Wrangler error screen
image: https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/og.png?v=d07fa55cf7914ba5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 19, 2025

## Easier debugging in Workers with improved Wrangler error screen

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler's error screen has received several improvements to enhance your debugging experience!

The error screen now features a refreshed design thanks to [youch ↗︎](https://www.npmjs.com/package/youch), with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.

| Before | After (Light) | After (Dark) |
| --- | --- | --- |
| ![Old error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/old-error-screen.yurLWiKb.png) | ![New light theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-light.CcroERTP.png) | ![New dark theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-dark.BIDA2RGg.png) |

Try it out now with `npx wrangler@latest dev` in your Workers project.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/#page","headline":"Easier debugging in Workers with improved Wrangler error screen","description":"Wrangler's error screen now features light and dark themes, more reliable source map resolution, and better error cause display.","url":"https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/og.png?v=d07fa55cf7914ba5","dateModified":"2025-08-19","datePublished":"2025-08-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
