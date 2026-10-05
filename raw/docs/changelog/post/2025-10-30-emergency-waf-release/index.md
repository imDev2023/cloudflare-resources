---
description: Cloudflare WAF managed rulesets 2025-10-30 emergency release
title: WAF Release - 2025-10-30 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/og.png?v=1fe7c329c4cd6899
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 30, 2025

## WAF Release - 2025-10-30 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Oracle E-Business Suite, tracked as CVE-2025-61884.

**Key Findings**

The flaw is easily exploitable and allows an unauthenticated attacker with network access to compromise Oracle Configurator, which can grant access to sensitive resources and configuration data. The affected versions include 12.2.3 through 12.2.14.

**Impact**

Successful exploitation of CVE-2025-61884 may result in unauthorized access to critical business data or full exposure of information accessible through Oracle Configurator. Administrators are strongly advised to apply vendor's patches and recommended mitigations to reduce this exposure.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...8827402f | N/A | Oracle E-Business Suite - SSRF - CVE:CVE-2025-61884 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/#page","headline":"WAF Release - 2025-10-30 - Emergency","description":"Cloudflare WAF managed rulesets 2025-10-30 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/og.png?v=1fe7c329c4cd6899","dateModified":"2025-10-30","datePublished":"2025-10-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
