---
description: Cloudflare Vite Plugin 1.0 is out now — with official support for Vite 6, React Router v7, and the full Developer Platform. Now you can run Vite’s dev server locally, while executing your code directly in the Workers runtime!
title: The Cloudflare Vite plugin is now Generally Available
image: https://developers.cloudflare.com/changelog/post/2025-04-08-vite-plugin/og.png?v=bbd730a77407d328
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2025

## The Cloudflare Vite plugin is now Generally Available

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-08-vite-plugin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) has [reached v1.0 ↗︎](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin) and is now Generally Available ("GA").

When you use `@cloudflare/vite-plugin`, you can use Vite's local development server and build tooling, while ensuring that while developing, your code runs in [`workerd` ↗︎](https://github.com/cloudflare/workerd), the open-source Workers runtime.

This lets you get the best of both worlds for a full-stack app — you can use [Hot Module Replacement ↗︎](https://vite.dev/guide/features.html#hot-module-replacement) from Vite right alongside [Durable Objects](https://developers.cloudflare.com/durable-objects/) and other runtime APIs and bindings that are unique to Cloudflare Workers.

`@cloudflare/vite-plugin` is made possible by the new [environment API ↗︎](https://vite.dev/guide/api-environment) in Vite, and was built [in partnership with the Vite team ↗︎](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin).

#### Framework support

You can build any type of application with `@cloudflare/vite-plugin`, using any rendering mode, from single page applications (SPA) and static sites to server-side rendered (SSR) pages and API routes.

[React Router v7 (Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/) is the first full-stack framework to provide full support for Cloudflare Vite plugin, allowing you to use all parts of Cloudflare's developer platform, without additional build steps.

You can also build complete full-stack apps on Workers **without a framework** — ["just use Vite" ↗︎](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin) and React together, and build a back-end API in the same Worker. Follow our [React SPA with an API tutorial](https://developers.cloudflare.com/workers/vite-plugin/tutorial/) to learn how.

#### Configuration

If you're already using [Vite ↗︎](https://vite.dev/) in your build and development toolchain, you can start using our plugin with minimal changes to your `vite.config.ts`:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [cloudflare()],
});
```

Take a look at the [documentation for our Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) for more information!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-08-vite-plugin/#page","headline":"The Cloudflare Vite plugin is now Generally Available","description":"Cloudflare Vite Plugin 1.0 is out now — with official support for Vite 6, React Router v7, and the full Developer Platform. Now you can run Vite’s dev server locally, while executing your code directly in the Workers runtime!","url":"https://developers.cloudflare.com/changelog/post/2025-04-08-vite-plugin/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-08-vite-plugin/og.png?v=bbd730a77407d328","dateModified":"2025-04-08","datePublished":"2025-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
