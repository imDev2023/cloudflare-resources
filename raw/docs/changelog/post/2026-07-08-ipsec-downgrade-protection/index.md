---
description: Cloudflare IPsec now supports the IKE_SA_INIT_FULL_TRANSCRIPT_AUTH extension to prevent quantum downgrade attacks on IKEv2 tunnels.
title: IPsec downgrade protection (beta)
image: https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/og.png?v=d15eaf7581dd67ee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2026

## IPsec downgrade protection (beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare IPsec now supports the [`IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/) IKEv2 extension to protect against downgrade attacks on IPsec tunnels.

IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable [on-path attacker ↗︎](https://www.cloudflare.com/learning/security/threats/on-path-attack/) can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.

Key details:

- Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.
- Cloudflare sends the `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` notification unconditionally as a responder when the feature flag is enabled.
- Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.
- This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.

Refer to [Downgrade protection](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/#page","headline":"IPsec downgrade protection (beta)","description":"Cloudflare IPsec now supports the IKE_SA_INIT_FULL_TRANSCRIPT_AUTH extension to prevent quantum downgrade attacks on IKEv2 tunnels.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/og.png?v=d15eaf7581dd67ee","dateModified":"2026-07-08","datePublished":"2026-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
