---
description: Configure millisecond or nanosecond timestamp precision for Logpush jobs.
title: Logpush — More granular timestamps
image: https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/og.png?v=9437153c22126694
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 25, 2026

## Logpush — More granular timestamps

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

- `rfc3339ms` — `2024-02-17T23:52:01.123Z`
- `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`

Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/#page","headline":"Logpush — More granular timestamps","description":"Configure millisecond or nanosecond timestamp precision for Logpush jobs.","url":"https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/og.png?v=9437153c22126694","dateModified":"2026-03-25","datePublished":"2026-03-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
