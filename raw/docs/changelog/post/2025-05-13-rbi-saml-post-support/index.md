---
description: Enable secure access to SSO-enabled applications in the remote browser.
title: SAML HTTP-POST bindings support for RBI
image: https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/og.png?v=3e594f10075b4849
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 13, 2025

## SAML HTTP-POST bindings support for RBI

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused `405` errors during login and improves compatibility with multi-factor authentication (MFA) flows.

With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to [set up Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/#page","headline":"SAML HTTP-POST bindings support for RBI","description":"Enable secure access to SSO-enabled applications in the remote browser.","url":"https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/og.png?v=3e594f10075b4849","dateModified":"2025-05-13","datePublished":"2025-05-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
