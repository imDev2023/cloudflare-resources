---
description: Cloudflare now automatically finds the most secure key agreement algorithm preferred by your origin servers, helping establish TLS 1.3 connections faster via Post-Quantum Encryption.
title: Faster and more secure TLS handshakes to your origins, automatically
image: https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/og.png?v=35a9109c16928f72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 21, 2026

## Faster and more secure TLS handshakes to your origins, automatically

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first `ClientHello`, helping avoid a `HelloRetryRequest` and one extra network round trip.

Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum `X25519MLKEM768` hybrid key agreement.

To change this behavior, go to **SSL/TLS** > **Overview** > **Origin connection & post-quantum encryption**. Turn off **Automatic key exchange** to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.

**Compliance requirements** apply only to TLS 1.3 connections. The **Post-quantum hybrid** option requires hybrid post-quantum key agreements support on your origin server. The **Federal Information Processing Standards (FIPS)** option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.

For requirements, configuration options, and rollout details, refer to [Automatic key exchange to origins](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/#page","headline":"Faster and more secure TLS handshakes to your origins, automatically","description":"Cloudflare now automatically finds the most secure key agreement algorithm preferred by your origin servers, helping establish TLS 1.3 connections faster via Post-Quantum Encryption.","url":"https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/og.png?v=35a9109c16928f72","dateModified":"2026-07-21","datePublished":"2026-07-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
