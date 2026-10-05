---
description: Cloudflare WAF managed rulesets 2025-10-13 release
title: WAF Release - 2025-10-13
image: https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/og.png?v=4577ddd265adf90c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 13, 2025

## WAF Release - 2025-10-13

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.

**Key Findings**

New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.

**Impact**

- CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson `ObjectMapper` abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c04bab5f | 100892 | JinJava - SSTI - CVE:CVE-2025-59340 | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/#page","headline":"WAF Release - 2025-10-13","description":"Cloudflare WAF managed rulesets 2025-10-13 release","url":"https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/og.png?v=4577ddd265adf90c","dateModified":"2025-10-13","datePublished":"2025-10-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
