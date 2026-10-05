---
description: A unified Routes page in the dashboard shows the routes for your Cloudflare Mesh, Cloudflare Tunnel, Cloudflare WAN, and Magic Transit connectors in one place, with an interactive network map.
title: Manage all your routes from one page in the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/og.png?v=b4cc5f82a4bf4d60
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2026

## Manage all your routes from one page in the dashboard

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

- **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
- **See every route in one table**, with its destination, type, connector, priority, and source, and filter or sort to find what you need.
- **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
- **Manage [virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
- **Test a route** to see which connector and next hop a destination resolves to before you commit a change.

To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/#page","headline":"Manage all your routes from one page in the dashboard","description":"A unified Routes page in the dashboard shows the routes for your Cloudflare Mesh, Cloudflare Tunnel, Cloudflare WAN, and Magic Transit connectors in one place, with an interactive network map.","url":"https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/og.png?v=b4cc5f82a4bf4d60","dateModified":"2026-06-19","datePublished":"2026-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
