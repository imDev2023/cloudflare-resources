# Platform and tooling: Get started and Developer Tools

This file covers the "Get started" and "Developer Tools" parts of the developers.cloudflare.com sidebar, plus the cross-product Fundamentals section, as mirrored on 2026-10-05.
It explains the docs homepage and Directory, the agent-facing docs features (Markdown, llms.txt, MCP servers, Cloudflare Skills, Agent Setup guides for ten coding agents), the learning resources (learning paths, use cases, reference architecture), the API and infrastructure-as-code tools (SDKs, Terraform, Pulumi), Support, the new Cloudflare CLI `cf` (beta since 2026-09-28), Wrangler, the account, token, permission, plan and network fundamentals, and the (still empty) migration guides section.
For each tool it records what it is, how to use it, how it authenticates, whether it is beta or GA, and the pages worth reading.
The companion file `api-reference.md` covers the REST API itself (base URL, envelope, pagination, rate limits, every top-level resource with operation counts, and local lookup recipes).
Everything here states only what the mirrored pages say; contradictions are flagged in the last section rather than resolved.

## Table of contents

1. [Docs homepage](#1-docs-homepage)
2. [Directory](#2-directory)
3. [Changelog and RSS](#3-changelog-and-rss)
4. [Docs for agents](#4-docs-for-agents)
5. [Agent Setup, Cloudflare Skills and MCP servers](#5-agent-setup-cloudflare-skills-and-mcp-servers)
6. [Dashboard AI assistants: Agent Lee and Cloudy](#6-dashboard-ai-assistants-agent-lee-and-cloudy)
7. [Resources: learning paths, use cases, reference architecture](#7-resources-learning-paths-use-cases-reference-architecture)
8. [API and IaC: SDKs, Terraform, Pulumi](#8-api-and-iac-sdks-terraform-pulumi)
9. [Support](#9-support)
10. [Cloudflare CLI (`cf`)](#10-cloudflare-cli-cf)
11. [Wrangler](#11-wrangler)
12. [Fundamentals](#12-fundamentals)
13. [Migration guides](#13-migration-guides)
14. [Build hooks for Web3 projects](#14-build-hooks-for-web3-projects)
15. [Gaps and contradictions](#15-gaps-and-contradictions)

---

## 1. Docs homepage

Source: https://developers.cloudflare.com/

The homepage title is "Cloudflare Developer Docs" with the tagline "Connect, protect, and build everywhere."
It has a "Get started" button pointing to https://developers.cloudflare.com/fundamentals/get-started/ and a "Copy prompt" button showing icons for Claude, Codex, Cursor and OpenCode.
A CLI selector ("Wrangler" or "CF") switches the code examples on the page between the two CLIs.

The "Powerful primitives" block groups products into four tabs, each with a one-line starter command:

| Tab | Starter command shown | Products linked |
| --- | --- | --- |
| Compute | `npm create cloudflare@latest my-app` | Workers, Containers, Durable Objects, Queues, Flagship |
| AI | `npx wrangler ai models` and `cf ai run @cf/meta/llama-3.1-8b-instruct --help` | Workers AI, AI Gateway, AI Search, Agents, Vectorize, Browser Run |
| Storage & Databases | `npx wrangler d1 create my-database` and `cf d1 --help` | R2, Basin, K2, D1, KV, Hyperdrive |
| Media | `curl --request POST https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/images/v1` | Images, Stream, Realtime |

The homepage promotes Cloudflare Connect 2026 in San Francisco, October 19 to 21 (as of 2026-10-05).
It shows a "What's new" strip of the latest changelog posts; on 2026-10-05 the newest entries were dated 2026-10-02 and included the Web Search API (AI Gateway, with Ceramic.ai, Exa and Linkup), strict service token authentication for Access, the PiHarness beta in the Agents SDK, 30 days of analytics on every plan, Workers Observability in Custom Dashboards, a D1 United States jurisdiction, Workers KV namespace jurisdictions GA, and `hash_in_range()` GA in Ruleset Engine expressions.
The security block claims Cloudflare's CDN caches content "in 330+ cities worldwide" and that its authoritative DNS is "consistently ranked #1 by DNSPerf".
Community links are Discord (https://discord.cloudflare.com/), X and the forum (https://community.cloudflare.com/); open source links are GitHub, GitHub Sponsors and the docs style guide.

## 2. Directory

Source: https://developers.cloudflare.com/directory/

The Directory is a filterable card list of every product area in the docs.
Filter groups are AI, Analytics, Application performance, Application security, Cloudflare One, Consumer services, Core platform, Developer platform, Docs collections, Media, Network security, Privacy and Storage.
The mirrored page lists 138 cards (as of 2026-10-05).
Cards worth knowing because they are new or easy to miss:

| Card | One-line description from the Directory | URL |
| --- | --- | --- |
| Agent Lee | AI co-pilot built into the dashboard | https://developers.cloudflare.com/agent-lee/ |
| Agent Memory | Persistent AI-powered memory for agents and applications | https://developers.cloudflare.com/agent-memory/ |
| Artifacts | Store, version and share filesystem artifacts across Workers, APIs and git-compatible tools | https://developers.cloudflare.com/artifacts/ |
| Basin, Basin Pipelines, Basin Catalog, Basin SQL | Analytics data in R2, streaming ingest, Iceberg tables, serverless SQL | https://developers.cloudflare.com/basin/ |
| Cloudflare CLI | Manage Cloudflare resources from one command-line interface | https://developers.cloudflare.com/cf/ |
| Cloudflare Wallets | Reserve a wallet handle and give your account and its agents a stable, human-readable identity for agentic payments | https://developers.cloudflare.com/wallets/ |
| Dynamic Workers | Spin up isolated Workers on demand to execute code | https://developers.cloudflare.com/dynamic-workers/ |
| Flagship | Feature flags evaluated at the edge for Workers | https://developers.cloudflare.com/flagship/ |
| K2 | A durable event stream | https://developers.cloudflare.com/k2/ |
| Monetization Gateway | Define monetization policies to charge any visitor accessing APIs, MCP tools, web pages or datasets | https://developers.cloudflare.com/monetization-gateway/ |
| MoQ | Protocol for live media | https://developers.cloudflare.com/moq/ |
| OAuth documentation | Create and integrate with Cloudflare using OAuth | https://developers.cloudflare.com/fundamentals/oauth/ |
| Randomness Beacon | drand, a distributed randomness service | https://developers.cloudflare.com/randomness-beacon/ |
| Resource Tagging | Key-value metadata on resources for organization, access control and billing attribution | https://developers.cloudflare.com/resource-tagging/ |
| Sandboxes | Isolated execution using Containers and Dynamic Workers | https://developers.cloudflare.com/sandbox/ |
| Tenant | Provision and manage Cloudflare accounts and services for your team or customers | https://developers.cloudflare.com/tenant/ |
| Version Management | Versioning, staging and rollbacks of configurations | https://developers.cloudflare.com/version-management/ |
| Web Search API | Ground AI agents with real-time web search results | https://developers.cloudflare.com/web-search/ |
| Web3 | Gateways to networks to help you develop applications without running infrastructure | https://developers.cloudflare.com/web3/ |

The machine-readable equivalent of the Directory is https://developers.cloudflare.com/llms.txt, which lists 113 product indexes grouped under Application performance, Application security, Cloudflare One, Consumer services, Core platform, Developer platform, Docs collections, Network security and Other (counted 2026-10-05).

## 3. Changelog and RSS

Sources: https://developers.cloudflare.com/changelog/ and https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/

The Changelog is a sidebar entry under Get started; the mirror holds 1,579 pages under `/changelog/` (counted 2026-10-05).
RSS feeds exist for all posts (https://developers.cloudflare.com/changelog/rss/index.xml), for each product group (for example `/changelog/rss/application-performance.xml`) and for each product.
API deprecations have their own RSS feed at https://developers.cloudflare.com/fundamentals/api/reference/deprecations/index.xml.
Changelog posts relevant to this file include "Cloudflare CLI is now in beta" (2026-09-28, https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/), Wrangler v4 (2025-03-13), Wrangler auto-configuration GA (2026-02-25), Markdown for Agents (2026-02-12) and granular API token permissions (2026-01-22).

## 4. Docs for agents

Source: https://developers.cloudflare.com/docs-for-agents/ (last updated Sep 29, 2026)

"Docs for agents" explains how AI agents can consume Cloudflare documentation and call Cloudflare APIs.
It names three approaches: agent skills, MCP servers and command-line tools.

### 4.1 Markdown versions of every page

Every docs page is available as Markdown in three ways, powered by Markdown for Agents:

- Select **Copy as Markdown** on any page.
- Append `/index.md` to the page URL, for example `https://developers.cloudflare.com/workers/get-started/index.md`.
- Send `Accept: text/markdown`, for example `curl "https://developers.cloudflare.com/workers/get-started/" --header "Accept: text/markdown"`.

Markdown responses carry `x-markdown-tokens` and `x-original-tokens` headers with estimated token counts of the Markdown and the original HTML.

### 4.2 llms.txt and llms-full.txt

| Endpoint | Content |
| --- | --- |
| https://developers.cloudflare.com/llms.txt | Page index grouped by product category, linking each product's own `llms.txt` |
| https://developers.cloudflare.com/llms-full.txt | Full content of all documentation in one file |
| `/<product>/llms.txt` (for example `/workers/llms.txt`) | Page index for one product |
| `/<product>/llms-full.txt` | Full content of one product's pages |

Every product `llms.txt` begins with the same note that any page can be retrieved as Markdown with an `Accept: text/markdown` header.

### 4.3 OpenAPI specification

The full API spec is published at https://github.com/cloudflare/api-schemas (JSON) for AI coding tools, API clients and code generators.
This knowledge base keeps a copy at `raw/api/openapi.json`; see `api-reference.md`.

### 4.4 CLIs for agents

The page lists two CLIs agents can run:

- The Cloudflare CLI `cf` (beta), which "covers the whole Cloudflare API and prints JSON output"; agents discover commands with `cf cli search` and inspect them with `cf schema`.
- Wrangler, which "develops and deploys Workers projects configured with `wrangler.jsonc` or `wrangler.toml`".

### 4.5 Concepts the page defines

- Model flexibility: Locked (vendor models only), BYOK (bring your own key), Multi-provider.
- Context approaches: Project memory (stored files or memory across sessions) and Indexed codebase (searchable repository index).

### 4.6 Markdown for Agents as a zone feature

Source: https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ (last updated Jul 13, 2026)

Markdown for Agents is also a feature you can turn on for your own zone, so AI clients that send `Accept: text/markdown` get your HTML converted to Markdown at the edge.
Enabling it in the dashboard requires a Pro or Business plan, per the page's "How to enable" step (as of 2026-10-05).
Via the API, send `PATCH /client/v4/zones/{zone_tag}/settings/content_converter` with `{"value": "on"}` using a token with Zone Settings edit permission.
It can be scoped to subdomains or paths with a configuration rule, and enabled for Cloudflare for SaaS custom hostnames.
Converted responses keep origin security and cache headers, set `Content-Type: text/markdown; charset=utf-8`, add `Accept` to `Vary`, recompute `Content-Length`, and drop `Content-Encoding`, `Content-Range`, `Transfer-Encoding`, `ETag` and `Last-Modified`.
If the origin sends no `content-signal` header, Cloudflare adds `Content-Signal: ai-train=yes, search=yes, ai-input=yes`; an origin value is preserved.
Output is YAML frontmatter (`title`, `description`, `image` from meta tags), then the body Markdown, then any JSON-LD as a fenced `json` block.

### 4.7 Structured error responses for agents

Source: https://developers.cloudflare.com/fundamentals/reference/error-responses/ (last updated May 5, 2026)

Cloudflare-generated errors (all 1xxx codes and Cloudflare-generated 500, 502, 504, 520 to 526) are returned as JSON (`application/json` or `application/problem+json`) or Markdown (`text/markdown`) when the client asks for them in `Accept`, and as HTML otherwise.
At equal quality values the first-listed type wins, `text/*` yields Markdown, and `*/*` or no header yields HTML.
Structured error responses are available on all plans including Free; Custom Error Rules that override them need a paid plan.
A zone that has an uploaded Error Page serves that HTML to every client regardless of `Accept`, unless a Custom Error Rule matches first.

## 5. Agent Setup, Cloudflare Skills and MCP servers

Sources: https://developers.cloudflare.com/agent-setup/ and its per-agent pages, https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/ (last updated Jul 28, 2026)

Agent Setup is a set of step-by-step guides to install a coding agent, connect Cloudflare Skills and MCP servers, and start deploying.
The index says "Every agent listed supports Skills and MCP."

### 5.1 The ten supported agents (as of 2026-10-05)

| Agent | Maker | Pricing | Model | Context | Install | How Cloudflare tooling is added | Guide |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | Anthropic | Subscription | Locked | Project memory | `curl -fsSL https://claude.ai/install.sh \| bash` | `/plugin marketplace add cloudflare/skills` then `/plugin install cloudflare@cloudflare` (installs Skills and registers MCP servers) | https://developers.cloudflare.com/agent-setup/claude-code/ |
| Codex | OpenAI | Hybrid | Locked | Project memory | `npm install -g @openai/codex` (WSL2 on Windows) | `/plugins`, search and install **Cloudflare**; desktop app: Plugins > Cloudflare | https://developers.cloudflare.com/agent-setup/codex/ |
| Cursor | Cursor | Subscription | Multi-provider | Indexed codebase | Download from cursor.com | `/add-plugin cloudflare` or the Cursor Marketplace | https://developers.cloudflare.com/agent-setup/cursor/ |
| GitHub Copilot | GitHub | Subscription | Multi-provider | Indexed codebase | VS Code extension (also JetBrains, Visual Studio, Xcode) | `npx skills add https://github.com/cloudflare/skills`; MCP in `.vscode/mcp.json`, `~/.copilot/mcp-config.json`, `.mcp.json` or `.github/mcp.json` | https://developers.cloudflare.com/agent-setup/github-copilot/ |
| OpenCode | Anomaly | BYOK | Multi-provider | Project memory | `curl -fsSL https://opencode.ai/install \| bash` | `npx skills add https://github.com/cloudflare/skills`; MCP under `"mcp"` in `.opencode.jsonc` with `"type": "remote"` | https://developers.cloudflare.com/agent-setup/opencode/ |
| Vibe | Mistral AI | Hybrid | Multi-provider | Project memory | `curl -LsSf https://mistral.ai/vibe/install.sh \| bash`, then `vibe --setup` | `npx skills add cloudflare/skills --skill '*' --yes` (project skills in `.agents/skills/`); MCP as `[[mcp_servers]]` in `~/.vibe/config.toml`, then `/mcp login <name>` | https://developers.cloudflare.com/agent-setup/vibe/ |
| Devin | Cognition | Subscription | Multi-provider | Indexed codebase | Devin Desktop download | `npx skills add https://github.com/cloudflare/skills`; MCP in `~/.codeium/windsurf/mcp_config.json` with `serverUrl` keys | https://developers.cloudflare.com/agent-setup/devin/ |
| Visual Studio Code | Microsoft | BYOK | Multi-provider | Project memory | VS Code plus GitHub Copilot extension (free tier works) | `.vscode/mcp.json` with root key `servers` (not `mcpServers`), then the **Start** CodeLens to run OAuth | https://developers.cloudflare.com/agent-setup/visual-studio-code/ |
| Command Code | Command Code | Subscription | Multi-provider | Project memory | `npm i -g command-code@latest` (alias `cmd`, `cmdc` on Windows) | `cmd skills add https://github.com/cloudflare/skills` (to `.commandcode/skills/`, `--global` for `~/.commandcode/skills/`); `cmd mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp` | https://developers.cloudflare.com/agent-setup/command-code/ |
| Bionic | LM Studio | Hybrid | Multi-provider | not stated | Download from lmstudio.ai | Create a **Code Project**, add `https://mcp.cloudflare.com/mcp` as a remote MCP server | https://developers.cloudflare.com/agent-setup/bionic/ |

Every guide says to start the agent from the project root where `wrangler.jsonc` or `cloudflare.config.ts` lives, because the agent reads bindings from it.
A screenshot walkthrough for VS Code (connect, OAuth, create and delete a DNS record by natural language) is at https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/.
That walkthrough recommends a demo account, warns that **Full access** lets the agent create and delete real resources, and says 401 errors in VS Code logs are expected until you select **Allow in this Session**.

### 5.2 Cloudflare Skills

Sources: https://developers.cloudflare.com/agent-setup/claude-code/ and https://developers.cloudflare.com/docs-for-agents/

Skills are task-specific instructions an agent loads on demand, following the Agent Skills standard (https://agentskills.io/home).
They are published in https://github.com/cloudflare/skills.
Every agent guide lists the same 16 skills (as of 2026-10-05):

| Skill | What it is for (from the guides) |
| --- | --- |
| `agents-sdk` | Build, debug or review Agents SDK applications using the `agents` package |
| `basin` | Basin Pipelines, Basin Catalog and Basin SQL; also covers the former Data Platform, Pipelines, R2 Data Catalog and R2 SQL names |
| `cloudflare` | Discover and choose Cloudflare products for an architecture, including when no product is named |
| `cloudflare-email-service` | Email Sending and Email Routing integrations |
| `cloudflare-one` | Design, configure, troubleshoot or review Cloudflare One Zero Trust and SASE deployments |
| `cloudflare-one-migrations` | Plan migrations from VPN, SWG or SASE platforms to Cloudflare One |
| `durable-objects` | Build, debug or review Durable Objects |
| `k2` | K2 or K2 Streams durable logs: stream setup, producing from Workers or HTTP, retention, subscriptions |
| `nextjs-on-cloudflare` | Next.js on Workers with vinext; installs vinext's upstream skills with `npx skills add cloudflare/vinext` if missing |
| `sandbox-migrate-to-next` | Migrate Sandbox apps from stable `@cloudflare/sandbox` to `@cloudflare/sandbox@next` (SDK 1.0 preview) |
| `sandbox-next` | Build Sandbox apps on `@cloudflare/sandbox@next` |
| `sandbox-stable` | Build Sandbox apps on the stable `@cloudflare/sandbox` |
| `turnstile-spin` | Set up, repair or migrate to Turnstile, including server-side Siteverify |
| `web-perf` | Audit or optimize Core Web Vitals and Lighthouse scores |
| `workers-best-practices` | Production best practices for writing, reviewing and configuring Workers |
| `wrangler` | Run or troubleshoot Wrangler commands and configure Worker projects |

The plugin also adds two slash commands: `/cloudflare:build-agent` (scaffold an Agents SDK project) and `/cloudflare:build-mcp` (scaffold a remote MCP server).
Manual skill directories per agent: Claude Code `~/.claude/skills/`, Cursor `~/.cursor/skills/`, OpenCode `~/.config/opencode/skills/`, Codex `~/.codex/skills/`, Pi `~/.pi/agent/skills/` (from the MCP servers catalog page).
The FAQ on the Claude Code guide recommends using Skills, MCP and a CLI together: Skills for platform knowledge, the API MCP server for platform operations, Wrangler for local dev and Workers commands, and `cf` for tasks across the whole API.

### 5.3 The Cloudflare API MCP server (Code Mode)

Source: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/

- URL: `https://mcp.cloudflare.com/mcp`; repository https://github.com/cloudflare/mcp.
- It exposes the entire Cloudflare API through two tools, `search()` and `execute()`; the model writes JavaScript against a typed representation of the OpenAPI spec, and the code runs in an isolated Dynamic Worker sandbox.
- The page's token comparison: native MCP with full schemas would be 2,594 tools and about 1,170,000 tokens; required-params-only about 244,000 tokens; Code Mode 2 tools and about 1,000 tokens.
- Auth: connecting redirects you to Cloudflare to authorize via OAuth and choose permissions; the authorization page offers **Read only**, **Full access** or **Custom** templates and account scoping (VS Code guide).
- For CI or automation, pass a Cloudflare API token as a bearer token in the `Authorization` header; both user tokens and account tokens are supported.
- Revoke a grant at **My Profile > Access Management > Connected Applications** (VS Code guide).
- Transport: use the Streamable HTTP endpoint at `/mcp`; the servers support the MCP 2026-07-28 specification and stateless requests from 2025 Streamable HTTP clients; historical `/sse` URLs are aliases for the same Streamable HTTP handler and do not serve the deprecated HTTP+SSE transport (as of 2026-10-05).

Minimal client config:

```json
{ "mcpServers": { "cloudflare-api": { "url": "https://mcp.cloudflare.com/mcp" } } }
```

### 5.4 Product-specific MCP servers

The catalog page (Jul 28, 2026) and the Agent Setup guides list slightly different sets; this table merges both and marks where each appears.

| Server | URL | Purpose | In catalog page | In Agent Setup list |
| --- | --- | --- | --- | --- |
| Documentation | https://docs.mcp.cloudflare.com/mcp | Up-to-date reference information (public, no OAuth per the Vibe guide) | yes | yes |
| Workers Bindings | https://bindings.mcp.cloudflare.com/mcp | Build Workers apps with storage, AI and compute primitives | yes | yes |
| Workers Builds | https://builds.mcp.cloudflare.com/mcp | Insights into and management of Workers Builds | yes | yes |
| Observability | https://observability.mcp.cloudflare.com/mcp | Debug logs and analytics | yes | yes |
| Radar | https://radar.mcp.cloudflare.com/mcp | Internet traffic insights, trends, URL scans | yes | yes |
| Container | https://containers.mcp.cloudflare.com/mcp | Spin up a sandbox development environment | yes | yes |
| Browser Run | https://browser.mcp.cloudflare.com/mcp | Fetch pages, convert to Markdown, screenshots | yes | yes |
| Logpush | https://logs.mcp.cloudflare.com/mcp | Summaries of Logpush job health | yes | yes |
| AI Gateway | https://ai-gateway.mcp.cloudflare.com/mcp | Search gateway logs, prompts and responses | yes | yes |
| AI Search (named "AutoRAG server" in Agent Setup) | https://autorag.mcp.cloudflare.com/mcp | List and search documents in AI Search instances | yes | yes |
| Audit Logs | https://auditlogs.mcp.cloudflare.com/mcp | Query audit logs and generate reports | yes | no |
| DNS Analytics | https://dns-analytics.mcp.cloudflare.com/mcp | Optimize DNS performance and debug | yes | yes |
| Digital Experience Monitoring | https://dex.mcp.cloudflare.com/mcp | Insight on critical applications | yes | yes |
| Cloudflare One CASB | https://casb.mcp.cloudflare.com/mcp | SaaS security misconfigurations | yes | yes |
| GraphQL | https://graphql.mcp.cloudflare.com/mcp | Analytics via the GraphQL API | yes | no |
| Agents SDK Documentation | https://agents.cloudflare.com/mcp | Token-efficient search of Agents SDK docs | yes | no |
| Cloudflare Blog | https://blog.mcp.cloudflare.com/mcp | Search and read Cloudflare Blog posts | no | yes |
| Demo Day | https://demo-day.mcp.cloudflare.com/mcp | A minimal demo MCP server | no | yes |

The Agent Setup configs for Copilot, OpenCode, Vibe and Devin install a standard set of five: `cloudflare` (API), `cloudflare-docs`, `cloudflare-bindings`, `cloudflare-builds`, `cloudflare-observability`.
The domain-specific servers live in https://github.com/cloudflare/mcp-server-cloudflare.
For enterprise control of agent MCP traffic, the docs point to MCP server portals in Cloudflare One (https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

### 5.5 Tips and troubleshooting from the guides

- Verify servers with `claude mcp list`; if a connection fails, remove and re-add the server (Claude Code guide).
- For CI/CD, skip OAuth by passing an API token as a bearer token (Claude Code guide).
- If the agent returns outdated product facts, enable the docs MCP server or point it at `llms.txt` (Claude Code guide).
- VS Code shows only three tools registered for the API server because of Code Mode (VS Code guide).
- Copilot loads `.github/copilot-instructions.md` on every interaction; Vibe and Command Code read `AGENTS.md`.

### 5.6 Temporary accounts for agent deploys

Source: https://developers.cloudflare.com/workers/platform/claim-deployments/ (last updated Jul 14, 2026)

An agent without Cloudflare credentials can run `npx wrangler deploy --temporary` (Wrangler 4.102.0 or later).
Wrangler creates or reuses a temporary preview account, deploys to a `workers.dev` URL, and prints a claim URL; the example output shows "Claim within: 60 minutes".
In an unauthenticated non-interactive session, plain `wrangler deploy` prints a hint telling the agent to rerun with `--temporary`.
Platforms can do the same server-side through `api.cloudflare.com/client/v4/provisioning/previews`, which returns temporary credentials and a claim URL to the backend.
For production and CI/CD the page says to use a permanent account with `wrangler login` or an API token.

## 6. Dashboard AI assistants: Agent Lee and Cloudy

Agent Lee (https://developers.cloudflare.com/agent-lee/, last updated Sep 24, 2026) is an AI co-pilot in the dashboard, opened with **Ask AI** in the upper-right corner.
It is in beta and available to Free plan accounts and select Enterprise customers (as of 2026-10-05).
It answers questions from account data, changes DNS records, zone settings and security rules with approval before execution, can undo its own changes, runs DNS and certificate diagnostics, charts analytics and can open support cases; it was previously called Cloudflare Agent.

Cloudy (https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/) is described as Cloudflare's first AI agent, powered by Workers AI, in beta in WAF, Zero Trust and Analytics.
It respects the logged-in user's RBAC permissions, does not train on customer configuration, and its chat interface can be turned off at **Manage Account > Configurations > Cloudy features**.

## 7. Resources: learning paths, use cases, reference architecture

### 7.1 Learning paths

Sources: https://developers.cloudflare.com/learning-paths/llms.txt and https://developers.cloudflare.com/resources/

The sidebar entry links to the Resources page filtered to learning paths; the Resources page also filters by Design guide, Reference architecture, Reference architecture diagram, Solution guide, Tutorial and Video.
The mirror holds 20 learning paths with 322 pages (counted 2026-10-05):

| Path folder | Pages | Modules (abbreviated) |
| --- | --- | --- |
| `application-security` | 25 | Account security, default traffic security (Browser Integrity, DDoS, DNSSEC, mTLS, SSL/TLS), WAF, Lists, Rate Limiting, Security Center |
| `china-network-overview` | 3 | Accelerate traffic inside and outside mainland China |
| `clientless-access` | 30 | Access applications, Tunnel, App Launcher, clientless Web Isolation |
| `cybersafe` | 20 | Project Cybersafe Schools, CIPA policies, Gateway, Email security |
| `data-center-protection` | 14 | Magic Transit: prefixes, tunnels, routes, Network Firewall, pre-flight checks |
| `dns-best-practices` | 6 | Four-phase DNS migration and DNSSEC re-activation |
| `durable-objects-course` | 8 | Build a WebRTC video call app with Durable Objects and WebSockets |
| `holistic-ai-security` | 16 | Shadow AI, MCP, AI usage policies in Zero Trust |
| `load-balancing` | 22 | Monitors, pools, steering, session affinity |
| `mtls` | 8 | mTLS with Application Security, Access and Workers |
| `prevent-ddos-attacks` | 14 | Baseline and advanced DDoS protection, protect origin IP |
| `r2-intro` | 6 | Public buckets, S3 compatibility, migrating data, Workers access |
| `replace-vpn` | 36 | Access policies, device agent, Gateway |
| `sase-overview-course` | 6 | SASE concepts |
| `secure-internet-traffic` | 47 | DNS, HTTP and egress policies, Browser Isolation |
| `secure-your-email` | 27 | Email security deployment |
| `surge-readiness` | 17 | Caching, security, custom pages and support before traffic spikes |
| `warp-overview-course` | 3 | WARP basics and diagnostic logs |
| `workers` | 10 | Serverless concepts, C3 and Wrangler, first Worker |
| `workflows-course` | 4 | Workflows, batching website data, cron triggers |

### 7.2 Use cases

Source: https://developers.cloudflare.com/use-cases/ (59 pages)

Use cases are organized as "Build something new" (web apps, AI applications, SaaS platforms, APIs and microservices) and "Secure and accelerate your applications" (application security, performance, company security, media and streaming, e-commerce).
Five cross-product solution guides target Free, Pro and Business plans:

- Discover and secure your API endpoints: https://developers.cloudflare.com/use-cases/solutions/discover-secure-api-endpoints/
- Enforce HTTPS and encrypt all traffic: https://developers.cloudflare.com/use-cases/solutions/encrypt-all-keep-site-secure/
- Protect your forms from spam and abuse (Turnstile widget plus mandatory server-side Siteverify; tokens validate once): https://developers.cloudflare.com/use-cases/solutions/protect-sensitive-forms-fraud-abuse/
- Stop account takeover attacks: https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/
- Stop malicious bots while allowing legitimate traffic: https://developers.cloudflare.com/use-cases/solutions/stop-malicious-bots/

Category pages most relevant to app builders: https://developers.cloudflare.com/use-cases/web-apps/, https://developers.cloudflare.com/use-cases/apis/, https://developers.cloudflare.com/use-cases/saas/ and https://developers.cloudflare.com/use-cases/ai/.
The caching use case says content is cached at "300+ Cloudflare edge locations" (https://developers.cloudflare.com/use-cases/performance/caching/).

### 7.3 Reference architecture

Source: https://developers.cloudflare.com/reference-architecture/ (80 pages)

Content types, from https://developers.cloudflare.com/reference-architecture/how-to-use/:

- Reference architectures: high-level conceptual documents (11, including CDN, Load Balancing, Magic Transit, SASE, Cloudflare Security Architecture, AI Security for Apps, and SASE with CrowdStrike, Microsoft and SentinelOne).
- Reference architecture diagrams: one solution or use case each (43 in the index, grouped AI, bots, content delivery, IoT, network, SASE, security, serverless, storage).
- Design guides: prescriptive guidance for architects (9, including ZTNA access policies, SaaS providers, WAF across zones, zero trust for startups).
- Implementation guides: step-by-step deployments, mostly linking into learning paths.

Diagrams most useful for application builders:

- Fullstack applications: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/
- Serverless global APIs: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-global-apis/
- Programmable platforms (Workers for Platforms): https://developers.cloudflare.com/reference-architecture/diagrams/serverless/programmable-platforms/
- Control and data plane pattern for Durable Objects: https://developers.cloudflare.com/reference-architecture/diagrams/storage/durable-object-control-data-plane-pattern/
- Storing user generated content in R2: https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/
- Event notifications for storage: https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/
- Bot management: https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/
- RAG, composable AI, enterprise AI agent workspace, AI vibe coding platform: under https://developers.cloudflare.com/reference-architecture/diagrams/ai/

## 8. API and IaC: SDKs, Terraform, Pulumi

### 8.1 API reference and SDKs

Sources: https://developers.cloudflare.com/api/, https://developers.cloudflare.com/fundamentals/api/reference/sdks/, https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/

The API reference root lists official libraries with their versions (as of 2026-10-05):

| Library | Version shown | Install | Repository |
| --- | --- | --- | --- |
| TypeScript | 7.3.0 | `npm install cloudflare` | https://github.com/cloudflare/cloudflare-typescript |
| Python | 5.9.0 | `pip install cloudflare` | https://github.com/cloudflare/cloudflare-python |
| Go | v7.12.0 | `go get -u github.com/cloudflare/cloudflare-go/v7@v7.12.0` | https://github.com/cloudflare/cloudflare-go |
| Terraform | 5.26.0 | `source = "cloudflare/cloudflare"`, `version = "~> 5.0"` | https://github.com/cloudflare/terraform-provider-cloudflare |

The SDKs page says to use cURL for quick CLI tests and bash or CI scripts, and an SDK inside applications or when chaining outputs.
TypeScript example: `const client = new Cloudflare({ apiToken: process.env["CLOUDFLARE_API_TOKEN"] }); const zones = await client.zones.list();`.
The SDKs automatically honor rate-limit headers and back off (https://developers.cloudflare.com/fundamentals/api/reference/limits/).

SDK support policy: Cloudflare actively supports only the latest major version unless a repo says otherwise; stages are early access, active support and end of life; old versions stay published.
Because the libraries are now generated from OpenAPI, Cloudflare relaxed semantic versioning: minor releases may contain breaking renames of methods, structures or types (Terraform is not changing); pin a known good version or at least the major version.
Full API mechanics are in `api-reference.md`.

### 8.2 Terraform

Sources: https://developers.cloudflare.com/terraform/ (26 pages)

What it is: Cloudflare's Terraform provider (https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) lets you define Cloudflare configuration as code, version it in Git and roll back.
Status: GA; provider 5.26.0 is the version shown on the API reference root (as of 2026-10-05).

Install (https://developers.cloudflare.com/terraform/installing/, updated Oct 2, 2026): `brew tap hashicorp/tap && brew install hashicorp/tap/terraform` on macOS, `sudo apt install terraform` on Linux, the HashiCorp installer on Windows.
The page warns that state breaks if you change the same resources through Terraform and also through the dashboard or API.

Auth: the provider takes `api_token` in the `provider "cloudflare"` block, or reads `CLOUDFLARE_API_TOKEN` from the environment; older examples also use `CLOUDFLARE_EMAIL` and `CLOUDFLARE_API_KEY`.

Minimal v5 configuration from the tutorial (https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/):

```hcl
terraform {
  required_providers {
    cloudflare = { source = "cloudflare/cloudflare", version = "~> 5" }
  }
}
provider "cloudflare" { api_token = "<YOUR_API_TOKEN>" }
resource "cloudflare_dns_record" "www" {
  zone_id = "<YOUR_ZONE_ID>"
  name    = "www"
  content = "203.0.113.10"
  type    = "A"
  ttl     = 1
  proxied = true
}
```

Tutorial sequence: 1 initialize, 2 track history, 3 HTTPS settings, 4 load balancing, 5 Page Rules, 6 revert configuration (https://developers.cloudflare.com/terraform/tutorial/).
Additional configuration guides cover DDoS managed rulesets, rate limiting rules, Transform Rules, WAF custom rules and WAF Managed Rules, plus linked examples for Bulk and Single Redirects, Cache Rules, Configuration Rules, Origin Rules, Snippets and Workers (https://developers.cloudflare.com/workers/platform/infrastructure-as-code/).

Advanced topics:

- Best practices: manage resources only in Terraform; split state by account, zone and product (and Rulesets by phase); use modules sparingly (https://developers.cloudflare.com/terraform/advanced-topics/best-practices/).
- Import: `cf-terraforming` (`brew tap cloudflare/cloudflare && brew install cloudflare/cloudflare/cf-terraforming`) generates config and import commands for existing resources; flags `--email/-e`, `--token/-t`, `--account/-a`, `--zone/-z` (https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/).
- Remote state in R2 with the `s3` backend: `region = "auto"`, `use_path_style = true`, the `skip_*` flags, `endpoints = { s3 = "https://<ACCOUNT_ID>.r2.cloudflarestorage.com" }` and a bucket-scoped R2 token with Object Read and Write (https://developers.cloudflare.com/terraform/advanced-topics/remote-backend/).
- Provider customization through `.tf` parameters or environment variables (https://developers.cloudflare.com/terraform/advanced-topics/provider-customization/).
- How-tos: partial (CNAME) zone and subdomain zone (Enterprise) creation.
- Troubleshooting: 403 when creating DNS records due to wrong zone data, and rule IDs changing in rulesets (use the `ref` field).

### 8.3 Pulumi

Sources: https://developers.cloudflare.com/pulumi/ (7 pages)

What it is: the Pulumi Cloudflare package (https://www.pulumi.com/registry/packages/cloudflare/) provisions Cloudflare in TypeScript, JavaScript, Python, Go, .NET, Java or YAML; Pulumi is Apache 2.0 open source.
Install: `brew install pulumi/tap/pulumi` (macOS), `curl -fsSL https://get.pulumi.com | sh` (Linux), MSI installer (Windows); verify with `pulumi version`.
Auth: a Cloudflare API token; the Hello World tutorial needs `Account-Workers Scripts-Edit`, `Zone-Workers Route-Edit` and `Zone-DNS-Edit`, plus a Pulumi Cloud account (`pulumi login`).
Tutorials:

- Add a site (zone and DNS records with `pulumi new`, `up`, `destroy`): https://developers.cloudflare.com/pulumi/tutorial/add-site/
- Deploy a Worker (script, route, DNS record): https://developers.cloudflare.com/pulumi/tutorial/hello-world/
- Manage secrets with Pulumi ESC: store `CLOUDFLARE_ACCOUNT_ID` and a secret `CLOUDFLARE_API_TOKEN` in an ESC environment and run `esc run <env> npx wrangler whoami`: https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/
- Pulumi plus Wrangler: call Wrangler from Pulumi for Workers and D1 migrations, and use a dynamic resource provider for Vectorize, which the Pulumi provider does not support directly: https://developers.cloudflare.com/pulumi/tutorial/dynamic-provider-and-wrangler/

## 9. Support

Sources: https://developers.cloudflare.com/support/ (121 pages), https://developers.cloudflare.com/support/contacting-cloudflare-support/ (last updated Jul 20, 2026)

Support sections: Contacting Cloudflare Support, Third-Party Software (WordPress, forums, Heroku, Azure egress), Troubleshooting, Cloudflare Status (https://www.cloudflarestatus.com/) and Disruptive Maintenance.

Support channels by plan (as of 2026-10-05):

| Channel | Enterprise | Business | Pro | Free |
| --- | --- | --- | --- | --- |
| Community forum | Yes | Yes | Recommended | Recommended |
| Discord (mainly Developer Platform) | Yes | Yes | Recommended | Recommended |
| Support case | Yes | Yes | Yes | No (billing, account and registrar cases only) |
| Chat | Yes | Yes | No | No |
| Emergency phone | Yes | No | No | No |

Initial response targets: Premium SLA P1 1 hour, P2 2 hours, P3 and P4 24 hours; Enterprise SLA P1 2 hours, P2 4 hours, P3 and P4 48 hours; Pay-as-you-go and Free have no SLA (as of 2026-10-05).
Support cannot change configuration on your behalf, debug your code, or discuss domains not tied to the contacting email; never share API keys with Support.
Emergency phone verification uses a dashboard single-use token (refreshes every 30 seconds) or an authenticator app, plus your Unique Customer ID.

Troubleshooting reference pages (https://developers.cloudflare.com/support/troubleshooting/):

- HTTP status families 1xx to 4xx, with pages for 400 to 451 and 499.
- Cloudflare 1xxx errors, for example 1000 (DNS points to prohibited IP), 1003 (direct IP access), 1015 (rate limited), 1016 (origin DNS error), 1020 (access denied), 1033 (Cloudflare Tunnel error), 1101 (rendering error), 1102 (Worker exceeded resource limits) and 1200 (cache connection limit).
- Cloudflare 10xxx errors (10028 to 10060), which are list and redirect validation errors.
- Cloudflare 5xx errors 500 to 530 and the error diagnostic headers page.
- Restoring original visitor IPs.

Connection timeouts that explain 52x errors (https://developers.cloudflare.com/fundamentals/reference/connection-limits/): complete TCP connection 19 s (522), TCP ACK 90 s (522), proxy idle 900 s (520), proxy read 125 s (524, configurable for Enterprise), proxy write 30 s (524), client keep-alive 400 s.

## 10. Cloudflare CLI (`cf`)

Sources: https://developers.cloudflare.com/cf/ (13 pages, last updated Sep 29 and 30, 2026)

### 10.1 What it is and status

`cf` is "one command-line interface for the public Cloudflare API and for Workers projects".
It is in beta (announced 2026-09-28); commands, configuration and Build Output can change before the stable release (as of 2026-10-05).
It provides more than 2,900 commands, most generated from the API schemas, typed project configuration in `cloudflare.config.ts`, project commands (`cf dev`, `cf build`, `cf deploy`) and local command search (`cf cli search`).
It is the only entry under "Developer Tools" in the sidebar.

### 10.2 Install and requirements

- `npm install --global cf` (or `yarn global add cf`, `pnpm add --global cf`, `bun add --global cf`); update with `cf@latest`.
- The package installs two identical commands, `cf` and `cloudflare` (use `cloudflare` if another `cf` is on PATH).
- Requires Node.js 22.18 or later; Bun is not supported as a runtime because loading `cloudflare.config.ts` fails on Bun.
- A project can add `cf` as a dev dependency; the global `cf` then hands each command to the project's copy so humans, agents and CI run one version (`npx cf@<VERSION>` one-offs are not handed off).
- Shell completion: `cf complete zsh >> ~/.zshrc` (also bash, fish, powershell).

### 10.3 Auth model

Source: https://developers.cloudflare.com/cf/get-started/

- `cf auth login` prints a link and one-time code and opens a browser; `--no-browser` for SSH or containers; `--force` to sign in again; `cf auth whoami` to check.
- `cf` keeps its own credentials and does not reuse a Wrangler login.
- Credential order: `CLOUDFLARE_API_TOKEN` (including from `.env`), then `--profile <NAME>`, then the profile bound to the directory or nearest parent with `cf auth activate`, then the default profile.
- `cf` does not support the Global API Key.
- Named profiles: `cf auth create <name>`, `cf auth activate <name> [dir]`, `cf auth deactivate`, `cf auth list`, `cf auth delete`; these refuse to run while `CLOUDFLARE_API_TOKEN` is set.
- `.env` in the current directory may supply `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_ZONE_ID`, `CLOUDFLARE_COMPLIANCE_REGION`, `CLOUDFLARE_ACCESS_CLIENT_ID` and `CLOUDFLARE_ACCESS_CLIENT_SECRET`; `.env.local` and `.env.<MODE>` are not read; real environment variables win; `--local` commands do not read it; build-first commands read it only after the build.

Account selection order: `CLOUDFLARE_ACCOUNT_ID`, then `accountId` in `cloudflare.config.ts`, then the account saved for the project, then the only accessible account (or a prompt).
The saved choice lives in `cloudflare-account.json` (or `cloudflare-account-<PROFILE>.json`) under `.cache/cloudflare/` in the nearest `node_modules`, or `.cloudflare/cache/` otherwise.
Non-interactive runs fail if more than one account is accessible and none is set; CI output redacts account names.
Zone-scoped commands take `--zone`/`-z` with a zone ID or a domain name; `--zone` beats `CLOUDFLARE_ZONE_ID`.

### 10.4 Using resource commands

Source: https://developers.cloudflare.com/cf/get-started/resources/ and https://developers.cloudflare.com/cf/agents/

```sh
cf zones list --name example.com
cf dns records list --zone example.com --type A
cf dns records create --zone <ZONE_ID> --body '{"type":"A","name":"test","content":"192.0.2.1","proxied":true}' --dry-run
cf dns records delete <RECORD_ID> --zone example.com --force
cf cli search "create D1 database"
cf schema d1 create
```

- Results are JSON on stdout (indented even when piped); progress and messages go to stderr; raw content (R2 objects, AI images) goes to stdout unchanged.
- Lists return one page; paging options differ per command (`--page`, `--per-page` on DNS records).
- `--dry-run` prints `method`, `url`, `pathParams`, `query`, `bodyKind` and `body` as JSON without sending and needs no credentials; use IDs in dry runs because names are not resolved.
- `--body` takes a full JSON request body; some operations accept input only that way.
- `cf cli search "<task>"` returns up to five matches as JSON, runs locally, needs no credentials, and needs the task quoted as one argument.
- `cf schema <command>` prints `operationId`, `httpMethod`, `path`, `pathParams`, `queryParams`, `hasRequestBody` and `requestBodyFields`; nested body fields get combined option names such as `read-replication-mode`.
- Root and group `--help` output reminds agents to use `cf cli search` first; mistyped commands list closest matches.
- Destructive commands prompt with default "no"; in non-interactive runs they print `Aborted.` and exit with status 0, so a zero exit does not prove a deletion.
- On some commands `--force` is also an API parameter, for example `cf workers delete --force` also deletes a Worker that other Workers reference.
- Resource commands use API identifiers (D1 database ID, not name) and act on remote resources; `--local` works only for KV keys and bulk, `cf d1 raw`, `cf d1 migrations list/apply`, R2 objects, and the list commands for D1, KV namespaces and R2 buckets.
- Local data lives in `~/.config/cloudflare/state/v3` (Linux) or `~/Library/Preferences/cloudflare/state/v3` (macOS), shared across projects, or `<DIR>/v3` with `--persist-to`.

### 10.5 Projects: init, dev, build, deploy

Source: https://developers.cloudflare.com/cf/projects/ and https://developers.cloudflare.com/cf/get-started/first-worker/

- `cf init my-worker` creates `src/index.ts`, `cloudflare.config.ts`, `vite.config.ts`, `package.json`, `tsconfig.json`, `.gitignore` and `.cloudflare/types/index.d.ts`; it uses the Cloudflare Vite plugin 2.0 beta (`@cloudflare/vite-plugin@beta`) and does not list Wrangler.
- Non-interactive: `cf init my-worker --package-manager npm` (npm, pnpm, yarn or bun) and `--no-install`.
- `cf init .` configures an existing app; Vite apps work, other frameworks are detected but may not build (Astro 6 and later does not build during the beta).
- `cf` does not run a dev server itself: it runs the framework's own command (only `--mode` is forwarded), or the declared Cloudflare build tool (the Vite plugin, or Wrangler 4.136.0 or later).
- `cf` does not run `package.json` scripts; chain extra steps like `"build": "tsc -b && cf build"`.
- `cf dev` (Vite default `http://localhost:5173/`; set `server.port` in `vite.config.ts`), `cf build` (writes and validates `.cloudflare/output/v0/`, no credentials), `cf deploy`.
- `cf deploy` options: `--dry-run`, `--message`, `--tag`, `--secrets-file`, `--dispatch-namespace`, `--containers-rollout immediate|gradual|none`, `--worker`, `--prebuilt`.
- `cf deploy` can provision missing resources for bindings without IDs, but does not write provisioned IDs back to `cloudflare.config.ts`.
- Modes replace Wrangler environments: `--mode`/`-m`; Vite defaults are `development` for dev and `production` for builds; Wrangler builds and API commands leave mode `undefined`; a function-form config returns one complete config per mode.
- Prebuilt deploys must pass exactly the mode recorded in `.cloudflare/output/v0/config.json` (`buildContext.mode`).
- `cf workers versions create` uploads without deploying (`--preview-alias` for a preview URL alias); `cf workers deployments create --strategy percentage --versions '[...]'` shifts traffic.
- `cf workers triggers deploy` applies routes, custom domains, `workers.dev`, crons, Queue consumers and Workflows without a new version.
- `cf previews deploy [name]` builds with `isPreview: true` and deploys a Worker Preview named after the branch (reads Workers Builds, GitHub Actions `GITHUB_HEAD_REF`/`GITHUB_REF_NAME`, GitLab `CI_COMMIT_REF_NAME`, then Git); no `--dry-run`; Durable Object-managed Containers are not supported in previews.
- `cf workers check` profiles startup locally and writes `worker-startup.cpuprofile`; `cf workers types` writes `.cloudflare/types/index.d.ts`.
- Automatic configuration runs on `cf dev`, `cf build`, `cf deploy` (including `--dry-run`), `cf previews deploy`, `cf workers versions create`, `cf workers triggers deploy`, `cf workers check` and `cf init` when no `cloudflare.config.ts` exists; in CI it applies changes and installs packages without asking.

### 10.6 `cloudflare.config.ts`

Sources: https://developers.cloudflare.com/cf/projects/cloudflare-config/ and https://developers.cloudflare.com/cf/projects/config-explorer/

Programmatic configuration is in open beta (as of 2026-10-05).
It needs Node.js 22.18+, `"type": "module"` in `package.json`, and `cf` as a dev dependency so `import { bindings, defineConfig, triggers, exports } from "cf/config"` resolves.
Import the entrypoint as `import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };` so TypeScript infers bindings and exported classes.

Default export fields: `accountId`, `complianceRegion` (`public` or `fedramp-high`), `worker`, `containers`.
`worker` fields: `name` and `compatibilityDate` (required), `entrypoint` (required for code), `assets`, `cache`, `compatibilityFlags`, `domains`, `env`, `exports`, `limits`, `logpush`, `observability`, `placement`, `previewUrls`, `tailConsumers`, `triggers`, `unsafe`, `workersDev`.
There is no `assets.directory` field; Vite's client build (including `publicDir`) supplies assets, and Wrangler-built projects keep it in a generated `wrangler.config.ts`.

Binding builders (`worker.env`):

| Area | Builders |
| --- | --- |
| Inline values | `text`, `json`, `secret` |
| Storage and data | `d1`, `kv`, `r2`, `hyperdrive`, `analyticsEngineDataset`, `artifacts`, `pipeline` |
| AI and media | `ai`, `aiSearch`, `aiSearchNamespace`, `agentMemory`, `browser`, `images`, `media`, `stream`, `vectorize` |
| Messaging | `queue`, `sendEmail` |
| Worker composition | `assets`, `dispatchNamespace`, `durableObject`, `worker`, `workerLoader`, `workflow` |
| Network and security | `mtlsCertificate`, `rateLimit`, `secretsStoreSecret`, `vpcNetwork`, `vpcService` |
| Platform metadata | `flagship`, `logfwdr`, `versionMetadata` |

Trigger builders (`worker.triggers`): `fetch` (routes), `queue`, `scheduled` (cron), `email` (Email Routing addresses), `connect` (TCP or UDP port; UDP adds `idleTimeoutMs`, `maxPendingBytes`).
Export builders (`worker.exports`): `exports.durableObject({ storage: "sqlite" | "legacy-kv" })` and `exports.workflow(...)`; `worker.exports` replaces Wrangler's ordered `migrations` history, with `state: "renamed"`/`renamedTo` and similar tombstones only for unapplied lifecycle changes.
Cross-Worker bindings accept a Worker name or an imported `defineWorker()` definition (import with the `.ts` extension or Node fails with `ERR_MODULE_NOT_FOUND`).

### 10.7 Migrating from Wrangler

Sources: https://developers.cloudflare.com/cf/wrangler/, https://developers.cloudflare.com/cf/wrangler/migrate/, https://developers.cloudflare.com/cf/wrangler/reference/

| Area | Wrangler | `cf` |
| --- | --- | --- |
| Coverage | Workers and a subset of products | Public API, 2,900+ commands |
| Sign-in | `wrangler login` | `cf auth login` (separate credentials) |
| Config | `wrangler.jsonc` / `wrangler.toml` | `cloudflare.config.ts` |
| Environments | `env` blocks, `--env` | Modes, `--mode` |
| Build | Wrangler bundler | Wrangler bundler or Cloudflare Vite plugin |
| Artifact | Internal | Build Output in `.cloudflare/output/v0/` |
| Output | Tables, `--json` on some | JSON for most API commands |
| IDs | Names for many resources | API IDs |
| Local vs remote | Some commands default to local | Remote; `--local` only for supported KV, D1, R2 |

- You can run `cf` resource commands inside an unmigrated Wrangler project; they ignore the Wrangler file and its `account_id`.
- Never run `cf dev`, `cf build`, `cf deploy` or `cf init .` in a Wrangler project before `cf migrate`; depending on the project they fail, or write a new config that ignores your entrypoint and bindings, and edit `package.json`, lockfile, `.gitignore` and `vite.config.ts`.
- `cf migrate --dry-run` then `cf migrate` writes `cloudflare.config.ts`, keeps names, bindings, IDs, routes and triggers, adds `cf` as a dev dependency, and marks follow-ups as `TODO(@cloudflare)`; the build fails until required items are resolved.
- Manual follow-ups include Durable Object migrations, Workflows, Containers, environments, build settings, source maps, D1 migration settings (pass `--dir`, `--pattern`, `--table`) and secrets; `site` (Workers Sites) is not supported.
- Still needs Wrangler (as of 2026-10-05): live logs (`npx wrangler tail <WORKER_NAME>`) and setting a single secret (`npx wrangler secret put <NAME> --name <WORKER_NAME>`, or `--secrets-file` on `cf deploy`).

### 10.8 CI and agents

Sources: https://developers.cloudflare.com/cf/ci/ and https://developers.cloudflare.com/cf/agents/

GitHub Actions pattern from the docs:

```yaml
env:
  CF_SEND_TELEMETRY: "false"
steps:
  - uses: actions/checkout@v6
  - uses: actions/setup-node@v6
    with: { node-version: 22, cache: npm }
  - run: npm ci
  - run: npx cf build
  - run: npx cf deploy --prebuilt --mode production --dry-run
  - if: github.event_name == 'push'
    run: npx cf deploy --prebuilt --mode production
    env:
      CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
      CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
```

Only the final step receives secrets, so fork pull requests still run the build and dry run.
`cf` treats a run as non-interactive without a terminal or when `CI` is detected: prompts take defaults or fail, destructive commands abort with exit 0, and `cf init` needs a directory.
Commit `cloudflare.config.ts` after running `cf init .` locally, so CI never runs automatic configuration.
Telemetry is anonymous; disable with `CF_SEND_TELEMETRY=false` or `DO_NOT_TRACK=1`.

For coding agents the docs suggest adding this line to a user-level `AGENTS.md` or `CLAUDE.md`: "When interacting with Cloudflare, use the `cf` CLI unless the project has a Wrangler configuration file."
Inside supported agents, `cf dev` also prints the Local Explorer API URL, which lets the agent read and change local binding data and query local traces and logs.

### 10.9 `cf` environment variables

Source: https://developers.cloudflare.com/cf/environment-variables/

| Variable | Effect |
| --- | --- |
| `CLOUDFLARE_API_TOKEN` | Token auth, beats every profile |
| `CLOUDFLARE_ACCOUNT_ID` | Account for account-scoped commands, beats `accountId` |
| `CLOUDFLARE_ZONE_ID` | Default zone (ID or name); `--zone` wins |
| `CLOUDFLARE_COMPLIANCE_REGION` | `public`, `fedramp_high` or `fedramp-high` |
| `CLOUDFLARE_API_BASE_URL` | Override API endpoint (only trusted endpoints) |
| `CLOUDFLARE_ACCESS_CLIENT_ID`, `CLOUDFLARE_ACCESS_CLIENT_SECRET` | Access service token for Access-protected Workers |
| `CLOUDFLARE_REGISTRY_PATH` | Local dev registry shared with Wrangler and Miniflare |
| `TUNNEL_MANAGEMENT_TOKEN` | Existing token for `cf tunnels tail` |
| `CF_SEND_TELEMETRY`, `WRANGLER_SEND_METRICS`, `DO_NOT_TRACK` | Telemetry; `DO_NOT_TRACK=1` always wins |
| `CF_QUIET`, `CF_NO_OSC_PROGRESS`, `CF_FORCE_OSC_PROGRESS`, `NO_COLOR`, `FORCE_COLOR` | Output and progress styling |
| `CI` | Force non-interactive behavior |
| `DEBUG` | Extra diagnostics and stack traces |

Most useful `cf` pages: https://developers.cloudflare.com/cf/get-started/, https://developers.cloudflare.com/cf/agents/, https://developers.cloudflare.com/cf/ci/, https://developers.cloudflare.com/cf/projects/, https://developers.cloudflare.com/cf/projects/cloudflare-config/, https://developers.cloudflare.com/cf/projects/config-explorer/, https://developers.cloudflare.com/cf/wrangler/migrate/, https://developers.cloudflare.com/cf/wrangler/reference/.

## 11. Wrangler

Sources: https://developers.cloudflare.com/workers/wrangler/ (43 pages)

### 11.1 What it is and status

Wrangler is "the Cloudflare Developer Platform command-line interface", used to build, test and deploy Workers projects.
It lives in https://github.com/cloudflare/workers-sdk together with `create-cloudflare` (C3) and Miniflare.
It is GA at major version 4; the highest version referenced in the mirrored docs is 4.145.0 (as of 2026-10-05), and features cite minimum versions such as 3.91.0 (JSON config), 4.102.0 (`--temporary`) and 4.136.0 (minimum for `cf` delegation).
Wrangler commands use the permissions of the authenticated member or API token.

### 11.2 Install

Source: https://developers.cloudflare.com/workers/wrangler/install-and-update/ (last updated Jul 21, 2026)

- Install per project: `npm i -D wrangler@latest` (yarn, pnpm and bun equivalents); run with `npx wrangler <COMMAND>`.
- `npx wrangler` without a local install uses the latest version.
- Supported Node.js: Current, Active LTS and Maintenance LTS; supported OS: macOS 13.5+, Windows 11, Linux with glibc 2.35 (written "glib" on the page).
- New projects usually start with `npm create cloudflare@latest` (C3), which `wrangler init` also calls.

### 11.3 Auth model

Sources: https://developers.cloudflare.com/workers/wrangler/commands/general/, https://developers.cloudflare.com/workers/wrangler/profiles/, https://developers.cloudflare.com/workers/wrangler/system-environment-variables/

- `wrangler login` runs OAuth in the browser with all scopes unless `--scopes` limits them (`--scopes-list` prints them); callback on `localhost:8976` (`--callback-host`, `--callback-port`).
- `wrangler login --device` uses the OAuth 2.0 Device Authorization Grant (RFC 8628): a URL and user code, valid up to 5 minutes, for SSH, containers and Codespaces.
- Credentials default to a plaintext TOML file (typically `~/.config/.wrangler/config/default.toml`); `--use-keyring` stores an AES-256-GCM encrypted `default.enc` with the key in the OS keychain (macOS Keychain, Linux libsecret `secret-tool`, Windows Credential Manager via `@napi-rs/keyring`).
- Authentication profiles (beta): `wrangler auth create <name>`, `wrangler auth activate <name> [dir]`, `--profile` per command, `wrangler auth list`, `deactivate`, `delete`.
- Profile resolution: `CLOUDFLARE_API_TOKEN`, then `--profile`, then nearest activated ancestor directory, then the default profile; account selection uses `account_id` in config or `CLOUDFLARE_ACCOUNT_ID`, else the profile's account; Wrangler never falls back to another account.
- CI uses `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`; legacy `CLOUDFLARE_API_KEY` plus `CLOUDFLARE_EMAIL` is also accepted; old `CF_*` names (`CF_API_TOKEN`, `CF_ACCOUNT_ID`, `CF_API_KEY`, `CF_EMAIL`, `CF_API_BASE_URL`) are listed too.
- Access-protected domains in CI: `CLOUDFLARE_ACCESS_CLIENT_ID` and `CLOUDFLARE_ACCESS_CLIENT_SECRET` (service token) instead of `cloudflared access login`.

Minimum Workers roles for common commands (https://developers.cloudflare.com/workers/authorization/workers/):

| Action | Command | Minimum role |
| --- | --- | --- |
| Tail logs | `wrangler tail` | Metadata Read-Only for that Worker |
| Deploy existing Worker | `wrangler deploy` | Editor for that Worker |
| Change routes or custom domains | `wrangler deploy` | Editor plus Workers Routes Write on each zone |
| Create a new Worker | `wrangler deploy` | Product-level Admin |
| Upload or deploy a version, roll back | `wrangler versions upload/deploy`, `wrangler rollback` | Editor for that Worker |
| Manage secrets | `wrangler secret put/delete` | Editor for that Worker |

### 11.4 Commands

Source: https://developers.cloudflare.com/workers/wrangler/commands/

| Command page | Main commands |
| --- | --- |
| Workers | `init`, `dev`, `deploy`, `preview` (plus `preview delete`, `preview secret`, `preview base-config secret`), `delete`, `setup`, `secret put/delete/list/bulk`, `tail`, `versions upload/deploy/list/view/secret`, `triggers deploy`, `deployments list/status`, `rollback`, `types`, `check startup` |
| General | `docs`, `login`, `logout`, `auth token/create/activate/deactivate/list/delete`, `whoami`, `telemetry disable/enable/status`, `complete` |
| Artifacts | `artifacts namespaces list/get`, `artifacts repos create/list/get/delete/issue-token` |
| Basin Pipelines | `pipelines` commands |
| Browser | `browser create/close/list/view` |
| Certificates | `mtls-certificate`, `cert` |
| Containers | container platform commands |
| D1 | `d1 create/info/list/delete/execute/export`, `d1 time-travel info/restore`, `d1 migrations create/list/apply`, `d1 insights` |
| Flagship | `flagship apps ...`, `flagship flags create/list/get/pull/update/set/rules/split/rollout/enable/disable/evaluate/delete/changelog` |
| Hyperdrive | `hyperdrive create/delete/get/list/update`, `hyperdrive planetscale signature` |
| KV | `kv namespace`, `kv key`, `kv bulk` |
| Pages | `pages dev`, `pages functions build`, `pages project ...`, `pages deployment ...`, `pages deploy`, `pages secret ...`, `pages download config` |
| Queues | `queues list/create/update/delete/info/purge`, consumers (worker and http), `pause-delivery`, `resume-delivery`, `queues subscription ...` |
| R2 | `r2 bucket`, `r2 object`, plus Basin Catalog and Basin SQL subcommands |
| Secrets Store | `secrets-store secret`, `secrets-store store` |
| Tunnel | Cloudflare Tunnel commands |
| Vectorize | `vectorize create/delete/get/list/query/insert/upsert/...`, metadata indexes |
| VPC | `vpc service create/delete/get/list/update` |
| Workers for Platforms | `dispatch-namespace list/get/create/delete/rename` |
| Workflows | `workflows list/describe/delete/trigger`, `workflows instances list/describe/send-event/terminate/restart/pause/resume/delete` |

Global flags on every command: `--help`, `--config` (not Pages), `--cwd`.
Notable `wrangler dev` options: multiple `-c` configs (the first is the primary Worker exposed over HTTP, the rest are reachable only via service bindings), `--port`, `--ip`, `--inspector-port`, `--local-protocol https` with `--https-key-path` and `--https-cert-path`, and `--env`.
`wrangler deploy` in a directory without config auto-detects the framework and configures it (`wrangler setup` configures without deploying); `--temporary` deploys to a claimable temporary account (section 5.6).
`wrangler preview` creates a Preview deployment for branch or PR work, named after the git branch by default, with `--json` output.

### 11.5 Configuration

Source: https://developers.cloudflare.com/workers/wrangler/configuration/ (last updated Oct 2, 2026)

- JSON (`wrangler.json`, `wrangler.jsonc`) is supported since Wrangler 3.91.0; Cloudflare recommends `wrangler.jsonc` for new projects, and some newer features are JSON-only.
- Add `"$schema": "./node_modules/wrangler/config-schema.json"` for editor validation; the sample sets `compatibility_date` to today's date.
- Automatic provisioning: bindings without IDs for KV, R2, D1, Flagship, AI Search, Agent Memory, Dispatch Namespaces and Queues are created on deploy with the Worker name as prefix, and their IDs are written back to the config file (not when deployed from the dashboard via Git).
- Treat the config file as the source of truth: deploys overwrite dashboard vars (unless `keep_vars = true`) and routes; secrets are only deleted by `wrangler secret delete`.
- Sections cover environments, inheritable and non-inheritable keys, routes and custom domains, triggers, observability, limits, every binding type, assets, containers (instance types, SSH), bundling, local dev, secrets, module aliasing, source maps and proxy support.

Environments are documented at https://developers.cloudflare.com/workers/wrangler/environments/; `CLOUDFLARE_ENV` selects one without `--env`.

### 11.6 Wrangler v4 changes

Source: https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/

- Node.js 16 dropped; Wrangler follows the Node.js lifecycle (the page tells v16 and v18 users to act).
- esbuild moved from 0.17.19 to 0.24, so wildcard dynamic imports now bundle every matching file, and esbuild may be bumped in minor versions.
- All commands that can run locally or remotely now default to local and need `--remote` for the API.
- Deprecated commands, flags and config were removed.

### 11.7 Other useful Wrangler references

- Programmatic API (`getPlatformProxy`, `unstable_startWorker`, `unstable_dev`, `createTestHarness`, `experimental_generateTypes`): https://developers.cloudflare.com/workers/wrangler/api/
- System environment variables (for example `WRANGLER_LOG`, `WRANGLER_OUTPUT_FILE_PATH` for ND-JSON deploy output in CI, `CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_<BINDING>`, `WRANGLER_BASIN_SQL_AUTH_TOKEN`): https://developers.cloudflare.com/workers/wrangler/system-environment-variables/
- Bundling and custom builds: https://developers.cloudflare.com/workers/wrangler/bundling/ and https://developers.cloudflare.com/workers/wrangler/custom-builds/
- Deprecations: https://developers.cloudflare.com/workers/wrangler/deprecations/
- CI/CD: https://developers.cloudflare.com/workers/ci-cd/

## 12. Fundamentals

Source: https://developers.cloudflare.com/fundamentals/ (134 pages)

### 12.1 Concepts: user profiles, accounts, zones, organizations

Source: https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/

- A user profile holds personal settings (email, language, communication preferences).
- An account is an organization account with one or more users and zones; it owns billing profiles, members, lists and account-level products such as Workers, Pages, Security Center and Bulk Redirects.
- A zone is a domain or subdomain added to Cloudflare; zone-level services such as Load Balancers and Cache Rules affect only that zone.
- Organizations (public beta, Enterprise and MSSP/Distributor only) are a top-level container over many accounts; Organization Super Administrators have implicit access to all accounts; MSSP structures allow up to 5 levels of nested sub-organizations (https://developers.cloudflare.com/fundamentals/organizations/, as of 2026-10-05).
- Find the account ID with dashboard search "Copy account ID" or Workers & Pages > Account Details; the zone ID is in the API section of the domain Overview page (https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
- Cloudflare is the primary authoritative DNS provider in a full setup; proxied records resolve to Cloudflare anycast IPs (https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/).
- Allow Cloudflare IP ranges (https://www.cloudflare.com/ips/) at the origin (https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/).
- Cloudflare proxies all HTTP methods except `CONNECT`, `TRACE` and `PURGE` (https://developers.cloudflare.com/fundamentals/concepts/traffic-flow-cloudflare/).
- Proxied HTTP ports: 80, 8080, 8880, 2052, 2082, 2086, 2095; HTTPS ports: 443, 2053, 2083, 2087, 2096, 8443; other ports need gray-clouded DNS or Spectrum (all TCP/UDP ports on Enterprise) (https://developers.cloudflare.com/fundamentals/reference/network-ports/).
- The fundamentals overview says Cloudflare serves 55 million HTTP requests per second on average (https://developers.cloudflare.com/fundamentals/).

### 12.2 Members, roles, scopes and policies

Sources: https://developers.cloudflare.com/fundamentals/manage-members/ and subpages

- A policy is actor plus role (PermissionGroup) plus scope (ResourceGroup); a member's effective permissions are the union of direct and User Group policies, and the Members view does not show group-inherited permissions.
- Scopes: account (all domains), specific domains, domain groups (created by a Super Administrator under Settings > Lists > Domain Group Manager), and specific resources (Access apps, IdPs, policies, service tokens, infrastructure targets, Tunnel instances, Mesh nodes).
- Each policy has one scope; a member can have many policies.
- The roles page lists 95 account-scoped, 14 domain-scoped and 9 resource-scoped roles (counted 2026-10-05, last updated Oct 2, 2026).
- Key account roles: Super Administrator - All Privileges (everything, including members, billing, and creating and managing all account-owned API tokens), Administrator (full account and subscriptions but not members or billing profile), Administrator Read Only, API Token Provisioning (create account API tokens), Billing, Workers Editor, Workers Platform Admin, Cloudflare R2 Admin, Turnstile, Secrets Store Admin/Deployer/Reporter, Hyperdrive Admin, Vectorize Admin.
- Key domain roles: Domain Administrator, Domain Administrator Read Only, Domain DNS, Cache Domain Purge, Bot Management, Zone Versioning.
- Dashboard SSO, SCIM provisioning (Okta, Entra, Authentik) and 2FA are documented under https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/ and https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/.

### 12.3 API tokens and keys

Sources: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/, https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/ (updated Sep 28, 2026), https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/, https://developers.cloudflare.com/fundamentals/api/get-started/keys/

| Credential | Owner | Format (new or rolled) | Where to create | Notes |
| --- | --- | --- | --- | --- |
| User API token | A user; acts as that user with a subset of their permissions | `cfut_` + 40 chars + checksum | My Profile > API Tokens | Best for ad hoc scripting; limit 50 per user |
| Account API token | The account (service principal) | `cfat_` + 40 chars + checksum | Manage Account > API Tokens (or Account API tokens) | Best for CI/CD and integrations that outlive a user; limit 500 per account; needs API Token Provisioning role or Super Administrator; GA |
| Global API Key (legacy) | A user; full user permissions | `cfk_` + 40 chars + checksum | My Profile > API Tokens > API Keys | One per user, no scoping, IP or TTL limits; only after email verification; not recommended |
| Origin CA key / Service Key (deprecated) | A user | Starts with `v1.0-` | My Profile > API Tokens > Origin CA Key | `X-Auth-User-Service-Key`; removal date September 30, 2026; replace with a token holding Zone SSL and Certificates Edit |

- Token creation: pick a template or custom token, choose permission groups (User, Account, Zone) at `Read` or `Edit` (Edit is full CRUDL), select resources, optionally restrict by client IP (CIDR `Is in` / `Is not in`) and TTL (`notBefore`/`notAfter`, dates at 00:00 UTC in the dashboard), then copy the secret, which is shown once.
- Verify a user token with `GET https://api.cloudflare.com/client/v4/user/tokens/verify`; account tokens have `GET /accounts/{account_id}/tokens/verify` (see `api-reference.md`); IP filtering does not apply to the verify endpoint.
- Roll a token (dashboard three-dot menu > Roll) to get a new secret with the same permissions; the old secret is invalidated.
- Pre-2026 tokens without prefixes keep working (Global key: 37 to 45 lowercase hex chars; user and account tokens: 40 alphanumeric chars).
- Leaked token detection: GitHub Secret Scanning checks public and private repos; for public repos Cloudflare auto-revokes and emails you, for private repos GitHub notifies you.
- Account token compatibility matrix lists unsupported products as of 2026-10-05: Intel Data Platform, Page Rules, Registrar, Super Bot Fight Mode, Turnstile and Zero Trust Client Platform; everything else in the matrix (including Workers, D1, R2, KV, Queues, Workflows, Workers AI, AI Gateway, DNS, Pages, Hyperdrive, Vectorize, Tunnels) is supported.

Templates (https://developers.cloudflare.com/fundamentals/api/reference/template/): Edit Zone DNS, Read billing info, Read analytics and logs, Edit Cloudflare Workers (Workers Routes, Scripts, KV, Tail, R2, Account Settings Read, User Details and Memberships Read), Edit load balancing configuration, WordPress, Create Additional Tokens (API Tokens Write, the only way to get User > API Tokens > Edit), Read All Resources.

Template URLs (https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/) pre-fill the creation form:

- User token: `https://dash.cloudflare.com/profile/api-tokens?permissionGroupKeys=[ENCODED_JSON]&accountId=*&zoneId=all&name=[NAME]`
- Account token: `https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=[ENCODED_JSON]&name=[NAME]`
- `permissionGroupKeys` is URL-encoded JSON like `[{"key":"dns","type":"edit"},{"key":"analytics","type":"read"}]`, with types `read`, `edit`, `revoke`, `run`, `purge`, and keys such as `workers_scripts`, `workers_kv_storage`, `workers_routes`, `workers_r2`, `account_settings`, `billing`.

Creating tokens via the API (https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/, updated Sep 28, 2026):

- Bootstrap with a dashboard token: Account API Tokens Edit for account tokens, the Create Additional Tokens template for user tokens, Account Settings Edit to invite members.
- A token has one or more policies with `effect` (`allow`/`deny`), `resources` and `permission_groups` (use IDs; names are cosmetic).
- Evaluation order: explicit DENY, then explicit ALLOW, then implicit DENY ALL.
- Resource strings: `com.cloudflare.api.account.<ACCOUNT_ID>`, `com.cloudflare.api.account.*`, `com.cloudflare.api.account.zone.<ZONE_ID>`, all zones in an account as `{"com.cloudflare.api.account.<ACCOUNT_ID>": {"com.cloudflare.api.account.zone.*": "*"}}`, all zones everywhere `com.cloudflare.api.account.zone.*`, and `com.cloudflare.api.user.<USER_TAG>` (yourself only).
- List permission groups: `GET /accounts/$ACCOUNT_ID/tokens/permission_groups` (needs Account API Tokens Read or Write; check `is_selectable`) or `GET /user/tokens/permission_groups`.

Permission catalog (https://developers.cloudflare.com/fundamentals/api/reference/permissions/, updated Oct 1, 2026): 6 user, 173 account and 74 zone permission groups, each printed twice (one table with "Edit" names, one with "Write" names).
Account groups relevant to app builders include Workers Scripts, Workers KV Storage, Workers R2 Storage, Workers Tail, Workers CI, Workers AI, D1, Queues, Pipelines, Vectorize, Hyperdrive, Containers, Pages, Turnstile, Images, Stream, AI Gateway (Read, Run, Edit; account-scoped only), Cloudflare Tunnel, Billing and Account API Tokens.
Zone groups include DNS, Zone, Zone Settings, Cache Purge, SSL and Certificates, Workers Routes, Page Rules, Firewall Services, Zone WAF, Load Balancers, Waiting Rooms, Health Checks, Logs and Web3 Hostnames.

Enterprise Super Administrators can disable API access for the whole account or per member (member setting overrides account setting) (https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/).
Troubleshooting: verify the token is `active`, check permission groups, use `Authorization: Bearer` not the email plus key headers, and remember you cannot create a token that exceeds your own role (https://developers.cloudflare.com/fundamentals/api/troubleshooting/).

### 12.4 API rate limits (summary)

Source: https://developers.cloudflare.com/fundamentals/api/reference/limits/ (last updated Aug 25, 2026)

As of 2026-10-05: 1,200 requests per 5 minutes per user or account token, 200 requests per second per IP, GraphQL up to 320 per 5 minutes by query cost, 50 user tokens per user, 500 account tokens per account.
Exceeding the global limit blocks all calls for the next five minutes with HTTP 429.
Details and headers are in `api-reference.md`.

### 12.5 OAuth applications

Sources: https://developers.cloudflare.com/fundamentals/oauth/ and subpages (updated Aug 2026)

- Available on Free, Pro, Business and Enterprise.
- Create a client at **Manage Account > OAuth clients** (needs Super Administrator, Administrator or "OAuth Client Write"), or `POST /accounts/$ACCOUNT_ID/oauth_clients` with an `OAuth Clients Write` token.
- Scope names correspond to API token permission names; list them with `GET https://api.cloudflare.com/client/v4/oauth/scopes`; `optional_scopes` must be a subset of `scopes`.
- Only the Authorization Code flow is supported for third-party clients: with a client secret (`client_secret_basic` or `client_secret_post`) for servers, or with PKCE `S256` and `token_endpoint_auth_method: none` for browser, mobile, desktop and CLI apps.
- Client Credentials, Implicit, Password and Device Authorization grants are not supported for third-party clients.
- New clients are private (only the parent account's members can authorize); making a client public is permanent and requires name, logo, client URL, scopes and domain verification.
- Endpoints: authorize `https://dash.cloudflare.com/oauth2/auth`, token `/oauth2/token`, revoke `/oauth2/revoke`, logout `/oauth2/logout`, userinfo `/oauth2/userinfo`, JWKS `/.well-known/jwks.json`, OpenID config `/.well-known/openid-configuration` (all on `dash.cloudflare.com`).
- Users review and revoke authorizations in the profile's Manage OAuth authorizations page; account admins can block public OAuth apps under Members > Settings > Public OAuth App access (existing grants are not removed).
- The consent screen marks apps with a green shield (Cloudflare-owned), blue outlined shield (third party, verified domain) or amber shield (unverified).

### 12.6 Plans and billing

Sources: https://developers.cloudflare.com/billing/, https://developers.cloudflare.com/billing/manage/change-plan/, https://developers.cloudflare.com/billing/understand/usage-based-billing/, https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/

- Plans referenced across Fundamentals and Support are Free, Pro, Business and Enterprise (with Enterprise App Sec Advanced and Core variants); the docs point to https://www.cloudflare.com/plans/ for prices.
- Billing runs every 30 days for monthly plans or annually; plans and add-ons are billed separately and some products are usage-based, charged for the previous period.
- Only Super Administrators change a domain plan; upgrades apply immediately, downgrades at period end, no refunds on downgrade; API: the page links the zone plans list method and the zone subscription update method, which in the OpenAPI spec are `GET /zones/{zone_id}/available_plans` and `PUT /zones/{zone_id}/subscription` (send `rate_plan` to change plan or `frequency` to change duration).
- Usage-based products with included usage (as of 2026-10-05): Workers 10M requests and 30M CPU-ms, R2 10 GB storage plus 1M Class A and 10M Class B operations, Load Balancing first 500K DNS queries, Argo first 1 GB; others vary by plan.
- Payment methods: Visa, Mastercard, American Express, Discover, PayPal, Apple Pay, Google Pay, Stripe Link, UnionPay, plus Instant Bank Payments via Link and stablecoins.
- Stablecoin payments: USDC on Base and Polygon via a Stripe-hosted page (`crypto.stripe.com`), with MetaMask, Phantom, Coinbase Wallet and 400+ WalletConnect wallets; a one-time smart contract permit authorizes the first and future charges (renewals, usage-based charges for Workers, R2 and Stream, prorated upgrades); payments are final with no chargebacks; refunds return USDC to the paying wallet; Cloudflare adds no fee and the payer pays gas; a card on file is the fallback (as of 2026-10-05).

### 12.7 API deprecations timeline (recent)

Source: https://developers.cloudflare.com/fundamentals/api/reference/deprecations/

| Posted | Change | Key dates |
| --- | --- | --- |
| 2026-10-02 | Radar top browsers and NetFlows summary endpoints, replaced by `/summary/{dimension}` | EOL April 2, 2027 |
| 2026-07-27 | Zone Settings Batch API (`GET/PATCH /zones/{zone_id}/settings`), use per-setting endpoints | EOL extended to March 31, 2027 |
| 2026-07-27 | Foundation DNS boolean setting | EOL November 23, 2026 |
| 2026-07-22 | Account names limited to 65 characters on create (was silently truncated to 120 bytes) | Enforced September 27, 2026 |
| 2026-07-21 | Account Roles API, use the IAM Permission Groups API | Deprecated July 21, 2026 |
| 2026-07-15 | Workers KV legacy namespace routes | EOL October 15, 2026 |
| 2026-07-09 | Zero Trust networks route endpoints and Tunnel connections field | EOL October 5, 2026 |
| 2026-06-29 | Legacy Registrar domain management API | EOL September 27, 2026 |
| 2026-03-19 | Service Key authentication (`X-Auth-User-Service-Key`) | EOL September 30, 2026 |
| 2026-01-23 | Changing a DNS record's type via the API | EOL June 30, 2026 |

### 12.8 Other reference pages worth knowing

- Glossary: https://developers.cloudflare.com/fundamentals/reference/glossary/
- Cloudflare HTTP headers: https://developers.cloudflare.com/fundamentals/reference/http-headers/
- Ray ID: https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/
- `/cdn-cgi/` endpoint: https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/
- Under Attack mode: https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/
- Scans and penetration testing policy: https://developers.cloudflare.com/fundamentals/reference/scans-penetration/
- Account and domain best practices: https://developers.cloudflare.com/fundamentals/reference/best-practices/
- Protect your origin server: https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/
- Audit Logs v2: https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/
- Zone holds (stop other accounts adding your zones): https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/

## 13. Migration guides

Source: https://developers.cloudflare.com/migration-guides/ (last updated Apr 24, 2026)

The section exists in the sidebar and contains no guides (as of 2026-10-05).
It says: "This section is still in work."
It adds: "Expect more guides soon."
Migration material lives elsewhere: `cf migrate` for Wrangler projects (section 10.7), Wrangler version migrations (https://developers.cloudflare.com/workers/wrangler/migration/), the `cloudflare-one-migrations` skill for VPN and SASE moves, and the DNS migration learning path (https://developers.cloudflare.com/learning-paths/dns-best-practices/).

## 14. Build hooks for Web3 projects

These are ways the tooling above can help launch dapps and token projects on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
None of the Get started or Developer Tools pages mention Solana, Ethereum, Base or Robinhood Chain directly; the chain-specific facts below come from the cited billing, API and x402 pages, and the rest is how the generic tooling applies.

- **Agent-driven deploys of dapp frontends and APIs.** Install the Cloudflare plugin in your coding agent (section 5.1) so it can scaffold Workers for token pages, mint sites or indexer APIs, and use the API MCP server for DNS, WAF and R2 without hand-written API calls.
  For throwaway demos, `wrangler deploy --temporary` gives a live `workers.dev` URL with no account, claimable within the window shown (section 5.6).
- **One CLI for chain-agnostic infra.** `cf` can create the D1 database for allowlists, the KV namespace for token metadata caches, the R2 bucket for NFT media, and the DNS records for a launch domain, all as JSON output that a launch script can pipe through `jq` (section 10.4).
  Use `--dry-run` in launch scripts and never trust exit code 0 on deletes without `--force` (section 10.4).
- **CI that never leaks deploy keys.** Use an account API token (`cfat_`, owned by the account, survives team changes) scoped to the exact permission groups, restricted by CI egress IPs and a TTL, stored as a repo secret, and passed only to the final deploy step (sections 10.8 and 12.3).
  The scannable prefixes mean a token committed to a public GitHub repo is auto-revoked (section 12.3).
- **Separate accounts per chain or per client.** `cf auth activate` and `wrangler auth activate` bind different OAuth profiles to different project directories, and pinning `account_id`/`accountId` prevents deploying a Base build into the Solana project's account (sections 10.3 and 11.3).
- **Reproducible infra for launches.** Terraform v5 or Pulumi can hold the zone, DNS, WAF rate-limit rules and Workers routes for a token launch, with state in R2 (section 8.2); `cf-terraforming` imports a setup first built by hand.
- **Bot and Sybil friction on mints, faucets and airdrops.** The forms solution guide (Turnstile plus server-side Siteverify, single-use tokens) applies directly to claim forms (section 7.2); Turnstile widgets can be managed through the API (see `api-reference.md`), but the account API token matrix lists Turnstile as not yet supported for account-owned tokens, so use a user token there (section 12.3).
- **Agent-readable project docs.** Turn on Markdown for Agents (Pro or Business) for a token's docs site so AI agents and wallets with agent features receive Markdown, and set your own `content-signal` header if you do not want the default `ai-train=yes` (section 4.6).
- **Machine-readable errors for bots and agents.** Without a custom Error Page, agents calling your dapp API get JSON or Markdown Cloudflare errors (for example 1015 rate limited) instead of HTML (section 4.7).
- **Paying Cloudflare in stablecoins.** Cloudflare accepts USDC on Base and Polygon for plans and usage-based Workers, R2 and Stream charges via a one-time permit, which lets a crypto-native project treasury pay infra without a card (section 12.6); Solana, Ethereum mainnet and Robinhood Chain are not listed as supported payment networks.
- **Charging agents for your API or data.** The Directory lists Monetization Gateway (charge visitors for APIs, MCP tools, pages or datasets) and Cloudflare Wallets (wallet handles for agentic payments); the x402 page under Agents lists Base, Ethereum, Solana and other networks for the `exact` scheme and does not list Robinhood Chain (https://developers.cloudflare.com/agents/tools/payments/x402/).
  See `protect-connect/05-monetize.md` for those products.
- **Reference designs to copy.** The "Serverless global APIs", "Fullstack applications", "Storing user generated content" and "Bot management" diagrams map directly onto an RPC proxy, a launchpad backend, NFT media storage and mint-bot defense (section 7.3).

## 15. Gaps and contradictions

- **MCP server lists differ.** The Agent Setup pages list 17 entries (the API server appears twice, as "Code mode API" and "Code Mode server") including "Cloudflare Blog", "Demo Day" and "AutoRAG", while the catalog page lists the API server plus 16 product servers including "Audit Logs", "GraphQL" and "Agents SDK Documentation", and names the autorag endpoint "AI Search server" (https://developers.cloudflare.com/agent-setup/claude-code/ versus https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/).
- **Endpoint counts disagree.** Docs for agents and Agent Setup say the API MCP server covers "over 2,500" or "2,500+" endpoints, the catalog table says 2,594 tools, `cf` says "more than 2,900 commands", and the OpenAPI spec mirrored the same day has 3,647 operations (see `api-reference.md`).
- **Claude Code troubleshooting mentions `mcp-remote`.** The Claude Code guide says to ensure `npx` and `mcp-remote` are available, while the catalog describes native Streamable HTTP at `/mcp` with no proxy; the guides do not reconcile this.
- **Rate limit unit is ambiguous.** The limits table says 1,200 per 5 minutes "per user/account token", while the note under it says the limit applies per user, cumulatively across dashboard, API key and API token traffic (https://developers.cloudflare.com/fundamentals/api/reference/limits/).
- **Edge location counts.** The homepage says the CDN caches in "330+ cities", while the caching use case says "300+ Cloudflare edge locations" (https://developers.cloudflare.com/ versus https://developers.cloudflare.com/use-cases/performance/caching/).
- **Terraform provider versions mixed.** The tutorials say snippets are v5 only and use `cloudflare_dns_record`, while the import page and the R2 backend page say "v4 SDK only" with `version = "~> 4"`, and the best practices page uses the v4 resource name `cloudflare_record`; the API root shows provider 5.26.0.
- **Wrangler `ai` commands.** The homepage shows `npx wrangler ai models`, but the Wrangler commands index has no AI command page.
- **Origin CA keys past end of life.** The Origin CA keys page and the deprecations page set removal for September 30, 2026, which is before this snapshot, yet the page still explains how to view and change the key, and the OpenAPI spec still lists `user_service_key` as an accepted scheme on 83 operations.
- **Legacy Workers roles.** The roles page lists "Workers Platform Admin" and "Workers Platform (Read-only)" as current account roles, while the Workers authorization page calls them legacy roles being replaced (without a deprecation date) (https://developers.cloudflare.com/fundamentals/manage-members/roles/ versus https://developers.cloudflare.com/workers/authorization/workers/).
- **Duplicate role entries.** "Connectivity Directory Admin", "Bind" and "Read" each appear twice in the account-scoped roles table.
- **OAuth Client Write role.** The OAuth page requires "OAuth Client Write" to create clients, but no such role appears in the roles page.
- **Device flow.** The OAuth page says the Device Authorization grant is not supported for third-party clients, while Wrangler (first-party) supports `wrangler login --device`; this is consistent only if first-party clients are exempt, which the pages do not say.
- **Permission names Edit versus Write.** The permissions page prints every group twice, once with "Edit" and once with "Write" names, and the mirror lost the tab labels that explain which naming applies where.
- **Provisioning behavior differs between CLIs.** Wrangler writes auto-provisioned resource IDs back into the config file, while `cf deploy` provisions but does not write IDs back to `cloudflare.config.ts`.
- **Stale timestamps and text.** The API deprecations page says "Last updated Apr 20, 2026" but contains entries dated October 2, 2026; the Cloudy page still says rollouts happen "throughout the rest of 2025".
- **Broken references.** The API overview and OpenAPI description link to `/fundamentals/basic-tasks/interact-with-cloudflare/`, which is not in the mirror, and the OpenAPI description points rate limits to a Workers for Platforms limits page that is also absent.
- **Migration guides empty.** The sidebar's Migration guides section has no guides.
- **Learning paths link.** The sidebar's Learning paths entry is a filtered Resources page, not `/learning-paths/`, so the 322 learning path pages are reachable only through the Resources filter or the per-path URLs.
- **Agent Lee availability.** Agent Lee is available to Free plan accounts and select Enterprise customers, which leaves Pro and Business unaddressed on the page.
- **Plans page.** Fundamentals has no page that compares Free, Pro, Business and Enterprise; prices are only on https://www.cloudflare.com/plans/, which is not part of the docs mirror.
