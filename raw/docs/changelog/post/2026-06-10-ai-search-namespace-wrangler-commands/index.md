---
description: Use new namespace-level Wrangler commands to create, list, update, and delete AI Search namespaces from the CLI.
title: Manage AI Search namespaces with Wrangler CLI
image: https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/og.png?v=1d2eeef19060e151
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2026

## Manage AI Search namespaces with Wrangler CLI

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports namespace-level Wrangler commands, making it easier to manage [namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/) from your terminal, scripts, and agent workflows.

The following commands are available:

| Command | Description |
| --- | --- |
| `wrangler ai-search namespace list` | List AI Search namespaces |
| `wrangler ai-search namespace create` | Create a new AI Search namespace |
| `wrangler ai-search namespace get` | Get details for a namespace |
| `wrangler ai-search namespace update` | Update a namespace description |
| `wrangler ai-search namespace delete` | Delete an AI Search namespace |

Create a namespace for a new application or tenant directly from the CLI:

```sh
wrangler ai-search namespace create docs-production --description "Production documentation search"
```

List namespaces with pagination or filter by name or description:

```sh
wrangler ai-search namespace list --search docs --page 1 --per-page 10
```

Use `--json` with `list`, `create`, `get`, and `update` to return structured output that automation and AI agents can parse directly.

Instance-level commands also now support a `--namespace` flag, so you can interact with instances inside a specific namespace from the CLI:

```sh
wrangler ai-search list --namespace docs-production
```

For full usage details, refer to the [AI Search Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/#page","headline":"Manage AI Search namespaces with Wrangler CLI","description":"Use new namespace-level Wrangler commands to create, list, update, and delete AI Search namespaces from the CLI.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/og.png?v=1d2eeef19060e151","dateModified":"2026-06-10","datePublished":"2026-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
