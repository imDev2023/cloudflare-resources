---
description: SQLite storage billing in January 2026
title: Billing for SQLite Storage
image: https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/og.png?v=6b2e32bb3be7dbfd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 12, 2025

## Billing for SQLite Storage

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).

To view your SQLite storage usage, go to the **Durable Objects** page

[Go to **Durable Objects** ↗](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.

Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to [SQLite storage pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend) announced in September 2024 with the [public beta ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/). Developers on the Workers Free plan will not be charged.

Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur [charges for requests and duration](https://developers.cloudflare.com/durable-objects/platform/pricing/#compute-billing), and no changes are being made to compute billing.

For more information about SQLite storage pricing and limits, refer to the [Durable Objects pricing documentation](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/#page","headline":"Billing for SQLite Storage","description":"SQLite storage billing in January 2026","url":"https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/og.png?v=6b2e32bb3be7dbfd","dateModified":"2025-12-12","datePublished":"2025-12-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
