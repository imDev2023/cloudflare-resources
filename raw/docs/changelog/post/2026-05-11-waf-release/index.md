---
description: Cloudflare WAF managed rulesets 2026-05-11 release
title: WAF Release - 2026-05-11
image: https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/og.png?v=5719e728df1f34d9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 11, 2026

## WAF Release - 2026-05-11

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...68b3c389 | N/A | Remote Code Execution - Java Deserialization - Body - Beta | Block | Disabled | This is a new detection. This rule is merged into the original rule "Remote Code Execution - Java Deserialization" (ID: ...744305c4). |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/#page","headline":"WAF Release - 2026-05-11","description":"Cloudflare WAF managed rulesets 2026-05-11 release","url":"https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/og.png?v=5719e728df1f34d9","dateModified":"2026-05-11","datePublished":"2026-05-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
