---
description: Cloudflare WAF managed rulesets 2025-10-07 emergency release
title: WAF Release - 2025-10-07 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/og.png?v=28bd1336a6e8a9f9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 7, 2025

## WAF Release - 2025-10-07 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device. The initial two rules were made available on September 28, with a third rule added today, October 7, for more robust protection.

- Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.

**Impact**

Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection. Administrators are strongly advised to apply vendor updates immediately.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...3a4d1bd6 | 100788B | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/#page","headline":"WAF Release - 2025-10-07 - Emergency","description":"Cloudflare WAF managed rulesets 2025-10-07 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/og.png?v=28bd1336a6e8a9f9","dateModified":"2025-10-07","datePublished":"2025-10-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
