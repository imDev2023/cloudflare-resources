---
description: Cloudflare reminds you to download your 2FA recovery keys
title: Automated reminders for backup codes
image: https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/og.png?v=cbf036c82e5d4e0b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 7, 2025

## Automated reminders for backup codes

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to **Profile** > **Security & Authentication** > **Backup codes**.

#### Sign-in security best practices

Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.

- Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.
- Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked
- Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.
- If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.
- If you use a custom email domain to sign in, [configure SSO ↗︎](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/).
- If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.
- If you manage a Cloudflare account for work:
  - Have at least two administrators in case one of them unexpectedly leaves your company
  - Use SCIM to automate permissions management for members in your Cloudflare account

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/#page","headline":"Automated reminders for backup codes","description":"Cloudflare reminds you to download your 2FA recovery keys","url":"https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/og.png?v=cbf036c82e5d4e0b","dateModified":"2025-10-07","datePublished":"2025-10-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
