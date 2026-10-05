---
description: Configure request header and response headers values can log eiterh raw or transformed value
title: Custom fields raw and transformed values support
image: https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/og.png?v=e62a749846a64697
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 18, 2025

## Custom fields raw and transformed values support

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom Fields now support logging both **raw and transformed values** for request and response headers in the HTTP requests dataset.

These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.

By default:

- Request headers are logged as raw values
- Response headers are logged as transformed values

These defaults can be overridden to suit your logging needs.

Note

Transformed and raw values for request and response headers are available **only via the API** and cannot be set through the UI.

For more information refer to [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/) documentation

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/#page","headline":"Custom fields raw and transformed values support","description":"Configure request header and response headers values can log eiterh raw or transformed value","url":"https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/og.png?v=e62a749846a64697","dateModified":"2025-04-18","datePublished":"2025-04-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
