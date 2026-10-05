---
description: Cloudflare WAF managed rulesets 2026-01-12 release
title: WAF Release - 2026-01-12
image: https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/og.png?v=c477658c83bd4a43
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 12, 2026

## WAF Release - 2026-01-12

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...48a1841a | N/A | SQLi - AND/OR MAKE\_SET/ELT - Beta | Log | Block | This rule is merged into the original rule "SQLi - AND/OR MAKE\_SET/ELT" (ID: ...252d3934) |
| Cloudflare Managed Ruleset | ...9e553ad3

N/A | SQLi - Benchmark Function - Beta | Log | Block  
 | This rule is merged into the original rule "SQLi - Benchmark Function" (ID: ...2ebc44ad)

 |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/#page","headline":"WAF Release - 2026-01-12","description":"Cloudflare WAF managed rulesets 2026-01-12 release","url":"https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/og.png?v=c477658c83bd4a43","dateModified":"2026-01-12","datePublished":"2026-01-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
