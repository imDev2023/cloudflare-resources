---
description: Improper drift detection in the Cloudflare Terraform Provider resulted in dozens of resources always indicating they needed to be updated or replaced.
title: Dozens of Cloudflare Terraform Provider resources now have proper drift detection
image: https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/og.png?v=9281d86b69486211
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 21, 2025

## Dozens of Cloudflare Terraform Provider resources now have proper drift detection

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your `terraform plan` to only show what resources are expected to change.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- API Shield
- Argo Smart Routing
- Argo Tiered Caching
- Bot Management
- BYOIP
- D1
- DNS
- Email Routing
- Hyperdrive
- Observatory
- Pages
- R2
- Rules
- SSL/TLS
- Waiting Room
- Workers
- Zero Trust

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/#page","headline":"Dozens of Cloudflare Terraform Provider resources now have proper drift detection","description":"Improper drift detection in the Cloudflare Terraform Provider resulted in dozens of resources always indicating they needed to be updated or replaced.","url":"https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/og.png?v=9281d86b69486211","dateModified":"2025-03-21","datePublished":"2025-03-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
