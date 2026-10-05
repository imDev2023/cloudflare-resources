---
description: Cloudflare WAF managed rulesets 2026-07-17 emergency release
title: WAF Release - 2026-07-17 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/og.png?v=627c0889ad98735e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 17, 2026

## WAF Release - 2026-07-17 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.

**Key Findings**

- Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.
- Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...550664b6 | N/A | Generic Rules - Unauthenticated RCE | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...ed933fcc | N/A | Generic Rules - SQLi | N/A | Block | This is a new detection. |
| Cloudflare Free Ruleset | ...b5ec246a | N/A | Generic Rules - Unauthenticated RCE | N/A | Block | This is a new detection. |
| Cloudflare Free Ruleset | ...33697a1a | N/A | Generic Rules - SQLi | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/#page","headline":"WAF Release - 2026-07-17 - Emergency","description":"Cloudflare WAF managed rulesets 2026-07-17 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/og.png?v=627c0889ad98735e","dateModified":"2026-07-17","datePublished":"2026-07-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
