---
title: Changelogs
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

Apr 30, 2026

[<h2>Shared dictionaries passthrough now in open beta</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/)

[Speed](https://developers.cloudflare.com/speed/)

[Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/) ([RFC 9842 ↗︎](https://www.rfc-editor.org/rfc/rfc9842.html)) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.

#### What changed

In passthrough mode, Cloudflare:

- Forwards the `Use-As-Dictionary` and `Available-Dictionary` headers between client and origin without modification.
- Treats `dcb` (Dictionary-Compressed Brotli) and `dcz` (Dictionary-Compressed Zstandard) as valid `Content-Encoding` values end to end, without recompressing them.
- Extends the cache key to vary on `Available-Dictionary` and `Accept-Encoding` so each delta-compressed variant is cached correctly.

Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching `Use-As-Dictionary` headers, and producing deltas in response to `Available-Dictionary` requests. Cloudflare handles the transport and the cache.

In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.

Shared dictionaries work with browsers that advertise `dcb` or `dcz` in `Accept-Encoding`. Today, this includes Chrome 130 or later and Edge 130 or later.

#### Get started

Turn on passthrough for your zone with a single API call:

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode" \
	--request PATCH \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"value": "passthrough"
	}'
```

You can also turn it on under **Speed** > **Settings** > **Content Optimization** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization). For full origin setup instructions and a working test recipe, refer to [Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/), or try the live demo at [canicompress.com ↗︎](https://canicompress.com/).

Apr 30, 2026

[<h2>WAF Release - 2026-04-30 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This emergency release introduces a new rule to block a cPanel & WHM Authentication Bypass related to CVE-2026-41940.

**Key Findings**

- CVE-2026-41940: A critical authentication bypass vulnerability in cPanel & WHM allows unauthenticated remote attackers to bypass authentication mechanisms and gain unauthorized administrative access to the web hosting control panel. This vulnerability affects the session validation logic, enabling attackers to craft malicious requests that circumvent normal authentication checks.

**Impact**

Successful exploitation allows unauthenticated attackers to gain administrative control over affected cPanel & WHM installations. This leads to complete server compromise, potential theft or manipulation of hosted data, and significant service disruption across managed environments.

We strongly recommend applying official vendor patches for cPanel & WHM immediately to address the underlying vulnerability.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...eb2b9e2f | N/A | cPanel - Auth Bypass - CVE:CVE-2026-41940 | N/A | Block | This is a new detection. |

Apr 30, 2026

[<h2>Web Analytics adds Navigation Type filtering and reporting</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics now supports **Navigation Type** reporting and filtering.

This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.

Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of "Back-forward" navigations versus "Back-forward Cache", those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.

The same applies for regular "Navigate" entries — where "Navigate Cache", "Navigate Prefetch Cache" and "Prerender" would provide instant document retrieval — and "Reload", where "Reload cache" would be more optimal.

A high volume of "Reload" entries can also indicate a potential stability problem with your website.

By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.

For more information, refer to [Navigation Types](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/#navigation-types).

#### Key benefits

- **Monitor Cache Effectiveness:** See how often your site is served from the HTTP cache or bfcache.
- **Identify Performance Bottlenecks:** Filter by the different types to understand performance opportunity of improving browser cache hit ratio.

#### Analyze navigation types in the Cloudflare dashboard

You can now find the **Navigation Type** dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using "equals", "does not equal", "in", or "not in" matchers.

![Navigation Type filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2646,height=1040,format=webp/_astro/dash-web_analytics-navigation-type-filter.Cculflhp.png)

To check the list of popular navigation types, select **Page views** on the Web Analytics sidebar and scroll down to the bottom:

![Navigation Types list in Page Views tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=500,format=webp/_astro/dash-web_analytics-navigation-types-list.CWaiEQzO.png)

Apr 29, 2026

[<h2>Digital experience tests to authenticated resources and enhanced configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital experience tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via [Cloudflare Secret Store](https://developers.cloudflare.com/secrets-store/).

Digital experience tests also have enhanced configuration options including:

- New HTTP methods (DELETE, PATCH, POST, PUT)
- Secret Store headers, custom plain text headers, and custom request bodies
- Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates

![Digital experience test configuration for Cloudflare Access applications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1374,format=webp/_astro/dex_test_auth_config.CD3G3zb_.png)![Digital experience enhanced test configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1496,format=webp/_astro/dex_test_enhanced_config.Nsv7Vcob.png)

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

Apr 29, 2026

[<h2>Gateway Authorization Proxy and hosted PAC files are now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [hosted PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now generally available for all plan types.

Authorization proxy endpoints add an identity-aware option alongside the existing [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint), using [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication to verify who a user is before applying Gateway filtering — without installing the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.

These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.

To get started, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/).

Apr 29, 2026

[<h2>Hyperdrive support for private databases with Workers VPC</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now connect Hyperdrive to a private database through a [Workers VPC service](https://developers.cloudflare.com/workers-vpc/). This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.

When creating a Hyperdrive configuration in the Cloudflare dashboard, choose **Connect to private database** and then **Workers VPC**. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.

You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:

```sh
npx wrangler hyperdrive create my-vpc-database \
  --service-id <YOUR_VPC_SERVICE_ID> \
  --database <DATABASE_NAME> \
  --user <DATABASE_USER> \
  --password <DATABASE_PASSWORD> \
  --scheme postgresql
```

Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.

To get started, refer to [Connect Hyperdrive to a private database using Workers VPC](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/).

Apr 28, 2026

[<h2>Internet outage notifications for devices</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-internet-outage-notification/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/) will display a dashboard notification when an Internet outage or traffic anomaly may impact a [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) device based on its geographic location or network connection.

This Internet outage and traffic anomaly data is pulled from [Cloudflare Radar ↗︎](https://radar.cloudflare.com/). All Internet outage and traffic anomaly observations can be viewed in the [Radar Outage Center ↗︎](https://radar.cloudflare.com/outage-center).

![Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=314,format=webp/_astro/dex_radar_ux_notification.CpdrUVYA.png)![Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2068,height=909,format=webp/_astro/dex_radar_analytics.GaPxWM6C.png)

Apr 28, 2026

[<h2>Cloudflare One Client speed tests</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-speed-test/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

IT teams can now remotely run speed tests from the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) to Cloudflare's network edge.

Each speed test includes the following metrics:

- Internet speed: download and upload throughput
- Latency: download, upload, unloaded latency, and jitter
- Network quality score: video streaming, webchat/real-time communication (RTC)

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Digital experience** > **Diagnostics** and select **Run diagnostics** to use the feature today.

![Cloudflare One client speed test result](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2906,height=1730,format=webp/_astro/dex_speed_test.DukupcRs.png)

Apr 28, 2026

[<h2>Create and manage DLP detection entries outside of profiles</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-detection-entries-outside-profiles/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now create, view, and manage DLP detection entries outside of profiles.

Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the **Detection entries** section and use them in custom DLP profiles.

For more information, refer to [Configure detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/).

Apr 28, 2026

[<h2>Detect PII records with a new predefined DLP profile</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: **Personally Identifiable Information (PII) Record**.

Most predefined and custom DLP profiles match when any enabled detection entry matches. The **Personally Identifiable Information (PII) Record** profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.

Detection entries included in the profile:

- AU Passport Number
- American Express Card Number
- Diners Club Card Number
- US Driver's License Number
- Email Address
- Full Name
- US Mailing Address
- Mastercard Card Number
- US Individual Tax Identification Number (ITIN)
- US Passport Number
- US Phone Number
- Union Pay Card Number
- United States SSN Numeric Detection
- Visa Card Number

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

Apr 28, 2026

[<h2>Account-level enforce DNS-only</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-enforce-dns-only/)

[DNS](https://developers.cloudflare.com/dns/)

You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new `enforce_dns_only` setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs. This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.

Caution

Enabling this setting exposes your origin IP addresses and removes all Cloudflare protections — including DDoS mitigation, WAF, caching, and all other proxy-based features — for every zone in your account. Use with extreme caution and only after proper [preparations](https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/#preparation).

#### Key characteristics

- **Account-level** — Affects all zones in the account simultaneously with a single API call.
- **Non-destructive** — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.
- **API-only** — Available through the API only, not in the Cloudflare dashboard.

#### What's affected

**Included:** Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.

**Excluded:** Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.

#### Before you enable

- Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.
- Review which origin IPs will become publicly visible through DNS queries.
- Test the API in a staging account before relying on it for incident response.

#### Availability

Available via API to all Cloudflare customers.

For information on how to use it, refer to [Enforce DNS-only developer documentation](https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/) .

Apr 28, 2026

[<h2>Realtime backlog metrics now available for Queues</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues](https://developers.cloudflare.com/queues/), Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:

- **`backlog_count`** — the number of unacknowledged messages in the queue
- **`backlog_bytes`** — the total size of those messages in bytes
- **`oldest_message_timestamp_ms`** — the timestamp of the oldest unacknowledged message

The following endpoints also now include a `metadata.metrics` object on the result field after successful message consumption:

- `/accounts/{account_id}/queues/{queue_id}/messages/pull`
- `/accounts/{account_id}/queues/{queue_id}/messages`
- `/accounts/{account_id}/queues/{queue_id}/messages/batch`

#### Javascript APIs

Call `env.QUEUE.metrics()` to get realtime backlog metrics:

```ts
const {
	backlogCount, // number
	backlogBytes, // number
	oldestMessageTimestamp, // Date | undefined
} = await env.QUEUE.metrics();
```

`env.QUEUE.send()` and `env.QUEUE.sendBatch()` also now return a metrics object on the response.

You can also query these fields via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) or view realtime backlog on the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/queues).

![Queues realtime backlog](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1402,height=494,format=webp/_astro/2026-04-28-queues-metrics.BYi0hgrD.png)

For more information, refer to [Queues metrics](https://developers.cloudflare.com/queues/observability/metrics/).

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

[<h2>Cache Response Rules now support zone versioning</h2>](https://developers.cloudflare.com/changelog/post/2026-04-27-cache-response-rules-zone-versioning/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

Cache Response Rules now work with [Version Management](https://developers.cloudflare.com/version-management/). You can version response-phase cache settings and promote them through environments, just like Cache Rules and other supported configurations.

#### What changed

Previously, Cache Response Rules were excluded from zone versioning. Any response-phase rule you created applied globally across all environments with no way to test changes in staging first. Cache Rules already supported versioning, but the response phase, where you modify `Cache-Control` directives, manage cache tags, and strip headers, did not.

Cache Response Rules are now fully integrated with Version Management. You can create or modify response-phase rules within a version, and those changes stay scoped to that version until promoted.

#### Benefits

- **Safe rollout of cache behavior changes**: Test response-phase rules in a staging environment before promoting to production. Catch unintended caching side effects early.
- **Parity with Cache Rules**: Cache Response Rules now follow the same versioning workflow as Cache Rules, so you can manage all cache configuration through a single promotion pipeline.
- **Independent environment control**: Run different response-phase cache settings per environment. For example, strip `Set-Cookie` headers in staging to validate cacheability without affecting production traffic.

#### Get started

Configure Cache Response Rules in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) under **Caching** > **Cache Rules**, or via the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). For more details, refer to the [Cache Response Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-response-rules/) and the [Version Management documentation](https://developers.cloudflare.com/version-management/).

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

Apr 27, 2026

[<h2>Unified workspace for Brand Protection</h2>](https://developers.cloudflare.com/changelog/post/2026-04-27-unified-workspace-brand-protection/)

[Security Center](https://developers.cloudflare.com/security-center/)

We have introduced a unified investigation workspace within Brand Protection to help analysts manage complex brand portfolios. Instead of jumping between individual queries, you can now consolidate your workflow into a single, cohesive view.

#### What's new

- You can now elect multiple saved queries from your dashboard to generate a consolidated "Combined Matches" view. This allows you to triage results from different brand queries in one unified table
- You can open query extended views in distinct tabs within the Brand Protection dashboard. This enables you to maintain multiple investigation contexts simultaneously and switch between them without losing your place.
- You can reset your workspace using the new "Clear Selection" action, making it easier to pivot between different investigation sets.

#### Key benefits

- Eliminate fragmented workflows by viewing all matches across different query buckets in a single table, reducing the need to click through dozens of individual query pages
- Correlate related campaigns by seeing similar domains or infrastructure patterns that appear across multiple saved queries

Learn more in our [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

Apr 27, 2026

[<h2>WAF Release - 2026-04-27</h2>](https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's release focuses on new improvements to enhance coverage.

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...80cec1dd | N/A | PostgreSQL - SQLi - COPY - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "PostgreSQL - SQLi - COPY - Body (ID: ...e7265a4e). The rule previously known as "PostgreSQL - SQLi - COPY" is now renamed to "PostgreSQL - SQLi - COPY - Body". |
| Cloudflare Managed Ruleset | ...2903de89 | N/A | PostgreSQL - SQLi - COPY - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...1036cfa6 | N/A | PostgreSQL - SQLi - COPY - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...55ff389e | N/A | SQLi - AND/OR MAKE\_SET/ELT - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - AND/OR MAKE\_SET/ELT - Body" (ID: ...252d3934). The rule previously known as "SQLi - AND/OR MAKE\_SET/ELT" is now renamed to "SQLi - AND/OR MAKE\_SET/ELT - Body". |
| Cloudflare Managed Ruleset | ...346487f9 | N/A | SQLi - AND/OR MAKE\_SET/ELT - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...1ac6ceca | N/A | SQLi - AND/OR MAKE\_SET/ELT - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...dd471337 | N/A | SQLi - Common Patterns - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - Common Patterns - Body" (ID: ...cb5d0b9b). The rule previously known as "SQLi - Common Patterns" is now renamed to "SQLi - Common Patterns - Body". |
| Cloudflare Managed Ruleset | ...975c07b7 | N/A | SQLi - Common Patterns - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...05b1b06b | N/A | SQLi - Common Patterns - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...dd0ba3c7 | N/A | SQLi - Equation - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - Equation - Body" (ID: ...c2eb3e7f). The rule previously known as "SQLi - Equation" is now renamed to "SQLi - Equation - Body". |
| Cloudflare Managed Ruleset | ...3d1c2384 | N/A | SQLi - Equation - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...e1149ea6 | N/A | SQLi - Equation - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...205adbb0 | N/A | SQLi - AND/OR Digit Operator Digit - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit - Body" (ID: ...3893c564). The rule previously known as "SQLi - AND/OR Digit Operator Digit" is now renamed to "SQLi - AND/OR Digit Operator Digit - Body". |
| Cloudflare Managed Ruleset | ...ad2abbaa | N/A | SQLi - AND/OR Digit Operator Digit - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...53acbc0d | N/A | SQLi - AND/OR Digit Operator Digit - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...2b45a97d | N/A | SQLi - Benchmark Function - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - Benchmark Function - Body" (ID: ...2ebc44ad). The rule previously known as "SQLi - Benchmark Function" is now renamed to "SQLi - Benchmark Function - Body". |
| Cloudflare Managed Ruleset | ...9889aadc | N/A | SQLi - Benchmark Function - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...491b28e9 | N/A | SQLi - Benchmark Function - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...2aa649de | N/A | SQLi - Comparison - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - Comparison - Body" (ID: ...e7907480). The rule previously known as "SQLi - Comparison" is now renamed to "SQLi - Comparison - Body". |
| Cloudflare Managed Ruleset | ...39e3e013 | N/A | SQLi - Comparison - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...f4bdb492 | N/A | SQLi - Comparison - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...a1ff3b34 | N/A | SQLi - String Concatenation - Body - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - String Concatenation - Headers" (ID: ...2116d2fe).The rule previously known as "SQLi - String Concatenation - Headers" is now renamed to "SQLi - String Concatenation - Body". |
| Cloudflare Managed Ruleset | ...0d0e6c3b | N/A | SQLi - String Concatenation - Headers | Log | Block | This is a new detection.(Former Id was ...846d1940) |
| Cloudflare Managed Ruleset | ...26cc211f | N/A | SQLi - String Concatenation - URI | Log | Block | This is a new detection. (Former Id was ...8fae8c84) |
| Cloudflare Managed Ruleset | ...eacc78ab | N/A | SQLi - SELECT Expression - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - SELECT Expression - Body" (ID: ...d0023a36). The rule previously known as "SQLi - SELECT Expression" is now renamed to "SQLi - SELECT Expression - Body". |
| Cloudflare Managed Ruleset | ...630bb223 | N/A | SQLi - SELECT Expression - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...dcd6efb5 | N/A | SQLi - SELECT Expression - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...18c47cea | N/A | SQLi - ORD and ASCII - Beta | Log | Block | This is a new detection. This rule is merged into the original rule "SQLi - ORD and ASCII- Body" (ID: ...d0d207f9). The rule previously known as "SQLi - ORD and ASCII" is now renamed to "SQLi - ORD and ASCII- Body". |
| Cloudflare Managed Ruleset | ...bdb1618f | N/A | SQLi - ORD and ASCII - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...1d0906b6 | N/A | SQLi - ORD and ASCII - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...9fe4eff5 | N/A | SQLi - Destructive Operations | Log | Block | This is a new detection. |

Apr 24, 2026

[<h2>Network Session Logs now available for all on-ramps</h2>](https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from [proxy endpoints (PAC files)](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) egress — on-ramps that previously did not generate session logs.

Customers who already consume the `zero_trust_network_sessions` dataset via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) or [Log Explorer](https://developers.cloudflare.com/log-explorer/) may see increased log volume if they use these on-ramps.

For field definitions, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/). For traffic analysis, refer to [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

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

[<h2>AAGUID restrictions and AMR matching for Access independent MFA</h2>](https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/) in Cloudflare Access now supports two additional organization-level controls:

- **[Restrict authenticators by AAGUID](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid)** — Limit enrollment to a specific set of WebAuthn authenticators using their [AAGUID ↗︎](https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid). This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new [List](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) type.
- **[AMR matching](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa)** — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the `amr` claim defined in [RFC 8176 ↗︎](https://datatracker.ietf.org/doc/html/rfc8176) and matches supported values such as `hwk`, `otp`, and `fpt` to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.

To get started, refer to [Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/20/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/20/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
