---
description: Cloudflare WAF managed rulesets 2026-09-30 release
title: WAF Release - 2026-09-30
image: https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/og.png?v=5a93ea2a4512f830
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## WAF Release - 2026-09-30

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new detections to enhance protection against a specific GitLab path traversal vulnerability, alongside advanced generic rules targeting HTTP request smuggling, directory traversal, and command injection attempts.

**Key Findings**

- CVE-2026-85706: A path traversal vulnerability affecting GitLab.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...cb14ded8 | N/A | Broken Access Control - Directory Traversal | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...0364bd7e | N/A | HTTP Request Smuggling - Request Body Anomaly - Beta | Log | Block | This rule is merged into the original rule "HTTP/2 Request Smuggling - Request Body Anomaly" (ID: ...1489d892). |
| Cloudflare Managed Ruleset | ...d498a69a | N/A | Command Injection - Generic 8 - body - Beta | Disabled | Disabled | This rule is merged into the original rule "Command Injection - Generic 8 - body" (ID: ...413592e2). |
| Cloudflare Managed Ruleset | ...87ae8cfc | N/A | GitLab - Path Traversal- CVE:CVE-2026-85706 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...549f7356 | N/A | Generic - Request routing cache inconsistency | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/#page","headline":"WAF Release - 2026-09-30","description":"Cloudflare WAF managed rulesets 2026-09-30 release","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/og.png?v=5a93ea2a4512f830","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
