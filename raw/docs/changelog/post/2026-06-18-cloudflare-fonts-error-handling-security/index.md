---
description: Cloudflare Fonts now passes `/cf-fonts` requests through to the origin on errors and includes additional input validation for security.
title: Cloudflare Fonts error handling and security improvements
image: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/og.png?v=a564406b279a0da7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 18, 2026

## Cloudflare Fonts error handling and security improvements

[Speed](https://developers.cloudflare.com/speed/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Fonts now forwards `/cf-fonts` requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/#page","headline":"Cloudflare Fonts error handling and security improvements","description":"Cloudflare Fonts now passes /cf-fonts requests through to the origin on errors and includes additional input validation for security.","url":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/og.png?v=a564406b279a0da7","dateModified":"2026-06-18","datePublished":"2026-06-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
