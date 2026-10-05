---
description: Hybrid ML-KEM protects appliance traffic against harvest-now, decrypt-later attacks
title: Post-quantum encryption support for Cloudflare One Appliance
image: https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/og.png?v=999e417c1e52d767
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 11, 2026

## Post-quantum encryption support for Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One Appliance version 2026.2.0 adds [post-quantum encryption](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.

This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.

For more information, refer to [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/#page","headline":"Post-quantum encryption support for Cloudflare One Appliance","description":"Hybrid ML-KEM protects appliance traffic against harvest-now, decrypt-later attacks","url":"https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/og.png?v=999e417c1e52d767","dateModified":"2026-02-11","datePublished":"2026-02-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
