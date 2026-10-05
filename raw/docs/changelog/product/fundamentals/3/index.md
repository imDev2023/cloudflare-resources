---
title: Cloudflare Fundamentals Changelog
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

Oct 7, 2025

[<h2>Automated reminders for backup codes</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to **Profile** > **Security & Authentication** > **Backup codes**.

#### Sign-in security best practices

Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.

- Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.
- Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked
- Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.
- If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.
- If you use a custom email domain to sign in, [configure SSO ↗︎](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/).
- If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.
- If you manage a Cloudflare account for work:
  - Have at least two administrators in case one of them unexpectedly leaves your company
  - Use SCIM to automate permissions management for members in your Cloudflare account

Oct 2, 2025

[<h2>Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Fine-grained permissions for **Access Applications, Identity Providers (IdPs), and Targets** is now available in Public Beta. This expands our RBAC model beyond account & zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.

#### What's New

- **[Access Applications ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3004,height=1410,format=webp/_astro/2025-10-01-fine-grained-permissioning-ux.BWVmQsVF.png)

Note

During the public beta, members must also be assigned an account-scoped, read only role to view resources in the dashboard. This restriction will be lifted in a future release.

- **Account Read Only** plus a fine-grained permission for a specific App, IdP, or Target
- **Cloudflare Zero Trust Read Only** plus fine-grained permission for a specific App, IdP, or Target

For more info:

- [Get started with Cloudflare Permissioning](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
- [Manage Member Permissioning via the UI & API](https://developers.cloudflare.com/fundamentals/manage-members/manage)

Oct 1, 2025

[<h2>Return markdown</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.

```sh
curl https://developers.cloudflare.com/workers/ -H 'Accept: text/markdown'  -v
```

If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example [here ↗︎](https://github.com/cloudflare/cloudflare-docs/pull/25493).

Sep 25, 2025

[<h2>Sign in with GitHub</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-sign-in-with-github/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare has launched sign in with GitHub as a log in option. This feature is available to all users with a verified email address who are not using SSO. To use it, simply click on the `Sign in with GitHub` button on the dashboard login page. You will be logged in with your primary GitHub email address.

#### For more information

- [Log in to Cloudflare](https://developers.cloudflare.com/fundamentals/user-profiles/login/)

Sep 25, 2025

[<h2>SSO for all</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-sso-for-all/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Single sign-on (SSO) streamlines the process of logging into Cloudflare for Enterprise customers who manage a custom email domain and manage their own identity provider. Instead of managing a password and two-factor authentication credentials directly for Cloudflare, SSO lets you reuse your existing login infrastructure to seamlessly log in. SSO also provides additional security opportunities such as device health checks which are not available natively within Cloudflare.

Historically, SSO was only available for Enterprise accounts. Today, we are announcing that we are making SSO available to all users for free. We have also added the ability to directly manage SSO configurations using the API. This removes the previous requirement to contact support to configure SSO.

#### For more information

- [Every Cloudflare feature, available to all ↗︎](https://blog.cloudflare.com/enterprise-grade-features-for-all/)
- [Configure Dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)

Sep 8, 2025

[<h2>Reminders about two-factor authentication backup codes</h2>](https://developers.cloudflare.com/changelog/post/2025-09-08-reminders-about-two-factor-authentication-backup-codes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Two-factor authentication is the best way to help protect your account from account takeovers, but if you lose your second factor, you could be locked out of your account. Lock outs are one of the top reasons customers contact Cloudflare support, and our policies often don't allow us to bypass two-factor authentication for customers that are locked out. Today we are releasing an improvement where Cloudflare will periodically remind you to securely save your backup codes so you don't get locked out in the future.

#### For more information

- [Two-factor authentication](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/)

Sep 3, 2025

[<h2>Introducing new headers for rate limiting on Cloudflare's API</h2>](https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare's API now supports rate limiting headers using the pattern developed by the [IETF draft on rate limiting ↗︎](https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html). This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.

Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.

As always, if you need any help with rate limits, please contact Support.

#### Changes

#### New Headers

**Headers that are always returned:**

- `Ratelimit`: List of service limit items, composed of the limit name, the remaining quota ( `r`) and the time next window resets ( `t`). For example: `"default";r=50;t=30`
- `Ratelimit-Policy`: List of quota policy items, composed of the policy name, the total quota ( `q`) and the time window the quota applies to ( `w`). For example: `"burst";q=100;w=60`

**Returned only when a rate limit has been reached (error code: 429):**

- Retry-After: Number of Seconds until more capacity is available, rounded up

#### SDK Back offs

- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached.

#### GraphQL and Edge APIs

These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL.

#### For more information

- [Rate limits at Cloudflare ↗︎](https://developers.cloudflare.com/fundamentals/api/reference/limits/)

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

Jun 23, 2025

[<h2>Cloudflare User Groups & SCIM User Groups are now in GA</h2>](https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're announcing the GA of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups**, strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.

**What's New**

**User Groups \[GA]**: [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups \[GA]**: Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

**Stability & Scale**: These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are now officially deprecated as of June 2, 2025. SCIM Virtual Groups end-of-life will take effect on December 2, 2025. We strongly recommend migrating to SCIM User Groups to ensure continued support for SCIM synchronization to the Cloudflare Dashboard. If you haven’t used Virtual Groups, no action is required.

For more info:

- [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
- [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

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

Jun 2, 2025

[<h2>Cloudflare User Groups & Enhanced Permission Policies are now in Beta</h2>](https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're excited to announce the Public Beta launch of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups**, expanding our RBAC capabilities to simplify user and group management at scale.

We've also visually overhauled the **Permission Policies UI** to make defining permissions more intuitive.

**What's New**

**User Groups \[BETA]**: [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups \[BETA]**: Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are deprecated as of 06/02/25. We recommend migrating SCIM Virtual Groups implementations to use [SCIM User Groups](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/). If you did not use Virtual Groups, no action is needed.

**Revamped Permission Policies UI \[BETA]**: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1884,format=webp/_astro/2025-06-02-permissions-policy-ux.2wLEPgVX.png)

Note

When opting into the Beta for User Groups and Permission Policies, you'll be transitioning to a new experience. Please be aware that opting out isn't currently available.

For more info:

- [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
- [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

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

Mar 26, 2025

[<h2>Updates to Account Home - Quick actions, traffic insights, Workers projects, and more</h2>](https://developers.cloudflare.com/changelog/post/2025-03-26-account-home-updates/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

![Updated Account Home](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2574,height=982,format=webp/_astro/2025-03-26-account-home-updates.CcOsD1dD.png)

Recently, Account Home has been updated to streamline your workflows:

- **Recent Workers projects**: You'll now find your projects readily accessible from a new `Developer Platform` tab on Account Home. See recently-modified projects and explore what you can work our developer-focused products.
- **Traffic and security insights**: Get a snapshot of domain performance at a glance with key metrics and trends.
- **Quick actions**: You can now perform common actions for your account, domains, and even Workers in just 1-2 clicks from the 3-dot menu.
- **Keep starred domains front and center**: Now, when you filter for starred domains on Account Home, we'll save your preference so you'll continue to only see starred domains by default.

We can't wait for you to take the new Account Home for a spin.

For more info:

- [Try the updated Account Home ↗︎](https://dash.cloudflare.com/)
- [Documentation on starred domains](https://developers.cloudflare.com/fundamentals/manage-domains/star-zones/)

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
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/fundamentals/3/#page","headline":"Cloudflare Fundamentals Changelog","url":"https://developers.cloudflare.com/changelog/product/fundamentals/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
