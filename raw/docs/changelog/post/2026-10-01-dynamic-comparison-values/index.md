---
description: Compare fields and function results in Rules expressions using equality and ordering operators.
title: Compare dynamic values in Rules expressions
image: https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/og.png?v=05226bd7d90a6eef
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Compare dynamic values in Rules expressions

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:

```txt
http.request.uri.path ne raw.http.request.uri.path
```

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/#page","headline":"Compare dynamic values in Rules expressions","description":"Compare fields and function results in Rules expressions using equality and ordering operators.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/og.png?v=05226bd7d90a6eef","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
