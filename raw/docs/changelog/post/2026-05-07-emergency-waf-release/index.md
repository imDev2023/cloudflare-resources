---
description: Cloudflare WAF managed rulesets 2026-05-07 emergency release
title: WAF Release - 2026-05-07 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/og.png?v=51e955104cdd2306
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## WAF Release - 2026-05-07 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces a new rule to detect Next.js App Router middleware and proxy bypass attempts via segment-prefetch routes (CVE-2026-44575).

**Key Findings**

CVE-2026-44575: Next.js Middleware / Proxy Bypass in App Router Applications via Segment-Prefetch Routes

Successful exploitation allows unauthenticated attackers to bypass middleware or proxy-based authorization checks in affected Next.js App Router applications. This leads to unauthorized access to protected content, potential exposure of sensitive application data, and compromise of application security boundaries.

We strongly recommend upgrading to Next.js 15.5.16 or 16.2.5 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, enforce authorization in the underlying route or page logic instead of relying solely on middleware.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...e77e4a53 | N/A | Next.js - Middleware Bypass via Invalid RSC Header - CVE:CVE-2026-44575 | N/A | Disabled | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/#page","headline":"WAF Release - 2026-05-07 - Emergency","description":"Cloudflare WAF managed rulesets 2026-05-07 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/og.png?v=51e955104cdd2306","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
