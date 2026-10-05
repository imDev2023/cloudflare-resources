---
description: Terraform v5.4.0 fixes a number of known bugs in the v5 Provider
title: Terraform v5.4.0 now available
image: https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/og.png?v=c2717fe966b833aa
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 6, 2025

## Terraform v5.4.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Removes the `worker_platforms_script_secret` resource from the provider (see [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret) for alternatives—applicable to both Workers and Workers for Platforms)
- Removes duplicated fields in `cloudflare_cloud_connector_rules` resource
- Fixes `cloudflare_workers_route` id issues [#5134 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134) [#5501 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501)
- Fixes issue around refreshing resources that have unsupported response types<details><summary>Affected resources</summary>

  - <code>cloudflare_certificate_pack</code>
  - <code>cloudflare_registrar_domain</code>
  - <code>cloudflare_stream_download</code>
  - <code>cloudflare_stream_webhook</code>
  - <code>cloudflare_user</code>
  - <code>cloudflare_workers_kv</code>
  - <code>cloudflare_workers_script</code></details>
- Fixes `cloudflare_workers_kv` state refresh issues
- Fixes issues around configurability of nested properties without computed values for the following resources<details><summary>Affected resources</summary>

  - <code>cloudflare_account</code>
  - <code>cloudflare_account_dns_settings</code>
  - <code>cloudflare_account_token</code>
  - <code>cloudflare_api_token</code>
  - <code>cloudflare_cloud_connector_rules</code>
  - <code>cloudflare_custom_ssl</code>
  - <code>cloudflare_d1_database</code>
  - <code>cloudflare_dns_record</code>
  - <code>email_security_trusted_domains</code>
  - <code>cloudflare_hyperdrive_config</code>
  - <code>cloudflare_keyless_certificate</code>
  - <code>cloudflare_list_item</code>
  - <code>cloudflare_load_balancer</code>
  - <code>cloudflare_logpush_dataset_job</code>
  - <code>cloudflare_magic_network_monitoring_configuration</code>
  - <code>cloudflare_magic_transit_site</code>
  - <code>cloudflare_magic_transit_site_lan</code>
  - <code>cloudflare_magic_transit_site_wan</code>
  - <code>cloudflare_magic_wan_static_route</code>
  - <code>cloudflare_notification_policy</code>
  - <code>cloudflare_pages_project</code>
  - <code>cloudflare_queue</code>
  - <code>cloudflare_queue_consumer</code>
  - <code>cloudflare_r2_bucket_cors</code>
  - <code>cloudflare_r2_bucket_event_notification</code>
  - <code>cloudflare_r2_bucket_lifecycle</code>
  - <code>cloudflare_r2_bucket_lock</code>
  - <code>cloudflare_r2_bucket_sippy</code>
  - <code>cloudflare_ruleset</code>
  - <code>cloudflare_snippet_rules</code>
  - <code>cloudflare_snippets</code>
  - <code>cloudflare_spectrum_application</code>
  - <code>cloudflare_workers_deployment</code>
  - <code>cloudflare_zero_trust_access_application</code>
  - <code>cloudflare_zero_trust_access_group</code></details>
- Fixed defaults that made `cloudflare_workers_script` fail when using Assets
- Fixed Workers Logpush setting in `cloudflare_workers_script` mistakenly being readonly
- Fixed `cloudflare_pages_project` broken when using "source"

The detailed [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0) is available on GitHub.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare), or by opening a [support ticket ↗︎](https://www.support.cloudflare.com/s/?language=en_US).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/#page","headline":"Terraform v5.4.0 now available","description":"Terraform v5.4.0 fixes a number of known bugs in the v5 Provider","url":"https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/og.png?v=c2717fe966b833aa","dateModified":"2025-05-06","datePublished":"2025-05-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
