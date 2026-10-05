---
description: Cloudflare WAF managed rulesets 2026-09-15 release
title: WAF Release - 2026-09-15
image: https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/og.png?v=7a1ca4801e3099f6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 15, 2026

## WAF Release - 2026-09-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...ca453d31 | N/A | SSRF - Cloud - 3 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...e540f17f | N/A | Version Control - Information Disclosure - Beta | Log | Block | This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529). |
| Cloudflare Managed Ruleset | ...ba458b4b | N/A | Command Injection - Generic 10 | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/#page","headline":"WAF Release - 2026-09-15","description":"Cloudflare WAF managed rulesets 2026-09-15 release","url":"https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/og.png?v=7a1ca4801e3099f6","dateModified":"2026-09-15","datePublished":"2026-09-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
