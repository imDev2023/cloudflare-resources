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

Jun 19, 2026

[<h2>Manage all your routes from one page in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

- **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
- **See every route in one table**, with its destination, type, connector, priority, and source, and filter or sort to find what you need.
- **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
- **Manage [virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
- **Test a route** to see which connector and next hop a destination resolves to before you commit a change.

To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

Jun 16, 2026

[<h2>Pay Per Crawl advanced configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

You can now configure advanced Pay Per Crawl settings for your zone, including:

- **Disable Pay Per Crawl by URI pattern** using [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) to offer free access to specific pages while charging for others.
- **Dynamic pricing** by having your origin return a `crawler-price` response header, or by using a [Cloudflare Worker](https://developers.cloudflare.com/workers/) to set prices based on request properties.

When dynamic pricing is enabled, Pay Per Crawl adds a `cf-pay-per-crawl` request header to origin requests so your origin or Worker can determine the appropriate price.

Refer to the [Advanced configuration documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/) for details.

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

Jun 4, 2026

[<h2>Billable usage and budget alerts now in product sidebars</h2>](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/) [D1](https://developers.cloudflare.com/d1/) [R2](https://developers.cloudflare.com/r2/) [KV](https://developers.cloudflare.com/kv/) [Queues](https://developers.cloudflare.com/queues/) [Vectorize](https://developers.cloudflare.com/vectorize/) [Durable Objects](https://developers.cloudflare.com/durable-objects/) [Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

Jun 3, 2026

[<h2>Introducing self-managed OAuth clients</h2>](https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.

OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.

#### What is new

Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.

#### Create an application

To create an application, go to **Manage account** > **OAuth clients** in your account on the Cloudflare dashboard.

[Go to **OAuth clients** ↗](https://dash.cloudflare.com/?to=/:account/oauth-clients)

#### Select limited scopes

If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.

Users can review the requested scopes before they consent.

#### Apps for both private and public use

Applications start with `private` visibility. Private applications can only be used by members of the account where the application was created.

To make an application available to any Cloudflare user, complete the prerequisites for `public` visibility.

For more information, refer to [client visibility](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients).

#### Client domain verification

Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.

After verification, users see a verified badge on the consent page.

For more information, refer to [domain verification](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification).

#### Learn more

For more information, refer to [OAuth clients](https://developers.cloudflare.com/fundamentals/oauth/).

Jun 1, 2026

[<h2>New Turnstile Events Logpush dataset in Cloudflare Logs</h2>](https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

- **Turnstile Events**: A new dataset with fields including `ASN`, `Action`, `BrowserMajor`, `BrowserName`, `ClientIP`, `CountryCode`, `EventType`, `Hostname`, `OSMajor`, `OSName`, `Sitekey`, `Timestamp`, and `UserAgent`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

May 29, 2026

[<h2>Updated fields across multiple Logpush datasets in Cloudflare Logs</h2>](https://developers.cloudflare.com/changelog/post/2026-05-29-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### Updated fields in existing datasets

- **DEX Device State Events** (added): `DeviceRegistrationProfileID`.
- **Gateway HTTP** (added): `AddedHeaders`, `DeletedHeaders`, and `SetHeaders`.
- **HTTP requests** (added): `MatchedRules`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

May 27, 2026

[<h2>Cloudflare Tunnel now runs connectivity pre-checks at startup</h2>](https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting with [`cloudflared` version 2026.5.2 ↗︎](https://github.com/cloudflare/cloudflared/releases), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) automates the entire [connectivity pre-checks workflow](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/) directly inside the binary. Previously, customers had to install `dig` and `netcat` and run those commands by hand to verify their environment. Now `cloudflared` does it natively at startup — and surfaces actionable remediation when something is blocked.

![cloudflared connectivity pre-checks output](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1012,format=webp/_astro/cloudflared-connectivity-prechecks.DRwN6tGe.gif)

On every `cloudflared tunnel run` (and `cloudflared tunnel diag`), the binary now natively checks:

- **DNS resolution** — `region1.v2.argotunnel.com` and `region2.v2.argotunnel.com` resolve to valid Cloudflare IPs.
- **Transport connectivity** — outbound `UDP (QUIC)` and `TCP (HTTP/2)` on port `7844`.
- **Management API** — outbound `TCP/443` to `api.cloudflare.com` for software updates.

Results are printed in a scannable CLI table with three states:

- ✅ **Pass** — the check succeeded.
- ⚠️ **Warn** — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.
- ❌ **Fail** — a blocking issue, with a specific remediation hint (for example, `Allow outbound UDP on port 7844`).

If DNS is unresolvable, or **both** UDP and TCP fail on port 7844, `cloudflared` exits early with the failure rather than looping on opaque `failed to dial` errors.

Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.

To get the new behavior, upgrade `cloudflared` to version `2026.5.2` or later. For more details, refer to the [Connectivity pre-checks documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).

May 21, 2026

[<h2>Modernized Billing Profile with new payment options</h2>](https://developers.cloudflare.com/changelog/post/2026-05-21-modernised-billing-profile/)

[Billing](https://developers.cloudflare.com/billing/)

The [Billing Profile](https://developers.cloudflare.com/billing/get-started/update-billing-info/) now has a modern UI and a single space that unifies billing information, payment method management and an enhanced subscriptions view under a single **Subscriptions** tab.

#### What changed

The **Subscriptions** tab brings billing information, payment method management, and your subscriptions together in one place. The payment management and **Pay overdue balances** flows now use the latest checkout as product purchase flows, so you can pay with Apple Pay, Google Pay, Link, and [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/) alongside cards and PayPal.

New cards complete 3D Secure authentication when the issuer requires it — for example, the EU under PSD2 and India under RBI.

![Modernized Billing Profile with the Subscriptions tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=909,height=676,format=webp/_astro/2026-05-21-modernised-billing-profile.D6PysUnl.png)

For details, refer to the [Billing Home](https://developers.cloudflare.com/billing/) documentation.

May 21, 2026

[<h2>Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</h2>](https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now scope Cloudflare permissions to individual [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the resource picker now lists [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes as scopable resource types. You can:

- Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.
- Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.
- Scope a single policy to one or many Tunnels and Mesh nodes at once.

#### How it works

Granular permissions are a parallel layer to existing account-level roles — they do not replace them.

- **Existing account-level roles continue to work.** A member with `Cloudflare Access` or `Cloudflare Zero Trust` retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.
- **Granular permissions are additive.** For any API request on a specific Tunnel or Mesh node, access is granted if the principal has **either** the account-level role **or** a granular permission for that resource.
- **Resource enumeration is authorization-aware.** Listing endpoints ( `GET /accounts/{id}/cfd_tunnel`, `GET /accounts/{id}/warp_connector`) return only the resources the principal has at least read access to.

#### Get started

- Configure [granular permissions for Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/guides/granular-permissions/).
- Configure [granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One](https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/).
- Review the [resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) on the Cloudflare role reference.

May 13, 2026

[<h2>New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</h2>](https://developers.cloudflare.com/changelog/post/2026-05-13-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

- **Email Security Post-Delivery Events**: A new dataset with fields including `AlertID`, `CompletedAt`, `Destination`, `FinalDisposition`, `Folder`, `From`, `FromName`, `MessageID`, `MessageTimestamp`, `MicrosoftTenantID`, `Operation`, `PostfixID`, `Reasons`, `Recipient`, `RequestedAt`, `RequestedBy`, `RequestedDisposition`, `Status`, `Subject`, `Success`, and `To`.
- **Magic Network Monitoring Flow Logs**: A new dataset with fields including `AWSVPCFlowJSON`, `Bits`, `DestinationAS`, `DestinationAddress`, `DestinationPort`, `DeviceID`, `EgressBits`, `EgressPackets`, `Ethertype`, `FlowProtocol`, `FlowTimestamp`, `NumFlows`, `PacketID`, `Packets`, `Protocol`, `RuleIDs`, `SampleRate`, `SampleRateType`, `SamplerAddress`, `SourceAS`, `SourceAddress`, `SourcePort`, `TcpFlags`, and `Timestamp`.

#### Updated fields in existing datasets

- **Firewall events** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, and `AISecurityUnsafeTopicCategories`.
- **HTTP requests** (added): `AISecurityInjectionScore`, `AISecurityPIICategories`, `AISecurityTokenCount`, `AISecurityUnsafeTopicCategories`, and `Subrequests`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

May 4, 2026

[<h2>Keyboard shortcuts for the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-05-04-keyboard-shortcuts/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now navigate, switch context, and take common actions in the Cloudflare dashboard without leaving your keyboard. Press `?` anywhere to see the full list. Keyboard shortcuts can be disabled by visiting your [profile settings ↗︎](https://dash.cloudflare.com/profile/settings).

#### Navigate

| Shortcut | Action |
| --- | --- |
| `g h` | Go to Home |
| `g a` | Go to account overview |
| `g z` | Go to zone overview |
| `g p` | Go to your profile |
| `g w` | Go to Workers & Pages |
| `g o` | Go to Zero Trust |
| `g b` | Go to billing |
| `g 1` – `g 5` | Go to a recent or pinned item (by position in sidebar) |
| `t →` | Move to the next tab |
| `t ←` | Move to the previous tab |
| `p →` | Move to the next page of a table |
| `p ←` | Move to the previous page of a table |

#### Take action

| Shortcut | Action |
| --- | --- |
| `/` | Open quick search |
| `?` | Show keyboard shortcuts |
| `s a` | Switch account |
| `s z` | Switch zone |
| `s .` | Star or unstar the current zone |
| `p .` | Pin or unpin the current page |
| `t s` | Toggle the sidebar open or closed |
| `t m` | Expand or collapse all sidebar menus |
| `t a` | Toggle Ask AI sidebar |
| `d .` | Toggle dark mode |
| `c u` | Copy the current URL |
| `c d` | Copy a deep link URL |

Apr 30, 2026

[<h2>Go SDK v7.0.0 Released</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) [Go SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v6.10.0...v7.0.0 ↗︎](https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0)

This is a major version release that includes breaking changes to three packages: `ai_search`, `email_security`, and `workers`. These changes reflect upstream API specification updates that improve type correctness and consistency.

**Please ensure you read through the list of changes below before moving to this version** - this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

See the [v7.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md) for before/after code examples and actions needed for each change.

#### AI Search - SearchForAgents Metadata Removed

The `SearchForAgents` nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.

**Removed Types:**

- `InstanceNewResponseMetadataSearchForAgents`
- `InstanceUpdateResponseMetadataSearchForAgents`
- `InstanceListResponseMetadataSearchForAgents`
- `InstanceDeleteResponseMetadataSearchForAgents`
- `InstanceReadResponseMetadataSearchForAgents`
- `InstanceNewParamsMetadataSearchForAgents`
- `InstanceUpdateParamsMetadataSearchForAgents`
- `NamespaceInstanceNewResponseMetadataSearchForAgents`
- `NamespaceInstanceUpdateResponseMetadataSearchForAgents`
- `NamespaceInstanceListResponseMetadataSearchForAgents`
- `NamespaceInstanceDeleteResponseMetadataSearchForAgents`
- `NamespaceInstanceReadResponseMetadataSearchForAgents`
- `NamespaceInstanceNewParamsMetadataSearchForAgents`
- `NamespaceInstanceUpdateParamsMetadataSearchForAgents`

#### Email Security - Path Parameter Type Changes

Multiple Email Security settings sub-resources have changed their path parameter types from `int64` to `string`:

- `AllowPolicies` ( `policyID int64` -> `policyID string`)
- `BlockSenders` ( `patternID int64` -> `patternID string`)
- `Domains` ( `domainID int64` -> `domainID string`)
- `ImpersonationRegistry` ( `displayNameID int64` -> `impersonationRegistryID string`)
- `TrustedDomains` ( `trustedDomainID int64` -> `trustedDomainID string`)

#### Email Security - Investigate Parameter Rename

The `Investigate.Get`, `Investigate.Move.New`, and `Investigate.Reclassify.New` methods now use `investigateID` instead of `postfixID` as the path parameter name.

#### Email Security - Domains BulkDelete Method Removed

The `SettingDomainService.BulkDelete` method and its associated types have been removed:

- `SettingDomainBulkDeleteResponse`
- `SettingDomainBulkDeleteParams`

#### Email Security - TrustedDomains Return Type Change

`SettingTrustedDomainService.New` now returns `*SettingTrustedDomainNewResponse` instead of `*SettingTrustedDomainNewResponseUnion`.

#### Email Security - Investigate.Move Return Type Change

`InvestigateMoveService.New` now returns `*pagination.SinglePage[InvestigateMoveNewResponse]` instead of `*[]InvestigateMoveNewResponse`.

#### Workers - Observability Telemetry Filter Restructuring

The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:

- `ObservabilityTelemetryKeysParams.Filters` now accepts `FiltersObjectFilterUnion` (was `[]interface\{\}`)
- `ObservabilityTelemetryQueryParams.Parameters.Filters` now accepts `FiltersObjectFilterUnion`
- `ObservabilityTelemetryValuesParams.Filters` now accepts `FiltersObjectFilterUnion`

New types include `FiltersObjectFiltersObject` (for group filters with `FilterCombination`) and `FiltersWorkersObservabilityFilterLeaf` (for leaf filters with typed `Operation`, `Type`, and `Value` fields).

#### Features

#### Organizations - Audit Logs (`client.Organizations.Logs.Audit`)

**NEW SERVICE:** Query organization audit logs with cursor-based pagination.

- `List()` - Retrieve audit logs

#### Browser Rendering (`client.BrowserRendering`)

- `client.BrowserRendering.Devtools.Browser.Targets.Close()` - Close a specific browser target (tab, page) by ID

#### Queues (`client.Queues`)

- `client.Queues.GetMetrics()` - Retrieve queue metrics for a specific queue

#### AI Search (`client.AISearch`)

- Added `WaitForCompletion` parameter to `NamespaceInstanceItemNewOrUpdateParams` and `NamespaceInstanceItemSyncParams` for synchronous indexing confirmation

#### Bug Fixes

- **Magic Transit**: `ConnectorService.List` parameter name corrected from `query` to `params` (non-functional, affects generated documentation only)

#### Deprecations

None in this release.

#### Get started

- [Download Go SDK v7.0.0 ↗︎](https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0)
- [Go SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/go/)
- [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md)

Apr 30, 2026

[<h2>Cloudflare Python SDK v5.0.0 Released</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v4.3.1...v5.0.0 ↗︎](https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0)

This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.

**Please review the breaking changes below before upgrading.** A migration guide is available at [v5.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md).

#### Breaking Changes

- **Python 3.8 is no longer supported.** The minimum required version is now Python 3.9.
- **`typing-extensions` minimum version bumped** from `>=4.10` to `>=4.14`.

The following resources have breaking changes. See the [v5.0.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md) for detailed migration instructions.

- `abusereports`
- `acm.totaltls`
- `apigateway.configurations`
- `cloudforceone.threatevents`
- `d1.database`
- `intel.indicatorfeeds`
- `logpush.edge`
- `origintlsclientauth.hostnames`
- `queues.consumers`
- `radar.bgp`
- `rulesets.rules`
- `schemavalidation.schemas`
- `snippets`
- `zerotrust.dlp`
- `zerotrust.networks`

#### Features

#### aiohttp Backend Support

The async client now supports an optional `aiohttp` HTTP backend for improved concurrency performance. Install with `pip install cloudflare[aiohttp]` and use `DefaultAioHttpClient()` as the `http_client` parameter.

#### Python 3.13 and 3.14 Support

Python 3.13 and 3.14 are now tested and supported.

#### New Services

The following top-level resources are new in this release:

| Resource | Client Path | Description |
| --- | --- | --- |
| AI Search | `aisearch` | AI-powered search capabilities |
| Connectivity | `connectivity` | Connectivity testing and diagnostics |
| Email Sending | `email_sending` | Email send and send\_raw endpoints |
| Fraud | `fraud` | Fraud detection and prevention |
| Google Tag Gateway | `google_tag_gateway` | Google Tag Gateway management |
| Organizations | `organizations` | Organization audit logs and management |
| R2 Data Catalog | `r2_data_catalog` | R2 Data Catalog operations |
| Realtime Kit | `realtime_kit` | Realtime communication (Calls/TURN) |
| Resource Tagging | `resource_tagging` | Resource tagging and labeling |
| Token Validation | `token_validation` | Token validation configuration and rules |
| Vulnerability Scanner | `vulnerability_scanner` | Vulnerability scanning, credential sets, and target environments |

#### New Endpoints on Existing Services

- **api\_gateway**: Labels endpoints
- **billing**: Billable usage PayGo endpoint
- **brand\_protection**: v2 endpoints
- **browser\_rendering**: DevTools methods
- **cache**: Origin cloud regions resource
- **custom\_origin\_trust\_store**: Custom origin trust store
- **dns**: `dns_records/usage` endpoints
- **email\_security**: Phishguard reports endpoint
- **iam**: User groups and user group members resources
- **radar**: Botnet Threat Feed and Post-Quantum endpoints
- **workers**: Observability Destinations resources
- **zero\_trust**: Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files
- **zones**: Zone environments endpoints

#### Bug Fixes

- Fixed `polymorphic_serialization` parameter in `model_dump` overrides
- Added `BaseModel` base to response `SchemaFieldStruct`/ `SchemaFieldList` stubs in Pipelines
- Added missing `model_rebuild`/ `update_forward_refs` for `SharedEntryCustomEntry` classes in DLP
- Made `RunQueryParametersNeedleValue` a `BaseModel` with `arbitrary_types_allowed` in Workers
- Removed duplicate `notification_url` field in webhook response types for Stream
- Resolved pre-existing codegen type errors
- Fixed `type: ignore[call-arg]` placement for mypy compatibility in Radar

#### Deprecations

Resources with `@deprecated` annotations on some methods include: `accounts`, `addressing`, `ai-gateway`, `aisearch`, `api-gateway`, `billing`, `cloudforce-one`, `dns`, `email-routing`, `email-security`, `filters`, `firewall`, `images`, `intel`, `kv`, `logpush`, `origin-tls-client-auth`, `pages`, `pipelines`, `radar`, `rate-limits`, `registrar`, `rulesets`, `ssl`, `user`, `workers`, `workers-for-platforms`, `zero-trust`, `zones`

#### Get started

- [Download Python SDK v5.0.0 ↗︎](https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0)
- [Python SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/python/)
- [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md)

Apr 30, 2026

[<h2>Cloudflare TypeScript SDK v6.0.0 Released</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

Full Changelog: [v6.0.0-beta.2...v6.0.0 ↗︎](https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0)

This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.

**Please ensure you read through the list of changes below before moving to this version** - this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

#### SDK Infrastructure

- **Retry-After handling changed**: The SDK now respects any server-specified `Retry-After` value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.
- **Empty response handling**: Responses with `content-length: 0` now return `undefined` instead of attempting to parse the body.
- **Environment variable reading**: Empty string env vars (for example, `CLOUDFLARE_API_TOKEN=""`) are now treated as unset.
- **Path query parameter merging**: URL search params embedded in endpoint paths are now extracted and merged into the query object.

#### Removed Endpoints (17)

17 HTTP endpoints were removed from the SDK, affecting `abuse-reports`, `cloudforce-one`, `dlp/profiles/predefined`, `email-security/investigate`, `email-security/settings`, and `intel/ip-list`.

#### Method Signature Changes

- `client.ai.toMarkdown.transform(file, \{ ...params \})` -> `client.ai.toMarkdown.transform(\{ ...params \})` -- `file` moved from positional arg into params body
- `client.radar.ai.toMarkdown.create(body, \{ ...params \})` -> `client.radar.ai.toMarkdown.create(\{ ...params \})` -- `body` moved from positional arg into params
- `client.abuseReports.create(reportType, \{ ...params \})` -> `client.abuseReports.create(reportParam, \{ ...params \})` -- positional arg renamed
- `client.iam.userGroups.members.create(userGroupId, [ ...body ])` -> `client.iam.userGroups.members.create(userGroupId, [ ...members ])` -- body array param renamed

#### Renamed Client Paths

- `client.originTLSClientAuth.hostnames.certificates` -> `client.originTLSClientAuth.zoneCertificates`
- `client.radar.netflows` -> `client.radar.netFlows` (casing change)

#### Return Type Changes (179)

- **133 methods now return `null`** instead of a typed response object. This primarily affects delete operations across `accounts`, `cache`, `d1`, `filters`, `firewall`, `hyperdrive`, `iam`, `kv`, `logpush`, `logs`, `r2`, `stream`, `workers`, `zero-trust`, `zones`, and others.
- **17 methods changed pagination type** (for example, `KeysCursorPaginationAfter` -> `KeysCursorLimitPagination`).
- **29 methods changed to a different named type** (for example, `CloudflaredCreateResponse` -> `CloudflareTunnel`).

#### Removed Types (43)

24 shared types removed from root namespace (`ASN`, `AuditLog`, `Member`, `Permission`, `Role`, `Subscription`, `Token`, etc.). 19 response types consolidated or renamed.

#### Resource Restructuring

19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.

#### New Top-Level Resources

11 entirely new resources added to the client:

| Resource | Client Path | Methods | Description |
| --- | --- | --- | --- |
| AI Search | `client.aiSearch` | 46 | Instances, namespaces, tokens, and items |
| Connectivity | `client.connectivity` | 5 | Directory service APIs |
| Email Sending | `client.emailSending` | 7 | Send and send\_raw endpoints |
| Fraud | `client.fraud` | 2 | Fraud detection API |
| Google Tag Gateway | `client.googleTagGateway` | 2 | Google Tag Gateway management |
| Organizations | `client.organizations` | 8 | Organization profiles and audit logs |
| R2 Data Catalog | `client.r2DataCatalog` | 11 | R2 Data Catalog routes |
| Realtime Kit | `client.realtimeKit` | 54 | Realtime Kit APIs |
| Resource Tagging | `client.resourceTagging` | 9 | Resource tagging routes |
| Token Validation | `client.tokenValidation` | 13 | Token validation rules |
| Vulnerability Scanner | `client.vulnerabilityScanner` | 21 | Vulnerability scanning |

#### New Sub-Resources on Existing Resources

- **browser-rendering**: `crawl`, `devtools` - Crawl endpoints and DevTools methods
- **cache**: `origin-cloud-regions` - Origin cloud regions resource
- **dns**: `usage` - DNS records usage endpoints
- **d1**: `time-travel` - Time travel get\_bookmark and restore
- **email-security**: `phishguard` - Phishguard reports endpoint
- **pipelines**: `sinks`, `streams` - Pipelines restructure
- **radar**: `agent-readiness`, `geolocations`, `post-quantum` - New analytics endpoints
- **workers**: `observability` - Observability destinations
- **zones**: `environments` - Zone environments endpoints
- **api-gateway**: `labels` - Labels endpoints
- **brand-protection**: `v2` - V2 endpoints
- **alerting**: `silences` - Alert silencing API
- **billing**: `usage` - Billable usage PayGo endpoint
- **iam**: `sso` - SSO Connectors resource
- **queues**: `getMetrics` method - Queues metrics endpoint
- **registrar**: `registration-status`, `update-status` - Registrar API convergence
- **zero-trust**: DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants

#### Bug Fixes

- Resolved type errors from codegen overwriting manual fixes
- Fixed `post()` usage for to-markdown endpoints to resolve async type error
- Added least-privilege permissions to all workflow jobs
- Reverted erroneous removal of rulesets resource methods and types
- Resolved prettier formatting errors in codegen output

#### Deprecations

The following resources now include `@deprecated` annotations on some methods:

`accounts`, `addressing`, `ai-gateway`, `aisearch`, `api-gateway`, `billing`, `cloudforce-one`, `custom-nameservers`, `dns`, `email-routing`, `email-security`, `filters`, `firewall`, `images`, `intel`, `keyless-certificates`, `kv`, `logpush`, `origin-tls-client-auth`, `page-shield`, `pages`, `pipelines`, `radar`, `rate-limits`, `registrar`, `rulesets`, `ssl`, `user`, `workers`, `workers-for-platforms`, `zero-trust`, `zones`

#### Get started

- [Download TypeScript SDK v6.0.0 ↗︎](https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0)
- [TypeScript SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/typescript/)
- [Full Changelog ↗︎](https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md)

Apr 29, 2026

[<h2>Instant Bank Payments via Link</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now pay for Cloudflare services directly from your bank account using [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

#### What changed

[Link ↗︎](https://link.co/) now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.

![Instant Bank Payments via Link at checkout](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=413,height=562,format=webp/_astro/2026-04-29-instant-bank-payments-link.ChGd-t7M.png)

#### How to use it

1. During checkout, select your bank account from your saved Link payment methods.
2. Confirm the payment.

After your first Link authentication, your bank account is available for future purchases without re-entering details.

#### Who is eligible

Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.

Bank-based Link payments appear in your billing history with the payment method shown as `link` and last four digits as `0000`. For details, refer to the [Instant Bank Payments via Link documentation](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

Apr 28, 2026

[<h2>Direct access to Support from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-direct-support-navigation/)

[Support](https://developers.cloudflare.com/support/)

#### Direct access to Support from the dashboard

The **Support** button in the dashboard global navigation header now takes you directly to the [Cloudflare Support Portal ↗︎](https://support.cloudflare.com), eliminating the previous dropdown menu.

This change ensures that when you need help, you spend less time navigating the UI and more time getting the answers you need.

#### What changed?

- **Previous behavior**: Selecting **? Support** opened a dropdown menu with various links (Help Center, Cloudflare Community, etc.).
- **New behavior**: Selecting **Support** immediately redirects your current tab to the Support Portal.

To learn more about the resources available to you, refer to the [Cloudflare Support documentation ↗︎](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Apr 27, 2026

[<h2>Structured error responses for Cloudflare 5xx errors</h2>](https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow [RFC 9457 (Problem Details for HTTP APIs) ↗︎](https://www.rfc-editor.org/rfc/rfc9457) and include a `Retry-After` HTTP header on retryable codes.

#### Changes

**5xx coverage.** Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.

**Fault attribution.** The `error_category` field tells agents where the fault lies:

- `origin` (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in `retry_after`.
- `cloudflare` (500) — Cloudflare's fault, not the website or the request. Short retry.
- `ssl` (525, 526) — the origin's TLS configuration is broken. Do not retry.

**Retry-After header.** Retryable codes (500, 502, 504, 520-524) include a `Retry-After` HTTP header matching the `retry_after` body field. Non-retryable codes (525, 526) do not include the header.

#### Negotiation behavior

| Request header sent | Response format |
| --- | --- |
| `Accept: application/json` | JSON (`application/json` content type) |
| `Accept: application/problem+json` | JSON (`application/problem+json` content type) |
| `Accept: application/json, text/markdown;q=0.9` | JSON |
| `Accept: text/markdown` | Markdown |
| `Accept: text/markdown, application/json` | Markdown (equal `q`, first-listed wins) |
| `Accept: */*` | HTML (default) |

#### Availability

Available now for all zones on all plans.

#### Get started

Get JSON response for error 522:

```bash
curl -s --compressed -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/522" | jq .
```

Check presence of the `Retry-After` HTTP header associated with the JSON response for error 521:

```bash
curl -s --compressed -D - -o /dev/null -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/521" | grep -i retry-after
```

References:

- [RFC 9457 — Problem Details for HTTP APIs ↗︎](https://www.rfc-editor.org/rfc/rfc9457)
- [Cloudflare 5xx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)

Apr 27, 2026

[<h2>Resource Tagging enters public beta</h2>](https://developers.cloudflare.com/changelog/post/2026-04-27-resource-tagging-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Resource Tagging](https://developers.cloudflare.com/resource-tagging/)

Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.

#### What's included

- **Broad resource type support** — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the [full list of supported resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/).
- **Powerful filtering** — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.
- **Account and zone-level endpoints** — Full CRUD operations across both scopes.
- **Token-based authentication** — Tagging supports [Account Owned Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) that persist independently of individual users, so your automation keeps running through credential rotations and team changes.
- **Flexible role support** — Super Administrators, Workers Admins, and Tag Admins can all manage tags.

#### API-first by design

The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.

#### Dashboard UI

You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to **Manage Account** > **Resource Tagging** to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.

![Tagged Resources dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2874,height=1234,format=webp/_astro/tagged-resources-dashboard.Dg5WvwiN.png)

#### What's coming next

In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.

#### Current limitations

- `PUT` replaces all tags on a resource (no partial update). Use the [GET, merge, PUT workflow](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/#add-a-single-tag) to modify individual tags safely.
- `DELETE` removes all tags from a resource. To remove a single tag, PUT the remaining tags back.
- Querying tags for a resource that has never been tagged returns `500` instead of `404`. This is a known beta limitation.

To get started, refer to the [Resource Tagging documentation](https://developers.cloudflare.com/resource-tagging/).

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

Apr 23, 2026

[<h2>Audit Logs v2 — Organization-level support</h2>](https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.

To retrieve organization-level audit logs, use the following endpoint:

```bash
GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit
```

This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.

Note

Organization-level audit logs are separate from account-level audit logs. Actions performed within a specific account continue to be available via the account-level Audit Logs UI, Audit Logs v2 API, and Logpush.

For more information, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

Apr 23, 2026

[<h2>Go SDK v6.10.0 Released</h2>](https://developers.cloudflare.com/changelog/post/2026-04-23-go-sdk-v6.10.0/)

[SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) [Go SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)

#### v6.10.0

In this release, you'll see a number of breaking changes. This is primarily due to changes in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries.

**Please ensure you read through the list of changes below before moving to this version** - this will help you understand any down or upstream issues it may cause to your environments.

#### Breaking Changes

See the [v6.10.0 Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md) for before/after code examples and actions needed for each change.

#### Abuse Reports - Registrar WHOIS Report Field Removals

Several fields have been removed from `AbuseReportNewParamsBodyAbuseReportsRegistrarWhoisReportRegWhoRequest`:

- `RegWhoGoodFaithAffirmation`
- `RegWhoLawfulProcessingAgreement`
- `RegWhoLegalBasis`
- `RegWhoRequestType`
- `RegWhoRequestedDataElements`

#### AI Search - Instance Params Restructured

The `InstanceNewParams` and `InstanceUpdateParams` types have been significantly restructured. Many fields have been moved or removed:

- `InstanceNewParams.TokenID`, `Type`, `CreatedFromAISearchWizard`, `WorkerDomain` removed
- `InstanceUpdateParams` — most configuration fields removed (including `IndexMethod`, `IndexingOptions`, `MaxNumResults`, `Metadata`, `Paused`, `PublicEndpointParams`, `Reranking`, `RerankingModel`, `RetrievalOptions`, `RewriteModel`, `RewriteQuery`, `ScoreThreshold`, `SourceParams`, `Summarization`, `SummarizationModel`, `SystemPromptAISearch`, `SystemPromptIndexSummarization`, `SystemPromptRewriteQuery`, `TokenID`, `CreatedFromAISearchWizard`, `WorkerDomain`)
- `InstanceSearchParams.Messages` field removed along with `InstanceSearchParamsMessage` and `InstanceSearchParamsMessagesRole` types

#### AI Search - InstanceItem Service Removed

The `InstanceItemService` type has been removed. The items sub-resource at `client.AISearch.Instances.Items` no longer exists in the non-namespace path. Use `client.AISearch.Namespaces.Instances.Items` instead.

#### AI Search - Token Types Removed

The following types have been removed from the `ai_search` package:

- `TokenDeleteResponse`
- `TokenListParams` (and associated `TokenListParamsOrderBy`, `TokenListParamsOrderByDirection`)

#### Email Security - Investigate Move Return Type Change

The `Investigate.Move.New()` method now returns a raw slice instead of a paginated wrapper:

- `New()` returns `*[]InvestigateMoveNewResponse` instead of `*pagination.SinglePage[InvestigateMoveNewResponse]`
- `NewAutoPaging()` method removed

#### Hyperdrive - Config Params Restructured

The `ConfigEditParams` type lost its `MTLS` and `Name` fields. The `HyperdriveMTLSParam` type lost `MTLS` and `Host` fields. The `Host` field on origin config changed from `param.Field[string]` to a plain `string`.

#### IAM - UserGroupMember Params and Return Types Changed

The `UserGroupMemberNewParams` struct has been restructured and the `New()` method now returns a paginated response:

- `UserGroupMemberNewParams.Body` renamed to `UserGroupMemberNewParams.Members`
- `UserGroupMemberNewParamsBody` renamed to `UserGroupMemberNewParamsMember`
- `UserGroupMemberUpdateParams.Body` renamed to `UserGroupMemberUpdateParams.Members`
- `UserGroupMemberUpdateParamsBody` renamed to `UserGroupMemberUpdateParamsMember`
- `UserGroups.Members.New()` returns `*pagination.SinglePage[UserGroupMemberNewResponse]` instead of `*UserGroupMemberNewResponse`

#### IAM - UserGroup List Direction Type Changed

The `UserGroupListParams.Direction` field changed from `param.Field[string]` to `param.Field[UserGroupListParamsDirection]` (typed enum with `asc`/`desc` values).

#### Pipelines - Delete Methods Now Return Typed Responses

Several delete methods across Pipelines now return typed responses instead of bare error:

- `Pipelines.DeleteV1()` returns `(*PipelineDeleteV1Response, error)` instead of `error`
- `Pipelines.Sinks.Delete()` returns `(*SinkDeleteResponse, error)` instead of `error`
- `Pipelines.Streams.Delete()` returns `(*StreamDeleteResponse, error)` instead of `error`

#### Queues - Message Response Types Removed

The following response envelope types have been removed:

- `MessageBulkPushResponseSuccess`
- `MessagePushResponseSuccess`
- `MessageAckResponse` fields `RetryCount` and `Warnings` removed

#### Secrets Store - Pagination Wrapper Removal and Type Changes

Methods now return direct types instead of `SinglePage` wrappers, and several internal types have been removed. Associated `AutoPaging` methods have also been removed:

- `Stores.New()` returns `*StoreNewResponse` instead of `*pagination.SinglePage[StoreNewResponse]`
- `Stores.NewAutoPaging()` method removed
- `Stores.Secrets.BulkDelete()` returns `*StoreSecretBulkDeleteResponse` instead of `*pagination.SinglePage[StoreSecretBulkDeleteResponse]`
- `Stores.Secrets.BulkDeleteAutoPaging()` method removed
- Removed types: `StoreDeleteResponse`, `StoreDeleteResponseEnvelopeResultInfo`, `StoreSecretDeleteResponse`, `StoreSecretDeleteResponseStatus`, `StoreSecretBulkDeleteResponse` (old shape), `StoreSecretBulkDeleteResponseStatus`, `StoreSecretDeleteResponseEnvelopeResultInfo`
- `StoreNewParams` restructured (old `StoreNewParamsBody` removed)
- `StoreSecretBulkDeleteParams` restructured

#### Stream - AudioTracks Return Type Change

The `AudioTracks.Get()` method now returns a dedicated response type instead of a paginated list. The `GetAutoPaging()` method has been removed:

- `Get()` returns `*AudioTrackGetResponse` instead of `*pagination.SinglePage[Audio]`
- `GetAutoPaging()` method removed

#### Stream - Clip Type Removal and Return Type Change

The `Clip.New()` method now returns the shared `Video` type. The following types have been entirely removed:

- `Clip`, `ClipPlayback`, `ClipStatus`, `ClipWatermark`

#### Stream - Copy and Clip Params Field Removals

- `ClipNewParams.MaxDurationSeconds`, `ThumbnailTimestampPct`, `Watermark` removed
- `CopyNewParams.ThumbnailTimestampPct`, `Watermark` removed

#### Stream - Download and Webhook Changes

- `DownloadNewResponseStatus` type removed
- `WebhookUpdateResponse` and `WebhookGetResponse` changed from `interface{}` type aliases to full struct types

#### Zero Trust - Access AI Control MCP Portal Union Types Removed

The following union interface types have been removed:

- `AccessAIControlMcpPortalListResponseServersUpdatedPromptsUnion`
- `AccessAIControlMcpPortalListResponseServersUpdatedToolsUnion`
- `AccessAIControlMcpPortalReadResponseServersUpdatedPromptsUnion`
- `AccessAIControlMcpPortalReadResponseServersUpdatedToolsUnion`

#### Features

#### Vulnerability Scanner (`client.VulnerabilityScanner`)

**NEW SERVICE:** Full vulnerability scanning management

- **CredentialSets** - CRUD for credential sets ( `New`, `Update`, `List`, `Delete`, `Edit`, `Get`)
- **Credentials** - Manage credentials within sets ( `New`, `Update`, `List`, `Delete`, `Edit`, `Get`)
- **Scans** - Create and manage vulnerability scans ( `New`, `List`, `Get`)
- **TargetEnvironments** - Manage scan target environments ( `New`, `Update`, `List`, `Delete`, `Edit`, `Get`)

#### AI Search - Namespaces (`client.AISearch.Namespaces`)

**NEW SERVICE:** Namespace-scoped AI Search management

- `New()`, `Update()`, `List()`, `Delete()`, `ChatCompletions()`, `Read()`, `Search()`
- **Instances** - Namespace-scoped instances ( `New`, `Update`, `List`, `Delete`, `ChatCompletions`, `Read`, `Search`, `Stats`)
- **Jobs** - Instance job management ( `New`, `Update`, `List`, `Get`, `Logs`)
- **Items** - Instance item management ( `List`, `Delete`, `Chunks`, `NewOrUpdate`, `Download`, `Get`, `Logs`, `Sync`, `Upload`)

#### Browser Rendering - Devtools (`client.BrowserRendering.Devtools`)

**NEW SERVICE:** DevTools protocol browser control

- **Session** - List and get devtools sessions
- **Browser** - Browser lifecycle management ( `New`, `Delete`, `Connect`, `Launch`, `Protocol`, `Version`)
- **Page** - Get page by target ID
- **Targets** - Manage browser targets ( `New`, `List`, `Activate`, `Get`)

#### Registrar (`client.Registrar`)

**NEW:** Domain check and search endpoints

- `Check()` - `POST /accounts/{account_id}/registrar/domain-check`
- `Search()` - `GET /accounts/{account_id}/registrar/domain-search`

**NEW:** Registration management (`client.Registrar.Registrations`)

- `New()`, `List()`, `Edit()`, `Get()`
- `RegistrationStatus.Get()` - Get registration workflow status
- `UpdateStatus.Get()` - Get update workflow status

#### Cache - Origin Cloud Regions (`client.Cache.OriginCloudRegions`)

**NEW SERVICE:** Manage origin cloud region configurations

- `New()`, `List()`, `Delete()`, `BulkDelete()`, `BulkEdit()`, `Edit()`, `Get()`, `SupportedRegions()`

#### Zero Trust - DLP Settings (`client.ZeroTrust.DLP.Settings`)

**NEW SERVICE:** DLP settings management

- `Update()`, `Delete()`, `Edit()`, `Get()`

#### Radar

- `AgentReadiness.Summary()` - Agent readiness summary by dimension
- `AI.MarkdownForAgents.Summary()` - Markdown-for-agents summary
- `AI.MarkdownForAgents.Timeseries()` - Markdown-for-agents timeseries

#### IAM (`client.IAM`)

- `UserGroups.Members.Get()` - Get details of a specific member in a user group
- `UserGroups.Members.NewAutoPaging()` - Auto-paging variant for adding members
- `UserGroups.NewParams.Policies` changed from required to optional

#### Bot Management

- `ContentBotsProtection` field added to `BotFightModeConfiguration` and `SubscriptionConfiguration` ( `block`/ `disabled`)

#### Deprecations

None in this release.

#### Get started

- [Download Go SDK v6.10.0 ↗︎](https://github.com/cloudflare/cloudflare-go/releases/tag/v6.10.0)
- [Go SDK documentation ↗︎](https://developers.cloudflare.com/api/sdks/go/)
- [Migration Guide ↗︎](https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md)

Apr 22, 2026

[<h2>Custom dashboards available to all customers</h2>](https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/)

[Analytics](https://developers.cloudflare.com/analytics/) [Log Explorer](https://developers.cloudflare.com/log-explorer/)

Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.

This update significantly expands the data available for visualization. Build charts based on any of the **100+ datasets** available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.

#### Log Explorer integration

Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.

#### Key benefits

- **Unified visibility**: Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.
- **Flexible monitoring**: Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.
- **Expanded limits**: Log Explorer customers can create up to **100 dashboards** (up from 25 for standard customers).

![Custom Dashboards home page showing dashboard list and chart previews](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1079,height=793,format=webp/_astro/customdashboardshome.BIpSvImM.jpg)

To get started, refer to the [Custom Dashboards documentation](https://developers.cloudflare.com/analytics/custom-dashboards/).

Apr 21, 2026

[<h2>Network Overview page in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-04-21-network-overview-page/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

A new **Network Overview** page in the Cloudflare dashboard gives you a single starting point for network security and connectivity products.

From the Network Overview page, you can:

- **Connect resources with [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)** - Create tunnels to connect your infrastructure to Cloudflare without exposing it to the public Internet.
- **Monitor traffic with Network Flow** - Get real-time visibility into traffic volume from your routers.
- **Configure Address Maps** - Map dedicated static IPs or BYOIP prefixes to specific hostnames.
- **Explore Magic Transit and Cloudflare WAN** - Set up DDoS protection for your networks and connectivity for your branch offices and data centers.

To find it, go to [**Networking** ↗︎](https://dash.cloudflare.com/?to=/:account/magic-networks/overview) in the dashboard sidebar.

If you already use [Magic Transit](https://developers.cloudflare.com/magic-transit/), [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/), or other Cloudflare network services products, your existing experience is unchanged.

![Network Overview page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1650,height=1362,format=webp/_astro/network-overview.4FLDtULW.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/3/#page","headline":"Core platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
