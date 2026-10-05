---
description: The Workers Vitest integration package has been renamed for version 1.
title: "@cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin"
image: https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/og.png?v=a0cfef2664a63cca
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 19, 2026

## @cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Version 1 of the Workers Vitest integration is published as [`@cloudflare/vitest-plugin` ↗︎](https://www.npmjs.com/package/@cloudflare/vitest-plugin). The package was formerly named `@cloudflare/vitest-pool-workers`.

The Vitest configuration API is unchanged. Existing projects must update the dependency name, package imports, and TypeScript `types` entries.

To migrate automatically, run:

npmyarnpnpm

```
npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
```

```
yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
```

```
pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin
```

The codemod updates your dependency, imports, and test TypeScript configuration. For manual migration steps, refer to [Migrate to Vitest plugin](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/).

For outbound request mocks in Workers tests, use the [`@msw/cloudflare` ↗︎](https://github.com/mswjs/cloudflare) integration. Refer to [Mock outbound requests](https://developers.cloudflare.com/workers/testing/vitest-integration/mock-outbound-requests/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/#page","headline":"@cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin","description":"The Workers Vitest integration package has been renamed for version 1.","url":"https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/og.png?v=a0cfef2664a63cca","dateModified":"2026-08-19","datePublished":"2026-08-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
