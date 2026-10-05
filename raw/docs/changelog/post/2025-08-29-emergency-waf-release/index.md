---
description: Cloudflare WAF managed rulesets 2025-08-29 emergency release
title: WAF Release - 2025-08-29 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/og.png?v=f6cec349bc5b7ed1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 29, 2025

## WAF Release - 2025-08-29 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.

**Key Findings**

- CVE-2025-55173: Arbitrary file download from the server via image optimization.
- CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.

**Impact**

Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...9ff4bfe3 | 100613 | Next.js - Dangerous File Download - CVE:CVE-2025-55173 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...69b9ea7d | 100616 | Next.js - Information Disclosure - CVE:CVE-2025-57752 | N/A | Block | This is a new detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/#page","headline":"WAF Release - 2025-08-29 - Emergency","description":"Cloudflare WAF managed rulesets 2025-08-29 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/og.png?v=f6cec349bc5b7ed1","dateModified":"2025-08-29","datePublished":"2025-08-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
