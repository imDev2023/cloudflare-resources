---
description: The Zone Overview dashboard now correctly classifies cached vs. uncached requests, aligning with the logic already used in HTTP Analytics.
title: Improved accuracy of cached request classification in analytics
image: https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/og.png?v=09fce1d9df81c950
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 18, 2025

## Improved accuracy of cached request classification in analytics

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.

Previously, requests were classified as "cached" based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.

The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in [HTTP Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/), so only requests genuinely served from cache are counted as cached.

**What changed:**

- **Zone Overview** — Cache ratios now reflect actual cache performance.
- **HTTP Analytics** — No change. HTTP Analytics already used the correct classification logic.
- **Historical data** — This fix applies to new requests only. Previously logged data is not retroactively updated.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/#page","headline":"Improved accuracy of cached request classification in analytics","description":"The Zone Overview dashboard now correctly classifies cached vs. uncached requests, aligning with the logic already used in HTTP Analytics.","url":"https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/og.png?v=09fce1d9df81c950","dateModified":"2025-12-18","datePublished":"2025-12-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
