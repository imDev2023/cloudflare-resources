---
description: DLP now uses a streaming ZIP handler that processes archive contents as data arrives, removing previous file size limitations for content within ZIP files.
title: Streaming ZIP file scanning removes per-file size limits
image: https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/og.png?v=644c35c3bb3a576f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2026

## Streaming ZIP file scanning removes per-file size limits

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.

Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.

This improvement is automatic — no configuration changes are required.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/#page","headline":"Streaming ZIP file scanning removes per-file size limits","description":"DLP now uses a streaming ZIP handler that processes archive contents as data arrives, removing previous file size limitations for content within ZIP files.","url":"https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/og.png?v=644c35c3bb3a576f","dateModified":"2026-03-26","datePublished":"2026-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
