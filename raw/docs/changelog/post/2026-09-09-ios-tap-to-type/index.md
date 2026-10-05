---
description: Browser Isolation displays an inline tap-to-type prompt for iOS users.
title: Improved iOS tap-to-type experience for Browser Isolation
image: https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/og.png?v=44b2045e88aa9dd4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 9, 2026

## Improved iOS tap-to-type experience for Browser Isolation

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) has improved the tap-to-type experience for users on iOS devices.

Previously, Browser Isolation displayed a full-screen overlay with the message `tap to type` when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.

If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.

![Inline tap-to-type prompt over a focused text field in Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1320,height=605,format=webp/_astro/tap-to-type.UmUg_KNp.jpg)

iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.

For more information on why this interaction is required, refer to [iOS limitations](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/#ios).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/#page","headline":"Improved iOS tap-to-type experience for Browser Isolation","description":"Browser Isolation displays an inline tap-to-type prompt for iOS users.","url":"https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/og.png?v=44b2045e88aa9dd4","dateModified":"2026-09-09","datePublished":"2026-09-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
