---
description: Connect a Cursor Origin repository to Workers Builds for automatic deployments, branch previews, and build status in Origin.
title: Workers Builds now supports Cursor Origin
image: https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/og.png?v=9b9120ec98b715f9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2026

## Workers Builds now supports Cursor Origin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Builds now supports repositories hosted in Cursor Origin. Connect a Cursor Origin repository to automatically build and deploy production changes, preview non-production branches, and see build status in pull requests.

Pushes to your production branch automatically build and deploy your Worker. When you enable [non-production branch builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds), each branch receives a version-specific preview URL and a stable preview URL that follows the latest build.

Cloudflare posts build status and preview links to the Cursor Origin pull request and creates a check run for each triggered build.

To get started, install the [Cloudflare app in Cursor ↗︎](https://cursor.com/codebase/settings/apps/public/cloudflare), choose the Cursor Origin repositories Cloudflare can access, and follow the prompts to configure your Worker build. For details, refer to the [Cursor Origin integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/#page","headline":"Workers Builds now supports Cursor Origin","description":"Connect a Cursor Origin repository to Workers Builds for automatic deployments, branch previews, and build status in Origin.","url":"https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/og.png?v=9b9120ec98b715f9","dateModified":"2026-09-22","datePublished":"2026-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
