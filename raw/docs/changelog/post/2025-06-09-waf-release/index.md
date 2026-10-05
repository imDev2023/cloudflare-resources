---
description: Cloudflare WAF managed rulesets 2025-06-09 release
title: WAF Release - 2025-06-09
image: https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/og.png?v=0f748095c6f6fdcd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 9, 2025

## WAF Release - 2025-06-09

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s update spotlights four critical vulnerabilities across CMS platforms, VoIP systems, and enterprise applications. Several flaws enable remote code execution or privilege escalation, posing significant enterprise risks.

**Key Findings**

- WordPress OttoKit Plugin (CVE-2025-27007): Privilege escalation flaw allows unauthenticated attackers to create or elevate user accounts, compromising WordPress administrative control.
- SAP NetWeaver (CVE-2025-42999): Remote Code Execution vulnerability enables attackers to execute arbitrary code on SAP NetWeaver systems, threatening core ERP and business operations.
- Fortinet FortiVoice (CVE-2025-32756): Buffer error vulnerability may lead to memory corruption and potential code execution, directly impacting enterprise VoIP infrastructure.
- Camaleon CMS (CVE-2024-46986): Remote Code Execution vulnerability allows attackers to gain full control over Camaleon CMS installations, exposing hosted content and underlying servers.

**Impact**

These vulnerabilities target widely deployed CMS, ERP, and VoIP systems. RCE flaws in SAP NetWeaver and Camaleon CMS allow full takeover of business-critical applications. Privilege escalation in OttoKit exposes WordPress environments to full administrative compromise. FortiVoice buffer handling issues risk destabilizing or fully compromising enterprise telephony systems.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...0debd86e | 100769 | WordPress OttoKit Plugin - Privilege Escalation - CVE:CVE-2025-27007 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5f57b448 | 100770 | SAP NetWeaver - Remote Code Execution - CVE:CVE-2025-42999 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...4df8857a | 100779 | Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...3b840107 | 100780 | Camaleon CMS - Remote Code Execution - CVE:CVE-2024-46986 | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/#page","headline":"WAF Release - 2025-06-09","description":"Cloudflare WAF managed rulesets 2025-06-09 release","url":"https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/og.png?v=0f748095c6f6fdcd","dateModified":"2025-06-09","datePublished":"2025-06-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
