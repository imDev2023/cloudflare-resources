---
description: Cloudflare WAF managed rulesets 2026-02-02 release
title: WAF Release - 2026-02-02
image: https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/og.png?v=91eb5d6b697e3914
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 2, 2026

## WAF Release - 2026-02-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.

**Key Findings**

- CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the `Q()` class.
- CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...30698ff3 | N/A | XWiki - Remote Code Execution - CVE:CVE-2025-24893 2 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...da8ba7e6 | N/A | Django SQLI - CVE:CVE-2025-64459 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...8d667511 | N/A | NoSQL, MongoDB - SQLi - Comparison - 2 | Block | Block | Rule metadata description refined. Detection unchanged. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/#page","headline":"WAF Release - 2026-02-02","description":"Cloudflare WAF managed rulesets 2026-02-02 release","url":"https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/og.png?v=91eb5d6b697e3914","dateModified":"2026-02-02","datePublished":"2026-02-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
