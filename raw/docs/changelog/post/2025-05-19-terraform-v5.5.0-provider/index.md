---
description: Terraform v5.5.0 fixes a number of known bugs in the v5 Provider
title: Terraform v5.5.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/og.png?v=03182f98f09b309c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2025

## Terraform v5.5.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Broad fixes across resources with recurring diffs, including, but not limited to:
  - `cloudflare_zero_trust_gateway_policy`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_tunnel_cloudflared_route`
  - `cloudflare_zone_setting`
  - `cloudflare_ruleset`
  - `cloudflare_page_rule`
- Zone settings can be re-applied without client errors
- Page rules conversion errors are fixed
- Failure to apply changes to `cloudflare_zero_trust_tunnel_cloudflared_route`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0) in GitHub.

#### Issues Closed

- [#5304: Importing cloudflare\_zero\_trust\_gateway\_policy invalid attribute filter value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare\_page\_rule import does not set values for all of the fields in terraform state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare\_page\_rule Page rule creation with redirect fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare\_turnstile\_wwidget not able to update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare\_cloud\_connector\_rules: Provider returned invalid result object after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare\_zone\_setting: "Invalid value for zone setting always\_use\_https" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/#page","headline":"Terraform v5.5.0 now available","description":"Terraform v5.5.0 fixes a number of known bugs in the v5 Provider","url":"https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/og.png?v=03182f98f09b309c","dateModified":"2025-05-19","datePublished":"2025-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
