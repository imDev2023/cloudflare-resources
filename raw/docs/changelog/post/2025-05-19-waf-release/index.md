---
description: Cloudflare WAF managed rulesets 2025-05-19 release
title: WAF Release - 2025-05-19
image: https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/og.png?v=d4b8d6e78ab00460
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2025

## WAF Release - 2025-05-19

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in *Block* mode.

**Key Findings**

- Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.
- BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.
- Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.
- Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured `mod_proxy` behavior. While not RCE, this is useful for pre-attack recon.

**Impact**

These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.

Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...75129820 | 100745 | Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...26a517f1 | 100747 | Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d7619ccb | 100749 | BentoML - Remote Code Execution - CVE:CVE-2025-27520 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f15bfda4 | 100753 | Craft CMS - Remote Code Execution - CVE:CVE-2024-56145 | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/#page","headline":"WAF Release - 2025-05-19","description":"Cloudflare WAF managed rulesets 2025-05-19 release","url":"https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/og.png?v=d4b8d6e78ab00460","dateModified":"2025-05-19","datePublished":"2025-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
