---
description: Cloudflare WAF managed rulesets 2026-08-07 release
title: WAF Release - 2026-08-07
image: https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/og.png?v=06bccb66cf838486
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2026

## WAF Release - 2026-08-07

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release updates WordPress XSS rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify XSS2Shell (CVE-2026-64638). It also disables the Command Injection - Obfuscation rule.

**Key Findings**

- CVE-2026-64638: A pre-authentication reflected cross-site scripting vulnerability affecting the WordPress login screen. Exploitation requires social engineering and explicit interaction by the target user. Under additional conditions, it may be escalated to remote code execution.

**Impact**

The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...9c6dff1c | N/A | Wordpress - XSS - CVE:CVE-2026-64638 | Block | N/A | Rule metadata description refined. Detection unchanged. |
| Cloudflare Free Ruleset | ...9ab5ed95 | N/A | Wordpress - XSS - CVE:CVE-2026-64638 | Block | N/A | Rule metadata description refined. Detection unchanged. |
| Cloudflare Managed Ruleset | ...761e7a4c | N/A | Command Injection - Obfuscation | Block | Disabled | Detection logic has been deprecated |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/#page","headline":"WAF Release - 2026-08-07","description":"Cloudflare WAF managed rulesets 2026-08-07 release","url":"https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/og.png?v=06bccb66cf838486","dateModified":"2026-08-07","datePublished":"2026-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
