---
description: TanStack Start apps can now prerender routes to static HTML at build time using the Cloudflare Vite plugin.
title: Static prerendering support for TanStack Start
image: https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/og.png?v=8eaa5922d639c33e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 19, 2025

## Static prerendering support for TanStack Start

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[TanStack Start ↗︎](https://tanstack.com/start/) apps can now prerender routes to static HTML at build time with access to build time environment variables and bindings, and serve them as [static assets](https://developers.cloudflare.com/workers/static-assets/). To enable prerendering, configure the `prerender` option of the TanStack Start plugin in your Vite config:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";

export default defineConfig({
  plugins: [
    cloudflare({ viteEnvironment: { name: "ssr" } }),
    tanstackStart({
      prerender: {
        enabled: true,
      },
    }),
  ],
});
```

This feature requires `@tanstack/react-start` v1.138.0 or later. See the [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/#static-prerendering) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/#page","headline":"Static prerendering support for TanStack Start","description":"TanStack Start apps can now prerender routes to static HTML at build time using the Cloudflare Vite plugin.","url":"https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-19-tanstack-start-prerendering/og.png?v=8eaa5922d639c33e","dateModified":"2025-12-19","datePublished":"2025-12-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
