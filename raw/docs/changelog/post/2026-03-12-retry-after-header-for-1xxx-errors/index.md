---
description: Cloudflare-generated 1xxx error responses now include a standard Retry-After HTTP header when the error is retryable, letting HTTP clients honour the server-suggested wait time directly from response headers.
title: Retry-After HTTP header for retryable 1xxx errors
image: https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/og.png?v=d42e194e240d363f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 12, 2026

## Retry-After HTTP header for retryable 1xxx errors

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare-generated 1xxx error responses now include a standard `Retry-After` HTTP header when the error is retryable. Agents and HTTP clients can read the recommended wait time from response headers alone — no body parsing required.

#### Changes

Seven retryable error codes now emit `Retry-After`:

| Error code | Retry-After (seconds) | Error name |
| --- | --- | --- |
| 1004 | 120 | DNS resolution error |
| 1005 | 120 | Banned zone |
| 1015 | 30 | Rate limited |
| 1033 | 120 | Argo Tunnel error |
| 1038 | 60 | HTTP headers limit exceeded |
| 1200 | 60 | Cache connection limit |
| 1205 | 5 | Too many redirects |

The header value matches the existing `retry_after` body field in JSON and Markdown responses.

If a WAF rate limiting rule has already set a dynamic `Retry-After` value on the response, that value takes precedence.

#### Availability

Available for all zones on all plans.

#### Verify

Check for the header on any retryable error:

```bash
curl -s --compressed -D - -o /dev/null -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | grep -i retry-after
```

References:

- [RFC 9110 section 10.2.3 - Retry-After ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-10.2.3)
- [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/#page","headline":"Retry-After HTTP header for retryable 1xxx errors","description":"Cloudflare-generated 1xxx error responses now include a standard Retry-After HTTP header when the error is retryable, letting HTTP clients honour the server-suggested wait time directly from response headers.","url":"https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/og.png?v=d42e194e240d363f","dateModified":"2026-03-12","datePublished":"2026-03-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
