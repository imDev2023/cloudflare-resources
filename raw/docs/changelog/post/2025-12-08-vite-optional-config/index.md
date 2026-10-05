---
description: When using the Cloudflare Vite plugin in an assets-only (static) site, a Wrangler configuration file is now optional.
title: Wrangler config is optional when using Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/og.png?v=e6d62a253329e015
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 8, 2025

## Wrangler config is optional when using Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When using the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) to build and deploy Workers, a Wrangler configuration file is now optional for assets-only (static) sites. If no `wrangler.toml`, `wrangler.json`, or `wrangler.jsonc` file is found, the plugin generates sensible defaults for an assets-only site. The `name` is based on the `package.json` or the project directory name, and the `compatibility_date` uses the latest date supported by your installed Miniflare version.

This allows easier setup for static sites using Vite. Note that SPAs will still need to [set `assets.not_found_handling` to `single-page-application` ↗︎](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/) in order to function correctly.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/#page","headline":"Wrangler config is optional when using Vite plugin","description":"When using the Cloudflare Vite plugin in an assets-only (static) site, a Wrangler configuration file is now optional.","url":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/og.png?v=e6d62a253329e015","dateModified":"2025-12-08","datePublished":"2025-12-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
