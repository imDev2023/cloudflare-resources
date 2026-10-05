---
description: Cloudflare WAF managed rulesets 2025-11-24 release
title: WAF Release - 2025-11-24
image: https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/og.png?v=161ff75c9ee1381a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 24, 2025

## WAF Release - 2025-11-24

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.

**Key Findings**

This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the `CGIINFO` header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.

**Impact**

- FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated `CGIINFO` header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...4e2e1a2e | N/A | FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446 | Log | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...b6c44ed5 | N/A | PHP Wrapper Injection - Body - Beta | Log | Disabled | This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:...1a3e521e) |
| Cloudflare Managed Ruleset | ...900f4015 | N/A | PHP Wrapper Injection - URI - Beta | Log | Disabled | This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:...8f76bd74) |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/#page","headline":"WAF Release - 2025-11-24","description":"Cloudflare WAF managed rulesets 2025-11-24 release","url":"https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/og.png?v=161ff75c9ee1381a","dateModified":"2025-11-24","datePublished":"2025-11-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
