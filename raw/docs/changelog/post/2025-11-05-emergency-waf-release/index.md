---
description: Cloudflare WAF managed rulesets 2025-11-05 emergency release
title: WAF Release - 2025-11-05 - Emergency
image: https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/og.png?v=23558aeb662ab4b3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 5, 2025

## WAF Release - 2025-11-05 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s emergency release introduces a new detection signature that enhances coverage for a critical vulnerability in the React Native Metro Development Server, tracked as CVE-2025-11953.

**Key Findings**

The Metro Development Server exposes an HTTP endpoint that is vulnerable to OS command injection (CWE-78). An unauthenticated network attacker can send a crafted request to this endpoint and execute arbitrary commands on the host running Metro. The vulnerability affects Metro/cli-server-api builds used by React Native Community CLI in pre-patch development releases.

**Impact**

Successful exploitation of CVE-2025-11953 may result in remote command execution on developer workstations or CI/build agents, leading to credential and secret exposure, source tampering, and potential lateral movement into internal networks. Administrators and developers are strongly advised to apply the vendor's patches and restrict Metro’s network exposure to reduce this risk.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c8e30c5b | N/A | React Native Metro - Command Injection - CVE:CVE-2025-11953 | N/A | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/#page","headline":"WAF Release - 2025-11-05 - Emergency","description":"Cloudflare WAF managed rulesets 2025-11-05 emergency release","url":"https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/og.png?v=23558aeb662ab4b3","dateModified":"2025-11-05","datePublished":"2025-11-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
