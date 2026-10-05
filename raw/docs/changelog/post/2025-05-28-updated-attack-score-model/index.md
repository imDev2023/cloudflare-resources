---
description: An updated attack score model for Cloudflare WAF to reduce false positives.
title: Updated attack score model
image: https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/og.png?v=4a0f2c978c0d1daf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2025

## Updated attack score model

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have deployed an updated attack score model focused on enhancing the detection of multiple false positives (FPs).

As a result of this improvement, some changes in observed attack scores are expected.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/#page","headline":"Updated attack score model","description":"An updated attack score model for Cloudflare WAF to reduce false positives.","url":"https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/og.png?v=4a0f2c978c0d1daf","dateModified":"2025-05-28","datePublished":"2025-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
