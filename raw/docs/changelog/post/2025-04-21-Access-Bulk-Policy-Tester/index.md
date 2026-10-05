---
description: Test and simulate Access policies before deploying them to production. The Access bulk policy tester allows you to test your policies against your entire user population before and after deploying them.
title: Access bulk policy tester
image: https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/og.png?v=2566c369723212fa
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2025

## Access bulk policy tester

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Access bulk policy tester](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application) is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).

![Example policy tester](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1531,height=693,format=webp/_astro/example-policy-tester.DCY8hQvx.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/#page","headline":"Access bulk policy tester","description":"Test and simulate Access policies before deploying them to production. The Access bulk policy tester allows you to test your policies against your entire user population before and after deploying them.","url":"https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/og.png?v=2566c369723212fa","dateModified":"2025-04-21","datePublished":"2025-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
