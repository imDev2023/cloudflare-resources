---
description: Cloudflare WAF managed rulesets 2025-09-28 emergency release
title: WAF Release - 2025-09-28 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/og.png?v=a3fa7eaf3e4c291b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 28, 2025

## WAF Release - 2025-09-28 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.

**Key Findings**

- Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.

**Impact**

Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...9ee0ab84 | 100788 | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d30f768e | 100788A | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/#page","headline":"WAF Release - 2025-09-28 - Emergency","description":"Cloudflare WAF managed rulesets 2025-09-28 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/og.png?v=a3fa7eaf3e4c291b","dateModified":"2025-09-28","datePublished":"2025-09-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
