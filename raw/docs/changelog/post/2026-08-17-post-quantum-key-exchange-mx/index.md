---
description: Cloudflare Email Security now supports post-quantum hybrid key exchange on inbound and outbound SMTP connections.
title: Post-quantum key exchange for MX deployments
image: https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/og.png?v=68a4c51489d38a1d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 17, 2026

## Post-quantum key exchange for MX deployments

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.

Inbound MX connections and outbound delivery connections now negotiate the [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) hybrid key agreement when the peer supports it, protecting SMTP traffic against [harvest-now, decrypt-later ↗︎](https://blog.cloudflare.com/pq-2024/) attacks.

Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/#page","headline":"Post-quantum key exchange for MX deployments","description":"Cloudflare Email Security now supports post-quantum hybrid key exchange on inbound and outbound SMTP connections.","url":"https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/og.png?v=68a4c51489d38a1d","dateModified":"2026-08-17","datePublished":"2026-08-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
