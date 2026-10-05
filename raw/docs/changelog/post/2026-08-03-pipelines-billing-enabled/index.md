---
description: Cloudflare Pipelines usage is now billed on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.
title: Billing is now enabled for Pipelines
image: https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/og.png?v=854ffb21fef77ba5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Billing is now enabled for Pipelines

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Billing is now enabled for [Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.

Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:

- **SQL transforms**: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).
- **Sinks (egress)**: $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.

Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) charges apply for data written to R2 buckets, and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply when writing to Iceberg tables.

For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:

| Dimension | Usage | Included | Billable | Cost |
| --- | --- | --- | --- | --- |
| Streams | 500 GB | Unlimited | 0 GB | $0.00 |
| SQL transforms | 500 GB | 50 GB | 450 GB | $18.00 |
| Sinks (Iceberg) | 300 GB | 50 GB | 250 GB | $15.00 |
| **Total** |  |  |  | **$33.00** |

For full pricing details and billing examples, refer to [Pipelines pricing](https://developers.cloudflare.com/basin-pipelines/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/#page","headline":"Billing is now enabled for Pipelines","description":"Cloudflare Pipelines usage is now billed on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/og.png?v=854ffb21fef77ba5","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
