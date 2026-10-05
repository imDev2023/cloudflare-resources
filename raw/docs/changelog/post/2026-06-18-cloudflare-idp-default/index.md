---
description: New Zero Trust organizations get the Cloudflare identity provider as their default login method instead of one-time PIN.
title: Cloudflare identity provider is now the default for new accounts
image: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/og.png?v=22f269dcdc23605d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 18, 2026

## Cloudflare identity provider is now the default for new accounts

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you create a new Zero Trust organization, Cloudflare now adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method. Previously, new organizations started with [one-time PIN (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/).

With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) whenever you need to.

This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/#page","headline":"Cloudflare identity provider is now the default for new accounts","description":"New Zero Trust organizations get the Cloudflare identity provider as their default login method instead of one-time PIN.","url":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/og.png?v=22f269dcdc23605d","dateModified":"2026-06-18","datePublished":"2026-06-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
