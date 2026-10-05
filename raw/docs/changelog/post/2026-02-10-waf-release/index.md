---
description: Cloudflare WAF managed rulesets 2026-02-10 release
title: WAF Release - 2026-02-10
image: https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/og.png?v=c81f9fdfa3beffbf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 10, 2026

## WAF Release - 2026-02-10

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...6aa0bef8 | N/A | Anomaly:Header:User-Agent - Fake Google Bot | Enabled | Disabled | We are changing the action for this rule from BLOCK to Disabled |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/#page","headline":"WAF Release - 2026-02-10","description":"Cloudflare WAF managed rulesets 2026-02-10 release","url":"https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/og.png?v=c81f9fdfa3beffbf","dateModified":"2026-02-10","datePublished":"2026-02-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
