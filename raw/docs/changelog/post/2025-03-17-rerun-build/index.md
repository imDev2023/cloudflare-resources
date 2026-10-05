---
description: Rerun builds for your Workers and Pages projects directly inside of GitHub.
title: Retry Pages &amp; Workers Builds Directly from GitHub
image: https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/og.png?v=ae53e3198c3e10ae
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 17, 2025

## Retry Pages & Workers Builds Directly from GitHub

[Workers](https://developers.cloudflare.com/workers/) [Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!

Let\\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.

For Pages and Workers projects connected to a GitHub repository:

1. When a build fails, go to your GitHub repository or pull request
2. Select the failed Check Run for the build
3. Select "Details" on the Check Run
4. Select "Rerun" to trigger a retry build for that commit

Learn more about [Pages Builds](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/) and [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/#page","headline":"Retry Pages & Workers Builds Directly from GitHub","description":"Rerun builds for your Workers and Pages projects directly inside of GitHub.","url":"https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/og.png?v=ae53e3198c3e10ae","dateModified":"2025-03-17","datePublished":"2025-03-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
