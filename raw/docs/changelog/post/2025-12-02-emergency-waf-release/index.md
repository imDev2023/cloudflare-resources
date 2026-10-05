---
description: Cloudflare WAF managed rulesets 2025-12-02 emergency release
title: WAF Release - 2025-12-02 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/og.png?v=e03ecc561baa90cc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 2, 2025

## WAF Release - 2025-12-02 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's emergency release introduces a new rule to block a critical RCE vulnerability in widely-used web frameworks through unsafe deserialization patterns.

**Key Findings**

New WAF rule deployed for RCE Generic Framework to block malicious POST requests containing unsafe deserialization patterns. If successfully exploited, this vulnerability allows attackers with network access via HTTP to execute arbitrary code remotely.

**Impact**

- Successful exploitation allows unauthenticated attackers to execute arbitrary code remotely through crafted serialization payloads, enabling complete system compromise, data exfiltration, and potential lateral movement within affected environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...5fb92fba | N/A | RCE Generic - Framework | N/A | Block | This is a new detection. |
| Cloudflare Free Ruleset | ...99702280 | N/A | RCE Generic - Framework | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/#page","headline":"WAF Release - 2025-12-02 - Emergency","description":"Cloudflare WAF managed rulesets 2025-12-02 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/og.png?v=e03ecc561baa90cc","dateModified":"2025-12-02","datePublished":"2025-12-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
