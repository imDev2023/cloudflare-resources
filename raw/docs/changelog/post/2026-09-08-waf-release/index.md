---
description: Cloudflare WAF managed rulesets 2026-09-08 release
title: WAF Release - 2026-09-08
image: https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/og.png?v=d86ff1aaabcd57e1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 8, 2026

## WAF Release - 2026-09-08

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c76ba662 | N/A | Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta | Log | Block | This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID: ...80256efe). |
| Cloudflare Managed Ruleset | ...208457cf | N/A | Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta | Log | Block | This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID: ...2ca6cce3). |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/#page","headline":"WAF Release - 2026-09-08","description":"Cloudflare WAF managed rulesets 2026-09-08 release","url":"https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/og.png?v=d86ff1aaabcd57e1","dateModified":"2026-09-08","datePublished":"2026-09-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
