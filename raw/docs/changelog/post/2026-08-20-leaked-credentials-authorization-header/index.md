---
description: Leaked credentials detection can now detect Basic Authentication credentials sent in the Authorization header.
title: Leaked credentials detection now scans Authorization headers
image: https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/og.png?v=d225854f29560dea
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 20, 2026

## Leaked credentials detection now scans Authorization headers

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) now scans the `Authorization` request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default.

This new default scan location decodes the `Authorization: Basic <credentials>` header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations. Matches populate the existing [leaked credentials fields](https://developers.cloudflare.com/waf/detections/leaked-credentials/#leaked-credentials-fields), such as `cf.waf.credential_check.password_leaked`, and trigger the [`Exposed-Credential-Check` managed transform header](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header) if configured, so you can reuse existing [custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) without changes.

This change was applied automatically for zones with leaked credentials detection enabled. No configuration changes are required.

For more information, refer to [Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/#page","headline":"Leaked credentials detection now scans Authorization headers","description":"Leaked credentials detection can now detect Basic Authentication credentials sent in the Authorization header.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/og.png?v=d225854f29560dea","dateModified":"2026-08-20","datePublished":"2026-08-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
