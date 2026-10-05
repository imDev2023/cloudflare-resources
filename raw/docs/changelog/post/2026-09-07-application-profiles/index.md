---
description: Learn expected request structures, analyze deviations, and selectively block non-conforming traffic.
title: Enforce positive security with Application Profiles
image: https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/og.png?v=d7cf74a0982588fd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 7, 2026

## Enforce positive security with Application Profiles

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Application Profiles add a positive-security layer to Cloudflare WAF. Instead of looking only for requests that resemble known attacks, Application Profiles learn what valid requests to your application look like and identify traffic that deviates from the expected structure.

The first available profile type, Schema Profiles, can learn path variables, query parameters, headers, cookies, JSON bodies, and form-encoded bodies. Profiles model field types and constraints such as numeric ranges, string lengths, and character classes. After a profile becomes available, an always-on detection classifies requests as conforming or non-conforming without blocking traffic.

Use **Profile Analysis** in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to review conformance trends and sampled violation details before enforcing a profile. When you are ready to mitigate traffic, use a [Custom Rule](https://developers.cloudflare.com/waf/custom-rules/) to scope enforcement by hostname, path, operation, or other security signals such as Attack Score.

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is also opening a closed beta to invited Enterprise customers without API Security. Contact your Cloudflare account team to express interest.

For more information, refer to [Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/#page","headline":"Enforce positive security with Application Profiles","description":"Learn expected request structures, analyze deviations, and selectively block non-conforming traffic.","url":"https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/og.png?v=d7cf74a0982588fd","dateModified":"2026-09-07","datePublished":"2026-09-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
