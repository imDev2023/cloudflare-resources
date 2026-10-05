---
description: View table maintenance schedules and run history, queue compaction from the dashboard, and browse catalogs with an updated layout.
title: R2 Data Catalog adds table maintenance visibility and manual queueing
image: https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/og.png?v=7d71f5cf05701f1d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 16, 2026

## R2 Data Catalog adds table maintenance visibility and manual queueing

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.

To view table maintenance details:

1. In the Cloudflare dashboard, go to **R2 Data Catalog**.
2. Select a catalog, then select the **Explorer** tab. The **Explorer** tab opens by default.
3. Select a table.
4. Select the **Maintenance** tab.

![Maintenance tab for an R2 Data Catalog table showing schedules and recent runs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=1544,format=webp/_astro/table-maintenance-view.C7KRSK-K.png)

The updated dashboard includes:

- **Maintenance tab** — View compaction and snapshot expiration settings, schedules, and next eligibility alongside the table's **Schema** and **Metadata** tabs.
- **Recent runs** — Review a paginated audit log with job status, duration, and expandable details for manifest rewrites, compaction, and snapshot expiration. Expanded rows include operation metrics for each maintenance operation.
- **Manual queueing** — Select **Queue maintenance** to request compaction during normal scheduler polling. The dashboard checks permissions and explains when another maintenance job conflicts with the request or the daily accepted-request limit has been reached.
- **Updated catalog layout** — Find catalog metrics in the **Metrics** tab, use the renamed **Explorer** tab to browse data, and switch between table details using tabs instead of a scroll-to-section sidebar.
- **Improved schema browser** — For accounts with the schema browser enabled, select a namespace to open its tables in the right pane while also expanding the namespace tree. The tree can now be collapsed to provide more space for table details.

For more information about compaction and snapshot expiration, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/#page","headline":"R2 Data Catalog adds table maintenance visibility and manual queueing","description":"View table maintenance schedules and run history, queue compaction from the dashboard, and browse catalogs with an updated layout.","url":"https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/og.png?v=7d71f5cf05701f1d","dateModified":"2026-09-16","datePublished":"2026-09-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
