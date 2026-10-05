---
description: Browse, edit, and programmatically access local resource data during development with a new browser UI and OpenAPI-powered REST API.
title: Local Explorer for local resource data
image: https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/og.png?v=a6281bab73d0ee8b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 13, 2026

## Local Explorer for local resource data

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through `.wrangler/state` to understand what data your Worker has stored locally.

Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press `e` in your terminal, or navigate to `/cdn-cgi/local/explorer` on your local dev server.

#### Supported resources

Local Explorer supports five resource types and works across multiple workers running locally:

- **[KV](https://developers.cloudflare.com/kv/)** — Browse keys, view values and metadata, create, update, and delete key-value pairs.
- **[R2](https://developers.cloudflare.com/r2/)** — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.
- **[D1](https://developers.cloudflare.com/d1/)** — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.
- **[Durable Objects](https://developers.cloudflare.com/durable-objects/)** (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.
- **[Workflows](https://developers.cloudflare.com/workflows/)** — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.

#### OpenAPI-powered REST API

Local Explorer exposes a REST API at `/cdn-cgi/local/explorer/api` that provides programmatic access to the same operations available in the browser. The root endpoint returns an [OpenAPI specification ↗︎](https://www.openapis.org/) describing all available endpoints, parameters, and response formats.

```sh
curl http://localhost:8787/cdn-cgi/local/explorer/api
```

Point an AI coding agent at `/cdn-cgi/local/explorer/api` and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.

For more details, refer to the [Local Explorer documentation](https://developers.cloudflare.com/workers/local-development/local-explorer/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/#page","headline":"Local Explorer for local resource data","description":"Browse, edit, and programmatically access local resource data during development with a new browser UI and OpenAPI-powered REST API.","url":"https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/og.png?v=a6281bab73d0ee8b","dateModified":"2026-04-13","datePublished":"2026-04-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
