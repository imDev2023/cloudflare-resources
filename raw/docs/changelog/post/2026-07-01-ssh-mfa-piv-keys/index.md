---
description: Add hardware-backed multi-factor authentication to SSH connections through Access for Infrastructure.
title: Independent MFA for infrastructure applications
image: https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/og.png?v=e2e24737fcadb907
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Independent MFA for infrastructure applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.

With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, `root`) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.

#### Enrollment

Users enroll their YubiKey PIV key through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). For enrollment instructions and SSH client setup, refer to [Enroll a PIV key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps).

#### Configuration

For setup instructions, refer to [Enforce MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/#page","headline":"Independent MFA for infrastructure applications","description":"Add hardware-backed multi-factor authentication to SSH connections through Access for Infrastructure.","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/og.png?v=e2e24737fcadb907","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
