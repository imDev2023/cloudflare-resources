---
description: Cloudflare WAF managed rulesets 2025-10-20 release
title: WAF Release - 2025-10-20
image: https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/og.png?v=c6476bcb3657f6a2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 20, 2025

## WAF Release - 2025-10-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.

**Key Findings**

New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.

**Impact**

- Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2b4101ab | 100598A | Remote Code Execution - Common Bash Bypass - Beta | Log | Block | This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: ...50cec478) |
| Cloudflare Managed Ruleset | ...a1118614 | 100916A | Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...c22b51d3 | N/A | HTTP Truncated | N/A | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/#page","headline":"WAF Release - 2025-10-20","description":"Cloudflare WAF managed rulesets 2025-10-20 release","url":"https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/og.png?v=c6476bcb3657f6a2","dateModified":"2025-10-20","datePublished":"2025-10-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
