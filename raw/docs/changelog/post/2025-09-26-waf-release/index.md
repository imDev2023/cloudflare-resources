---
description: Cloudflare WAF managed rulesets 2025-09-26 release
title: WAF Release - 2025-09-26
image: https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/og.png?v=4239ac8cd0e0e5f9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 26, 2025

## WAF Release - 2025-09-26

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Managed Ruleset Updated**

This update introduces 11 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a67d8561 | 100859A | SQLi - UNION - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...4de80468 | 100889 | Command Injection - Generic 9 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f2be3ddf | 100890 | Information Disclosure - Common Files - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...80a252a8 | 100891 | Anomaly:URL - Relative Paths | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7e7d3865 | 100894 | XSS - Inline Function | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3792565c | 100895 | XSS - DOM | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...42978e38 | 100896 | SQLi - MSSQL Length Enumeration | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3ab43f7e | 100897 | Generic Rules - Code Injection - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c1686741 | 100898 | SQLi - Evasion | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...20999be0 | 100899 | SQLi - Probing 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...b4026c88 | 100900 | SQLi - Probing | N/A | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/#page","headline":"WAF Release - 2025-09-26","description":"Cloudflare WAF managed rulesets 2025-09-26 release","url":"https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/og.png?v=4239ac8cd0e0e5f9","dateModified":"2025-09-26","datePublished":"2025-09-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
