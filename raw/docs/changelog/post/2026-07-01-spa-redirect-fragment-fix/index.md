---
description: Access no longer over-encodes URL fragment characters, fixing post-login redirects for single-page applications with fragment-based routing.
title: Fix redirect URL fragment encoding for single-page applications
image: https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/og.png?v=60c7048d7e9e09ba
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Fix redirect URL fragment encoding for single-page applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Access now correctly preserves URL fragment characters (`/`, `?`, `=`, `&`, `;`) when redirecting users back to an application after login. Previously, these characters were encoded with `encodeURIComponent`, which mangled fragment-based routes used by single-page applications (SPAs).

For example, an SPA URL like `https://app.example.com/#/dashboard?tab=settings&view=advanced` would previously redirect to a broken URL after login. This is now handled correctly.

If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/#page","headline":"Fix redirect URL fragment encoding for single-page applications","description":"Access no longer over-encodes URL fragment characters, fixing post-login redirects for single-page applications with fragment-based routing.","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/og.png?v=60c7048d7e9e09ba","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
