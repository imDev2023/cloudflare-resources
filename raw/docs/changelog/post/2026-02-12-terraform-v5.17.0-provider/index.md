---
description: Terraform v5.17.0 adds AI Search support, improves Workers Script placement, and includes state upgraders for smooth migrations
title: Terraform v5.17.0 now available
image: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/og.png?v=02be38a9aec8772c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2026

## Terraform v5.17.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we have established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to help you migrate from v4 to v5 with ease.

This release brings new capabilities for AI Search, enhanced Workers Script placement controls, and numerous bug fixes based on community feedback. We also begun laying foundational work for improving the v4 to v5 migration process. Stay tuned for more details as we approach the March 2026 release timeline.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

#### Features

- **ai\_search\_instance:** add data source for querying AI Search instances
- **ai\_search\_token:** add data source for querying AI Search tokens
- **account:** add support for tenant unit management with new `unit` field
- **account:** add automatic mapping from `managed_by.parent_org_id` to `unit.id`
- **authenticated\_origin\_pulls\_certificate:** add data source for querying authenticated origin pull certificates
- **authenticated\_origin\_pulls\_hostname\_certificate:** add data source for querying hostname-specific authenticated origin pull certificates
- **authenticated\_origin\_pulls\_settings:** add data source for querying authenticated origin pull settings
- **workers\_kv:** add `value` field to data source to retrieve KV values directly
- **workers\_script:** add `script` field to data source to retrieve script content
- **workers\_script:** add support for `simple` rate limit binding
- **workers\_script:** add support for targeted placement mode with `placement.target` array for specifying placement targets (region, hostname, host)
- **workers\_script:** add `placement_mode` and `placement_status` computed fields
- **zero\_trust\_dex\_test:** add data source with filter support for finding specific tests
- **zero\_trust\_dlp\_predefined\_profile:** add `enabled_entries` field for flexible entry management

#### Bug Fixes

- **account:** map `managed_by.parent_org_id` to `unit.id` in unmarshall and add acceptance tests
- **authenticated\_origin\_pulls\_certificate:** add certificate normalization to prevent drift
- **authenticated\_origin\_pulls:** handle array response and implement full lifecycle
- **authenticated\_origin\_pulls\_hostname\_certificate:** fix resource and tests
- **cloudforce\_one\_request\_message:** use correct `request_id` field instead of `id` in API calls
- **dns\_zone\_transfers\_incoming:** use correct `zone_id` field instead of `id` in API calls
- **dns\_zone\_transfers\_outgoing:** use correct `zone_id` field instead of `id` in API calls
- **email\_routing\_settings:** use correct `zone_id` field instead of `id` in API calls
- **hyperdrive\_config:** add proper handling for write-only fields to prevent state drift
- **hyperdrive\_config:** add normalization for empty `mtls` objects to prevent unnecessary diffs
- **magic\_network\_monitoring\_rule:** use correct `account_id` field instead of `id` in API calls
- **mtls\_certificates:** fix resource and test
- **pages\_project:** revert build\_config to computed optional
- **stream\_key:** use correct `account_id` field instead of `id` in API calls
- **total\_tls:** use upsert pattern for singleton zone setting
- **waiting\_room\_rules:** use correct `waiting_room_id` field instead of `id` in API calls
- **workers\_script:** add support for placement mode/status
- **zero\_trust\_access\_application:** update v4 version on migration tests
- **zero\_trust\_device\_posture\_rule:** update tests to match API
- **zero\_trust\_dlp\_integration\_entry:** use correct `entry_id` field instead of `id` in API calls
- **zero\_trust\_dlp\_predefined\_entry:** use correct `entry_id` field instead of `id` in API calls
- **zero\_trust\_organization:** fix plan issues

#### Chores

- add state upgraders to 95+ resources to lay the foundation for replacing Grit (still under active development)
- **certificate\_pack:** add state migration handler for SDKv2 to Framework conversion
- **custom\_hostname\_fallback\_origin:** add comprehensive lifecycle test and migration support
- **dns\_record:** add state migration handler for SDKv2 to Framework conversion
- **leaked\_credential\_check:** add import functionality and tests
- **load\_balancer\_pool:** add state migration handler with detection for v4 vs v5 format
- **pages\_project:** add state migration handlers
- **tiered\_cache:** add state migration handlers
- **zero\_trust\_dlp\_predefined\_profile:** deprecate `entries` field in favor of `enabled_entries`

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/#page","headline":"Terraform v5.17.0 now available","description":"Terraform v5.17.0 adds AI Search support, improves Workers Script placement, and includes state upgraders for smooth migrations","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/og.png?v=02be38a9aec8772c","dateModified":"2026-02-12","datePublished":"2026-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
