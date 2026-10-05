---
description: Cloudflare WAF managed rulesets 2026-04-15 release
title: WAF Release - 2026-04-15
image: https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/og.png?v=bea49d536ac1cca9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2026

## WAF Release - 2026-04-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces a new detection for a critical Remote Code Execution (RCE) vulnerability in Mesop (CVE-2026-33057), alongside protections for high-impact vulnerabilities in Cisco Secure Firewall Management Center (CVE-2026-20079) and FortiClient EMS (CVE-2026-21643). Additionally, this release includes an update to our existing React Server DoS coverage to address recently identified resource exhaustion vectors (CVE-2026-23869).

**Key Findings**

- Cisco Secure FMC (CVE-2026-20079): A vulnerability in the web-based management interface of Cisco Secure Firewall Management Center (FMC) that allows an unauthenticated, remote attacker to execute arbitrary commands or bypass security filters.
- FortiClient EMS (CVE-2026-21643): A critical vulnerability in the FortiClient EMS permitting unauthorized access or administrative configuration manipulation via crafted HTTP requests.
- Mesop (CVE-2026-33057): A vulnerability in the Mesop Python-based UI framework where unauthenticated attackers can execute arbitrary code by sending specially crafted, Base64-encoded payloads in the request body.

**Impact**

Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, gain administrative control over network management infrastructure, or trigger server-side resource exhaustion. Administrators are strongly encouraged to apply official vendor updates.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...aef9415b | N/A | Cisco Secure FMC - RCE via upgradeReadinessCall - CVE:CVE-2026-20079 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...ee7be621 | N/A | FortiClient EMS - Pre-Auth SQL Injection - CVE:CVE-2026-21643 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c953a72b | N/A | Mesop - Remote Code Execution - Base64 Payload - CVE:CVE-2026-33057 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...50c08f6f | N/A | React Server - DOS - CVE:CVE-2026-23864 - 1 - Beta | Log | Block | This rule has been merged into the original rule "React Server - DOS - CVE:CVE-2026-23864 - 1" (ID: ...61680354) |
| Cloudflare Managed Ruleset | ...ebd81645 | N/A | XSS, HTML Injection - Link Tag - URI (beta) | N/A | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...0af34bba | N/A | XSS, HTML Injection - Embed Tag - URI (beta) | N/A | Disabled | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/#page","headline":"WAF Release - 2026-04-15","description":"Cloudflare WAF managed rulesets 2026-04-15 release","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/og.png?v=bea49d536ac1cca9","dateModified":"2026-04-15","datePublished":"2026-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
