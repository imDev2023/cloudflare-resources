---
description: Cloudflare WAF managed rulesets 2026-06-15
title: WAF Release - 2026-06-15
image: https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/og.png?v=f9fe249185b89c77
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 15, 2026

## WAF Release - 2026-06-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.

**Key Findings**

- CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...b4c29bc6 | N/A | Ghost CMS - SQLi - CVE:CVE-2026-26980 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...b56f403f | N/A | SQLi - Obfuscated Boolean - URI | Log | Disabled | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/#page","headline":"WAF Release - 2026-06-15","description":"Cloudflare WAF managed rulesets 2026-06-15","url":"https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/og.png?v=f9fe249185b89c77","dateModified":"2026-06-15","datePublished":"2026-06-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
