---
description: Organizations with multiple Cloudflare accounts can now share a single identity provider configuration across accounts using IdP federation.
title: Share identity providers across accounts with IdP federation
image: https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/og.png?v=76f3be66f72c7a1b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 4, 2026

## Share identity providers across accounts with IdP federation

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/), which allows organizations to share a single identity provider across multiple Cloudflare accounts.

Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.

Key capabilities:

- **One IdP, many accounts** — Configure your IdP once and share it with all accounts in your organization.
- **Lifecycle management** — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.
- **Immutable recipient connections** — IdP connections in recipient accounts cannot be accidentally modified or deleted.

To get started, refer to [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/#page","headline":"Share identity providers across accounts with IdP federation","description":"Organizations with multiple Cloudflare accounts can now share a single identity provider configuration across accounts using IdP federation.","url":"https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/og.png?v=76f3be66f72c7a1b","dateModified":"2026-06-04","datePublished":"2026-06-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
