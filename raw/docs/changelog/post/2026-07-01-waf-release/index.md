---
description: Cloudflare WAF managed rulesets 2026-07-01
title: WAF Release - 2026-07-01
image: https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/og.png?v=1d25e0b37a76c6d1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## WAF Release - 2026-07-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.

**Key Findings**

- CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d84c92c9 | N/A | Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c12cf9c8 | N/A | Anomaly:Header:User-Agent - Fake Bing or MSN Bot | Enabled | Disabled | We are changing the action for this rule from BLOCK to Disabled |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/#page","headline":"WAF Release - 2026-07-01","description":"Cloudflare WAF managed rulesets 2026-07-01","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/og.png?v=1d25e0b37a76c6d1","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
