---
description: Manage Artifacts namespaces, repos, and repo-scoped tokens from the command line using Wrangler.
title: Manage Artifacts namespaces and repos with Wrangler CLI
image: https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/og.png?v=3905514210df26d0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 18, 2026

## Manage Artifacts namespaces and repos with Wrangler CLI

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.

Available commands:

- `wrangler artifacts namespaces list` — List Artifacts namespaces in your account.
- `wrangler artifacts namespaces get` — Get metadata for a namespace.
- `wrangler artifacts repos create` — Create a repo in a namespace.
- `wrangler artifacts repos list` — List repos in a namespace.
- `wrangler artifacts repos get` — Get metadata for a repo.
- `wrangler artifacts repos delete` — Delete a repo.
- `wrangler artifacts repos issue-token` — Issue a repo-scoped token for Git access.

To get started, refer to the [Wrangler Artifacts commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/#page","headline":"Manage Artifacts namespaces and repos with Wrangler CLI","description":"Manage Artifacts namespaces, repos, and repo-scoped tokens from the command line using Wrangler.","url":"https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/og.png?v=3905514210df26d0","dateModified":"2026-05-18","datePublished":"2026-05-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
