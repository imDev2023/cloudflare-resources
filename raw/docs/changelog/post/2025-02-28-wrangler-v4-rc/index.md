---
description: You can now try out the v4 RC for Wrangler by installing `wrangler@4.0.0-rc.0`
title: Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0
image: https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/og.png?v=48bee72fef400879
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 28, 2025

## Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released a release candidate of the next major version of [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for Cloudflare Workers — `wrangler@4.0.0-rc.0`.

You can run the following command to install it and be one of the first to try it out:

npmyarnpnpmbun

```
npm i wrangler@v4-rc
```

```
yarn add wrangler@v4-rc
```

```
pnpm add wrangler@v4-rc
```

```
bun add wrangler@v4-rc
```

Unlike previous major versions of Wrangler, which were [foundational rewrites ↗︎](https://blog.cloudflare.com/wrangler-v2-beta/) and [rearchitectures ↗︎](https://blog.cloudflare.com/wrangler3/) — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change. Before we release Wrangler v4 and advance past the release candidate stage, we'll share a detailed migration guide in the Workers developer docs. But for the vast majority of cases, you won't need to do anything to migrate — things will just work as they do today. We are sharing this release candidate in advance of the official release of v4, so that you can try it out early and share feedback.

#### New JavaScript language features that you can now use with Wrangler v4

Version 4 of Wrangler updates the version of [esbuild ↗︎](https://esbuild.github.io/) that Wrangler uses internally, allowing you to use modern JavaScript language features, including:

##### The `using` keyword from Explicit Resource Management

The [`using` keyword from the Explicit Resource Management standard](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/#explicit-resource-management) makes it easier to work with the [JavaScript-native RPC system built into Workers](https://developers.cloudflare.com/workers/runtime-apis/rpc/). This means that when you obtain a stub, you can ensure that it is automatically disposed when you exit scope it was created in:

```js
function sendEmail(id, message) {
  using user = await env.USER_SERVICE.findUser(id);
  await user.sendEmail(message);

  // user[Symbol.dispose]() is implicitly called at the end of the scope.
}
```

##### Import attributes

[Import attributes ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with) allow you to denote the type or other attributes of the module that your code imports. For example, you can import a JSON module, using the following syntax:

```js
import data from "./data.json" with { type: "json" };
```

#### Other changes

##### `--local` is now the default for all CLI commands

All commands that access resources (for example, `wrangler kv`, `wrangler r2`, `wrangler d1`) now access local datastores by default, ensuring consistent behavior.

##### Clearer policy for the minimum required version of Node.js required to run Wrangler

Moving forward, the [active, maintenance, and current versions of Node.js ↗︎](https://nodejs.org/en/about/previous-releases) will be officially supported by Wrangler. This means the minimum officially supported version of Node.js you must have installed for Wrangler v4 will be Node.js v18 or later. This policy mirrors how many other packages and CLIs support older versions of Node.js, and ensures that as long as you are using a version of Node.js that the Node.js project itself supports, this will be supported by Wrangler as well.

##### Features previously deprecated in Wrangler v3 are now removed in Wrangler v4

All previously deprecated features in [Wrangler v2 ↗︎](https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v2) and in [Wrangler v3 ↗︎](https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v3) have now been removed. Additionally, the following features that were deprecated during the Wrangler v3 release have been removed:

- Legacy Assets (using `wrangler dev/deploy --legacy-assets` or the `legacy_assets` config file property). Instead, we recommend you [migrate to Workers assets ↗︎](https://developers.cloudflare.com/workers/static-assets/).
- Legacy Node.js compatibility (using `wrangler dev/deploy --node-compat` or the `node_compat` config file property). Instead, use the [`nodejs_compat` compatibility flag ↗︎](https://developers.cloudflare.com/workers/runtime-apis/nodejs). This includes the functionality from legacy `node_compat` polyfills and natively implemented Node.js APIs.
- `wrangler version`. Instead, use `wrangler --version` to check the current version of Wrangler.
- `getBindingsProxy()` (via `import { getBindingsProxy } from "wrangler"`). Instead, use the [`getPlatformProxy()` API ↗︎](https://developers.cloudflare.com/workers/wrangler/api/#getplatformproxy), which takes exactly the same arguments.
- `usage_model`. This no longer has any effect, after the [rollout of Workers Standard Pricing ↗︎](https://blog.cloudflare.com/workers-pricing-scale-to-zero/).

We'd love your feedback! If you find a bug or hit a roadblock when upgrading to Wrangler v4, [open an issue on the `cloudflare/workers-sdk` repository on GitHub ↗︎](https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/#page","headline":"Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0","description":"You can now try out the v4 RC for Wrangler by installing wrangler@4.0.0-rc.0","url":"https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/og.png?v=48bee72fef400879","dateModified":"2025-02-28","datePublished":"2025-02-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
