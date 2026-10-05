---
description: View account-level analytics for your Images transformation usage.
title: View transformation analytics in Images
image: https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/og.png?v=50effa0a8399481c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 23, 2026

## View transformation analytics in Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now view account-level analytics for your Images transformation usage.

Go to **Images & Stream** > **Transformations** > **Analytics** to view sampled estimates of image transformation request traffic, including:

- Requests by source, split between URL-based transformations and Images binding transformations
- Top zones, transformation configurations, and origin hosts for URL-based requests
- Top Worker scripts for Images binding requests

Use these analytics to identify the zones, configurations, origins, and Workers generating the most image transformation requests.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/#page","headline":"View transformation analytics in Images","description":"View account-level analytics for your Images transformation usage.","url":"https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/og.png?v=50effa0a8399481c","dateModified":"2026-09-23","datePublished":"2026-09-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
