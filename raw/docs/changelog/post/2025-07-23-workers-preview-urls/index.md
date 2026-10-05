---
description: Get shareable preview links for every code change you make to a Cloudflare Worker, making it easier to test and collaborate before going live
title: Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers
image: https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/og.png?v=3c142a8dfb287261
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 22, 2025

## Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.

This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch. These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.

![PR comment preview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2900,height=1064,format=webp/_astro/preview-urls-comment.0wQffFIq.png)

#### Preview URL types

Each comment includes **two preview URLs** as shown above:

- **Commit Preview URL**: Unique to the specific version/commit (e.g., `<version-prefix>-<worker-name>.<subdomain>.workers.dev`)
- **Branch Preview URL**: A stable alias based on the branch name (e.g., `<branch-name>-<worker-name>.<subdomain>.workers.dev`)

#### How it works

When you create a pull request:

- **A preview alias is automatically created** based on the Git branch name (e.g., `<branch-name>` becomes `<branch-name>-<worker-name>.<subdomain>.workers.dev`)
- **No configuration is needed**, the alias is generated for you
- **The link stays the same** even as you add commits to the same branch
- **Preview URLs are posted directly to your pull request as comments** (just like they are in Cloudflare Pages)

#### Custom alias name

You can also assign a custom preview alias using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/), by passing the `--preview-alias` flag when [uploading a version](https://developers.cloudflare.com/workers/wrangler/commands/general/#versions-upload) of your Worker:

```bash
wrangler versions upload --preview-alias staging
```

#### Limitations while in beta

- Only available on the **workers.dev** subdomain (custom domains not yet supported)
- Requires **Wrangler v4.21.0+**
- Preview URLs are not generated for Workers that use [Durable Objects](https://developers.cloudflare.com/durable-objects/)
- Not yet supported for [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/#page","headline":"Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers","description":"Get shareable preview links for every code change you make to a Cloudflare Worker, making it easier to test and collaborate before going live","url":"https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/og.png?v=3c142a8dfb287261","dateModified":"2025-07-22","datePublished":"2025-07-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
