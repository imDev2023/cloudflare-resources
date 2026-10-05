---
description: Ships only the latest runtime types and drops the dated entrypoints.
title: Simpler runtime types with @cloudflare/workers-types v5
image: https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/og.png?v=597acd791067cdc3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 3, 2026

## Simpler runtime types with @cloudflare/workers-types v5

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have released version 5 of [`@cloudflare/workers-types` ↗︎](https://www.npmjs.com/package/@cloudflare/workers-types). This release simplifies the package to expose only the latest runtime types.

We still recommend that you generate types for your Worker using [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/general/#types), but if you want to use the package directly, you can install it with your package manager of choice:

npmyarnpnpmbun

```
npm i -D @cloudflare/workers-types@latest
```

```
yarn add -D @cloudflare/workers-types@latest
```

```
pnpm add -D @cloudflare/workers-types@latest
```

```
bun add -d @cloudflare/workers-types@latest
```

The package now exposes two entrypoints:

- `@cloudflare/workers-types` reflects the latest compatibility date, using the latest stable compatibility flags.
- `@cloudflare/workers-types/experimental` reflects APIs behind experimental compatibility flags.

The dated entrypoints, such as `@cloudflare/workers-types/2022-11-30` and `@cloudflare/workers-types/2023-03-01`, are removed. With runtime type generation in [Wrangler v4](https://developers.cloudflare.com/workers/wrangler/), you can generate these with the `wrangler types` command to create types locked to your Worker's compatibility date.

For more information, refer to [TypeScript language support](https://developers.cloudflare.com/workers/languages/typescript/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/#page","headline":"Simpler runtime types with @cloudflare/workers-types v5","description":"Ships only the latest runtime types and drops the dated entrypoints.","url":"https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/og.png?v=597acd791067cdc3","dateModified":"2026-07-03","datePublished":"2026-07-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
