---
description: Use wrangler workflows commands with the --local flag to manage Workflows running in a local wrangler dev session.
title: All Wrangler commands for Workflows now support local development
image: https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/og.png?v=44008e334ee1ced6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 1, 2026

## All Wrangler commands for Workflows now support local development

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

All `wrangler workflows` commands now accept a `--local` flag to target a Workflow running in a local `wrangler dev` session instead of the production API.

You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:

```sh
npx wrangler workflows list --local
npx wrangler workflows trigger my-workflow --local
npx wrangler workflows instances list my-workflow --local
npx wrangler workflows instances pause my-workflow <INSTANCE_ID> --local
npx wrangler workflows instances send-event my-workflow <INSTANCE_ID> --type my-event --local
```

All commands also accept `--port` to target a specific `wrangler dev` session (defaults to `8787`).

For more information, refer to [Workflows local development](https://developers.cloudflare.com/workflows/build/local-development/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/#page","headline":"All Wrangler commands for Workflows now support local development","description":"Use wrangler workflows commands with the --local flag to manage Workflows running in a local wrangler dev session.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/og.png?v=44008e334ee1ced6","dateModified":"2026-04-01","datePublished":"2026-04-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
