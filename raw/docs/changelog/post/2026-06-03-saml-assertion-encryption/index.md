---
description: Encrypt SAML assertions from your identity provider to Cloudflare Access for enhanced security.
title: SAML assertion encryption for identity providers
image: https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/og.png?v=0cbf0c697d6c6df1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 3, 2026

## SAML assertion encryption for identity providers

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.

Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.

![SAML encryption toggle in the identity provider configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=344,format=webp/_astro/saml-encryption.J5jmiYv8.png)

SAML encryption includes built-in certificate lifecycle management:

- **Automatic certificate generation**: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.
- **Certificate rotation**: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.
- **PEM export**: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.

To get started, refer to [Encrypt SAML assertions](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/#page","headline":"SAML assertion encryption for identity providers","description":"Encrypt SAML assertions from your identity provider to Cloudflare Access for enhanced security.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/og.png?v=0cbf0c697d6c6df1","dateModified":"2026-06-03","datePublished":"2026-06-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
