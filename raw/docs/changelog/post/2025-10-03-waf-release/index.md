---
description: Cloudflare WAF managed rulesets 2025-10-03 release
title: WAF Release - 2025-10-03
image: https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/og.png?v=9a66d15b8fb7c859
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 3, 2025

## WAF Release - 2025-10-03

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Managed Ruleset Updated**

This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d61fac74 | 100902 | Generic Rules - Command Execution - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...514aeeb8 | 100908 | Generic Rules - Command Execution - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...8d46a6f4 | 100910 | Generic Rules - Command Execution - 4 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1bd0a329 | 100915 | Generic Rules - Command Execution - 5 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5e51450a | 100899 | Generic Rules - Content-Type Abuse | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7996012f | 100914 | Generic Rules - Content-Type Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...93209312 | 100911 | Generic Rules - Cookie Header Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...0f373b3f | 100905 | Generic Rules - NoSQL Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...78a0ed04 | 100913 | Generic Rules - NoSQL Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5d649624 | 100907 | Generic Rules - Parameter Pollution | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...fd1c674e | 100906 | Generic Rules - PHP Object Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...34c88168 | 100904 | Generic Rules - Prototype Pollution | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3ab43f7e | 100897 | Generic Rules - Prototype Pollution 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...0d94ee22 | 100903 | Generic Rules - Reverse Shell | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d5add8e3 | 100909 | Generic Rules - Reverse Shell - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...565c78b0 | 100898 | Generic Rules - SSJI NoSQL | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...12b837a0 | 100896 | Generic Rules - SSRF | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...11c4fb00 | 100895 | Generic Rules - Template Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d3ed0123 | 100895A | Generic Rules - Template Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7501a1d9 | 100912 | Generic Rules - XXE | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...dc55cdb6 | 100900 | Relative Paths - Anomaly Headers | N/A | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/#page","headline":"WAF Release - 2025-10-03","description":"Cloudflare WAF managed rulesets 2025-10-03 release","url":"https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/og.png?v=9a66d15b8fb7c859","dateModified":"2025-10-03","datePublished":"2025-10-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
