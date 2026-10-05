---
description: Workers with a compatibility date of 2026-08-04 or later enable Node.js compatibility by default.
title: Node.js compatibility is now enabled by default
image: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/og.png?v=2ae03e3f8b21f232
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## Node.js compatibility is now enabled by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers now enable the `nodejs_compat` and `nodejs_compat_v2` compatibility flags by default for [compatibility dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of `2026-08-04` or later. These flags are not used for these compatibility dates because the compatibility date enables the same behavior.

This means all [Node.js built-in APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) supported by the Workers runtime are available by default, including `node:crypto`, `node:buffer`, `node:stream`, `node:net`, `node:dns`, `node:fs`, `node:http`, and more. npm packages that depend on these APIs will work without additional configuration.

Workers using an earlier compatibility date are not affected. They can still opt in by adding `nodejs_compat` to `compatibility_flags`.

New projects do not need to add either flag. Existing projects can update their compatibility date without removing them. Wrangler, Miniflare, the Cloudflare Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting the runtime.

To turn off Node.js compatibility completely, remove any `nodejs_compat` and `nodejs_compat_v2` flags. Then add both of the following flags:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  // Set this to today's date
  "compatibility_date": "2026-10-05",
  "compatibility_flags": [
    "no_nodejs_compat",
    "no_nodejs_compat_v2"
  ]
}
```

```toml
# Set this to today's date
compatibility_date = "2026-10-05"
compatibility_flags = ["no_nodejs_compat", "no_nodejs_compat_v2"]
```

For more information, refer to the [Node.js compatibility documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/#page","headline":"Node.js compatibility is now enabled by default","description":"Workers with a compatibility date of 2026-08-04 or later enable Node.js compatibility by default.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/og.png?v=2ae03e3f8b21f232","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
