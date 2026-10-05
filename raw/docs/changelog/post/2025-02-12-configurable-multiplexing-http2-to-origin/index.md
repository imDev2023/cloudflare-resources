---
description: Enterprise customers can now configure HTTP/2 multiplexing settings to optimize origin connections and improve cache performance.
title: Configurable multiplexing HTTP/2 to Origin
image: https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/og.png?v=ad64a2fce970a6d6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2025

## Configurable multiplexing HTTP/2 to Origin

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.

#### How it works

HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:

1. **Control concurrent streams**: Adjust the maximum number of concurrent streams per connection.
2. **Optimize connection reuse**: Fine-tune connection pooling behavior for your origin infrastructure.
3. **Reduce connection overhead**: Minimize the number of TCP connections required between Cloudflare and your origin.
4. **Improve cache performance**: Better connection management can enhance cache fetch efficiency.

#### Benefits

- **Customizable performance**: Tailor multiplexing settings to your origin's capabilities.
- **Reduced latency**: Fewer connection handshakes improve response times.
- **Lower origin load**: More efficient connection usage reduces server resource consumption.
- **Enhanced scalability**: Better connection management supports higher traffic volumes.

#### Get started

Enterprise customers can configure HTTP/2 multiplexing settings in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/) or through our [API](https://developers.cloudflare.com/api/).

Important consideration

This setting needs to be tuned carefully for your origin infrastructure. Setting the concurrent stream limit too high can negatively impact performance by saturating the shared TCP connection and overwhelming server processing capacity, leading to increased latency for individual requests.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/#page","headline":"Configurable multiplexing HTTP/2 to Origin","description":"Enterprise customers can now configure HTTP/2 multiplexing settings to optimize origin connections and improve cache performance.","url":"https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/og.png?v=ad64a2fce970a6d6","dateModified":"2025-02-12","datePublished":"2025-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
