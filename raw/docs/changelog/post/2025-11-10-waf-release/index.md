---
description: Cloudflare WAF managed rulesets 2025-11-10 release
title: WAF Release - 2025-11-10
image: https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/og.png?v=6038e45848b763fd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 10, 2025

## WAF Release - 2025-11-10

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.

**Key Findings**

- These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.

**Impact**

Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...606285e6 | N/A | Generic Rules - Prototype Pollution - URI | Log | Disabled | This is a new detection |
| Cloudflare Managed Ruleset | ...4f59ff26 | N/A | Generic Rules - Prototype Pollution - Body | Log | Disabled | This is a new detection |
| Cloudflare Managed Ruleset | ...7efbeb39 | N/A | Generic Rules - Prototype Pollution - Header - Form | Log | Disabled | This is a new detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/#page","headline":"WAF Release - 2025-11-10","description":"Cloudflare WAF managed rulesets 2025-11-10 release","url":"https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-10-waf-release/og.png?v=6038e45848b763fd","dateModified":"2025-11-10","datePublished":"2025-11-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
