---
description: Cloudflare WAF managed rulesets 2025-10-23 emergency release
title: WAF Release - 2025-10-23 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/og.png?v=7541d93d1a6c41d1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 23, 2025

## WAF Release - 2025-10-23 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.

**Key Findings**

This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update enhances detection logic to provide more resilient protection against exploitation attempts.

**Impact**

Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c6ef59a1 | N/A | Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/#page","headline":"WAF Release - 2025-10-23 - Emergency","description":"Cloudflare WAF managed rulesets 2025-10-23 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/og.png?v=7541d93d1a6c41d1","dateModified":"2025-10-23","datePublished":"2025-10-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
