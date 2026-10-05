---
description: Cloudflare WAF managed rulesets 2025-05-05 release
title: WAF Release - 2025-05-05
image: https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/og.png?v=a371001b17ad074e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 5, 2025

## WAF Release - 2025-05-05

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.

**Key Findings**

GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.

The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.

**Impact**

Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:

- GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE
- SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances
- XWiki (CVE-2025-24893) - High priority for development environments
- Langflow (CVE-2025-3248) - Important for AI workflow platforms
- MinIO (CVE-2025-31489) - Important for object storage implementations

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d0b7a392 | 100724 | GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...717a9e42 | 100748 | XWiki - Remote Code Execution - CVE:CVE-2025-24893 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...e9cf745d | 100750 | SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040, CVE:CVE-2021-20041, CVE:CVE-2021-20042 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d29da333 | 100751 | Langflow - Remote Code Execution - CVE:CVE-2025-3248 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...caa7b208 | 100752 | MinIO - Auth Bypass - CVE:CVE-2025-31489 | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/#page","headline":"WAF Release - 2025-05-05","description":"Cloudflare WAF managed rulesets 2025-05-05 release","url":"https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/og.png?v=a371001b17ad074e","dateModified":"2025-05-05","datePublished":"2025-05-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
