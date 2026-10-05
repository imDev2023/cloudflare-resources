---
description: Cloudflare WAF managed rulesets 2026-02-16 release
title: WAF Release - 2026-02-16
image: https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/og.png?v=8214e0416eb1bc80
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 16, 2026

## WAF Release - 2026-02-16

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.

**Key Findings**

- CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the `/h/rest` endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.
- CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via `?inline&import` when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...833761f7 | N/A | Zimbra - Local File Inclusion - CVE:CVE-2025-68645 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...950ed8c8 | N/A | Vite - WASM Import Path Traversal - CVE:CVE-2025-31125 | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/#page","headline":"WAF Release - 2026-02-16","description":"Cloudflare WAF managed rulesets 2026-02-16 release","url":"https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-16-waf-release/og.png?v=8214e0416eb1bc80","dateModified":"2026-02-16","datePublished":"2026-02-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
