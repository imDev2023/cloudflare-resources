---
description: Cloudflare WAF managed rulesets 2025-09-24 emergency release
title: WAF Release - 2025-09-24 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/og.png?v=15be5755e7ed6425
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 24, 2025

## WAF Release - 2025-09-24 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights a critical vendor-specific vulnerability: a deserialization flaw in the License Servlet of Fortra’s GoAnywhere MFT. By forging a license response signature, an attacker can trigger deserialization of arbitrary objects, potentially leading to command injection.

**Key Findings**

- GoAnywhere MFT (CVE-2025-10035): Deserialization vulnerability in the License Servlet that allows attackers with a forged license response signature to deserialize arbitrary objects, potentially resulting in command injection.

**Impact**

GoAnywhere MFT (CVE-2025-10035): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...e08b39f3 | 100787 | Fortra GoAnywhere - Auth Bypass - CVE:CVE-2025-10035 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/#page","headline":"WAF Release - 2025-09-24 - Emergency","description":"Cloudflare WAF managed rulesets 2025-09-24 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/og.png?v=15be5755e7ed6425","dateModified":"2025-09-24","datePublished":"2025-09-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
