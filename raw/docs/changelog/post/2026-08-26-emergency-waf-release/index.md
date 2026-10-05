---
description: Cloudflare WAF managed rulesets 2026-08-26 emergency release
title: WAF Release - 2026-08-26 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/og.png?v=7a8fdc1bcea1dc12
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## WAF Release - 2026-08-26 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.

**Key Findings**

- CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.
- GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.

**Impact**

Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2ca6cce3 | N/A | Next.js - Remote Code Execution - CVE:CVE-2026-75604 | Block | N/A | Rule metadata description refined. Detection unchanged. |
| Cloudflare Managed Ruleset | ...80256efe | N/A | Next.js - Image Optimizer Remote Code Execution via Crafted AVIF | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/#page","headline":"WAF Release - 2026-08-26 - Emergency","description":"Cloudflare WAF managed rulesets 2026-08-26 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/og.png?v=7a8fdc1bcea1dc12","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
