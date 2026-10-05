---
description: Cloudflare Internal DNS is now generally available, consolidating public and private DNS onto a single global control plane.
title: Internal DNS is now generally available
image: https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/og.png?v=3a60125876c0b5df
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 15, 2026

## Internal DNS is now generally available

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.

#### Why it matters

- **Consolidate DNS operations.** Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.
- **Simplify split-horizon DNS.** Internal and external resolution are defined as separate [views](https://developers.cloudflare.com/dns/internal-dns/dns-views/) over shared zones, managed from a single control plane — so there is no drift to chase down.
- **Extend Zero Trust to DNS.** Resolver policies decide which users and devices resolve against which view, enforced by the same [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) that already governs the rest of your traffic.

Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.

```json
POST /zones
{
  "account": {
    "id": "<ACCOUNT_ID>"
  },
  "name": "corp.internal",
  "type": "internal"
}
```

Internal DNS is included with [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for Enterprise customers. To get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/#page","headline":"Internal DNS is now generally available","description":"Cloudflare Internal DNS is now generally available, consolidating public and private DNS onto a single global control plane.","url":"https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/og.png?v=3a60125876c0b5df","dateModified":"2026-07-15","datePublished":"2026-07-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
