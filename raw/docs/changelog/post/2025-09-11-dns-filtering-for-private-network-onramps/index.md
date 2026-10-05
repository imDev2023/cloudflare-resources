---
description: Magic WAN and WARP Connector traffic can now privately route DNS queries to the Gateway resolver without public Internet exposure.
title: DNS filtering for private network onramps
image: https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/og.png?v=a63071ecfc1f8e3f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2025

## DNS filtering for private network onramps

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Magic WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering) and [WARP Connector](https://developers.cloudflare.com/mesh/features/routes/#dns-filtering) users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.

Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including [Internal DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#internal-dns) and [hostname-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites).

To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, `172.64.36.1` and `172.64.36.2`. Once you configure DNS resolution and filtering, you can use *Source Internal IP* as a traffic selector in your [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) for routing private DNS traffic to your [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/#page","headline":"DNS filtering for private network onramps","description":"Magic WAN and WARP Connector traffic can now privately route DNS queries to the Gateway resolver without public Internet exposure.","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/og.png?v=a63071ecfc1f8e3f","dateModified":"2025-09-11","datePublished":"2025-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
