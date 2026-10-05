---
description: View per-replica status, Mesh IPs, and connection details for HA-enabled Mesh nodes. Manually promote a passive replica to active directly from the dashboard.
title: High availability replica management for Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/og.png?v=9991d9e43c523672
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## High availability replica management for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) dashboard now shows per-replica details for [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.

![Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1155,format=webp/_astro/mesh-ha-replicas.Dvf1GMmQ.gif)

#### What's new

- **Replica tabs** on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.
- **Active/passive badges** identify which replica is currently routing traffic.
- **Manual failover** — promote a passive replica to active with a single click. The previous active replica switches to standby.
- **HA badge** in the overview table identifies nodes running multiple replicas.
- **Active replica IP** shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.

#### Manual failover

To manually promote a passive replica:

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/mesh), go to **Networking** > **Mesh**.
2. Select an HA-enabled node.
3. Select the passive replica tab.
4. Select **Promote to active** and confirm.

Traffic reroutes to the promoted replica immediately. Refer to [High availability](https://developers.cloudflare.com/mesh/features/high-availability/) for details on failover behavior.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/#page","headline":"High availability replica management for Cloudflare Mesh","description":"View per-replica status, Mesh IPs, and connection details for HA-enabled Mesh nodes. Manually promote a passive replica to active directly from the dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/og.png?v=9991d9e43c523672","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
