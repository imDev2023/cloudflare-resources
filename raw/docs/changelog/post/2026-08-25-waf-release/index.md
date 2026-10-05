---
description: Cloudflare WAF managed rulesets 2026-08-25 release
title: WAF Release - 2026-08-25
image: https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/og.png?v=d199afffc37df957
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## WAF Release - 2026-08-25

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.

**Key Findings**

- Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.
- The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.
- A Generic Rules - Remote Code Execution detection is added in Block mode.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...1489d892 | N/A | HTTP/2 Request Smuggling - Request Body Anomaly | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...20646260 | N/A | XSS - JavaScript Event Handler Coercion - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...d706d517 | N/A | XSS - JavaScript Event Handler Coercion - Body | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...660886c8 | N/A | XSS - JavaScript Event Handler Coercion - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c293b926 | N/A | XSS, HTML Injection - Script Tag - Beta | Log | Block | This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID: ...7b58420b). |
| Cloudflare Managed Ruleset | ...2ca6cce3 | N/A | Generic Rules - Remote Code Execution | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/#page","headline":"WAF Release - 2026-08-25","description":"Cloudflare WAF managed rulesets 2026-08-25 release","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/og.png?v=d199afffc37df957","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
