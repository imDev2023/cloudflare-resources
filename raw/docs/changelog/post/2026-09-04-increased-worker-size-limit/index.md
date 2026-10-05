---
description: The compressed Worker size limits (3 MB free / 10 MB paid) have been removed. Cloudflare now only checks the uncompressed bundle size, which is 64 MiB across all plans.
title: Deploy larger Workers — up to 64 MiB for both free and paid plans
image: https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/og.png?v=2a863311c9454bfe
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2026

## Deploy larger Workers — up to 64 MiB for both free and paid plans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.

When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.

To check your Worker's bundle size before deploying:

```sh
wrangler deploy --outdir bundled/ --dry-run
```

```sh
Total Upload: 259.61 KiB / gzip: 47.23 KiB
```

The `Total Upload` value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The `gzip` value is shown for reference but is no longer a limit.

For more information, refer to the [Worker size limits documentation](https://developers.cloudflare.com/workers/platform/limits/#worker-size).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/#page","headline":"Deploy larger Workers — up to 64 MiB for both free and paid plans","description":"The compressed Worker size limits (3 MB free / 10 MB paid) have been removed. Cloudflare now only checks the uncompressed bundle size, which is 64 MiB across all plans.","url":"https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/og.png?v=2a863311c9454bfe","dateModified":"2026-09-04","datePublished":"2026-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
