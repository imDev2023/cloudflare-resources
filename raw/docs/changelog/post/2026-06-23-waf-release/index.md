---
description: Cloudflare WAF managed rulesets 2026-06-23
title: WAF Release - 2026-06-23
image: https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/og.png?v=5fbdbf937de6d8fc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 23, 2026

## WAF Release - 2026-06-23

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new managed protection to address a critical pre-authentication OS command injection vulnerability in Ivanti Sentry (CVE-2026-10520).

**Key Findings**

- CVE-2026-10520: An OS command injection vulnerability in Ivanti Sentry allows remote, unauthenticated attackers to execute arbitrary system commands with root privileges. The flaw stems from improper sanitization of input strings parsed during internal configuration handling.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...242fdf83 | N/A | Ivanti Sentry - Command Injection - CVE:CVE-2026-10520 | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/#page","headline":"WAF Release - 2026-06-23","description":"Cloudflare WAF managed rulesets 2026-06-23","url":"https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-23-waf-release/og.png?v=5fbdbf937de6d8fc","dateModified":"2026-06-23","datePublished":"2026-06-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
