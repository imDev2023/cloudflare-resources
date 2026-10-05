---
description: Additional permissions required for ZT datasets
title: Logpush Permission Update for Zero Trust Datasets
image: https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/og.png?v=247d23e3310ebb60
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 5, 2025

## Logpush Permission Update for Zero Trust Datasets

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Permissions](https://developers.cloudflare.com/logs/logpush/permissions/) for managing Logpush jobs related to [Zero Trust datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.

To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:

- Logs Edit
- Zero Trust: PII Read

Note

Update your UI, API or Terraform configurations to include the new permissions. Requests to Zero Trust datasets will fail due to insufficient access without the additional permission.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/#page","headline":"Logpush Permission Update for Zero Trust Datasets","description":"Additional permissions required for ZT datasets","url":"https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/og.png?v=247d23e3310ebb60","dateModified":"2025-11-05","datePublished":"2025-11-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
