---
description: DNSSEC-backed TLSA records now available on regional MX hostnames for verified encrypted email delivery
title: DANE Support for MX Deployments
image: https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/og.png?v=735a7c19747e9951
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 6, 2026

## DANE Support for MX Deployments

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.

- Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.
- DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/#page","headline":"DANE Support for MX Deployments","description":"DNSSEC-backed TLSA records now available on regional MX hostnames for verified encrypted email delivery","url":"https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/og.png?v=735a7c19747e9951","dateModified":"2026-04-06","datePublished":"2026-04-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
