---
description: Workers Builds and Cloudflare Pages now have documented build image policies outlining deprecation timelines and version update procedures.
title: Build image policies for Workers Builds and Cloudflare Pages
image: https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/og.png?v=c38e77417d105f2a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 18, 2025

## Build image policies for Workers Builds and Cloudflare Pages

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've published build image policies for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#build-image-policy) and [Cloudflare Pages](https://developers.cloudflare.com/pages/configuration/build-image/#build-image-policy), which establish:

- **Minor version updates**: We typically update preinstalled software to the latest available minor version without notice. For tools that don't follow semantic versioning (e.g., Bun or Hugo), we provide 3 months’ notice.
- **Major version updates**: Before preinstalled software reaches end-of-life, we update to the next stable LTS version with 3 months’ notice.
- **Build image version deprecation (Pages only)**: We provide 6 months’ notice before deprecation. Projects on v1 or v2 will be automatically moved to v3 on their specified deprecation dates.

To prepare for updates, monitor the [Cloudflare Changelog ↗︎](https://developers.cloudflare.com/changelog/), dashboard notifications, and email. You can also [override default versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#overriding-default-versions) to maintain specific versions.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/#page","headline":"Build image policies for Workers Builds and Cloudflare Pages","description":"Workers Builds and Cloudflare Pages now have documented build image policies outlining deprecation timelines and version update procedures.","url":"https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/og.png?v=c38e77417d105f2a","dateModified":"2025-12-18","datePublished":"2025-12-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
