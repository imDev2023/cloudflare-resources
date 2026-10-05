---
description: Cloudflare WAF managed rulesets 2025-09-15 release
title: WAF Release - 2025-09-15
image: https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/og.png?v=7d4372d0faa700e7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 15, 2025

## WAF Release - 2025-09-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week's focus highlights newly disclosed vulnerabilities in DevOps tooling, data visualization platforms, and enterprise CMS solutions. These issues include sensitive information disclosure and remote code execution, putting organizations at risk of credential leakage, unauthorized access, and full system compromise.

**Key Findings**

- Argo CD (CVE-2025-55190): Exposure of sensitive information could allow attackers to access credential data stored in configurations, potentially leading to compromise of Kubernetes workloads and secrets.
- DataEase (CVE-2025-57773): Insufficient input validation enables JNDI injection and insecure deserialization, resulting in remote code execution (RCE). Successful exploitation grants attackers control over the application server.
- Sitecore (CVE-2025-53694): A sensitive information disclosure flaw allows unauthorized access to confidential information stored in Sitecore deployments, raising the risk of data breaches and privilege escalation.

**Impact**

These vulnerabilities expose organizations to serious risks, including credential theft, unauthorized access, and full system compromise. Argo CD's flaw may expose Kubernetes secrets, DataEase exploitation could give attackers remote execution capabilities, and Sitecore's disclosure issue increases the likelihood of sensitive data leakage and business impact.

Administrators are strongly advised to apply vendor patches immediately, rotate exposed credentials, and review access controls to mitigate these risks.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2ee2085f | 100646 | Argo CD - Information Disclosure - CVE:CVE-2025-55190s | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f5e20788 | 100874 | DataEase - JNDI injection - CVE:CVE-2025-57773 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...005a12fd | 100880 | Sitecore - Information Disclosure - CVE:CVE-2025-53694 | Log | Block | This is a New Detection |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/#page","headline":"WAF Release - 2025-09-15","description":"Cloudflare WAF managed rulesets 2025-09-15 release","url":"https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/og.png?v=7d4372d0faa700e7","dateModified":"2025-09-15","datePublished":"2025-09-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
