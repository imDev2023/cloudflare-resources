---
description: With Node.js compatibility on, process.env is automatically populated with environment variables and secrets
title: Access your Worker's environment variables from process.env
image: https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/og.png?v=9a670896958412a6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 11, 2025

## Access your Worker's environment variables from process.env

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now access [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) and [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) on [`process.env`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/process/#processenv) when using the [`nodejs_compat` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

```js
const apiClient = ApiClient.new({ apiKey: process.env.API_KEY });
const LOG_LEVEL = process.env.LOG_LEVEL || "info";
```

In Node.js, environment variables are exposed via the global `process.env` object. Some libraries assume that this object will be populated, and many developers may be used to accessing variables in this way.

Previously, the `process.env` object was always empty unless written to in Worker code. This could cause unexpected errors or friction when developing Workers using code previously written for Node.js.

Now, [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), and [version metadata](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/) can all be accessed on `process.env`.

To opt-in to the new `process.env` behaviour now, add the [`nodejs_compat_populate_process_env`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-auto-populating-processenv) compatibility flag to your `wrangler.json` configuration:

```jsonc
{
	// Rest of your configuration
	// Add "nodejs_compat_populate_process_env" to your compatibility_flags array
	"compatibility_flags": ["nodejs_compat", "nodejs_compat_populate_process_env"],
	// Rest of your configuration
```

```toml
compatibility_flags = [ "nodejs_compat", "nodejs_compat_populate_process_env" ]
```

After April 1, 2025, populating `process.env` will become the default behavior when both `nodejs_compat` is enabled and your Worker's `compatibility_date` is after "2025-04-01".

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/#page","headline":"Access your Worker's environment variables from process.env","description":"With Node.js compatibility on, process.env is automatically populated with environment variables and secrets","url":"https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/og.png?v=9a670896958412a6","dateModified":"2025-03-11","datePublished":"2025-03-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
