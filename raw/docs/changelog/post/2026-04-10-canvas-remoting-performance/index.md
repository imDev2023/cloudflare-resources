---
description: Browser Isolation now renders Canvas applications using vector commands instead of bitmaps, reducing bandwidth by 10x.
title: Canvas Remoting optimizes performance for productivity applications
image: https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/og.png?v=008e73362e7840b1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 10, 2026

## Canvas Remoting optimizes performance for productivity applications

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Remote Browser Isolation now supports **Canvas Remoting**, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.

#### Key improvements

- **10x bandwidth reduction:** Microsoft Word and other Office apps use 90% less bandwidth
- **Smooth performance:** Google Sheets maintains consistent 30fps rendering
- **Responsive terminals:** Web-based development environments and AI notebooks work in real-time
- **Zero configuration:** Enabled by default for all Browser Isolation customers

#### How it works

Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:

1. Captures Canvas draw commands at the source
2. Converts them to lightweight vector instructions
3. Renders Canvas content on the client

This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.

#### Managing Canvas Remoting

To temporarily disable for troubleshooting:

- Right-click the isolated webpage background
- Select **Disable Canvas Remoting**
- Re-enable the same way by selecting **Enable Canvas Remoting**

#### Limitations

Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to [Canvas Remoting](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/canvas-remoting/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/#page","headline":"Canvas Remoting optimizes performance for productivity applications","description":"Browser Isolation now renders Canvas applications using vector commands instead of bitmaps, reducing bandwidth by 10x.","url":"https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/og.png?v=008e73362e7840b1","dateModified":"2026-04-10","datePublished":"2026-04-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
