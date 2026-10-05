---
description: Create, run, and manage Cloudflare Tunnels directly from the Wrangler CLI without leaving your terminal.
title: Manage Cloudflare Tunnels with Wrangler
image: https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/og.png?v=758346f1d4d48d72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 19, 2026

## Manage Cloudflare Tunnels with Wrangler

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage [Cloudflare Tunnels](https://developers.cloudflare.com/tunnel/) directly from [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for the Cloudflare Developer Platform. The new [`wrangler tunnel`](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/) commands let you create, run, and manage tunnels without leaving your terminal.

![Wrangler tunnel commands demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1094,format=webp/_astro/wrangler-tunnel.DOqrtGGg.gif)

Available commands:

- `wrangler tunnel create` — Create a new remotely managed tunnel.
- `wrangler tunnel list` — List all tunnels in your account.
- `wrangler tunnel info` — Display details about a specific tunnel.
- `wrangler tunnel delete` — Delete a tunnel.
- `wrangler tunnel run` — Run a tunnel using the cloudflared daemon.
- `wrangler tunnel quick-start` — Start a free, temporary tunnel without an account using [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

Wrangler handles downloading and managing the [cloudflared](https://developers.cloudflare.com/tunnel/downloads/) binary automatically. On first use, you will be prompted to download `cloudflared` to a local cache directory.

These commands are currently experimental and may change without notice.

To get started, refer to the [Wrangler tunnel commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/#page","headline":"Manage Cloudflare Tunnels with Wrangler","description":"Create, run, and manage Cloudflare Tunnels directly from the Wrangler CLI without leaving your terminal.","url":"https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/og.png?v=758346f1d4d48d72","dateModified":"2026-03-19","datePublished":"2026-03-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
