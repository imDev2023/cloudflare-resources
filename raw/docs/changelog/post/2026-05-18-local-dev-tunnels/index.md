---
description: You can now share local dev servers through Cloudflare Tunnel from Wrangler and the Cloudflare Vite plugin, with support for quick tunnels and named tunnels.
title: Share local dev servers through Cloudflare Tunnel in Wrangler and Vite
image: https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/og.png?v=94bab0ed20715fb2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 18, 2026

## Share local dev servers through Cloudflare Tunnel in Wrangler and Vite

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now share local dev sessions through [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and get a public URL when using either [Wrangler](https://developers.cloudflare.com/workers/wrangler/) or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). This is useful when you need to share a preview, test a webhook, or access your app from another device.

![Vite local dev tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=678,format=webp/_astro/vite-local-dev-tunnel.CW4xpgIR.gif)

This lets you either:

- start a temporary [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) with a random `*.trycloudflare.com` hostname, or
- use an existing [named tunnel](https://developers.cloudflare.com/tunnel/get-started/#create-a-tunnel) for a stable hostname and to restrict access with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/).

To start a tunnel, press `t` in Wrangler or `t + Enter` in Vite while your dev server is running. For details on setting up a named tunnel, refer to [Share a local dev server](https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/#page","headline":"Share local dev servers through Cloudflare Tunnel in Wrangler and Vite","description":"You can now share local dev servers through Cloudflare Tunnel from Wrangler and the Cloudflare Vite plugin, with support for quick tunnels and named tunnels.","url":"https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/og.png?v=94bab0ed20715fb2","dateModified":"2026-05-18","datePublished":"2026-05-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
