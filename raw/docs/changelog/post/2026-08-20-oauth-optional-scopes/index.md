---
description: OAuth clients can now mark scopes as required or optional
title: Optional OAuth scopes
image: https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/og.png?v=b9bd9c01cb75b4db
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## Optional OAuth scopes

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're announcing the GA of Optional OAuth Scopes.

OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .

#### What's New

**Optional Scopes:** OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.

**Scope Selection:** On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.

**Templates:** The consent screen now includes **Read Only** and **Full Access** templates to make scope selection faster and easier.

**Search:** Users can now search scopes in the consent screen.

Learn how to [select client scopes](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#select-scopes) and [edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/#page","headline":"Optional OAuth scopes","description":"OAuth clients can now mark scopes as required or optional","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/og.png?v=b9bd9c01cb75b4db","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
