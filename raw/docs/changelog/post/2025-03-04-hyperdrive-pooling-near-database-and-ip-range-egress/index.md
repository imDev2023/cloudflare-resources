---
description: Hyperdrive now pools database connections closer to your database to reduce query latency, and now also provides a documented IP address range for IP ACLs.
title: Hyperdrive reduces query latency by up to 90% and now supports IP access control lists
image: https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/og.png?v=d87efb80722824eb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 7, 2025

## Hyperdrive reduces query latency by up to 90% and now supports IP access control lists

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.

![Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1732,height=836,format=webp/_astro/hyperdrive-regional-pooling-query-latency-improvement.Bzz_xvHZ.png)

By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.

With this update, Hyperdrive also uses [Cloudflare's standard IP address ranges ↗︎](https://www.cloudflare.com/ips/) to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.

Refer to [documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).

This improvement is enabled on all Hyperdrive configurations.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/#page","headline":"Hyperdrive reduces query latency by up to 90% and now supports IP access control lists","description":"Hyperdrive now pools database connections closer to your database to reduce query latency, and now also provides a documented IP address range for IP ACLs.","url":"https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/og.png?v=d87efb80722824eb","dateModified":"2025-03-07","datePublished":"2025-03-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
