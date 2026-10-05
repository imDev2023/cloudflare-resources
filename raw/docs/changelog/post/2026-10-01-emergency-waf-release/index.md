---
description: Cloudflare WAF managed rulesets 2026-10-01 emergency release
title: WAF Release - 2026-10-01 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/og.png?v=365b4a29871a035d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## WAF Release - 2026-10-01 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This update provides immediate defense against a vulnerability affecting Citrix NetScaler ADC and Gateway appliances, deploying protection against improper input validation vectors.

**Key Findings**

- CVE-2026-88771: An improper input validation vulnerability affecting Citrix NetScaler ADC and Gateway allows an unauthenticated attacker to execute arbitrary commands.

**Impact**

We strongly recommend that administrators apply the latest versions to fully secure origin servers. Additionally, customers should review configurations against applicable preconditions and follow standard incident response processes if signs of compromise are identified.

Detailed Rule Changes

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...827ab216 | N/A | Citrix Netscaler ADC and Gateway - Improper input validation - CVE:CVE-2026-88771 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/#page","headline":"WAF Release - 2026-10-01 - Emergency","description":"Cloudflare WAF managed rulesets 2026-10-01 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/og.png?v=365b4a29871a035d","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
