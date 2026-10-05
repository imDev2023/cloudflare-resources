---
description: You can now configure origin parameters such as TLS verification, HTTP Host header, connection timeouts, and more when editing a published application in the Cloudflare dashboard.
title: Configure origin application settings for Cloudflare Tunnel in the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/og.png?v=1f20e18c819fac64
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 18, 2026

## Configure origin application settings for Cloudflare Tunnel in the dashboard

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/). These settings control how `cloudflared` connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.

![Configure origin application settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-origin-settings-dashboard.CsC2RwFC.gif)

When editing a published application, expand **Additional application settings** to configure parameters organized into three categories:

- **HTTP** — Set a custom HTTP Host header or disable chunked encoding.
- **TLS** — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.
- **Connection** — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.

[Go to **Tunnels** ↗](https://dash.cloudflare.com/?to=/:account/tunnels)

For the full list of origin parameters, refer to [Origin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/#page","headline":"Configure origin application settings for Cloudflare Tunnel in the dashboard","description":"You can now configure origin parameters such as TLS verification, HTTP Host header, connection timeouts, and more when editing a published application in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/og.png?v=1f20e18c819fac64","dateModified":"2026-08-18","datePublished":"2026-08-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
