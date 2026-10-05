---
description: Super Slurper now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to Cloudflare R2 up to 5x faster
title: Super Slurper now transfers data to R2 up to 5x faster
image: https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/og.png?v=18479b2f9162158d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 14, 2025

## Super Slurper now transfers data to R2 up to 5x faster

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to [Cloudflare R2](https://developers.cloudflare.com/r2/) up to 5x faster than it did before.

We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using [Cloudflare Workers](https://developers.cloudflare.com/workers/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Queues](https://developers.cloudflare.com/queues/) — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)

![Super Slurper Objects Migrated](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=974,height=493,format=webp/_astro/slurper-objects-over-time-border.BFDkMQUw.png)

*Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)*

For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our [documentation](https://developers.cloudflare.com/r2/data-migration/super-slurper/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/#page","headline":"Super Slurper now transfers data to R2 up to 5x faster","description":"Super Slurper now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to Cloudflare R2 up to 5x faster","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/og.png?v=18479b2f9162158d","dateModified":"2025-02-14","datePublished":"2025-02-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
