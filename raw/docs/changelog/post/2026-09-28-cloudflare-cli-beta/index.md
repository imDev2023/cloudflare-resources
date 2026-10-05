---
description: The Cloudflare CLI, cf, is now in beta. Use one command-line interface to manage resources across the Cloudflare API and to create, develop, and deploy Workers.
title: Cloudflare CLI is now in beta
image: https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/og.png?v=4ec58a21377d20d5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 28, 2026

## Cloudflare CLI is now in beta

[Workers](https://developers.cloudflare.com/workers/) [Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun

```
npm install --global cf
```

```
yarn global add cf
```

```
pnpm add --global cf
```

```
bun add --global cf
```

```sh
cf auth login
```

With `cf`, you can:

- **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
- **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
- **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
- **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.

`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/#page","headline":"Cloudflare CLI is now in beta","description":"The Cloudflare CLI, cf, is now in beta. Use one command-line interface to manage resources across the Cloudflare API and to create, develop, and deploy Workers.","url":"https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/og.png?v=4ec58a21377d20d5","dateModified":"2026-09-28","datePublished":"2026-09-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
