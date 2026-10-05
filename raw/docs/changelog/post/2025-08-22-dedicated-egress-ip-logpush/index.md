---
description: Set up dedicated egress IPs for Logpush using Aegis IPs
title: Dedicated Egress IP for Logpush
image: https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/og.png?v=c845249a40f6ae22
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 22, 2025

## Dedicated Egress IP for Logpush

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with [Aegis IP](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/), your log destination only needs to allow Aegis IPs making setup more secure.

Highlights:

- Fixed egress IPs ensure your destination only accepts traffic from known addresses.
- Works with any supported Logpush destination.
- Recommended to use a dedicated zone as a proxy for easier management.

To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the [Logpush documentation](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/#page","headline":"Dedicated Egress IP for Logpush","description":"Set up dedicated egress IPs for Logpush using Aegis IPs","url":"https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/og.png?v=c845249a40f6ae22","dateModified":"2025-08-22","datePublished":"2025-08-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
