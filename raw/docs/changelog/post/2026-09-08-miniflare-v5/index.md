---
description: Miniflare v5 updates internal local development APIs without requiring changes for Wrangler or Vite plugin users.
title: Miniflare v5 prepares local development for the cf CLI
image: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/og.png?v=8e283b958fd06a7e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 8, 2026

## Miniflare v5 prepares local development for the cf CLI

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Miniflare v5 prepares Cloudflare local development tooling for the upcoming `cf` CLI.

Miniflare powers local Workers development behind `wrangler dev`, the Cloudflare Vite plugin, and `@cloudflare/vitest-plugin`. Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.

The most significant change is a new configuration shape which aligns Miniflare with `cloudflare.config.ts`, the programmatic Cloudflare configuration format now available for testing.

Other breaking changes include:

- Removed deprecated APIs and options, such as legacy alpha D1 bindings.
- Removed now-unused, internal APIs like `wrappedBindings`
- Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.
- Moved local-only /cdn-cgi routes under /cdn-cgi/local.
- Replaced per-resource persistence options with shared persistence root options.

For a more comprehensive list, refer to [Miniflare's changelog ↗︎](https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha)

This work sets up a cleaner foundation for the next generation of local development tooling, including the new `cf` CLI.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/#page","headline":"Miniflare v5 prepares local development for the cf CLI","description":"Miniflare v5 updates internal local development APIs without requiring changes for Wrangler or Vite plugin users.","url":"https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/og.png?v=8e283b958fd06a7e","dateModified":"2026-09-08","datePublished":"2026-09-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
