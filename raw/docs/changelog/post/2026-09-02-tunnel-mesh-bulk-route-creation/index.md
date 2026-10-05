---
description: The Routes page now supports adding multiple destinations and queuing up several Cloudflare Tunnel and Cloudflare Mesh routes before creating them in a single action.
title: Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once
image: https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/og.png?v=11c81f919227c808
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

- **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
- **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
- **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.

The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/#page","headline":"Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once","description":"The Routes page now supports adding multiple destinations and queuing up several Cloudflare Tunnel and Cloudflare Mesh routes before creating them in a single action.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/og.png?v=11c81f919227c808","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
