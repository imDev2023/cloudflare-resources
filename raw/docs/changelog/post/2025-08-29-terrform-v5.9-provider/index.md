---
description: Terraform v5.9 stabilizes a number of resources and known issues
title: Terraform v5.9 now available
image: https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/og.png?v=8ee7672de256963a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 29, 2025

## Terraform v5.9 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

This release includes a new resource, `cloudflare_snippet`, which replaces `cloudflare_snippets`. `cloudflare_snippet` is now considered deprecated but can still be used. Please utilize `cloudflare_snippet` as soon as possible.

#### Changes

- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes

For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0) in GitHub.

#### Issues Closed

- [#5921: In cloudflare\_ruleset removing an existing rule causes recreation of later rules ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare\_zero\_trust\_access\_application is not idempotent ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare\_workers\_script) Durable Object migrations not applied ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare\_workers\_script secret\_text environment variable gets replaced on every deploy ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare\_zone suddenly started showing drift ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare\_zero\_trust\_list always marked for change due to read only attributes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare\_zero\_trust\_gateway\_certificate unable to manage resource (cant mark as active/inactive) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare\_dns\_records is always updated in-place ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare\_zero\_trust\_gateway\_policy after upgrade to V5 provider & also setting expiration fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare\_zero\_trust\_access\_application ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare\_zone\_setting inconsistent value of "editable" upon apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare\_zero\_trust\_access\_policies" data source ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare\_zero\_trust\_access\_application type warp diff on every apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare\_zone\_dnssec fails with HTTP/400 "Malformed request body" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare\_ruleset http\_request\_cache\_settings bypass mismatch between dashboard and terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare\_account\_member invalid type 'string' for field 'roles' ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new issue if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [GitHub Repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/#page","headline":"Terraform v5.9 now available","description":"Terraform v5.9 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/og.png?v=8ee7672de256963a","dateModified":"2025-08-29","datePublished":"2025-08-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
