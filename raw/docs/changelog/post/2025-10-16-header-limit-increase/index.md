---
description: Cloudflare's CDN and Workers platform now support up to 128 KB for request and response headers
title: Increased HTTP header size limit to 128 KB
image: https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/og.png?v=b12e91d64db6e3f2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 16, 2025

## Increased HTTP header size limit to 128 KB

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### CDN now supports 128 KB request and response headers 🚀

We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to **128 KB** for both **request and response headers**.

Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with `HTTP 413` (Request Header Fields Too Large) errors.

---

#### What's new?

- **Support for large headers:** You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.
- **Reduces `413` and `520` HTTP errors:** This change drastically reduces the likelihood of customers encountering `HTTP 413` errors from large request headers or `HTTP 520` errors caused by oversized response headers, improving the overall reliability of your web applications.
- **Enhanced functionality:** This is especially beneficial for applications that rely on:
  - A large number of cookies.
  - Large Content-Security-Policy (CSP) response headers.
  - Advanced use cases with Cloudflare Workers that generate large response headers.

This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.

---

To learn more and get started, refer to the [Cloudflare Fundamentals documentation](https://developers.cloudflare.com/fundamentals/reference/connection-limits/#request-limits).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/#page","headline":"Increased HTTP header size limit to 128 KB","description":"Cloudflare's CDN and Workers platform now support up to 128 KB for request and response headers","url":"https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/og.png?v=b12e91d64db6e3f2","dateModified":"2025-10-16","datePublished":"2025-10-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
