---
description: Cloudflare IPsec post-quantum key agreement is now generally available with validated third-party platforms.
title: Post-quantum IPsec interoperability with third-party devices
image: https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/og.png?v=c8c25eb4d6835ddc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## Post-quantum IPsec interoperability with third-party devices

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. [Cisco ↗︎](https://www.cisco.com/) and [Fortinet ↗︎](https://www.fortinet.com/) are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

Post-quantum IPsec uses [RFC 9370 ↗︎](https://datatracker.ietf.org/doc/rfc9370/) and [draft-ietf-ipsecme-ikev2-mlkem ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) to negotiate hybrid key agreement during the IKEv2 `IKE_INTERMEDIATE` phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against [harvest-now, decrypt-later ↗︎](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) attacks.

Key details:

- Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.
- Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.
- Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.
- No additional licensing required.

Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.

For supported key exchange methods and the list of validated platforms, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/#page","headline":"Post-quantum IPsec interoperability with third-party devices","description":"Cloudflare IPsec post-quantum key agreement is now generally available with validated third-party platforms.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/og.png?v=c8c25eb4d6835ddc","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
