---
description: You can now empty an entire bucket or delete folders directly from the R2 dashboard.
title: Empty buckets and delete folders from the R2 dashboard
image: https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/og.png?v=fcb1dcfa170287df
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## Empty buckets and delete folders from the R2 dashboard

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now empty an entire [R2](https://developers.cloudflare.com/r2/) bucket or delete folders directly from the dashboard. Emptying a bucket is required before you can delete it. Previously, this required scripting or configuring [lifecycle rules](https://developers.cloudflare.com/r2/buckets/object-lifecycles/). Now, the dashboard can handle it in a single action.

#### Empty a bucket

Go to your bucket's **Settings** tab and select **Empty** under the **Empty Bucket** section. This deletes all objects in the bucket while preserving the bucket and its configuration. For large buckets, the operation runs in the background and the dashboard displays progress.

Emptying a bucket is also a prerequisite for deleting it. The dashboard now guides you through both steps in one place.

![Empty Bucket and Delete Bucket sections in the R2 dashboard Settings tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3380,height=1776,format=webp/_astro/empty-bucket-changelog.DjuMZppm.png)

#### Delete folders

R2 uses a flat object structure. The dashboard groups objects that share a common prefix into folders when the **View prefixes as directories** checkbox is selected. Deleting a folder removes every object under that prefix.

From the **Objects** tab, you can select one or more folders and delete them alongside individual objects.

For step-by-step instructions, refer to [Delete buckets](https://developers.cloudflare.com/r2/buckets/delete-buckets/) and [Delete objects](https://developers.cloudflare.com/r2/objects/delete-objects/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/#page","headline":"Empty buckets and delete folders from the R2 dashboard","description":"You can now empty an entire bucket or delete folders directly from the R2 dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/og.png?v=fcb1dcfa170287df","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
