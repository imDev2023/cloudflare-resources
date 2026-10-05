---
description: Confidence intervals are now supported in the GraphQL Analytics API to show statistical ranges for sampled data results
title: New Confidence Intervals in GraphQL Analytics API
image: https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/og.png?v=d3e2138ae8d4fcc3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2025

## New Confidence Intervals in GraphQL Analytics API

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The GraphQL Analytics API now supports confidence intervals for `sum` and `count` fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.

- **Supported datasets**: Adaptive (sampled) datasets only.
- **Supported fields**: All `sum` and `count` fields.
- **Usage**: The confidence `level` must be provided as a decimal between 0 and 1 (e.g. `0.90`, `0.95`, `0.99`).
- **Default**: If no confidence level is specified, no intervals are returned.

For examples and more details, see the [GraphQL Analytics API documentation](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/#page","headline":"New Confidence Intervals in GraphQL Analytics API","description":"Confidence intervals are now supported in the GraphQL Analytics API to show statistical ranges for sampled data results","url":"https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/og.png?v=d3e2138ae8d4fcc3","dateModified":"2025-10-01","datePublished":"2025-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
