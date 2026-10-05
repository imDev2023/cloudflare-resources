---
description: Cloudflare WAF managed rulesets 2026-03-02 release
title: WAF Release - 2026-03-02
image: https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/og.png?v=070b889379921569
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 2, 2026

## WAF Release - 2026-03-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for vulnerabilities in SmarterTools SmarterMail (CVE-2025-52691 and CVE-2026-23760), alongside improvements to an existing Command Injection (nslookup) detection to enhance coverage.

**Key Findings**

- CVE-2025-52691: SmarterTools SmarterMail mail server is vulnerable to Arbitrary File Upload, allowing an unauthenticated attacker to upload files to any location on the mail server, potentially enabling remote code execution.
- CVE-2026-23760: SmarterTools SmarterMail versions prior to build 9511 contain an authentication bypass vulnerability in the password reset API permitting unaunthenticated to reset system administrator accounts failing to verify existing password or reset token.

**Impact**

Successful exploitation of these SmarterMail vulnerabilities could lead to full system compromise or unauthorized administrative access to mail servers. Administrators are strongly encouraged to apply vendor patches without delay.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...966ec6b1 | N/A | SmarterMail - Arbitrary File Upload - CVE-2025-52691 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...ee964a8c | N/A | SmarterMail - Authentication Bypass - CVE-2026-23760 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...75b64d99 | N/A | Command Injection - Nslookup - Beta | Log | Block | This rule is merged into the original rule "Command Injection - Nslookup" (ID: ...b090ba9a) |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/#page","headline":"WAF Release - 2026-03-02","description":"Cloudflare WAF managed rulesets 2026-03-02 release","url":"https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/og.png?v=070b889379921569","dateModified":"2026-03-02","datePublished":"2026-03-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
