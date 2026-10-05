---
description: We are changing the maximum request-payload size inspected by the Cloudflare WAF
title: Updating the WAF maximum payload values
image: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/og.png?v=9136cebe879d144e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 5, 2025

## Updating the WAF maximum payload values

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are reinstating the maximum request-payload size the Cloudflare WAF inspects, with WAF on Enterprise zones inspecting up to 128 KB.

**Key Findings**

On [December 5, 2025](https://developers.cloudflare.com/changelog/2025-12-05-rcs-vuln/), we initially attempted to increase the maximum WAF payload limit to 1 MB across all plans. However, an automatic rollout for all customers proved impractical because the increase led to a surge in false positives for existing managed rules.

This issue was particularly notable within the Cloudflare Managed Ruleset and the Cloudflare OWASP Core Ruleset, impacting customer traffic.

**Impact**

Customers on paid plans can increase the limit to 1 MB for any of their zones by contacting Cloudflare Support. Free zones are already protected up to 1 MB and do not require any action.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/#page","headline":"Updating the WAF maximum payload values","description":"We are changing the maximum request-payload size inspected by the Cloudflare WAF","url":"https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/og.png?v=9136cebe879d144e","dateModified":"2025-12-05","datePublished":"2025-12-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
