---
description: Cloudflare WAF managed rulesets 2025-12-10 emergency release
title: WAF Release - 2025-12-10 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/og.png?v=4931ced6b89fd431
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 10, 2025

## WAF Release - 2025-12-10 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.

**Key Findings**

Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.

**Impact**

These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...15fce168 | N/A | React - Remote Code Execution - CVE:CVE-2025-55182 - 2 | N/A | Block | This is an improved detection. |
| Cloudflare Free Ruleset | ...74746aff | N/A | React - Remote Code Execution - CVE:CVE-2025-55182 - 2 | N/A | Block | This is an improved detection. |
| Cloudflare Managed Ruleset | ...fefb4e9b | N/A | Generic - Server Function Source Code Exposure | N/A | Block | This is a new detection. |
| Cloudflare Free Ruleset | ...251e86aa | N/A | Generic - Server Function Source Code Exposure | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...102ec699 | N/A | Generic - Server Function Resource Exhaustion | N/A | Disabled | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/#page","headline":"WAF Release - 2025-12-10 - Emergency","description":"Cloudflare WAF managed rulesets 2025-12-10 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-10-emergency-waf-release/og.png?v=4931ced6b89fd431","dateModified":"2025-12-10","datePublished":"2025-12-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
