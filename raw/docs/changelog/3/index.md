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

Sep 25, 2026

[<h2>See every release and gradual deployment on Workers Metrics charts</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) charts now show every release in the selected time range, including the full progression of [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/). This makes it easier to correlate changes in memory, CPU time, errors, or latency with the code that was serving traffic.

![Memory usage chart showing a gradual deployment as a shaded rollout band](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-memory-usage.C5rkO7VY.png)

A gradual deployment appears as a single rollout across the chart, with shading that increases as more traffic moves to the new version. Hover over a rollout to see the previous and new versions, the rollout duration, and the traffic percentage configured at each step.

![Invocations chart showing traffic shifting from the previous version to the new version during a gradual deployment](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-invocations.BvQMAKnw.png)

Use these annotations to:

- **Find when a regression started** — See which traffic percentage was configured when errors, latency, CPU time, or wall time changed.
- **Compare rollout stages** — Check whether a metric changed as more traffic moved to the new version.
- **Confirm rollbacks** — Rollbacks appear as separate release events, so you can check whether metrics recovered after a rollback.

Direct deployments that send 100% of traffic to a single version still appear as individual markers. Nearby direct deployments are grouped to reduce visual clutter. Versions that are only uploaded, or only configured at 0%, do not appear on metrics charts.

To view release annotations, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics).

Sep 24, 2026

[<h2>RFC 8509 root key trust anchor sentinel support</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/)

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

1.1.1.1 now supports [RFC 8509 ↗︎](https://datatracker.ietf.org/doc/html/rfc8509) root key trust anchor sentinels. They let you check whether the responding resolver trusts a DNSSEC root key ahead of a key rollover.

To check for KSK-2024 (key tag 38696), query DNSSEC-signed names in `dnstest.dev`:

```sh
# On a sentinel-aware resolver that trusts KSK-2024:

# Returns NOERROR with an A answer.
dig @1.1.1.1 root-key-sentinel-is-ta-38696.dnstest.dev. A +noall +comments +answer

# Returns SERVFAIL without an answer.
dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +noall +comments +answer

# CD bypasses sentinel processing and returns the original A answer.
dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +cdflag +noall +comments +answer
```

For background on DNSSEC validation, refer to [DNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/).

Sep 24, 2026

[<h2>MCP server portals are now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) are now generally available to all Cloudflare customers. A portal gives users one endpoint for approved Model Context Protocol (MCP) servers. Cloudflare Access logs tool, prompt, and resource activity.

Since the open beta, MCP server portals have added:

- [Gateway routing](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway) for HTTP logging and data loss prevention (DLP) scanning
- [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies) that control how portals reduce tool definitions and token use
- [Static OAuth client credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials) for providers that do not support Dynamic Client Registration
- [Session management](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions) for reconnecting servers and changing authorizations from the portal
- [Service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token) for autonomous agents and machine-to-machine access
- [Logpush support](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) for exporting portal activity to external storage or a security information and event management (SIEM) system

To create a portal and connect an MCP client, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

Sep 24, 2026

[<h2>R2 bandwidth usage metrics</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/)

[R2](https://developers.cloudflare.com/r2/)

New [R2](https://developers.cloudflare.com/r2/) product-level **Metrics** page in the Cloudflare dashboard shows bandwidth usage. You can view usage across all buckets or per bucket.

[Go to **R2 Metrics** ↗](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 upload and download throughput across all buckets over 24 hours](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1443,height=747,format=webp/_astro/r2-bandwidth-metrics.9lTC-zY2.png)

Bandwidth throughput is split by object upload and download. The [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) exposes the same bandwidth usage metrics that power the dashboard for your queries and analytics.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

Sep 24, 2026

[<h2>Declare Workflows in the \`exports\` configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

You can now declare the Workflows a Worker defines in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of your Wrangler configuration file. Previously, a Worker could only define a Workflow through a `workflows` binding, even when the Worker never called the Workflow itself.

Key each entry by the name of the class that extends `WorkflowEntrypoint`:

```jsonc
{
	"exports": {
		"MyWorkflow": {
			"type": "workflow",
			"name": "my-workflow",
			"limits": {
				"steps": 25000,
			},
			"schedules": ["0 * * * *"],
		},
	},
}
```

```toml
[exports.MyWorkflow]
type = "workflow"
name = "my-workflow"
schedules = [ "0 * * * *" ]

  [exports.MyWorkflow.limits]
  steps = 25_000
```

A `workflow` export accepts the same settings as a `workflows` binding: `limits`, `schedules`, and `default_retention`. When you run `wrangler deploy`, Wrangler creates or updates the Workflow with these settings.

You can declare a Workflow as both a binding and an export. Both declarations must use the same class, and cannot set the same setting to different values.

A `workflows` binding to a Workflow in another Worker cannot use the same `name` as a Workflow export in this Worker. Workflow names are unique per account.

Workflow exports require Wrangler 4.139.0 or above.

For more information, refer to [Declare Workflows in `exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports).

Sep 23, 2026

[<h2>Durable Object name search now supports 128 characters</h2>](https://developers.cloudflare.com/changelog/post/2026-09-24-durable-object-name-search-limit/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Durable Object name searches in the Cloudflare dashboard now accept up to 128 characters, up from 20.

Search results and recent invocation lists show up to 128 characters before being truncated with an ellipsis. This limit applies to the object filter on the **Metrics** tab and object search in **Data Studio**.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/) and [Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/).

Sep 23, 2026

[<h2>Traffic Destination selector in Gateway policies</h2>](https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Destination** selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN.

#### Available traffic destination values

| UI name | API value | Description |
| --- | --- | --- |
| Internet | `internet` | Traffic to the public Internet |
| Cloudflare WAN | `cloudflare_wan` | Traffic through a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connection |
| Cloudflare Tunnel | `cloudflare_tunnel` | Traffic to a private origin through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) |
| Cloudflare One Client | `device_client` | Traffic to another device running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) |
| Mesh | `mesh` | Traffic through a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node |

The selector uses the `net.offramp.type` API field in both HTTP and Network policies.

| UI name | API example |
| --- | --- |
| Traffic Destination | `net.offramp.type == "internet"` |

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

Sep 23, 2026

[<h2>View transformation analytics in Images</h2>](https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now view account-level analytics for your Images transformation usage.

Go to **Images & Stream** > **Transformations** > **Analytics** to view sampled estimates of image transformation request traffic, including:

- Requests by source, split between URL-based transformations and Images binding transformations
- Top zones, transformation configurations, and origin hosts for URL-based requests
- Top Worker scripts for Images binding requests

Use these analytics to identify the zones, configurations, origins, and Workers generating the most image transformation requests.

Sep 23, 2026

[<h2>Add Mesh participants with guided onboarding</h2>](https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) now makes it faster to add and manage participants from the dashboard. Select **Add participant** from **Networking** > **Mesh** to deploy a [Mesh node](https://developers.cloudflare.com/mesh/get-started/) or find the information needed to connect a [client device](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).

![Adding a Cloudflare Mesh node through the guided dashboard workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=680,format=webp/_astro/guided-participant-onboarding-clicks.B0r-5ElX.gif)

The updated dashboard includes the following improvements:

- **More Mesh node deployment options** — Install a node on Linux, Kubernetes, Docker Compose, or Docker CLI. The dashboard provides requirements, commands, configuration, and links for each method. Refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/) for container deployment details.
- **Client device installation guidance** — Access platform-specific [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) installers, mobile QR codes, and your Cloudflare One organization name. Use the organization name to log in from the client after installation.
- **Unified participant management** — View [Mesh nodes and enrolled client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/#1-enroll-the-cloudflare-one-client) in one table. Search devices, filter participants by type or status, open device details, and load additional results from each participant source. If one source fails, participants from the other source remain available while you retry the request.

You must still install the Cloudflare One Client, log in to your organization, and test the connection.

For complete setup instructions, refer to [Get started with Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/).

Sep 22, 2026

[<h2>Automatically manage inactive Access service tokens</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit.

To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule. Cleanup runs gradually in the background, so eligible tokens may not be disabled or deleted immediately.

For configuration instructions, refer to [Manage inactive service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#manage-inactive-service-tokens).

Sep 22, 2026

[<h2>Private MCP server support for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).

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

Sep 22, 2026

[<h2>WAF Release - 2026-09-22</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new threat detections to enhance protection against Server-Side Request Forgery (SSRF) attempts using non-standard IP notations or jar loopback payloads, alongside new defenses against Server-Side Template Injection (SSTI) targeting Jinja environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...5f21b651 | N/A | SSRF - Cloud,Link-Local non-standard IP notation | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...0f0313d6 | N/A | SSRF - Block jar HTTP loopback payload | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...75cd912a | N/A | SSRF - Local non-standard IP notation | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...a1ba83f6 | N/A | SSTI - Jinja Dangerous Globals Chain | Log | Block | This is a new detection. |

Sep 22, 2026

[<h2>Workers Builds now supports Cursor Origin</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/)

[Workers](https://developers.cloudflare.com/workers/)

Workers Builds now supports repositories hosted in Cursor Origin. Connect a Cursor Origin repository to automatically build and deploy production changes, preview non-production branches, and see build status in pull requests.

Pushes to your production branch automatically build and deploy your Worker. When you enable [non-production branch builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds), each branch receives a version-specific preview URL and a stable preview URL that follows the latest build.

Cloudflare posts build status and preview links to the Cursor Origin pull request and creates a check run for each triggered build.

To get started, install the [Cloudflare app in Cursor ↗︎](https://cursor.com/codebase/settings/apps/public/cloudflare), choose the Cursor Origin repositories Cloudflare can access, and follow the prompts to configure your Worker build. For details, refer to the [Cursor Origin integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/).

Sep 22, 2026

[<h2>Test every pull request in an isolated environment with Worker Previews</h2>](https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/)

[Workers](https://developers.cloudflare.com/workers/)

You can now test every change you make in an isolated, production-like environment with [Worker Previews ↗︎](https://blog.cloudflare.com/worker-previews/). [Each Preview](https://developers.cloudflare.com/workers/previews/) runs under the same Worker with its own code, configuration, URL, and observability, isolated from production and every other Preview.

#### Configure each Preview

Define the variables, bindings, and settings that new Previews start with in the [`previews` block of your Wrangler configuration file](https://developers.cloudflare.com/workers/previews/configuration/). Set secrets with Wrangler commands. You can override one Preview without changing production or other Previews.

For [Durable Objects](https://developers.cloudflare.com/workers/previews/resources/#durable-objects) and [Containers](https://developers.cloudflare.com/workers/previews/resources/#containers), Cloudflare automatically provisions separate namespaces, storage, apps, and instances for every Preview. State changes, sessions, memory, migrations, and concurrent tests remain scoped to that Preview. To isolate KV, D1, R2, or another account-level resource, [bind the Preview to a separate resource](https://developers.cloudflare.com/workers/previews/resources/).

![Diagram comparing production with three Previews, each with its own URL, code, configuration, and Durable Object state](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1370,format=webp/_astro/preview-resource-isolation.CyeUXRJS.png)

#### Deploy and share every change

Use Wrangler 4.135.0 or later to [deploy a Preview](https://developers.cloudflare.com/workers/previews/get-started/):

```sh
npx wrangler preview
```

Or [connect your repository to Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-preview-builds) to create Previews automatically and post their URLs to pull requests.

Each Preview gets a [stable URL](https://developers.cloudflare.com/workers/previews/#urls) that updates with every push, so reviewers always see the latest changes. Each deployment also gets an immutable URL, so you can compare or return to an exact version.

After you create a Preview, use the environment breadcrumb next to your Worker's name to switch between Production and every Preview:

![Worker dashboard showing the Preview dropdown and an overview of bindings, metrics, and deployments](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2386,height=1304,format=webp/_astro/previews-dash-overview.BL1UHZHT.png)

#### Inspect and revise before production

Each Preview has its own [logs, errors, metrics, and traces](https://developers.cloudflare.com/workers/previews/test-and-debug/). Send traffic to its URL, inspect what happened, push a fix, and verify the next deployment before production.

![Preview Observability tab showing success and error events for a pull request](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1418,height=1236,format=webp/_astro/preview-observability.COYT0y5H.png)

#### Use production-like hostnames

Serve Preview URLs on `workers.dev`, a [custom domain](https://developers.cloudflare.com/workers/previews/custom-domains/), or both. Custom domains let authentication providers, cookies, cross-origin resource sharing (CORS), and OAuth redirects work as they will in production. You can also protect Preview URLs with Cloudflare Access.

Configure a domain for Preview traffic from the Worker's **Domains** tab:

![Domains tab showing a custom domain configured for Preview traffic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2876,height=1454,format=webp/_astro/customdomainonly.8AG_6tc-.png)

For setup instructions and current limitations, refer to the [Worker Previews documentation](https://developers.cloudflare.com/workers/previews/).

Sep 21, 2026

[<h2>Cloudflare One Client for macOS (version 2026.8.1755.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- Fixed Extra Logging failing to capture packets across all interfaces.
- Fixed an issue that could prevent remote diagnostics from completing.
- Fixed DNS connectivity checks failing on IPv6-only networks.
- Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
- Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 21, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.1755.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 21, 2026

[<h2>Browser Run adds session and DevTools methods to browser bindings</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/) browser bindings now provide typed methods for session management and DevTools operations. You can acquire a session, connect a browser client, create Live View URLs, manage targets, and close sessions without constructing HTTP requests.

The new `acquire()` and `launch()` methods also accept [`outboundByHost`](https://developers.cloudflare.com/browser-run/features/outbound-workers/). This lets you route requests for selected hostnames through another Worker, including a Worker that adds authentication or reaches a private service.

```js
const connection = await env.BROWSER.launch({
	outboundByHost: {
		"private.example.test": env.OUTBOUND,
	},
});
```

```ts
const connection = await env.BROWSER.launch({
	outboundByHost: {
		"private.example.test": env.OUTBOUND,
	},
});
```

Use `connectSession(sessionId)` when you need to acquire and connect in separate steps. The method returns a session-pinned `webSocket` Fetcher for a CDP client.

The binding also includes session methods for Live View, active sessions, session history, limits, session details, and cleanup. The nested `devtools` binding provides typed methods for browser version information, protocol descriptions, and target operations such as listing, creating, activating, and closing targets.

Refer to the [Browser binding API documentation](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) for method signatures and the [outbound Worker feature guide](https://developers.cloudflare.com/browser-run/features/outbound-workers/) for routing examples.

Sep 21, 2026

[<h2>Give teammates access to specific Workers directly from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/)

[Workers](https://developers.cloudflare.com/workers/)

You can now grant teammates scoped access to specific Workers directly from the Workers dashboard.

Go to your Worker and click **Invite**.

![Invite button on a Worker's overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2366,height=1134,format=webp/_astro/invite-button.BtZmWRrA.png)

Enter the teammate's email address, choose the appropriate access level, and click **Invite**.

![Dialog for inviting a teammate and choosing their access level](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=748,height=724,format=webp/_astro/invite-dialog.Bo5P-iat.png)

You can grant a user one of the following access levels:

- **Metadata Read-Only**: View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.
- **Content Read-Only**: Read Worker code, settings, and observability data without the ability to modify or deploy changes.
- **Editor**: Update and deploy a Worker without the ability to delete it.
- **Admin**: Everything included with Editor, plus the ability to delete the Worker.

If the teammate is already an account member, they will receive access to the Worker immediately. If they are not an account member, Cloudflare will send them an invitation to join the account, and they will receive access to the Worker after accepting the invitation.

Only account members with the Super Administrator role can invite users from a Worker's dashboard.

For details about available roles and scopes, refer to the [Workers roles and permissions documentation](https://developers.cloudflare.com/workers/authorization/workers/).

Sep 18, 2026

[<h2>Inspect logs, network requests, and DOM in Session Recordings</h2>](https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run Session Recordings](https://developers.cloudflare.com/browser-run/features/session-recording/) now include an **Inspect** panel, giving you more context to understand what happened during a browser session without having to reproduce it.

![Inspecting logs, network requests, and the DOM in a Browser Run Session Recording](https://developers.cloudflare.com/images/browser-run/session-recording-inspect.gif)

The **Logs** tab lets you search captured console output and filter messages by level. The **Network** tab shows each request's method, status, headers, payload, response, and timing waterfall, with the option to download the session's network activity as a HAR file.

You can also [retrieve recorded network activity via API](https://developers.cloudflare.com/browser-run/features/session-recording/#retrieve-network-activity-via-api) as raw JSON or a HAR file for use in your own debugging and analysis workflows.

The **DOM** tab provides an expandable view of the page structure at the end of the recording and lets you copy the reconstructed HTML. For sessions with multiple browser tabs, the Inspect panel updates to show data for the tab selected in the recording viewer.

To get started, enable recording when launching a browser session. After the session closes, open **Browser Run** > **Runs** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run/runs) and select the recording icon next to the session.

Refer to the [Session recording documentation](https://developers.cloudflare.com/browser-run/features/session-recording/) for setup instructions and current limits.

Sep 18, 2026

[<h2>Unified Routing generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Unified Routing is generally available for Cloudflare WAN and Magic Transit.

Unified Routing improves the integration between Cloudflare One and the standard connectivity onramps supported by Cloudflare WAN. It is capable of many new features including Automatic Return Routing, BGP and custom client subnets.

We recommend Unified Routing for all new accounts.

For details, refer to [Cloudflare WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) and [Magic Transit traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#unified-routing).

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

[<h2>Delete Workflow instances individually or in batches</h2>](https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

You can now delete one or up to 100 Workflow instances and their stored state via the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/) or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. [Storage billing](https://developers.cloudflare.com/workflows/reference/pricing/#storage-usage) is based on the average daily peak.

Delete one instance by calling [`delete()`](https://developers.cloudflare.com/workflows/build/workers-api/#delete) on its handle:

```ts
const instance = await env.MY_WORKFLOW.get("instance-abc");
await instance.delete();
```

If a Workflow deletes its own instance, execution stops during `await instance.delete()`. Code after the call does not run.

Delete multiple instances by calling [`deleteBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch) on the Workflow binding:

```ts
const result = await env.MY_WORKFLOW.deleteBatch([
	"instance-abc",
	"instance-def",
]);

console.log(result.deleted);
console.log(result.errors);
```

The batch result contains `{ id }` entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.

Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use `latest` to delete the most recently created instance. Use `--local` against a local `wrangler dev` session:

*instance-ids.jsonjson*

```json
["instance-abc", "instance-def"]
```

```sh
npx wrangler workflows instances delete my-workflow <INSTANCE_ID>
npx wrangler workflows instances delete my-workflow <INSTANCE_ID> <INSTANCE_ID>
npx wrangler workflows instances delete my-workflow latest
npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json
npx wrangler workflows instances delete my-workflow <INSTANCE_ID> --local
```

For more information, refer to [Delete Workflow instances](https://developers.cloudflare.com/workflows/build/trigger-workflows/#delete-workflow-instances), [`delete`](https://developers.cloudflare.com/workflows/build/workers-api/#delete), and [`deleteBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch).

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/3/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
