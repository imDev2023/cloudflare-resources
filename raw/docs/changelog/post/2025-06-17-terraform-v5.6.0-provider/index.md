---
description: Terraform v5.6.0 fixes a number of known bugs in the v5 Provider
title: Terraform v5.6.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/og.png?v=680c24f0c60cfda5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 17, 2025

## Terraform v5.6.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Broad fixes across resources with recurring diffs, including, but not limited to:
  - `cloudflare_zero_trust_access_identity_provider`
    - `cloudflare_zone`
- `cloudflare_page_rules` runtime panic when setting `cache_level` to `cache_ttl_by_status`
- Failure to serialize requests in `cloudflare_zero_trust_tunnel_cloudflared_config`
- Undocumented field 'priority' on `zone_lockdown` resource
- Missing importability for `cloudflare_zero_trust_device_default_profile_local_domain_fallback` and `cloudflare_account_subscription`
- New resources:
  - `cloudflare_schema_validation_operation_settings`
  - `cloudflare_schema_validation_schemas`
  - `cloudflare_schema_validation_settings`
  - `cloudflare_zero_trust_device_settings`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0) in GitHub.

#### Issues Closed

- [#5098: 500 Server Error on updating 'zero\_trust\_tunnel\_cloudflared\_virtual\_network' Terraform resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
- [#5148: cloudflare\_user\_agent\_blocking\_rule doesn’t actually support user agents ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
- [#5472: cloudflare\_zone showing changes in plan after following upgrade steps ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
- [#5508: cloudflare\_zero\_trust\_tunnel\_cloudflared\_config failed to serialize http request ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
- [#5509: cloudflare\_zone: Problematic Terraform behaviour with paused zones ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
- [#5520: Resource 'cloudflare\_magic\_wan\_static\_route' is not working ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
- [#5524: Optional fields cause crash in cloudflare\_zero\_trust\_tunnel\_cloudflared(s) when left null ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
- [#5526: Provider v5 migration issue: no import method for cloudflare\_zero\_trust\_device\_default\_profile\_local\_domain\_fallback ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
- [#5532: cloudflare\_zero\_trust\_access\_identity\_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5561: cloudflare\_zero\_trust\_tunnel\_cloudflared: cannot rotate tunnel secret ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
- [#5569: cloudflare\_zero\_trust\_device\_custom\_profile\_local\_domain\_fallback not allowing multiple DNS Server entries ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
- [#5577: Panic modifying page\_rule resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
- [#5653: cloudflare\_zone\_setting resource schema confusion in 5.5.0: value vs enabled ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/#page","headline":"Terraform v5.6.0 now available","description":"Terraform v5.6.0 fixes a number of known bugs in the v5 Provider","url":"https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/og.png?v=680c24f0c60cfda5","dateModified":"2025-06-17","datePublished":"2025-06-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
