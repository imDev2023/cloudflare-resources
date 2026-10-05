---
description: "Stream has added support for DVR for Live broadcasts. In other words, for those who didn’t witness the magic of TiVo, you can now allow your viewers to rewind and replay Live content during broadcasts.\n"
title: "Rewind, Replay, Resume: Introducing DVR for Stream Live"
image: https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/og.png?v=7d87638f6088adec
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 14, 2025

## Rewind, Replay, Resume: Introducing DVR for Stream Live

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Previously, all viewers watched "the live edge," or the latest content of the broadcast, synchronously. If a viewer paused for more than a few seconds, the player would automatically "catch up" when playback started again. Seeking through the broadcast was only available once the recording was available after it concluded.

Starting today, customers can make a small adjustment to the player embed or manifest URL to enable the DVR experience for their viewers. By offering this feature as an opt-in adjustment, our customers are empowered to pick the best experiences for their applications.

When building a player embed code or manifest URL, just add `dvrEnabled=true` as a query parameter. There are some things to be aware of when using this option. For more information, refer to [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/#page","headline":"Rewind, Replay, Resume: Introducing DVR for Stream Live","description":"Stream has added support for DVR for Live broadcasts. In other words, for those who didn’t witness the magic of TiVo, you can now allow your viewers to rewind and replay Live content during broadcasts.","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/og.png?v=7d87638f6088adec","dateModified":"2025-02-14","datePublished":"2025-02-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
