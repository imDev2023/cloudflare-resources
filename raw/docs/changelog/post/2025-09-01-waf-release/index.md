---
description: Cloudflare WAF managed rulesets 2025-09-01 release
title: WAF Release - 2025-09-01
image: https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/og.png?v=fabfb40dbe14bd49
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 1, 2025

## WAF Release - 2025-09-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, a critical vulnerability was disclosed in Fortinet FortiWeb (versions 7.6.3 and below, versions 7.4.7 and below, versions 7.2.10 and below, and versions 7.0.10 and below), linked to improper parameter handling that could allow unauthorized access.

**Key Findings**

- Fortinet FortiWeb (CVE-2025-52970): A vulnerability may allow an unauthenticated remote attacker with access to non-public information to log in as any existing user on the device via a specially crafted request.

**Impact**

Exploitation could allow an unauthenticated attacker to impersonate any existing user on the device, potentially enabling them to modify system settings or exfiltrate sensitive information, posing a serious security risk. Upgrading to the latest vendor-released version is strongly recommended.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c49b7cf8 | 100586 | Fortinet FortiWeb - Auth Bypass - CVE:CVE-2025-52970 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...790c9dde | 100136C | XSS - JavaScript - Headers and Body | N/A | N/A | Rule metadata description refined. Detection unchanged. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/#page","headline":"WAF Release - 2025-09-01","description":"Cloudflare WAF managed rulesets 2025-09-01 release","url":"https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/og.png?v=fabfb40dbe14bd49","dateModified":"2025-09-01","datePublished":"2025-09-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
