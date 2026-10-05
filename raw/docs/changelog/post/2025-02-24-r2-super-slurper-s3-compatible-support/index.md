---
description: Super Slurper now supports migrations from all S3-compatible storage providers
title: Super Slurper now supports migrations from all S3-compatible storage providers
image: https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/og.png?v=771a5a98d053784a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2025

## Super Slurper now supports migrations from all S3-compatible storage providers

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) can now migrate data from any S3-compatible object storage provider to [Cloudflare R2](https://developers.cloudflare.com/r2/). This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.

![Super Slurper S3-Compatible Source](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=757,height=348,format=webp/_astro/super-slurper-s3-compat-screenshot-border.D8Gd5eye.png)

For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our [documentation](https://developers.cloudflare.com/r2/data-migration/super-slurper/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/#page","headline":"Super Slurper now supports migrations from all S3-compatible storage providers","description":"Super Slurper now supports migrations from all S3-compatible storage providers","url":"https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/og.png?v=771a5a98d053784a","dateModified":"2025-02-24","datePublished":"2025-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
