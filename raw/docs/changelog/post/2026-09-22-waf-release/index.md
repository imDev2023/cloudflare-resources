---
description: Cloudflare WAF managed rulesets 2026-09-22 release
title: WAF Release - 2026-09-22
image: https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/og.png?v=15c0ec992ca3e37e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2026

## WAF Release - 2026-09-22

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new threat detections to enhance protection against Server-Side Request Forgery (SSRF) attempts using non-standard IP notations or jar loopback payloads, alongside new defenses against Server-Side Template Injection (SSTI) targeting Jinja environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...5f21b651 | N/A | SSRF - Cloud,Link-Local non-standard IP notation | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...0f0313d6 | N/A | SSRF - Block jar HTTP loopback payload | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...75cd912a | N/A | SSRF - Local non-standard IP notation | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...a1ba83f6 | N/A | SSTI - Jinja Dangerous Globals Chain | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/#page","headline":"WAF Release - 2026-09-22","description":"Cloudflare WAF managed rulesets 2026-09-22 release","url":"https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/og.png?v=15c0ec992ca3e37e","dateModified":"2026-09-22","datePublished":"2026-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
