---
description: Remotely restart managed services, power cycle, or shut down a Cloudflare One Appliance — with optional persistent state purge.
title: Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/og.png?v=702f968796e90631
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 17, 2026

## Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now restart, reboot, or shut down a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard or via API.

![Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-07-17-appliance-restart-reboot-shutdown.DKqTLOh6.gif)

- **Restart** — Restart managed services. Purges temporary and (optionally) persistent state.
- **Reboot** — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.
- **Shutdown** — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.

In the dashboard, go to **Networking** > **Connectors** > **Appliances**, select an appliance, then **Edit** > **Operations** to send an operation. Via API, `POST` to the `/accounts/{account_id}/magic/connectors/{connector_id}/interrupts` endpoint.

For details, refer to [Appliance operations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/#page","headline":"Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard","description":"Remotely restart managed services, power cycle, or shut down a Cloudflare One Appliance — with optional persistent state purge.","url":"https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/og.png?v=702f968796e90631","dateModified":"2026-07-17","datePublished":"2026-07-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
