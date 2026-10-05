---
description: Cloudflare WAF managed rulesets 2026-03-12 emergency release
title: WAF Release - 2026-03-12 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/og.png?v=891b78aafeff72a3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 12, 2026

## WAF Release - 2026-03-12 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2026-1281 and CVE-2026-1340), alongside a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts within the `Content-Security-Policy` (CSP) HTTP request header.

**Key Findings**

- CVE-2026-1281 & CVE-2026-1340: Ivanti Endpoint Manager Mobile processes HTTP requests through Apache RevwriteMap directives that pass user-controlled input to Bash scripts ( `/mi/bin/map-appstore-url` and `/mi/bin/map-aft-store-url`). Bash scripts do not sanitize user input and are vulnerable to shell arithmetic expansion thereby allowing attackers to achieve unauthenticated remote code execution.
- Generic XSS in CSP Header: This rule identifies malicious payloads embedded within the request's `Content-Security-Policy` header. It specifically targets scenarios where web frameworks or applications trust and extract values directly from the CSP header in the incoming request without sufficient validation. Attackers can provide crafted header values to inject scripts or malicious directives that are subsequently processed by the server.

**Impact**

Successful exploitation of Ivanti EPMM vulnerability allows unauthenticated remote code execution and generic XSS in CSP header allows attackers to inject malicious scripts during page rendering. In environments using server-side caching, this poisoned XSS content can subsequently be cached and automatically served to all visitors.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...796ea2f6 | N/A | Ivanti EPMM - Code Injection - CVE:CVE-2026-1281 CVE:CVE-2026-1340 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...ee964a8c | N/A | Anomaly:Header:Content-Security-Policy | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/#page","headline":"WAF Release - 2026-03-12 - Emergency","description":"Cloudflare WAF managed rulesets 2026-03-12 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/og.png?v=891b78aafeff72a3","dateModified":"2026-03-12","datePublished":"2026-03-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
