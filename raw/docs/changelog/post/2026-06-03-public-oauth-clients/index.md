---
description: Developers can now create self-managed OAuth clients that integrate with Cloudflare.
title: Introducing self-managed OAuth clients
image: https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/og.png?v=60ea2aa30f0166eb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 3, 2026

## Introducing self-managed OAuth clients

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.

OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.

#### What is new

Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.

#### Create an application

To create an application, go to **Manage account** > **OAuth clients** in your account on the Cloudflare dashboard.

[Go to **OAuth clients** ↗](https://dash.cloudflare.com/?to=/:account/oauth-clients)

#### Select limited scopes

If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.

Users can review the requested scopes before they consent.

#### Apps for both private and public use

Applications start with `private` visibility. Private applications can only be used by members of the account where the application was created.

To make an application available to any Cloudflare user, complete the prerequisites for `public` visibility.

For more information, refer to [client visibility](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients).

#### Client domain verification

Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.

After verification, users see a verified badge on the consent page.

For more information, refer to [domain verification](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification).

#### Learn more

For more information, refer to [OAuth clients](https://developers.cloudflare.com/fundamentals/oauth/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/#page","headline":"Introducing self-managed OAuth clients","description":"Developers can now create self-managed OAuth clients that integrate with Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/og.png?v=60ea2aa30f0166eb","dateModified":"2026-06-03","datePublished":"2026-06-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
