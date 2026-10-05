---
description: Configure Logpush to Google BigQuery directly from the Cloudflare dashboard.
title: Logpush to BigQuery — Cloudflare dashboard support
image: https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/og.png?v=9cce73925a75e931
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## Logpush to BigQuery — Cloudflare dashboard support

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.

Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the **Logpush** page in the Cloudflare dashboard by selecting **Google BigQuery** as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.

For more information, refer to [Enable Logpush to Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/#page","headline":"Logpush to BigQuery — Cloudflare dashboard support","description":"Configure Logpush to Google BigQuery directly from the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/og.png?v=9cce73925a75e931","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
