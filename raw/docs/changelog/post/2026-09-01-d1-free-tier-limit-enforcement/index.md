---
description: Beginning September 1, 2026, D1 queries on Workers Free accounts that exceed daily row read or row write limits will fail and return errors.
title: D1 enforces free tier daily query limits
image: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/og.png?v=a4553263d2ae132a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 1, 2026

## D1 enforces free tier daily query limits

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Beginning September 1, 2026, D1 queries on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) will fail when an account exceeds the daily [row read or row write limits](https://developers.cloudflare.com/d1/platform/pricing/). Queries via the [Workers Binding API](https://developers.cloudflare.com/d1/worker-api/) and the [REST API](https://developers.cloudflare.com/d1/rest-api/) will return errors until the limit resets at midnight UTC. Stored data is not affected.

You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:

| Error | Description |
| --- | --- |
| Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row read limit. |
| Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row write limit. |

Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add [indexes](https://developers.cloudflare.com/d1/best-practices/use-indexes/) to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers).

For more information on D1 errors and how to handle them, refer to the [D1 error list](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/#page","headline":"D1 enforces free tier daily query limits","description":"Beginning September 1, 2026, D1 queries on Workers Free accounts that exceed daily row read or row write limits will fail and return errors.","url":"https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/og.png?v=a4553263d2ae132a","dateModified":"2026-09-01","datePublished":"2026-09-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
