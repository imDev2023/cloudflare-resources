---
description: DHCP server settings now accept multiple DNS server IP addresses
title: Cloudflare One Appliance supports multiple DNS server IPs
image: https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/og.png?v=0a7cf8e01e54b018
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2025

## Cloudflare One Appliance supports multiple DNS server IPs

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.

Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.

For configuration details, refer to [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/#page","headline":"Cloudflare One Appliance supports multiple DNS server IPs","description":"DHCP server settings now accept multiple DNS server IP addresses","url":"https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/og.png?v=0a7cf8e01e54b018","dateModified":"2025-04-30","datePublished":"2025-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
