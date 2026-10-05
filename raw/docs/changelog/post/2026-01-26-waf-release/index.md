---
description: Cloudflare WAF managed rulesets 2026-01-26 release
title: WAF Release - 2026-01-26
image: https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/og.png?v=cbd57a2809465348
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 26, 2026

## WAF Release - 2026-01-26

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 ([https://www.cve.org/CVERecord?id=CVE-2026-23864 ↗︎](https://www.cve.org/CVERecord?id=CVE-2026-23864)).

**Key Findings**

- CVE-2026-23864 ([https://www.cve.org/CVERecord?id=CVE-2026-23864 ↗︎](https://www.cve.org/CVERecord?id=CVE-2026-23864)) affects `react-server-dom-parcel`, `react-server-dom-turbopack`, and `react-server-dom-webpack` packages.
- Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...61680354 | N/A | React Server - DOS - CVE:CVE-2026-23864 - 1 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...dcdffcf8 | N/A | React Server - DOS - CVE:CVE-2026-23864 - 2 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...349edbc6 | N/A | React Server - DOS - CVE:CVE-2026-23864 - 3 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/#page","headline":"WAF Release - 2026-01-26","description":"Cloudflare WAF managed rulesets 2026-01-26 release","url":"https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-26-waf-release/og.png?v=cbd57a2809465348","dateModified":"2026-01-26","datePublished":"2026-01-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
