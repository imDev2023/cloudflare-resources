---
description: AI agents can inspect local traces and logs to find, fix, and verify Worker failures.
title: AI agents can debug Workers with local tracing
image: https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/og.png?v=8064c1783eeb4946
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## AI agents can debug Workers with local tracing

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`wrangler dev` and `vite dev` automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.

#### Debug with AI agents

When the tooling detects an AI agent session, it prints a terminal hint pointing to the [Local Explorer API](https://developers.cloudflare.com/workers/local-development/local-explorer/#api) at `/cdn-cgi/local/explorer/api`. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.

The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.

#### Inspect traces in Local Explorer

Humans can inspect the same [traces](https://developers.cloudflare.com/workers/observability/traces/) and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.

![Local Explorer showing a failed Worker trace with spans, timing, and errors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=847,format=webp/_astro/local-trace-failed-request.Bf0avznU.png)

Automatic spans cover handler calls, outbound `fetch()` calls, and binding calls. Custom spans appear alongside these automatic spans.

For more details, refer to the [Local Explorer documentation](https://developers.cloudflare.com/workers/local-development/local-explorer/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/#page","headline":"AI agents can debug Workers with local tracing","description":"AI agents can inspect local traces and logs to find, fix, and verify Worker failures.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/og.png?v=8064c1783eeb4946","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
