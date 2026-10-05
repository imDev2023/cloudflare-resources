---
description: Cloudflare WAF managed rulesets 2026-08-17 release
title: WAF Release - 2026-08-17
image: https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/og.png?v=4a55f908350b97bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 17, 2026

## WAF Release - 2026-08-17

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release updates WordPress remote code execution rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify CVE-2026-65640.

**Key Findings**

- CVE-2026-65640: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.

**Impact**

The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...3590a4ad | N/A | Wordpress - Remote Code Execution - CVE:CVE-2026-65640 | Block | N/A | Rule metadata description refined. Detection unchanged. |
| Cloudflare Free Ruleset | ...cfe1a93c | N/A | Wordpress - Remote Code Execution - CVE:CVE-2026-65640 | Block | N/A | Rule metadata description refined. Detection unchanged. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/#page","headline":"WAF Release - 2026-08-17","description":"Cloudflare WAF managed rulesets 2026-08-17 release","url":"https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/og.png?v=4a55f908350b97bb","dateModified":"2026-08-17","datePublished":"2026-08-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
