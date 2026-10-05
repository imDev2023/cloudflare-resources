---
description: Record object operations with response status codes below 400 and inspect per-request events in Workers Observability.
title: R2 Data Access Logs
image: https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/og.png?v=cced01881ac6732b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2026

## R2 Data Access Logs

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below `400`.

Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through `r2.dev` or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.

Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.

Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to [R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/#page","headline":"R2 Data Access Logs","description":"Record object operations with response status codes below 400 and inspect per-request events in Workers Observability.","url":"https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/og.png?v=cced01881ac6732b","dateModified":"2026-09-04","datePublished":"2026-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
