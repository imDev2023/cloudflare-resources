---
description: Terraform v5.14.0 stabilizes a number of resources and known issues
title: Terraform v5.14.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/og.png?v=4bb041b4fc486176
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 5, 2025

## Terraform v5.14.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.14 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Deprecation notice

Resource affected: `api_shield_discovery_operation`

Cloudflare continuously discovers and updates API endpoints and web assets of your web applications. To improve the maintainability of these dynamic resources, we are working on reducing the need to actively engage with discovered operations.

The corresponding public API endpoint of [discovered operations ↗︎](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/) is not affected and will continue to be supported.

#### Features

- **pages\_project**: Add v4 -> v5 migration tests ([#6506 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/pull/6506))

#### Bug fixes

- **account\_members**: Makes member policies a set ([#6488 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6488))
- **pages\_project**: Ensures non empty refresh plans ([#6515 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6515))
- **R2**: Improves sweeper ([#6512 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6512))
- **workers\_kv**: Ignores value import state for verify ([#6521 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6521))
- **workers\_script**: No longer treats the migrations attribute as WriteOnly ([#6489 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6489))
- **workers\_script**: Resolves resource drift when worker has unmanaged secret ([#6504 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6504))
- **zero\_trust\_device\_posture\_rule**: Preserves input.version and other fields ([#6500 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6500)) and ([#6503 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6503))
- **zero\_trust\_dlp\_custom\_profile**: Adds sweepers for `dlp_custom_profile`
- **zone\_subscription|account\_subscription**: Adds `partners_ent` as valid enum for `rate_plan.id` ([#6505 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6505))
- **zone**: Ensures datasource model schema parity ([#6487 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6487))
- **subscription**: Updates import signature to accept account\_id/subscription\_id to import account subscription ([#6510 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6510))

#### Upgrade to newer version

We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/#page","headline":"Terraform v5.14.0 now available","description":"Terraform v5.14.0 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/og.png?v=4bb041b4fc486176","dateModified":"2025-12-05","datePublished":"2025-12-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
