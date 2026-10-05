---
description: Cloudflare WAF managed rulesets 2025-04-22 release
title: WAF Release - 2025-04-22
image: https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/og.png?v=dfb7224e4bb73f95
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 22, 2025

## WAF Release - 2025-04-22

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.

When deciding which exploits to tackle, Cloudflare tunes into the attackers' areas of focus. Cloudflare's network intelligence provides a unique lens into attacker activity – for instance, through the volume of blocked requests related with CVE exploits after updating WAF Managed Rules with new detections.

From this week's releases, one indicator that RCE is a "hot topic" attack type is the fact that the Oracle PeopleSoft RCE rule accounts for half of all of the new rule matches. This rule patches CVE-2023-22047, a high-severity vulnerability in the Oracle PeopleSoft suite that allows unauthenticated attackers to access PeopleSoft Enterprise PeopleTools data through remote code execution. This is particularly concerning because of the nature of the data managed by PeopleSoft – this can include payroll records or student profile information. This CVE, along with five others, are addressed with the latest detection update to WAF Managed Rules.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a5be3327 | 100738 | GitLab - Auth Bypass - CVE:CVE-2023-7028 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...6c9531fa | 100740 | Splunk Enterprise - Remote Code Execution - CVE:CVE-2025-20229 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f40bbc2b | 100741 | Oracle PeopleSoft - Remote Code Execution - CVE:CVE-2023-22047 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5462167c | 100742 | CrushFTP - Auth Bypass - CVE:CVE-2025-31161 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...caa7b208 | 100743 | Ivanti - Buffer Error - CVE:CVE-2025-22457 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d52139a8 | 100744 | Oracle Access Manager - Remote Code Execution - CVE:CVE-2021-35587 | Log | Disabled | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/#page","headline":"WAF Release - 2025-04-22","description":"Cloudflare WAF managed rulesets 2025-04-22 release","url":"https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/og.png?v=dfb7224e4bb73f95","dateModified":"2025-04-22","datePublished":"2025-04-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
