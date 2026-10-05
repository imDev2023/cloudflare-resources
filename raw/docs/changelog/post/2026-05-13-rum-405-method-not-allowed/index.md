---
description: The /cdn-cgi/rum beacon endpoint now returns 405 Method Not Allowed instead of 404 when called with an unsupported HTTP method.
title: /cdn-cgi/rum endpoint now returns 405 for non-POST requests
image: https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/og.png?v=e6781c1ebe05e91c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 13, 2026

## /cdn-cgi/rum endpoint now returns 405 for non-POST requests

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `/cdn-cgi/rum` beacon endpoint now returns `405 Method Not Allowed` for non-POST requests instead of `404 Not Found`. The response includes an `Allow: POST, OPTIONS` header per [RFC 9110 §15.5.6 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6).

Previously, sending a `GET` or other non-POST request to this endpoint returned a `404`, which was misleading because it suggested the endpoint did not exist. The new `405` response clearly indicates that the endpoint exists but only accepts `POST` requests.

The Web Analytics beacon (`beacon.min.js`) already uses `POST` for all metric submissions, so this change does not affect normal beacon operation. `OPTIONS` requests for CORS preflight continue to work as before.

For more information, refer to the [Web Analytics FAQ](https://developers.cloudflare.com/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/#page","headline":"/cdn-cgi/rum endpoint now returns 405 for non-POST requests","description":"The /cdn-cgi/rum beacon endpoint now returns 405 Method Not Allowed instead of 404 when called with an unsupported HTTP method.","url":"https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/og.png?v=e6781c1ebe05e91c","dateModified":"2026-05-13","datePublished":"2026-05-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
