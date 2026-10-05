---
description: Cloudflare One Client for Linux (version 2026.6.836.0)
title: Cloudflare One Client for Linux (version 2026.6.836.0)
image: https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/og.png?v=547d2fc225fde87e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Cloudflare One Client for Linux (version 2026.6.836.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.

If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:

```bash
sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo
sudo dnf clean all
sudo dnf install cloudflare-warp
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/#page","headline":"Cloudflare One Client for Linux (version 2026.6.836.0)","description":"Cloudflare One Client for Linux (version 2026.6.836.0)","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/og.png?v=547d2fc225fde87e","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
