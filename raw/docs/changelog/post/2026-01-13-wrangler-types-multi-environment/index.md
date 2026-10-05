---
description: The `wrangler types` command now aggregates bindings from all environments by default, ensuring complete type coverage across your deployment environments.
title: "`wrangler types` now generates types for all environments"
image: https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/og.png?v=2dd9574854ac21b1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 13, 2026

## \`wrangler types\` now generates types for all environments

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `wrangler types` command now generates TypeScript types for bindings from **all environments** defined in your Wrangler configuration file by default.

Previously, `wrangler types` only generated types for bindings in the top-level configuration (or a single environment when using the `--env` flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.

Now, running `wrangler types` collects bindings from all environments and includes them in the generated `Env` type. This ensures your types are complete regardless of which environment you deploy to.

#### Generating types for a specific environment

If you want the previous behavior of generating types for only a specific environment, you can use the `--env` flag:

```sh
wrangler types --env production
```

Learn more about [generating types for your Worker](https://developers.cloudflare.com/workers/wrangler/commands/general/#types) in the Wrangler documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/#page","headline":"`wrangler types` now generates types for all environments","description":"The wrangler types command now aggregates bindings from all environments by default, ensuring complete type coverage across your deployment environments.","url":"https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/og.png?v=2dd9574854ac21b1","dateModified":"2026-01-13","datePublished":"2026-01-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
