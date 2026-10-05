---
description: Cloudflare WAF managed rulesets 2026-08-11 release
title: WAF Release - 2026-08-11
image: https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/og.png?v=dd1cef2e061b9bd4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 11, 2026

## WAF Release - 2026-08-11

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.

**Key Findings**

- A new detection provides protection against vBulletin CVE-2026-61511.
- Two existing detections have been improved to strengthen coverage.

**Impact**

Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...94f3006b | N/A | vBulletin - Remote Code Execution - CVE:CVE-2026-61511 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...098b749e | N/A | Version Control - Information Disclosure - Beta | Log | Block | This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529) |
| Cloudflare Managed Ruleset | ...d56225d8 | N/A | vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta | Log | Block | This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: ...8fe9f1c7) |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/#page","headline":"WAF Release - 2026-08-11","description":"Cloudflare WAF managed rulesets 2026-08-11 release","url":"https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/og.png?v=dd1cef2e061b9bd4","dateModified":"2026-08-11","datePublished":"2026-08-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
