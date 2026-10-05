---
description: Wrangler v4 is available!
title: Use the latest JavaScript features with Wrangler CLI v4
image: https://developers.cloudflare.com/changelog/post/2025-03-13-wrangler-v4/og.png?v=34aa810f878a088d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 13, 2025

## Use the latest JavaScript features with Wrangler CLI v4

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-13-wrangler-v4/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released the next major version of [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for Cloudflare Workers — `wrangler@4.0.0`. Wrangler v4 is a major release focused on updates to underlying systems and dependencies, along with improvements to keep Wrangler commands consistent and clear.

You can run the following command to install it in your projects:

npmyarnpnpmbun

```
npm i wrangler@latest
```

```
yarn add wrangler@latest
```

```
pnpm add wrangler@latest
```

```
bun add wrangler@latest
```

Unlike previous major versions of Wrangler, which were [foundational rewrites ↗︎](https://blog.cloudflare.com/wrangler-v2-beta/) and [rearchitectures ↗︎](https://blog.cloudflare.com/wrangler3/) — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change.

A [detailed migration guide](https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4) is available and if you find a bug or hit a roadblock when upgrading to Wrangler v4, [open an issue on the `cloudflare/workers-sdk` repository on GitHub ↗︎](https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml).

Going forward, we'll continue supporting Wrangler v3 with bug fixes and security updates until Q1 2026, and with critical security updates until Q1 2027, at which point it will be out of support.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-13-wrangler-v4/#page","headline":"Use the latest JavaScript features with Wrangler CLI v4","description":"Wrangler v4 is available!","url":"https://developers.cloudflare.com/changelog/post/2025-03-13-wrangler-v4/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-13-wrangler-v4/og.png?v=34aa810f878a088d","dateModified":"2025-03-13","datePublished":"2025-03-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
