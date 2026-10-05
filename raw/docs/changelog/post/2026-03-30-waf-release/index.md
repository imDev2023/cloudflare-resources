---
description: Cloudflare WAF managed rulesets 2026-03-30 release
title: WAF Release - 2026-03-30
image: https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/og.png?v=ac244d913816188e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 30, 2026

## WAF Release - 2026-03-30

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for a critical authentication bypass vulnerability in Fortinet products (CVE-2025-59718), alongside three new generic detection rules designed to identify and block HTTP Parameter Pollution attempts. Additionally, this release includes targeted protection for a high-impact unrestricted file upload vulnerability in Magento and Adobe Commerce.

**Key Findings**

- CVE-2025-59718: An improper cryptographic signature verification vulnerability in Fortinet FortiOS, FortiProxy, and FortiSwitchManager. This may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication using a maliciously crafted SAML message, if that feature is enabled on the device.
- Magento 2 - Unrestricted File Upload: A critical flaw in Magento and Adobe Commerce allows unauthenticated attackers to bypass security checks and upload malicious files to the server, potentially leading to Remote Code Execution (RCE).

**Impact**

Successful exploitation of the Fortinet and Magento vulnerabilities could allow unauthenticated attackers to gain administrative control or deploy webshells, leading to complete server compromise and data theft.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2f7f95e9 | N/A | Generic Rules - Parameter Pollution - Body | Log | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...319731a4

N/A | Generic Rules - Parameter Pollution - Header - Form | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...def262dd

N/A | Generic Rules - Parameter Pollution - URI | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...70a36147 | N/A | Magento 2 - Unrestricted file upload | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...2ffcca9f | N/A | Fortinet FortiCloud SSO - Authentication Bypass - CVE:CVE-2025-59718 | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/#page","headline":"WAF Release - 2026-03-30","description":"Cloudflare WAF managed rulesets 2026-03-30 release","url":"https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/og.png?v=ac244d913816188e","dateModified":"2026-03-30","datePublished":"2026-03-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
