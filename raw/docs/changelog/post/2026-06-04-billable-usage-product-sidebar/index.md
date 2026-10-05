---
description: View current spend and create budget alerts without leaving the product page.
title: Billable usage and budget alerts now in product sidebars
image: https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/og.png?v=f695b9c01007b60a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 4, 2026

## Billable usage and budget alerts now in product sidebars

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/) [D1](https://developers.cloudflare.com/d1/) [R2](https://developers.cloudflare.com/r2/) [KV](https://developers.cloudflare.com/kv/) [Queues](https://developers.cloudflare.com/queues/) [Vectorize](https://developers.cloudflare.com/vectorize/) [Durable Objects](https://developers.cloudflare.com/durable-objects/) [Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/#page","headline":"Billable usage and budget alerts now in product sidebars","description":"View current spend and create budget alerts without leaving the product page.","url":"https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/og.png?v=f695b9c01007b60a","dateModified":"2026-06-04","datePublished":"2026-06-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
