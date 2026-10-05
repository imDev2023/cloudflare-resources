---
description: Cloudflare's cache now runs on Pingora, our Rust-based proxy framework, delivering lower latency, improved RFC compliance, and a foundation for future caching capabilities.
title: Pingora now powers Cloudflare's cache
image: https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/og.png?v=63bd8cc76ed80175
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 4, 2026

## Pingora now powers Cloudflare's cache

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's cache now runs on a new proxy built on [Pingora ↗︎](https://github.com/cloudflare/pingora), the Rust-based framework that already serves a significant portion of Cloudflare's network traffic. The new proxy is faster, more memory-safe, and designed to evolve our cache architecture. It delivers immediate performance improvements and enables new caching capabilities.

#### What this brings

- **Lower latency**: The new proxy reduces per-request overhead through improved connection reuse.
- **Reduced cache MISSes**: Enhanced cache retention improves origin offload.
- **Better RFC compliance**: Caching behavior more closely follows HTTP caching standards.
- **Foundation for future features**: The new architecture enables upcoming improvements to cache functionality and efficiency.

#### New features

- **Asynchronous `stale-while-revalidate`**: Every request returns stale content immediately while revalidation happens in the background, instead of the first request after expiry blocking on the origin. Refer to the [asynchronous `stale-while-revalidate` changelog](https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/) for details.
- **Unbuffered bypass by default**: Responses that bypass cache are streamed directly to the client without buffering, reducing time-to-first-byte for uncacheable content.

#### Behavioral changes

The new architecture introduces the following behavioral changes to improve RFC compliance and correctness:

- **`Vary: *` results in cache bypass**: According to [RFC 9110 Section 12.5.5 ↗︎](https://httpwg.org/specs/rfc9110.html#field.vary), a `Vary` header value of `*` indicates the response varies on factors beyond request headers and must not be served from cache. Cloudflare now bypasses cache for these responses instead of storing them.
- **`Set-Cookie` stripped on MISS and EXPIRED**: For cacheable assets, `Set-Cookie` is now stripped on MISS and EXPIRED responses, not only on HITs.
- **Floating-point TTL values**: Floating-point time-to-live values (for example, `max-age=1.5`) are rounded down to the nearest integer instead of being rejected as invalid.

#### What's next

A deeper look at the new cache proxy is coming soon to the [Cloudflare blog ↗︎](https://blog.cloudflare.com/). For background on the underlying framework, read:

- [Open sourcing Pingora: our Rust framework for building programmable network services ↗︎](https://blog.cloudflare.com/pingora-open-source/)
- [How we built Pingora, the proxy that connects Cloudflare to the Internet ↗︎](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/#page","headline":"Pingora now powers Cloudflare's cache","description":"Cloudflare's cache now runs on Pingora, our Rust-based proxy framework, delivering lower latency, improved RFC compliance, and a foundation for future caching capabilities.","url":"https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/og.png?v=63bd8cc76ed80175","dateModified":"2026-05-04","datePublished":"2026-05-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
