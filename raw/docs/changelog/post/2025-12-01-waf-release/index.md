---
description: Cloudflare WAF managed rulesets 2025-12-01 release
title: WAF Release - 2025-12-01
image: https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/og.png?v=ae15c89917650a6c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 1, 2025

## WAF Release - 2025-12-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for remote code execution attempts targeting Monsta FTP (CVE-2025-34299), alongside improvements to an existing XSS detection to enhance coverage.

**Key Findings**

- CVE-2025-34299 is a critical remote code execution flaw in Monsta FTP, arising from improper handling of user-supplied parameters within the file-handling interface. Certain builds allow crafted requests to bypass sanitization and reach backend PHP functions that execute arbitrary commands. Attackers can send manipulated parameters through the web panel to trigger command execution within the application’s runtime environment.

**Impact**

If exploited, the vulnerability enables full remote command execution on the underlying server, allowing takeover of the hosting environment, unauthorized file access, and potential lateral movement. As the flaw can be triggered without authentication on exposed Monsta FTP instances, it represents a severe risk for publicly reachable deployments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a4fcc8a8 | N/A | Monsta FTP - Remote Code Execution - CVE:CVE-2025-34299 | Log | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...b7492846 | N/A | XSS - JS Context Escape - Beta | Log | Block | This rule is merged into the original rule "XSS - JS Context Escape" (ID: ...7a3769d3) |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/#page","headline":"WAF Release - 2025-12-01","description":"Cloudflare WAF managed rulesets 2025-12-01 release","url":"https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/og.png?v=ae15c89917650a6c","dateModified":"2025-12-01","datePublished":"2025-12-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
