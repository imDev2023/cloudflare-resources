---
description: The dashboard and Wrangler now warn you before manual delete operations that could corrupt an R2 Data Catalog.
title: R2 Data Catalog warns before you delete data manually
image: https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/og.png?v=61bc8d7b49c3b7b6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 7, 2026

## R2 Data Catalog warns before you delete data manually

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.

To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.

#### Dashboard

When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.

![R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1886,height=684,format=webp/_astro/data-catalog-delete-warning.DoBR0sFO.png)

#### Wrangler

Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:

```txt
Data Catalog is enabled for this bucket. 
Proceeding may leave the data catalog in an invalid state. Continue?
```

To learn how to safely manage and delete data in your tables, refer to the [R2 Data Catalog documentation](https://developers.cloudflare.com/basin-catalog/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/#page","headline":"R2 Data Catalog warns before you delete data manually","description":"The dashboard and Wrangler now warn you before manual delete operations that could corrupt an R2 Data Catalog.","url":"https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/og.png?v=61bc8d7b49c3b7b6","dateModified":"2026-07-07","datePublished":"2026-07-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
