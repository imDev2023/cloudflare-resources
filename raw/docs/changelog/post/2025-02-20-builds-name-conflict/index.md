---
description: Workers Builds automatically creates a pull request to update the name field in the wrangler file if it doesn’t match your Worker's name in the Cloudflare dashboard.
title: Autofix Worker name configuration errors at build time
image: https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/og.png?v=27257e82682e4807
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 20, 2025

## Autofix Worker name configuration errors at build time

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![Auto-fixing Workers Name in Git Repo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2416,height=1128,format=webp/_astro/gh-auto-pr-name.BHTtigEg.png)

Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.

Here's how it works:

1. Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.
2. Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.
3. Once you merge this pull request, Cloudflare will run another build.

We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.

This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, [#workers-and-pages-feature-suggestions ↗︎](https://discord.com/channels/595317990191398933/1064502845061210152).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/#page","headline":"Autofix Worker name configuration errors at build time","description":"Workers Builds automatically creates a pull request to update the name field in the wrangler file if it doesn’t match your Worker's name in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/og.png?v=27257e82682e4807","dateModified":"2025-02-20","datePublished":"2025-02-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
