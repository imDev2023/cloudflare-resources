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

Apr 2, 2026

[<h2>BigQuery as Logpush destination</h2>](https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports **BigQuery** as a native destination.

Logs from Cloudflare can be sent to [Google Cloud BigQuery ↗︎](https://cloud.google.com/bigquery) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

For more information, refer to the [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/) documentation.

Apr 1, 2026

[<h2>All Wrangler commands for Workflows now support local development</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

All `wrangler workflows` commands now accept a `--local` flag to target a Workflow running in a local `wrangler dev` session instead of the production API.

You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:

```sh
npx wrangler workflows list --local
npx wrangler workflows trigger my-workflow --local
npx wrangler workflows instances list my-workflow --local
npx wrangler workflows instances pause my-workflow <INSTANCE_ID> --local
npx wrangler workflows instances send-event my-workflow <INSTANCE_ID> --type my-event --local
```

All commands also accept `--port` to target a specific `wrangler dev` session (defaults to `8787`).

For more information, refer to [Workflows local development](https://developers.cloudflare.com/workflows/build/local-development/).

Apr 1, 2026

[<h2>Create, manage, search AI Search instances with Wrangler CLI</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) supports a `wrangler ai-search` command namespace. Use it to manage instances from the command line.

The following commands are available:

| Command | Description |
| --- | --- |
| `wrangler ai-search create` | Create a new instance with an interactive wizard |
| `wrangler ai-search list` | List all instances in your account |
| `wrangler ai-search get` | Get details of a specific instance |
| `wrangler ai-search update` | Update the configuration of an instance |
| `wrangler ai-search delete` | Delete an instance |
| `wrangler ai-search search` | Run a search query against an instance |
| `wrangler ai-search stats` | Get usage statistics for an instance |

The `create` command guides you through setup, choosing a name, source type (`r2` or `web`), and data source. You can also pass all options as flags for non-interactive use:

```sh
wrangler ai-search create my-instance --type r2 --source my-bucket
```

Use `wrangler ai-search search` to query an instance directly from the CLI:

```sh
wrangler ai-search search my-instance --query "how do I configure caching?"
```

All commands support `--json` for structured output that scripts and AI agents can parse directly.

For full usage details, refer to the [Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).

Apr 1, 2026

[<h2>Logs UI refresh</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-logs-ui-refresh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.

![Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2984,height=842,format=webp/_astro/cf1-new-logs-ui.DxF4x0l-.png)

The updated UI includes:

- **Filter by field** - Select any field value to add it as a filter and narrow down your results.
- **Customizable fields** - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.
- **View details** - Select a timestamp to view the full details of a log entry.
- **Switch to classic view** - Return to the previous log viewer interface if needed.

For more information, refer to [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/) and [Gateway activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/).

Apr 1, 2026

[<h2>Routing Section Expansion on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now features an expanded [Routing section ↗︎](https://radar.cloudflare.com/routing) with dedicated sub-pages, providing a more organized and in-depth view of the global routing ecosystem. This restructuring lays the groundwork for additional routing features and widgets coming in the near future.

#### Dedicated sub-pages

The single Routing page has been split into three focused sub-pages:

- [**Overview** ↗︎](https://radar.cloudflare.com/routing) — Routing statistics, IP address space trends, BGP announcements, and the new Top 100 ASes ranking.
- [**RPKI** ↗︎](https://radar.cloudflare.com/routing/rpki) — RPKI validation status, ASPA deployment trends, and per-ASN ASPA provider details.
- [**Anomalies** ↗︎](https://radar.cloudflare.com/routing/anomalies) — BGP route leaks, origin hijacks, and Multi-Origin AS (MOAS) conflicts.

![Screenshot of the routing section menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=574,height=342,format=webp/_astro/routing-section-menu.CEq17il_.png)

#### New widgets

The routing overview now includes a **Top 100 ASes** table ranking autonomous systems by customer cone size, IPv4 address space, or IPv6 address space. Users can switch between rankings using a segmented control.

![Screenshot of the top-100 ASes table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1426,format=webp/_astro/top-100-ases-table.ZBSReN_5.png)

The RPKI sub-page introduces a **RPKI validation** view for per-ASN pages, showing prefixes grouped by RPKI validation status (Valid, Invalid, Unknown) with visibility scores.

![Screenshot of the RPKI validation view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=978,format=webp/_astro/rpki-validation-view.D3eQih4x.png)

#### Improved IP address space chart

The [IP address space ↗︎](https://radar.cloudflare.com/routing) chart now displays both IPv4 and IPv6 trends stacked vertically and is available on global, country, and AS views.

![Screenshot of the IPv4 and IPv6 combined IP space chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1310,format=webp/_astro/combined-ipv4-ipv6-space.DQ5qc8la.png)

Check out the [Radar routing section ↗︎](https://radar.cloudflare.com/routing) to explore the data, and stay tuned for more routing insights coming soon.

Apr 1, 2026

[<h2>New QUIC RTT and delivery rate fields</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/)

[Rules](https://developers.cloudflare.com/rules/)

Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing [`cf.timings.client_tcp_rtt_msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.

Previously, QUIC RTT and delivery rate data was only available via the `Server-Timing: cfL4` response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.timings.client_quic_rtt_msec` | Integer | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns `0` for TCP connections. |
| `cf.edge.l4.delivery_rate` | Integer | The most recent data delivery rate estimate for the client connection, in bytes per second. Returns `0` when L4 statistics are not available for the request. |

#### Example: Route slow connections to a lightweight origin

Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:

**Rule expression:**

```txt
cf.timings.client_tcp_rtt_msec > 200 or cf.timings.client_quic_rtt_msec > 200
```

**Header modifications:**

| Operation | Header name | Value |
| --- | --- | --- |
| Set | `X-High-Latency` | `true` |

#### Example: Match low-bandwidth connections

```txt
cf.edge.l4.delivery_rate > 0 and cf.edge.l4.delivery_rate < 100000
```

For more information, refer to [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/) and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

Apr 1, 2026

[<h2>Deploy Hooks are now available for Workers Builds</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.

Each Deploy Hook is a unique URL tied to a specific branch. Send it a `POST` and your Worker builds and deploys.

```sh
curl -X POST "https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/<DEPLOY_HOOK_ID>"
```

To create one, go to **Workers & Pages** > your Worker > **Settings** > **Builds** > **Deploy Hooks**.

Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) can rebuild your project on a schedule:

```js
export default {
	async scheduled(event, env, ctx) {
		ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
	},
};
```

```ts
export default {
  async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
    ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
  },
} satisfies ExportedHandler<Env>;
```

You can also use Deploy Hooks to [rebuild when your CMS publishes new content](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#cms-integration) or [deploy from a Slack slash command](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command).

#### Built-in optimizations

- **Automatic deduplication**: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.
- **Last triggered**: The dashboard shows when each hook was last triggered.
- **Build source**: Your Worker's build history shows which Deploy Hook started each build by name.

Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see [Limits & pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).

To get started, read the [Deploy Hooks documentation](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/).

Apr 1, 2026

[<h2>New L4 transport telemetry fields in Workers</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/)

[Workers](https://developers.cloudflare.com/workers/)

Three new properties are now available on `request.cf` in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.

Previously, this telemetry was only available via the `Server-Timing: cfL4` response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.

#### New properties

| Property | Type | Description |
| --- | --- | --- |
| `clientTcpRtt` | number \| undefined | The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, `22`. |
| `clientQuicRtt` | number \| undefined | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, `42`. |
| `edgeL4` | Object \| undefined | Layer 4 transport statistics. Contains `deliveryRate` (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, `123456`. |

#### Example: Log connection quality metrics

```js
export default {
  async fetch(request) {
    const cf = request.cf;

    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;
    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;
    const transport = cf.clientTcpRtt ? "TCP" : "QUIC";

    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);

    const headers = new Headers(request.headers);
    headers.set("X-Client-RTT", String(rtt));
    headers.set("X-Delivery-Rate", String(deliveryRate));

    return fetch(new Request(request, { headers }));
  },
};
```

For more information, refer to [Workers Runtime APIs: Request](https://developers.cloudflare.com/workers/runtime-apis/request/).

Mar 31, 2026

[<h2>Internal DNS - now in open beta</h2>](https://developers.cloudflare.com/changelog/post/2026-03-31-internal-dns-open-beta/)

[DNS](https://developers.cloudflare.com/dns/)

Internal DNS is now in open beta.

#### Who can use it?

Internal DNS is bundled as a part of Cloudflare Gateway and is now available to every Enterprise customer with one of the following subscriptions:

- Cloudflare Zero Trust Enterprise
- Cloudflare Gateway Enterprise

To learn more and get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

Mar 30, 2026

[<h2>WAF Release - 2026-03-30</h2>](https://developers.cloudflare.com/changelog/post/2026-03-30-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's release introduces new detections for a critical authentication bypass vulnerability in Fortinet products (CVE-2025-59718), alongside three new generic detection rules designed to identify and block HTTP Parameter Pollution attempts. Additionally, this release includes targeted protection for a high-impact unrestricted file upload vulnerability in Magento and Adobe Commerce.

**Key Findings**

- CVE-2025-59718: An improper cryptographic signature verification vulnerability in Fortinet FortiOS, FortiProxy, and FortiSwitchManager. This may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication using a maliciously crafted SAML message, if that feature is enabled on the device.
- Magento 2 - Unrestricted File Upload: A critical flaw in Magento and Adobe Commerce allows unauthenticated attackers to bypass security checks and upload malicious files to the server, potentially leading to Remote Code Execution (RCE).

**Impact**

Successful exploitation of the Fortinet and Magento vulnerabilities could allow unauthenticated attackers to gain administrative control or deploy webshells, leading to complete server compromise and data theft.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2f7f95e9 | N/A | Generic Rules - Parameter Pollution - Body | Log | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...319731a4

N/A | Generic Rules - Parameter Pollution - Header - Form | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...def262dd

N/A | Generic Rules - Parameter Pollution - URI | Log | Disabled  
 | This is a new detection.

 |
| Cloudflare Managed Ruleset | ...70a36147 | N/A | Magento 2 - Unrestricted file upload | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...2ffcca9f | N/A | Fortinet FortiCloud SSO - Authentication Bypass - CVE:CVE-2025-59718 | Log | Block | This is a new detection. |

Mar 27, 2026

[<h2>New RFC 9440 mTLS certificate fields in Workers</h2>](https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/)

[Workers](https://developers.cloudflare.com/workers/)

Four new fields are now available on `request.cf.tlsClientAuth` in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format — the same standard format used by the `Client-Cert` and `Client-Cert-Chain` HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `certRFC9440` | String | The client leaf certificate in RFC 9440 format (`:base64-DER:`). Empty if no client certificate was presented. |
| `certRFC9440TooLarge` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted from `certRFC9440`. |
| `certChainRFC9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB. |
| `certChainRFC9440TooLarge` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted from `certChainRFC9440`. |

#### Example: forwarding client certificate headers to your origin

```js
export default {
  async fetch(request) {
    const tls = request.cf.tlsClientAuth;

    // Only forward if cert was verified and chain is complete
    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {
      return new Response("Unauthorized", { status: 401 });
    }

    const headers = new Headers(request.headers);
    headers.set("Client-Cert", tls.certRFC9440);
    headers.set("Client-Cert-Chain", tls.certChainRFC9440);

    return fetch(new Request(request, { headers }));
  },
};
```

For more information, refer to [Client certificate variables](https://developers.cloudflare.com/ssl/client-certificates/client-certificate-variables/#workers-variables) and [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/).

Mar 26, 2026

[<h2>Code Mode for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support [Code Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/), a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.

To turn it off, edit the portal in **Access controls** > **AI controls** and turn off **Code Mode** under **Basic information**.

When Code Mode is active, the portal exposes a single `code` tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed `codemode.*` methods for each upstream tool. The generated code runs in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment, keeping authentication credentials and environment variables out of the model context.

To use Code Mode, append `?codemode=search_and_execute` to your portal URL when connecting from an MCP client:

```txt
https://<subdomain>.<domain>/mcp?codemode=search_and_execute
```

For more information, refer to [Code Mode](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode).

Mar 26, 2026

[<h2>Context optimization for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the `optimize_context` query parameter to the portal URL.

#### `minimize_tools`

Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special `query` tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=minimize_tools
```

#### `search_and_execute`

Hides all upstream tools and exposes only two tools: `query` and `execute`. The `query` tool searches and retrieves tool definitions. The `execute` tool runs the upstream tools in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=search_and_execute
```

For more information, refer to [Optimize context](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context).

Mar 26, 2026

[<h2>Easily connect Containers and Sandboxes to Workers</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) now support connecting directly to Workers over HTTP. This allows you to call Workers functions and [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/), like [KV](https://developers.cloudflare.com/kv) or [R2](https://developers.cloudflare.com/r2/), from within the container at specific hostnames.

#### Run Worker code

Define an `outbound` handler to capture any HTTP request or use `outboundByHost` to capture requests to individual hostnames and IPs.

```js
export class MyApp extends Sandbox {}

MyApp.outbound = async (request, env, ctx) => {
	// you can run arbitrary functions defined in your Worker on any HTTP request
	return await someWorkersFunction(request.body);
};

MyApp.outboundByHost = {
	"my.worker": async (request, env, ctx) => {
		return await anotherFunction(request.body);
	},
};
```

In this example, requests from the container to `http://my.worker` will run the function defined within `outboundByHost`, and any other HTTP requests will run the `outbound` handler. These handlers run entirely inside the Workers runtime, outside of the container sandbox.

#### Access Workers bindings

Each handler has access to `env`, so it can call any binding set in [Wrangler config](https://developers.cloudflare.com/workers/wrangler/configuration/#bindings). Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.

```js
export class MyApp extends Sandbox {}

MyApp.outboundByHost = {
	"my.kv": async (request, env, ctx) => {
		const key = new URL(request.url).pathname.slice(1);
		const value = await env.KV.get(key);
		return new Response(value ?? "", { status: value ? 200 : 404 });
	},
	"my.r2": async (request, env, ctx) => {
		const key = new URL(request.url).pathname.slice(1);
		const object = await env.BUCKET.get(key);
		return new Response(object?.body ?? "", { status: object ? 200 : 404 });
	},
};
```

Now, from inside the container sandbox, `curl http://my.kv/some-key` will access [Workers KV](https://developers.cloudflare.com/kv) and `curl http://my.r2/some-object` will access [R2](https://developers.cloudflare.com/r2/).

#### Access Durable Object state

Use `ctx.containerId` to reference the container's automatically provisioned [Durable Object](https://developers.cloudflare.com/durable-objects).

```js
export class MyContainer extends Container {}

MyContainer.outboundByHost = {
	"get-state.do": async (request, env, ctx) => {
		const id = env.MY_CONTAINER.idFromString(ctx.containerId);
		const stub = env.MY_CONTAINER.get(id);
		return stub.getStateForKey(request.body);
	},
};
```

This provides an easy way to associate state with any container instance, and includes a [built-in SQLite database](https://developers.cloudflare.com/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api).

#### Get Started Today

Upgrade to `@cloudflare/containers` version 0.2.0 or later, or `@cloudflare/sandbox` version 0.8.0 or later to use outbound Workers.

Refer to [Containers outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) and [Sandboxes outbound traffic](https://developers.cloudflare.com/sandbox/guides/outbound-traffic/) for more details and examples.

Mar 26, 2026

[<h2>Streaming ZIP file scanning removes per-file size limits</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.

Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.

This improvement is automatic — no configuration changes are required.

Mar 26, 2026

[<h2>Access Durable Object jurisdiction via \`ctx.id.jurisdiction\`</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

`ctx.id.jurisdiction` inside a Durable Object now reports the [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction) the object was created in — for example `"eu"` when accessed through `env.MY_DURABLE_OBJECT.jurisdiction("eu")` — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve `jurisdiction`, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#jurisdiction).

```js
export class RegionalRoom extends DurableObject {
	async fetch(request) {
		// "eu" when accessed through env.MY_DURABLE_OBJECT.jurisdiction("eu")
		const region = this.ctx.id.jurisdiction;
		return new Response(`Hello from ${region ?? "the default region"}!`);
	}
}

// Worker
export default {
	async fetch(request, env) {
		const stub = env.MY_DURABLE_OBJECT.jurisdiction("eu").getByName("general");
		return stub.fetch(request);
	},
};
```

`ctx.id.jurisdiction` is `undefined` for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have `jurisdiction` stored; to backfill the value, reschedule the alarm from a `fetch()` or RPC handler.

Mar 26, 2026

[<h2>URL Scanner improvements on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) ships several improvements to the [URL Scanner ↗︎](https://radar.cloudflare.com/scan) that make scan reports more informative and easier to share:

- **Live screenshots** — the summary card now includes an option to capture a live screenshot of the scanned URL on demand using the [Browser Rendering](https://developers.cloudflare.com/browser-run/) API.
- **Save as PDF** — a new button generates a print-optimized document aggregating all tab contents (Summary, Security, Network, Behavior, and Indicators) into a single file.
- **Download as JSON** — raw scan data is available as a JSON download for programmatic use.
- **Redesigned summary layout** — page information and security details are now displayed side by side with the screenshot, with a layout that adapts to narrower viewports.
- **File downloads** — downloads are separated into a dedicated card with expandable rows showing each file's source URL and SHA256 hash.
- **Detailed IP address data** — the Network tab now includes additional detail per IP address observed during the scan.

![Screenshot of the redesigned URL Scanner summary on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2424,height=2658,format=webp/_astro/url-scanner-summary-redesign.DO4wDjQ3.png)

Explore these improvements on the [Cloudflare Radar URL Scanner ↗︎](https://radar.cloudflare.com/scan).

Mar 25, 2026

[<h2>Detect and sanitize HAR files</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.

Gateway now includes a predefined DLP profile called **Unsanitized HAR** that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.

#### How to configure a HAR file policy

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall Policies** > **HTTP** and create a new HTTP policy using the **DLP Profile** selector:

| Selector | Operator | Value | Action |
| --- | --- | --- | --- |
| DLP Profile | in | *Unsanitized HAR* | |

Then choose one of the following actions:

- **Block**: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.
- **Block** with **Gateway Redirect**: Intercepts the upload and redirects the user to `https://har-sanitizer.pages.dev/`, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.

#### Sanitized HAR recognition

HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.

#### Visibility in Gateway logs

Gateway logs will reflect whether a detected HAR file was classified as **Unsanitized** or **Sanitized**, giving your security team full visibility into HAR file activity across your organization.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

Mar 25, 2026

[<h2>Logpush — More granular timestamps</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

- `rfc3339ms` — `2024-02-17T23:52:01.123Z`
- `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`

Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.

Mar 25, 2026

[<h2>New mTLS certificate fields for Transform Rules</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized `Client-Cert` and `Client-Cert-Chain` header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.

Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, `:MIIDsT...Vw==:`. A chain of intermediates is expressed as a comma-separated list of such values.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.tls_client_auth.cert_rfc9440` | String | The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented. |
| `cf.tls_client_auth.cert_rfc9440_too_large` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be `false`. |
| `cf.tls_client_auth.cert_chain_rfc9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB. |
| `cf.tls_client_auth.cert_chain_rfc9440_too_large` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted. |

The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.

#### Example: Forwarding client certificate headers to your origin server

Add a request header transform rule to set the `Client-Cert` and `Client-Cert-Chain` headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:

**Rule expression:**

```txt
cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked
```

**Header modifications:**

| Operation | Header name | Value |
| --- | --- | --- |
| Set | `Client-Cert` | `cf.tls_client_auth.cert_rfc9440` |
| Set | `Client-Cert-Chain` | `cf.tls_client_auth.cert_chain_rfc9440` |

To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates `cf.tls_client_auth.cert_verified` and `cf.tls_client_auth.cert_revoked`.

Prevent header injection

You should ensure that `Client-Cert` and `Client-Cert-Chain` headers received by your origin server can only originate from this transform rule — any client could send these headers directly.

- **If you use WAF custom rules to block requests with invalid mTLS connections:** The transform rule is sufficient. For all requests that reach your origin server, the rule will overwrite any existing `Client-Cert` and `Client-Cert-Chain` headers.
- **If you do not enforce mTLS at the WAF:** Add another transform rule that removes any incoming `Client-Cert` and `Client-Cert-Chain` headers from all requests (use expression `true`), ordered before the rule above. This ensures your origin server cannot receive client-supplied values for these HTTP headers.

For more information, refer to [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/), [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/), and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

Mar 25, 2026

[<h2>Declare required secrets in your Wrangler configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/)

[Workers](https://developers.cloudflare.com/workers/)

The new `secrets` configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.

```jsonc
{
	"secrets": {
		"required": ["API_KEY", "DB_PASSWORD"],
	},
}
```

```toml
[secrets]
required = [ "API_KEY", "DB_PASSWORD" ]
```

#### Local development

When `secrets` is defined, `wrangler dev` and `vite dev` load only the keys listed in `secrets.required` from `.dev.vars` or `.env`/`process.env`. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.

#### Type generation

`wrangler types` generates typed bindings from `secrets.required` instead of inferring names from `.dev.vars` or `.env`. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated `Env` type marks secrets that only appear in some environments as optional.

#### Deploy

`wrangler deploy` and `wrangler versions upload` validate that all secrets in `secrets.required` are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.

For more information, refer to the [`secrets` configuration property](https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property) reference.

Mar 24, 2026

[<h2>Advanced WAF customization for AI Crawl Control blocks</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.

If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the **Crawlers** page with a link to view the rule directly in WAF.

For more information, refer to [WAF rule management](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management).

Mar 24, 2026

[<h2>Cache Response Rules</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now control how Cloudflare handles origin responses without changing your origin. Cache Response Rules let you modify `Cache-Control` directives, manage cache tags, and strip headers like `Set-Cookie` from origin responses *before* they reach Cloudflare's cache. Whether traffic is cached or passed through dynamically, these rules give you control over origin response behavior that was previously out of reach.

#### What changed

Cache Rules previously only operated on request attributes. Cache Response Rules introduce a new response phase that evaluates origin responses and lets you act on them before caching. You can now:

- **Modify `Cache-Control` directives**: Set or remove individual directives like `no-store`, `no-cache`, `max-age`, `s-maxage`, `stale-while-revalidate`, `immutable`, and more. For example, remove a `no-cache` directive your origin sends so Cloudflare can cache the asset, or set an `s-maxage` to control how long Cloudflare stores it.
- **Set a different browser `Cache-Control`**: Send a different `Cache-Control` header downstream to browsers and other clients than what Cloudflare uses internally, giving you independent control over edge and browser caching strategies.
- **Manage cache tags**: Add, set, or remove cache tags on responses, including converting tags from another CDN's header format into Cloudflare's `Cache-Tag` header. This is especially useful if you are migrating from a CDN that uses a different tag header or delimiter.
- **Strip headers that block caching**: Remove `Set-Cookie`, `ETag`, or `Last-Modified` headers from origin responses before caching, so responses that would otherwise be treated as uncacheable can be stored and served from cache.

#### Benefits

- **No origin changes required**: Fix caching behavior entirely from Cloudflare, even when your origin configuration is locked down or managed by a different team.
- **Simpler CDN migration**: Match caching behavior from other CDN providers without rewriting your origin. Translate cache tag formats and override directives that do not align with Cloudflare's defaults.
- **Native support, fewer workarounds**: Functionality that previously required workarounds is now built into Cache Rules with full Tiered Cache compatibility.
- **Fine-grained control**: Use expressions to match on request and response attributes, then apply precise cache settings per rule. Rules are stackable and composable with existing Cache Rules.

#### Get started

Configure Cache Response Rules in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) under **Caching** > **Cache Rules**, or via the [Rulesets API ↗︎](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). For more details, refer to the [Cache Rules documentation ↗︎](https://developers.cloudflare.com/cache/how-to/cache-response-rules/).

Mar 24, 2026

[<h2>Use Docker Hub images with Containers</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/)

[Containers](https://developers.cloudflare.com/containers/)

Containers now support [Docker Hub ↗︎](https://hub.docker.com/) images. You can use a fully qualified Docker Hub image reference in your [Wrangler configuration ↗︎](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.

```jsonc
{
	"containers": [
		{
			// Example: docker.io/cloudflare/sandbox:0.7.18
			"image": "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>",
		},
	],
}
```

```toml
[[containers]]
image = "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>"
```

Containers also support private Docker Hub images. To configure credentials, refer to [Use private Docker Hub images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-docker-hub-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).

Mar 24, 2026

[<h2>OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports [OIDC Claims](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims) as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.

With this update, you can:

- Filter traffic in [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies based on OIDC claim values.
- Apply custom [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) to route DNS queries to specific resolvers depending on a user's OIDC claims.
- Control [egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/) to assign dedicated egress IPs based on OIDC claim attributes.

For example, you can create a policy that routes traffic differently for users with `department=engineering` in their OIDC claims, or restrict access to certain destinations based on a user's role claim.

To get started, configure [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) on your identity provider and use the **OIDC Claims** selector in the Gateway policy builder.

For more information, refer to [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/24/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/24/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
