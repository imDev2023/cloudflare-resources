---
description: IPsec and GRE tunnel configuration now shows pre-loaded Anycast IPs
title: Anycast IPs displayed on the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/og.png?v=0b06825ee9ca5613
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2026

## Anycast IPs displayed on the dashboard

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.

Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.

No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.

For more information, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/#page","headline":"Anycast IPs displayed on the dashboard","description":"IPsec and GRE tunnel configuration now shows pre-loaded Anycast IPs","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/og.png?v=0b06825ee9ca5613","dateModified":"2026-02-12","datePublished":"2026-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
