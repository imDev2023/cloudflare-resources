---
description: Terraform v5.19.0 introduces 14 new resources and significantly improves v4 to v5 migration with automatic state upgraders and tf-migrate tool support
title: Terraform v5.19.0 now available
image: https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/og.png?v=3f3fd31fbfb79f10
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 24, 2026

## Terraform v5.19.0 now available

[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/#page","headline":"Terraform v5.19.0 now available","description":"Terraform v5.19.0 introduces 14 new resources and significantly improves v4 to v5 migration with automatic state upgraders and tf-migrate tool support","url":"https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/og.png?v=3f3fd31fbfb79f10","dateModified":"2026-04-24","datePublished":"2026-04-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
