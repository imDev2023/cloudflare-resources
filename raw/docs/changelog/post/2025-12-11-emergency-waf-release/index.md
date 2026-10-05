---
description: Cloudflare WAF managed rulesets 2025-12-11 emergency release
title: WAF Release - 2025-12-11 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/og.png?v=0ffec8e4a5d48b88
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 11, 2025

## WAF Release - 2025-12-11 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.

**Key Findings**

Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).

**Impact**

These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...fefb4e9b | N/A | React - Leaking Server Functions - CVE:CVE-2025-55183 | N/A | Block | This was labeled as Generic - Server Function Source Code Exposure. |
| Cloudflare Free Ruleset | ...251e86aa | N/A | React - Leaking Server Functions - CVE:CVE-2025-55183 | N/A | Block | This was labeled as Generic - Server Function Source Code Exposure. |
| Cloudflare Managed Ruleset | ...102ec699 | N/A | React - DoS - CVE:CVE-2025-55184 | N/A | Disabled | This was labeled as Generic – Server Function Resource Exhaustion. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/#page","headline":"WAF Release - 2025-12-11 - Emergency","description":"Cloudflare WAF managed rulesets 2025-12-11 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/og.png?v=0ffec8e4a5d48b88","dateModified":"2025-12-11","datePublished":"2025-12-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
