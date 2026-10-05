---
description: Cloudflare WAF managed rulesets 2025-09-04 emergency release
title: WAF Release - 2025-09-04 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/og.png?v=c92895659250c939
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2025

## WAF Release - 2025-09-04 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, new critical vulnerabilities were disclosed in Sitecore’s Sitecore Experience Manager (XM), Sitecore Experience Platform (XP), specifically versions 9.0 through 9.3, and 10.0 through 10.4. These flaws are caused by unsafe data deserialization and code reflection, leaving affected systems at high risk of exploitation.

**Key Findings**

- CVE-2025-53690: Remote Code Execution through Insecure Deserialization
- CVE-2025-53691: Remote Code Execution through Insecure Deserialization
- CVE-2025-53693: HTML Cache Poisoning through Unsafe Reflections

**Impact**

Exploitation could allow attackers to execute arbitrary code remotely on the affected system and conduct cache poisoning attacks, potentially leading to further compromise. Applying the latest vendor-released solution without delay is strongly recommended.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...0ee2c15e | 100878 | Sitecore - Remote Code Execution - CVE:CVE-2025-53691 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...7c5b669c | 100631 | Sitecore - Cache Poisoning - CVE:CVE-2025-53693 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...6c410240 | 100879 | Sitecore - Remote Code Execution - CVE:CVE-2025-53690 | N/A | Block | This is a new detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/#page","headline":"WAF Release - 2025-09-04 - Emergency","description":"Cloudflare WAF managed rulesets 2025-09-04 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/og.png?v=c92895659250c939","dateModified":"2025-09-04","datePublished":"2025-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
