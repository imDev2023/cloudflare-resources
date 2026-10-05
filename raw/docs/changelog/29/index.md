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

Feb 12, 2026

[<h2>Introducing Markdown for Agents</h2>](https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare's network now supports real-time content conversion at the source, for enabled zones using [content negotiation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation) headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for `text/markdown` in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

Here is a curl example with the `Accept` negotiation header requesting this page from our developer documentation:

```bash
curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \
  -H "Accept: text/markdown"
```

The response to this request is now formatted in markdown:

```http
HTTP/2 200
date: Wed, 11 Feb 2026 11:44:48 GMT
content-type: text/markdown; charset=utf-8
content-length: 2899
vary: accept
x-markdown-tokens: 725
content-signal: ai-train=yes, search=yes, ai-input=yes

---
title: Markdown for Agents · Cloudflare Agents docs
---

## What is Markdown for Agents

Markdown has quickly become the lingua franca for agents and AI systems
as a whole. The format’s explicit structure makes it ideal for AI processing,
ultimately resulting in better results while minimizing token waste.
...
```

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) and our [blog announcement ↗︎](https://blog.cloudflare.com/markdown-for-agents/) for more details.

Feb 12, 2026

[<h2>Content Type Dimension for AI Bots in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes content type insights for AI bot and crawler traffic. The new `content_type` dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.

The content type dimension and filter are available via the following API endpoints:

- [`/ai/bots/summary/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/)
- [`/ai/bots/timeseries_groups/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/)

Content type categories:

- **HTML** - Web pages ( `text/html`)
- **Images** - All image formats ( `image/*`)
- **JSON** - JSON data and API responses ( `application/json`, `*+json`)
- **JavaScript** - Scripts ( `application/javascript`, `text/javascript`)
- **CSS** - Stylesheets ( `text/css`)
- **Plain Text** - Unformatted text ( `text/plain`)
- **Fonts** - Web fonts ( `font/*`, `application/font-*`)
- **XML** - XML documents and feeds ( `text/xml`, `application/xml`, `application/rss+xml`, `application/atom+xml`)
- **YAML** - Configuration files ( `text/yaml`, `application/yaml`)
- **Video** - Video content and streaming ( `video/*`, `application/ogg`, `*mpegurl`)
- **Audio** - Audio content ( `audio/*`)
- **Markdown** - Markdown documents ( `text/markdown`)
- **Documents** - PDFs, Office documents, ePub, CSV ( `application/pdf`, `application/msword`, `text/csv`)
- **Binary** - Executables, archives, WebAssembly ( `application/octet-stream`, `application/zip`, `application/wasm`)
- **Serialization** - Binary API formats ( `application/protobuf`, `application/grpc`, `application/msgpack`)
- **Other** - All other content types

Additionally, individual [bot information pages ↗︎](https://radar.cloudflare.com/bots/directory/gptbot) now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.

![Screenshot of the Content Type Distribution chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=874,format=webp/_astro/ai-bots-content-type.B7xP9p4S.png)

Check out the [AI Insights page ↗︎](https://radar.cloudflare.com/ai-insights#content-type) to explore the data.

Feb 12, 2026

[<h2>Enhanced Logo Matching for Brand Protection</h2>](https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/)

[Security Center](https://developers.cloudflare.com/security-center/)

We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.

#### What's new

- **Configurable match thresholds**: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.
- **Visual match scores**: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.
- **Direct logo previews**: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.

#### Key benefits

- **Expose sophisticated impersonators** who use slightly altered logos to bypass basic detection filters.
- **Faster triage** of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.

Ready to protect your visual identity? Learn more in our [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

Feb 12, 2026

[<h2>Terraform v5.17.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we have established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to help you migrate from v4 to v5 with ease.

This release brings new capabilities for AI Search, enhanced Workers Script placement controls, and numerous bug fixes based on community feedback. We also begun laying foundational work for improving the v4 to v5 migration process. Stay tuned for more details as we approach the March 2026 release timeline.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

#### Features

- **ai\_search\_instance:** add data source for querying AI Search instances
- **ai\_search\_token:** add data source for querying AI Search tokens
- **account:** add support for tenant unit management with new `unit` field
- **account:** add automatic mapping from `managed_by.parent_org_id` to `unit.id`
- **authenticated\_origin\_pulls\_certificate:** add data source for querying authenticated origin pull certificates
- **authenticated\_origin\_pulls\_hostname\_certificate:** add data source for querying hostname-specific authenticated origin pull certificates
- **authenticated\_origin\_pulls\_settings:** add data source for querying authenticated origin pull settings
- **workers\_kv:** add `value` field to data source to retrieve KV values directly
- **workers\_script:** add `script` field to data source to retrieve script content
- **workers\_script:** add support for `simple` rate limit binding
- **workers\_script:** add support for targeted placement mode with `placement.target` array for specifying placement targets (region, hostname, host)
- **workers\_script:** add `placement_mode` and `placement_status` computed fields
- **zero\_trust\_dex\_test:** add data source with filter support for finding specific tests
- **zero\_trust\_dlp\_predefined\_profile:** add `enabled_entries` field for flexible entry management

#### Bug Fixes

- **account:** map `managed_by.parent_org_id` to `unit.id` in unmarshall and add acceptance tests
- **authenticated\_origin\_pulls\_certificate:** add certificate normalization to prevent drift
- **authenticated\_origin\_pulls:** handle array response and implement full lifecycle
- **authenticated\_origin\_pulls\_hostname\_certificate:** fix resource and tests
- **cloudforce\_one\_request\_message:** use correct `request_id` field instead of `id` in API calls
- **dns\_zone\_transfers\_incoming:** use correct `zone_id` field instead of `id` in API calls
- **dns\_zone\_transfers\_outgoing:** use correct `zone_id` field instead of `id` in API calls
- **email\_routing\_settings:** use correct `zone_id` field instead of `id` in API calls
- **hyperdrive\_config:** add proper handling for write-only fields to prevent state drift
- **hyperdrive\_config:** add normalization for empty `mtls` objects to prevent unnecessary diffs
- **magic\_network\_monitoring\_rule:** use correct `account_id` field instead of `id` in API calls
- **mtls\_certificates:** fix resource and test
- **pages\_project:** revert build\_config to computed optional
- **stream\_key:** use correct `account_id` field instead of `id` in API calls
- **total\_tls:** use upsert pattern for singleton zone setting
- **waiting\_room\_rules:** use correct `waiting_room_id` field instead of `id` in API calls
- **workers\_script:** add support for placement mode/status
- **zero\_trust\_access\_application:** update v4 version on migration tests
- **zero\_trust\_device\_posture\_rule:** update tests to match API
- **zero\_trust\_dlp\_integration\_entry:** use correct `entry_id` field instead of `id` in API calls
- **zero\_trust\_dlp\_predefined\_entry:** use correct `entry_id` field instead of `id` in API calls
- **zero\_trust\_organization:** fix plan issues

#### Chores

- add state upgraders to 95+ resources to lay the foundation for replacing Grit (still under active development)
- **certificate\_pack:** add state migration handler for SDKv2 to Framework conversion
- **custom\_hostname\_fallback\_origin:** add comprehensive lifecycle test and migration support
- **dns\_record:** add state migration handler for SDKv2 to Framework conversion
- **leaked\_credential\_check:** add import functionality and tests
- **load\_balancer\_pool:** add state migration handler with detection for v4 vs v5 format
- **pages\_project:** add state migration handlers
- **tiered\_cache:** add state migration handlers
- **zero\_trust\_dlp\_predefined\_profile:** deprecate `entries` field in favor of `enabled_entries`

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

Feb 11, 2026

[<h2>Post-quantum encryption support for Cloudflare One Appliance</h2>](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance version 2026.2.0 adds [post-quantum encryption](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.

This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.

For more information, refer to [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/).

Feb 11, 2026

[<h2>Workers are no longer limited to 1000 subrequests</h2>](https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/)

[Workers](https://developers.cloudflare.com/workers/)

Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more `fetch()` calls or requests to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as open websockets on [Durable Objects](https://developers.cloudflare.com/durable-objects) or long-running [Workflows](https://developers.cloudflare.com/workflows), as these could often exceed this limit and error.

By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this limit can be increased up to 10 million by setting the new `subrequests` limit in your Wrangler configuration file.

```jsonc
{
	"limits": {
		"subrequests": 50000,
	},
}
```

```toml
[limits]
subrequests = 50_000
```

Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.

To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.

```jsonc
{
	"limits": {
		"subrequests": 10,
		"cpu_ms": 1000,
	},
}
```

```toml
[limits]
subrequests = 10
cpu_ms = 1_000
```

For more information, refer to the [Wrangler configuration documentation for limits](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

Feb 11, 2026

[<h2>Improved React Server Components support in the Cloudflare Vite plugin</h2>](https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/)

[Workers](https://developers.cloudflare.com/workers/)

The Cloudflare Vite plugin now integrates seamlessly [@vitejs/plugin-rsc ↗︎](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc), the official Vite plugin for [React Server Components ↗︎](https://react.dev/reference/rsc/server-components).

A `childEnvironments` option has been added to the plugin config to enable using multiple environments within a single Worker. The parent environment can then import modules from a child environment in order to access a separate module graph. For a typical RSC use case, the plugin might be configured as in the following example:

*vite.config.tsts*

```ts
export default defineConfig({
	plugins: [
		cloudflare({
			viteEnvironment: {
				name: "rsc",
				childEnvironments: ["ssr"],
			},
		}),
	],
});
```

`@vitejs/plugin-rsc` provides the lower level functionality that frameworks, such as [React Router ↗︎](https://reactrouter.com/how-to/react-server-components), build upon. The GitHub repository includes a [basic Cloudflare example ↗︎](https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single).

Feb 10, 2026

[<h2>WAF Release - 2026-02-10</h2>](https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...6aa0bef8 | N/A | Anomaly:Header:User-Agent - Fake Google Bot | Enabled | Disabled | We are changing the action for this rule from BLOCK to Disabled |

Feb 9, 2026

[<h2>Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.

#### Readonly connections

Agents can now restrict WebSocket clients to read-only access, preventing them from modifying agent state. This is useful for dashboards, spectator views, or any scenario where clients should observe but not mutate.

New hooks: `shouldConnectionBeReadonly`, `setConnectionReadonly`, `isConnectionReadonly`. Readonly connections block both client-side `setState()` and mutating `@callable()` methods, and the readonly flag survives hibernation.

```js
class MyAgent extends Agent {
	shouldConnectionBeReadonly(connection) {
		// Make spectators readonly
		return connection.url.includes("spectator");
	}
}
```

```ts
class MyAgent extends Agent {
	shouldConnectionBeReadonly(connection) {
		// Make spectators readonly
		return connection.url.includes("spectator");
	}
}
```

#### Custom MCP OAuth providers

The new `createMcpOAuthProvider` method on the `Agent` class allows subclasses to override the default OAuth provider used when connecting to MCP servers. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.

```js
class MyAgent extends Agent {
	createMcpOAuthProvider(callbackUrl) {
		return new MyCustomOAuthProvider(this.ctx.storage, this.name, callbackUrl);
	}
}
```

```ts
class MyAgent extends Agent {
	createMcpOAuthProvider(callbackUrl: string): AgentMcpOAuthProvider {
		return new MyCustomOAuthProvider(this.ctx.storage, this.name, callbackUrl);
	}
}
```

#### MCP SDK upgrade to 1.26.0

Upgraded the MCP SDK to 1.26.0 to prevent cross-client response leakage. Stateless MCP Servers should now create a new `McpServer` instance per request instead of sharing a single instance. A guard is added in this version of the MCP SDK which will prevent connection to a Server instance that has already been connected to a transport. Developers will need to modify their code if they declare their `McpServer` instance as a global variable.

#### MCP OAuth callback URL security fix

Added `callbackPath` option to `addMcpServer` to prevent instance name leakage in MCP OAuth callback URLs. When `sendIdentityOnConnect` is `false`, `callbackPath` is now required — the default callback URL would expose the instance name, undermining the security intent. Also fixes callback request detection to match via the `state` parameter instead of a loose `/callback` URL substring check, enabling custom callback paths.

#### Deprecate `onStateUpdate` in favor of `onStateChanged`

`onStateChanged` is a drop-in rename of `onStateUpdate` (same signature, same behavior). `onStateUpdate` still works but emits a one-time console warning per class. `validateStateChange` rejections now propagate a `CF_AGENT_STATE_ERROR` message back to the client.

#### x402 v2 migration

Migrated the x402 MCP payment integration from the legacy `x402` package to `@x402/core` and `@x402/evm` v2.

**Breaking changes for x402 users:**

- Peer dependencies changed: replace `x402` with `@x402/core` and `@x402/evm`
- `PaymentRequirements` type now uses v2 fields (e.g. `amount` instead of `maxAmountRequired`)
- `X402ClientConfig.account` type changed from `viem.Account` to `ClientEvmSigner` (structurally compatible with `privateKeyToAccount()`)

```bash
npm uninstall x402
npm install @x402/core @x402/evm
```

Network identifiers now accept both legacy names and CAIP-2 format:

```ts
// Legacy name (auto-converted)
{
	network: "base-sepolia",
}

// CAIP-2 format (preferred)
{
	network: "eip155:84532",
}
```

**Other x402 changes:**

- `X402ClientConfig.network` is now optional — the client auto-selects from available payment requirements
- Server-side lazy initialization: facilitator connection is deferred until the first paid tool invocation
- Payment tokens support both v2 ( `PAYMENT-SIGNATURE`) and v1 ( `X-PAYMENT`) HTTP headers
- Added `normalizeNetwork` export for converting legacy network names to CAIP-2 format
- Re-exports `PaymentRequirements`, `PaymentRequired`, `Network`, `FacilitatorConfig`, and `ClientEvmSigner` from `agents/x402`

#### Other improvements

- Fix `useAgent` and `AgentClient` crashing when using `basePath` routing
- CORS handling delegated to partyserver's native support (simpler, more reliable)
- Client-side `onStateUpdateError` callback for handling rejected state updates

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest
```

Feb 9, 2026

[<h2>Interactive browser terminals in Sandboxes</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/)

[Agents](https://developers.cloudflare.com/agents/)

The [Sandbox SDK ↗︎](https://github.com/cloudflare/sandbox-sdk) now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.

#### `sandbox.terminal(request)`

The new `terminal()` method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.

```js
// Worker: proxy WebSocket to container terminal
return sandbox.terminal(request, { cols: 80, rows: 24 });
```

```ts
// Worker: proxy WebSocket to container terminal
return sandbox.terminal(request, { cols: 80, rows: 24 });
```

#### Multiple terminals per sandbox

Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.

```js
// Multiple isolated terminals in the same sandbox
const dev = await sandbox.getSession("dev");
return dev.terminal(request);
```

```ts
// Multiple isolated terminals in the same sandbox
const dev = await sandbox.getSession("dev");
return dev.terminal(request);
```

#### xterm.js addon

The new `@cloudflare/sandbox/xterm` export provides a `SandboxAddon` for [xterm.js ↗︎](https://xtermjs.org/) with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.

```js
import { SandboxAddon } from "@cloudflare/sandbox/xterm";

const addon = new SandboxAddon({
	getWebSocketUrl: ({ sandboxId, origin }) =>
		`${origin}/ws/terminal?id=${sandboxId}`,
	onStateChange: (state, error) => updateUI(state),
});
terminal.loadAddon(addon);
addon.connect({ sandboxId: "my-sandbox" });
```

```ts
import { SandboxAddon } from "@cloudflare/sandbox/xterm";

const addon = new SandboxAddon({
	getWebSocketUrl: ({ sandboxId, origin }) =>
		`${origin}/ws/terminal?id=${sandboxId}`,
	onStateChange: (state, error) => updateUI(state),
});
terminal.loadAddon(addon);
addon.connect({ sandboxId: "my-sandbox" });
```

#### Upgrade

To update to the latest version:

```sh
npm i @cloudflare/sandbox@latest
```

Feb 9, 2026

[<h2>Analytics enhancements</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-analytics-enhancements/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.

![AI Crawl Control path patterns](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2256,height=1262,format=webp/_astro/ai-crawl-control-path-patterns.0xT_lucE.png)

**Path pattern grouping**

- In the **Metrics** tab > **Most popular paths** table, use the new **Patterns** tab that groups requests by URI pattern ( `/blog/*`, `/api/v1/*`, `/docs/*`) to identify which site areas crawlers target most. Refer to the screenshot above.

**Enhanced referral analytics**

- Destination patterns show which site areas receive AI-driven referral traffic.
- In the **Metrics** tab, a new **Referrals over time** chart shows trends by operator or source.

**Data transfer metrics**

- In the **Metrics** tab > **Allowed requests over time** chart, toggle **Bytes** to show bandwidth consumption.
- In the **Crawlers** tab, a new **Bytes Transferred** column shows bandwidth per crawler.

**Image exports**

- Export charts and tables as images for reports and presentations.

Learn more about [analyzing AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/).

Feb 9, 2026

[<h2>AI Search now with more granular controls over indexing</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/)

[AI Search](https://developers.cloudflare.com/ai-search/)

Get your content updates into [AI Search](https://developers.cloudflare.com/ai-search/) faster and avoid a full rescan when you do not need it.

#### Reindex individual files without a full sync

Updated a file or need to retry one that errored? When you know exactly which file changed, you can now [reindex it directly](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) instead of rescanning your entire data source.

Go to **Overview** > **Indexed Items** and select the sync icon next to any file to reindex it immediately.

![Sync individual files from Indexed Items](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2118,height=782,format=webp/_astro/individual-file-indexing.CQgoIj85.png)

#### Crawl only the sitemap you need

By default, AI Search crawls all sitemaps listed in your `robots.txt`, up to the [maximum files per index limit](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#limits). If your site has multiple sitemaps but you only want to index a specific set, you can now [specify a single sitemap URL](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap) to limit what the crawler visits.

For example, if your `robots.txt` lists both `blog-sitemap.xml` and `docs-sitemap.xml`, you can specify just `https://example.com/docs-sitemap.xml` to index only your documentation.

Configure your selection anytime in **Settings** > **Parsing options** > **Specific sitemaps**, then trigger a sync to apply the changes.

![Specify a sitemap in Parsinh options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1973,height=387,format=webp/_astro/specify-sitemap.pLCkwmJ-.png)

Learn more about [indexing controls](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) and [website crawling configuration](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap).

Feb 9, 2026

[<h2>R2 SQL now supports approximate aggregation functions</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/)

R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.

#### New functions

- `APPROX_PERCENTILE_CONT(column, percentile)` — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.
- `APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)` — Weighted percentile calculation where each row contributes proportionally to its weight column value.
- `APPROX_MEDIAN(column)` — Returns the approximate median. Equivalent to `APPROX_PERCENTILE_CONT(column, 0.5)`.
- `APPROX_DISTINCT(column)` — Returns the approximate number of distinct values. Works on any column type.
- `APPROX_TOP_K(column, k)` — Returns the `k` most frequent values with their counts as a JSON array.

All functions support `WHERE` filters. All except `APPROX_TOP_K` support `GROUP BY`.

#### Examples

```sql
-- Percentile analysis on revenue data
SELECT approx_percentile_cont(total_amount, 0.25),
       approx_percentile_cont(total_amount, 0.5),
       approx_percentile_cont(total_amount, 0.75)
FROM my_namespace.sales_data
```

```sql
-- Median per department
SELECT department, approx_median(total_amount)
FROM my_namespace.sales_data
GROUP BY department
```

```sql
-- Approximate distinct customers by region
SELECT region, approx_distinct(customer_id)
FROM my_namespace.sales_data
GROUP BY region
```

```sql
-- Top 5 most frequent departments
SELECT approx_top_k(department, 5)
FROM my_namespace.sales_data
```

```sql
-- Combine approximate and standard aggregations
SELECT COUNT(*),
       AVG(total_amount),
       approx_percentile_cont(total_amount, 0.5),
       approx_distinct(customer_id)
FROM my_namespace.sales_data
WHERE region = 'North'
```

For the full syntax and additional examples, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/).

Feb 9, 2026

[<h2>Tabs and pivots</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-tabs-and-pivots/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer now supports multiple concurrent queries with the new Tabs feature. Work with multiple queries simultaneously and pivot between datasets to investigate malicious activity more effectively.

#### Key capabilities

- **Multiple tabs:** Open and switch between multiple query tabs to compare results across different datasets.
- **Quick filtering:** Select the filter button from query results to add a value as a filter to your current query.
- **Pivot to new tab:** Use Cmd + click on the filter button to start a new query tab with that filter applied.
- **Preserved progress:** Your query progress is preserved on each tab if you navigate away and return.

For more information, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).

Feb 6, 2026

[<h2>Visualize data, share links, and create exports with the new Workers Observability dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/)

[Workers](https://developers.cloudflare.com/workers/)

The [Workers Observability dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/) has some major updates to make it easier to debug your application's issues and share findings with your team.

![Workers Observability dashboard showing events view with event details and share options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2540,height=1170,format=webp/_astro/2026-01-22-events_share_obs_wobs.BvzY4TNV.png)

You can now:

- **Create visualizations** — Build charts from your Worker data directly in a Worker's Observability tab
- **Export data as JSON or CSV** — Download logs and traces for offline analysis or to share with teammates
- **Share events and traces** — Generate direct URLs to specific events, invocations, and traces that open standalone pages with full context
- **Customize table columns** — Improved field picker to add, remove, and reorder columns in the events table
- **Expandable event details** — Expand events inline to view full details without leaving the table
- **Keyboard shortcuts** — Navigate the dashboard with hotkey support

![Workers Observability dashboard showing a P99 CPU time visualization grouped by outcome](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2596,height=1314,format=webp/_astro/2026-01-22-vis_qb_wobs.Bb5eVQNT.png)

These updates are now live in the Cloudflare dashboard, both in a Worker's Observability tab and in the account-level Observability dashboard for a unified experience. To get started, go to **Workers & Pages** > select your Worker > **Observability**.

Feb 4, 2026

[<h2>New reference documentation</h2>](https://developers.cloudflare.com/changelog/post/2026-02-09-reference-documentation/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

New reference documentation is now available for AI Crawl Control:

- **[GraphQL API reference](https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/)** — Query examples for crawler requests, top paths, referral traffic, and data transfer. Includes key filters for detection IDs, user agents, and referrer domains.
- **[Bot reference](https://developers.cloudflare.com/ai-crawl-control/reference/bots/)** — Detection IDs and user agents for major AI crawlers from OpenAI, Anthropic, Google, Meta, and others.
- **[Worker templates](https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/)** — Deploy the x402 Payment-Gated Proxy to monetize crawler access or charge bots while letting humans through free.

Feb 4, 2026

[<h2>Cloudflare Queues now available on Workers Free plan</h2>](https://developers.cloudflare.com/changelog/post/2026-02-04-queues-free-plan/)

[Queues](https://developers.cloudflare.com/queues/)

[Cloudflare Queues](https://developers.cloudflare.com/queues) is now part of the Workers free plan, offering guaranteed message delivery across up to **10,000 queues** to either [Cloudflare Workers](https://developers.cloudflare.com/workers) or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers). Every Cloudflare account now includes **10,000 operations per day** across reads, writes, and deletes. For more details on how each operation is defined, refer to [Queues pricing ↗︎](https://developers.cloudflare.com/workers/platform/pricing/#queues).

All features of the existing Queues functionality are available on the free plan, including unlimited [event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/). Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.

If you are new to Cloudflare Queues, follow [this guide ↗︎](https://developers.cloudflare.com/queues/get-started/) or try one of our [tutorials](https://developers.cloudflare.com/queues/tutorials/) to get started.

Feb 4, 2026

[<h2>Visualize your Workflows in the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Cloudflare Workflows now automatically generates visual diagrams from your code

Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:

- Understand how steps connect and execute
- Visualize loops and nested logic
- Follow branching paths for conditional logic

![Example diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1927,height=1530,format=webp/_astro/2026-02-03-workflows-diagram.BfQAnWL3.png)

You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.

Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/workflows) to see their diagrams.

Feb 3, 2026

[<h2>Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</h2>](https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/)

[Agents](https://developers.cloudflare.com/agents/) [Workflows](https://developers.cloudflare.com/workflows/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings first-class support for [Cloudflare Workflows](https://developers.cloudflare.com/workflows/), synchronous state management, and new scheduling capabilities.

#### Cloudflare Workflows integration

Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.

Use the new `AgentWorkflow` class to define workflows with typed access to your Agent:

```js
import { AgentWorkflow } from "agents/workflows";

export class ProcessingWorkflow extends AgentWorkflow {
	async run(event, step) {
		// Call Agent methods via RPC
		await this.agent.updateStatus(event.payload.taskId, "processing");

		// Non-durable: progress reporting to clients
		await this.reportProgress({ step: "process", percent: 0.5 });
		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });

		// Durable via step: idempotent, won't repeat on retry
		await step.mergeAgentState({ taskProgress: 0.5 });

		const result = await step.do("process", async () => {
			return processData(event.payload.data);
		});

		await step.reportComplete(result);
		return result;
	}
}
```

```ts
import { AgentWorkflow } from "agents/workflows";
import type { AgentWorkflowEvent, AgentWorkflowStep } from "agents/workflows";

export class ProcessingWorkflow extends AgentWorkflow<MyAgent, TaskParams> {
	async run(event: AgentWorkflowEvent<TaskParams>, step: AgentWorkflowStep) {
		// Call Agent methods via RPC
		await this.agent.updateStatus(event.payload.taskId, "processing");

		// Non-durable: progress reporting to clients
		await this.reportProgress({ step: "process", percent: 0.5 });
		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });

		// Durable via step: idempotent, won't repeat on retry
		await step.mergeAgentState({ taskProgress: 0.5 });

		const result = await step.do("process", async () => {
			return processData(event.payload.data);
		});

		await step.reportComplete(result);
		return result;
	}
}
```

Start workflows from your Agent with `runWorkflow()` and handle lifecycle events:

```js
export class MyAgent extends Agent {
	async startTask(taskId, data) {
		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
			taskId,
			data,
		});
		return { instanceId };
	}

	async onWorkflowProgress(workflowName, instanceId, progress) {
		this.broadcast(JSON.stringify({ type: "progress", progress }));
	}

	async onWorkflowComplete(workflowName, instanceId, result) {
		console.log(`Workflow ${instanceId} completed`);
	}

	async onWorkflowError(workflowName, instanceId, error) {
		console.error(`Workflow ${instanceId} failed:`, error);
	}
}
```

```ts
export class MyAgent extends Agent {
	async startTask(taskId: string, data: string) {
		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
			taskId,
			data,
		});
		return { instanceId };
	}

	async onWorkflowProgress(
		workflowName: string,
		instanceId: string,
		progress: unknown,
	) {
		this.broadcast(JSON.stringify({ type: "progress", progress }));
	}

	async onWorkflowComplete(
		workflowName: string,
		instanceId: string,
		result?: unknown,
	) {
		console.log(`Workflow ${instanceId} completed`);
	}

	async onWorkflowError(
		workflowName: string,
		instanceId: string,
		error: unknown,
	) {
		console.error(`Workflow ${instanceId} failed:`, error);
	}
}
```

Key workflow methods on your Agent:

- `runWorkflow(workflowName, params, options?)` — Start a workflow with optional metadata
- `getWorkflow(workflowId)` / `getWorkflows(criteria?)` — Query workflows with cursor-based pagination
- `approveWorkflow(workflowId)` / `rejectWorkflow(workflowId)` — Human-in-the-loop approval flows
- `pauseWorkflow()`, `resumeWorkflow()`, `terminateWorkflow()` — Workflow control

#### Synchronous setState()

State updates are now synchronous with a new `validateStateChange()` validation hook:

```js
export class MyAgent extends Agent {
	validateStateChange(oldState, newState) {
		// Return false to reject the change
		if (newState.count < 0) return false;
		// Return modified state to transform
		return { ...newState, lastUpdated: Date.now() };
	}
}
```

```ts
export class MyAgent extends Agent<Env, State> {
	validateStateChange(oldState: State, newState: State): State | false {
		// Return false to reject the change
		if (newState.count < 0) return false;
		// Return modified state to transform
		return { ...newState, lastUpdated: Date.now() };
	}
}
```

#### scheduleEvery() for recurring tasks

The new `scheduleEvery()` method enables fixed-interval recurring tasks with built-in overlap prevention:

```js
// Run every 5 minutes
await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });
```

```ts
// Run every 5 minutes
await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });
```

#### Callable system improvements

- **Client-side RPC timeout** — Set timeouts on callable method invocations
- **`StreamingResponse.error(message)`** — Graceful stream error signaling
- **`getCallableMethods()`** — Introspection API for discovering callable methods
- **Connection close handling** — Pending calls are automatically rejected on disconnect

```js
await agent.call("method", [args], {
	timeout: 5000,
	stream: { onChunk, onDone, onError },
});
```

```ts
await agent.call("method", [args], {
	timeout: 5000,
	stream: { onChunk, onDone, onError },
});
```

#### Email and routing enhancements

**Secure email reply routing** — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.

**Routing improvements:**

- `basePath` option to bypass default URL construction for custom routing
- Server-sent identity — Agents send `name` and `agent` type on connect
- New `onIdentity` and `onIdentityChange` callbacks on the client

```js
const agent = useAgent({
	basePath: "user",
	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
});
```

```ts
const agent = useAgent({
	basePath: "user",
	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
});
```

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest
```

For the complete Workflows API reference and patterns, see [Run Workflows](https://developers.cloudflare.com/agents/runtime/execution/run-workflows/).

Feb 3, 2026

[<h2>Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</h2>](https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/)

[R2](https://developers.cloudflare.com/r2/)

[Local Uploads](https://developers.cloudflare.com/r2/buckets/local-uploads/) is now available in open beta. Enable it on your [R2](https://developers.cloudflare.com/r2/) bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to [How R2 works](https://developers.cloudflare.com/r2/how-r2-works/) for details on how data is written to your bucket.

In our tests, we observed **up to 75% reduction in Time to Last Byte (TTLB)** for upload requests when Local Uploads is enabled.

![Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=596,format=webp/_astro/local-uploads-latency.R4pUgVuI.png)

This feature is ideal when:

- Your users are globally distributed
- Upload performance and reliability is critical to your application
- You want to optimize write performance without changing your bucket's primary location

To enable Local Uploads on your bucket, find **Local Uploads** in your bucket settings in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/r2/overview), or run:

```sh
npx wrangler r2 bucket local-uploads enable <BUCKET_NAME>
```

Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard [Class A operation costs](https://developers.cloudflare.com/r2/pricing/) same as upload requests made without Local Uploads.

For more information, refer to [Local Uploads](https://developers.cloudflare.com/r2/buckets/local-uploads/).

Feb 3, 2026

[<h2>Threat actor identification with "also known as" aliases</h2>](https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/)

[Security Center](https://developers.cloudflare.com/security-center/)

Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, **Cloudflare Threat Events** now include an **Also known as** field, providing a list of common aliases and industry-standard names for the groups we track.

This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the **Attacker** field) or by adding it as a column in your configurable table view.

#### Key benefits

- Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.
- Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.

For more information on how to access this data, refer to the [Threat Events API documentation ↗︎](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/).

Feb 2, 2026

[<h2>Improved Accessibility and Search for Monitoring</h2>](https://developers.cloudflare.com/changelog/post/2026-02-02-improved-accessibility-search-for-monitoring/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We have updated the Monitoring page to provide a more streamlined and insightful experience for administrators, improving both data visualization and dashboard accessibility.

- **Enhanced Visual Layout**: Optimized contrast and the introduction of stacked bar charts for clearer data visualization and trend analysis. ![visual-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3212,height=2344,format=webp/_astro/monitoring-bar-charts.Bi-4BuXC.png)
- **Improved Accessibility & Usability**:
  - **Widget Search**: Added search functionality to multiple widgets, including Policies, Submitters, and Impersonation.
  - **Actionable UI**: All available actions are now accessible via dedicated buttons.
  - **State Indicators**: Improved UI states to clearly communicate loading, empty datasets, and error conditions. ![buttons-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3178,height=664,format=webp/_astro/monitoring-buttons.DORPJvP_.png)
- **Granular Data Breakdowns**: New views for dispositions by month, malicious email details, link actions, and impersonations. ![monthly-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3202,height=1486,format=webp/_astro/monitoring-monthly-dispositions.CYuI5d9y.png)

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Feb 2, 2026

[<h2>WAF Release - 2026-02-02</h2>](https://developers.cloudflare.com/changelog/post/2026-02-02-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.

**Key Findings**

- CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the `Q()` class.
- CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...30698ff3 | N/A | XWiki - Remote Code Execution - CVE:CVE-2025-24893 2 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...da8ba7e6 | N/A | Django SQLI - CVE:CVE-2025-64459 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...8d667511 | N/A | NoSQL, MongoDB - SQLi - Comparison - 2 | Block | Block | Rule metadata description refined. Detection unchanged. |

Jan 30, 2026

[<h2>Reduced minimum cache TTL for Workers KV to 30 seconds</h2>](https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/)

[KV](https://developers.cloudflare.com/kv/)

The minimum `cacheTtl` parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both `get()` and `getWithMetadata()` methods.

This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.

The `cacheTtl` parameter defines how long a KV result is cached at the global network location it is accessed from:

```js
// Read with custom cache TTL
const value = await env.NAMESPACE.get("my-key", {
	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)
});

// getWithMetadata also supports the reduced cache TTL
const valueWithMetadata = await env.NAMESPACE.getWithMetadata("my-key", {
	cacheTtl: 30, // Cache for minimum 30 seconds
});
```

The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds `cacheTtl`.

This change affects all KV read operations using the binding API. For more information, consult the [Workers KV cache TTL documentation](https://developers.cloudflare.com/kv/api/read-key-value-pairs/#cachettl-parameter).

Jan 30, 2026

[<h2>BGP over GRE and IPsec tunnels</h2>](https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

For configuration details, refer to:

- [Configure BGP routes for Magic WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
- [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/29/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/29/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
