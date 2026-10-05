---
description: "Media Transformations now supports `audio` mode, which extracts audio from a video.\n"
title: Audio mode for Media Transformations
image: https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/og.png?v=6eaed03313e2e0f8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 22, 2025

## Audio mode for Media Transformations

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We now support `audio` mode! Use this feature to extract audio from a source video, outputting an M4A file to use in downstream workflows like [AI inference](https://developers.cloudflare.com/workers-ai/), content moderation, or transcription.

For example,

*Example URLtext*

```text
https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>
https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/<input video with diction>
```

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/#page","headline":"Audio mode for Media Transformations","description":"Media Transformations now supports audio mode, which extracts audio from a video.","url":"https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/og.png?v=6eaed03313e2e0f8","dateModified":"2025-07-22","datePublished":"2025-07-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
