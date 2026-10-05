---
description: Cloudflare WAF managed rulesets 2026-07-14
title: WAF Release - 2026-07-14
image: https://developers.cloudflare.com/changelog/post/2026-07-14-waf-release/og.png?v=948e192742a6855a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 14, 2026

## WAF Release - 2026-07-14

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-14-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new rules targeting critical infrastructure vulnerabilities. These include an unauthenticated memory disclosure flaw in Citrix NetScaler ADC and Gateway (CVE-2026-8451) and a high-severity pre-authentication remote code execution (RCE) vulnerability in Progress Kemp LoadMaster (CVE-2026-8037).

**Key Findings**

- CVE-2026-8451: An insufficient input validation vulnerability affects Citrix NetScaler ADC and NetScaler Gateway appliances configured as a SAML Identity Provider (IdP). Remote, unauthenticated attackers can exploit this flaw by sending malformed requests to trigger a memory overread, allowing them to leak chunks of sensitive data from adjacent appliance memory.
- CVE-2026-8037: A critical OS command injection vulnerability in Progress Kemp LoadMaster load balancers allows unauthenticated remote attackers to achieve remote code execution (RCE).

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...76973ac4 | N/A | Citrix Netscaler ADC - Insufficient Input Validation - CVE:CVE-2026-8451 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...10233f36 | N/A | Progress Kemp LoadMaster - Remote Code Execution - CVE:CVE-2026-8037 | Log | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-14-waf-release/#page","headline":"WAF Release - 2026-07-14","description":"Cloudflare WAF managed rulesets 2026-07-14","url":"https://developers.cloudflare.com/changelog/post/2026-07-14-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-14-waf-release/og.png?v=948e192742a6855a","dateModified":"2026-07-14","datePublished":"2026-07-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
