---
description: Gateway now supports egressing customer traffic using IPv4/v6 prefixes they already own.
title: Gateway BYOIP Dedicated Egress IPs now available.
image: https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/og.png?v=e9f8feb6276faa3e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2025

## Gateway BYOIP Dedicated Egress IPs now available.

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.

Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.

Get started by following the [BYOIP onboarding process](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip). Once your IPs are onboarded, go to **Gateway** > **Egress policies** and select or create an egress policy. In **Select an egress IP**, choose *Use dedicated egress IPs (Cloudflare or BYOIP)*, then select your BYOIP address from the dropdown menu.

![Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=933,height=459,format=webp/_astro/Gateway-byoip-dedicated-egress-ips.D0pzLAbV.png)

For more information, refer to [BYOIP for dedicated egress IPs](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/#page","headline":"Gateway BYOIP Dedicated Egress IPs now available.","description":"Gateway now supports egressing customer traffic using IPv4/v6 prefixes they already own.","url":"https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/og.png?v=e9f8feb6276faa3e","dateModified":"2025-08-21","datePublished":"2025-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
