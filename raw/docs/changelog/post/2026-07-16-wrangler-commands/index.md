---
description: Create Flagship apps, bind them to Workers, switch feature flags, and run rollouts with wrangler flagship.
title: Manage Flagship from the command line with Wrangler
image: https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/og.png?v=4165ebd0137d3ef2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 16, 2026

## Manage Flagship from the command line with Wrangler

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Wrangler](https://developers.cloudflare.com/workers/wrangler/)** now includes `wrangler flagship`, a command suite for managing [Flagship](https://developers.cloudflare.com/flagship/) apps and feature flags from your terminal.

Create an app and, if you use it from a Worker, add it to your `wrangler.json` or `wrangler.jsonc` file as a binding:

```bash
wrangler flagship apps create "My Worker App" \
  --binding FLAGS \
  --update-config
```

Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:

```bash
wrangler flagship flags create <APP_ID> new-checkout

wrangler flagship flags create <APP_ID> checkout-flow \
  --variation control=old-checkout \
  --variation treatment=new-checkout \
  --default control \
  --type string
```

After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:

```bash
wrangler flagship flags update <APP_ID> checkout-flow --default treatment
wrangler flagship flags disable <APP_ID> checkout-flow
wrangler flagship flags enable <APP_ID> checkout-flow
```

For release workflows, use `rollout`, `split`, and `rules` to change exposure without redeploying your Worker:

```bash
wrangler flagship flags rollout <APP_ID> new-checkout \
  --to on \
  --percentage 25 \
  --by user_id

wrangler flagship flags split <APP_ID> checkout-flow \
  --weight control=80 \
  --weight treatment=20 \
  --by user_id

wrangler flagship flags rules update <APP_ID> checkout-flow \
  --priority 1 \
  --when "country equals US"
```

These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.

Refer to the [`wrangler flagship` command reference](https://developers.cloudflare.com/flagship/reference/wrangler-commands/) for the full command guide.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/#page","headline":"Manage Flagship from the command line with Wrangler","description":"Create Flagship apps, bind them to Workers, switch feature flags, and run rollouts with wrangler flagship.","url":"https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/og.png?v=4165ebd0137d3ef2","dateModified":"2026-07-16","datePublished":"2026-07-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
