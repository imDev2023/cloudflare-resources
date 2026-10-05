---
description: Cloudflare WAF managed rulesets 2025-11-21 release
title: WAF Release - 2025-11-21
image: https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/og.png?v=541d1dd168aeb124
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 21, 2025

## WAF Release - 2025-11-21

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a critical detection for CVE-2025-61757, a vulnerability in the Oracle Identity Manager REST WebServices component.

**Key Findings**

This flaw allows unauthenticated attackers with network access over HTTP to fully compromise the Identity Manager, potentially leading to a complete takeover.

**Impact**

Oracle Identity Manager (CVE-2025-61757): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...39fdbe7e | N/A | Oracle Identity Manager - Pre-Auth RCE - CVE:CVE-2025-61757 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/#page","headline":"WAF Release - 2025-11-21","description":"Cloudflare WAF managed rulesets 2025-11-21 release","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-21-emergency-waf-release/og.png?v=541d1dd168aeb124","dateModified":"2025-11-21","datePublished":"2025-11-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
