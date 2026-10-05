---
description: Cloudflare WAF managed rulesets 2026-01-20 release
title: WAF Release - 2026-01-20
image: https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/og.png?v=eeeca20c5b646b15
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## WAF Release - 2026-01-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against SQL injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...68d90c8f | N/A | SQLi - Comment - Beta | Log | Block | This rule is merged into the original rule "SQLi - Comment" (ID: ...6d8d8fe4) |
| Cloudflare Managed Ruleset | ...faa045cf

N/A | SQLi - Comparison - Beta | Log | Block  
 | This rule is merged into the original rule "SQLi - Comparison" (ID: ...e7907480)

 |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/#page","headline":"WAF Release - 2026-01-20","description":"Cloudflare WAF managed rulesets 2026-01-20 release","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-waf-release/og.png?v=eeeca20c5b646b15","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
