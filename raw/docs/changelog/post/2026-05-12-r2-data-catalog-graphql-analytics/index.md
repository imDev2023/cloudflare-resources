---
description: Monitor Iceberg REST API operations and table maintenance jobs for your R2 Data Catalog warehouses using the GraphQL Analytics API.
title: R2 Data Catalog now exposes metrics via the GraphQL Analytics API
image: https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/og.png?v=c303671747eb55b6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## R2 Data Catalog now exposes metrics via the GraphQL Analytics API

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), Spark, Snowflake, and DuckDB to your data in R2.

You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). Two new datasets are available:

- **`r2CatalogDataOperationsAdaptiveGroups`** tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.
- **`r2CatalogTableMaintenanceAdaptiveGroups`** tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.

Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.

For detailed schema information and example queries, refer to the [R2 Data Catalog metrics and analytics documentation](https://developers.cloudflare.com/basin-catalog/observability/metrics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/#page","headline":"R2 Data Catalog now exposes metrics via the GraphQL Analytics API","description":"Monitor Iceberg REST API operations and table maintenance jobs for your R2 Data Catalog warehouses using the GraphQL Analytics API.","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/og.png?v=c303671747eb55b6","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
