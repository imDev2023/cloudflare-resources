---
description: Cloudflare WAF managed rulesets 2026-03-23 release
title: WAF Release - 2026-03-23
image: https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/og.png?v=d16ccddff26bfaed
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 23, 2026

## WAF Release - 2026-03-23

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on new improvements to enhance coverage.

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...97321c6c | N/A | Command Injection - Generic 9 - URI Vector | Log | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...1eb7a999

N/A | Command Injection - Generic 9 - Header Vector | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...0677175f

N/A | Command Injection - Generic 9 - Body Vector | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...479da68f | N/A | PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132 (beta) | Log | Block | This rule has been merged into the original rule "PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132" (ID: ...824b817c) |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/#page","headline":"WAF Release - 2026-03-23","description":"Cloudflare WAF managed rulesets 2026-03-23 release","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-23-waf-release/og.png?v=d16ccddff26bfaed","dateModified":"2026-03-23","datePublished":"2026-03-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
