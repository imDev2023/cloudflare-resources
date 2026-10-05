---
description: Configure Cloudflare Access to request fresh identity provider authentication for each SAML login.
title: Require fresh authentication for SAML identity providers
image: https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/og.png?v=511558421a4c57c0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 14, 2026

## Require fresh authentication for SAML identity providers

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on **Require reauthentication** in the Cloudflare dashboard, or set `force_authn` to `true` through the API. Access will then set `ForceAuthn` to `true` in signed and unsigned SAML authentication requests.

This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is `false`.

For configuration details, refer to [Require fresh authentication at the identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/#page","headline":"Require fresh authentication for SAML identity providers","description":"Configure Cloudflare Access to request fresh identity provider authentication for each SAML login.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/og.png?v=511558421a4c57c0","dateModified":"2026-09-14","datePublished":"2026-09-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
