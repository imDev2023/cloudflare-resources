---
description: Cloudflare WAF managed rulesets 2025-04-02 release
title: WAF Release - 2025-04-02
image: https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/og.png?v=79e7768ec2b14d6e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 2, 2025

## WAF Release - 2025-04-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...622f0483 | 100732 | Sitecore - Code Injection - CVE:CVE-2025-27218 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0f101cca | 100733 | Angular-Base64-Upload - Remote Code Execution - CVE:CVE-2024-42640 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...1bbcd247 | 100734 | Apache Camel - Remote Code Execution - CVE:CVE-2025-29891 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...90aea1ca | 100735 | Progress Software WhatsUp Gold - Remote Code Execution - CVE:CVE-2024-4885 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d9d8c5f2 | 100737 | Apache Tomcat - Remote Code Execution - CVE:CVE-2025-24813 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...a28a42c4 | 100659 | Common Payloads for Server-side Template Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...daa4b037 | 100659 | Common Payloads for Server-side Template Injection - Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...48f6a9cf | 100642 | LDAP Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...e0713e9f | 100642 | LDAP Injection Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...1bc977d1 | 100005 | DotNetNuke - File Inclusion - CVE:CVE-2018-9126, CVE:CVE-2011-1892, CVE:CVE-2022-31474 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...bb70a463 | 100527 | Apache Struts - CVE:CVE-2021-31805 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...0c99546a | 100702 | Command Injection - CVE:CVE-2022-24108 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...9a5581d0 | 100622C | Ivanti - Command Injection - CVE:CVE-2023-46805, CVE:CVE-2024-21887, CVE:CVE-2024-22024 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...06d0b009 | 100536C | GraphQL Command Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...1651d0c8 | 100536 | GraphQL Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...af00f61d | 100536A | GraphQL Introspection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...a41e5b67 | 100536B | GraphQL SSRF | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...433e5b3d | 100559A | Prototype Pollution - Common Payloads | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...4816b26f | 100559A | Prototype Pollution - Common Payloads - Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...fcea5ed2 | 100734 | Apache Camel - Remote Code Execution - CVE:CVE-2025-29891 | N/A | Disabled | N/A |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/#page","headline":"WAF Release - 2025-04-02","description":"Cloudflare WAF managed rulesets 2025-04-02 release","url":"https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/og.png?v=79e7768ec2b14d6e","dateModified":"2025-04-02","datePublished":"2025-04-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
