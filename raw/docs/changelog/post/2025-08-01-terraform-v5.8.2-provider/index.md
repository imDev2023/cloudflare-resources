---
description: Terraform v5.8.2 stabilizes a number of resources and known issues
title: Terraform v5.8.2 now available
image: https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/og.png?v=e94b77bc3ce01d1d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 1, 2025

## Terraform v5.8.2 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2) in GitHub.

#### Issues Closed

- [#5666: cloudflare\_ruleset example lists id which is a read-only field ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare\_logpush\_job plan always suggests changes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare\_list\_item would be recreated "created" state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare\_zone\_subscription: uses wrong ID field in Read/Update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare\_api\_token resource always shows changes (drift) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare\_workers\_script with bindings fails to be destroyed ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare\_workers\_script Unable to deploy worker assets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare\_workers\_script 500 internal server error when uploading python ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare\_workers\_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare\_workers\_script randomly fails to deploy when changing compatibility\_date ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare\_workers\_script (v5.2.0) ignoring content and bindings properties ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare\_workers\_script always detects changes after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare\_zero\_trust\_access\_identity\_provider gives recurring change on OTP pin login ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare\_r2\_custom\_domain doesn't roundtrip jurisdiction properly ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare\_api\_shield\_schema resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/#page","headline":"Terraform v5.8.2 now available","description":"Terraform v5.8.2 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/og.png?v=e94b77bc3ce01d1d","dateModified":"2025-08-01","datePublished":"2025-08-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
