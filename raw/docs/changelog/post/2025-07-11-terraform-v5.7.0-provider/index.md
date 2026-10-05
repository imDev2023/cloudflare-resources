---
description: Terraform v5.7.0 fixes a number of known bugs in the v5 Provider
title: Terraform v5.7.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/og.png?v=44f46e6f02774687
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 14, 2025

## Terraform v5.7.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.

Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Addressed permanent diff bug on Cloudflare Tunnel config
- State is now saved correctly for Zero Trust Access applications
- Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
- `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
- Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
- New resource:
  - `cloudflare_zero_trust_tunnel_warp_connector`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0) in GitHub.

#### Issues Closed

- [#5563: cloudflare\_logpull\_retention is missing import ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
- [#5608: cloudflare\_zero\_trust\_access\_policy in 5.5.0 provider gives error upon apply unexpected new value: .app\_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
- [#5612: data.cloudflare\_zero\_trust\_access\_applications does not exact match ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
- [#5532: cloudflare\_zero\_trust\_access\_identity\_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5662: cloudflare\_zero\_trust\_access\_policy does not support OIDC claims ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
- [#5565: Running Terraform with the cloudflare\_zero\_trust\_access\_policy resource results in updates on every apply, even when no changes are made - breaks idempotency ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
- [#5529: cloudflare\_zero\_trust\_access\_application: self hosted applications with private ips require public domain ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/#page","headline":"Terraform v5.7.0 now available","description":"Terraform v5.7.0 fixes a number of known bugs in the v5 Provider","url":"https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/og.png?v=44f46e6f02774687","dateModified":"2025-07-14","datePublished":"2025-07-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
