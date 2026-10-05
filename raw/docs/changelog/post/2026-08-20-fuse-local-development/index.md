---
description: Local Containers support FUSE with compatible Docker configurations.
title: Use FUSE in local Containers development
image: https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/og.png?v=654c31365c989a86
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## Use FUSE in local Containers development

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to `wrangler dev`, the Cloudflare Vite plugin, and direct Miniflare use.

Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when `/dev/fuse` is available.

Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.

For requirements and troubleshooting, refer to [FUSE support during local development](https://developers.cloudflare.com/containers/guides/local-dev/#fuse-support). For a complete example, refer to [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/#page","headline":"Use FUSE in local Containers development","description":"Local Containers support FUSE with compatible Docker configurations.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/og.png?v=654c31365c989a86","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
