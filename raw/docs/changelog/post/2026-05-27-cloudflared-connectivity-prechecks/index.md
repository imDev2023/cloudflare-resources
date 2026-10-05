---
description: Starting with cloudflared 2026.5.2, Cloudflare Tunnel automates the connectivity pre-check workflow at startup — no more manual dig and netcat commands.
title: Cloudflare Tunnel now runs connectivity pre-checks at startup
image: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/og.png?v=07f32d2cef3d3888
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 27, 2026

## Cloudflare Tunnel now runs connectivity pre-checks at startup

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting with [`cloudflared` version 2026.5.2 ↗︎](https://github.com/cloudflare/cloudflared/releases), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) automates the entire [connectivity pre-checks workflow](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/) directly inside the binary. Previously, customers had to install `dig` and `netcat` and run those commands by hand to verify their environment. Now `cloudflared` does it natively at startup — and surfaces actionable remediation when something is blocked.

![cloudflared connectivity pre-checks output](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1012,format=webp/_astro/cloudflared-connectivity-prechecks.DRwN6tGe.gif)

On every `cloudflared tunnel run` (and `cloudflared tunnel diag`), the binary now natively checks:

- **DNS resolution** — `region1.v2.argotunnel.com` and `region2.v2.argotunnel.com` resolve to valid Cloudflare IPs.
- **Transport connectivity** — outbound `UDP (QUIC)` and `TCP (HTTP/2)` on port `7844`.
- **Management API** — outbound `TCP/443` to `api.cloudflare.com` for software updates.

Results are printed in a scannable CLI table with three states:

- ✅ **Pass** — the check succeeded.
- ⚠️ **Warn** — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.
- ❌ **Fail** — a blocking issue, with a specific remediation hint (for example, `Allow outbound UDP on port 7844`).

If DNS is unresolvable, or **both** UDP and TCP fail on port 7844, `cloudflared` exits early with the failure rather than looping on opaque `failed to dial` errors.

Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.

To get the new behavior, upgrade `cloudflared` to version `2026.5.2` or later. For more details, refer to the [Connectivity pre-checks documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/#page","headline":"Cloudflare Tunnel now runs connectivity pre-checks at startup","description":"Starting with cloudflared 2026.5.2, Cloudflare Tunnel automates the connectivity pre-check workflow at startup — no more manual dig and netcat commands.","url":"https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/og.png?v=07f32d2cef3d3888","dateModified":"2026-05-27","datePublished":"2026-05-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
