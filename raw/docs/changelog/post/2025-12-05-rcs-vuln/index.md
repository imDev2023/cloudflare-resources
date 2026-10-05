---
description: Updating WAF to run on requests body of up to 1 MB
title: Increased WAF payload limit for all plans
image: https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/og.png?v=b31ab128a00840de
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 5, 2025

## Increased WAF payload limit for all plans

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAF now inspects request-payload size of up to 1 MB across all plans to enhance our detection capabilities for React RCE (CVE-2025-55182).

**Key Findings**

React payloads commonly have a default maximum size of 1 MB. Cloudflare WAF previously inspected up to 128 KB on Enterprise plans, with even lower limits on other plans.

**Update:** We later reinstated the maximum request-payload size the Cloudflare WAF inspects. Refer to [Updating the WAF maximum payload values](https://developers.cloudflare.com/changelog/2025-12-05-waf-max-payload-size-change/) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/#page","headline":"Increased WAF payload limit for all plans","description":"Updating WAF to run on requests body of up to 1 MB","url":"https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/og.png?v=b31ab128a00840de","dateModified":"2025-12-05","datePublished":"2025-12-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
