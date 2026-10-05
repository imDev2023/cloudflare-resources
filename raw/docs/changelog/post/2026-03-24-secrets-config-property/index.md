---
description: The new `secrets` configuration property lets you declare which secrets your Worker requires.
title: Declare required secrets in your Wrangler configuration
image: https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/og.png?v=42571acf1e07297f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 25, 2026

## Declare required secrets in your Wrangler configuration

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The new `secrets` configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.

```jsonc
{
	"secrets": {
		"required": ["API_KEY", "DB_PASSWORD"],
	},
}
```

```toml
[secrets]
required = [ "API_KEY", "DB_PASSWORD" ]
```

#### Local development

When `secrets` is defined, `wrangler dev` and `vite dev` load only the keys listed in `secrets.required` from `.dev.vars` or `.env`/`process.env`. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.

#### Type generation

`wrangler types` generates typed bindings from `secrets.required` instead of inferring names from `.dev.vars` or `.env`. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated `Env` type marks secrets that only appear in some environments as optional.

#### Deploy

`wrangler deploy` and `wrangler versions upload` validate that all secrets in `secrets.required` are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.

For more information, refer to the [`secrets` configuration property](https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property) reference.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/#page","headline":"Declare required secrets in your Wrangler configuration","description":"The new secrets configuration property lets you declare which secrets your Worker requires.","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/og.png?v=42571acf1e07297f","dateModified":"2026-03-25","datePublished":"2026-03-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
