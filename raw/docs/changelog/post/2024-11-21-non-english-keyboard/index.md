---
description: Introduced support for non-English keyboard configurations in the remote browser, enhancing the global user experience.
title: Improved non-English keyboard support
image: https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/og.png?v=dff0cea1eaa80954
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 21, 2024

## Improved non-English keyboard support

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/#page","headline":"Improved non-English keyboard support","description":"Introduced support for non-English keyboard configurations in the remote browser, enhancing the global user experience.","url":"https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/og.png?v=dff0cea1eaa80954","dateModified":"2024-11-21","datePublished":"2024-11-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
