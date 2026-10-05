---
description: Terraform v5.20.0 adds 24 new resources including Secrets Store, Zero Trust DLP classification, and Flagship feature flags, and bumps the Go SDK to cloudflare-go v7.
title: Terraform v5.20.0 now available
image: https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/og.png?v=685c047cbac3ca72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 12, 2026

## Terraform v5.20.0 now available

[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every [2-3 weeks ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.

#### New resources

- **cloudflare\_ai\_search\_namespace:** Manage AI Search namespaces
- **cloudflare\_custom\_csr:** Manage custom certificate signing requests
- **cloudflare\_dls\_prefix\_binding:** Manage DLS regional service prefix bindings
- **cloudflare\_flagship\_app:** Manage Flagship feature flag apps
- **cloudflare\_flagship\_flag:** Manage Flagship feature flags
- **cloudflare\_google\_tag\_gateway:** Manage Google Tag Gateway
- **cloudflare\_load\_balancer\_monitor\_group:** Manage load balancer monitor groups
- **cloudflare\_oauth\_client:** Manage IAM OAuth clients
- **cloudflare\_origin\_cloud\_region:** Manage origin cloud regions (v2 endpoints)
- **cloudflare\_secrets\_store:** Manage Secrets Store instances
- **cloudflare\_secrets\_store\_secret:** Manage Secrets Store secrets
- **cloudflare\_share:** Manage resource shares
- **cloudflare\_share\_recipient:** Manage share recipients
- **cloudflare\_share\_resource:** Manage shared resources
- **cloudflare\_zero\_trust\_device\_deployment\_groups:** Manage Zero Trust device deployment groups
- **cloudflare\_zero\_trust\_dlp\_data\_class:** Manage DLP data classes
- **cloudflare\_zero\_trust\_dlp\_data\_tag:** Manage DLP data tags
- **cloudflare\_zero\_trust\_dlp\_data\_tag\_category:** Manage DLP data tag categories
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_group:** Manage DLP sensitivity groups
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_level:** Manage DLP sensitivity levels
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_level\_order:** Manage DLP sensitivity level ordering
- **cloudflare\_zero\_trust\_resource\_library\_application:** Manage Zero Trust resource library applications
- **cloudflare\_zero\_trust\_resource\_library\_category:** Manage Zero Trust resource library categories
- **cloudflare\_zero\_trust\_tunnel\_warp\_connector\_config:** Manage WARP connector tunnel configurations

#### Features

- **cache:** add create (POST) method for smart\_tiered\_cache
- **cache:** update OPCR config to v2 endpoints
- **dlp:** promote classification Stainless config to main
- **dlp:** add custom prompt topics endpoint
- **email\_security\_block\_sender:** state upgrader for v4 to v5 migration
- **email\_security\_impersonation\_registry:** state upgrader for v4 to v5 migration
- **email\_security\_trusted\_domains:** state upgrader for v4 to v5 migration
- **snippets:** add Terraform `id_property` annotations for snippet and snippet\_rules
- bump Go SDK to cloudflare-go v7

#### Bug fixes

- **account\_member:** missing upgrade path from v5.0–v5.15
- **authenticated\_origin\_pulls\_settings:** nil pointer panic
- **bot\_management:** restore `content_bots_protection` handling in model.go
- **dns\_record:** prevent FQDN normalization from swallowing name shortening changes
- **list:** nullify empty nested objects to prevent inconsistent result after apply
- **load\_balancer\_pool:** accept early-v5 object-shape state at schema\_version=0
- **load\_balancer\_pool:** add `UseStateForUnknown` for `load_shedding` attribute to prevent drift
- **r2\_custom\_domain:** restore degraded-response handling in resource.go
- **regional\_hostname:** update cloudflare-go imports from v6 to v7
- **secrets\_store:** fix model/schema parity and guard acceptance tests
- **spectrum\_application:** accept early-v5 object-shape state at schema\_version=0
- **worker:** preserve `observability.traces.propagation_policy` across reads
- **worker:** add `propagation_policy` to observability defaults
- **worker\_version:** restore handwritten D1 `database_id` handling
- **workers\_custom\_domain:** missing `CertId` field in state migration
- **workers\_script:** restore annotations Read workaround stripped by codegen
- **zero\_trust\_access\_identity\_provider:** change `read_only` from computed to optional
- **zero\_trust\_access\_identity\_provider:** add `UseStateForUnknown` to SAML-only config fields
- **zero\_trust\_access\_identity\_provider:** use `UseNonNullStateForUnknown` on scim\_config fields
- **zero\_trust\_access\_policy:** populate `account_id` when migrating zone-scoped v4 state
- **zero\_trust\_access\_policy:** missing `common_names` transform in migration
- gracefully handle nil pointer dereference when config has `attributes_flat` during migration
- set initial schema version to 500 for all new resources

#### Refactors

Extracted `MoveState` nil guard into shared helper

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/#page","headline":"Terraform v5.20.0 now available","description":"Terraform v5.20.0 adds 24 new resources including Secrets Store, Zero Trust DLP classification, and Flagship feature flags, and bumps the Go SDK to cloudflare-go v7.","url":"https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/og.png?v=685c047cbac3ca72","dateModified":"2026-06-12","datePublished":"2026-06-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
