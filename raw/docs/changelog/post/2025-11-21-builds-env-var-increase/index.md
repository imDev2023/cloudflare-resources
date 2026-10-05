---
description: Workers Builds now supports up to 64 environment variables per Worker with 5 KB per variable, up from a previous 5 KB total limit.
title: Environment variable limits increase for Workers Builds
image: https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/og.png?v=3fc608ad5d777388
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 21, 2025

## Environment variable limits increase for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now supports up to 64 environment variables, and each environment variable can be up to 5 KB in size. The previous limit was 5 KB total across all environment variables.

This change enables better support for complex build configurations, larger application settings, and more flexible CI/CD workflows.

For more details, refer to the [build limits documentation](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/#definitions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/#page","headline":"Environment variable limits increase for Workers Builds","description":"Workers Builds now supports up to 64 environment variables per Worker with 5 KB per variable, up from a previous 5 KB total limit.","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/og.png?v=3fc608ad5d777388","dateModified":"2025-11-21","datePublished":"2025-11-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
