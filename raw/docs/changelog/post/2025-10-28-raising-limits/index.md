---
description: Higher concurrency and creation limits for Workflow instances now available
title: Increased Workflows instance and concurrency limits
image: https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/og.png?v=eb51a88046a4424c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 31, 2025

## Increased Workflows instance and concurrency limits

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've raised the [Cloudflare Workflows](https://developers.cloudflare.com/workflows/) account-level limits for all accounts on the [Workers paid plan](https://developers.cloudflare.com/workers/platform/pricing/):

- **Instance creation rate** increased from 100 workflow instances per 10 seconds to 100 instances per second
- **Concurrency limit** increased from 4,500 to 10,000 workflow instances per account

These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to [the getting started guide](https://developers.cloudflare.com/workflows/get-started/guide/).

If your application requires a higher limit, fill out the [Limit Increase Request Form](https://developers.cloudflare.com/workers/platform/limits/) or contact your account team. Please refer to [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/#page","headline":"Increased Workflows instance and concurrency limits","description":"Higher concurrency and creation limits for Workflow instances now available","url":"https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/og.png?v=eb51a88046a4424c","dateModified":"2025-10-31","datePublished":"2025-10-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
