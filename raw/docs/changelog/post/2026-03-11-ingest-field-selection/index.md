---
description: Select specific log fields to ingest into Log Explorer to optimize storage and focus on relevant data.
title: Ingest field selection for Log Explorer
image: https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/og.png?v=6e928181c9d1f5c2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 11, 2026

## Ingest field selection for Log Explorer

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.

Previously, ingesting logs often meant taking an "all or nothing" approach to data fields. With **Ingest Field Selection**, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.

#### Key capabilities

- **Granular control:** Select only the specific fields you need when enabling a new dataset.
- **Dynamic updates:** Update fields for existing, already enabled logstreams at any time.
- **Historical consistency:** Even if you disable a field later, you can still query and receive results for that field for the period it was captured.
- **Data integrity:** Core fields, such as `Timestamp`, are automatically retained to ensure your logs remain searchable and chronologically accurate.

#### Example configuration

When configuring a dataset via the dashboard or API, you can define a specific set of fields. The `Timestamp` field remains mandatory to ensure data indexability.

```json
{
  "dataset": "firewall_events",
  "enabled": true,
  "fields": [
    "Timestamp",
    "ClientRequestHost",
    "ClientIP",
    "Action",
    "EdgeResponseStatus",
    "OriginResponseStatus"
  ]
}
```

For more information, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/#page","headline":"Ingest field selection for Log Explorer","description":"Select specific log fields to ingest into Log Explorer to optimize storage and focus on relevant data.","url":"https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/og.png?v=6e928181c9d1f5c2","dateModified":"2026-03-11","datePublished":"2026-03-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
