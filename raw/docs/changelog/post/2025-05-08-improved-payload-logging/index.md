---
description: We have upgraded WAF Payload Logging to enhance rule diagnostics and usability.
title: Improved Payload Logging for WAF Managed Rules
image: https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/og.png?v=2c3544cb80fd2bd8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 8, 2025

## Improved Payload Logging for WAF Managed Rules

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:

- **Targeted logging**: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.
- **Visual highlighting**: Matched content is visually highlighted in the UI for faster identification.
- **Enhanced context**: Logs now include surrounding context to make diagnostics more effective.

![Log entry showing payload logging details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=751,format=webp/_astro/2025-05-payload-logging-update.1M29LjNm.png)

Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can [get started](https://developers.cloudflare.com/waf/managed-rules/payload-logging/).

**Note:** The structure of the `encrypted_matched_data` field in Logpush has changed from `Map<Field, Value>` to `Map<Field, {Before: bytes, Content: Value, After: bytes}>`. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/#page","headline":"Improved Payload Logging for WAF Managed Rules","description":"We have upgraded WAF Payload Logging to enhance rule diagnostics and usability.","url":"https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/og.png?v=2c3544cb80fd2bd8","dateModified":"2025-05-08","datePublished":"2025-05-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
