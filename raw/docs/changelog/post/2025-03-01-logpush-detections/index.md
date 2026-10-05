---
description: Send detection logs to an endpoint of your choice with Cloudflare Logpush.
title: Use Logpush for Email security detections
image: https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/og.png?v=5cb284ced72be5e6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 1, 2025

## Use Logpush for Email security detections

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select **Email security alerts** as the dataset.

![logpush-detections](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=927,height=688,format=webp/_astro/Logpush-Detections.Dc5tHta3.png)

For more information, refer to [Enable detection logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs).

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/#page","headline":"Use Logpush for Email security detections","description":"Send detection logs to an endpoint of your choice with Cloudflare Logpush.","url":"https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/og.png?v=5cb284ced72be5e6","dateModified":"2025-03-01","datePublished":"2025-03-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
