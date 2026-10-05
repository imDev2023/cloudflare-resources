---
description: Cloudflare now provides more accurate visibility into client request cancellations over HTTP/3, improving observability and reducing unnecessary origin load
title: Enhanced HTTP/3 request cancellation visibility
image: https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/og.png?v=bcc2467ce029b11e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 19, 2026

## Enhanced HTTP/3 request cancellation visibility

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Enhanced HTTP/3 request cancellation visibility

Cloudflare now provides more accurate visibility into HTTP/3 client request cancellations, giving you better insight into real client behavior and reducing unnecessary load on your origins.

Previously, when an HTTP/3 client cancelled a request, the cancellation was not always actioned immediately. This meant requests could continue through the CDN — potentially all the way to your origin — even after the client had abandoned them. In these cases, logs would show the upstream response status (such as `200` or a timeout-related code) rather than reflecting the client cancellation.

Now, Cloudflare terminates cancelled HTTP/3 requests immediately and accurately logs them with a `499` status code.

---

#### Better observability for client behavior

When HTTP/3 clients cancel requests, Cloudflare now immediately reflects this in your logs with a `499` status code. This gives you:

- **More accurate traffic analysis**: Understand exactly when and how often clients cancel requests.
- **Clearer debugging**: Distinguish between true errors and intentional client cancellations.
- **Better availability metrics**: Separate client-initiated cancellations from server-side issues.

---

#### Reduced origin load

Cloudflare now terminates cancelled requests faster, which means:

- **Less wasted compute**: Your origin no longer processes requests that clients have already abandoned.
- **Lower bandwidth usage**: Responses are no longer generated and transmitted for cancelled requests.
- **Improved efficiency**: Resources are freed up to handle active requests.

---

#### What to expect in your logs

You may notice an increase in `499` status codes for HTTP/3 traffic. For HTTP/3, a `499` indicates the client [cancelled the request stream ↗︎](https://datatracker.ietf.org/doc/html/rfc9114#section-4.1.1) before receiving a complete response — the underlying connection may remain open. This is a normal part of web traffic.

**Tip**: If you use `499` codes in availability calculations, consider whether client-initiated cancellations should be excluded from error rates. These typically represent normal user behavior — such as closing a browser, navigating away from a page, mobile network drops, or cancelling a download — rather than service issues.

---

For more information, refer to [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/#page","headline":"Enhanced HTTP/3 request cancellation visibility","description":"Cloudflare now provides more accurate visibility into client request cancellations over HTTP/3, improving observability and reducing unnecessary origin load","url":"https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/og.png?v=bcc2467ce029b11e","dateModified":"2026-01-19","datePublished":"2026-01-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
