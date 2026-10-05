---
description: Cloudflare WAF managed rulesets 2026-08-04
title: WAF Release - 2026-08-04
image: https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/og.png?v=6a724b3d52fd6d31
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## WAF Release - 2026-08-04

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.

**Key Findings**

- CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.
- CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.
- Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...052b07cf | N/A | Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...3a5b40d6 | N/A | Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066 | Block | Block | This was labeled as File Upload - RCE. |
| Cloudflare Managed Ruleset | ...743a63ec | N/A | SSRF - Local - 2 - Beta | Disabled | - | This detection has been removed. |
| Cloudflare Managed Ruleset | ...c2e84e2d | N/A | SSRF - Cloud - Beta | Disabled | - | This detection has been removed. |
| Cloudflare Managed Ruleset | ...ab8af26f | N/A | SSRF - Cloud - 2 - Beta | Disabled | - | This detection has been removed. |
| Cloudflare Managed Ruleset | ...25ba9d7c | N/A | SSRF - Cloud | Disabled | Block | We are changing the action for this rule from Disabled to BLOCK |
| Cloudflare Managed Ruleset | ...01a076eb | N/A | SSRF - Local - Beta | Disabled | - | This detection has been removed. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/#page","headline":"WAF Release - 2026-08-04","description":"Cloudflare WAF managed rulesets 2026-08-04","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-waf-release/og.png?v=6a724b3d52fd6d31","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
