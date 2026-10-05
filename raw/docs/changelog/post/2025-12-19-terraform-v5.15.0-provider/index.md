---
description: Terraform v5.15.0 stabilizes a number of resources and known issues
title: Terraform v5.15.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/og.png?v=37e6051e5da7ec60
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 19, 2025

## Terraform v5.15.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Features

- **ai\_search:** Add AI Search endpoints ([6f02adb ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915))
- **certificate\_pack:** Ensure proper Terraform resource ID handling for path parameters in API calls ([081f32a ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a))
- **worker\_version:** Support `startup_time_ms` ([286ab55 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba))
- **zero\_trust\_dlp\_custom\_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
- **zero\_trust\_dlp\_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
- **zero\_trust\_dlp\_integration\_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
- **zero\_trust\_dlp\_predefined\_entry:** Support `upload_status` ([7dc0fe3 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c))
- **zero\_trust\_gateway\_policy:** Support `forensic_copy` ([5741fd0 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b))
- **zero\_trust\_list:** Support additional types (category, location, device) ([5741fd0 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b))

#### Bug fixes

- **access\_rules:** Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. ([4457791 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d))
- **cloudflare\_pages\_project:** Addressing drift issues ([6edffcf ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e)) ([3db318e ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0))
- **cloudflare\_worker:** Can be cleanly imported ([4859b52 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f))
- **cloudflare\_worker:** Ensure clean imports ([5b525bc ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a))
- **list\_items:** Add validation for IP List items to avoid inconsistent state ([b6733dc ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada))
- **zero\_trust\_access\_application:** Remove all conditions from sweeper ([3197f1a ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7))
- **spectrum\_application:** Map missing fields during spectrum resource import ([#6495 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495)) ([ddb4e72 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa))

#### Upgrade to newer version

We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/#page","headline":"Terraform v5.15.0 now available","description":"Terraform v5.15.0 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/og.png?v=37e6051e5da7ec60","dateModified":"2025-12-19","datePublished":"2025-12-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
