---
description: Cloudflare WAF managed rulesets 2025-08-07 emergency release
title: WAF Release - 2025-08-07 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/og.png?v=6f4764f51202eedd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2025

## WAF Release - 2025-08-07 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s highlight focuses on two critical vulnerabilities affecting key infrastructure and enterprise content management platforms. Both flaws present significant remote code execution risks that can be exploited with minimal or no user interaction.

**Key Findings**

- Squid (≤6.3) — CVE-2025-54574: A heap buffer overflow occurs when processing Uniform Resource Names (URNs). This vulnerability may allow remote attackers to execute arbitrary code on the server. The issue has been resolved in version 6.4.
- Adobe AEM (≤6.5.23) — CVE-2025-54253: Due to a misconfiguration, attackers can achieve remote code execution without requiring any user interaction, posing a severe threat to affected deployments.

**Impact**

Both vulnerabilities expose critical attack vectors that can lead to full server compromise. The Squid heap buffer overflow allows remote code execution by crafting malicious URNs, which can lead to server takeover or denial of service. Given Squid’s widespread use as a caching proxy, this flaw could be exploited to disrupt network traffic or gain footholds inside secure environments.

Adobe AEM’s remote code execution vulnerability enables attackers to run arbitrary code on the content management server without any user involvement. This puts sensitive content, application integrity, and the underlying infrastructure at extreme risk. Exploitation could lead to data theft, defacement, or persistent backdoor installation.

These findings reinforce the urgency of updating to the patched versions — Squid 6.4 and Adobe AEM 6.5.24 or later — and reviewing configurations to prevent exploitation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...ef7e015b | 100844 | Adobe Experience Manager Forms - Remote Code Execution - CVE:CVE-2025-54253 | N/A | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...baec057a | 100840 | Squid - Buffer Overflow - CVE:CVE-2025-54574 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/#page","headline":"WAF Release - 2025-08-07 - Emergency","description":"Cloudflare WAF managed rulesets 2025-08-07 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/og.png?v=6f4764f51202eedd","dateModified":"2025-08-07","datePublished":"2025-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
