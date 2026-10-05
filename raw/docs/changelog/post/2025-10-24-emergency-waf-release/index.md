---
description: Cloudflare WAF managed rulesets 2025-10-24 emergency release
title: WAF Release - 2025-10-24 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/og.png?v=3b7d970609a5c0cd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 24, 2025

## WAF Release - 2025-10-24 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.

**Key Findings**

The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.

**Impact**

Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...bd72ba08 | N/A | Windows Server - Deserialization - CVE:CVE-2025-59287 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/#page","headline":"WAF Release - 2025-10-24 - Emergency","description":"Cloudflare WAF managed rulesets 2025-10-24 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/og.png?v=3b7d970609a5c0cd","dateModified":"2025-10-24","datePublished":"2025-10-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
