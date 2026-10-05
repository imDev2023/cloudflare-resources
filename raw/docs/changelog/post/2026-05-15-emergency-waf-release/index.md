---
description: Cloudflare WAF managed rulesets 2026-05-15 emergency release
title: WAF Release - 2026-05-15 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/og.png?v=349680d1622fe7d6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 15, 2026

## WAF Release - 2026-05-15 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's `is_args` stale-state bug (CVE-2026-42945).

**Key Findings**

CVE-2026-42945: nginx Heap Buffer Overflow via Stale `is_args` in Rewrite Module

Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in `ngx_http_script_copy_capture_code()` causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.

We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid `rewrite` directives with `?` in the replacement string followed by `set` or `if` referencing capture groups.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...7e52be73 | N/A | nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...9df0ee6c | N/A | nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/#page","headline":"WAF Release - 2026-05-15 - Emergency","description":"Cloudflare WAF managed rulesets 2026-05-15 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/og.png?v=349680d1622fe7d6","dateModified":"2026-05-15","datePublished":"2026-05-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
