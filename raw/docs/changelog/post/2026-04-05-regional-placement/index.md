---
description: Specify regions or jurisdictions to control where your containers run.
title: Control where your Containers run with regional and jurisdictional placement
image: https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/og.png?v=9701a0f14ab6e6bc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 5, 2026

## Control where your Containers run with regional and jurisdictional placement

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now specify placement constraints to control where your [Containers](https://developers.cloudflare.com/containers/) run.

| Constraint | Values | Use case |
| --- | --- | --- |
| `regions` | `ENAM`, `WNAM`, `EEUR`, `WEUR` | Geographic placement |
| `jurisdiction` | `eu`, `fedramp` | Compliance boundaries |

Use `regions` to limit placement to specific geographic areas. Use `jurisdiction` to restrict containers to compliance boundaries — `eu` maps to European regions (EEUR, WEUR) and `fedramp` maps to North American regions (ENAM, WNAM).

Refer to [Containers placement](https://developers.cloudflare.com/containers/concepts/placement/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/#page","headline":"Control where your Containers run with regional and jurisdictional placement","description":"Specify regions or jurisdictions to control where your containers run.","url":"https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/og.png?v=9701a0f14ab6e6bc","dateModified":"2026-04-05","datePublished":"2026-04-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
