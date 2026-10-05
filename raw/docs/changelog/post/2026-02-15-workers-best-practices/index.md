---
description: Best practices for building production Workers, covering configuration, architecture, observability, security, and code patterns.
title: New Best Practices guide for Workers
image: https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/og.png?v=01956831f6e2096a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 15, 2026

## New Best Practices guide for Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [Workers Best Practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.

Key guidance includes:

- **Keep your compatibility date current and enable `nodejs_compat`** — Ensure you have access to the latest runtime features and Node.js built-in modules.

```jsonc
{
	"name": "my-worker",
	"main": "src/index.ts",
	// Set this to today's date
	"compatibility_date": "2026-10-05",
	"compatibility_flags": ["nodejs_compat"],
}
```

```toml
name = "my-worker"
main = "src/index.ts"
# Set this to today's date
compatibility_date = "2026-10-05"
compatibility_flags = [ "nodejs_compat" ]
```

- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.

To learn more, refer to [Workers Best Practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/#page","headline":"New Best Practices guide for Workers","description":"Best practices for building production Workers, covering configuration, architecture, observability, security, and code patterns.","url":"https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/og.png?v=01956831f6e2096a","dateModified":"2026-02-15","datePublished":"2026-02-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
