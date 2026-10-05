---
title: Terraform Changelog
image: https://developers.cloudflare.com/og-changelog.png
---

[Skip to content](#main-content)

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

Jun 12, 2026

[<h2>Terraform v5.20.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/)

[Terraform](https://developers.cloudflare.com/terraform/)

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

Apr 24, 2026

[<h2>Terraform v5.19.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/)

[Terraform](https://developers.cloudflare.com/terraform/)

Terraform Provider v5.19.0 introduces 14 new resources spanning AI Gateway, Pipelines, R2 Data Catalog, User Groups, Vulnerability Scanner, Workers Observability, and Zero Trust capabilities. This release significantly improves the v4 to v5 migration experience with automatic state upgraders for 26 resources, working seamlessly with the new [tf-migrate CLI tool ↗︎](https://github.com/cloudflare/tf-migrate) to automate resource renames, attribute updates, and `moved` block generation. Together, these enhancements reduce manual migration effort and minimize risk when upgrading from v4 to v5.

**Note:** `cmd/migrate` is deprecated in favor of `tf-migrate` and will be removed in a future release ([#7062 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/pull/7062))

#### New Resources

- **cloudflare\_ai\_gateway**: Manage AI Gateway instances
- **cloudflare\_certificate\_authorities\_hostname\_associations**: Manage mTLS certificate hostname associations
- **cloudflare\_custom\_page\_asset**: Manage custom page assets
- **cloudflare\_pipeline**: Manage Cloudflare Pipelines
- **cloudflare\_r2\_data\_catalog**: Manage R2 Data Catalog
- **cloudflare\_user\_group**: Manage user groups
- **cloudflare\_user\_group\_members**: Manage user group memberships
- **cloudflare\_vulnerability\_scanner\_credential**: Manage vulnerability scanner credentials
- **cloudflare\_vulnerability\_scanner\_credential\_set**: Manage vulnerability scanner credential sets
- **cloudflare\_vulnerability\_scanner\_target\_environment**: Manage vulnerability scanner target environments
- **cloudflare\_workers\_observability\_destination**: Manage Workers Observability destinations
- **cloudflare\_zero\_trust\_device\_ip\_profile**: Manage Zero Trust device IP profiles
- **cloudflare\_zero\_trust\_device\_subnet**: Manage Zero Trust device subnets
- **cloudflare\_zero\_trust\_dlp\_settings**: Manage Zero Trust DLP settings

#### Features

#### V4 to V5 Migration State Upgraders

State upgraders added for seamless migration from v4 to v5 for the following resources:

- account
- account\_member
- account\_token
- authenticated\_origin\_pulls
- authenticated\_origin\_pulls\_hostname\_certificate
- byo\_ip\_prefix
- custom\_hostname
- custom\_ssl
- leaked\_credential\_check
- leaked\_credential\_check\_rule
- logpush\_ownership\_challenge
- mtls\_certificate
- observatory\_scheduled\_test
- pages\_domain
- regional\_tiered\_cache
- turnstile\_widget
- workers\_custom\_domain
- zero\_trust\_device\_custom\_profile
- zero\_trust\_device\_default\_profile
- zero\_trust\_device\_posture\_integration
- zero\_trust\_gateway\_certificate
- zero\_trust\_gateway\_settings
- zero\_trust\_organization
- zero\_trust\_tunnel\_cloudflared\_virtual\_network
- zone\_setting

#### Other Features

- **ruleset**: Add `content_converter` and `redirects_for_ai_training` support to configuration rules
- **zero\_trust\_gateway\_logging**: Make importable

#### Bug Fixes

#### Migration & State Management

- **account\_member**: Add UseStateForUnknown to status field to prevent drift
- **authenticated\_origin\_pulls\_settings**: Fix no prior schema and no-op upgrade
- **certificate\_pack**: Initialize empty lists instead of null in state upgrader to prevent drift
- **migrations**: Handle ambiguous schema\_version state for v4/v5 coexistence
- **zero\_trust\_access\_policy**: Fix nil pointer panic in state upgrader; set PriorSchema nil for v4 state upgrade

#### Resource-Specific Fixes

- **ai\_search\_instance**: Restore original defaults for cache and cache\_threshold; conflict resolution
- **apijson**: Return empty object from MarshalForPatch when no fields are serializable
- **dlp\_predefined\_profile**: Eliminate perpetual entries and enabled\_entries drift
- **dns\_record**: Avoid unnecessary drift for ipv4\_only and ipv6\_only attributes; remove private\_routing default value
- **drift**: Preserve prior state values for optional fields not returned by API
- **healthcheck**: Use buildHealthcheckPlanChecks helper for correct plan checks per migration source; update assertions
- **leaked\_credential\_check\_rule**: Handle empty ID from v4 provider state migration
- **list\_item**: Remove context
- **logpush\_job**: Update model for migration
- **ruleset**: Fix migration; add redirects\_for\_ai\_training to SourceV4ActionParametersModel; fix duplicate model attribute
- **worker**: Add UseStateForUnknown() plan modifiers and update tests for observability.traces
- **workers\_custom\_domain**: Handle HTTP 200 no content header; update assertions
- **workers\_script**: Fix model drift
- **zero\_trust\_access\_identity\_provider**: Fix boolean drifts
- **zero\_trust\_device\_managed\_networks**: Upgrade resource state
- **zero\_trust\_gateway\_policy**: Make filters Computed+Optional to prevent drift
- **zero\_trust\_gateway\_settings**: Fix breaking changes; implement sweeper to reset account to clean defaults
- **zone\_setting**: Migration test improvements and fixes

#### Documentation

- **healthcheck**: Update port description to clarify defaults
- Add application-scoped access policy migration guidance
- Update zone\_settings\_override migration guide for tf-migrate v2 workflow

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Apr 24, 2026

[<h2>Automate migration from Cloudflare's Terraform v4 to v5 provider</h2>](https://developers.cloudflare.com/changelog/post/2026-04-24-tf-migrate-tool-released/)

[Terraform](https://developers.cloudflare.com/terraform/)

We're excited to announce **tf-migrate**, a purpose-built CLI tool that simplifies migrating from Cloudflare Terraform Provider v4 to v5.

#### v5 is stable and ready for production

**Terraform Provider v5 is stable and actively receiving updates.** We encourage all users to migrate to v5 to take advantage of ongoing enhancements and new capabilities.

Cloudflare uses tf-migrate to migrate our own infrastructure — the same tool we're providing to the community — ensuring the best possible migration experience.

#### What tf-migrate does

**tf-migrate** automates the tedious and error-prone parts of the v4 to v5 migration process:

- **Resource type renames** – Automatically updates `cloudflare_record` → `cloudflare_dns_record`, `cloudflare_access_application` → `cloudflare_zero_trust_access_application`, and 40+ other renamed resources
- **Attribute transformations** – Updates field names (e.g., `value` → `content` for DNS records) and restructures nested blocks
- **Moved block generation** – Creates Terraform 1.8+ `moved` blocks to prevent resource replacements and ensure zero-downtime migrations
- **Cross-file reference updates** – Automatically finds and updates all references to renamed resources across your entire configuration
- **Dry-run mode** – Preview all changes before applying them to ensure safety

Combined with the automatic state upgraders introduced in v5.19+, tf-migrate eliminates the manual work and risk that previously made v5 migrations challenging. Tf-migrate operates directly on the config, and the built-in state upgraders handle the rest.

#### Supported resources

Tf-migrate currently supports the most common Terraform resources our customers use. We are actively working to expand coverage, with the most commonly used resources prioritized first.

For the complete list of supported resources and their migration status, refer to the [v5 Stabilization Tracker ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). This list is updated regularly as additional resources are stabilized and migration support is added.

Resources not yet supported by tf-migrate will need to be migrated manually using the [version 5 upgrade guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). The upgrade guide provides step-by-step instructions for handling resource renames, attribute changes, and state migrations.

#### Get started

- [Download tf-migrate ↗︎](https://github.com/cloudflare/tf-migrate/releases)
- [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Terraform Provider documentation ↗︎](https://developers.cloudflare.com/terraform/)
- [v5 Stabilization Tracker ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

We have been releasing Betas over the past month and a half while testing this tool. See the full changelog of those Betas here: [tf-migrate releases ↗︎](https://github.com/cloudflare/tf-migrate/releases).

Feb 12, 2026

[<h2>Terraform v5.17.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Jan 20, 2026

[<h2>Terraform v5.16.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Features

- **custom\_pages:** add "waf\_challenge" as new supported error page type identifier in both resource and data source schemas
- **list:** enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6
- **magic\_wan\_gre\_tunnel:** add automatic\_return\_routing attribute for automatic routing control
- **magic\_wan\_gre\_tunnel:** add BGP configuration support with new BGP model attribute
- **magic\_wan\_gre\_tunnel:** add bgp\_status computed attribute for BGP connection status information
- **magic\_wan\_gre\_tunnel:** enhance schema with BGP-related attributes and validators
- **magic\_wan\_ipsec\_tunnel:** add automatic\_return\_routing attribute for automatic routing control
- **magic\_wan\_ipsec\_tunnel:** add BGP configuration support with new BGP model attribute
- **magic\_wan\_ipsec\_tunnel:** add bgp\_status computed attribute for BGP connection status information
- **magic\_wan\_ipsec\_tunnel:** add custom\_remote\_identities attribute for custom identity configuration
- **magic\_wan\_ipsec\_tunnel:** enhance schema with BGP and identity-related attributes
- **ruleset:** add request body buffering support
- **ruleset:** enhance ruleset data source with additional configuration options
- **workers\_script:** add observability logs attributes to list data source model
- **workers\_script:** enhance list data source schema with additional configuration options

#### Bug Fixes

- **account\_member**: fix resource importability issues
- **dns\_record:** remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function
- **load\_balancer:** fix session\_affinity\_ttl type expectations to match Float64 in initial creation and Int64 after migration
- **workers\_kv:** handle special characters correctly in URL encoding

#### Documentation

- **account\_subscription:** update schema description for rate\_plan.sets attribute to clarify it returns an array of strings
- **api\_shield:** add resource-level description for API Shield management of auth ID characteristics
- **api\_shield:** enhance auth\_id\_characteristics.name attribute description to include JWT token configuration format requirements
- **api\_shield:** specify JSONPath expression format for JWT claim locations
- **hyperdrive\_config:** add description attribute to name attribute explaining its purpose in dashboard and API identification
- **hyperdrive\_config:** apply description improvements across resource, data source, and list data source schemas
- **hyperdrive\_config:** improve schema descriptions for cache settings to clarify default values
- **hyperdrive\_config:** update port description to clarify defaults for different database types

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

Dec 19, 2025

[<h2>Terraform v5.15.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Dec 5, 2025

[<h2>Terraform v5.14.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Nov 20, 2025

[<h2>Terraform v5.13.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure its stability and reliability, including the v5.13 release. We have also pivoted from an [issue-to-issue approach to a resource-per-resource approach ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes new features, new resources and data sources, bug fixes, updates to our Developer Documentation, and more.

#### Breaking Change

Please be aware that there are breaking changes for the `cloudflare_api_token` and `cloudflare_account_token` resources. These changes eliminate configuration drift caused by policy ordering differences in the Cloudflare API.

For more specific information about the changes or the actions required, please see the [detailed Repository changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.13.0).

#### Features

- **New resources and data sources added**
  - cloudflare\_connectivity\_directory
  - cloudflare\_sso\_connector
  - cloudflare\_universal\_ssl\_setting
- **api\_token+account\_tokens:** state upgrader and schema bump ([#6472 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6472))
- **docs:** make docs explicit when a resource does not have import support
- **magic\_transit\_connector:** support self-serve license key ([#6398 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6398))
- **worker\_version:** add content\_base64 support
- **worker\_version:** boolean support for run\_worker\_first ([#6407 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6407))
- **workers\_script\_subdomains:** add import support ([#6375 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6375))
- **zero\_trust\_access\_application:** add proxy\_endpoint for ZT Access Application ([#6453 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6453))
- **zero\_trust\_dlp\_predefined\_profile:** Switch DLP Predefined Profile endpoints, introduce enabled\_entries attribute

#### Bug Fixes

- **account\_token:** token policy order and nested resources ([#6440 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6440))
- allow r2\_bucket\_event\_notification to be applied twice without failing ([#6419 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6419))
- **cloudflare\_worker+cloudflare\_worker\_version:** import for the resources ([#6357 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6357))
- **dns\_record:** inconsistent apply error ([#6452 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6452))
- **pages\_domain:** resource tests ([#6338 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6338))
- **pages\_project:** unintended resource state drift ([#6377 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6377))
- **queue\_consumer:** id population ([#6181 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6181))
- **workers\_kv:** multipart request ([#6367 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6367))
- **workers\_kv:** updating workers metadata attribute to be read from endpoint ([#6386 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6386))
- **workers\_script\_subdomain:** add note to cloudflare\_workers\_script\_subdomain about redundancy with cloudflare\_worker ([#6383 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6383))
- **workers\_script:** allow config.run\_worker\_first to accept list input
- **zero\_trust\_device\_custom\_profile\_local\_domain\_fallback:** drift issues ([#6365 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6365))
- **zero\_trust\_device\_custom\_profile:** resolve drift issues ([#6364 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6364))
- **zero\_trust\_dex\_test:** correct configurability for 'targeted' attribute to fix drift
- **zero\_trust\_tunnel\_cloudflared\_config:** remove warp\_routing from cloudflared\_config ([#6471 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6471))

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized. We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.

#### For more info

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

Aug 29, 2025

[<h2>Terraform v5.9 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Aug 15, 2025

[<h2>Terraform v5.8.4 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-terraform-v5.8.4-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.

One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes

For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4) in GitHub.

#### Issues Closed

- [#5017: 'Uncaught Error: No such module' using cloudflare\_snippets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare\_workers\_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare\_argo\_smart\_routing importing doesn't read the actual value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Aug 1, 2025

[<h2>Terraform v5.8.2 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Jul 14, 2025

[<h2>Terraform v5.7.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Jun 17, 2025

[<h2>Terraform v5.6.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

May 19, 2025

[<h2>Terraform v5.5.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

May 6, 2025

[<h2>Terraform v5.4.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

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

Mar 21, 2025

[<h2>Dozens of Cloudflare Terraform Provider resources now have proper drift detection</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your `terraform plan` to only show what resources are expected to change.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- API Shield
- Argo Smart Routing
- Argo Tiered Caching
- Bot Management
- BYOIP
- D1
- DNS
- Email Routing
- Hyperdrive
- Observatory
- Pages
- R2
- Rules
- SSL/TLS
- Waiting Room
- Workers
- Zero Trust

Mar 21, 2025

[<h2>Cloudflare Terraform Provider now properly redacts sensitive values</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In the [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in [Cloudflare's OpenAPI Schema ↗︎](https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml) are now annotated with `x-sensitive: true`. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- Alerts and Audit Logs
- Device API
- DLP
- DNS
- Magic Visibility
- Magic WAN
- TLS Certs and Hostnames
- Tunnels
- Turnstile
- Workers
- Zaraz

Feb 3, 2025

[<h2>Terraform v5 Provider is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2025-02-03-terraform-v5-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

![Screenshot of Terraform defining a Zone](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1330,height=296,format=webp/_astro/2024-02-03-terraform-v5-screenshot.mW8OaFoS.png)

Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.

The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the [upgrade guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade) for best practices, or the [blog post on automatically generating Cloudflare's Terraform Provider ↗︎](https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/) for more information about the approach.

For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/terraform/#page","headline":"Terraform Changelog","url":"https://developers.cloudflare.com/changelog/product/terraform/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
