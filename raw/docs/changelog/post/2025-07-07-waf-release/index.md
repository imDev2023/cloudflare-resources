---
description: Cloudflare WAF managed rulesets 2025-07-07 release
title: WAF Release - 2025-07-07
image: https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/og.png?v=8b1227e841c0b517
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 7, 2025

## WAF Release - 2025-07-07

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.

**Key Findings**

- Next.js - Auth Bypass: A newly detected authentication bypass flaw in the Next.js framework allows attackers to access protected routes or APIs without proper authorization, undermining application access controls.
- Fortinet FortiVoice (CVE-2025-32756): A buffer error vulnerability in FortiVoice systems that could lead to memory corruption and potential code execution or service disruption in enterprise telephony environments.
- Roundcube (CVE-2025-49113): A critical RCE flaw allowing unauthenticated attackers to execute arbitrary PHP code via crafted requests, leading to full compromise of mail servers and user inboxes.

**Impact**

These vulnerabilities affect core business infrastructure, from web interfaces to voice communications and email platforms. The Roundcube RCE and FortiVoice buffer flaw offer potential for deep system access, while the Next.js auth bypass undermines trust boundaries in modern web apps.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...7eb35ee6 | 100795 | Next.js - Auth Bypass | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c329aeb0 | 100796 | Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...ab314023 | 100797 | Roundcube - Remote Code Execution - CVE:CVE-2025-49113 | Log | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/#page","headline":"WAF Release - 2025-07-07","description":"Cloudflare WAF managed rulesets 2025-07-07 release","url":"https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/og.png?v=8b1227e841c0b517","dateModified":"2025-07-07","datePublished":"2025-07-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
