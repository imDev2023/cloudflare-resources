---
description: Attack Signature Detection separates attack detection from mitigation and exposes signature match metadata for investigation and Security Rules.
title: Attack Signature Detection is now available in Early Access
image: https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/og.png?v=10af3d16f019b591
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 7, 2026

## Attack Signature Detection is now available in Early Access

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Attack Signature Detection is now available in Early Access. It evaluates requests against Cloudflare attack signatures and records matches without applying a mitigation action, allowing you to investigate detected traffic before deciding how to respond.

In **Security Analytics** > **Attack Analysis**, you can review matching signature references, categories, confidence levels, and request outcomes. You can then use these fields in [Security Rules](https://developers.cloudflare.com/security/rules/) and combine them with request properties such as hostname, path, and HTTP method to apply scoped mitigation.

Attack Signature Detection uses the same signature definitions as [Cloudflare Managed Rules](https://developers.cloudflare.com/waf/managed-rules/), but it does not inherit your Managed Rules actions, overrides, or deployment configuration. Managed Rules remain the recommended baseline protection during Early Access.

Contact your Cloudflare account team to request access. For more information, refer to [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/#page","headline":"Attack Signature Detection is now available in Early Access","description":"Attack Signature Detection separates attack detection from mitigation and exposes signature match metadata for investigation and Security Rules.","url":"https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/og.png?v=10af3d16f019b591","dateModified":"2026-09-07","datePublished":"2026-09-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
