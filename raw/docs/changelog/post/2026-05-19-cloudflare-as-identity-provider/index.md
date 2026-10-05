---
description: Use Cloudflare as an identity provider in Access and build policies based on Cloudflare account membership.
title: Cloudflare as identity provider and account membership selector
image: https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/og.png?v=8013053fe640ad38
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2026

## Cloudflare as identity provider and account membership selector

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports using Cloudflare itself as an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/). If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.

Cloudflare is now the **default identity provider for all newly created Zero Trust accounts**, replacing One-time PIN.

This also enables two new capabilities:

- **Cloudflare Account Member selector** — A new [policy selector](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors) that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.
- **Restrict to account members** — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.

To get started, add Cloudflare as an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) in your Zero Trust settings.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/#page","headline":"Cloudflare as identity provider and account membership selector","description":"Use Cloudflare as an identity provider in Access and build policies based on Cloudflare account membership.","url":"https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/og.png?v=8013053fe640ad38","dateModified":"2026-05-19","datePublished":"2026-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
