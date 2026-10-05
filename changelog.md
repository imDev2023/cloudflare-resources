# Cloudflare changelog digest

Snapshot: built on 2026-10-05 from the mirror of `https://developers.cloudflare.com/changelog/` in `raw/docs/changelog/` (1,307 individual posts dated 2024-02-26 to 2026-10-02, plus listing pages).

The Cloudflare changelog is a single stream of dated posts, each tagged with one or more of 91 products that roll up into 13 product groups, and it is followed through a global RSS feed, 7 product-group feeds and per-product feeds.
In the twelve months from 2025-10-01 to 2026-10-05 it published 912 entries, more than twice the 395 posted before that in the mirror; Developer platform is the largest group (420 entries in the window) and AI more than doubled from 57 entries in 2025 to 132 in 2026 so far.
The year's dominant themes were agent infrastructure (frequent Agents SDK releases, MCP 2026-07-28 support, MCP server portals GA, Sandboxes and Containers GA, Dynamic Workers, Browser Run, Kitesurf, temporary accounts for agents), a large Workers AI model refresh with an 18-model deprecation and paid-plan gating of frontier models, the unification of Workers AI and AI Gateway billing, the launch and GA of Basin (the renamed data platform) with billing switched on, and the Magic-to-Cloudflare networking renames with Unified Routing reaching GA.
Payments for agents arrived at the very end of the window: Monetization Gateway (closed beta) and AI Gateway Machine Payments (beta) both use x402, the latter paying from a stablecoin wallet, both on 2026-09-30.
Breaking changes and deprecations clustered around SDK majors (Python v5, TypeScript v6, Go v7), Workers runtime defaults tied to compatibility dates, API retirements (Service Keys on 2026-09-30, Tunnel CIDR route endpoints on 2026-10-05, legacy KV routes on 2026-10-15) and Durable Objects moving to SQLite only for new namespaces.
No changelog entry mentions Ethereum gateways, IPFS gateways, web3 gateway product changes or randomness (drand).

## Contents

1. [How the changelog is organised and how to follow it](#how-the-changelog-is-organised-and-how-to-follow-it)
2. [Counts](#counts)
3. [Per-product-group digest, 2025-10-01 to 2026-10-05](#per-product-group-digest-2025-10-01-to-2026-10-05)
   1. [AI](#ai)
   2. [Developer platform: Workers, Pages, Workers for Platforms, Cloudflare CLI](#developer-platform-workers-pages-workers-for-platforms-cloudflare-cli)
   3. [Developer platform: Containers, Sandboxes, Workflows, Workers VPC, Artifacts, Flagship, Email Service, media](#developer-platform-containers-sandboxes-workflows-workers-vpc-artifacts-flagship-email-service-media)
   4. [Storage and data](#storage-and-data)
   5. [Application security](#application-security)
   6. [Application performance and network security](#application-performance-and-network-security)
   7. [Cloudflare One](#cloudflare-one)
   8. [Core platform, analytics and consumer services](#core-platform-analytics-and-consumer-services)
4. [Month-by-month timeline of 2026](#month-by-month-timeline-of-2026)
5. [Deprecations and breaking changes (whole mirror)](#deprecations-and-breaking-changes-whole-mirror)
6. [Web3, payments and agents](#web3-payments-and-agents)
7. [Gaps and contradictions](#gaps-and-contradictions)

## How the changelog is organised and how to follow it

### Where things live

- The landing page `https://developers.cloudflare.com/changelog/` shows the newest posts first, with a filter for "All products", 13 product groups and 91 products (mirrored at `raw/docs/changelog/index.md`).
- Older posts are on numbered listing pages `https://developers.cloudflare.com/changelog/2/` to `/53/` (mirrored as `raw/docs/changelog/2/` to `53/`); page 53 ends with the oldest entries from 2024.
- Each entry has its own page at `https://developers.cloudflare.com/changelog/post/<slug>/`, mirrored at `raw/docs/changelog/post/<slug>/index.md` (1,307 posts).
  Most slugs start with a date (`YYYY-MM-DD-topic`), but 9 do not (for example `scheduled-waf-release`, `Gateway-application-categories-added`), and 8 slugs carry a date more than 30 days away from the publish date (see Gaps).
- A post page shows the publish date, the title, one link per product tag, "Copy as Markdown" and "View as Markdown" (`.../index.md`) links and an "Agent setup" link, then the body; a JSON-LD block carries `datePublished` and `dateModified`.
- Per-product filters are pages at `https://developers.cloudflare.com/changelog/product/<product>/` (91 mirrored, paginated as `/product/<product>/2/` and so on), for example `/changelog/product/workers/` or `/changelog/product/monetization-gateway/`.
- Per-group filters are pages at `https://developers.cloudflare.com/changelog/product-group/<group>/` for the 13 groups: `ai`, `analytics`, `application-performance`, `application-security`, `cloudflare-one`, `consumer-services`, `core-platform`, `developer-platform`, `docs-collections`, `media`, `network-security`, `privacy`, `storage`.
- One post can carry several product tags and therefore appear in several groups: 282 posts carry more than one product tag and 654 belong to more than one group.

### RSS feeds

The "Available RSS Feeds" page (`https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/`, last updated Apr 20, 2026) lists:

- The global feed, `https://developers.cloudflare.com/changelog/rss/index.xml`, which every changelog listing page also links as "Subscribe to RSS".
- Seven product-area feeds: `application-performance.xml`, `application-security.xml`, `cloudflare-one.xml`, `consumer-services.xml`, `core-platform.xml`, `developer-platform.xml` and `network-security.xml`, all under `https://developers.cloudflare.com/changelog/rss/`.
- One feed per product at `https://developers.cloudflare.com/changelog/rss/<product>.xml` (88 product feeds, for example `workers.xml`, `ai-gateway.xml`, `monetization-gateway.xml`, `web-search.xml`, `basin.xml`, `cf.xml` for the Cloudflare CLI); 96 distinct feed URLs in total.
- Separate feeds outside the changelog for the DDoS managed rulesets (`https://developers.cloudflare.com/ddos-protection/change-log/network/index.xml` and `.../change-log/http/index.xml`) and for API deprecations (`https://developers.cloudflare.com/fundamentals/api/reference/deprecations/index.xml`).

The "Consuming RSS Feeds" page (`https://developers.cloudflare.com/fundamentals/new-features/consuming-rss-feeds/`) says items carry HTML in `<description>`, the products of an entry in `<category>` tags, and a single product in a custom `<product>` tag kept "for legacy reasons"; it recommends `<category>`, and points to Slack, Microsoft Teams and Google Chat as RSS consumers.

### Practical ways to follow it

- To watch one product, subscribe to its product feed or open its `/changelog/product/<product>/` page.
- To watch a whole area, use one of the seven area feeds; the AI, Analytics, Docs collections, Media, Privacy and Storage groups have filter pages but no listed group feed.
- To read a post as Markdown, append `index.md` to its URL, as the "View as Markdown" link does.
- WAF managed ruleset changes are announced in weekly "WAF Release" posts (tag WAF) plus a rolling `https://developers.cloudflare.com/changelog/post/scheduled-waf-release/` post listing upcoming action changes.

## Counts

All counts are of individual posts in the mirror, by publish date (`datePublished`).
A post counts once per year, but once in every group or product it is tagged with, so group and product rows add up to more than the total.

| Year | Entries |
| --- | --- |
| 2024 | 29 |
| 2025 | 507 |
| 2026 | 771 |
| Total | 1307 |

Entries per product group, by publish year and for the twelve-month digest window.
Group membership comes from the changelog's own product-group pages.

| Product group | 2024 | 2025 | 2026 (to 2026-10-05) | All years | 2025-10-01 to 2026-10-05 |
| --- | --- | --- | --- | --- | --- |
| Developer platform | 6 | 233 | 368 | 607 | 420 |
| Cloudflare One | 12 | 111 | 202 | 325 | 234 |
| Application security | 5 | 102 | 112 | 219 | 143 |
| Core platform | 7 | 77 | 125 | 209 | 153 |
| AI | 1 | 57 | 132 | 190 | 145 |
| Analytics | 4 | 45 | 85 | 134 | 107 |
| Storage | 1 | 46 | 79 | 126 | 89 |
| Network security | 10 | 29 | 59 | 98 | 64 |
| Application performance | 10 | 35 | 49 | 94 | 53 |
| Docs collections | 0 | 27 | 46 | 73 | 56 |
| Consumer services | 0 | 10 | 26 | 36 | 30 |
| Media | 0 | 10 | 15 | 25 | 15 |
| Privacy | 0 | 1 | 3 | 4 | 3 |

Entries per month since January 2025, the first month with more than ten posts.

| Month | Entries |
| --- | --- |
| 2025-01 | 19 |
| 2025-02 | 39 |
| 2025-03 | 41 |
| 2025-04 | 47 |
| 2025-05 | 36 |
| 2025-06 | 40 |
| 2025-07 | 37 |
| 2025-08 | 55 |
| 2025-09 | 52 |
| 2025-10 | 58 |
| 2025-11 | 46 |
| 2025-12 | 37 |
| 2026-01 | 48 |
| 2026-02 | 64 |
| 2026-03 | 76 |
| 2026-04 | 115 |
| 2026-05 | 77 |
| 2026-06 | 75 |
| 2026-07 | 92 |
| 2026-08 | 104 |
| 2026-09 | 98 |
| 2026-10 | 22 |

Entries per product tag (all 91 products that have at least one post), over all years and in the digest window.

| Product tag | All years | 2025-10-01 to 2026-10-05 |
| --- | --- | --- |
| Workers | 253 | 161 |
| WAF | 122 | 73 |
| Cloudflare One | 78 | 64 |
| Cloudflare Fundamentals | 70 | 53 |
| Access | 65 | 51 |
| Cloudflare One Client | 62 | 56 |
| Gateway | 46 | 28 |
| Agents | 42 | 33 |
| Cloudflare WAN | 41 | 31 |
| Workers AI | 36 | 27 |
| Radar | 34 | 28 |
| AI Search | 32 | 25 |
| Basin | 32 | 27 |
| Logs | 30 | 25 |
| Browser Run | 30 | 22 |
| Durable Objects | 30 | 25 |
| Rules | 29 | 15 |
| Workflows | 28 | 21 |
| Email security | 26 | 11 |
| R2 | 26 | 19 |
| Containers | 26 | 25 |
| AI Gateway | 25 | 17 |
| Data Loss Prevention | 24 | 14 |
| Security Center | 24 | 21 |
| Cache / CDN | 23 | 12 |
| Cloudflare Tunnel | 20 | 16 |
| Terraform | 18 | 8 |
| Cloudflare Tunnel for SASE | 17 | 11 |
| Hyperdrive | 17 | 9 |
| Log Explorer | 17 | 11 |
| AI Crawl Control | 16 | 12 |
| Cloudflare One Appliance | 15 | 12 |
| Magic Transit | 14 | 10 |
| DNS | 14 | 8 |
| Basin Catalog | 14 | 12 |
| Stream | 12 | 4 |
| Queues | 12 | 7 |
| Basin SQL | 12 | 11 |
| CASB | 11 | 7 |
| Email Service | 11 | 7 |
| Cloudflare Mesh | 11 | 11 |
| Digital Experience Monitoring | 10 | 7 |
| D1 | 10 | 5 |
| Basin Pipelines | 10 | 8 |
| Browser Isolation | 9 | 4 |
| Cloudflare Network Firewall | 9 | 6 |
| Load Balancing | 9 | 5 |
| KV | 8 | 5 |
| SSL/TLS | 8 | 4 |
| Cloudflare Images | 8 | 6 |
| Analytics | 8 | 7 |
| Workers VPC | 8 | 8 |
| Workers for Platforms | 7 | 1 |
| API Shield | 7 | 6 |
| Audit Logs | 7 | 4 |
| Vectorize | 7 | 5 |
| Artifacts | 7 | 7 |
| Pages | 6 | 2 |
| SDK | 6 | 6 |
| Cloudflare Web Analytics | 5 | 4 |
| Realtime | 5 | 5 |
| Logpush | 5 | 5 |
| Network Flow | 4 | 2 |
| Network Interconnect | 4 | 1 |
| Risk Score | 4 | 2 |
| Secrets Store | 4 | 0 |
| Flagship | 4 | 4 |
| Sandboxes | 4 | 4 |
| Bots | 4 | 4 |
| Workers Analytics Engine | 3 | 3 |
| Support | 3 | 3 |
| Speed | 3 | 3 |
| Multi-Cloud Networking | 2 | 0 |
| Registrar | 2 | 0 |
| Security Overview | 2 | 2 |
| Organizations | 2 | 2 |
| Go SDK | 2 | 2 |
| Billing | 2 | 2 |
| 1.1.1.1 (DNS Resolver) | 2 | 2 |
| Zaraz | 1 | 0 |
| Cloudflare for SaaS | 1 | 0 |
| Privacy Proxy | 1 | 1 |
| Resource Tagging | 1 | 1 |
| Data Localization Suite | 1 | 1 |
| Turnstile | 1 | 1 |
| Agent Lee | 1 | 1 |
| Logpush Connectors | 1 | 1 |
| Automatic Platform Optimization | 1 | 1 |
| Cloudflare CLI | 1 | 1 |
| Monetization Gateway | 1 | 1 |
| Web Search API | 1 | 1 |

## Per-product-group digest, 2025-10-01 to 2026-10-05

Each bullet gives the publish date, a type label (Launch, GA, Beta, Pricing, Limits, Deprecation, Breaking, Rename, Change, Security, Release), what the post says, and the changelog URL(s).
Products are grouped by the group they mainly belong to; a post tagged with several products is listed under the most specific one.
Counts per product are entries tagged with that product in the window.

### AI

#### Agents (Agents SDK, Think, Code Mode, Sandbox SDK, MCP)

33 entries tagged Agents in the window.
The Agents SDK shipped roughly every two to four weeks, from v0.2.24 (November 2025) to v0.20.0 (July 2026), and several releases carried breaking changes.

- **2025-11-26 - Release** - Agents SDK v0.2.24 added resumable streaming in `AIChatAgent`, a redesigned `MCPClientManager` API (`registerServer()`, `connectToServer()`), a default JSON schema validator for the MCP client, and fixes so schedules can safely destroy the agent.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-26-agents-resumable-streaming/
- **2025-12-22 - Breaking** - Agents SDK v0.3.0, `workers-ai-provider` v3.0.0 and `ai-gateway-provider` v3.0.0 moved to AI SDK v6, with the unified tool pattern and dynamic tool approval (`needsApproval`).
  The post says `convertToModelMessages()` is now asynchronous, the `CoreMessage` type was removed in favour of `ModelMessage`, and the v5 static-only tool checks need new helper functions.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/
- **2026-02-03 - Release** - Agents SDK v0.3.7 added first-class Workflows integration, synchronous state, `scheduleEvery()`, a `basePath` routing option and server-sent identity (`onIdentity`, `onIdentityChange`).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/
- **2026-02-09 - Breaking** - Agents SDK v0.4.0 added readonly WebSocket connections, MCP security changes, custom MCP OAuth providers (`createMcpOAuthProvider`) and migrated the x402 integration to x402 v2 (details in the Web3 section).
  `onStateChanged` replaces `onStateUpdate` (the old name still works with a one-time warning), and when `sendIdentityOnConnect` is `false` a `callbackPath` is now required.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/
- **2026-02-09 - Launch** - The Sandbox SDK gained PTY passthrough through a `terminal()` method so browser terminal UIs can attach to sandbox shells over WebSocket.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/
- **2026-02-13 - Launch** - The new `@cloudflare/tanstack-ai` package and `workers-ai-provider` v3.1.1 shipped with GLM-4.7-Flash; `createAISearch` became the canonical export, renamed from AutoRAG, and `createAutoRAG` now emits a deprecation warning.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/
- **2026-02-17 - Release** - Agents SDK v0.5.0 added `this.retry()` with exponential backoff, per-connection protocol message control, and the first stable `@cloudflare/ai-chat` (v0.1.0).
  `autoContinueAfterToolResult` now defaults to `true`, and a row size guard compacts messages as they approach the SQLite 2 MB limit.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/
- **2026-02-20 - Breaking** - `@cloudflare/codemode` v0.1.0 was rewritten as a runtime-agnostic modular SDK; `experimental_codemode()` and `CodeModeProxy` were removed and `createCodeTool()` moved to `@cloudflare/codemode/ai`.
  Network access from generated code is blocked by default (`globalOutbound: null`).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/
- **2026-02-23 - Launch** - The Sandbox SDK added `createBackup()` and `restoreBackup()` for point-in-time directory snapshots, with named backups and TTLs.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/
- **2026-02-25 - Release** - Agents SDK v0.6.0 lets an Agent and an McpAgent in the same Worker talk over RPC through a Durable Object binding, makes OAuth opt-in for simple MCP connections, and un-deprecates the client tool APIs (`createToolsFromClientSchemas`, `clientTools`, `AITool`, `extractClientToolSchemas`).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/
- **2026-03-02 - Breaking** - Agents SDK v0.7.0 rewrote observability on `diagnostics_channel` (replacing `Observability.emit()` and `console.log()`), added `keepAlive()` to prevent Durable Object eviction, and added `waitForMcpConnections` (default wait 10 seconds).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/
- **2026-03-03 - Launch** - Sandboxes support real-time filesystem watching through `sandbox.watch()`, an inotify-backed Server-Sent Events stream.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/
- **2026-03-17 - Breaking** - `@cloudflare/codemode` v0.2.1 added a `@cloudflare/codemode/mcp` entry point and dropped `ai` and `zod` as required peer dependencies of the main entry; the post flags a breaking change in v0.2.0 that moved `generateTypes` and the `ToolDescriptor` types to `@cloudflare/codemode/ai`.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/
- **2026-03-23 - Breaking** - Agents SDK v0.8.0 exposes a readable `state` property, makes cron schedules idempotent by default, adds a typed `AgentClient`, and migrates to Zod 4; Zod v3 is no longer supported.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/
- **2026-04-15 - Launch** - Agent Lee, the dashboard AI assistant, gained write operations (for example creating DNS records or changing SSL mode) and generative UI charts.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/
- **2026-05-13 - Breaking** - Agents SDK v0.12.4 keeps server chat turns running when a client stream is interrupted (opt out with `cancelOnClientAbort: true`), adds durable Think submissions and Voice connection control, and removes `ChatOptions.tools` from the TypeScript API.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/
- **2026-05-29 - Launch** - Sandboxes can share a service on a public preview URL through `sandbox.tunnels`, defaulting to a quick tunnel on `*.trycloudflare.com`.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/
- **2026-06-02 - Release** - Agents SDK v0.14.0 added Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks and durable reasoning steps inside Workflows for `@cloudflare/think`.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/
- **2026-06-16 - Release** - Agents SDK v0.16.1 lets agents browse through Browser Run, write code against tools through Code Mode, and pass client tools to Think sub-agents.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-agents-sdk-v0.16.1/
- **2026-06-26 - Release** - Agents SDK v0.17.0 added detached (background) sub-agent runs with a `maxBudgetMs` ceiling (default 24 hours) and `cancelAgentTool(runId)`, plus a single `runTurn` entry point.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-26-agents-sdk-v0.17.0/
- **2026-07-13 - Launch** - Agents connected to MCP servers with `addMcpServer` can answer MCP elicitation requests, in form mode or URL mode (for example third-party authorization or payment).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/
- **2026-07-22 - Change** - MCP clients reuse converted schemas while a connection keeps the same tool catalog, Think gained an opt-out for automatic MCP tool exposure, and Code Mode exposes direct host APIs.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/
- **2026-07-23 - Change** - `agents`, `@cloudflare/ai-chat`, `@cloudflare/codemode` and `@cloudflare/think` support both AI SDK v6 and v7 (peer ranges `ai@^6 || ^7`, `@ai-sdk/react@^3 || ^4`).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-23-ai-sdk-v6-v7-support/
- **2026-07-27 - Deprecation** - Agents SDK v0.20.0 added client and server support for the MCP 2026-07-28 release candidate, with stateless MCP serving that needs no transport session or Durable Object.
  `McpAgent` is deprecated and feature-frozen with no removal version announced, `createMcpHandler(v1Server, options)` is scheduled for removal in the next major version, and the `callTool(params, resultSchema, options)` overload (and the matching `withX402Client` overload) is a compatibility overload.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/
- **2026-07-28 - Breaking** - Cloudflare's product MCP servers support MCP 2026-07-28 on stateless servers; historical `/sse` URLs still work as aliases but no longer serve the deprecated HTTP+SSE transport.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/
- **2026-08-03 - Beta** - Early preview of `@cloudflare/computer`, an open-source agent runtime that orchestrates between isolates and full Linux containers with a SQLite-backed virtual filesystem.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/
- **2026-08-04 - Launch** - Agent tracing for Think, Flue and AI SDK apps instrumented by the Agents SDK, shown alongside Workers runtime operations; payload recording is off by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/
- **2026-08-22 - Change** - Wrangler and the Cloudflare API MCP server use optional OAuth scopes, so users can grant fewer scopes in the consent dialog.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/
- **2026-09-11 - Release** - `@cloudflare/voice` v0.4.0 adds per-turn latency and outcome diagnostics for Voice Agents (off by default, event names may change).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/
- **2026-10-01 - Release** - `@cloudflare/workers-oauth-provider` reached v1 with a split API (authorization server and resource server in separate Workers over a Service Binding) and full MCP 2026-07-28 authorization support; a migration guide and a `migrate-to-1.0` agent skill ship in the package.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/
- **2026-10-02 - Beta** - `PiHarness` adds first-class support for the Pi 1.0 and Pi Durable agent harness (built with Earendil); the post says the API will likely change.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/

#### Workers AI

27 entries tagged Workers AI in the window.

- **2025-10-02 - Launch** - Deepgram Flux (`@cf/deepgram/flux`) launched for voice agents; official pricing was to be charged after a promotional period ending October 31, 2025.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/
- **2025-10-23 - Change** - Markdown Conversion gained an endpoint to list supported formats.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/
- **2025-11-25 - Launch** - FLUX.2 [dev] from Black Forest Labs launched; the post said pricing was expected to drop within days.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/
- **2026-01-15 - Launch** - FLUX.2 [klein] 4B launched (fixed 4-step inference), followed by FLUX.2 [klein] 9B on 2026-01-28.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/
- **2026-02-13 - Launch** - GLM-4.7-Flash (`@cf/zai-org/glm-4.7-flash`) launched with multi-turn tool calling.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/
- **2026-03-04 - Change** - Markdown Conversion accepts a `conversionOptions` object per file type.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/
- **2026-03-11 - Launch** - NVIDIA Nemotron 3 Super (`@cf/nvidia/nemotron-3-120b-a12b`, 120B total, 12B active) launched.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/
- **2026-03-19 - Launch** - Kimi K2.5 (`@cf/moonshotai/kimi-k2.5`), described as the first frontier-scale open-source model on the platform, launched with a 256k context window; cached tokens are now surfaced as a usage metric and discounted versus input tokens, and asynchronous batch inference is available.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-19-kimi-k2-5-workers-ai/
- **2026-04-04 - Launch** - Google Gemma 4 26B A4B (`@cf/google/gemma-4-26b-a4b-it`) launched.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/
- **2026-04-20 - Launch** - Kimi K2.6 (`@cf/moonshotai/kimi-k2.6`, 1T total, 32B active, 262.1k context) launched with Day 0 support.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/
- **2026-05-08 - Deprecation** - Planned model deprecations: 18 models were deprecated on May 30, 2026, including `@cf/moonshotai/kimi-k2.5` (auto-aliased to the higher-priced `kimi-k2.6`), the Llama 2, Llama 3 and Llama 3.1 8B/70B instruct models, `mistral-7b-instruct-v0.1` and `v0.2`, `gemma-7b-it`, `gemma-3-12b-it`, `hermes-2-pro-mistral-7b`, `phi-2`, `sqlcoder-7b-2`, `uform-gen2-qwen-500m` and `bart-large-cnn`.
  The Kimi K2.5 date moved from the originally stated May 10, 2026 to May 30, 2026; `-fast` and `-lora` variants stay active, and the post warns LoRA models may be deprecated later.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/
- **2026-06-12 - Launch** - Kimi K2.7 Code (`@cf/moonshotai/kimi-k2.7-code`) launched with thinking mode and a 262.1k context window.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/
- **2026-06-16 - Launch** - GLM-5.2 (`@cf/zai-org/glm-5.2`) launched with a 262,144 token context window.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/
- **2026-07-08 - Launch** - Moondream 3.1 (`@cf/moondream/moondream3.1-9B-A2B`) launched; `toMarkdown` gained GIF and BMP support the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/
- **2026-07-10 - Change** - Markdown Conversion gained `output.format: "text"` for plain text (default stays `markdown`).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/
- **2026-07-28 - Pricing** - Kimi K2.6, Kimi K2.7 Code and GLM-5.2 now require the Workers Paid plan; Free plan requests return HTTP `403` (internal error `5035`).
  The post restates that Workers Paid starts at $5 per month and includes 10,000 free Neurons per day.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/
- **2026-08-07 - Pricing** - Workers AI and AI Gateway unified model access and billing: prepaid AI Gateway credits can pay for Workers AI (gateway setting **Unified billing**), and give access to the frontier models without Workers Paid, at 50 requests per minute per model when billed with credits versus 20 requests per minute through standard Workers AI billing.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
- **2026-08-14 - Launch** - DeepSeek V4 Flash and Pro (`@cf/deepseek-ai/deepseek-v4-flash-0731`, `@cf/deepseek-ai/deepseek-v4-pro-0813`) launched as the first Workers AI models with a 1,048,576 token context window; they require Workers Paid or AI Gateway credits.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/
- **2026-08-17 - Launch** - Qwen 3.8 27B (`@cf/qwen/qwen3.8-27b`) vision language model launched.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/
- **2026-08-26 - Launch** - GLM-5.3 Flash (`@cf/zai-org/glm-5.3-flash`, 320B total, 18B active, first multimodal GLM on Workers AI) launched; Workers Paid or credits required.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/
- **2026-08-28 - Pricing** - GLM-5.3 (`@cf/zai-org/glm-5.3`) launched at the same price as GLM-5.2: $1.40 per million input tokens, $0.26 per million cached input tokens and $4.40 per million output tokens.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/
- **2026-09-17 - Change** - The `rejectIfBusy` option lets synchronous inference fail fast instead of waiting in a capacity queue.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/
- **2026-10-01 - Launch** - Clef and Clef-flash (`@cf/cloudflare/clef`, `@cf/cloudflare/clef-flash`), the first models trained by the Workers AI team, are open-source decision models that return probabilities for typed questions (`noul`, `choice`, `score`).
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/

#### AI Search (formerly AutoRAG)

25 entries tagged AI Search in the window.

- **2025-10-28 - Launch** - Reranking and API-set system prompts.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/
- **2025-11-19 - Launch** - Custom HTTP headers for crawling login-protected websites.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/
- **2026-01-20 - Launch** - Path include/exclude filtering for website and R2 sources, and programmatic instance creation through the REST API.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-simplified-api/
- **2026-02-09 - Change** - Per-file reindexing and single-sitemap selection.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/
- **2026-03-23 - Deprecation** - New OpenAI-compatible `/search` and `/chat/completions` REST endpoints; users of the previous AutoRAG endpoints (`/autorag/rags/`) are advised to migrate.
  Public endpoints, UI snippets, MCP support and up to 5 custom metadata fields per instance shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/
- **2026-04-01 - Launch** - `wrangler ai-search` commands; namespace commands followed on 2026-06-10 and sync job commands on 2026-07-02.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/
- **2026-04-08 - Launch** - CSS content selectors for website sources, and four more Workers AI models.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/
- **2026-04-16 - Breaking** - Instances created from this date come with built-in storage and a vector index, plus a new namespace binding and cross-instance search; existing bindings have a migration guide.
  Hybrid search (vector plus BM25) and relevance boosting shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/
- **2026-06-24 - Change** - Similarity cache responses now use the instance `cache_ttl`, default 48 hours.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/
- **2026-07-08 - Change** - List items can be filtered by exact object `key`; extensionless R2 objects with a supported `Content-Type` can be indexed (2026-09-11); six more Workers AI text models including the DeepSeek V4 models (2026-08-26) and GLM-5.3 Flash (2026-08-30) are supported.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/
- **2026-07-30 - Launch** - Integrations for the Vercel AI SDK (new `ai-search-provider` package), LangChain and the Agents SDK.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-30-ai-search-agent-sdks/
- **2026-08-06 - Launch** - Custom domains, authentication and multi-instance endpoints for public search endpoints (default host `search.ai.cloudflare.com`), plus crawling for sites without complete sitemaps.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/
- **2026-08-25 - Limits** - Custom metadata values share a 10 KiB metadata envelope per vector; the first 64 UTF-8 bytes of each string remain filterable.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/
- **2026-10-01 - GA** - AI Search is generally available, with usage-based billing starting November 1, 2026.
  New instances use hybrid search by default, Workers AI embedding and reranking calls are included in AI Search pricing (and leave the Workers AI bill and AI Gateway logs), OCR is available on every account, and plain-text files and OCR PDFs can be up to 10 MiB while other formats stay at 4 MiB.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/

#### AI Gateway

17 entries tagged AI Gateway in the window.

- **2026-02-19 - Change** - New top-level AI section in the dashboard and simpler AI Gateway onboarding.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/
- **2026-03-02 - Launch** - Using `default` as the gateway ID auto-creates a gateway on the first request.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/
- **2026-03-17 - Change** - The `cf-aig-collect-log-payload: false` header logs metadata without storing request and response bodies.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/
- **2026-04-02 - Launch** - Gateway-level automatic retries (up to 5 attempts, 100 ms to 5 s delay, constant, linear or exponential backoff).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/
- **2026-05-21 - Launch** - AI Gateway moved to the AI REST API on `api.cloudflare.com` with four endpoints, including `POST /ai/run`, `POST /ai/v1/chat/completions` and an OpenAI Responses-compatible endpoint; third-party requests route through the account's default gateway.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/
- **2026-06-05 - Launch** - Spend limits: cost-based budgets by model, provider or metadata, for Unified Billing and BYOK.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/
- **2026-06-12 - Change** - Logs capture the client user agent.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/
- **2026-08-05 - Launch** - Cloudflare Access integration (protect a gateway, identity-aware spend limits and logs) and the User Insights spend and anomaly dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-05-user-insights/
- **2026-08-07 - Pricing** - Unified billing with Workers AI (see Workers AI).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
- **2026-08-19 - Pricing** - GPT-5.6 Sol at 50% off through September 18, 2026 for Unified Billing users only ($2.50 versus $5 per million input tokens, $15 versus $30 per million output tokens).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-19-gpt-5-6-sol-discount/
- **2026-09-01 - Change** - Monthly usage invoices show one total per model and model names were standardised (for example `anthropic/claude-haiku-4.5`).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/
- **2026-09-09 - Change** - Custom costs accept `per_cache_read_token` and `per_cache_write_token`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/
- **2026-09-14 - Change** - **Require provider credentials** (`byok_only: true`) blocks fallback to Unified Billing for BYOK third-party requests.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/
- **2026-09-29 - Change** - User Insights groups conversations by task and flags model overuse.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/
- **2026-09-30 - Beta** - Machine Payments: pay for inference with x402 from a stablecoin wallet (details in the Web3 section).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/
- **2026-10-02 - Beta** - Web Search API launched through AI Gateway (see Web Search API).
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/

#### Browser Run (formerly Browser Rendering)

22 entries tagged Browser Run in the window.

- **2026-03-04 - Limits** - REST API rate limit on Workers Paid rose from 3 to 10 requests per second (180 to 600 per minute).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/
- **2026-03-10 - Beta** - New `/crawl` endpoint in open beta crawls a whole site from one URL and returns HTML, Markdown or JSON; the post was later edited to clarify crawling behaviour with respect to site guidance.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
- **2026-04-10 - Launch** - Chrome DevTools Protocol (CDP) endpoint and MCP client support, usable from any environment.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/
- **2026-04-14 - Launch** - `wrangler browser` commands.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/
- **2026-04-15 - Rename** - Browser Rendering was renamed Browser Run, and Workers Paid concurrency was raised from 30 to 120 concurrent browsers per account and from 30 new browsers per minute to 1 per second.
  Live View, Human in the Loop, Session Recordings and WebMCP support shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-observability/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/
- **2026-05-28 - Launch** - `quickAction()` on the browser binding calls Quick Actions from Workers without API tokens.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/
- **2026-06-11 - Change** - `/snapshot` accepts a `formats` parameter (HTML, screenshot, Markdown, accessibility tree); a standalone `/accessibilityTree` endpoint followed on 2026-07-07.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/
- **2026-07-28 - Launch** - Structured Human in the Loop handoff through Cloudflare-specific CDP commands; a dashboard Playground followed on 2026-07-31.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-human-in-the-loop/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-31-br-dashboard-playground/
- **2026-08-06 - Beta** - Kitesurf, a stateless agent-first browser running on Workers, free while in beta; the post says it uses 3 to 7 times less CPU and memory than Chromium for common agentic tasks (opt in with `browser=kitesurf`).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/
- **2026-08-20 - Limits** - Workers Paid defaults rose from 120 to 200 concurrent browsers, 1 to 3 new browsers per second and 10 to 30 Quick Actions requests per second.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/
- **2026-08-31 - Change** - `/crawl` respects the Content Signals `use` directive through a `contentUse` parameter (`reference` or `full`, default `full`).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/
- **2026-09-14 - Launch** - Guardrails restrict a session's HTTP and HTTPS requests to permitted hostnames.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/
- **2026-09-18 - Change** - Session Recordings gained an Inspect panel with logs, network (HAR download) and DOM.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/
- **2026-09-21 - Launch** - Typed session and DevTools methods on browser bindings, with `outboundByHost` on `acquire()` and `launch()`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/
- **2026-09-25 - Launch** - Crawl jobs publish started, updated and finished events to Queues.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/
- **2026-09-28 - Breaking** - WebMCP works in Kitesurf and Lab sessions through `document.modelContext`; Lab sessions no longer expose `navigator.modelContextTesting`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/
- **2026-09-29 - Change** - A session accepts multiple concurrent CDP connections.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/

#### Vectorize

5 entries tagged Vectorize in the window.

- **2026-01-23 - Limits** - Maximum vectors per index doubled from 5 million to 10 million (1,536 dimensions at 32-bit precision unchanged).
  Source: https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/
- **2026-03-16 - Limits** - `topK` with `returnValues: true` or `returnMetadata: "all"` rose from 20 to 50.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/
- **2026-07-01 - Change** - Write-ahead log throughput improved: median time for a change to become queryable fell from 2 minutes to under 30 seconds, p99 from 5 minutes to under 2 minutes.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/
- **2026-08-04 - Limits** - Maximum vectors per index doubled again, from 10 million to 20 million.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/

#### AI Crawl Control

12 entries tagged AI Crawl Control in the window.

- **2025-10-14 - Change** - Enhanced metrics with drilldowns, filters and CSV export; a Robots.txt compliance tab followed on 2025-10-21 and per-crawler drilldowns on 2025-11-10.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-10-ai-crawl-control-crawler-info/
- **2025-12-10 - Breaking** - Pay Per Crawl (private beta) added a Discovery API, free-page configuration and a `crawler-error` header; payment headers must now be part of the Web Bot Auth `signature-input` (details in the Web3 section).
  Source: https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/
- **2025-12-18 - Change** - A new Overview tab became the default view.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-18-overview-tab/
- **2026-01-13 - Launch** - AI Crawl Control Read Only role.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-13-ai-crawl-control-read-only-role/
- **2026-02-04 - Launch** - Reference docs for the GraphQL API, AI bot detection IDs and Worker templates, including an x402 Payment-Gated Proxy.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-reference-documentation/
- **2026-03-24 - Change** - Custom edits to the underlying WAF rule are preserved when crawler actions change.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/
- **2026-04-17 - Launch** - Redirects for AI Training (301 to canonical URLs for verified AI training crawlers), a Content Format chart, and the Robots.txt tab renamed Directives with an Agent Readiness score link.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-tools-for-agentic-internet/
- **2026-06-16 - Launch** - Pay Per Crawl advanced configuration: disable by URI pattern and dynamic pricing through a `crawler-price` origin header or a Worker.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/

#### Agent Lee, Web Search API and Monetization Gateway

- **2026-04-15 - Launch** - Agent Lee write operations and generative UI (see Agents).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/
- **2026-08-12 - Launch** - Agent Lee can export generated code into a temporary repository to clone; Agent Lee remains in beta.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/
- **2026-09-30 - Beta** - Monetization Gateway entered closed beta (details in the Web3 section).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/
- **2026-10-02 - Beta** - Web Search API launched in beta with three providers (Ceramic.ai, Exa, Linkup), all supporting Zero Data Retention through Cloudflare; it runs through AI Gateway and is billed to AI Gateway credits at each provider's list price with no markup, via REST (`/ai/websearch/`) or `env.AI.websearch()`.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/

### Developer platform: Workers, Pages, Workers for Platforms, Cloudflare CLI

#### Workers

161 entries tagged Workers in the window.
Workers is the most-tagged product in the changelog; many of its tagged entries are primarily about Agents, Durable Objects or Workflows and are listed under those products.

Runtime, limits and compatibility changes:

- **2025-10-10 - Limits** - Worker startup time limit rose from 400 ms to 1 second.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/
- **2025-10-23 - Change** - Preview URLs now default to the `workers.dev` setting when not explicitly configured.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/
- **2026-02-11 - Limits** - The 1,000 subrequests per invocation limit was lifted on paid plans: the default is 10,000 and a new `subrequests` limit can raise it to 10 million; Free stays at 50 external and 1,000 Cloudflare-service subrequests.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/
- **2026-03-24 - Beta** - Dynamic Workers entered open beta for paid users: a Worker loads other Workers at runtime (`load(code)` or `get(id, callback)`).
  Pricing: 1,000 unique Dynamic Workers per month included then $0.002 per Dynamic Worker per day, 10 million requests then $0.30 per million, 30 million CPU ms then $0.02 per million CPU ms; helper libraries `@cloudflare/codemode`, `@cloudflare/worker-bundler` and `@cloudflare/shell` launched alongside.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/
- **2026-03-27 - Change** - RFC 9440 mTLS certificate fields on `request.cf.tlsClientAuth`; L4 transport telemetry fields on `request.cf` followed on 2026-04-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/
- **2026-04-07 - Breaking** - WebSockets automatically reply to Close frames for compatibility dates on or after `2026-04-07` (`web_socket_auto_reply_to_close`).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/
- **2026-04-09 - Limits** - The six simultaneous connections limit now only applies while waiting for response headers.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-09-relaxed-connection-limiting/
- **2026-04-21 - Breaking** - Binary WebSocket frames are delivered as `Blob` by default for compatibility dates on or after `2026-03-17`; opt out with `no_websocket_standard_binary_type`.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/
- **2026-06-11 - Change** - Dynamic Workers usage count in the dashboard and GraphQL (`distinctDynamicWorkerCount`), with data back to June 1, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/
- **2026-06-28 - Change** - `fetch()` supports the `cf.vary` request option.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/
- **2026-08-03 - Launch** - Python and JavaScript Workers can call each other over Workers RPC.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/
- **2026-08-04 - Breaking** - `nodejs_compat` behaviour is on by default for compatibility dates `2026-08-04` or later.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/
- **2026-09-02 - Launch** - Python Workers support WSGI and ASGI frameworks such as Django and Flask; Python 3.14 became the default for compatibility date `2026-09-08` or later.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-08-python-workers-314/
- **2026-09-04 - Limits** - The compressed size limit (3 MB Free, 10 MB Paid) was removed; only the 64 MiB uncompressed bundle limit applies on all plans.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/
- **2026-09-29 - Launch** - Workers Cache supports `invalidate()` to mark cached responses stale for revalidation.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/
- **2026-10-01 - Launch** - Web Crypto supports post-quantum ML-KEM-768, ML-KEM-1024, ML-DSA-44, ML-DSA-65 and ML-DSA-87 (opt-in API).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/

Tooling, Wrangler and deployment:

- **2025-10-03 - Launch** - One-click Cloudflare Access for `workers.dev` and Preview URLs; from 2025-12-04 it creates reusable Access policies.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-03-one-click-access-for-workers/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/
- **2025-10-09 - Launch** - Terraform provider v5.11.0 uploads static assets and manages Workflows (`cloudflare_workflow`).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-09-assets-terraform/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-09-workflows-terraform/
- **2025-10-24 - Beta** - Automatic provisioning of KV, D1 and R2 resources referenced in Wrangler config (open beta); TanStack Start support in the Vite plugin the same day.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-24-automatic-resource-provisioning/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/
- **2025-11-03 - Change** - Smaller Wrangler improvements through the year: ND-JSON command output (`WRANGLER_OUTPUT_FILE_PATH`, `WRANGLER_OUTPUT_FILE_DIRECTORY`), `CLOUDFLARE_ENV` environment selection (2025-11-09), a diff against dashboard settings on `wrangler deploy` (2025-11-21), experimental framework autoconfig (2025-12-16), `wrangler auth token` (2025-12-18), shell tab completions (2026-01-09), `wrangler types --check` (2026-01-12), `.sql` files importable by default (2026-01-20) and `wrangler check startup` bundle and CPU summaries (2026-07-31).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-31-wrangler-startup-profile-summary/
- **2025-11-07 - Beta** - Workers automatic tracing entered open beta.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-07-automatic-tracing/
- **2025-11-21 - Limits** - Workers Builds supports 64 environment variables of up to 5 KB each, previously 5 KB total.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/
- **2025-12-08 - Launch** - Pywrangler for Python packages and Python cold start snapshots; the Vite plugin no longer needs a Wrangler config for static sites and accepts programmatic config.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-optional-config/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/
- **2025-12-18 - Change** - Published build image policies for Workers Builds and Pages: minor updates without notice, 3 months notice for major updates before end of life.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/
- **2026-01-01 - Launch** - Microfrontends template with a router Worker.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-01-microfrontends/
- **2026-01-13 - Change** - `wrangler types` generates types for all environments by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-13-wrangler-types-multi-environment/
- **2026-01-22 - Launch** - Placement hints (`placement.region`) to run near legacy cloud regions.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/
- **2026-02-06 - Change** - Workers Observability dashboard refresh; a structured query language followed on 2026-02-25.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-06-observability-ui-refresh/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-24-observability-query-language/
- **2026-02-16 - Deprecation** - The Quick Editor DevTools inspector was deprecated and replaced with a log viewer.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/
- **2026-02-25 - GA** - Wrangler 4.68.0 automatic configuration: `wrangler deploy` detects the framework and works without a config file, now generally available and the default.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/
- **2026-03-25 - Change** - New `secrets` config property declares required secrets.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/
- **2026-04-01 - Launch** - Deploy Hooks for Workers Builds (10 builds per minute per Worker, 100 per account).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/
- **2026-04-13 - Launch** - Local Explorer (Wrangler 4.82.1+, Vite plugin 1.32.0+) for local resource data.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-13-local-explorer/
- **2026-05-07 - Change** - Automatic tracing propagates across Worker-to-Worker and Durable Object subrequests; custom spans (`tracing.enterSpan()`) on 2026-06-16, `startActiveSpan()` on 2026-07-28 and more OpenTelemetry span APIs on 2026-09-25.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/
- **2026-05-14 - Launch** - Domains tab in the Worker dashboard (buy a domain through Registrar and connect it).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-14-domains-tab/
- **2026-05-18 - Launch** - Share local dev servers through Cloudflare Tunnel from Wrangler and Vite.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/
- **2026-06-03 - Change** - Bulk secrets API endpoint; opt-in OS keychain storage for Wrangler OAuth credentials.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/
- **2026-06-19 - Launch** - Temporary accounts: AI agents can deploy with `wrangler deploy --temporary` (Wrangler 4.102.0+) to a claimable preview account; a Temporary Accounts REST API for platforms followed on 2026-07-14.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-14-temporary-accounts-api/
- **2026-07-02 - Launch** - Wrangler auth profiles bound to directories.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/
- **2026-07-03 - Breaking** - `@cloudflare/workers-types` v5 exposes only the latest runtime types; dated entrypoints such as `/2022-11-30` and `/2023-03-01` were removed.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/
- **2026-07-08 - Launch** - Cloudflare Drop deploys a static site without an account, live for 1 hour unless claimed.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/
- **2026-07-09 - Change** - Wrangler sends npm dependency metadata on deploy for dependency analytics and future supply chain features (opt out with `dependencies_instrumentation`).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/
- **2026-07-27 - Launch** - `createTestHarness()` for integration tests against a production build.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/
- **2026-07-30 - Change** - Workers Builds defaults to Node.js 24.18.0 (22.23.2 also preinstalled).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/
- **2026-08-04 - Launch** - `wrangler login --device` (OAuth device flow) and local tracing for AI agents through the Local Explorer API.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-wrangler-login-device-flow/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/
- **2026-08-19 - Rename** - `@cloudflare/vitest-pool-workers` v1 is published as `@cloudflare/vitest-plugin`; projects must update dependency names, imports and `types` (a codemod is provided).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/
- **2026-08-24 - Change** - Console methods keep exception name, message and stack in logs; JavaScript RPC session spans in traces (2026-09-17); every release and gradual deployment drawn on Workers Metrics charts (2026-09-25).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/
- **2026-09-08 - Breaking** - Miniflare v5 prepares for the `cf` CLI and removes deprecated APIs such as legacy alpha D1 bindings, `wrappedBindings` and built-in module discovery.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/
- **2026-09-15 - Launch** - Per-Worker access with four roles for teammates, agents and CI; dashboard invites followed on 2026-09-21.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/
- **2026-09-22 - Launch** - Worker Previews (isolated per-change environments configured in a `previews` block) and Cursor Origin repositories in Workers Builds.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/

#### Cloudflare CLI

- **2026-09-28 - Beta** - The Cloudflare CLI `cf` entered beta: one CLI for the public API (more than 2,900 commands) and Workers projects, with a typed `cloudflare.config.ts`, `cf migrate` from Wrangler, and `cf cli search` for agents; commands, configuration and Build Output may change before stable.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/

#### Workers for Platforms and Pages

Workers for Platforms: 1 entry, Pages: 2 entries in the window.

- **2025-12-18 - Change** - Workers for Platforms got a dashboard UI for namespaces and scripts.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-18-dashboard-improvements/
- **2026-01-23 - Limits** - Pages paid plans can have 100,000 files per site, up from 20,000, by setting `PAGES_WRANGLER_MAJOR_VERSION=4`; Free stays at 20,000.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/
- **2026-08-11 - Change** - Pages skips superseded queued builds (Workers Builds did the same on 2026-07-24).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-24-skip-superseded-builds/

### Developer platform: Containers, Sandboxes, Workflows, Workers VPC, Artifacts, Flagship, Email Service, media

#### Containers

25 entries tagged Containers in the window.

- **2025-10-01 - Limits** - Larger instance types up to `standard-4` (4 vCPU, 12 GiB memory, 20 GB disk); the table runs `lite` (1/16 vCPU, 256 MiB, 2 GB), `basic`, `standard-1`, `standard-2`, `standard-3` and `standard-4`.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/
- **2025-11-21 - Pricing** - CPU for Containers and Sandboxes is billed on active usage only, at $0.00002 per vCPU-second, instead of provisioned resources; memory and disk pricing unchanged.
  R2 buckets can be mounted as FUSE volumes the same day.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-21-fuse-support-in-containers/
- **2026-01-05 - Launch** - Custom instance types (`vcpu`, `memory_mib`, `disk_mb`) for all users, previously select Enterprise customers only, bounded by `standard-4`.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/
- **2026-02-17 - Launch** - Docker-in-Docker in Containers and Sandboxes.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/
- **2026-02-25 - Limits** - Account-wide concurrent limits rose about 15 times: memory 400 GiB to 6 TiB, vCPU 100 to 1,500, disk 2 TB to 30 TB.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/
- **2026-03-12 - Launch** - SSH into running instances through Wrangler (`wrangler_ssh`, `ssh-ed25519` keys) and `wrangler containers instances`; SSH became enabled by default on 2026-05-12 (still reachable only through `wrangler containers ssh`), and `ProxyCommand` support followed on 2026-05-28.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-ssh-proxy-command/
- **2026-03-24 - Launch** - Public and private Docker Hub images; Google Artifact Registry images followed on 2026-07-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/
- **2026-03-26 - Launch** - Outbound Workers: containers call Workers and bindings over HTTP through `outbound` and `outboundByHost` handlers; on 2026-04-13 they gained credential injection, TLS interception, allow and deny lists and per-instance egress policies.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-13-sandbox-outbound-workers-tls-auth/
- **2026-04-05 - Launch** - Placement constraints: `regions` (`ENAM`, `WNAM`, `EEUR`, `WEUR`) and `jurisdiction` (`eu`, `fedramp`).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/
- **2026-04-13 - GA** - Containers and Sandboxes are generally available, citing higher limits and active-CPU pricing.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/
- **2026-06-18 - Launch** - `this.ctx.container.exec()` starts processes in a running container.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/
- **2026-08-20 - Change** - Miniflare grants local containers the Docker privileges FUSE needs (not rootful Docker on Linux).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/
- **2026-09-10 - Launch** - Containers as the execution environment for Codex through the OpenAI Agents API.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/
- **2026-09-29 - Limits** - Custom instance types no longer have the 2 GB disk per 1 GiB memory ratio; any custom type can use up to the 20 GB maximum.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/
- **2026-09-30 - Beta** - The `durable_object` scheduling policy (a Durable Object picks image and instance size at runtime) and container filesystem snapshots (`snapshotContainer()`) entered public beta.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/

#### Sandboxes (Sandbox SDK)

4 entries tagged Sandboxes in the window.
Several Sandbox SDK features (PTY terminals, backups, file watching, tunnels) were tagged Agents and are listed there.

- **2026-06-09 - Deprecation** - Several Sandbox SDK features were deprecated: the HTTP and WebSocket transports (RPC is the recommended default, and the old transports "will not ship in future Sandbox SDK majors"), `exposePort()` in favour of tunnels, default sessions (the `enableDefaultSession` flag arrived in 0.10.3 and both will be removed), and buffered `readFile`, `writeFile` and `exec` stream equivalents.
  The desktop feature was removed in 0.10.2; a Sandbox SDK 1.0 preview shipped on `@cloudflare/sandbox@next`.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/
- **2026-07-21 - Launch** - Devin Outposts runs Devin sessions in Cloudflare Containers sandboxes; Cursor Cloud Agents self-hosted machines followed on 2026-09-02.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-devin-outposts/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/
- **2026-09-30 - Release** - Sandbox SDK 1.0: your own Durable Object class controls each sandbox through `this.ctx.container`, with a migration guide from 0.x.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-sandbox-sdk-1-0/

#### Workflows

21 entries tagged Workflows in the window.

- **2025-10-31 - Limits** - Workers Paid creation rate rose from 100 instances per 10 seconds to 100 per second and concurrency from 4,500 to 10,000 instances.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/
- **2026-02-04 - Beta** - Dashboard Workflow diagrams generated from code (beta, JavaScript and TypeScript).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/
- **2026-03-03 - Limits** - Steps per instance: 10,000 by default and configurable to 25,000 on Workers Paid, up from 1,024; persisted state stays 100 MB (Free) and 1 GB (Paid).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/
- **2026-03-06 - Change** - Step context exposes the retry attempt; more context (`config`) and `ReadableStream` outputs beyond the 1 MiB step output limit came on 2026-04-21.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/
- **2026-03-23 - Change** - Instance `pause()`, `resume()`, `restart()` and `terminate()` in local dev; all `wrangler workflows` commands accept `--local` from 2026-04-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-local-dev-instance-methods/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/
- **2026-04-15 - Limits** - Concurrency 10,000 to 50,000, creation rate 100 per second per account to 300 per second per account (100 per workflow), queued instances per Workflow 1 million to 2 million.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/
- **2026-05-01 - Launch** - `@cloudflare/dynamic-workflows` runs durable Workflows inside Dynamic Workers.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-01-dynamic-workflows/
- **2026-06-02 - Launch** - Cron schedules on the Workflow binding.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/
- **2026-06-05 - Launch** - Saga-style rollbacks per `step.do()`, executed in reverse order; rollback handlers got step context on 2026-06-23.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/
- **2026-07-07 - Pricing** - Per-step billing added; step and storage billing on Workers Paid starts no earlier than August 10, 2026.
  Workers Free includes 3,000 steps per day and 1 GB-month; Workers Paid includes 500,000 steps per month then $0.80 per 100,000 steps, and 1 GB-month then $0.20 per GB-month.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-workflows-billing-updates/
- **2026-07-09 - Change** - Dynamic retry delay functions (`retries.delay` as a function).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/
- **2026-09-10 - Change** - New Workflows on Workers Paid created from September 10, 2026 retain completed and errored instance state for 7 days by default instead of 30 (maximum still 30); Free keeps 3 days.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/
- **2026-09-15 - Launch** - `WorkflowInstance.subscribe()` and `GET /subscribe` stream instance events; deletion of one or up to 100 instances (Wrangler 4.125.0+) followed on 2026-09-17.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/
- **2026-09-24 - Change** - Workflows can be declared in the `exports` config and called through `ctx.exports` (2026-09-27) without a `workflows` binding.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/

#### Workers VPC

8 entries tagged Workers VPC in the window.

- **2025-11-05 - Beta** - Workers VPC Services (beta) let Workers reach private APIs and databases in any cloud or on premises through Cloudflare Tunnel; the slug carries the date 2025-09-25.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/
- **2026-02-13 - Change** - Cloudflare Origin CA certificates are trusted for HTTPS to private services.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/
- **2026-03-20 - Change** - Per-service Metrics tab.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/
- **2026-04-14 - Beta** - VPC Network bindings and Cloudflare Mesh support entered public beta (bind by `tunnel_id` or `cf1:network`).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/
- **2026-05-21 - Launch** - `cf1:network` reaches Cloudflare WAN destinations (GRE, IPsec, CNI); raw TCP through `connect()` followed on 2026-06-16.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/

#### Artifacts

7 entries tagged Artifacts in the window.

- **2026-04-16 - Beta** - Artifacts, Git-compatible versioned storage for tens of millions of repos, entered private beta (the title says "now in beta").
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/
- **2026-05-18 - Launch** - Wrangler commands, event subscriptions (2026-05-19), dashboard management (2026-06-17), CI on push through the CI SDK (2026-08-04) and EU or US jurisdictions (2026-08-13).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/
- **2026-10-01 - Beta** - Artifacts is in open beta on Workers Paid, with deploys through Workers Builds and a binding for repo management.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/

#### Flagship

4 entries tagged Flagship in the window.

- **2026-05-26 - Beta** - Flagship feature flags entered public beta, evaluated inside Workers without outbound HTTP, backed by KV and Durable Objects, with OpenFeature-compatible SDKs.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/
- **2026-06-10 - Launch** - API reference; `wrangler flagship` (2026-07-16) and app-scoped API tokens (2026-08-26) followed.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/

#### Email Service

7 entries tagged Email Service in the window.

- **2026-04-16 - Beta** - Email Sending entered public beta on Workers Paid (`env.EMAIL.send()` or REST) and joined Email Routing under the new Cloudflare Email Service, with an Agents SDK `onEmail` hook and an Email MCP server.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/
- **2026-06-08 - Beta** - Authenticated SMTP submission (beta) on `smtp.mx.cloudflare.net:465`.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/
- **2026-07-15 - Launch** - Sending events (`message.delivered`, `message.bounced` and others) through Queues event subscriptions; Activity log message preview followed on 2026-07-17.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/
- **2026-09-04 - Change** - Email Routing rules managed from the Wrangler `addresses` field.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/
- **2026-09-25 - Change** - Suppressions can be scoped to `account` (default) or one `sending_domain`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/

#### Realtime, Stream and Cloudflare Images

Realtime: 5 entries, Stream: 4, Cloudflare Images: 6 in the window.

- **2026-02-24 - Change** - Stream live inputs can be disabled to reject RTMPS and SRT.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/
- **2026-03-06 - Change** - RealtimeKit real-time transcription in 10 languages using Deepgram Nova-3 on Workers AI.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/
- **2026-03-18 - Launch** - Media Transformations Workers binding for video resize, crop, frame and audio extraction.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/
- **2026-05-07 - Launch** - Stream bindings for Workers.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/
- **2026-05-27 - Launch** - Images transformation flows, including provider flows to migrate from another service.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/
- **2026-05-28 - Change** - RealtimeKit per-participant audio track recording; the Realtime SFU WebSocket adapter auto-reconnects and buffers media (2026-05-29); Email Sending accepts display names on recipient addresses (2026-05-28).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-realtimekit-track-recording/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/
- **2026-06-08 - GA** - RealtimeKit post-meeting transcription is generally available.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/
- **2026-06-10 - Launch** - `env.IMAGES.hosted` manages hosted images from Workers; new `composite`, `fit` (`aspect-crop`, `scale-up`) and AI `upscale` options on 2026-06-16; text rasterization on 2026-09-02; analytics on 2026-09-23.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/
- **2026-07-01 - Pricing** - The Images binding is billed per unique transformation per calendar month, like URL transformations, and `.info()` calls are no longer billed.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/
- **2026-07-31 - Security** - Stream live input broadcast keys can be rotated without changing the input ID.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/
- **2026-08-13 - Change** - Realtime SFU DataChannels can be unordered or partially reliable (default stays reliable and ordered).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-13-datachannels-reliability-ordering/

#### Privacy Proxy

- **2026-04-15 - Change** - Privacy Proxy metrics are queryable through the GraphQL Analytics API, now the recommended default.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-graphql-analytics-api/

### Storage and data

#### Durable Objects

25 entries tagged Durable Objects in the window.

- **2025-10-16 - Beta** - Data Studio (beta) lets you view and edit each SQLite-backed Durable Object's storage in the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-16-durable-objects-data-studio/
- **2025-10-31 - Limits** - WebSocket messages in Workers, Durable Objects and Browser Rendering can be up to 32 MiB, up from 1 MiB.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/
- **2025-12-12 - Pricing** - Storage billing for SQLite-backed Durable Objects was to be enabled in January 2026, target date January 7, 2026 (no earlier), at the SQLite storage pricing announced in September 2024; Workers Free is not charged, and compute billing has been on since the public beta.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/
- **2025-12-15 - Change** - New "Rules of Durable Objects" best practices guide.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-15-rules-of-durable-objects/
- **2026-02-24 - Breaking** - `deleteAll()` also deletes the alarm for Workers with compatibility date `2026-02-24` or later.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/
- **2026-03-15 - Change** - `ctx.id.name` exposes the name used with `idFromName()` or `getByName()`; `ctx.id.jurisdiction` followed on 2026-03-26.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-26-durable-object-id-jurisdiction/
- **2026-06-19 - Change** - New location hints `apac-ne` and `apac-se`; outbound connections (`connect()` or outbound WebSocket) now keep an object alive for up to 15 minutes each, where previously it was evicted after 70 to 140 seconds without incoming traffic.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/
- **2026-06-25 - Launch** - `evictDurableObject` and `evictAllDurableObjects` test helpers in `cloudflare:test`.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/
- **2026-06-26 - Launch** - New `us` jurisdiction for Durable Objects.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/
- **2026-06-30 - Launch** - Memory Usage chart (P50 to P999) for Workers and Durable Objects against the 128 MB per-isolate limit.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/
- **2026-07-04 - Change** - A declarative `exports` field in the Wrangler config replaces the imperative `migrations` array for Durable Object class lifecycle (states `created`, `deleted`, `renamed`, `transferred`, `expecting-transfer`).
  Source: https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/
- **2026-07-09 - Breaking** - Accounts without an existing key-value backed Durable Object namespace can no longer create one; new namespaces must use SQLite (`new_sqlite_classes`), and a `new_classes` migration fails on affected accounts.
  The post calls this part of a move toward SQLite as the single backend, ahead of a future migration path for existing key-value backed objects.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/
- **2026-07-20 - Change** - Total storage chart per namespace; instance-ID filtering for logs and traces (`$workers.durableObjectId`) followed on 2026-07-24, and a Deployments tab on 2026-08-20.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-durable-objects-deployments-tab/
- **2026-08-25 - Change** - `ctx.abort({ retryAlarm: false })` stops an interrupted alarm from retrying.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/
- **2026-08-28 - Limits** - A Durable Object can have up to ten distinct Dynamic Workers with in-flight requests, up from four.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/
- **2026-09-23 - Limits** - Dashboard name search accepts 128 characters, up from 20.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-24-durable-object-name-search-limit/
- **2026-10-01 - Breaking** - Pending I/O (service binding calls, RPC or `fetch()` to other Durable Objects, `ctx.container.monitor()`, `waitUntil()` promises and timers) now keeps a Durable Object alive without a connected client, by default for compatibility date `2026-10-01` or later (flags `durable_object_io_tasks_prevent_eviction` and `durable_object_io_tasks_do_not_prevent_eviction`).
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/

#### R2

19 entries tagged R2 in the window.
Several R2-tagged posts concern R2 Data Catalog, which is covered under Basin below.

- **2026-02-03 - Beta** - R2 Local Uploads entered open beta: object data is written near the client and replicated asynchronously to the bucket while staying strongly consistent.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/
- **2026-04-30 - Change** - Empty a bucket or delete folders from the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/
- **2026-07-24 - Launch** - Sippy incremental migration now supports Azure Blob Storage and any S3-compatible provider, in addition to Amazon S3 and Google Cloud Storage.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/
- **2026-08-17 - Launch** - New `us` jurisdiction for R2 buckets.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/
- **2026-09-04 - GA** - R2 Data Access Logs are generally available for non-jurisdictional buckets, delivered to Workers Observability on a best-effort basis.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/
- **2026-09-24 - Launch** - Product-level R2 Metrics page with bandwidth usage.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/

#### Basin (formerly Cloudflare Data Platform: Pipelines, R2 Data Catalog, R2 SQL)

27 entries tagged Basin in the window.
Basin Catalog had 12, Basin SQL 11 and Basin Pipelines 8 tagged entries in the window; posts before 2026-10-01 use the old product names.

- **2025-10-06 - Change** - R2 Data Catalog table-level compaction.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/
- **2025-12-12 - Change** - R2 SQL aggregations (`GROUP BY`, `HAVING`) and schema discovery.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-12-aggregation-support-and-more/
- **2025-12-18 - Launch** - R2 Data Catalog automatic snapshot expiration; from 2026-04-22 expiration also deletes unreferenced data files.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/
- **2026-02-09 - Change** - R2 SQL approximate aggregation functions; on 2026-03-23 over 190 new functions, expressions and complex types; on 2026-04-20 JSON functions and `EXPLAIN FORMAT JSON`; on 2026-05-15 JOINs and subqueries; on 2026-06-08 and 2026-06-22 set operations, `SELECT DISTINCT` and window functions.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/
- **2026-02-24 - Change** - Pipelines dropped-event metrics, typed bindings and a Simple setup mode.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/
- **2026-05-04 - Launch** - Pipelines and R2 Data Catalog in Terraform provider v5.19.0.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/
- **2026-05-28 - Pricing** - Pricing announced, with billing not yet enabled and at least 30 days notice promised: Pipelines ingress free, SQL transforms $0.04 per GB, sinks $0.03 per GB (JSON) or $0.06 per GB (Parquet or Iceberg), 1 GB per month free per dimension on Workers Free and 50 GB on Workers Paid; R2 Data Catalog $9.00 per million catalog operations and compaction at $0.005 per GB plus $2.00 per million objects; R2 SQL $2.50 per TB scanned with 10 GB per month included.
  The slugs of these three posts carry the date 2026-05-11.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/
- **2026-05-28 - Change** - R2 Data Catalog got a dedicated dashboard section; delete warnings (2026-07-07), read-only API tokens (2026-07-13), manifest optimization in compaction (2026-07-13), R2 SQL in the dashboard (2026-07-08) and table maintenance visibility (2026-09-16) followed.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-16-table-maintenance-dashboard/
- **2026-06-04 - Deprecation** - The `pipeline` field in the `pipelines` binding config was renamed `stream`; the old field is deprecated but still accepted.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/
- **2026-08-03 - Pricing** - Billing enabled on non-enterprise accounts for Pipelines, R2 Data Catalog and R2 SQL, at the prices announced in May.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/
- **2026-10-01 - GA** - Basin, formerly the Cloudflare Data Platform, is generally available, with Basin Pipelines (formerly Cloudflare Pipelines), Basin Catalog (formerly R2 Data Catalog) and Basin SQL (formerly R2 SQL).
  Existing Pipelines, R2 Data Catalog and R2 SQL resources keep working and "will be deprecated over time".
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/
- **2026-10-01 - Limits** - Per-stream ingest for Basin Pipelines rose from 5 MB/s to 1 GB/s.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/

#### D1

5 entries tagged D1 in the window.

- **2025-11-05 - Launch** - Jurisdictions (`eu`, `fedramp`) can be set at database creation only.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/
- **2026-05-29 - Change** - `migrations_pattern` glob supports nested migration layouts such as Drizzle's.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/
- **2026-09-01 - Limits** - From September 1, 2026, D1 queries on Workers Free fail once the account exceeds the daily row read or row write limit, until midnight UTC; stored data is unaffected.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
- **2026-10-02 - Launch** - New `us` jurisdiction for D1.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/

#### KV

5 entries tagged KV in the window.

- **2026-01-20 - Change** - Redesigned KV dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-kv-dash-ui-homepage/
- **2026-01-30 - Limits** - Minimum `cacheTtl` for `get()` and `getWithMetadata()` lowered from 60 to 30 seconds (default stays 60 seconds).
  Source: https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/
- **2026-07-15 - Deprecation** - Legacy KV API routes under `/accounts/{account_id}/workers/namespaces/*` were deprecated on July 15, 2026 and stop working on October 15, 2026; the replacement is `/accounts/{account_id}/storage/kv/namespaces/*` with identical parameters and payloads.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/
- **2026-10-02 - GA** - KV namespace jurisdictions (`eu`, `us`, `fedramp`) are generally available, settable only at namespace creation.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/

#### Queues

7 entries tagged Queues in the window.

- **2026-01-09 - Launch** - Workers Builds publishes build events to a Queue (event subscriptions).
  Source: https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/
- **2026-02-04 - Pricing** - Queues joined the Workers Free plan: up to 10,000 queues and 10,000 operations per day per account.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-04-queues-free-plan/
- **2026-04-28 - Change** - Realtime backlog metrics (`backlog_count`, `backlog_bytes`, `oldest_message_timestamp_ms`) in the dashboard, REST API and JavaScript API.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/

#### Hyperdrive

9 entries tagged Hyperdrive in the window.

- **2025-12-04 - Change** - `wrangler dev` can connect to remote and TLS databases through `localConnectionString`.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/
- **2026-02-23 - Breaking** - Queries using PostgreSQL `STABLE` functions (for example `NOW()`, `CURRENT_TIMESTAMP`) are no longer cached, in addition to `VOLATILE` functions.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/
- **2026-03-19 - Change** - Custom TLS/SSL certificates for MySQL.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/
- **2026-04-29 - Launch** - Private databases through Workers VPC, now the recommended route.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/
- **2026-05-15 - Change** - Connection pool size metrics (`hyperdrivePoolSizesAdaptiveGroups`).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/
- **2026-06-18 - Launch** - Create PlanetScale Postgres and MySQL databases from Cloudflare, billed on the Cloudflare invoice for pay-as-you-go customers (contract customers from July).
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/
- **2026-08-07 - GA** - MySQL support is generally available at Postgres pricing; dashboard restart of a configuration shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/
- **2026-09-16 - Launch** - Hyperdrive from Python Workers.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-16-hyperdrive-python-workers/

#### Workers Analytics Engine and Secrets Store

3 entries tagged Workers Analytics Engine in the window.
Secrets Store had no entries in the window.

- **2025-10-02 - Change** - New SQL functions (`argMin`, `argMax`, `topK` and others), more aggregate and date functions on 2025-11-12, and `HAVING` and `LIKE` on 2026-01-07.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/

#### Cross-product storage billing

- **2026-06-04 - Change** - Pay-as-you-go customers see billable usage and can create budget alerts from the overview pages of Workers and Pages, D1, R2, KV, Queues, Vectorize, Durable Objects and Containers.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/

### Application security

#### WAF

73 entries tagged WAF in the window.
Of these, 64 are "WAF Release" managed ruleset posts (18 marked Emergency), published roughly weekly; the series in the mirror starts on 2025-01-06 and totals 107 posts.
New detections usually ship in Log or Disabled mode and move to Block in a later release, and a "Scheduled changes" post lists upcoming action changes.

- **2025-10-06 - Security** - Emergency Oracle E-Business Suite RCE rule against active exploitation, followed by more Oracle EBS coverage (CVE-2025-61884, 2025-10-30), Cisco ASA and FTD (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363, 2025-10-07), Adobe Commerce and Magento (CVE-2025-54236, 2025-10-23) and WSUS (CVE-2025-59287, 2025-10-24).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-06-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-23-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-30-emergency-waf-release/
- **2025-12-02 - Security** - Emergency rule for unsafe deserialization RCE in React Server Components, renamed "React - RCE - CVE-2025-55182" on 2025-12-03; CVE-2025-55183 and CVE-2025-55184 rules followed on 2025-12-11.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-02-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-03-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/
- **2025-12-05 - Limits** - Cloudflare first said the WAF would inspect request payloads up to 1 MB on all plans (previously 128 KB on Enterprise, less on other plans) for the React RCE, then reinstated the previous maximum the same day because of a surge in false positives; paid plans can ask Support for 1 MB per zone.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/
- **2026-02-10 - Change** - "Anomaly:Header:User-Agent - Fake Google Bot" moved from Block to Disabled; "Fake Bing or MSN Bot" followed on 2026-07-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/
- **2026-04-07 - Security** - A rule for RCE in an MCP Server (CVE-2026-23744).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-07-waf-release/
- **2026-04-14 - Change** - The Email Address Obfuscation decode script now loads with `defer` (non-render-blocking).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-email-obfuscation-defer/
- **2026-05-07 - Security** - WAF rules and framework adapter mitigations for a batch of React Server Components and Next.js vulnerabilities, enabled by default with Block for all Managed Ruleset users including the Free Managed Ruleset; an emergency Next.js middleware bypass rule (CVE-2026-44575) shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/
- **2026-05-15 - Security** - Emergency nginx rewrite module heap overflow rules (CVE-2026-42945); other notable 2026 emergency releases covered Ivanti EPMM (2026-03-12), cPanel and WHM auth bypass (CVE-2026-41940, 2026-04-30), a web-framework RCE and SQLi (2026-07-17), Next.js (CVE-2026-75604, 2026-08-26), an actively exploited Adobe Commerce and Magento zero-day (2026-09-10), WordPress and JFrog Artifactory (2026-09-25) and Citrix NetScaler (2026-10-01).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-12-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/
- **2026-06-15 - Launch** - Cloudforce One threat intelligence fields (`cf.intel.ip.*`) for IPs seen in threat activity in the past seven days, usable in custom and rate limiting rules.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/
- **2026-08-20 - Change** - Leaked credentials detection scans `Authorization: Basic` headers by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/
- **2026-09-07 - Launch** - Application Profiles (Schema Profiles) add positive security by learning valid request structure, with a closed beta for invited Enterprise customers without API Security; Attack Signature Detection entered Early Access the same day (log-only matches in Security Analytics).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/
- **2026-09-30 - Change** - Scheduled changes for the 2026-10-06 release (beta rule merges and new detections such as F5 BIG-IP).
  Source: https://developers.cloudflare.com/changelog/post/scheduled-waf-release/

#### Rules

15 entries tagged Rules in the window.

- **2025-10-30 - Launch** - TCP fields (whether a request used TCP, client TCP RTT); QUIC RTT and delivery rate fields followed on 2026-04-01.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/
- **2026-01-12 - Change** - `ip.src.metro_code` populated with DMA data.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/
- **2026-01-20 - Launch** - Array and map functions (`split`, `join` and others), `encode_base64()` and `sha256()` on 2026-01-22.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/
- **2026-01-27 - Launch** - Request and response body buffering modes in Configuration Rules.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/
- **2026-03-18 - Launch** - `cf.timings.worker_msec`; RFC 9440 mTLS fields in Transform Rules on 2026-03-25.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/
- **2026-07-16 - Change** - Cache Rules accept bot management fields and `ip.src.asnum`.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/
- **2026-08-13 - Launch** - Cloud Connector supports Oracle Cloud Infrastructure Object Storage.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/
- **2026-09-17 - Launch** - Rulesets validation (dry run) before deployment.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/
- **2026-09-22 - Limits** - `concat()` accepts up to 32 arguments, up from 16.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/
- **2026-10-01 - Launch** - `coalesce()` and dynamic values on both sides of comparisons; `hash_in_range()` became globally available for HTTP products on all plans on 2026-10-02.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/

#### Security Center (Cloudforce One, Brand Protection, URL Scanner, Security Insights)

21 entries tagged Security Center in the window.

- **2025-10-17 - Beta** - Application Security reports in closed beta.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-17-app-sec-reports/
- **2025-10-27 - Change** - Cloudforce One RFI token usage shown; CSV export for RFIs on 2026-05-07.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-27-RFI-Tokens-in-Dash/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-CSV-export-for-RFIs/
- **2025-10-31 - Launch** - Brand Protection: report logo misuse, configurable logo match thresholds from 75% (2026-02-12), dismiss matches (2026-03-06), logo match preview (2026-03-18), unified workspace (2026-04-27) and automated Cease and Desist letters (2026-06-10).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-31-brand-protection-logo-dashboard-report-abuse/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-18-brand-protection-logo-match-preview/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-unified-workspace-brand-protection/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/
- **2025-11-21 - Launch** - Threat insights in Threat Events, then STIX2 output (2026-01-12), "also known as" aliases (2026-02-03), graphs (2026-02-19), saved views (2026-02-23), alerts and digests (2026-04-08), TAXII output (2026-05-06), WAF rules from saved views and Threat Actor Profiles (2026-06-08).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-21-Threat-Events-now-show-events-insights/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-19-threat-events-graphs/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-23-Saved-views-in-threat-events/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/
- **2026-01-14 - Change** - URL Scanner PDF reports; an Agent Readiness tab with six scores (including Commerce) on 2026-05-12.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-14-Download-URL-Scanner-Report-PDF/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/
- **2026-05-29 - Change** - Security Insights scans run by default for all accounts: Free every 7 days, Pro and Business every 3 days, Enterprise daily.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-29-security-insights-default-scans/

#### API Shield

6 entries tagged API Shield in the window.

- **2025-11-12 - GA** - BOLA attack detection on managed endpoints; the post marks the end of the beta period for these scans.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-12-bola-attack-detection/
- **2025-11-25 - Launch** - Zombie endpoint detection (`cf-risk-zombie` after 32 days without traffic).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/
- **2026-03-09 - Beta** - Web and API Vulnerability Scanner (stateful DAST) in open beta for all API Shield customers, through the API.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-09-vulnerability-scanner/
- **2026-03-23 - Change** - `webAssetsOperationId` and `webAssetsLabelsManaged` in GraphQL HTTP datasets.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/
- **2026-08-25 - Launch** - JWT validation supports symmetric `HS256`, `HS384`, `HS512` keys; limits rose to 32 token configurations per zone with 16 keys each on 2026-08-27.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/

#### Bots, Turnstile and Security Overview

Bots: 4, Turnstile: 1, Security Overview: 2 entries in the window.

- **2026-03-17 - Change** - New Security Overview UI; archiving of security action items on 2026-04-20.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-17-new-security-overview-ui/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/
- **2026-07-01 - Change** - AI traffic controls for all plans group AI bots into Search, Agent and Training; from September 15, 2026 new domains default to blocking Training and Agent bots on pages that display ads while Search stays allowed.
  BotBase (a directory of known bots) and Business Insights launched for Enterprise Bot Management the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/
- **2026-07-13 - Launch** - Precursor client-side JavaScript for session-based bot detection rolled out to all customers.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/
- **2026-08-10 - GA** - Turnstile Spin is generally available, with setup from the dashboard, Wrangler or an AI coding agent including server-side siteverify.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/
- **2026-09-16 - Change** - `jsd_api_results_enabled` controls whether JavaScript Detections API results feed bot scoring.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/

### Application performance and network security

#### Cloudflare WAN, Magic Transit, Cloudflare Network Firewall, Network Flow and Network Interconnect

Cloudflare WAN: 31 entries, Magic Transit: 10, Cloudflare Network Firewall: 6, Network Flow: 2, Network Interconnect: 1 in the window.
The year's thread is Unified Routing, which went from beta to GA, with network firewall features ported to it one by one.

- **2025-11-06 - Beta** - Automatic Return Routing (beta) lets IPsec, GRE and CNI on-ramps learn return paths without static routes; it requires the new Unified Routing mode (beta).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/
- **2026-01-15 - Rename** - The Network Services dashboard menu was reorganised by capability: Magic Transit and Magic WAN config moved under **Routes** and **Connectors**, Magic Firewall policies became **Firewall Policies**, and Magic WAN Connectors became **Appliances**.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-15-networking-navigation-update/
- **2026-01-27 - Beta** - Configurable Cloudflare source IPs (beta) for traffic to private networks: IPv4 from `100.64.0.0/12` by default (any `/12` configurable), IPv6 from `2606:4700:cf1:5000::/64`.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/
- **2026-01-30 - Beta** - BGP peering over IPsec and GRE tunnel on-ramps (beta) configurable in the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/
- **2026-02-12 - Change** - Anycast IPs shown in the dashboard when configuring tunnels.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-anycast-ips-on-dashboard/
- **2026-02-17 - Rename** - Brand renames: Magic WAN to Cloudflare WAN, Magic WAN IPsec to Cloudflare IPsec, Magic WAN GRE to Cloudflare GRE, Magic WAN Connector to Cloudflare One Appliance, Magic Firewall to Cloudflare Network Firewall, Magic Network Monitoring to Network Flow, Magic Cloud Networking to Cloudflare One Multi-cloud Networking; no action required and billing unchanged.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/
- **2026-03-24 - Change** - The top-level Interconnects page moved to **Connectors** > **Interconnects**.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-interconnects-navigation-update/
- **2026-04-21 - Change** - Advanced Network Firewall Country rules work in Unified Routing; IP lists, IDS and SIP followed on 2026-07-08, Threat Intel Lists on 2026-08-19 and Managed Rulesets on 2026-09-25.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-19-unified-routing-threat-lists/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-25-unified-routing-managed-rulesets/
- **2026-04-30 - GA** - Post-quantum IPsec (ML-KEM hybrid key agreement, RFC 9370) with third-party devices is generally available, with Cisco and Fortinet validated first.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/
- **2026-05-11 - Change** - Standard NAT-T: IKE can start on UDP 500 and switch to 4500.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-11-nat-t-port-500/
- **2026-05-12 - Change** - New Magic Transit and Cloudflare WAN accounts get a single IPv4 anycast address by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/
- **2026-05-18 - Change** - Network Analytics fully supports Unified Routing.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/
- **2026-06-02 - Change** - Cisco IOS XE integration guide updated with PQC, PBR and IP SLA.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-02-cisco-ios-xe/
- **2026-07-08 - Beta** - IPsec downgrade protection (`IKE_SA_INIT_FULL_TRANSCRIPT_AUTH`) in beta for Cloudflare WAN and Magic Transit.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/
- **2026-09-18 - GA** - Unified Routing is generally available for Cloudflare WAN and Magic Transit, with Automatic Return Routing, BGP and custom client subnets.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/

#### Cache / CDN

12 entries tagged Cache / CDN in the window.

- **2025-11-07 - Change** - Cache keys visible in Cloudflare Trace; audit logs for cache purge events followed on 2025-11-25.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/
- **2026-02-26 - Breaking** - `stale-while-revalidate` is fully asynchronous: the first request after expiry gets stale content with an `UPDATING` status; about 75% of Enterprise zones were migrated with the rest rolling out through the quarter.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/
- **2026-03-24 - Launch** - Cache Response Rules modify `Cache-Control`, cache tags and headers such as `Set-Cookie` before caching; zone versioning support came on 2026-04-27.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-cache-response-rules-zone-versioning/
- **2026-04-17 - Launch** - Smart Tiered Cache cloud region hints for public cloud origins.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-smart-tiered-cache-for-public-cloud/
- **2026-05-04 - Breaking** - Cloudflare's cache now runs on a Pingora-based proxy; bypassed responses are streamed unbuffered by default and `Set-Cookie` is stripped on MISS and EXPIRED for cacheable assets, not only on HIT.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/
- **2026-05-26 - Change** - Uncacheable responses now always report `BYPASS` instead of a mix of `BYPASS` and `MISS`, so MISS rates fall and hit ratios rise.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/
- **2026-07-02 - Launch** - Cache Rules honour `Vary` to store multiple versions of a URL.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-02-vary-for-cache-rules/
- **2026-09-02 - Change** - Origin Range Requests (`origin_range_requests.mode`) configurable through the Rulesets API.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/
- **2026-09-28 - Launch** - Invalidation marks content stale instead of purging it (same rate limits as purge); purges now force a cache miss for Cache Reserve content regardless of purge type.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/

#### DNS and 1.1.1.1

DNS: 8 entries, 1.1.1.1: 2 in the window.

- **2026-03-20 - Change** - DNS Analytics and DNS Firewall Analytics available for Customer Metadata Boundary EU.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-20-dns-analytics-cmb-eu/
- **2026-03-31 - Beta** - Internal DNS entered open beta, bundled with Gateway for Enterprise customers with qualifying subscriptions.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-31-internal-dns-open-beta/
- **2026-04-28 - Launch** - Account-level `enforce_dns_only` kill switch answers proxied records with origin IPs across all zones (Spectrum, Tunnel CNAMEs, R2 custom domains, Web3 gateways and Workers custom domains are excluded).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-enforce-dns-only/
- **2026-05-20 - Change** - Refreshed DNS records UX, default first for Free plans.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-20-new-dns-records-ux/
- **2026-06-10 - Limits** - Enterprise accounts get account-level DNS record quotas instead of per-zone limits: 1,000,000 public and 1,000,000 internal records by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/
- **2026-07-09 - Change** - DNS Firewall dashboard exposes previously API-only settings.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-new-dns-firewall-ux/
- **2026-07-28 - Breaking** - The 1.1.1.1 DoH JSON API `data` field format changes (presentation format instead of RFC 3597 hex, numeric DNSSEC algorithm identifiers, quoted `HINFO` strings); the post calls these breaking changes and recommends wireformat for stability.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/
- **2026-09-14 - Change** - Shadowed record warnings for all zones.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/
- **2026-09-24 - Launch** - 1.1.1.1 supports RFC 8509 root key trust anchor sentinels (for example KSK-2024, key tag 38696).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/

#### Load Balancing

5 entries tagged Load Balancing in the window.

- **2025-10-16 - Launch** - Monitor Groups combine multiple health monitors; the slug carries the date 2025-08-15.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-15-monitor-groups-for-load-balancing/
- **2026-08-03 - Change** - Fallback pool traffic shown separately in analytics; stateful health notifications that auto-resolve (2026-08-07); pool name filtering (2026-08-17).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/
- **2026-08-31 - Launch** - Pool sets (API) combine geographic matching with per-location steering.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/

#### SSL/TLS

4 entries tagged SSL/TLS in the window.

- **2026-04-07 - Change** - mTLS and BYO CA management in the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-07-mtls-byoca-dashboard/
- **2026-06-17 - Launch** - Post-quantum ML-DSA (FIPS 204) certificates accepted for Authenticated Origin Pulls and the Custom Origin Trust Store.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-17-pqc-mldsa-aop-cots/
- **2026-07-21 - Change** - Automatic TLS 1.3 key exchange prediction to origins, on for all zones, preferring post-quantum when supported.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/
- **2026-08-13 - GA** - Certificate Transparency Monitoring is generally available on all plans.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/

#### Speed, Automatic Platform Optimization and Cloudflare Web Analytics

Speed: 3, APO: 1, Web Analytics: 4 entries in the window; Cloudflare for SaaS and Zaraz had none.

- **2026-04-30 - Beta** - Shared dictionaries passthrough (RFC 9842) in open beta on all plans; Web Analytics Navigation Type reporting the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/
- **2026-05-13 - Breaking** - `/cdn-cgi/rum` returns `405 Method Not Allowed` (with `Allow: POST, OPTIONS`) for non-POST requests instead of `404`.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/
- **2026-06-18 - Change** - Cloudflare Fonts forwards `/cf-fonts` requests to origin on invalid paths or errors.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/
- **2026-06-23 - Deprecation** - AMP and Signed Exchanges (SXG) reached end of life: disabled since October 2025, no longer configurable, the Zone API errors and rulesets containing SXG configuration fail to save.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/
- **2026-07-14 - Change** - Account-wide Web Analytics dashboards for accounts with more than 100 sites no longer time out; the slug carries the date 2026-06-10.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/
- **2026-08-21 - Change** - Improved soft navigation measurement for SPAs (complete on 2026-09-04) may change reported pageviews, visits and LCP.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/
- **2026-08-27 - Change** - APO again caches HTML requests without an explicit `Accept: text/html` header after a regression.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/

### Cloudflare One

#### Cloudflare One (platform-wide)

64 entries tagged Cloudflare One in the window.

- **2025-11-17 - Change** - New Cloudflare One navigation: product names removed from many top-level items, pages moved and consolidated, searchable by old and new names.
  Source: https://developers.cloudflare.com/changelog/post/new-cloudflare-one-navigation-and-product-experience/
- **2025-12-16 - Change** - Duplicate action for supported resources; copy resources as JSON or a POST request from 2026-03-02.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-16-new-duplicate-action-for-supported-cloudflare-one-resources/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/
- **2026-04-06 - Beta** - Organizations entered public beta for enterprises: a new top-level container for managing multiple accounts, members, analytics and shared policies.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/
- **2026-04-14 - Rename** - Cloudflare Mesh launched: post-quantum encrypted private networking between servers, laptops and phones over TCP, UDP and ICMP; WARP Connector became Cloudflare Mesh (connectors are now mesh nodes), peer-to-peer connectivity became Mesh connectivity, and the node limit rose from 10 to 50 per account.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/
- **2026-04-15 - Change** - Redesigned Access application and Gateway policy builders; Logs UI refresh on 2026-04-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-new-rule-and-application-builders/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-logs-ui-refresh/
- **2026-06-19 - Change** - One Routes page for Mesh, Tunnel, Cloudflare WAN and Magic Transit routes.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/

#### Access

51 entries tagged Access in the window.

- **2025-10-02 - Beta** - Fine-grained (resource-scoped) permissions for Access applications, IdPs and targets in public beta; Access policies and service tokens followed on 2026-02-13, and from 2026-08-19 resource-scoped members no longer need an extra account read-only role to list resources.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/
- **2025-10-28 - GA** - Private hostname applications support all ports and protocols, no longer only HTTPS on 443 with SNI; generally available on all plans.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/
- **2025-11-14 - Change** - SSH certificate authority can be generated in the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/
- **2026-01-22 - Launch** - Require Access protection for all hostnames in an account (deny by default); new API token permissions (Access: Organizations Revoke, Population Read, Population Write) the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/
- **2026-02-17 - Launch** - "Allow clientless access" for private apps and policies on bookmark applications.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-clientless-access-for-private-apps/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/
- **2026-03-01 - Launch** - Clipboard controls for browser-based RDP (both directions denied by default for new policies); file transfer controls (beta) on 2026-07-07 and bulk PDF print on 2026-07-16.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/
- **2026-03-04 - Launch** - User Risk Score selector in Access policies.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/
- **2026-03-20 - Launch** - Managed OAuth lets CLIs, agents and scripts authenticate to Access apps with an OAuth 2.0 authorization code flow instead of `cloudflared access curl`.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-20-managed-oauth/
- **2026-04-15 - Launch** - Independent MFA at organization, application and policy level without relying on the IdP; AAGUID restrictions and AMR matching on 2026-04-23; YubiKey PIV keys for SSH on 2026-07-01 and FIDO2 keys for SSH on 2026-08-12.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/
- **2026-05-19 - Launch** - Cloudflare as an identity provider with a "restrict to account members" option; it became the default login method for new Zero Trust organizations (instead of one-time PIN) on 2026-06-18.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-19-cloudflare-as-identity-provider/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/
- **2026-06-03 - Launch** - SAML assertion encryption, IdP federation across accounts (2026-06-04) and SAML `ForceAuthn` (2026-09-14).
  Source: https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/
- **2026-07-20 - Change** - Plaintext HTTP private apps on port 80 use the browser login flow instead of the client pop-up.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/
- **2026-08-03 - Change** - "Eager redirect cookie" setting for multi-domain apps (previously automatic for five or fewer hostnames), on by default for new apps.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/
- **2026-08-14 - Launch** - Enable Access on a Worker across all its domains, or make all Workers private by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/
- **2026-08-25 - Security** - Service token rotation grace periods (1 hour to 30 days) and temporary disabling; new secrets created on or after August 26, 2026 use the scannable format `cfast_` plus 40 characters plus an 8-character checksum (existing secrets keep working); inactive token cleanup (30 to 365 days) on 2026-09-22.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/
- **2026-09-15 - Launch** - Access for Infrastructure supports Resource Tagging tags on targets; from 2026-10-01 inline tagging needs only `Zero Trust Write`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/
- **2026-10-02 - Breaking** - Strict service token authentication: failed service-token requests get `401` or `403` instead of a `302` login redirect, only Service Auth policies can authorize them, and no `CF_Authorization` cookie is returned.
  Organizations created on or after October 5, 2026 have it on by default and cannot turn it off; older organizations can opt in (`strict_service_token_auth`).
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/

MCP server portals (Access):

- **2026-02-27 - Beta** - MCP server portal logs exportable with Logpush (Enterprise); portals were in beta.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/
- **2026-03-20 - Launch** - Portal traffic can route through Gateway for HTTP logging and DLP; managed OAuth on by default for new portals.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-20-mcp-portal-gateway-routing/
- **2026-03-26 - Change** - Code Mode on by default on all portals, plus `optimize_context` options; session management (2026-04-02), homepage and sign-out (2026-04-17), tool and prompt aliases (2026-05-28), service tokens (2026-06-26), static OAuth client credentials for servers without Dynamic Client Registration (2026-07-31).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/
- **2026-07-30 - Deprecation** - Four Code Mode policies (`off`, `opt_in`, `default_on`, `enforced`) replace the deprecated `allow_code_mode` boolean; new portals default to Opt-in.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/
- **2026-08-25 - Change** - Portals support the stateless MCP 2026-07-28 specification with fallback to 2025 Streamable HTTP; private MCP servers through Gateway from 2026-09-22.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/
- **2026-09-24 - GA** - MCP server portals are generally available to all customers.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/

#### Gateway

28 entries tagged Gateway in the window.

- **2025-10-10 - Change** - New domain categories and new HTTP application categories (2025-10-28); remapping of existing applications into the new categories to finish by January 30, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-10-new-domain-categories/
  Source: https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/
- **2025-10-20 - Change** - Scheduled DNS policies from the dashboard.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/
- **2025-12-17 - Change** - Shadow IT analytics at domain level.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-17-shadow-it-domain-analytics/
- **2026-02-27 - Beta** - Protocol Detection added IMAP, POP3, SMTP, MySQL, rsync, LDAP and NTP (beta).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/
- **2026-03-04 - Beta** - Gateway Authorization Proxy (Access-authenticated proxy endpoints) and hosted PAC files in open beta for all plans; both became generally available on 2026-04-29.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/
- **2026-03-24 - Change** - OIDC claims selector in Firewall, Resolver and Egress policies.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/
- **2026-04-20 - Launch** - Network session analytics dashboard; Network Session Logs for all on-ramps including PAC proxy endpoints and Browser Isolation egress (2026-04-24), which may increase `zero_trust_network_sessions` volume.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/
- **2026-05-12 - Launch** - Natural-language policy creation and regex authoring (2026-05-27).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudy-regex-assistance/
- **2026-06-05 - Launch** - Workers using a `cf1:network` VPC Network binding egress to the Internet through Gateway, so Zero Trust policies apply to Worker traffic.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/
- **2026-06-30 - Change** - Resource-scoped roles for Gateway policies and lists; Browser Isolation policies follow them from 2026-09-30.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/
- **2026-07-15 - GA** - Internal DNS is generally available (open beta since 2026-03-31).
  Source: https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-31-internal-dns-open-beta/
- **2026-07-17 - Launch** - Header add, overwrite and delete on Allow policies; maximum DNS TTL setting on 2026-07-28.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/
- **2026-08-12 - Beta** - MCP traffic detection (`experimental.is_mcp`, beta) with an AI Security dashboard, and a Traffic Source selector; Traffic Destination selector on 2026-09-23.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/
- **2026-08-13 - Launch** - Package registry security: `pkg.*` selectors to allow or block software package downloads by ecosystem, name and version.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/
- **2026-09-29 - Change** - Network logs identify Mesh nodes, Workers VPC traffic and the Tunnel replica.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/

#### Cloudflare One Client (formerly WARP client)

56 entries tagged Cloudflare One Client in the window.
Release posts come per platform (Windows, macOS, Linux) and per channel (GA or Beta); posts up to early 2026 say "WARP client", and from 2026-04-02 they say "Cloudflare One Client".

- **2025-10-07 - Security** - GA 2025.8.779.0; the Linux package public key must be updated if installed before September 12, 2025 so the repository keeps working after December 4, 2025.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-07-warp-linux-ga/
- **2025-11-11 - Release** - GA 2025.9.558.0 brought Path MTU Discovery (PMTUD) and a local network instability message.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-11-warp-windows-ga/
- **2026-01-13 - Release** - GA 2025.10.186.0 added fleet-wide connectivity control by an external signal and (Windows) an Antivirus posture check.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-13-warp-windows-ga/
- **2026-03-10 - Beta** - Beta 2026.3.566.1 introduced the redesigned client interface, which reached GA in 2026.4.1350.0 on 2026-05-11 (including Linux).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-10-warp-macos-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-11-warp-linux-ga/
- **2026-06-24 - Security** - macOS beta 2026.6.782.1 generates hardware-backed registration tokens in the Secure Enclave.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-24-warp-macos-beta/
- **2026-07-21 - Release** - Hotfix 2026.6.880.0 fixed a regression that greatly increased DNS-over-TCP queries; 2026.7.1376.0 and 2026.7.1377.0 (2026-08-28) fixed failing DNS queries across platforms.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-warp-windows-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-28-warp-windows-ga/
- **2026-09-30 - Release** - Latest beta in the mirror: Windows 2026.8.2033.1.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/

#### Data Loss Prevention

14 entries tagged Data Loss Prevention in the window.

- **2025-10-01 - Change** - File type controls for executables and disk images.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/
- **2026-03-25 - Launch** - Predefined "Unsanitized HAR" profile; streaming ZIP scanning removes per-file size limits (2026-03-26).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/
- **2026-04-14 - Deprecation** - Account-level DLP settings (OCR, AI context analysis, payload masking); profile-level advanced settings will be deprecated in a future release; the slug carries the date 2025-04-14.
  Configurable payload log masking and Cloudflare API token detections (`cfk_`, `cfut_`, `cfat_`) shipped the same day.
  Source: https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-configurable-payload-log-masking/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/
- **2026-04-28 - Launch** - Detection entries managed outside profiles, a PII Record profile (three entries in close proximity), Data Classification (2026-04-30) and new predefined entries including crypto wallets such as `Bitcoin Wallet` (2026-04-30).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-detection-entries-outside-profiles/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-standalone-predefined-detection-entries/
- **2026-06-11 - Launch** - Custom natural-language topics for AI prompt protection.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/
- **2026-07-10 - Change** - Source code detection only evaluates whole source files, reducing false positives.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-10-source-code-detection-improvements/
- **2026-08-21 - Launch** - DLP test scan without Gateway traffic; Passive Detection (generally available) on 2026-09-14.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/

#### Email security

11 entries tagged Email security in the window.

- **2025-10-17 - Launch** - On-demand security reports.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-16-on-demand-security-report/
- **2025-11-18 - Rename** - "Final Disposition" column renamed "Status" (Submitted, Accepted, Rejected); "Reclassify" renamed "Submit" on 2025-12-03.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-18-temporary-adjustment-to-final-disposition-column/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-03-submission-terminology-update/
- **2026-03-15 - Limits** - Investigations paging no longer capped at 1,000 records.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/
- **2026-04-06 - Security** - DANE TLSA records for regional MX hostnames; post-quantum X25519MLKEM768 on SMTP connections on 2026-08-17.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/
- **2026-08-12 - Launch** - Blocked content rules (plaintext or regex on subject and body).
  Source: https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/

#### CASB, Browser Isolation, DEX, Risk Score

CASB: 7, Browser Isolation: 4, DEX: 7, Risk Score: 2 entries in the window.

- **2025-10-28 - Change** - CASB Read and CASB roles; weekly digest (2025-11-14), Cloudy summaries (2026-02-20), webhooks (2026-04-09), Claude Compliance API integration (2026-05-19), remediation policies for Microsoft 365 and Google Workspace (2026-08-21), Zoom integration (2026-09-09).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-14-casb-digest/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-20-cloudy-in-casb/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/
- **2025-11-12 - Launch** - DEX Logpush datasets; EU Customer Metadata Boundary (2026-02-19); outage notifications and remote speed tests (2026-04-28); tests to authenticated resources (2026-04-29); Wi-Fi and network analytics (2026-07-09).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-dex-internet-outage-notification/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-dex-speed-test/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/
- **2026-01-15 - Launch** - CrowdStrike device score behaviours in User Risk Scoring; high-risk browsing signals on 2026-04-08.
  Source: https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/
- **2026-04-10 - Launch** - Browser Isolation Canvas Remoting (the post cites 90% less bandwidth for Office apps); authorization proxy endpoint support on 2026-07-07.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/

#### Cloudflare Mesh, Cloudflare One Appliance, Tunnel for SASE and Data Localization Suite

Cloudflare Mesh: 11, Cloudflare One Appliance: 12, Tunnel for SASE: 11, Data Localization Suite: 1 entries; Multi-Cloud Networking had none in the window.

- **2025-11-06 - Change** - Magic WAN Connector (now Cloudflare One Appliance) can designate a WAN port for breakout; NetFlow for breakout traffic on 2025-12-31.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/
- **2026-02-11 - Security** - Appliance 2026.2.0 uses hybrid ML-KEM post-quantum TLS 1.3 to the edge and injects the secret into IPsec ESP.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/
- **2026-04-07 - Beta** - LACP link aggregation (up to six LAN ports, beta); custom DHCP options, source-based breakout and Virtual Appliance self-serve via API and Terraform (2026-05-07); dashboard self-serve registration (2026-07-06); restart, reboot and shutdown (2026-07-17); hypervisor downloads for VMware ESXi, Proxmox and libvirt/KVM (2026-08-24); custom applications and DHCP options in the dashboard (2026-09-02).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-dhcp-options/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-24-virtual-appliance-self-serve-download/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/
- **2026-05-06 - Change** - Mesh IPv6 CIDR routes; resource-scoped permissions for Tunnel and Mesh (2026-05-21); HA replica management (2026-05-28); hostname routes (2026-07-02); `cloudflare/mesh` container image (2026-08-07); guided participant onboarding (2026-09-23).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/
- **2026-06-23 - Launch** - Regional Services supports Regionalized IP Bindings for BYOIP prefixes.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/

### Core platform, analytics and consumer services

#### Cloudflare Fundamentals (account, API, dashboard, errors)

53 entries tagged Cloudflare Fundamentals in the window.

Account security and identity:

- **2025-10-07 - Security** - Backup code reminders; email two-factor authentication on 2025-10-30; users without 2FA are prompted to enrol in email 2FA at login from 2026-01-23 (enrolment stays optional).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-30-email-2FA/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-23-New-2FA-Experience/
- **2025-10-14 - Change** - SSO configuration in the dashboard (SSO was announced as free during Birthday Week); SCIM for Authentik (GA) on 2026-03-18 and SCIM audit logging the same day; SCIM `PUT` group sync on 2026-08-21.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-14-sso-self-service-ux/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/
- **2026-03-19 - Deprecation** - Service Key authentication for the Cloudflare API is deprecated and stops working on September 30, 2026; API Tokens replace it.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/
- **2026-04-10 - Security** - API tokens use identifiable patterns detectable by secret scanning tools.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-10-secret-scanning-support/
- **2026-04-14 - Change** - OAuth consent lets users pick specific accounts and revoke apps; self-managed public OAuth clients for third-party developers (2026-06-03); publisher verification shields (2026-08-05); optional OAuth scopes GA (2026-08-20).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/
- **2026-07-21 - Deprecation** - The Account Roles API is deprecated in favour of the Permission Groups API, with no end-of-life date yet; the response schema differs.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/
- **2026-08-21 - Change** - API `403` responses include a `documentation_url`; saved login profiles (up to five per device) the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-21-one-click-login/
- **2026-10-01 - Change** - Members with the API Token Provisioning role can create Account API tokens, no longer only Super Administrators.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/

Platform limits and behaviour:

- **2025-10-16 - Limits** - Maximum request and response header size rose to 128 KB, from 32 KB total with 16 KB per header.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/
- **2026-01-19 - Change** - HTTP/3 request cancellations are terminated faster, so more `499` status codes may appear.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/
- **2026-09-04 - Limits** - Enterprise customers can self-serve a CDN maximum upload size up to 5 GB (default stays 500 MB).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/

Agent-facing responses:

- **2025-10-01 - Change** - Cloudflare docs can be retrieved as Markdown.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/
- **2026-02-12 - Launch** - Markdown for Agents converts HTML to Markdown at the edge for enabled zones when clients send `Accept: text/markdown`; on 2026-02-16 the origin response limit rose from 1 MB to 2 MB; from 2026-07-13 the origin Content Signals policy is authoritative and the default added is `Content-Signal: ai-train=yes, search=yes, ai-input=yes`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/
- **2026-02-26 - Breaking** - Cloudflare 1xxx errors return Markdown when requested; on 2026-03-11 JSON with RFC 9457 Problem Details was added and the frontmatter field `http_status` was renamed `status` (also `what_happened` renamed); `Retry-After` headers for seven retryable codes on 2026-03-12; 5xx errors (500, 502, 504, 520 to 526) got the same structured responses on 2026-04-27.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/

Accounts, billing and dashboard:

- **2026-01-27 - Change** - Dashboard timezone preference; keyboard shortcuts on 2026-05-04; Network Overview page on 2026-04-21.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-27-timezone-preferences/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-04-keyboard-shortcuts/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-network-overview-page/
- **2026-04-06 - Beta** - Organizations public beta (see Cloudflare One); Distributor, MSSP and Agency partners can add Organization members themselves from 2026-07-17 (those Organization types are still in beta).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-17-distributor-mssp-self-serve-members/
- **2026-04-21 - Launch** - Billable Usage dashboard and Budget alerts for pay-as-you-go; from 2026-07-20 budget alerts are on by default with a $10 account-level threshold (excluding recurring subscription fees), rolled out in cohorts.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/
- **2026-04-27 - Beta** - Resource Tagging entered public beta (key-value tags on zones, Workers, D1, R2, KV, Tunnels, Access apps and more).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-27-resource-tagging-public-beta/
- **2026-04-29 - Change** - Instant Bank Payments via Link for US self-serve accounts; modernised Billing Profile with Apple Pay, Google Pay, Link and PayPal (2026-05-21).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-21-modernised-billing-profile/
- **2026-08-04 - Change** - Create standalone Free accounts from the dashboard; on 2026-09-17 also via API (user-owned tokens or OAuth) and inside Enterprise Organizations; the slug of the latter carries 2026-09-15.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-free-dashboard-button/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-15-free-account-creation/

#### Terraform and SDKs

Terraform: 8, SDK: 6, Go SDK: 2 entries in the window.

- **2025-11-20 - Breaking** - Terraform provider v5.13.0 to v5.17.0 shipped on a 2 to 3 week cadence after many v5 issue reports; v5.13.0 has breaking changes for `cloudflare_api_token` and `cloudflare_account_token`.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-19-terraform-v5.15.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/
- **2026-04-24 - Release** - Terraform v5.19.0 added 14 resources (AI Gateway, Pipelines, R2 Data Catalog, user groups and others) and state upgraders for 26 resources; the `tf-migrate` CLI automates v4 to v5 migration (for example `cloudflare_record` to `cloudflare_dns_record`); v5.20.0 on 2026-06-12 added 24 resources and moved to cloudflare-go v7.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-24-tf-migrate-tool-released/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/
- **2026-04-30 - Breaking** - Major SDK releases: Python SDK v5.0.0 (drops Python 3.8, optional aiohttp), TypeScript SDK v6.0.0 (17 endpoints removed, `Retry-After` honoured above 60 seconds) and Go SDK v7.0.0 (breaking changes in `ai_search`, `email_security`, `workers`); betas were announced on 2026-01-20 (TypeScript) and 2026-02-13 (Python), and Go v6.10.0 on 2026-04-23 also had breaking changes.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-23-go-sdk-v6.10.0/

#### Logs, Logpush and Log Explorer

Logs: 25, Logpush: 5, Log Explorer: 11, Logpush Connectors: 1 entries in the window.

- **2025-10-27 - Launch** - Microsoft Sentinel connector built on the Codeless Connector Framework replaces the Azure Functions connector; the Azure Functions connector must be migrated by 2026-09-14 because Microsoft ends the HTTP Data Collector API (2026-08-26 post).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-27-Sentinel-connector/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/
- **2025-11-05 - Breaking** - Managing Logpush jobs for Zero Trust datasets (Access, Gateway, DEX) now requires two permissions.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/
- **2025-11-11 - Launch** - Logpush health dashboards; SentinelOne (2025-12-11), BigQuery (2026-04-02, dashboard 2026-04-14) and Pipelines (2026-04-20) destinations.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-11-health-dashboards/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-11-sentinelone-destination/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/
- **2025-11-13 - Launch** - Log Explorer added 14 datasets, query cancellation and result distribution; tabs and pivots (2026-02-09), ingest field selection (2026-03-11), dataset deletion (2026-08-26).
  Source: https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-04-query-cancellation/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-tabs-and-pivots/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/
- **2026-03-09 - Change** - New datasets through the year: MCP Portal Logs (2026-03-09), Email Security Post-Delivery Events (2026-05-13), Turnstile Events (2026-06-01), WebSocket Analytics (2026-06-24 and 2026-07-07), account-scoped firewall events (2026-06-30), Account Abuse Protection Events and Magic BGP Logs (2026-08-20), and `ClientTLSKeyExchangeGroup` for per-zone post-quantum visibility (2026-08-20).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-13-log-fields-updated/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-01-log-fields-updated/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/
- **2026-03-25 - Change** - `rfc3339ms` and `rfc3339ns` timestamp formats; subrequest merging (up to 50 per parent) on 2026-04-21; DDoS traffic filtering on 2026-09-18.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/
- **2026-09-30 - Pricing** - Logpush is available on Free, Pro, Business and Enterprise with usage-based pricing: internal exports 25 GB per month then $0.03 per GB, external exports 25 GB then $0.10 per GB, transformations 1 GB then $0.04 per GB; existing Enterprise contracts keep their pricing through renewal; Logpush Transformers (SQL before delivery) are generally available.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/

#### Analytics and Audit Logs

Analytics: 7, Audit Logs: 4 entries in the window.

- **2025-10-01 - Launch** - Confidence intervals for `sum` and `count` on adaptive GraphQL datasets.
  Source: https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/
- **2025-12-18 - Change** - Zone Overview cached-request classification fixed; about 15% of requests previously classified as cached were affected.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/
- **2026-02-18 - Change** - `cfWorker` metric in the `Server-Timing` header (on by default with RUM).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/
- **2026-03-10 - GA** - Audit Logs v2 is generally available, covering about 95% of products (up from about 75% in v1); beta logs back to about February 8, 2026 expire about April 9, 2026; organization-level logs via API (2026-04-23) and dashboard (2026-06-24); Resource History (2026-07-27).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/
- **2026-04-22 - GA** - Custom Dashboards available to all customers on 100+ GraphQL datasets (Log Explorer customers can create up to 100 dashboards, others 25); Workers Observability logs and traces datasets added on 2026-10-02.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/
- **2026-08-14 - Change** - WebSocket data transfer and duration now reported for the full connection, not only the `101` handshake.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/
- **2026-10-02 - Limits** - Every plan gets at least 30 days of adaptive analytics: Free and Pro retain at least 31 days and can query 30 days per request, previously 24 hours to 8 days.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/

#### Cloudflare Tunnel

16 entries tagged Cloudflare Tunnel in the window.

- **2025-11-11 - Deprecation** - `cloudflared proxy-dns` is removed from new releases starting February 2, 2026, because of a vulnerability in an underlying DNS library.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-11-cloudflared-proxy-dns/
- **2026-02-20 - Change** - Tunnel management in the main dashboard (Networking > Tunnels); `wrangler tunnel` commands (2026-03-19); multi-replica log streaming (2026-03-20) and live logs in the main dashboard (2026-08-10); origin settings in the dashboard (2026-08-18).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/
- **2026-05-27 - Change** - `cloudflared` 2026.5.2 runs connectivity pre-checks at startup.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/
- **2026-07-09 - Breaking** - On October 5, 2026 the CIDR-encoded route endpoints (`/teamnet/routes/network/{ip_network_encoded}`) are removed in favour of `route_id` endpoints, and tunnel list and get responses drop the `connections` field.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
- **2026-08-11 - GA** - Hostname routing is generally available; the default range for initial resolved (token) IPs moves from CGNAT to `172.64.128.0/20` and `2606:4700:0cf1:4000::/64` because Chrome 142 Local Network Access blocks CGNAT addresses.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/
- **2026-09-18 - Deprecation** - Starting in 2027, no new `cloudflared` releases for 32-bit Windows and Intel-based macOS.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/
- **2026-10-02 - Security** - Quick Tunnels can require email one-time PIN authentication with `--allowed-mail`.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/

#### Radar

28 entries tagged Radar in the window.
Radar shipped a steady stream of datasets and tools; the most notable:

- **2025-10-06 - Launch** - Browser post-quantum detection; CT log insights (2025-10-09); TLD insights (2025-10-27); Cloud Observatory origins API (2025-11-24).
  Source: https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/
  Source: https://developers.cloudflare.com/changelog/post/2025-11-24-radar-cloud-observability/
- **2026-02-12 - Launch** - Content type dimension for AI bots; ASPA deployment insights (2026-02-25); origin post-quantum tracking and Key Transparency dashboard (2026-02-27); Network Quality Test (2026-03-03); region filtering (2026-03-06).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-27-radar-pq-key-transparency/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-03-radar-network-quality-test/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/
- **2026-04-17 - Launch** - AI Insights: adoption of AI agent standards (Agent Readiness API); routing section expansion (2026-04-01), MRT Explorer (2026-05-19), ASPA path validation (2026-08-24).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-24-radar-aspa-validation/
- **2026-06-18 - Change** - Workers AI popularity on Radar is now measured by number of inferences instead of unique accounts, including historical data.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/
- **2026-08-07 - Beta** - Radar Researcher, an AI assistant for Radar data (beta), plus WebMCP support; richer sources on 2026-08-26.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-radar-researcher-and-webmcp/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-radar-researcher-improvements/

#### Support, Registrar, Billing and other core products

- **2026-04-07 - Change** - Redesigned Support Portal; direct Support button (2026-04-28); rebuilt Cloudflare Status page with its own notification system and unchanged Status API (2026-08-11).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-direct-support-navigation/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/
- **Registrar** - The Registrar API beta post (search, availability and pricing, registration, usable from Cloudflare MCP) has a publish date of 2025-04-15 but a slug dated 2026-04-15, so it may belong to this window; no other Registrar entry falls in the window.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/

## Month-by-month timeline of 2026

The biggest announcements of each month, chosen for breadth of impact (new products, GA and beta transitions, pricing, limits and breaking changes); details and sources are in the digest above.

### January 2026 (48 entries)

- 2026-01-05: Custom Container instance types for all users. https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/
- 2026-01-20: AI Search instances can be created through the REST API; TypeScript SDK v6.0.0-beta.1 with many breaking changes. https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-simplified-api/ https://developers.cloudflare.com/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/
- 2026-01-22: Account-wide "require Access protection" (deny by default) for hostnames; Workers placement hints. https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/ https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/
- 2026-01-23: Vectorize indexes up to 10 million vectors; Pages paid plans up to 100,000 files. https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/ https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/

### February 2026 (64 entries)

- 2026-02-03: R2 Local Uploads open beta. https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/
- 2026-02-04: Queues on the Workers Free plan (10,000 operations per day). https://developers.cloudflare.com/changelog/post/2026-02-04-queues-free-plan/
- 2026-02-09: Agents SDK v0.4.0 migrates to x402 v2. https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/
- 2026-02-11: Workers subrequest limit lifted to 10,000 by default and up to 10 million on paid plans. https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/
- 2026-02-12: Markdown for Agents at the edge. https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/
- 2026-02-17: Magic WAN, Magic Firewall, Magic Network Monitoring and related products renamed (Cloudflare WAN, Cloudflare Network Firewall, Network Flow, Cloudflare One Appliance). https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/
- 2026-02-25: Containers concurrency limits up about 15 times; `wrangler deploy` without config (autoconfig) GA. https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/ https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/

### March 2026 (76 entries)

- 2026-03-03: Workflows up to 25,000 steps per instance. https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/
- 2026-03-10: Browser Rendering `/crawl` endpoint open beta; Audit Logs v2 GA. https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/ https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/
- 2026-03-19: Service Key API authentication deprecated, to stop working on 2026-09-30; Kimi K2.5, the first frontier-scale open model on Workers AI. https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/ https://developers.cloudflare.com/changelog/post/2026-03-19-kimi-k2-5-workers-ai/
- 2026-03-20: Managed OAuth for Cloudflare Access (non-browser clients and agents). https://developers.cloudflare.com/changelog/post/2026-03-20-managed-oauth/
- 2026-03-24: Dynamic Workers open beta with published pricing; Cache Response Rules. https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/ https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/
- 2026-03-31: Internal DNS open beta. https://developers.cloudflare.com/changelog/post/2026-03-31-internal-dns-open-beta/

### April 2026 (115 entries)

- 2026-04-06: Organizations public beta for enterprises. https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/
- 2026-04-13: Containers and Sandboxes GA. https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/
- 2026-04-14: Cloudflare Mesh launched (WARP Connector renamed); VPC Networks public beta. https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/ https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/
- 2026-04-15: Browser Rendering renamed Browser Run with 4 times the concurrency; Workflows limits raised to 50,000 concurrent instances; Access independent MFA; Agent Lee write operations. https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/ https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/ https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/ https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/
- 2026-04-16: Email Sending public beta under Cloudflare Email Service; Artifacts private beta; AI Search built-in storage and hybrid search. https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/ https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/ https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/
- 2026-04-21: Billable Usage dashboard and Budget alerts. https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/
- 2026-04-27: Resource Tagging public beta. https://developers.cloudflare.com/changelog/post/2026-04-27-resource-tagging-public-beta/
- 2026-04-29: Gateway Authorization Proxy and hosted PAC files GA. https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/
- 2026-04-30: Python SDK v5.0.0, TypeScript SDK v6.0.0 and Go SDK v7.0.0, all with breaking changes; post-quantum IPsec with third-party devices GA. https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/ https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/ https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/ https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/

### May 2026 (77 entries)

- 2026-05-04: Cloudflare's cache now runs on Pingora, changing bypass buffering and `Set-Cookie` stripping. https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/
- 2026-05-07: WAF and framework adapter mitigations for React and Next.js vulnerabilities, on by default for all Managed Ruleset users. https://developers.cloudflare.com/changelog/post/2026-05-06-react-nextjs-vulnerabilities/
- 2026-05-08: 18 Workers AI models deprecated on 2026-05-30, Kimi K2.5 aliased to the pricier K2.6. https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/
- 2026-05-21: AI Gateway moves to the unified AI REST API on `api.cloudflare.com`. https://developers.cloudflare.com/changelog/post/2026-05-21-rest-api/
- 2026-05-26: Flagship feature flags public beta. https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/
- 2026-05-28: Pricing announced for Pipelines, R2 Data Catalog and R2 SQL (billing not yet on). https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/ https://developers.cloudflare.com/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/ https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/

### June 2026 (75 entries)

- 2026-06-05: AI Gateway spend limits; Workflows saga rollbacks; Workers egress through Gateway. https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/ https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/ https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/
- 2026-06-09: Sandbox SDK feature deprecations and the Sandbox SDK 1.0 preview. https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/
- 2026-06-18: Cloudflare identity provider becomes the default for new Zero Trust organizations; PlanetScale databases billed through Cloudflare. https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/ https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/
- 2026-06-19: Temporary accounts let AI agents deploy Workers without signing up. https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/
- 2026-06-23: AMP and Signed Exchanges end of life. https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/
- 2026-06-26: Durable Objects `us` jurisdiction. https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/

### July 2026 (92 entries)

- 2026-07-01: AI traffic controls by behaviour (Search, Agent, Training) for all plans, with new defaults for new domains from 2026-09-15; Images binding billed per unique transformation. https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/ https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/
- 2026-07-07: Workflows per-step billing, starting no earlier than 2026-08-10. https://developers.cloudflare.com/changelog/post/2026-07-07-workflows-billing-updates/
- 2026-07-09: New Durable Object namespaces must use SQLite; Tunnel CIDR route endpoints and `connections` field to be removed on 2026-10-05. https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/ https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
- 2026-07-15: Legacy KV namespace API routes deprecated, ending 2026-10-15; Internal DNS GA. https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/ https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/
- 2026-07-27: Agents SDK v0.20.0 supports MCP 2026-07-28 and deprecates `McpAgent`. https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/
- 2026-07-28: Kimi K2.6, Kimi K2.7 Code and GLM-5.2 require the Workers Paid plan; Cloudflare MCP servers move to stateless MCP 2026-07-28. https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/ https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/

### August 2026 (104 entries)

- 2026-08-03: Billing enabled for Pipelines, R2 Data Catalog and R2 SQL. https://developers.cloudflare.com/changelog/post/2026-08-03-pipelines-billing-enabled/ https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/ https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/
- 2026-08-04: Node.js compatibility on by default from compatibility date `2026-08-04`; Vectorize up to 20 million vectors. https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/ https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/
- 2026-08-06: Kitesurf, an agent-first browser on Workers, free in beta. https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/
- 2026-08-07: Workers AI and AI Gateway unify model access and billing (prepaid credits pay for Workers AI); Hyperdrive MySQL GA. https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/ https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/
- 2026-08-10: Turnstile Spin GA. https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/
- 2026-08-11: Hostname routing GA with a new public range for initial resolved IPs. https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/
- 2026-08-14: DeepSeek V4 Flash and Pro, the first Workers AI models with a 1,048,576 token context. https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/
- 2026-08-20: Browser Run defaults raised to 200 concurrent browsers. https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/

### September 2026 (98 entries)

- 2026-09-01: D1 enforces Workers Free daily row limits. https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
- 2026-09-04: Workers size limit becomes 64 MiB uncompressed on all plans; R2 Data Access Logs GA. https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/ https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/
- 2026-09-07: WAF Application Profiles (positive security) and Attack Signature Detection early access. https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/ https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/
- 2026-09-18: Unified Routing GA for Cloudflare WAN and Magic Transit. https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/
- 2026-09-22: Worker Previews for every pull request. https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/
- 2026-09-24: MCP server portals GA. https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/
- 2026-09-28: Cloudflare CLI `cf` beta; cache invalidation instead of purge. https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/ https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/
- 2026-09-30: Monetization Gateway closed beta and AI Gateway Machine Payments beta, both on x402; Logpush on all plans with usage-based pricing; Sandbox SDK 1.0. https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/ https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/ https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/ https://developers.cloudflare.com/changelog/post/2026-09-30-sandbox-sdk-1-0/

### October 2026 (22 entries, to 2026-10-02)

- 2026-10-01: AI Search GA (billing from 2026-11-01); Basin GA (Pipelines, R2 Data Catalog and R2 SQL renamed); Artifacts open beta; Clef decision models; Workers OAuth Provider v1; Durable Objects stay alive on pending I/O. https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/ https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/ https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/ https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/ https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/ https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/
- 2026-10-02: Web Search API beta; KV jurisdictions GA; D1 `us` jurisdiction; at least 30 days of analytics on every plan; strict service token authentication for Access. https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/ https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/ https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/ https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/ https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/

## Deprecations and breaking changes (whole mirror)

Every deprecation, removal, end of life, forced migration, breaking change and behaviour-changing default found in the 1,307 mirrored posts (2024-02-26 to 2026-10-02), in publish-date order.
The mirror has no deprecation-type posts before 2025; the 2024 posts are product launches and the move of each product's old changelog into this one.
Cutoff dates still in the future on 2026-10-05 are marked "upcoming".

### Upcoming cutoffs (as of 2026-10-05)

| Effective date | What happens | Source |
| --- | --- | --- |
| 2026-10-05 | Tunnel and Zero Trust Networks CIDR-encoded route endpoints removed; tunnel list and get responses drop `connections` | https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/ |
| 2026-10-05 | New Zero Trust organizations get strict service token authentication on, with no way to turn it off | https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/ |
| 2026-10-15 | Legacy KV routes `/accounts/{account_id}/workers/namespaces/*` stop working | https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/ |
| 2026-11-01 | AI Search usage-based billing begins | https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/ |
| 2027 (no day given) | No new `cloudflared` builds for 32-bit Windows and Intel-based macOS | https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/ |
| Not announced | `McpAgent` frozen (no removal version); `createMcpHandler(v1Server, options)` removed in the next Agents SDK major; Account Roles API end of life; Audit Logs v1 retirement; Sandbox SDK HTTP and WebSocket transports and default sessions; DLP profile-level advanced settings; Pipelines, R2 Data Catalog and R2 SQL resources "deprecated over time"; Terraform `cmd/migrate` | see entries below |

### 2025

- **2025-02-02 - Breaking** - Five unused fields removed from the DNS record `meta` object (`auto_added`, `managed_by_apps` and `apps_install_id`, `managed_by_argo_tunnel` and `argo_tunnel_id`), rolling out over up to four weeks.
  Source: https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/
- **2025-02-03 - Breaking** - Terraform Provider v5 GA is a ground-up rewrite with breaking changes for some resource types.
  Source: https://developers.cloudflare.com/changelog/post/2025-02-03-terraform-v5-provider/
- **2025-02-28 - Breaking** - Wrangler v4.0.0-rc.0 removes everything deprecated in Wrangler v2 and v3, including legacy assets (`--legacy-assets`, `legacy_assets`), legacy Node.js compatibility (`--node-compat`, `node_compat`), `wrangler version`, `getBindingsProxy()` (use `getPlatformProxy()`) and `usage_model`; resource commands such as `wrangler kv`, `wrangler r2` and `wrangler d1` now target local datastores by default.
  Source: https://developers.cloudflare.com/changelog/post/2025-02-28-wrangler-v4-rc/
- **2025-03-18 - Deprecation** - The `agents-sdk` npm package was renamed `agents` and the old package marked deprecated.
  Source: https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/
- **2025-04-15 - Deprecation** - The `cloudflare_workers_secret` and `cloudflare_workers_for_platforms_script_secret` Terraform resources are to be removed in a future release.
  Source: https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/
- **2025-05-30 - Change** - Pages builds use the V3 build image with Node.js 22 by default for new projects; Node.js 18 is end of life.
  Source: https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/
- **2025-06-02 - Deprecation** - SCIM Virtual Groups (`CF-<accountID>-<Role Name>`) deprecated as of June 2, 2025, with end of life on December 2, 2025 (end-of-life date given in the 2025-06-23 GA post).
  Source: https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/
  Source: https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/
- **2025-06-09 - Breaking** - Workers native integrations removed from the dashboard (Integrations tab gone); new connections use `wrangler secret put`.
  Source: https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/
- **2025-06-18 - Breaking** - Gateway evaluates Network policies before HTTP policies from July 14, 2025, so some users no longer see the HTTP block page.
  Source: https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/
- **2025-06-30 - Breaking** - Email Routing requires SPF or DKIM authentication on forwarded mail from July 3, 2025.
  Source: https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/
- **2025-06-30 - Change** - Cloudflare One Agent for Android 2.4.2 and iOS 1.11 disable QLogs by default and ignore the previous QLog setting.
  Source: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/
  Source: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/
- **2025-07-01 - Deprecation** - Radar `verified_bots` endpoints deprecated in favour of the new bot insights APIs.
  Source: https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/
- **2025-07-22 - Breaking** - The Gateway Google Bard application (ID 1198) was removed and replaced by Gemini; policies referencing Bard no longer function.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/
- **2025-08-11 - Change** - `MessageChannel` and `MessagePort` are global by default for compatibility date `2025-08-15` or later (`no_expose_global_message_channel` to disable).
  Source: https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/
- **2025-08-14 - Breaking** - Python Workers handlers move into an entrypoint class by default; `disable_python_no_global_handlers` keeps the old style.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/
- **2025-08-15 - Change** - `node:fs` is available by default with `nodejs_compat` from compatibility date `2025-09-01`.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-15-nodejs-fs/
- **2025-08-22 - Deprecation** - Audit Logs v1 retirement announced as coming, with timelines to be shared later (repeated at v2 GA on 2026-03-10: "a deprecation timeline will be communicated separately").
  Source: https://developers.cloudflare.com/changelog/post/2025-08-22-audit-logs-v2-logpush/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/
- **2025-08-25 - Change** - Workers Assets serve JavaScript as `text/javascript` instead of `application/javascript`.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/
- **2025-08-29 - Deprecation** - Terraform v5.9 replaces `cloudflare_snippets` with `cloudflare_snippet` (see Gaps for contradictory wording).
  Source: https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/
- **2025-09-01 - Breaking** - Email security roles no longer grant read or write access to other Zero Trust products.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/
- **2025-09-02 - Breaking** - From December 1, 2025, Tunnel and Zero Trust Networks list endpoints no longer return deleted tunnels, routes, subnets and virtual networks by default.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/
- **2025-09-10 - Breaking** - Agents SDK v0.1.0 and `workers-ai-provider` v2.0.0 move to AI SDK v5 (tool definitions use `inputSchema`).
  Source: https://developers.cloudflare.com/changelog/post/2025-09-03-agents-sdk-beta-v5/
- **2025-09-17 - Breaking** - "Preview URLs now default to opt-in": a one-time update disabled preview URLs on existing Workers whose `workers.dev` subdomain was disabled; on 2025-10-23 the unconfigured default was changed to follow the `workers.dev` setting.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/
- **2025-11-05 - Breaking** - Managing Logpush jobs for Zero Trust datasets requires two permissions.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/
- **2025-11-06 - Change** - Gateway application remapping into new categories completes by January 30, 2026; rules on old categories need review.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/
- **2025-11-11 - Deprecation** - `cloudflared proxy-dns` removed from new releases starting February 2, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-11-cloudflared-proxy-dns/
- **2025-11-20 - Breaking** - Terraform v5.13.0 breaking changes for `cloudflare_api_token` and `cloudflare_account_token`; v5.14.0 (2025-12-05) carries a deprecation notice for `api_shield_discovery_operation`.
  Source: https://developers.cloudflare.com/changelog/post/2025-11-20-terraform-v5.13.0-provider/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-terraform-v5.14.0-provider/
- **2025-12-05 - Breaking** - WAF payload inspection raised to 1 MB on all plans, then reverted the same day to the previous maximum (128 KB on Enterprise) because of false positives.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/
- **2025-12-12 - Pricing** - Storage billing for SQLite-backed Durable Objects targeted for January 7, 2026 (Workers Paid only).
  Source: https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/
- **2025-12-22 - Breaking** - Agents SDK v0.3.0 and providers v3.0.0 move to AI SDK v6 (`CoreMessage` removed, `convertToModelMessages()` async, `generateObject` `mode` removed).
  Source: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/

### 2026

- **2026-01-20 - Breaking** - TypeScript SDK v6.0.0-beta.1 (many breaking changes); Python SDK v5.0.0-beta.1 followed on 2026-02-13.
  Source: https://developers.cloudflare.com/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/
- **2026-02-09 - Breaking** - Agents SDK v0.4.0: x402 v2 peer dependencies and types (see Web3 section); `onStateUpdate` deprecated for `onStateChanged`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/
- **2026-02-12 - Deprecation** - Terraform v5.17.0 deprecates `entries` on `zero_trust_dlp_predefined_profile` in favour of `enabled_entries`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-terraform-v5.17.0-provider/
- **2026-02-13 - Deprecation** - `createAutoRAG` deprecated in favour of `createAISearch`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/
- **2026-02-16 - Deprecation** - Workers Quick Editor DevTools inspector replaced by a log viewer.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/
- **2026-02-17 - Rename** - Magic WAN, Magic Firewall, Magic Network Monitoring, Magic WAN Connector and Magic Cloud Networking brand names retired.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/
- **2026-02-20 - Breaking** - `@cloudflare/codemode` v0.1.0 removes `experimental_codemode()` and `CodeModeProxy`; v0.2.0 moves `generateTypes` (2026-03-17).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/
- **2026-02-23 - Breaking** - Hyperdrive stops caching queries with PostgreSQL `STABLE` functions.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/
- **2026-02-24 - Breaking** - Durable Objects `deleteAll()` also deletes alarms from compatibility date `2026-02-24`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-24-deleteall-deletes-alarms/
- **2026-02-26 - Breaking** - `stale-while-revalidate` becomes asynchronous (`UPDATING` status).
  Source: https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/
- **2026-03-02 - Breaking** - Agents SDK v0.7.0 replaces the `Observability.emit()` system with `diagnostics_channel` events.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/
- **2026-03-11 - Breaking** - Cloudflare error Markdown frontmatter field `http_status` renamed `status`.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/
- **2026-03-19 - Deprecation** - Service Key authentication deprecated; Service Keys stop working on September 30, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/
- **2026-03-23 - Breaking** - Agents SDK v0.8.0 drops Zod v3; the AI Search post of the same day asks AutoRAG API (`/autorag/rags/`) users to migrate to the new endpoints.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/
- **2026-03-24 - Change** - The top-level Interconnects dashboard page was removed (now under Connectors).
  Source: https://developers.cloudflare.com/changelog/post/2026-03-24-interconnects-navigation-update/
- **2026-04-07 - Breaking** - Workers WebSockets auto-reply to Close frames from compatibility date `2026-04-07`.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/
- **2026-04-14 - Deprecation** - DLP profile-level advanced settings to be deprecated in a future release, in favour of account-level settings.
  Source: https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/
- **2026-04-14 - Rename** - WARP Connector renamed Cloudflare Mesh (connectors become mesh nodes).
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/
- **2026-04-15 - Rename** - Browser Rendering renamed Browser Run.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/
- **2026-04-16 - Breaking** - New AI Search instances use built-in storage and a new namespace binding, with a binding migration guide.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/
- **2026-04-21 - Breaking** - Workers WebSocket binary frames arrive as `Blob` by default from compatibility date `2026-03-17`.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/
- **2026-04-23 - Breaking** - Go SDK v6.10.0 breaking changes; Go SDK v7.0.0, Python SDK v5.0.0 (drops Python 3.8) and TypeScript SDK v6.0.0 (17 endpoints removed) on 2026-04-30.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-23-go-sdk-v6.10.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/
- **2026-04-24 - Deprecation** - Terraform v5.19.0 deprecates `cmd/migrate` in favour of `tf-migrate`.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-24-terraform-v5.19.0-provider/
- **2026-05-04 - Breaking** - Pingora-based cache streams bypassed responses unbuffered and strips `Set-Cookie` on MISS and EXPIRED.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/
- **2026-05-08 - Deprecation** - 18 Workers AI models deprecated on May 30, 2026 (Kimi K2.5 date moved from May 10).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/
- **2026-05-12 - Change** - Containers SSH through Wrangler enabled by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/
- **2026-05-13 - Breaking** - Agents SDK v0.12.4 removes `ChatOptions.tools`; `/cdn-cgi/rum` returns `405` instead of `404` for non-POST requests the same day.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/
- **2026-05-26 - Change** - Uncacheable responses report `BYPASS` instead of `MISS`.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/
- **2026-06-04 - Deprecation** - Pipelines binding field `pipeline` renamed `stream` (old field still accepted).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/
- **2026-06-09 - Deprecation** - Sandbox SDK: HTTP and WebSocket transports, `exposePort()`, default sessions and buffered stream equivalents deprecated; desktop removed in 0.10.2.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/
- **2026-06-18 - Change** - Cloudflare identity provider replaces one-time PIN as the default login method for new Zero Trust organizations.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/
- **2026-06-23 - Deprecation** - AMP and Signed Exchanges end of life; Zone API errors and SXG rulesets fail to save.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/
- **2026-07-01 - Change** - From September 15, 2026 new domains block Training and Agent AI bots on ad pages by default.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/
- **2026-07-03 - Breaking** - `@cloudflare/workers-types` v5 removes dated entrypoints.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/
- **2026-07-09 - Breaking** - New KV-backed Durable Object namespaces blocked on accounts without one; Tunnel CIDR route endpoints and `connections` field removed on October 5, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
- **2026-07-15 - Deprecation** - Legacy KV namespace routes deprecated, stop working October 15, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/
- **2026-07-21 - Deprecation** - Account Roles API deprecated for the Permission Groups API, no end-of-life date.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/
- **2026-07-27 - Deprecation** - `McpAgent` deprecated and feature-frozen; `createMcpHandler(v1Server, options)` scheduled for removal in the next major; MCP 2026-07-28 itself deprecates Roots, Sampling, Logging, HTTP+SSE and Dynamic Client Registration.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/
- **2026-07-28 - Breaking** - Cloudflare MCP server `/sse` URLs no longer serve HTTP+SSE; Kimi K2.6, K2.7 Code and GLM-5.2 return `403` on Workers Free; 1.1.1.1 DoH JSON `data` format changes.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/
- **2026-07-30 - Deprecation** - MCP portal `allow_code_mode` boolean deprecated for `code_mode`.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/
- **2026-08-04 - Breaking** - `nodejs_compat` on by default from compatibility date `2026-08-04`.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/
- **2026-08-11 - Breaking** - Initial resolved IPs for hostname routing move from CGNAT to `172.64.128.0/20` and `2606:4700:0cf1:4000::/64`.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/
- **2026-08-19 - Rename** - `@cloudflare/vitest-pool-workers` becomes `@cloudflare/vitest-plugin`.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-19-vitest-plugin/
- **2026-08-26 - Deprecation** - Azure Functions-based Microsoft Sentinel connector unsupported after 2026-09-14; Access service token secrets created from this date use the `cfast_` format.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/
  Source: https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/
- **2026-09-01 - Limits** - D1 Workers Free queries fail after the daily row limits.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
- **2026-09-08 - Breaking** - Miniflare v5 removes deprecated APIs (legacy alpha D1 bindings, `wrappedBindings`, built-in module discovery).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/
- **2026-09-10 - Change** - New Workflows on Workers Paid default to 7-day instance retention instead of 30.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/
- **2026-09-18 - Deprecation** - `cloudflared` 32-bit Windows and Intel macOS builds end in 2027.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/
- **2026-09-28 - Breaking** - Browser Run Lab sessions no longer expose `navigator.modelContextTesting`; purges force a cache miss for Cache Reserve content.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/
  Source: https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/
- **2026-10-01 - Deprecation** - Pipelines, R2 Data Catalog and R2 SQL resources "will be deprecated over time" after the Basin GA; Durable Objects stay alive on pending I/O from compatibility date `2026-10-01`.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/
- **2026-10-02 - Breaking** - Strict service token authentication, mandatory for organizations created on or after October 5, 2026.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/

## Web3, payments and agents

Method: every mirrored post was searched for x402, stablecoin, USDC, wallet, payment, pay per crawl, Monetization Gateway, Machine Payments, Ethereum, `eip155`, IPFS, web3, randomness, drand, blockchain, crypto, Bitcoin, Solana and NET Dollar.
The entries below are every hit that concerns payments, crypto or web3, in date order, with the details each post gives.

### What is not in the changelog

- No entry announces or changes the Ethereum gateway, the IPFS gateway or any web3 gateway product; the only web3 gateway mention is an exclusion in the DNS-only kill switch (below).
- No entry mentions randomness, drand or a randomness beacon.
- No entry mentions USDC, Solana, NET Dollar or a named stablecoin; "stablecoin" appears only in the Machine Payments post.
- "Ethereum" never appears as a word; the only EVM references are the `@x402/evm` package, the `ClientEvmSigner` type and the CAIP-2 identifier `eip155:84532` in the Agents SDK x402 migration.
- Monetization Gateway has exactly one changelog entry (its closed beta) and its own product filter and feed (`/changelog/product/monetization-gateway/`, `rss/monetization-gateway.xml`), listed under the Core platform feed.

### x402 and agent payments

- **2026-02-04 - AI Crawl Control: x402 Payment-Gated Proxy template** - New AI Crawl Control reference documentation includes Worker templates, among them an "x402 Payment-Gated Proxy" to monetize crawler access or charge bots while letting humans through free.
  The post's slug is dated 2026-02-09.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-reference-documentation/
- **2026-02-09 - Agents SDK v0.4.0: x402 v2 migration (breaking)** - The Agents SDK's x402 MCP payment integration moved from the legacy `x402` package to `@x402/core` and `@x402/evm` v2.
  Breaking changes for x402 users: replace the `x402` peer dependency with `@x402/core` and `@x402/evm` (`npm uninstall x402`, `npm install @x402/core @x402/evm`); `PaymentRequirements` uses v2 fields (for example `amount` instead of `maxAmountRequired`); `X402ClientConfig.account` changes from `viem.Account` to `ClientEvmSigner` (structurally compatible with `privateKeyToAccount()`).
  Network identifiers accept both legacy names and CAIP-2, with the post's example pairing legacy `"base-sepolia"` with the preferred `"eip155:84532"`; a `normalizeNetwork` export converts legacy names to CAIP-2.
  `X402ClientConfig.network` became optional (the client auto-selects from the payment requirements), the server side lazily connects to the facilitator on the first paid tool invocation, payment tokens are accepted in both the v2 `PAYMENT-SIGNATURE` and v1 `X-PAYMENT` HTTP headers, and `agents/x402` re-exports `PaymentRequirements`, `PaymentRequired`, `Network`, `FacilitatorConfig` and `ClientEvmSigner`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/
- **2026-07-13 - Agents SDK: MCP elicitation** - Agents connected to MCP servers with `addMcpServer` can answer elicitation requests; URL mode asks for consent before opening an out-of-band flow "such as third-party authorization or payment".
  Connections advertise only the modes that have handlers, and the advertised modes survive Durable Object hibernation.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/
- **2026-07-27 - Agents SDK v0.20.0: x402 client overload deprecated** - The `MCPClientManager.callTool(params, resultSchema, options)` overload "and the equivalent `withX402Client` overload" are compatibility overloads with no removal version announced; the replacement is `callTool(params, options)` or `callTool(confirm, params, options)`.
  Source: https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/
- **2026-09-30 - Monetization Gateway closed beta** - Monetization Gateway lets sellers (domain owners) charge agents for access to APIs, MCP tools, sites and datasets.
  Sellers define which requests require payment, the cost and where the payment should be sent; buyers receive payment instructions, sign an authorization and receive the resource after the payment has been settled.
  It uses the x402 protocol to handle payment authorization within the HTTP request flow; access is requested in the dashboard (`dash.cloudflare.com/?to=/:account/monetize/monetization-gateway`), with docs at `/monetization-gateway/` and a blog post at `blog.cloudflare.com/monetization-gateway-beta/`.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/
- **2026-09-30 - AI Gateway Machine Payments beta (x402, stablecoin wallet)** - Clients can use x402 to pay for eligible inference requests "directly from a stablecoin wallet instead of maintaining a prepaid credit balance".
  It is available for the `/ai/run` endpoint with select open models; the request authenticates with a Cloudflare API token and adds the Cloudflare-specific header `Payment-Method: x402` (the example calls model `z-ai/glm-4.7-flash` at `https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run`).
  An x402-compatible client handles the payment challenge, signs an authorization from the client's wallet and retries the request.
  Machine Payments currently requires customers to be based in the United States and to have a credit card on file; prerequisites, eligible models and transaction details are on the "Machine Payments (x402)" docs page (`/ai-gateway/features/machine-payments/`).
  Source: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/

### Pay Per Crawl and HTTP 402 (AI Crawl Control)

- **2025-07-01 - Pay Per Crawl (private beta)** - Site owners can require payment from AI crawlers each time they access content: set pricing and choose which crawlers to charge, manage payments via Stripe, and see analytics on successful deliveries; crawler operators use HTTP headers to request and accept pricing and receive confirmations of charges.
  Source: https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/
- **2025-08-27 - Custom 402 responses** - On paid plans, AI Crawl Control blocks can return `402 Payment Required` instead of `403`, with a custom body carrying licensing contact information.
  Source: https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/
- **2025-12-10 - Pay Per Crawl enhancements (private beta, breaking for crawlers)** - A Discovery API, `GET https://crawlers-api.ai-audit.cfdata.org/charged_zones`, lets verified crawlers (Web Bot Auth) list participating domains.
  Payment headers (`crawler-exact-price` or `crawler-max-price`) must now be included in the Web Bot Auth `signature-input` components, to prevent tampering and replay with modified pricing.
  Error responses carry a new `crawler-error` header with 11 error codes; site owners can make pages free with a Configuration Rule ("Disable Pay Per Crawl" on a URI pattern), and `/robots.txt`, `/sitemap.xml`, `/security.txt`, `/.well-known/security.txt` and `/crawlers.json` are always free.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/
- **2026-06-16 - Pay Per Crawl advanced configuration** - Disable Pay Per Crawl by URI pattern with Configuration Rules, and dynamic pricing through an origin `crawler-price` response header or a Worker; with dynamic pricing on, origin requests carry a `cf-pay-per-crawl` header.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/

### Related agent-economy and AI billing entries

- **2026-04-17 - Agent readiness** - AI Crawl Control links to an Agent Readiness score; Radar tracks adoption of AI agent standards; on 2026-05-12 URL Scanner added six Agent Readiness scores, one of them "Commerce".
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-tools-for-agentic-internet/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/
  Source: https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/
- **2026-06-05 - AI Gateway spend limits** - Dollar budgets per model, provider or metadata (for example $200 per user per day), for Unified Billing and BYOK.
  Source: https://developers.cloudflare.com/changelog/post/2026-06-05-spend-limits/
- **2026-07-01 - AI traffic by behaviour** - Search, Agent and Training categories; the post frames Search as traffic that should bring "referral traffic or other equitable compensation".
  Source: https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/
- **2026-08-07 - Prepaid AI Gateway credits pay for Workers AI** - One credit balance for Workers AI and third-party models, and access to frontier models without Workers Paid.
  Source: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
- **2026-09-14 - BYOK-only gateways** - `byok_only: true` prevents fallback to Unified Billing.
  Source: https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/
- **2026-10-02 - Web Search API** - Billed to AI Gateway credits at each provider's list price with no markup.
  Source: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/

### Other crypto and web3 mentions

- **2026-04-28 - DNS: Web3 gateways excluded from enforce DNS-only** - The account-level `enforce_dns_only` kill switch does not affect "Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains", which continue to operate normally.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-28-enforce-dns-only/
- **2026-04-30 - DLP: crypto wallet detections** - New predefined DLP detection entries include "crypto wallets", with `Bitcoin Wallet` given as an example.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-30-standalone-predefined-detection-entries/

### Non-crypto payment methods for Cloudflare's own billing

- **2026-04-29 - Instant Bank Payments via Link** - US self-serve accounts can pay from a bank account through Link; payments show as method `link` with last four digits `0000`.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/
- **2026-05-21 - Billing Profile** - Apple Pay, Google Pay, Link, Instant Bank Payments, cards and PayPal; 3D Secure where the issuer requires it (EU PSD2, India RBI).
  Source: https://developers.cloudflare.com/changelog/post/2026-05-21-modernised-billing-profile/

## Gaps and contradictions

### Coverage gaps in the mirror and in the changelog itself

- The mirror holds 1,307 posts, every post linked from any listing page; the oldest dated post is from 2024-02-26 and real coverage starts in June 2024.
  The 2024-06-16 Cloudflare One post says older product updates live on per-product changelog pages (for example `/cloudflare-one/changelog/access/`), which are outside `raw/docs/changelog/`, so the "whole history" deprecation list starts in 2025.
- DDoS managed ruleset changes and the API deprecations list have their own feeds and pages and are not changelog posts; this file does not cover them.
- The RSS page lists group feeds for only 7 of the 13 groups shown on the changelog (none for AI, Analytics, Docs collections, Media, Privacy, Storage), and no product feed for the `logpush` and `logpush-connectors` product pages.
- The RSS page says "Last updated Apr 20, 2026" but lists feeds for products first announced later, such as Web Search API (`web-search.xml`, first post 2026-10-02), Monetization Gateway and Basin.
- The "Consuming RSS Feeds" example item links to `https://developers.cloudflare.com/changelog/2025-02-14-example-ai-prompts/`, while every mirrored post lives under `/changelog/post/<slug>/`.
- Every changelog listing page, including product and group pages, links "Subscribe to RSS" to the global feed rather than the page's own feed.
- Several announced cutoffs have no follow-up post in the mirror confirming they happened: Durable Objects SQLite storage billing (target 2026-01-07), Gateway application remapping (by 2026-01-30), `cloudflared proxy-dns` removal (2026-02-02), Workflows step billing (no earlier than 2026-08-10), Service Key shutdown (2026-09-30), the new AI bot defaults for new domains (2026-09-15) and the Tunnel CIDR route endpoint removal (2026-10-05, the snapshot date).
- Open-ended deprecations without dates: Audit Logs v1 retirement ("will be communicated separately"), Account Roles API end of life, `McpAgent` removal, DLP profile-level advanced settings, Sandbox SDK transports and default sessions, Pipelines, R2 Data Catalog and R2 SQL resources after Basin GA, Terraform `cmd/migrate`, and Workers AI LoRA models ("may be deprecated in the future").
- Many digest bullets summarise posts whose code samples were not reproduced; the post pages hold the exact configuration and API shapes.

### Dates that disagree

Eight posts have a slug date more than 30 days away from the publish date, two more are 24 and 29 days off, and nine slugs carry no ISO date at all; this file uses the publish date throughout.

| Slug | Published | Gap |
| --- | --- | --- |
| `2025-02-25-rum-exclude-eu` | 2024-02-26 | slug one year later |
| `2025-04-14-account-level-dlp-settings` | 2026-04-14 | slug one year earlier |
| `2026-04-15-registrar-api-beta` | 2025-04-15 | slug one year later; the post mentions Cloudflare MCP and agent workflows |
| `2025-07-01-Access-Supports-Customer-Metadata-Boundary` | 2025-08-14 | 44 days |
| `2025-08-15-monitor-groups-for-load-balancing` | 2025-10-16 | 62 days |
| `2025-08-15-gemini-application-replaces-bard` | 2025-07-22 | slug 24 days later |
| `2025-09-25-workers-vpc` | 2025-11-05 | 41 days |
| `2025-12-11-builds-event-subscriptions` | 2026-01-09 | 29 days |
| `2026-06-10-improved-reliability-for-web-analytics-dash` | 2026-07-14 | 34 days |
| `2026-06-15-budget-alerts-default-on` | 2026-07-20 | 35 days |

The Registrar API beta and the DLP account-level settings posts are year-flipped in opposite directions, so their true dates cannot be settled from the mirror alone.

### Statements that conflict or were reversed

- **WAF payload limit, 2025-12-05**: one post says the WAF now inspects up to 1 MB on all plans; a second post the same day says the limit was reinstated (128 KB on Enterprise) because of false positives, and the first post carries an "Update" note.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-rcs-vuln/
  Source: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/
- **Pay Per Crawl free pages**: "Disable Pay Per Crawl" by URI pattern through Configuration Rules is described as new on 2025-12-10 and again as new on 2026-06-16.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/
  Source: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/
- **Terraform v5.9 snippets**: the post says "`cloudflare_snippet` is now considered deprecated but can still be used" and, a few lines later, that `cloudflare_snippet` replaces `cloudflare_snippets` and "`cloudflare_snippets` is now deprecated".
  Source: https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/
- **Preview URL defaults**: 2025-09-17 "Preview URLs now default to opt-in", then 2025-10-23 says an unconfigured preview URL follows the `workers.dev` setting and that both default to enabled when neither is set.
  Source: https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/
  Source: https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/
- **Kimi K2.5 deprecation date**: the 2026-05-08 post says the date was "originally stated" as May 10, 2026 and moved to May 30, 2026; no mirrored post contains the original May 10 announcement.
  Source: https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/
- **Agents SDK client tool APIs**: v0.3.0 deprecated `AITool`, `extractClientToolSchemas()` and `createToolsFromClientSchemas()` in favour of server-side `tool()`, and v0.6.0 "undeprecated" them (plus `clientTools` and the `tools` option on `useAgentChat`) for tools defined at runtime.
  Source: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/
  Source: https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/
- **Artifacts beta stage**: the 2026-04-16 title says "now in beta" while the body says "private beta"; open beta followed on 2026-10-01.
  Source: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/
- **Browser Rendering `/crawl`**: the 2026-03-10 post carries an edit note "to clarify crawling behavior with respect to site guidance", so earlier copies of the post may differ.
  Source: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
- **Agents SDK "zero breaking changes"**: v0.5.0 says `@cloudflare/ai-chat` ships "with zero breaking changes", but the same post changes the default of `autoContinueAfterToolResult` to `true`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/
- **Product names in flux**: posts written before a rename keep the old names (Magic WAN, Magic Firewall, Magic Network Monitoring, WARP client, WARP Connector, Browser Rendering, R2 Data Catalog, R2 SQL, Pipelines, AutoRAG), while their product tags show the new names (Cloudflare WAN, Cloudflare Network Firewall, Network Flow, Cloudflare One Client, Cloudflare Mesh, Browser Run, Basin Catalog, Basin SQL, Basin Pipelines, AI Search); the Tunnel API still calls Mesh nodes `warp_connector`.
  Source: https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/
  Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/
  Source: https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/
  Source: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
