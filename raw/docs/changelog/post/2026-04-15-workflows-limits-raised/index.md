---
description: Concurrency limit for Workflows instances is now 50,000. Instance creation rate limit has been raised to 300 instances per second per account, maintaining a limit of 100 instances per second per workflow.
title: Increased concurrency, creation rate, and queued instance limits for Workflows instances
image: https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/og.png?v=4a4d3093dd4f76e2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2026

## Increased concurrency, creation rate, and queued instance limits for Workflows instances

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) limits have been raised to the following:

| Limit | Previous | New |
| --- | --- | --- |
| Concurrent instances (running in parallel) | 10,000 | 50,000 |
| Instance creation rate (per account) | 100/second per account | 300/second per account, 100/second per workflow |
| Queued instances per Workflow <sup>[1](#user-content-fn-1)</sup> | 1 million | 2 million |

These increases apply to all users on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/). Refer to the [Workflows limits documentation](https://developers.cloudflare.com/workflows/reference/limits/) for more details.

#### Footnotes

1. Queued instances are instances that have been created or awoken and are waiting for a concurrency slot. [↩](#user-content-fnref-1)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/#page","headline":"Increased concurrency, creation rate, and queued instance limits for Workflows instances","description":"Concurrency limit for Workflows instances is now 50,000. Instance creation rate limit has been raised to 300 instances per second per account, maintaining a limit of 100 instances per second per workflow.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/og.png?v=4a4d3093dd4f76e2","dateModified":"2026-04-15","datePublished":"2026-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
