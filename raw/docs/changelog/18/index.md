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

May 19, 2026

[<h2>Event subscriptions for Artifacts lifecycle events</h2>](https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/)

[Artifacts](https://developers.cloudflare.com/artifacts/) [Queues](https://developers.cloudflare.com/queues/)

You can now receive [event notifications](https://developers.cloudflare.com/queues/event-subscriptions/) for [Artifacts](https://developers.cloudflare.com/artifacts/) repository changes and consume them from a Worker to build commit-driven automation.

This allows you to:

- Run custom workflows when a repository is created or imported
- Kick off a build and deploy a change when an agent pushes to a repo
- Trigger a review agent on every push

Available events include:

- **Account-level events** ( `artifacts` source) — `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`
- **Repository-level events** ( `artifacts.repo` source) — `pushed`, `cloned`, `fetched`

To learn more, refer to [Artifacts documentation](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

May 19, 2026

[<h2>CASB adds support for Claude Compliance API</h2>](https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/) now integrates with the [Claude Compliance API ↗︎](https://support.claude.com/en/articles/13015708-access-the-compliance-api). This enhancement gives security teams visibility into Claude usage patterns, admin activity, and compliance-relevant events across their organization.

The Claude Compliance API provides structured access to audit logs and administrative actions within Claude Enterprise and Claude Platform. Cloudflare CASB ingests this data to surface security findings that help organizations enhance their security posture and enforce AI governance.

#### Key capabilities

Starting today, security teams can scan for security findings across the following assets:

- **Public projects** — Projects set to public visibility
- **Project attachment** — Files and documents added to projects that violate DLP policies
- **Chat files** — User-uploaded and provider-generated files that violate DLP policies
- **Chat messages** — User prompts and provider responses that violate DLP policies
- **Artifacts** — Provider-generated documents and files that violate DLP policies

#### Learn more

This [integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/) is available to all Cloudflare One customers. New Cloudflare customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the dashboard. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.

May 19, 2026

[<h2>MRT Explorer on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes an [MRT Explorer ↗︎](https://radar.cloudflare.com/routing/mrt-explorer) tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.

#### Loading a file

Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.

![Screenshot of the MRT Explorer file input form](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2428,height=898,format=webp/_astro/mrt-explorer-form.DKnzUqMC.png)

#### Inspecting events

Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.

![Screenshot of the MRT Explorer event list](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1536,format=webp/_astro/mrt-explorer-list.8fq2u5Kc.png)

#### Event details

Clicking on the "View details" action opens a modal with additional properties and the full event JSON.

![Screenshot of the MRT Explorer event details modal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=1890,format=webp/_astro/mrt-explorer-details.EMcHevWw.png)

#### Shareable URLs

When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.

Try the [MRT Explorer on Cloudflare Radar ↗︎](https://radar.cloudflare.com/routing/mrt-explorer).

May 18, 2026

[<h2>Manage Artifacts namespaces and repos with Wrangler CLI</h2>](https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

You can now manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.

Available commands:

- `wrangler artifacts namespaces list` — List Artifacts namespaces in your account.
- `wrangler artifacts namespaces get` — Get metadata for a namespace.
- `wrangler artifacts repos create` — Create a repo in a namespace.
- `wrangler artifacts repos list` — List repos in a namespace.
- `wrangler artifacts repos get` — Get metadata for a repo.
- `wrangler artifacts repos delete` — Delete a repo.
- `wrangler artifacts repos issue-token` — Issue a repo-scoped token for Git access.

To get started, refer to the [Wrangler Artifacts commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/).

May 18, 2026

[<h2>Network Analytics support for Unified Routing</h2>](https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/)

[Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) is now fully supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.

This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.

For the remaining beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

May 18, 2026

[<h2>Share local dev servers through Cloudflare Tunnel in Wrangler and Vite</h2>](https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/)

[Workers](https://developers.cloudflare.com/workers/)

You can now share local dev sessions through [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and get a public URL when using either [Wrangler](https://developers.cloudflare.com/workers/wrangler/) or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). This is useful when you need to share a preview, test a webhook, or access your app from another device.

![Vite local dev tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=678,format=webp/_astro/vite-local-dev-tunnel.CW4xpgIR.gif)

This lets you either:

- start a temporary [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) with a random `*.trycloudflare.com` hostname, or
- use an existing [named tunnel](https://developers.cloudflare.com/tunnel/get-started/#create-a-tunnel) for a stable hostname and to restrict access with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/).

To start a tunnel, press `t` in Wrangler or `t + Enter` in Vite while your dev server is running. For details on setting up a named tunnel, refer to [Share a local dev server](https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/).

May 15, 2026

[<h2>R2 SQL now supports JOINs, subqueries, and multi-table queries</h2>](https://developers.cloudflare.com/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.

R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.

#### New capabilities

- **JOINs** — `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`, `CROSS JOIN`, and implicit joins (comma-separated `FROM` with conditions in `WHERE`)
- **Subqueries** — `IN` / `NOT IN`, `EXISTS` / `NOT EXISTS`, scalar subqueries in `SELECT` / `WHERE` / `HAVING`, and derived tables (subqueries in `FROM`)
- **Multi-table CTEs** — `WITH` clauses can reference different tables and include JOINs
- **Self-joins** — join a table with itself using different aliases
- **Multi-way joins** — join three or more tables in a single query

#### Examples

#### Two-table JOIN with aggregation

```sql
SELECT z.domain, z.plan, COUNT(*) AS request_count
FROM my_namespace.zones z
INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id
WHERE z.plan = 'enterprise'
GROUP BY z.domain, z.plan
ORDER BY request_count DESC
LIMIT 20
```

#### `EXISTS` subquery

```sql
SELECT z.domain, z.plan
FROM my_namespace.zones z
WHERE EXISTS (
    SELECT 1 FROM my_namespace.firewall_events f
    WHERE f.zone_id = z.zone_id AND f.action = 'block'
)
ORDER BY z.domain
LIMIT 20
```

#### Multi-table CTE with JOIN

```sql
WITH top_zones AS (
    SELECT zone_id, COUNT(*) AS req_count
    FROM my_namespace.http_requests
    GROUP BY zone_id
    ORDER BY req_count DESC
    LIMIT 50
),
zone_threats AS (
    SELECT zone_id, COUNT(*) AS threat_count
    FROM my_namespace.firewall_events
    WHERE risk_score > 0.5
    GROUP BY zone_id
)
SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count
FROM top_zones tz
LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id
ORDER BY tz.req_count DESC
LIMIT 20
```

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance with joins, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

May 15, 2026

[<h2>Hyperdrive exposes database connection pool size metrics</h2>](https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/) [Workers](https://developers.cloudflare.com/workers/)

You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/), you can see `waitingClients`, `currentPoolSize`, `availablePoolSlots`, and `maxPoolSize` for each of your configurations.

A new **Pool connections** chart has been added to the **Metrics** tab of each Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com). You can use the location selector to drill down into specific locations hosting your connection pool by airport code.

![Hyperdrive pool size metrics chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2604,height=890,format=webp/_astro/hyperdrive-pool-size-metrics-chart.DZxLTFgB.png)

The chart shows:

- **Waiting clients**: Client requests waiting for an available connection.
- **Open connections**: Active connections to your database.
- **Pool size maximum**: Your configured origin connection limit.

Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to [increase your Hyperdrive connection limit](https://developers.cloudflare.com/hyperdrive/platform/limits/#request-a-limit-increase).

#### Pool size metrics

The `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/) exposes the following key connection pool metrics for each Hyperdrive configuration:

Under `avg`:

- **`currentPoolSize`** — Average number of connections currently open in the pool.
- **`availablePoolSlots`** — Average number of pool connections available for checkout.
- **`waitingClients`** — Average number of clients waiting for a connection from the pool.

Under `max`:

- **`maxPoolSize`** — Configured maximum size of the connection pool.
- **`currentPoolSize`** — Peak number of connections open in the pool.
- **`waitingClients`** — Peak number of clients waiting for a connection from the pool.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/hyperdrive/observability/metrics/) and [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

May 15, 2026

[<h2>WAF Release - 2026-05-15 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's `is_args` stale-state bug (CVE-2026-42945).

**Key Findings**

CVE-2026-42945: nginx Heap Buffer Overflow via Stale `is_args` in Rewrite Module

Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in `ngx_http_script_copy_capture_code()` causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.

We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid `rewrite` directives with `?` in the replacement string followed by `set` or `if` referencing capture groups.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...7e52be73 | N/A | nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945 | N/A | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...9df0ee6c | N/A | nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945 | N/A | Block | This is a new detection. |

May 14, 2026

[<h2>New Domains tab in the Workers dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-05-14-domains-tab/)

[Workers](https://developers.cloudflare.com/workers/)

In your Worker's dashboard, there is now a dedicated **Domains** tab where you can purchase a new domain through Cloudflare Registrar and have it automatically connected, add an [existing domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), and manage all of your Worker's routing in one place.

![The new Domains tab in the Workers dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1678,height=1026,format=webp/_astro/domains-tab.Cey2Oyr-.png)

You can also enable or disable your [`workers.dev` subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) and [Preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/), put them behind [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) to require sign-in, and jump directly to [analytics](https://developers.cloudflare.com/analytics/) or domain overview for any connected domain.

To get started, go to **Workers & Pages**, select a Worker, and open the **Domains** tab.

[Go to **Workers & Pages** ↗](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

May 13, 2026

[<h2>Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</h2>](https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.

#### Chat recovery improvements

`@cloudflare/ai-chat` now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling `stop()` still cancels the server turn.

Set `cancelOnClientAbort: true` if browser or client aborts should also cancel the server turn:

```js
const chat = useAgentChat({
	agent: "assistant",
	name: "user-123",
	cancelOnClientAbort: true,
});
```

```tsx
const chat = useAgentChat({
	agent: "assistant",
	name: "user-123",
	cancelOnClientAbort: true,
});
```

Notable bug fixes:

- Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.
- Recovered chat continuations no longer leave `useAgentChat` stuck in a streaming state when the original socket disconnects before a terminal response.
- Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.
- `isServerStreaming` now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.

#### Agent state and routing fixes

`agents@0.12.4` prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.

Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.

`getAgentByName()` now supports `routingRetry` for transient Durable Object routing failures:

```js
import { getAgentByName } from "agents";

const agent = await getAgentByName(env.AssistantAgent, "user-123", {
	routingRetry: {
		maxAttempts: 3,
	},
});
```

```ts
import { getAgentByName } from "agents";

const agent = await getAgentByName(env.AssistantAgent, "user-123", {
	routingRetry: {
		maxAttempts: 3,
	},
});
```

#### Durable Think submissions

`@cloudflare/think` now supports durable programmatic submissions. `submitMessages()` provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.

`Think.chat()` RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.

`ChatOptions.tools` has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime `options.tools` values passed by legacy callers are ignored with a warning.

#### Think message pruning behavior change

`@cloudflare/think` no longer applies `pruneMessages({ toolCalls: "before-last-2-messages" })` to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.

`truncateOlderMessages` still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from `beforeTurn`:

```js
import { Think } from "@cloudflare/think";
import { pruneMessages } from "ai";

export class MyAgent extends Think {
	beforeTurn(ctx) {
		return {
			messages: pruneMessages({
				messages: ctx.messages,
				toolCalls: "before-last-2-messages",
			}),
		};
	}
}
```

```ts
import { Think } from "@cloudflare/think";
import { pruneMessages } from "ai";

export class MyAgent extends Think<Env> {
	beforeTurn(ctx) {
		return {
			messages: pruneMessages({
				messages: ctx.messages,
				toolCalls: "before-last-2-messages",
			}),
		};
	}
}
```

#### Voice agent connection control

`@cloudflare/voice` adds an `enabled` option to `useVoiceAgent`. React apps can now delay creating and connecting a `VoiceClient` until prerequisites such as capability tokens are ready.

```js
const voice = useVoiceAgent({
	agent: "MyVoiceAgent",
	enabled: Boolean(token),
});
```

```tsx
const voice = useVoiceAgent({
	agent: "MyVoiceAgent",
	enabled: Boolean(token),
});
```

This release also fixes Workers AI speech-to-text session edge cases and `withVoice` text streaming from AI SDK `textStream` responses.

#### Other improvements

- **Streamable HTTP routing** — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.
- **Structured tool output** — Tool output shapes are preserved when truncating older messages or oversized persisted rows.
- **Non-chat Think tool steps** — Think agent-tool children can complete without emitting assistant text and can return structured output through `getAgentToolOutput`.
- **Sub-agent schedules** — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.
- **`@cloudflare/codemode`** — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest
```

Refer to the [Agents API reference](https://developers.cloudflare.com/agents/runtime/) and [Chat agents documentation](https://developers.cloudflare.com/agents/communication-channels/chat/chat-agents/) for more information.

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

May 13, 2026

[<h2>/cdn-cgi/rum endpoint now returns 405 for non-POST requests</h2>](https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

The `/cdn-cgi/rum` beacon endpoint now returns `405 Method Not Allowed` for non-POST requests instead of `404 Not Found`. The response includes an `Allow: POST, OPTIONS` header per [RFC 9110 §15.5.6 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6).

Previously, sending a `GET` or other non-POST request to this endpoint returned a `404`, which was misleading because it suggested the endpoint did not exist. The new `405` response clearly indicates that the endpoint exists but only accepts `POST` requests.

The Web Analytics beacon (`beacon.min.js`) already uses `POST` for all metric submissions, so this change does not affect normal beacon operation. `OPTIONS` requests for CORS preflight continue to work as before.

For more information, refer to the [Web Analytics FAQ](https://developers.cloudflare.com/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum).

May 12, 2026

[<h2>R2 Data Catalog now exposes metrics via the GraphQL Analytics API</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), Spark, Snowflake, and DuckDB to your data in R2.

You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). Two new datasets are available:

- **`r2CatalogDataOperationsAdaptiveGroups`** tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.
- **`r2CatalogTableMaintenanceAdaptiveGroups`** tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.

Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.

For detailed schema information and example queries, refer to the [R2 Data Catalog metrics and analytics documentation](https://developers.cloudflare.com/basin-catalog/observability/metrics/).

May 12, 2026

[<h2>Refreshed Access login page</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

The [Access login page](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-login-page/) and [one-time password (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.

**Before:**

![Screenshot of the previous Access login page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=532,height=906,format=webp/_astro/access-login-old.CwNVkCQH.png)

**After:**

![Screenshot of the updated Access login page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=541,height=722,format=webp/_astro/access-login-new.Y7WUfg9G.png)

The updated login experience includes:

- **Unified authentication card** - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.
- **Consistent button styling** - Identity provider buttons use a uniform size and layout for easier scanning and selection.
- **Better mobile experience** - Responsive layout improvements ensure the login page renders correctly on phones and tablets.
- **Dark mode support** - The login page now supports dark mode.

May 12, 2026

[<h2>New accounts assigned a single IPv4 anycast address</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.

Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.

To request additional anycast IP addresses for your account, contact your account team.

For tunnel configuration guidance, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/) for Cloudflare WAN or [Configure tunnel endpoints](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/) for Magic Transit.

May 12, 2026

[<h2>SSH through Wrangler is now enabled by default for Containers</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/)

[Containers](https://developers.cloudflare.com/containers/)

SSH through Wrangler is now enabled by default for [Containers](https://developers.cloudflare.com/containers/). Previously, you had to set `ssh.enabled` to `true` in your Container configuration before you could connect.

This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through [`wrangler containers ssh`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-ssh), which authenticates against your Cloudflare account. You also need to add an `ssh-ed25519` public key to `authorized_keys` before anyone can connect, so enabling SSH alone does not grant access.

To connect, add a public key to your Container configuration and run `wrangler containers ssh <INSTANCE_ID>`:

```jsonc
{
	"containers": [
		{
			"authorized_keys": [
				{
					"name": "<NAME>",
					"public_key": "<YOUR_PUBLIC_KEY_HERE>",
				},
			],
		},
	],
}
```

```toml
[[containers]]
[[containers.authorized_keys]]
name = "<NAME>"
public_key = "<YOUR_PUBLIC_KEY_HERE>"
```

To disable SSH, set `ssh.enabled` to `false` in your Container configuration:

```jsonc
{
	"containers": [
		{
			"ssh": {
				"enabled": false,
			},
		},
	],
}
```

```toml
[[containers]]
[containers.ssh]
enabled = false
```

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

May 12, 2026

[<h2>Create Gateway firewall policies with natural language</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports natural language policy creation for [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.

![Create with AI button on the Gateway firewall policies page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2360,height=1088,format=webp/_astro/gateway-create-with-ai.BYG07coh.png)

To create a policy with natural language, select **Create with AI** on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.

The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.

A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.

For more information, refer to [Gateway firewall policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

May 12, 2026

[<h2>Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/)

[Security Center](https://developers.cloudflare.com/security-center/)

We’ve added a new **Agent Readiness** tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.

The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't "agent-ready," these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.

This update provides material value by breaking down readiness into six actionable categories:

- **Basic Web Presence**
- **Discoverability**
- **Content Accessibility**
- **Bot Access Control**
- **Protocol Discovery**
- **Commerce**

#### Accessing the report

You can view these scores for any scanned URL directly in the dashboard or via our API.

- **Dashboard:** Go to **Protect & Connect > Application Security > Investigate**. After running a scan, select the **Agent Readiness** tab in the report.
- **API:** Use the [URL Scanner API ↗︎](https://developers.cloudflare.com/radar/investigate/url-scanner/) to programmatically retrieve these scores for your infrastructure.

To learn more about the methodology behind these scores, refer to the [blogpost ↗︎](https://blog.cloudflare.com/agent-readiness/).

May 11, 2026

[<h2>Cloudflare One Client for Windows (version 2026.4.1350.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-05-11-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

- Right click context menu to access the most common client actions quickly
- Built-in captive portal login experience

**Additional Changes and improvements**

- Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.

**Known issues**

- Registration authentication for devices via the integrated WebView2 browser is unavailable in this version as a temporary measure. As a result, the client will utilize the default browser on the device to complete the authentication process.
- An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.
- Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.
- DNS resolution may be broken when the following conditions are all true:
  - The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while the client is connected.  
     To work around this issue, please reconnect the client by selecting "disconnect" and then "connect" in the client user interface.

May 11, 2026

[<h2>Cloudflare One Client for macOS (version 2026.4.1350.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-05-11-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

- Right click context menu to access the most common client actions quickly
- Built-in captive portal login experience

**Additional Changes and improvements**

- Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.

May 11, 2026

[<h2>Cloudflare One Client for Linux (version 2026.4.1350.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-05-11-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

- Right click context menu to access the most common client actions quickly
- Built-in captive portal login experience

**Changes and improvements**

- Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.
- Official support for RHEL 9 has been added for Cloudflare Mesh nodes. To install the RHEL 9 package, the Extra Packages for Enterprise Linux (EPEL) repository must be active, as it contains dependencies required for the tray icon and captive portal webview.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.

May 11, 2026

[<h2>NAT-T support for IKE on UDP port 500</h2>](https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/)

Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port `500` and switches to UDP port `4500` after NAT is detected.

Previously, devices behind NAT had to be configured to initiate IKE on UDP port `4500` directly. Devices that started on UDP port `500` could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.

What changed:

- Devices behind NAT can now initiate IKE on either UDP port `500` or UDP port `4500`.
- Devices that start IKE on UDP port `500` and switch to UDP port `4500` after NAT detection now complete the handshake successfully.
- No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.

This change does not affect existing tunnels:

- Tunnels using UDP port `500` with no NAT detected continue to operate as before.
- Tunnels configured to start IKE on UDP port `4500` continue to operate as before.
- NAT detection logic is unchanged.

For configuration details, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/).

May 11, 2026

[<h2>WAF Release - 2026-05-11</h2>](https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**Key Findings**

- Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...68b3c389 | N/A | Remote Code Execution - Java Deserialization - Body - Beta | Block | Disabled | This is a new detection. This rule is merged into the original rule "Remote Code Execution - Java Deserialization" (ID: ...744305c4). |

May 8, 2026

[<h2>Planned model deprecations on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.

#### Recommended replacements

- [`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) — fast multilingual model with multi-turn tool calling and coding capabilities.
- [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) — efficient open model with vision and tool calling.
- [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) — capable tool-calling and vision model for agentic workloads and coding.

For pricing, refer to the [Workers AI pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Kimi K2.5

We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.

#### Models deprecated on May 30, 2026

- `@cf/moonshotai/kimi-k2.5` --> `@cf/moonshotai/kimi-k2.6`
- `@hf/meta-llama/meta-llama-3-8b-instruct`
- `@cf/meta/llama-3-8b-instruct`
- `@cf/meta/llama-3-8b-instruct-awq`
- `@cf/meta/llama-3.1-8b-instruct`
- `@cf/meta/llama-3.1-8b-instruct-awq`
- `@cf/meta/llama-3.1-70b-instruct`
- `@cf/meta/llama-2-7b-chat-int8`
- `@cf/meta/llama-2-7b-chat-fp16`
- `@cf/mistral/mistral-7b-instruct-v0.1`
- `@hf/mistral/mistral-7b-instruct-v0.2`
- `@hf/google/gemma-7b-it`
- `@cf/google/gemma-3-12b-it`
- `@hf/nousresearch/hermes-2-pro-mistral-7b`
- `@cf/microsoft/phi-2`
- `@cf/defog/sqlcoder-7b-2`
- `@cf/unum/uform-gen2-qwen-500m`
- `@cf/facebook/bart-large-cnn`

#### Variants that remain active

The `-fast` and `-lora` variants of models will remain active, including:

- `@cf/meta/llama-3.3-70b-instruct-fp8-fast`
- `@cf/meta/llama-3.1-8b-instruct-fast`
- `@cf/google/gemma-7b-it-lora`
- `@cf/google/gemma-2b-it-lora`
- `@cf/mistral/mistral-7b-instruct-v0.2-lora`
- `@cf/meta-llama/llama-2-7b-chat-hf-lora`

LoRA models may be deprecated in the future. We will be adding more LoRA capabilities to the catalog, and will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.

For the full list of available models, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/18/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/18/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
