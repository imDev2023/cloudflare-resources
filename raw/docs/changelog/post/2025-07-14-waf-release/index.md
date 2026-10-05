---
description: Cloudflare WAF managed rulesets 2025-07-14 release
title: WAF Release - 2025-07-14
image: https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/og.png?v=b7cbbe5cda9cdd5c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 14, 2025

## WAF Release - 2025-07-14

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.

**Key Findings**

- XSS – Attribute Overloading: A novel cross-site scripting technique where attackers abuse custom or non-standard HTML attributes to smuggle payloads into the DOM. These payloads evade traditional sanitization logic, especially in frameworks that loosely validate attributes or trust unknown tokens.
- XSS – onToggle Event Abuse: Exploits the lesser-used onToggle event (triggered by elements like `<details>`) to execute arbitrary JavaScript when users interact with UI elements. This vector is often overlooked by static analyzers and can be embedded in seemingly benign components.

**Impact**

These vulnerabilities target both user-facing components and back-end databases, introducing potential vectors for credential theft, session hijacking, or full data exfiltration. The XSS variants bypass conventional filters through overlooked HTML behaviors, while the obfuscated SQLi enables attackers to stealthily probe back-end logic, making them especially difficult to detect and block.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2aa3d845 | 100798 | XSS - Attribute Overloading | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...37548d06 | 100799 | XSS - OnToggle | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/#page","headline":"WAF Release - 2025-07-14","description":"Cloudflare WAF managed rulesets 2025-07-14 release","url":"https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/og.png?v=b7cbbe5cda9cdd5c","dateModified":"2025-07-14","datePublished":"2025-07-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
