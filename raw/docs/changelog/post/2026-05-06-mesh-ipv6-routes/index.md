---
description: Cloudflare Mesh nodes now support advertising IPv6 CIDR routes in addition to IPv4.
title: IPv6 CIDR routes for Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/og.png?v=4452464acd6ccb5b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 6, 2026

## IPv6 CIDR routes for Cloudflare Mesh

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.

![IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2906,height=1352,format=webp/_astro/mesh-ipv6-routes.CC-jlZkw.png)

To add an IPv6 route, follow the same steps as [adding an IPv4 route](https://developers.cloudflare.com/mesh/features/routes/#add-a-route) — enter the IPv6 CIDR (for example, `fd00::/64`) when configuring the route in the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/mesh) or via the API.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/#page","headline":"IPv6 CIDR routes for Cloudflare Mesh","description":"Cloudflare Mesh nodes now support advertising IPv6 CIDR routes in addition to IPv4.","url":"https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/og.png?v=4452464acd6ccb5b","dateModified":"2026-05-06","datePublished":"2026-05-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
