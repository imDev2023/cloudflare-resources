---
title: Core platform Changelog
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

Jul 1, 2025

[<h2>AI Crawl Control refresh</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-refresh/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.

- From the new **AI Crawlers** tab: block specific AI crawlers.
- From the new **Metrics** tab: view AI Crawl Control metrics.

![Block AI crawlers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1323,height=798,format=webp/_astro/manage-ai-crawlers.6UgS8dSG.png) ![Analyze AI crawler activity](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=834,format=webp/_astro/analyze-metrics.C52pJZVg.png)

To get started, explore:

- [Manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/).
- [Analyze AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/).

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

Jun 18, 2025

[<h2>Log Explorer is GA</h2>](https://developers.cloudflare.com/changelog/post/2025-06-18-log-explorer-ga/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) is now GA, providing native observability and forensics for traffic flowing through Cloudflare.

Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.

![Log Explorer dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=208,format=webp/_astro/log-explorer-dash.CJSVLZ7Y.png)

With Log Explorer, you can now:

- **Monitor security and performance issues with custom dashboards** – use natural language to define charts for measuring response time, error rates, top statistics and more.
- **Investigate and troubleshoot issues with Log Search** – use data type-aware search filters or custom sql to investigate detailed logs.
- **Save time and collaborate with saved queries** – save Log Search queries for repeated use or sharing with other users in your account.
- **Access Log Explorer at the account and zone level** – easily find Log Explorer at the account and zone level for querying any dataset.

For help getting started, refer to [our documentation](https://developers.cloudflare.com/log-explorer/).

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

Jun 9, 2025

[<h2>More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/)

[Rules](https://developers.cloudflare.com/rules/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) can now fetch and store [assets](https://developers.cloudflare.com/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard) and [error pages](https://developers.cloudflare.com/rules/custom-errors/#error-pages) from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.

**What’s new:**

- You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.
- These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.

This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.

Learn more in the [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) documentation.

Jun 9, 2025

[<h2>Match Workers subrequests by upstream zone — cf.worker.upstream\_zone now supported in Transform Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/)

[Rules](https://developers.cloudflare.com/rules/)

You can now use the [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field in [Transform Rules](https://developers.cloudflare.com/rules/transform/) to control rule execution based on whether a request originates from [Workers](https://developers.cloudflare.com/workers/), including subrequests issued by Workers in other zones.

![Match Workers subrequests by upstream zone in Transform Rules](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1446,height=988,format=webp/_astro/transform-rule-subrequest-matching.BeUBEN67.png)

**What's new:**

- `cf.worker.upstream_zone` is now supported in Transform Rules expressions.
- Skip or apply logic conditionally when handling [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

For example, to add a header when the subrequest comes from another zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):

```txt
(cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")
```

Selected operation under **Modify request header**: *Set static*

**Header name**: `X-External-Workers-Subrequest`

**Value**: `1`

This gives you more granular control in how you handle incoming requests for your zone.

Learn more in the [Transform Rules](https://developers.cloudflare.com/rules/transform/) documentation and [Rules language fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) reference.

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

May 30, 2025

[<h2>Fine-tune image optimization — WebP now supported in Configuration Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/)

[Rules](https://developers.cloudflare.com/rules/)

You can now enable [Polish](https://developers.cloudflare.com/images/polish/activate-polish/) with the `webp` format directly in [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.

**What’s new:**

- [WebP](https://developers.cloudflare.com/images/polish/compression/#webp) is now a supported [value](https://developers.cloudflare.com/rules/configuration-rules/settings/#polish) in the **Polish** setting for Configuration Rules.

This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.

Learn more in the [Polish](https://developers.cloudflare.com/images/polish/) and [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) documentation.

May 23, 2025

[<h2>New GraphQL Analytics API Explorer and MCP Server</h2>](https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/)

[Analytics](https://developers.cloudflare.com/analytics/)

We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:

#### GraphQL API Explorer

The new [GraphQL API Explorer ↗︎](https://graphql.cloudflare.com/explorer) helps you build, test, and run queries directly in your browser. Features include:

- In-browser schema documentation to browse available datasets and fields
- Interactive query editor with autocomplete and inline documentation
- A "Run in GraphQL API Explorer" button to execute example queries from our docs
- Seamless OAuth authentication — no manual setup required

![GraphQL API Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2626,height=974,format=webp/_astro/graphql-api-explorer.CPUNZZ5B.png)

#### GraphQL Model Context Protocol (MCP) Server

MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our [blog post ↗︎](https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/) for details on how they work and which servers are available. The new [GraphQL MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql) helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:

- Explore what data is available to query
- Generate and refine queries using natural language, with one-click links to run them in the API Explorer
- Build dashboards and visualizations from structured query outputs

Example prompts include:

- “Show me HTTP traffic for the last 7 days for example.com”
- “What GraphQL node returns firewall events?”
- “Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”

We’re continuing to expand these tools, and your feedback helps shape what’s next. [Explore the documentation](https://developers.cloudflare.com/analytics/graphql-api/) to learn more and get started.

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

May 9, 2025

[<h2>More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</h2>](https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/)

[Rules](https://developers.cloudflare.com/rules/)

You can now use IP, Autonomous System (AS), and Hostname [custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) to route traffic to [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/), giving you greater precision and control over how you match and process requests at the edge.

In Snippets, you can now also match on [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/), unlocking smarter edge logic for everything from request filtering and mitigation to [tarpitting](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/) and logging.

**What’s new:**

- [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or [Lists API](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/list/). Great for shared logic across zones.
- [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.

![New fields in Snippets](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1383,height=1351,format=webp/_astro/snippets-lists-scores.D05l6zgc.png)

These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.

Learn more in the [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.

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

Apr 24, 2025

[<h2>Custom Errors are now Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2025-04-24-custom-errors-ga/)

[Rules](https://developers.cloudflare.com/rules/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.

You can now manage **Custom Error Rules**, **Custom Error Assets**, and redesigned **Error Pages** directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.

What's new:

- **Custom Errors are now GA** – Available on all paid plans and ready for production traffic.
- **UI for Custom Error Rules and Assets** – Manage your zone-level rules from the Rules > Overview and your zone-level assets from the Rules > Settings tabs.
- **Define inline content or upload assets** – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.
- **Refreshed UI and new name for Error Pages** – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.
- **Powered by Ruleset Engine** – Custom Error Rules support [conditional logic](https://developers.cloudflare.com/ruleset-engine/rules-language/) and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or [other Cloudflare products](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/). You can also configure [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) to add, change, or remove HTTP headers from responses returned by Custom Error Rules.

Learn more in the [Custom Errors documentation](https://developers.cloudflare.com/rules/custom-errors/).

Apr 18, 2025

[<h2>Custom fields raw and transformed values support</h2>](https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/)

[Logs](https://developers.cloudflare.com/logs/)

Custom Fields now support logging both **raw and transformed values** for request and response headers in the HTTP requests dataset.

These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.

By default:

- Request headers are logged as raw values
- Response headers are logged as transformed values

These defaults can be overridden to suit your logging needs.

Note

Transformed and raw values for request and response headers are available **only via the API** and cannot be set through the UI.

For more information refer to [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/) documentation

Apr 15, 2025

[<h2>Cloudflare Registrar API is now in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/)

[Registrar](https://developers.cloudflare.com/registrar/)

Cloudflare Registrar API is now in beta.

You can now use the Cloudflare API to:

- Search for domain names.
- Check real-time availability and pricing.
- Register supported domains programmatically.

This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.

Because the Registrar API is part of the Cloudflare API, it can also be used in [Cloudflare MCP ↗︎](https://github.com/cloudflare/mcp) and other agent-driven workflows.

If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:

- `Search for domain ideas for a coffee shop based in Evergreen, Colorado.`
- `Check whether example.com is available and show me the current price.`
- `Register example.com`

For supported operations, extension availability, and workflow details, refer to:

- [Registrar API guide ↗︎](https://developers.cloudflare.com/registrar/registrar-api/)
- [Registrar API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar)

Apr 9, 2025

[<h2>Cloudflare Snippets are now Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/)

[Rules](https://developers.cloudflare.com/rules/)

![Cloudflare Snippets are now GA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1126,format=webp/_astro/snippets-ga.BJr3csvv.png)

[Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/) are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.

You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.

What's new:

- **Snippets are now GA** – Available at no extra cost on all Pro, Business, and Enterprise plans.
- **Ready for production** – Snippets deliver a production-grade experience built for scale.
- **Part of the Cloudflare Rules platform** – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.
- **Trace integration** – Use [Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/) to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.![Snippets shown in Cloudflare Trace results](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=334,format=webp/_astro/snippets-ga-trace.WlCshaFo.gif)

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/snippets/).

Mar 27, 2025

[<h2>Register and renew .ai and .shop domains at cost</h2>](https://developers.cloudflare.com/changelog/post/2025-03-27-ai-domains-available/)

[Registrar](https://developers.cloudflare.com/registrar/)

![Example search for .ai domains](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1788,height=818,format=webp/_astro/2025-03-27-ai-domains-available.D96eztke.png)

Cloudflare Registrar now supports `.ai` and `.shop` domains. These are two of our most highly-requested top-level domains (TLDs) and are great additions to the [300+ other TLDs we support ↗︎](https://domains.cloudflare.com/tlds).

Starting today, customers can:

- Register and renew these domains *at cost* without any markups or add-on fees
- Enjoy best-in-class security and performance with native integrations with Cloudflare DNS, CDN, and SSL services like one-click DNSSEC
- Combat domain hijacking with [Custom Domain Protection ↗︎](https://www.cloudflare.com/products/registrar/custom-domain-protection/) (available on enterprise plans)

We can't wait to see what AI and e-commerce projects you deploy on Cloudflare. To get started, transfer your domains to Cloudflare or [search for new ones to register ↗︎](https://domains.cloudflare.com/).

Mar 27, 2025

[<h2>Audit logs (version 2) - Beta Release</h2>](https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.

Availability: Audit logs (version 2) is now in Beta, with support limited to **API access**.

Use the following API endpoint to retrieve audit logs:

```js
GET https://api.cloudflare.com/client/v4/accounts/<account_id>/logs/audit?since=<date>&before=<date>
```

You can access detailed documentation for audit logs (version 2) Beta API release [here ↗︎](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/).

**Key Improvements in the Beta Release:**

- **Automated & standardized logging**: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.
- **Expanded product coverage**: Increased audit log coverage from 75% to 95%. Key API endpoints such as `/accounts`, `/zones`, and `/organizations` are now included.
- **Granular filtering**: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.
- **Enhanced context and traceability**: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.
- **Comprehensive activity capture**: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.

**Known Limitations in Beta**

- Error handling for the API is not implemented.
- There may be gaps or missing entries in the available audit logs.
- UI is unavailable in this Beta release.
- System-level logs and User-Activity logs are not included.

Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: [Introducing Automatic Audit Logs ↗︎](https://blog.cloudflare.com/introducing-automatic-audit-logs/)

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

Mar 6, 2025

[<h2>One-click Logpush Setup with R2 Object Storage</h2>](https://developers.cloudflare.com/changelog/post/2025-03-06-oneclick-logpush/)

[Logs](https://developers.cloudflare.com/logs/)

We’ve streamlined the [Logpush](https://developers.cloudflare.com/logs/logpush/) setup process by integrating R2 bucket creation directly into the Logpush workflow!

Now, you no longer need to navigate multiple pages to manually create an R2 bucket or copy credentials. With this update, you can seamlessly **configure a Logpush job to R2 in just one click**, reducing friction and making setup faster and easier.

This enhancement makes it easier for customers to adopt Logpush and R2.

For more details refer to our [Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/) documentation.

Feb 12, 2025

[<h2>Increased Cloudflare Rules limits</h2>](https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/)

[Rules](https://developers.cloudflare.com/rules/)

We have upgraded and streamlined [Cloudflare Rules](https://developers.cloudflare.com/rules/) limits across all plans, simplifying rule management and improving scalability for everyone.

**New limits by product:**

- [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)
  - Free: **20** → **10,000** URL redirects across lists
  - Pro: **500** → **25,000** URL redirects across lists
  - Business: **500** → **50,000** URL redirects across lists
  - Enterprise: **10,000** → **1,000,000** URL redirects across lists
- [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  - Free: **5** → **10** connectors
  - Enterprise: **125** → **300** connectors
- [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)
  - Pro: **5** → **25** error assets and rules
  - Business: **20** → **50** error assets and rules
  - Enterprise: **50** → **300** error assets and rules
- [Snippets](https://developers.cloudflare.com/rules/snippets/)
  - Pro: **10** → **25** code snippets and rules
  - Business: **25** → **50** code snippets and rules
  - Enterprise: **50** → **300** code snippets and rules
- [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/), [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), [Compression Rules](https://developers.cloudflare.com/rules/compression-rules/), [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/), [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/), and [Transform Rules](https://developers.cloudflare.com/rules/transform/)
  - Enterprise: **125** → **300** rules

Gradual rollout

Limits are updated gradually. Some customers may still see previous limits until the rollout is fully completed in the first half of 2025.

Feb 11, 2025

[<h2>Custom Errors (beta): Stored Assets & Account-level Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/)

[Rules](https://developers.cloudflare.com/rules/)

We're introducing [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.

This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.

This brings the following new capabilities:

- **Custom error assets** – Fetch and store external error pages at the edge for use in error responses.
- **Account-Level custom errors** – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.

You can use Cloudflare API to upload your existing assets for use with Custom Errors:

```bash
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "name": "maintenance",
  "description": "Maintenance template page",
  "url": "https://example.com/"
}'
```

You can then reference the stored asset in a Custom Error rule:

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "rules": [
		{
			"action": "serve_error",
			"action_parameters": {
				"asset_name": "maintenance",
				"content_type": "text/html",
				"status_code": 503
			},
			"enabled": true,
			"expression": "http.request.uri.path contains \"error\""
		}
	]
}'
```

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
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/8/#page","headline":"Core platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
