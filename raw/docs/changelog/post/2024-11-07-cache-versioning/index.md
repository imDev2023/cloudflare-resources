---
description: Cache now supports versioned environments for staging configurations and purging staged content independently.
title: Stage and test cache configurations safely
image: https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/og.png?v=1d649275de2fa267
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 7, 2024

## Stage and test cache configurations safely

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.

#### How it works

With versioned environments, you can:

1. **Create staging versions** of your cache configuration.
2. **Test cache rules** in a non-production environment.
3. **Purge staged content** independently from production.
4. **Validate changes** before promoting to production.

This capability integrates with Cloudflare's broader [versioning system](https://developers.cloudflare.com/version-management/), allowing you to manage cache configurations alongside other zone settings.

#### Benefits

- **Risk-free testing**: Validate configuration changes without impacting production.
- **Independent purging**: Clear staging cache without affecting live content.
- **Deployment confidence**: Catch issues before they reach end users.
- **Team collaboration**: Multiple team members can work on different versions.

#### Get started

To get started, refer to the [version management documentation](https://developers.cloudflare.com/version-management/).

Important limitation

Cache Reserve is only supported for your production environment. Staged environments can use standard cache functionality, but Cache Reserve persistence is limited to production deployments.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/#page","headline":"Stage and test cache configurations safely","description":"Cache now supports versioned environments for staging configurations and purging staged content independently.","url":"https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/og.png?v=1d649275de2fa267","dateModified":"2024-11-07","datePublished":"2024-11-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
