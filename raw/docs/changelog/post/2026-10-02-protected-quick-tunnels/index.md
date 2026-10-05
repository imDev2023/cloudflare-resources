---
description: Restrict access to a Quick Tunnel to specific email addresses or domains using the new --allowed-mail flag in cloudflared.
title: Protect Quick Tunnels with email authentication
image: https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/og.png?v=cd8d55a72ec2ec02
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## Protect Quick Tunnels with email authentication

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.

```sh
cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com
```

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

- A single email address: `--allowed-mail alice@example.com`
- Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
- Every address on a domain: `--allowed-mail '*@example.com'`

Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/#page","headline":"Protect Quick Tunnels with email authentication","description":"Restrict access to a Quick Tunnel to specific email addresses or domains using the new --allowed-mail flag in cloudflared.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/og.png?v=cd8d55a72ec2ec02","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
