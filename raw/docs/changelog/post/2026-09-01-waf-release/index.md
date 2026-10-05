---
description: Cloudflare WAF managed rulesets 2026-09-01 release
title: WAF Release - 2026-09-01
image: https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/og.png?v=72d9fe1c88f8d80c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 1, 2026

## WAF Release - 2026-09-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.

**Key Findings**

- SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...bcfa0966 | N/A | SQLi - WHERE Comparison With WITH Clause | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/#page","headline":"WAF Release - 2026-09-01","description":"Cloudflare WAF managed rulesets 2026-09-01 release","url":"https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/og.png?v=72d9fe1c88f8d80c","dateModified":"2026-09-01","datePublished":"2026-09-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
