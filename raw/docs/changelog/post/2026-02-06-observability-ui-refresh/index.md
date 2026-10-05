---
description: The new Workers Observability dashboard includes new features like data visualizations, shareable links, and exports (JSON/CSV).
title: Visualize data, share links, and create exports with the new Workers Observability dashboard
image: https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/og.png?v=355ed4a6458af402
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 6, 2026

## Visualize data, share links, and create exports with the new Workers Observability dashboard

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Workers Observability dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/) has some major updates to make it easier to debug your application's issues and share findings with your team.

![Workers Observability dashboard showing events view with event details and share options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2540,height=1170,format=webp/_astro/2026-01-22-events_share_obs_wobs.BvzY4TNV.png)

You can now:

- **Create visualizations** — Build charts from your Worker data directly in a Worker's Observability tab
- **Export data as JSON or CSV** — Download logs and traces for offline analysis or to share with teammates
- **Share events and traces** — Generate direct URLs to specific events, invocations, and traces that open standalone pages with full context
- **Customize table columns** — Improved field picker to add, remove, and reorder columns in the events table
- **Expandable event details** — Expand events inline to view full details without leaving the table
- **Keyboard shortcuts** — Navigate the dashboard with hotkey support

![Workers Observability dashboard showing a P99 CPU time visualization grouped by outcome](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2596,height=1314,format=webp/_astro/2026-01-22-vis_qb_wobs.Bb5eVQNT.png)

These updates are now live in the Cloudflare dashboard, both in a Worker's Observability tab and in the account-level Observability dashboard for a unified experience. To get started, go to **Workers & Pages** > select your Worker > **Observability**.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/#page","headline":"Visualize data, share links, and create exports with the new Workers Observability dashboard","description":"The new Workers Observability dashboard includes new features like data visualizations, shareable links, and exports (JSON/CSV).","url":"https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/og.png?v=355ed4a6458af402","dateModified":"2026-02-06","datePublished":"2026-02-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
