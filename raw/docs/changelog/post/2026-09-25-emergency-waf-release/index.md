---
description: Cloudflare WAF managed rulesets 2026-09-25 emergency release
title: WAF Release - 2026-09-25 - Emergency
image: https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/og.png?v=90b4741c3dcc79f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2026

## WAF Release - 2026-09-25 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This update provides immediate defense against critical vulnerabilities affecting WordPress and JFrog Artifactory, including path traversal, local file inclusion (LFI), cross-site scripting (XSS), and authentication bypass exploits.

**Key Findings**

- CVE-2026-87902: A high-severity Path Traversal and Local File Inclusion (LFI) vulnerability affecting WordPress. Unauthenticated attackers can exploit this flaw to read arbitrary files on the host server, potentially exposing sensitive configuration data or system files.
- CVE-2026-42018 & CVE-2026-82329: Critical authentication bypass vulnerabilities affecting JFrog Artifactory. Successful exploitation allows unauthenticated attackers to bypass security controls and achieve unauthorized access to the Artifactory instance.

**Impact**

We strongly recommend that administrators apply the latest vendor patches for WordPress and JFrog Artifactory to fully secure origin servers.

Detailed Rule Changes

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...70a43f96 | N/A | Wordpress - Path Traversal, Local File Inclusion - CVE:CVE-2026-87902 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...909a4db4 | N/A | Wordpress - XSS - Comment | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c797ef03 | N/A | JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-42018 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...a813ac74 | N/A | JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-82329 | N/A | Block | This is a new detection. |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/#page","headline":"WAF Release - 2026-09-25 - Emergency","description":"Cloudflare WAF managed rulesets 2026-09-25 emergency release","url":"https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/og.png?v=90b4741c3dcc79f4","dateModified":"2026-09-25","datePublished":"2026-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
