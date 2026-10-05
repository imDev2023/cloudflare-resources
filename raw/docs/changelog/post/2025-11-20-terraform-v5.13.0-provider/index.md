---
description: Terraform v5.13.0 stabilizes a number of resources and known issues
title: Terraform v5.13.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/og.png?v=bb533385ab04f5d2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 20, 2025

## Terraform v5.13.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.

#### Breaking Change

Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.

For more specific information about the changes or the actions required, please see the [detailed Repository changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0).

#### Features

- **New resources and data sources added**
  - cloudflare\_connectivity\_directory
  - cloudflare\_sso\_connector
  - cloudflare\_universal\_ssl\_setting
- **api\_token+account\_tokens:** state upgrader and schema bump ([#6472 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472))
- **docs:** make docs explicit when a resource does not have import support
- **magic\_transit\_connector:** support self-serve license key ([#6398 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398))
- **worker\_version:** add content\_base64 support
- **worker\_version:** boolean support for run\_worker\_first ([#6407 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407))
- **workers\_script\_subdomains:** add import support ([#6375 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375))
- **zero\_trust\_access\_application:** add proxy\_endpoint for ZT Access Application ([#6453 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453))
- **zero\_trust\_dlp\_predefined\_profile:** Switch DLP Predefined Profile endpoints, introduce enabled\_entries attribute

#### Bug Fixes

- **account\_token:** token policy order and nested resources ([#6440 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440))
- allow r2\_bucket\_event\_notification to be applied twice without failing ([#6419 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419))
- **cloudflare\_worker+cloudflare\_worker\_version:** import for the resources ([#6357 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357))
- **dns\_record:** inconsistent apply error ([#6452 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452))
- **pages\_domain:** resource tests ([#6338 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338))
- **pages\_project:** unintended resource state drift ([#6377 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377))
- **queue\_consumer:** id population ([#6181 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181))
- **workers\_kv:** multipart request ([#6367 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367))
- **workers\_kv:** updating workers metadata attribute to be read from endpoint ([#6386 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386))
- **workers\_script\_subdomain:** add note to cloudflare\_workers\_script\_subdomain about redundancy with cloudflare\_worker ([#6383 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383))
- **workers\_script:** allow config.run\_worker\_first to accept list input
- **zero\_trust\_device\_custom\_profile\_local\_domain\_fallback:** drift issues ([#6365 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365))
- **zero\_trust\_device\_custom\_profile:** resolve drift issues ([#6364 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364))
- **zero\_trust\_dex\_test:** correct configurability for 'targeted' attribute to fix drift
- **zero\_trust\_tunnel\_cloudflared\_config:** remove warp\_routing from cloudflared\_config ([#6471 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471))

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more info

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/#page","headline":"Terraform v5.13.0 now available","description":"Terraform v5.13.0 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/og.png?v=bb533385ab04f5d2","dateModified":"2025-11-20","datePublished":"2025-11-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
