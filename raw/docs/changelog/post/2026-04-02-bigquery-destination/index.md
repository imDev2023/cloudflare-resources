---
description: Enable BigQuery as a Logpush destination
title: BigQuery as Logpush destination
image: https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/og.png?v=35462e4d62aca12c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 2, 2026

## BigQuery as Logpush destination

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush now supports **BigQuery** as a native destination.

Logs from Cloudflare can be sent to [Google Cloud BigQuery ↗︎](https://cloud.google.com/bigquery) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

For more information, refer to the [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/#page","headline":"BigQuery as Logpush destination","description":"Enable BigQuery as a Logpush destination","url":"https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/og.png?v=35462e4d62aca12c","dateModified":"2026-04-02","datePublished":"2026-04-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
