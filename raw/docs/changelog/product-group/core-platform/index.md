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

Oct 2, 2026

[<h2>30 days of analytics data on every plan</h2>](https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/)

[Analytics](https://developers.cloudflare.com/analytics/)

Every plan now gets at least 30 days of analytics data. Adaptive analytics datasets, such as HTTP requests, security events, and DNS analytics, retain at least 31 days of data for Free and Pro domains, and you can query up to 30 days in a single request. Previously, Free and Pro domains could see between 24 hours and 8 days of history depending on the dataset.

A full month of history lets you investigate an issue after it happens, compare today with the same day in previous weeks, and tell a one-time spike from a longer trend. The change applies in the Cloudflare dashboard, in [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), and through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Domain analytics also now live in one place. In the Cloudflare dashboard, select a domain and go to **Analytics** to see Traffic, Performance, Security, Cache, Origin, DNS, and Visitors as tabs that share one time range and one set of filters. Account-level analytics are under **Observability** > **Analytics**.

This change does not alter which datasets or fields your plan can access. Aggregated datasets, such as `httpRequests1hGroups`, keep their existing per-plan limits. To check the exact retention and query window for a zone or account, query the [settings](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/) for each dataset.

For plan-specific limits, refer to [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/#availability), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#availability), and [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/#node-limits-and-availability).

Oct 2, 2026

[<h2>Workers Observability logs and traces in Custom Dashboards</h2>](https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/)

[Analytics](https://developers.cloudflare.com/analytics/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)**, let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).

Oct 2, 2026

[<h2>hash\_in\_range() is globally available for HTTP products</h2>](https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/)

[Rules](https://developers.cloudflare.com/rules/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:

```txt
hash_in_range(0, 100, cf.random_seed) < 10
```

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:

```txt
hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)
```

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).

Oct 2, 2026

[<h2>Protect Quick Tunnels with email authentication</h2>](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.

```sh
cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com
```

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

- A single email address: `--allowed-mail alice@example.com`
- Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
- Every address on a domain: `--allowed-mail '*@example.com'`

Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

Oct 1, 2026

[<h2>Account members can self-serve create Account API tokens</h2>](https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Account API token creation is no longer limited to Super Administrators. Members with the **API Token Provisioning** role can now create Account API tokens via the Dashboard, API, Terraform, or CF CLI, making it easier for developers and platform teams to provision credentials without depending on a Super Administrator for Account API Token Provisioning.

![Creating an Account API Token via CF CLI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1540,height=818,format=webp/_astro/2026-10-01-account-api-token-provisioning.Dn0G5DUa.png)

#### What's new

- **Delegated creation**: Members with the **API Token Provisioning** role can create Account API tokens from the dashboard. Administrators can grant this role through the dashboard, API, or Terraform.
- **OAuth support for token creation**: OAuth clients that request the `account_api_tokens:create` scope, starting with Cloudflare CLI, can create Account API tokens.
- **Account API token permissions limited to the creator’s access at creation time**: Members can only create an Account API Token using the permissions they already have. For OAuth-created tokens, permissions are also limited to the scopes granted during authorization.
- **Creator attribution and visibility**: Account API tokens now include creator metadata. Super Administrators and Administrators can view all Account API tokens in an account, while members with the **API Token Provisioning** role can only view tokens they created.

For more information, refer to [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/), [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/), and [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

Oct 1, 2026

[<h2>Handle missing values with coalesce()</h2>](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/)

[Rules](https://developers.cloudflare.com/rules/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:

```txt
http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")
```

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).

Oct 1, 2026

[<h2>Compare dynamic values in Rules expressions</h2>](https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:

```txt
http.request.uri.path ne raw.http.request.uri.path
```

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).

Sep 30, 2026

[<h2>Logpush is now available on all plans with usage-based pricing</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

- **Internal exports**: 25 GB per month, then $0.03 per additional GB.
- **External exports**: 25 GB per month, then $0.10 per additional GB.
- **Transformations**: 1 GB per month, then $0.04 per additional GB.

R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

[<h2>Transformers are now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

[<h2>Monetization Gateway closed beta</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/)

[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)

Monetization Gateway is now available in closed beta. Sellers can use it to charge agents for access to APIs, Model Context Protocol (MCP) tools, sites, and datasets.

Sellers (domain owners) define which requests require payment, the cost, and where the payment should be sent. Buyers receive the payment instructions, sign an authorization, and receive the resource after the payment has been settled. The Monetization Gateway uses the x402 protocol to handle payment authorization within the HTTP request flow.

To learn more, request access in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway), review the [Monetization Gateway documentation](https://developers.cloudflare.com/monetization-gateway/), or read the [blog ↗︎](https://blog.cloudflare.com/monetization-gateway-beta/).

Sep 29, 2026

[<h2>Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

- **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
- **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs**, select **Columns**, and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

| Field | Description |
| --- | --- |
| `OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`. |
| `Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`. |
| `SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions. |
| `SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions. |
| `DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel. |

For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

Sep 22, 2026

[<h2>concat() now supports up to 32 arguments</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/)

[Rules](https://developers.cloudflare.com/rules/)

The `concat()` function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data.

A common use case is adding a request header that sends context to your origin. The following Rulesets API request adds a Request Header Transform Rule to an existing `http_request_late_transform` phase ruleset. Its 18-argument expression combines request and network information into one header value:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "ref": "add_request_context_header",
    "description": "Add request context for the origin",
    "expression": "true",
    "action": "rewrite",
    "action_parameters": {
      "headers": {
        "X-Request-Context": {
          "operation": "set",
          "expression": "concat(\"ip=\", to_string(ip.src), \";country=\", ip.src.country, \";host=\", http.host, \";method=\", http.request.method, \";path=\", http.request.uri.path, \";query=\", http.request.uri.query, \";ray-id=\", cf.ray_id, \";asn=\", to_string(ip.src.asnum), \";user-agent=\", http.user_agent)"
        }
      }
    }
  }'
```

For more information, refer to the [`concat()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) and [HTTP request header modification](https://developers.cloudflare.com/rules/transform/request-header-modification/).

Sep 18, 2026

[<h2>Filter DDoS attack traffic from Logpush jobs</h2>](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:

```json
{
	"filter_attack_traffic": true
}
```

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).

Sep 18, 2026

[<h2>cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027</h2>](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

Sep 17, 2026

[<h2>Create additional Free accounts through the dashboard and API</h2>](https://developers.cloudflare.com/changelog/post/2026-09-15-free-account-creation/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're expanding how customers create accounts across Cloudflare, making it easier to self-serve account creation in the dashboard, automate standalone account creation with user-owned API tokens or OAuth access tokens, and create Free accounts directly within Enterprise Organizations.

#### What's New

**Dashboard account creation:** All cloudflare customers can create additional Free accounts directly through self-serve flows in the Cloudflare dashboard.

**Enterprise Organization account creation:** Super Administrators can now create up to five Free accounts directly within an Enterprise Organization. This makes it easier to provision and manage additional accounts and directly associate them with your Organization.

**API and OAuth account creation:** Customers can now create standalone Free accounts programmatically via User-owned API tokens or OAuth access tokens.

For more information:

- [Create a Free account in the dashboard](https://developers.cloudflare.com/fundamentals/account/create-account/)
- [Create an account via the API](https://developers.cloudflare.com/api/resources/accounts/methods/create/)
- [Create Free accounts in an Enterprise Organization](https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/#create-new-accounts)

Sep 17, 2026

[<h2>Validate Rulesets changes before deployment</h2>](https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration.

The Cloudflare dashboard performs this validation automatically when you create or update rules from **Security** > **Security rules** or **Rules** > **Overview**.

Supported Rulesets API mutation endpoints now also accept the `dry_run=true` query parameter. A dry run performs the same authorization and server-side validation checks as the requested change, but does not persist or publish it. Successful operations that normally return a `200` response return `result: null`. Operations that normally return `204` continue to do so.

#### API example

Add `dry_run=true` to a Rulesets API request to validate it without creating the ruleset:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets?dry_run=true" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "Custom firewall rules",
    "kind": "zone",
    "phase": "http_request_firewall_custom",
    "rules": [
      {
        "action": "block",
        "expression": "ip.src.country eq \"GB\"",
        "description": "Block requests from the United Kingdom",
        "enabled": true
      }
    ]
  }'
```

For more information, refer to [Validate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/).

Sep 4, 2026

[<h2>Enterprise customers can self-serve CDN upload limits up to 5 GB</h2>](https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/)

Enterprise customers can now configure a zone's CDN **Maximum Upload Size** up to 5 GB directly from the **Network** page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.

The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.

Refer to [Cache upload limits](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits) and [Workers request body size limits](https://developers.cloudflare.com/workers/platform/limits/#request-and-response-limits) for details.

Sep 2, 2026

[<h2>Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</h2>](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

- **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
- **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
- **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.

The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

Aug 28, 2026

[<h2>Improved dataset configuration in Log Explorer</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-dataset-configuration/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.

- **Grouped field selection** organizes fields by category and shows the number selected in each group.
- **Field details** identify each field's data type and mark required or deprecated fields.
- **Bulk controls** let you select all fields or reset the selection to the dataset defaults.
- **Ingestion filters** let you ingest all events or only events that match your conditions.

These controls are available when you add a dataset or select **Actions** > **Edit** for an enabled dataset.

For more information, refer to [Configure fields and filters](https://developers.cloudflare.com/log-explorer/manage-datasets/#configure-fields-and-filters).

Aug 26, 2026

[<h2>Delete Log Explorer datasets</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete**, and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.

Aug 26, 2026

[<h2>Azure Functions-based Microsoft Sentinel connector deprecation</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/)

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) [Logs](https://developers.cloudflare.com/logs/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

- [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
- [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
- [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)

For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).

Aug 21, 2026

[<h2>Enriched 403 responses for the Cloudflare API</h2>](https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare API `403 Forbidden` responses now include a `documentation_url` field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.

**What's New**

**Enriched 403 error responses**: When a Cloudflare API request is denied, the error response now includes a `documentation_url` field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.

**Faster troubleshooting**: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.

**Better support for tools and agents**: Agents can use the \\documentation\_url\` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.\`

Example 403 response:

```json
{
  "success": false,
  "errors": [
    {
      "code": 10000,
      "message": "Forbidden",
      "documentation_url": "https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list"
    }
  ],
  "messages": [],
  "result": null
}
```

For more info:

- [Browse the Cloudflare API documentation](https://developers.cloudflare.com/api/)
- [Review Cloudflare roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
- [Review API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/)

Aug 21, 2026

[<h2>Saved login profiles for returning users</h2>](https://developers.cloudflare.com/changelog/post/2026-08-21-one-click-login/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare Dashboard users can now save login profiles on a device for faster sign-in on future visits.

![Saved login profiles for returning users](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2212,height=1544,format=webp/_astro/2026-08-21-one-click-login.CbMATqrT.png)

**What's New**

**Save login profiles on a device**: After a successful sign-in, users can choose to save a login profile on that device. Saved profiles store the email address, login method, and last-used profile locally in the browser.

**Faster sign-in for returning users**: Saved profiles appear directly on the login page. Selecting one can prefill the email field for password logins or resume the associated SSO or social login flow.

Up to five login profiles can be saved per device, and saved profiles can be removed from the profile list at any time.

For more info:

- [Log in to Cloudflare](https://developers.cloudflare.com/fundamentals/user-profiles/login/)
- [Set up dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)

Aug 21, 2026

[<h2>Improved SCIM 2.0 group synchronization</h2>](https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Dashboard SCIM now supports replacing groups using HTTP `PUT`, as defined by [RFC 7644 section 3.5.1 ↗︎](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1). This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.

**What's New**

**Group replacement via `PUT`**: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

- [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

Aug 20, 2026

[<h2>Optional OAuth scopes</h2>](https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're announcing the GA of Optional OAuth Scopes.

OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .

#### What's New

**Optional Scopes:** OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.

**Scope Selection:** On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.

**Templates:** The consent screen now includes **Read Only** and **Full Access** templates to make scope selection faster and easier.

**Search:** Users can now search scopes in the consent screen.

Learn how to [select client scopes](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#select-scopes) and [edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/#page","headline":"Core platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
