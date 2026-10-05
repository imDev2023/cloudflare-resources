---
description: Cloudflare WAF managed rulesets 2026-04-30 emergency release
title: WAF Release - 2026-04-30 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/og.png?v=19f22c366e47026b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 30, 2026

## WAF Release - 2026-04-30 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces a new rule to block a cPanel & WHM Authentication Bypass related to CVE-2026-41940.

**Key Findings**

- CVE-2026-41940: A critical authentication bypass vulnerability in cPanel & WHM allows unauthenticated remote attackers to bypass authentication mechanisms and gain unauthorized administrative access to the web hosting control panel. This vulnerability affects the session validation logic, enabling attackers to craft malicious requests that circumvent normal authentication checks.

**Impact**

Successful exploitation allows unauthenticated attackers to gain administrative control over affected cPanel & WHM installations. This leads to complete server compromise, potential theft or manipulation of hosted data, and significant service disruption across managed environments.

We strongly recommend applying official vendor patches for cPanel & WHM immediately to address the underlying vulnerability.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...eb2b9e2f | N/A | cPanel - Auth Bypass - CVE:CVE-2026-41940 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/#page","headline":"WAF Release - 2026-04-30 - Emergency","description":"Cloudflare WAF managed rulesets 2026-04-30 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/og.png?v=19f22c366e47026b","dateModified":"2026-04-30","datePublished":"2026-04-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
