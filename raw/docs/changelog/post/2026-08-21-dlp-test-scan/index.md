---
description: Test scan lets you test text, files, and HAR data against DLP profiles and inspect match details — no Gateway traffic required.
title: Test Data Loss Prevention profiles without sending traffic through Gateway
image: https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/og.png?v=912890907b8b851f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2026

## Test Data Loss Prevention profiles without sending traffic through Gateway

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Test scan** lets you check how [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.

![Test scan results showing matched profiles, detection entries, and match context](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=587,format=webp/_astro/dlp-test-scan.Dm6EgN6x.gif)

Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.

Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your [Zero Trust plan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

For more details, refer to the [Test scan documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/test-scan/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/#page","headline":"Test Data Loss Prevention profiles without sending traffic through Gateway","description":"Test scan lets you test text, files, and HAR data against DLP profiles and inspect match details — no Gateway traffic required.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/og.png?v=912890907b8b851f","dateModified":"2026-08-21","datePublished":"2026-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
