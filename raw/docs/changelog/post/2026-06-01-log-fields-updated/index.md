---
description: The Turnstile Events Logpush dataset is now available in Cloudflare Logs.
title: New Turnstile Events Logpush dataset in Cloudflare Logs
image: https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/og.png?v=d44d5b1303909b7c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 1, 2026

## New Turnstile Events Logpush dataset in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

- **Turnstile Events**: A new dataset with fields including `ASN`, `Action`, `BrowserMajor`, `BrowserName`, `ClientIP`, `CountryCode`, `EventType`, `Hostname`, `OSMajor`, `OSName`, `Sitekey`, `Timestamp`, and `UserAgent`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/#page","headline":"New Turnstile Events Logpush dataset in Cloudflare Logs","description":"The Turnstile Events Logpush dataset is now available in Cloudflare Logs.","url":"https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/og.png?v=d44d5b1303909b7c","dateModified":"2026-06-01","datePublished":"2026-06-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
