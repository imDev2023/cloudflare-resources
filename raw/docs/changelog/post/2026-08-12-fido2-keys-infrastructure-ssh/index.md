---
description: Enforce FIDO2 hardware key authentication on SSH connections to infrastructure applications.
title: Independent MFA supports FIDO2 for infrastructure applications
image: https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/og.png?v=e519f0a7c1c354a1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 12, 2026

## Independent MFA supports FIDO2 for infrastructure applications

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/#page","headline":"Independent MFA supports FIDO2 for infrastructure applications","description":"Enforce FIDO2 hardware key authentication on SSH connections to infrastructure applications.","url":"https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/og.png?v=e519f0a7c1c354a1","dateModified":"2026-08-12","datePublished":"2026-08-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
