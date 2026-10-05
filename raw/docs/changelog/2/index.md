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

Sep 30, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.2033.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/)

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

For Zero Trust documentation, see: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/ For Consumer documentation, see: https://developers.cloudflare.com/warp-client/

Sep 30, 2026

[<h2>Pay for AI inference with Machine Payments</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway now supports Machine Payments in beta. With Machine Payments, clients can use the x402 protocol to pay for eligible inference requests directly from a stablecoin wallet instead of maintaining a prepaid credit balance.

Machine Payments is available for the `/ai/run` endpoint with select open models. To request x402 payment, authenticate with a Cloudflare API token and include the Cloudflare-specific `Payment-Method: x402` header:

```bash
curl -iX POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Payment-Method: x402" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "z-ai/glm-4.7-flash",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }
  }'
```

An x402-compatible client handles the payment challenge, signs an authorization from the client's wallet, and retries the request. Machine Payments currently requires customers to be based in the United States and have a credit card on file.

For prerequisites, eligible models, and transaction details, refer to [Machine Payments (x402)](https://developers.cloudflare.com/ai-gateway/features/machine-payments/).

Sep 30, 2026

[<h2>Role-based access control for Browser Isolation policies</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the *Isolate* action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

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

Sep 30, 2026

[<h2>WAF Release - 2026-09-30</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new detections to enhance protection against a specific GitLab path traversal vulnerability, alongside advanced generic rules targeting HTTP request smuggling, directory traversal, and command injection attempts.

**Key Findings**

- CVE-2026-85706: A path traversal vulnerability affecting GitLab.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...cb14ded8 | N/A | Broken Access Control - Directory Traversal | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...0364bd7e | N/A | HTTP Request Smuggling - Request Body Anomaly - Beta | Log | Block | This rule is merged into the original rule "HTTP/2 Request Smuggling - Request Body Anomaly" (ID: ...1489d892). |
| Cloudflare Managed Ruleset | ...d498a69a | N/A | Command Injection - Generic 8 - body - Beta | Disabled | Disabled | This rule is merged into the original rule "Command Injection - Generic 8 - body" (ID: ...413592e2). |
| Cloudflare Managed Ruleset | ...87ae8cfc | N/A | GitLab - Path Traversal- CVE:CVE-2026-85706 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...549f7356 | N/A | Generic - Request routing cache inconsistency | N/A | Block | This is a new detection. |

Sep 30, 2026

[<h2>WAF Release - Scheduled changes for 2026-10-06</h2>](https://developers.cloudflare.com/changelog/post/scheduled-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Announcement Date | Release Date | Release Behavior | Legacy Rule ID | Rule ID | Description | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09-22 | 2026-10-06 | Log | N/A | ...a056caff | Command Injection - Generic 8 - uri - Beta | This rule will be merged into the original rule "Command Injection - Generic 8 - uri" (ID: ...ee159e2e). |
| 2026-09-30 | 2026-10-06 | Log | N/A | ...7206c737 | F5 BIG-IP - UnAuth Heap-Overflow - CVE:CVE-2026-94127 | This is a new detection. |

Sep 29, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.2028.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-windows-beta/)

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

Sep 29, 2026

[<h2>Cloudflare One Client for macOS (version 2026.8.2028.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-macos-beta/)

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

Sep 29, 2026

[<h2>Identify model overuse and potential savings with User Insights</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway User Insights now gives you more context about the traffic flowing through your gateway. It shows what users and agents are doing with AI, and where a selected model may be more capable than a task requires.

On the analysis side, User Insights groups conversations by task, tracks conversation turns, and helps you compare model fit with cost and latency.

![User Insights task and model analysis grouped by task categories](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1434,height=606,format=webp/_astro/user-insights-task-analysis.CS2pm7wg.png)

The Potential Savings view highlights requests that may work with faster or less expensive models without compromising output quality. These are the same signals that Cloudflare's [Auto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/) uses to select a model based on task and cost.

![Potential Savings view comparing tasks and suggested models](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=669,format=webp/_astro/user-insights-potential-savings.C7j_Gjcn.png)

These new insights are available to all AI Gateway customers at no additional cost. For more information, refer to [User Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/).

Sep 29, 2026

[<h2>Connect multiple clients to one Browser Run session</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/) sessions now accept multiple concurrent connections. Before, a session accepted only one connection at a time, and other Workers had to wait until that connection closed. Now multiple Workers can connect to the same browser at the same time.

Each `puppeteer.connect()` call opens its own Chrome DevTools Protocol (CDP) connection. Create a separate browser context for each request to keep its pages, cookies, and storage apart from other clients.

```js
const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
const context = await browser.createBrowserContext();

try {
	const page = await context.newPage();
	await page.goto("https://example.com");
	// ...
} finally {
	await context.close();
	await browser.disconnect(); // keep the shared browser running
}
```

```ts
const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
const context = await browser.createBrowserContext();

try {
	const page = await context.newPage();
	await page.goto("https://example.com");
	// ...
} finally {
	await context.close();
	await browser.disconnect(); // keep the shared browser running
}
```

Sharing sessions means fewer new browsers to launch, less cold-start time, and fewer [concurrent browsers](https://developers.cloudflare.com/browser-run/limits/) counted against your limits.

Concurrent connections require `@cloudflare/puppeteer` version 1.1.0 or later.

Refer to [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/) for a full example.

Sep 29, 2026

[<h2>Custom Container instance types no longer have a disk to memory ratio limit</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) custom instance types no longer limit disk based on memory. Previously, a custom instance type could have a maximum of 2 GB of disk for each 1 GiB of memory. You can now allocate up to the 20 GB disk maximum to any custom instance type.

Use this to run workloads that need more disk than memory, such as workloads with large container images, datasets, or build caches. The maximum image size is the same as the instance disk space, so more disk also lets you deploy larger images.

For example, a custom instance type with 1 vCPU and 3 GiB of memory was previously limited to 6 GB of disk. It can now use 20 GB:

```jsonc
{
	"containers": [
		{
			"image": "./Dockerfile",
			"instance_type": {
				"vcpu": 1,
				"memory_mib": 3072,
				"disk_mb": 20000,
			},
		},
	],
}
```

```toml
[[containers]]
image = "./Dockerfile"

  [containers.instance_type]
  vcpu = 1
  memory_mib = 3_072
  disk_mb = 20_000
```

The other custom instance type constraints do not change, including the minimum of 3 GiB of memory per vCPU. For the full list, refer to [Custom Instance Types](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types).

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

Sep 29, 2026

[<h2>Workers Cache — mark cached responses stale with invalidate()</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Cache](https://developers.cloudflare.com/workers/cache/) now supports `invalidate()`, the soft counterpart of `purge()`. `purge()` deletes matching cached responses, so the next request is a cache miss. `invalidate()` keeps them but marks them stale, so the cache revalidates them with your Worker instead.

To revalidate a response, the cache sends your Worker a conditional request built from the validators stored with it — for example, `If-None-Match` carrying the cached `ETag`. If your Worker answers `304 Not Modified`, the cache keeps the stored body. If your Worker answers with a full `200` response, that response replaces the cached one.

`invalidate()` accepts the same options as `purge()`: `tags`, `pathPrefixes`, or `purgeEverything`. It follows the same per-entrypoint scoping and resolves to the same result object. Call it as `ctx.cache.invalidate()`, or import `cache` from `cloudflare:workers` and call `cache.invalidate()`.

Use `invalidate()` when one call covers many cached responses but only some of them changed. Your Worker needs to emit `ETag` or `Last-Modified` and answer matching conditional requests with `304`. Each unchanged response then costs a validator check instead of a full regeneration:

*src/index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		if (request.method === "POST") {
			// Write the updated catalog, then mark every cached product page stale.
			await syncCatalog(env, await request.json());
			await ctx.cache.invalidate({ tags: ["products"] });
			return new Response("Synced");
		}

		const product = await getProduct(env, request);
		const etag = `"${product.revision}"`;
		const headers = {
			"Cache-Control": "public, max-age=86400",
			"Cache-Tag": "products",
			ETag: etag,
		};

		// The product has not changed since it was cached. Answer 304, and the
		// cache keeps the body it already has.
		if (request.headers.get("If-None-Match") === etag) {
			return new Response(null, { status: 304, headers });
		}

		return new Response(renderProductPage(product), { headers });
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request, env, ctx): Promise<Response> {
		if (request.method === "POST") {
			// Write the updated catalog, then mark every cached product page stale.
			await syncCatalog(env, await request.json());
			await ctx.cache.invalidate({ tags: ["products"] });
			return new Response("Synced");
		}

		const product = await getProduct(env, request);
		const etag = `"${product.revision}"`;
		const headers = {
			"Cache-Control": "public, max-age=86400",
			"Cache-Tag": "products",
			ETag: etag,
		};

		// The product has not changed since it was cached. Answer 304, and the
		// cache keeps the body it already has.
		if (request.headers.get("If-None-Match") === etag) {
			return new Response(null, { status: 304, headers });
		}

		return new Response(renderProductPage(product), { headers });
	},
} satisfies ExportedHandler<Env>;
```

For more information, refer to [Invalidate cached responses](https://developers.cloudflare.com/workers/cache/purge/#invalidate-cached-responses).

Sep 28, 2026

[<h2>Browser Run adds WebMCP to Kitesurf and moves to document.modelContext</h2>](https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/) now works in [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) sessions as well as [Lab sessions](https://developers.cloudflare.com/browser-run/features/webmcp/#get-started). Both backends use the `document.modelContext` API from the [WebMCP Community Group draft ↗︎](https://webmachinelearning.github.io/webmcp/). Lab sessions no longer expose `navigator.modelContextTesting`.

To list and run page tools:

- **Chrome DevTools**: Use the **Application** > **WebMCP** panel in the live view of a Lab session or in the [Kitesurf playground ↗︎](https://kitesurf.dev/).
- **AI agents**: Start [Chrome DevTools MCP](https://developers.cloudflare.com/browser-run/features/webmcp/#using-an-ai-agent) with the `--category-experimental-webmcp` flag to add the `list_webmcp_tools` and `execute_webmcp_tool` tools.
- **CDP clients**: Use the `WebMCP` CDP domain.

Sep 28, 2026

[<h2>Invalidate cached content instead of purging it</h2>](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now invalidate cached content instead of purging it. Invalidation marks matching content as stale. On the next request, Cloudflare revalidates the content with your origin. If your origin responds with `304 Not Modified`, Cloudflare reuses the cached content instead of downloading it again.

Use invalidation to refresh a group of assets when only some of them have changed. For example, invalidate all content that shares a cache tag. Cloudflare reuses unchanged assets instead of downloading them again. This requires your origin to return an `ETag` or `Last-Modified` header and support conditional requests.

Invalidation supports the same selectors as purge: URLs, cache tags, hostnames, URL prefixes, and everything. To invalidate content, send a `POST` request to the new `invalidate_cache` endpoint:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"tags":["product-images"]}'
```

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

Your cache settings determine whether Cloudflare serves stale content while it revalidates. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. To stop serving cached content, purge it instead.

Invalidation requests count toward the same [rate limits](https://developers.cloudflare.com/cache/guides/invalidate-cache/#limits) as purge requests.

Purge behavior for Cache Reserve also changes with this release. For details, refer to [Cache Reserve purge behavior](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#purge-behavior).

For more information, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/).

Sep 28, 2026

[<h2>Purge now forces a cache miss for Cache Reserve content</h2>](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

Purge requests now force a cache miss for [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) content, regardless of purge type. Previously, purging by cache tag, hostname, prefix, or everything marked matching Cache Reserve content for revalidation. Purging by URL already removed content from Cache Reserve and is unchanged.

This change applies to purge requests from the API and the dashboard. Cache Reserve now handles purges the same way as the edge cache.

#### Cost impact

After a purge, the next request for affected content is a Cache Reserve miss. Your origin must deliver the content in full, even if it has not changed. Cloudflare then writes the content to Cache Reserve again, which is billed as a [Class A operation](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#pricing).

Purging by tag, hostname, prefix, or everything does not delete content from Cache Reserve right away. Matching content continues to incur storage costs until a later request replaces it or its retention period ends.

If you frequently purge Cache Reserve content by tag, hostname, prefix, or everything, review the effect on your origin egress and Cache Reserve usage.

#### Keep revalidating Cache Reserve content

To keep content in Cache Reserve and revalidate it instead, send the same request to the new `invalidate_cache` endpoint:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"tags":["product-images"]}'
```

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

If your origin responds with `304 Not Modified`, Cloudflare reuses the stored content instead of fetching it from your origin again. Compared with purging, invalidation reduces origin egress but not Cache Reserve operations. Updating the stored content after a `304` response is still a Class A operation. Invalidating by URL also updates the stored content when you send the request, which is a Class A operation.

Unlike the previous purge behavior, invalidation can serve stale content while it revalidates if your cache settings allow it. This applies only to copies in the edge cache, not to content served from Cache Reserve. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. For details, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/#stale-content-during-revalidation).

Sep 28, 2026

[<h2>Cloudflare CLI is now in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)

[Workers](https://developers.cloudflare.com/workers/) [Cloudflare CLI](https://developers.cloudflare.com/cf/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun

```
npm install --global cf
```

```
yarn global add cf
```

```
pnpm add --global cf
```

```
bun add --global cf
```

```sh
cf auth login
```

With `cf`, you can:

- **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
- **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
- **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
- **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.

`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

Sep 27, 2026

[<h2>Call Workflows declared in \`exports\` through \`ctx.exports\`</h2>](https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

A Worker can now call the Workflows it declares in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of its Wrangler configuration through [`ctx.exports`](https://developers.cloudflare.com/workers/runtime-apis/context/#exports). You no longer need a `workflows` binding to call a Workflow from the Worker that defines it.

Each Workflow is keyed by class name, and has the same API as a Workflow binding:

*src/index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		const instance = await ctx.exports.MyWorkflow.create({
			params: { name: "World" },
		});
		return Response.json({ id: instance.id });
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request, env, ctx): Promise<Response> {
		const instance = await ctx.exports.MyWorkflow.create({
			params: { name: "World" },
		});
		return Response.json({ id: instance.id });
	},
} satisfies ExportedHandler<Env>;
```

A `workflows` binding and a `workflow` export with the same `name` share their instances. You can move a Workflow from a binding to an export without losing its instances.

`wrangler dev`, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), and the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) run Workflows on `ctx.exports` locally. Local development requires Wrangler 4.142.0, `@cloudflare/vite-plugin` 1.61.0, or `@cloudflare/vitest-plugin` 1.3.0 or above.

In Vitest, `introspectWorkflow()` and `introspectWorkflowInstance()` still need a Workflow binding. To introspect a Workflow declared in `exports`, add a [test-only binding](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#introspect-workflows-declared-in-exports) to it.

For more information, refer to [Call a Workflow through `ctx.exports`](https://developers.cloudflare.com/workflows/build/workers-api/#call-a-workflow-through-ctxexports).

Sep 25, 2026

[<h2>Subscribe to Browser Run crawl events</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/)

[Browser Run](https://developers.cloudflare.com/browser-run/) [Queues](https://developers.cloudflare.com/queues/)

[Browser Run crawl jobs](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) can publish lifecycle events to [Cloudflare Queues](https://developers.cloudflare.com/queues/). Subscribe to started, updated, and finished events to track progress or trigger downstream processing without polling.

To create an account-level subscription, run the following command:

npmyarnpnpm

```
npx wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

```
yarn wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

```
pnpm wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

For payload examples, refer to the [Browser Run event schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/#browser-run).

Sep 25, 2026

[<h2>Managed Rulesets supported in Unified Routing</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-unified-routing-managed-rulesets/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Managed Rulesets are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode.

For the full list of feature availability, refer to [Check feature availability before upgrading](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Sep 25, 2026

[<h2>Suppress recipients for one sending domain</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/)

[Email Service](https://developers.cloudflare.com/email-service/)

[Email Sending suppressions](https://developers.cloudflare.com/email-service/concepts/suppressions/) now have a **scope**:

- **`account`**: The suppression applies to every sending domain and subdomain in your account. This is the default.
- **`sending_domain`**: The suppression applies to one sending domain only. A suppression for `mail.myappexample.com` does not block mail from `myappexample.com`.

Most importantly, Email Sending now automatically creates bounce and complaint suppressions at the sending-domain level. This provides greater granularity by preventing an issue with one sending domain from suppressing the recipient across your entire account.

To add a suppression for one sending domain in the dashboard, go to **Email Sending** > **Suppressions** and select **Sending domain** in **Scope**. Imports can also set a scope for each row or a default scope.

In the API, pass `scope` when you create the suppression:

```bash
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/email/sending/suppressions \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "email": "user@example.net",
    "scope": { "type": "sending_domain", "value": "mail.myappexample.com" }
  }'
```

The [suppressions API](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/) returns `scope` on every suppression. To list the suppressions for one domain, use `scope_type=sending_domain&scope_value=mail.myappexample.com`. If you omit `scope`, the API creates an `account` suppression, so existing integrations continue to work.

Refer to [Suppression lists](https://developers.cloudflare.com/email-service/concepts/suppressions/#suppression-scope) and [Manage suppressions](https://developers.cloudflare.com/email-service/configuration/suppressions/) for details.

Sep 25, 2026

[<h2>WAF Release - 2026-09-25 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This update provides immediate defense against critical vulnerabilities affecting WordPress and JFrog Artifactory, including path traversal, local file inclusion (LFI), cross-site scripting (XSS), and authentication bypass exploits.

**Key Findings**

- CVE-2026-87902: A high-severity Path Traversal and Local File Inclusion (LFI) vulnerability affecting WordPress. Unauthenticated attackers can exploit this flaw to read arbitrary files on the host server, potentially exposing sensitive configuration data or system files.
- CVE-2026-42018 & CVE-2026-82329: Critical authentication bypass vulnerabilities affecting JFrog Artifactory. Successful exploitation allows unauthenticated attackers to bypass security controls and achieve unauthorized access to the Artifactory instance.

**Impact**

We strongly recommend that administrators apply the latest vendor patches for WordPress and JFrog Artifactory to fully secure origin servers.

Detailed Rule Changes

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...70a43f96 | N/A | Wordpress - Path Traversal, Local File Inclusion - CVE:CVE-2026-87902 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...909a4db4 | N/A | Wordpress - XSS - Comment | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c797ef03 | N/A | JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-42018 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...a813ac74 | N/A | JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-82329 | N/A | Block | This is a new detection. |

Sep 25, 2026

[<h2>Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs</h2>](https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/)

[Workers](https://developers.cloudflare.com/workers/)

[Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) in Workers now support more of the OpenTelemetry span API, so you can instrument more of your code and record errors directly on your spans.

- **`tracing.startSpan(name)`** creates a span without making it the active span, and returns it. Other spans do not nest under it. Call `span.end()` when the operation is complete.
- **`tracing.getActiveSpan()`** returns the currently active span. Use it to annotate the current span from helper functions and libraries without passing the span object through your code. Outside any custom span, it returns the invocation's root span.
- **`span.recordException(exception)`** records an exception event on a span. It accepts an `Error`, a string, or an object with a `code`, `name`, or `message`.
- **`span.setAttributes(attributes)`** sets multiple attributes at once. `setAttribute()` and `setAttributes()` now return the span, so you can chain calls.

*src/index.jsjs*

```js
import { tracing } from "cloudflare:workers";

export default {
	async fetch(request, env) {
		const user = await authenticate(request, env);

		// Annotate the invocation's root span
		tracing.getActiveSpan()?.setAttributes({
			"user.id": user.id,
			"user.plan": user.plan,
		});

		const span = tracing.startSpan("load-profile");
		try {
			return Response.json(await loadProfile(env, user.id));
		} catch (err) {
			span.recordException(err);
			throw err;
		} finally {
			span.end();
		}
	},
};
```

*src/index.tsts*

```ts
import { tracing } from "cloudflare:workers";

export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const user = await authenticate(request, env);

		// Annotate the invocation's root span
		tracing.getActiveSpan()?.setAttributes({
			"user.id": user.id,
			"user.plan": user.plan,
		});

		const span = tracing.startSpan("load-profile");
		try {
			return Response.json(await loadProfile(env, user.id));
		} catch (err) {
			span.recordException(err as Error);
			throw err;
		} finally {
			span.end();
		}
	},
};
```

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/2/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
