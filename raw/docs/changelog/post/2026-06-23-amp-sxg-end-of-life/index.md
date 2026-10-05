---
description: Cloudflare AMP/SXG support has reached end of life.
title: Cloudflare AMP/SXG is now end of life.
image: https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/og.png?v=ea9845c694beb1bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 23, 2026

## Cloudflare AMP/SXG is now end of life.

[Speed](https://developers.cloudflare.com/speed/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Accelerated Mobile Pages (AMP) and Signed Exchanges (SXG) support has reached end of life. The features have been disabled since October 2025, so customers who had them configured should see no change to their traffic.

Customers will no longer be able to configure AMP/SXG through API or rulesets. The Zone API will start throwing errors. Rulesets with the SXG configuration will fail to save until SXG has been removed.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/#page","headline":"Cloudflare AMP/SXG is now end of life.","description":"Cloudflare AMP/SXG support has reached end of life.","url":"https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/og.png?v=ea9845c694beb1bb","dateModified":"2026-06-23","datePublished":"2026-06-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
