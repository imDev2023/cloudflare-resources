# Cloudflare GitHub org catalog

This file catalogs the public repositories of the [cloudflare GitHub org](https://github.com/cloudflare) as of 2026-10-05, built from `raw/github/repos.tsv` (all 580 public repos) and the 80 READMEs in `raw/github/readmes/`, plus links counted in the docs mirror `raw/docs/`.
It covers 302 repos: every non-archived repo with 50 or more stars (227) and every repo, archived or not and at any star count, whose name or description matches workers, agents, mcp, sdk, templates, web3, ethereum, ipfs, crypto, wallet, x402 or payments (159 matches, overlapping with the first set).
Repos are grouped by purpose, one line each with stars, primary language, last push date and what it is, taken from the repo description and, where mirrored, the README or the docs page that links it.
For Web3 builders the short answer is that the org has almost no chain-specific code: the useful pieces are the Agents SDK with x402, the `mpp-proxy` payment gate, the real-time stack (Durable Objects, PartyKit, Realtime) and the general Workers toolchain, while the IPFS repos are old forks and monitors.

## Contents

- [Org at a glance](#org-at-a-glance)
- [Most useful for Web3 apps](#most-useful-for-web3-apps)
- [Web3, IPFS and payments](#web3-ipfs-and-payments)
- [Agents and AI](#agents-and-ai)
- [MCP](#mcp)
- [Workers runtime, CLIs and build tooling](#workers-runtime-clis-and-build-tooling)
- [Workers libraries and frameworks](#workers-libraries-and-frameworks)
- [SDKs, API clients, plugins and infrastructure as code](#sdks-api-clients-plugins-and-infrastructure-as-code)
- [Templates and starters](#templates-and-starters)
- [Examples and demos](#examples-and-demos)
- [Networking, proxies and protocols](#networking-proxies-and-protocols)
- [Cryptography, TLS and privacy](#cryptography-tls-and-privacy)
- [Linux, eBPF and observability](#linux-ebpf-and-observability)
- [Systems libraries, data structures, Nginx and Lua](#systems-libraries-data-structures-nginx-and-lua)
- [Frontend and web libraries](#frontend-and-web-libraries)
- [Docs, websites and talks](#docs-websites-and-talks)
- [Archived and legacy](#archived-and-legacy)
- [Notable repos outside the selection rule](#notable-repos-outside-the-selection-rule)
- [Gaps and contradictions](#gaps-and-contradictions)

## Org at a glance

All counts are as of 2026-10-05 from `raw/github/repos.tsv`.

| Measure | Value |
| --- | --- |
| Public repos | 580 |
| Archived | 98 |
| Forks | 77 |
| Non-archived with 50+ stars | 227 |
| Non-archived with 1,000+ stars | 50 |
| Repos covered in this file | 302 |
| Top languages | TypeScript 126, Go 105, JavaScript 102, Rust 65, Python 35, C 33 |
| Last push on 2026-04-23 or 2026-04-24 | 350 |

Top five by stars: `pingora` (27,585), `security-audit-skill` (24,667), `cloudflared` (16,032), `quiche` (12,744), `cloudflare-os` (10,895).
Keyword hits across all 580 repos (name or description): worker 98, agent 17, mcp 4, sdk 7, template 51, web3 1, ethereum 0, ipfs 4, crypto 5, wallet 0, x402 0, payment 0.
No repo name or description mentions ethereum, wallet, x402 or payments; x402 appears only inside the `agents` README, and `mpp-proxy` is described only by the docs.
Each line notes "docs links" when the docs mirror links the repo five or more times, and "README mirrored" when its README is in `raw/github/readmes/`.

## Most useful for Web3 apps

These are the repos most worth knowing for dapps, launchpads, indexers and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
The "why" column says what the source states; the use is the knowledge base's suggestion, not a claim by Cloudflare.

| Repo | What the source says | Use in a Web3 build |
| --- | --- | --- |
| [agents](https://github.com/cloudflare/agents) (5,775 stars) | Agents SDK with x402 payments, MCP, scheduling, WebSockets and SQL on Durable Objects; `x402` and `x402-mcp` examples | Pay-per-call APIs or MCP tools paid via x402; per-user trading bots or launch assistants with their own state and cron |
| [mpp-proxy](https://github.com/cloudflare/mpp-proxy) (65 stars) | Worker that returns `402` with an MPP challenge and forwards after payment | Paywall a price feed, indexer API or token-metadata endpoint without changing the origin |
| [workers-sdk](https://github.com/cloudflare/workers-sdk) (4,602 stars) | Wrangler, C3 and Miniflare | Build, test and deploy every Worker below |
| [templates](https://github.com/cloudflare/templates) (2,140 stars) | Official starter templates | Start a D1, KV, R2 or Durable Object backend for a launchpad quickly |
| [partykit](https://github.com/cloudflare/partykit) (1,279 stars) | PartyServer, PartySocket, Yjs and pubsub on Durable Objects | Live trading rooms, order-book or chat fan-out over WebSockets |
| [workers-chat-demo](https://github.com/cloudflare/workers-chat-demo) (1,120 stars) | One Durable Object per room with WebSockets, history and per-IP rate limits | Reference design for a token chat room with rate limiting |
| [realtimekit-ui](https://github.com/cloudflare/realtimekit-ui) (68 stars) | Pre-built UI components for RealtimeKit | Audio or video rooms for launch events and AMAs |
| [realtime-examples](https://github.com/cloudflare/realtime-examples) (150 stars) | Simpler Realtime (SFU) examples | Starting point for WebRTC rooms |
| [moq-rs](https://github.com/cloudflare/moq-rs) (171 stars) | Rust implementation of IETF MoQ Transport | Low-latency live streams of launches |
| [workers-rs](https://github.com/cloudflare/workers-rs) (3,710 stars) | Write Workers in Rust via WebAssembly | Reuse Rust code (for example Solana-side serialization) inside a Worker |
| [sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) (1,146 stars) | Per-user Linux sandboxes with R2 backups | Run heavier node or CLI tooling that cannot run in a Worker |
| [capnweb](https://github.com/cloudflare/capnweb) (4,009 stars) | Object-capability RPC for the web stack | Typed RPC between a trading UI and its Worker backend |
| [workers-oauth-provider](https://github.com/cloudflare/workers-oauth-provider) (1,879 stars) | OAuth 2.1 for APIs and remote MCP servers | Auth for an MCP server that exposes on-chain data |
| [web-bot-auth](https://github.com/cloudflare/web-bot-auth) (165 stars) | Sign and verify orchestrated HTTP requests | Identify your own agents or bots to protected endpoints |
| [turnstile-demo-workers](https://github.com/cloudflare/turnstile-demo-workers) (266 stars) | Turnstile-protected form on Workers | Bot gate on allowlist, airdrop or waitlist forms |
| [pipelines-starter](https://github.com/cloudflare/pipelines-starter) (13 stars) | Starter for Pipelines, streaming data into R2 | Ingest swap or transfer events into R2 for analytics |
| [workflows-starter](https://github.com/cloudflare/workflows-starter) (50 stars) | Starter for Workflows (durable execution) | Retryable indexer or settlement steps |
| [d1-northwind](https://github.com/cloudflare/d1-northwind) (159 stars) | D1 demo app | Pattern for a SQL-backed trades or holders table |
| [cloudflare-typescript](https://github.com/cloudflare/cloudflare-typescript) (816 stars) | Official TypeScript API client | Provision DNS, Workers and storage from deploy scripts |
| [circl](https://github.com/cloudflare/circl) (1,725 stars) | Post-quantum and elliptic-curve primitives in Go | Crypto primitives for Go services; experimental per README |
| [ipfs-gateway-monitor](https://github.com/cloudflare/ipfs-gateway-monitor) (35 stars) | Measures IPFS gateway performance into Prometheus (blog) | Monitor IPFS gateways serving token metadata |
| [go-ipfs](https://github.com/cloudflare/go-ipfs) (55 stars) | Fork of the Go IPFS implementation | Historic; the live product is the Web3 gateways docs section |
| [cfweb3](https://github.com/cloudflare/cfweb3) (318 stars) | No description or README | Unknown contents; check the repo before relying on it |

Related docs (not repos): the Web3 product with Ethereum and IPFS gateways at https://developers.cloudflare.com/web3/, agentic payments with x402 and MPP at https://developers.cloudflare.com/agents/tools/payments/, and the x402 page of Monetization Gateway at https://developers.cloudflare.com/monetization-gateway/x402/.
The blog mirror also holds the 2026-08-04 post "Announcing Cloudflare Wallets", but as of 2026-10-05 no public repo in the org names wallets.

## Web3, IPFS and payments

Everything in the selection that touches IPFS, Web3 or payments by name, description or docs.
5 repos.

- [cfweb3](https://github.com/cloudflare/cfweb3) (318 stars, JavaScript, pushed 2026-04-23): No description, no topics and no README in the mirror; the name is the only Web3 signal.
- [mpp-proxy](https://github.com/cloudflare/mpp-proxy) (65 stars, TypeScript, pushed 2026-08-14, 5 docs links): No description in repos.tsv. Per the docs it is a Worker template that sits in front of any HTTP backend, answers protected routes with `402` and a Machine Payments Protocol (MPP) challenge, verifies payment, forwards the request and issues a 1-hour session cookie ([docs](https://developers.cloudflare.com/agents/tools/payments/mpp-charge-for-http-content/)).
- [go-ipfs](https://github.com/cloudflare/go-ipfs) (55 stars, Go, pushed 2026-04-24, fork): IPFS implementation in Go. Fork; linked from the blog posts on IPFS safe mode and end-to-end integrity.
- [ipfs-gateway-monitor](https://github.com/cloudflare/ipfs-gateway-monitor) (35 stars, Go, pushed 2026-04-23): No description; the blog post `ipfs-measurements` says it checks the performance of an IPFS gateway and exports it to Prometheus.
- [interface-go-ipfs-core](https://github.com/cloudflare/interface-go-ipfs-core) (1 star, Go, pushed 2026-04-23, fork): Fork; no description.

## Agents and AI

Agent frameworks, AI apps and agent skills.
22 repos.

- [security-audit-skill](https://github.com/cloudflare/security-audit-skill) (24,667 stars, JavaScript, pushed 2026-09-14, README mirrored): A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings. Six-phase audit skill that seeded Cloudflare's vulnerability discovery harness (README).
- [cloudflare-os](https://github.com/cloudflare/cloudflare-os) (10,895 stars, TypeScript, pushed 2026-10-05, README mirrored): Agent workspace built on Cloudflare Workers for creating documents, building apps, and running agents with your company’s context and systems. Agent chat UI plus sandboxed "gadget" app development, used internally by a large portion of Cloudflare's workforce (README).
- [moltworker](https://github.com/cloudflare/moltworker) (9,952 stars, TypeScript, pushed 2026-05-09, README mirrored): Run OpenClaw, (formerly Moltbot, formerly Clawdbot) on Cloudflare Workers. README marks it an experimental proof of concept that needs the Workers Paid plan for Sandbox containers.
- [computer](https://github.com/cloudflare/computer) (9,484 stars, TypeScript, pushed 2026-10-05, 12 docs links, README mirrored): Give your agent a computer. Virtual filesystem inside a Durable Object (SQLite) with a pluggable `workspace.runtime`, one backend being a FUSE mount in a sandbox container (README).
- [agentic-inbox](https://github.com/cloudflare/agentic-inbox) (8,176 stars, TypeScript, pushed 2026-04-23, README mirrored): A self-hosted email client with an AI agent, running entirely on Cloudflare Workers.
- [agents](https://github.com/cloudflare/agents) (5,775 stars, TypeScript, pushed 2026-10-05, 262 docs links, README mirrored): Build and deploy AI Agents on Cloudflare. The Agents SDK: Durable Object backed agents with state sync, `@callable()` RPC, scheduling, WebSockets, AI chat, MCP server and client, Workflows, Email, Voice, Code Mode, sandboxed execution, x402 payments and React hooks; examples include `x402/` and `x402-mcp/` (README).
- [vibesdk](https://github.com/cloudflare/vibesdk) (5,395 stars, TypeScript, pushed 2026-09-22, 14 docs links, README mirrored): An open-source vibe coding platform that helps you build your own vibe-coding platform, built entirely on Cloudflare stack. Live at build.cloudflare.dev; uses Durable Objects, Dynamic Workers, Durable Object Facets and Artifacts (README).
- [skills](https://github.com/cloudflare/skills) (2,988 stars, Shell, pushed 2026-10-01, 41 docs links, README mirrored): Skills for teaching agents how to build on Cloudflare. Agent Skills for Cloudflare, installable as a Codex or Claude plugin together with the Cloudflare MCP server (README).
- [agents-starter](https://github.com/cloudflare/agents-starter) (1,342 stars, TypeScript, pushed 2026-08-19, 18 docs links, README mirrored): A starter kit for building ai agents on Cloudflare. Starter for AI chat agents on the Agents SDK using Workers AI with no API key (README).
- [ai](https://github.com/cloudflare/ai) (1,187 stars, TypeScript, pushed 2026-09-11, 22 docs links, README mirrored): No description; README lists `workers-ai-provider` (Vercel AI SDK), `ai-search-provider` and `@cloudflare/tanstack-ai`.
- [artifact-fs](https://github.com/cloudflare/artifact-fs) (1,167 stars, Go, pushed 2026-09-11, README mirrored): ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical. Git-backed FUSE filesystem daemon that hydrates file contents on demand; part of Cloudflare Artifacts; README calls it a beta release.
- [sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) (1,146 stars, TypeScript, pushed 2026-09-30, 48 docs links, README mirrored): Run sandboxed code environments on Cloudflare's edge network. `@cloudflare/sandbox`: a Durable Object plus Container per user or task, adding `Files`, `S3Mount` and `DirectoryBackup` to R2 (README).
- [agent-skills-discovery-rfc](https://github.com/cloudflare/agent-skills-discovery-rfc) (353 stars, none, pushed 2026-04-23): A mechanism for discovering Agent Skills using the .well-known URI path prefix as specified in RFC 8615 for discovering Agent Skills.
- [claude-managed-agents](https://github.com/cloudflare/claude-managed-agents) (325 stars, TypeScript, pushed 2026-08-12, 13 docs links): No description; the Sandbox docs page "Claude Managed Agents" links it as the template, with D1 migrations and R2 snapshots in its onboarding ([docs](https://developers.cloudflare.com/sandbox/coding-agents/claude-managed-agents/)).
- [cloudflare-os-starter](https://github.com/cloudflare/cloudflare-os-starter) (313 stars, TypeScript, pushed 2026-09-11): A guide for customizing your Cloudflare OS deployment.
- [telescope](https://github.com/cloudflare/telescope) (309 stars, TypeScript, pushed 2026-10-02): Cross-browser web performance testing agent.
- [chatgpt-plugin](https://github.com/cloudflare/chatgpt-plugin) (296 stars, JavaScript, pushed 2026-04-23): Build ChatGPT plugins with Cloudflare's Developer Platform.
- [awesome-agents](https://github.com/cloudflare/awesome-agents) (201 stars, TypeScript, pushed 2026-04-23): Awesome Agents.
- [ai-utils](https://github.com/cloudflare/ai-utils) (197 stars, TypeScript, pushed 2026-06-08): Developer toolkit that makes it simple to build with the Workers AI platform.
- [openai-workers-relay](https://github.com/cloudflare/openai-workers-relay) (161 stars, TypeScript, pushed 2026-04-23): A relay server for OpenAI's realtime API, for Cloudflare Workers.
- [vinext-agents-example](https://github.com/cloudflare/vinext-agents-example) (114 stars, TypeScript, pushed 2026-05-23): vinext ⨉ agents sdk.
- [workers-wonnx](https://github.com/cloudflare/workers-wonnx) (51 stars, Rust, pushed 2026-04-23): No description.

## MCP

Model Context Protocol servers and tooling.
4 repos.

- [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) (4,353 stars, TypeScript, pushed 2026-10-01, 75 docs links, README mirrored): No description; README lists remote servers at `https://<name>.mcp.cloudflare.com/mcp` (docs, bindings, builds, observability, containers, browser, logs, ai-gateway, autorag, dns-analytics, dex, casb, radar, blog, demo-day) and recommends `cloudflare/mcp` for broad API access.
- [mcp](https://github.com/cloudflare/mcp) (922 stars, TypeScript, pushed 2026-10-02, 23 docs links, README mirrored): MCP server for the Cloudflare API. README: "2500 endpoints in 1k tokens" via Code Mode, served at `https://mcp.cloudflare.com/mcp`.
- [workers-mcp](https://github.com/cloudflare/workers-mcp) (647 stars, TypeScript, pushed 2026-04-23, README mirrored): Talk to a Cloudflare Worker from Claude Desktop! README warns to build a remote MCP server instead.
- [playwright-mcp](https://github.com/cloudflare/playwright-mcp) (258 stars, TypeScript, pushed 2026-04-23, 15 docs links): Playwright MCP fork that works with Cloudflare Browser Rendering.

## Workers runtime, CLIs and build tooling

The Workers runtime, Wrangler, language toolchains and deploy tooling.
25 repos.

- [vinext](https://github.com/cloudflare/vinext) (9,087 stars, TypeScript, pushed 2026-10-05, 23 docs links, README mirrored): Vite plugin that reimplements the Next.js API surface - deploy anywhere. README: "Under active development", not yet a drop-in replacement for every Next.js app.
- [workerd](https://github.com/cloudflare/workerd) (8,809 stars, C++, pushed 2026-10-05, 38 docs links, README mirrored): The JavaScript / Wasm runtime that powers Cloudflare Workers. Usable as a self-hosted app server, a local dev tool or a programmable HTTP proxy (README).
- [workers-sdk](https://github.com/cloudflare/workers-sdk) (4,602 stars, TypeScript, pushed 2026-10-05, 181 docs links, README mirrored): Home to Wrangler, the CLI for Cloudflare Workers. Monorepo for `wrangler`, `create-cloudflare` (C3), `miniflare` and Chrome DevTools patches (README).
- [workers-rs](https://github.com/cloudflare/workers-rs) (3,710 stars, Rust, pushed 2026-10-03, 20 docs links, README mirrored): Write Cloudflare Workers in 100% Rust via WebAssembly.
- [wrangler-action](https://github.com/cloudflare/wrangler-action) (1,964 stars, TypeScript, pushed 2026-09-28, README mirrored): easily deploy cloudflare workers applications using wrangler and github actions.
- [forge](https://github.com/cloudflare/forge) (1,029 stars, TypeScript, pushed 2026-10-02, README mirrored): No description; README: schema-first OpenAPI code generation whose first output is the `cf` CLI.
- [cf](https://github.com/cloudflare/cf) (772 stars, TypeScript, pushed 2026-10-05, README mirrored): The agentic CLI for the entire Cloudflare API. README: install "the open beta"; introduces `cloudflare.config.ts` and JSON-first output for agents.
- [ci](https://github.com/cloudflare/ci) (595 stars, TypeScript, pushed 2026-09-14, 5 docs links, README mirrored): Cloudflare-native continuous integration powered by Workflows and Sandbox. `@cloudflare/ci`, a CI engine built on Workflows and Sandbox (README).
- [workers-types](https://github.com/cloudflare/workers-types) (383 stars, TypeScript, pushed 2026-09-09, 5 docs links): TypeScript type definitions for authoring Cloudflare Workers.
- [workerskv.gui](https://github.com/cloudflare/workerskv.gui) (315 stars, Svelte, pushed 2026-04-23): (WIP) A cross-platform Desktop application for exploring Workers KV Namespace data.
- [saffron](https://github.com/cloudflare/saffron) (249 stars, Rust, pushed 2026-04-23): The cron parser powering Cron Triggers on Cloudflare Workers.
- [html-rewriter-wasm](https://github.com/cloudflare/html-rewriter-wasm) (219 stars, TypeScript, pushed 2026-04-23): WebAssembly version of HTMLRewriter.
- [serverless-cloudflare-workers](https://github.com/cloudflare/serverless-cloudflare-workers) (181 stars, JavaScript, pushed 2026-04-23): Serverless provider plugin for Cloudflare Workers.
- [workers-wasi](https://github.com/cloudflare/workers-wasi) (159 stars, C++, pushed 2026-04-23): No description.
- [serverless-action](https://github.com/cloudflare/serverless-action) (125 stars, Dockerfile, pushed 2026-04-23): No description.
- [workers-py](https://github.com/cloudflare/workers-py) (119 stars, Python, pushed 2026-10-01, 10 docs links): Write Cloudflare Workers in 100% Python via Pyodide.
- [homebrew-cloudflare](https://github.com/cloudflare/homebrew-cloudflare) (118 stars, Ruby, pushed 2026-09-27): No description.
- [deploy.workers.cloudflare.com](https://github.com/cloudflare/deploy.workers.cloudflare.com) (78 stars, JavaScript, pushed 2026-04-23): Deploy Cloudflare Workers applications with (almost) no-config, using GitHub Actions.
- [wasm-coredump](https://github.com/cloudflare/wasm-coredump) (46 stars, Rust, pushed 2026-04-23): Cloudflare Workers Wasm Coredump Service.
- [managed-component-to-cloudflare-worker](https://github.com/cloudflare/managed-component-to-cloudflare-worker) (27 stars, TypeScript, pushed 2026-04-23): Deploy Managed Components as Cloudflare Workers and use them in Cloudflare Zaraz.
- [lasso](https://github.com/cloudflare/lasso) (16 stars, JavaScript, pushed 2026-04-23): A Worker that caches wrangler's binary dependencies, so you can install wrangler if NPM or GitHub are having a bad day.
- [workers-nodejs-compat-matrix](https://github.com/cloudflare/workers-nodejs-compat-matrix) (16 stars, JavaScript, pushed 2026-06-14): https://workers-nodejs-compat-matrix.pages.dev.
- [workerd-cxx](https://github.com/cloudflare/workerd-cxx) (11 stars, Rust, pushed 2026-08-13, fork): workerd-cxx is a fork of cxx crate for workerd/edgeworker project.
- [workerd-tools](https://github.com/cloudflare/workerd-tools) (8 stars, CMake, pushed 2026-10-04): Prebuilt tools and utilities required for ongoing development in the workerd repo.
- [pyodide-build-scripts](https://github.com/cloudflare/pyodide-build-scripts) (6 stars, Python, pushed 2026-04-23): Automated build processes for Cloudflare Workers Pyodide distribution.

## Workers libraries and frameworks

Libraries that run inside Workers or wrap Workers features.
16 repos.

- [capnweb](https://github.com/cloudflare/capnweb) (4,009 stars, TypeScript, pushed 2026-10-05, README mirrored): JavaScript/TypeScript-native, low-boilerplate, object-capability RPC system. Cap'n Web, an object-capability RPC protocol by the author of Cap'n Proto (README).
- [workers-oauth-provider](https://github.com/cloudflare/workers-oauth-provider) (1,879 stars, TypeScript, pushed 2026-10-05, 103 docs links, README mirrored): OAuth provider library for Cloudflare Workers. OAuth 2.1 for HTTP APIs and remote MCP servers; needs a KV namespace bound as `OAUTH_KV` (README).
- [partykit](https://github.com/cloudflare/partykit) (1,279 stars, TypeScript, pushed 2026-08-03, README mirrored): PartyKit, for Workers. PartyServer, PartySocket, Y-PartyServer (Yjs) and partysub for real-time apps on Durable Objects (README).
- [chanfana](https://github.com/cloudflare/chanfana) (766 stars, TypeScript, pushed 2026-08-31, README mirrored): OpenAPI 3 and 3.1 schema generator and validator for Hono, itty-router and more!
- [actors](https://github.com/cloudflare/actors) (427 stars, TypeScript, pushed 2026-04-23, 21 docs links, README mirrored): An easier way to build with Cloudflare Durable Objects. README: "in active development".
- [puppeteer](https://github.com/cloudflare/puppeteer) (376 stars, TypeScript, pushed 2026-10-01, 13 docs links): Puppeteer Core fork that works with Cloudflare Browser Workers.
- [containers](https://github.com/cloudflare/containers) (270 stars, TypeScript, pushed 2026-08-24): Enhance your Workers with serverless containers.
- [stream-react](https://github.com/cloudflare/stream-react) (198 stars, TypeScript, pushed 2026-04-23): No description.
- [playwright](https://github.com/cloudflare/playwright) (124 stars, TypeScript, pushed 2026-09-22, 23 docs links): Playwright fork that works with Cloudflare Browser Rendering.
- [workers-honeycomb-logger](https://github.com/cloudflare/workers-honeycomb-logger) (84 stars, TypeScript, pushed 2026-04-23): A library to easily send request events and traces to https://honeycomb.io.
- [flagship](https://github.com/cloudflare/flagship) (71 stars, TypeScript, pushed 2026-10-05, 6 docs links): OpenFeature compliant provider for Cloudflare's low-latency feature flag platform.
- [realtimekit-ui](https://github.com/cloudflare/realtimekit-ui) (68 stars, TypeScript, pushed 2026-10-05): RealtimeKit UI provides pre-built, ready-to-use UI components for integrating with Cloudflare RealtimeKit.
- [pages-plugins](https://github.com/cloudflare/pages-plugins) (62 stars, TypeScript, pushed 2026-04-23): No description.
- [worker-sentry](https://github.com/cloudflare/worker-sentry) (52 stars, JavaScript, pushed 2026-04-23): Sentry over Access for Worker.
- [workers-google-analytics](https://github.com/cloudflare/workers-google-analytics) (38 stars, JavaScript, pushed 2026-04-23): Middleware for Google Analytics tracking in Workers.
- [cabidela](https://github.com/cloudflare/cabidela) (29 stars, TypeScript, pushed 2026-09-08): Cabidela is a small, fast, eval-less, Cloudflare Workers compatible, dynamic JSON Schema validator.

## SDKs, API clients, plugins and infrastructure as code

Cloudflare API clients, Terraform, CMS plugins and other integrations.
17 repos.

- [cloudflare-go](https://github.com/cloudflare/cloudflare-go) (2,097 stars, Go, pushed 2026-10-01, 52 docs links, README mirrored): The official Go library for the Cloudflare API. Generated with Stainless (README).
- [cf-terraforming](https://github.com/cloudflare/cf-terraforming) (1,407 stars, Go, pushed 2026-10-04, 11 docs links, README mirrored): A command line utility to facilitate terraforming your existing Cloudflare resources.
- [terraform-provider-cloudflare](https://github.com/cloudflare/terraform-provider-cloudflare) (1,342 stars, Go, pushed 2026-10-03, 1152 docs links, README mirrored): Cloudflare Terraform Provider.
- [cloudflare-typescript](https://github.com/cloudflare/cloudflare-typescript) (816 stars, TypeScript, pushed 2026-10-03, 129 docs links, README mirrored): The official TypeScript library for the Cloudflare API. Generated with Stainless (README).
- [cloudflare-php](https://github.com/cloudflare/cloudflare-php) (674 stars, PHP, pushed 2026-06-18, README mirrored): PHP library for the Cloudflare v4 API. README calls it community-maintained and covering a subset of the API.
- [cloudflare-python](https://github.com/cloudflare/cloudflare-python) (511 stars, Python, pushed 2026-10-03, 59 docs links, README mirrored): The official Python library for the Cloudflare API. Generated with Stainless; sync and async clients (README).
- [origin-ca-issuer](https://github.com/cloudflare/origin-ca-issuer) (335 stars, Go, pushed 2026-09-25, 6 docs links): cert-manager issuer for Origin CA.
- [cloudflare-rs](https://github.com/cloudflare/cloudflare-rs) (318 stars, Rust, pushed 2026-04-23): Rust library for the Cloudflare v4 API.
- [mod_cloudflare](https://github.com/cloudflare/mod_cloudflare) (262 stars, C, pushed 2026-04-24, 6 docs links): No description.
- [Cloudflare-WordPress](https://github.com/cloudflare/Cloudflare-WordPress) (248 stars, PHP, pushed 2026-08-08): A Cloudflare plugin for WordPress.
- [api-schemas](https://github.com/cloudflare/api-schemas) (193 stars, none, pushed 2026-10-05): No description, no language.
- [helm-charts](https://github.com/cloudflare/helm-charts) (142 stars, Smarty, pushed 2026-04-23): No description; topics cloudflare, helm, kubernetes.
- [logshare](https://github.com/cloudflare/logshare) (81 stars, Go, pushed 2026-04-24): logshare is a library & CLI client for retrieving logs from Cloudflare's Enterprise Log Share service.
- [cloudflare-access-for-atlassian](https://github.com/cloudflare/cloudflare-access-for-atlassian) (52 stars, Java, pushed 2026-04-24): Authenticate Atlasssian products when using Cloudflare Access.
- [Cloudflare-Magento](https://github.com/cloudflare/Cloudflare-Magento) (52 stars, PHP, pushed 2026-04-24): A Cloudflare plugin for Magento2.
- [cloudflare-plugin-frontend](https://github.com/cloudflare/cloudflare-plugin-frontend) (36 stars, JavaScript, pushed 2026-04-24): A React/Redux front-end for Cloudflare's WordPress, Magento2, and cPanel plugins.
- [cf-product-infrastructure-templates](https://github.com/cloudflare/cf-product-infrastructure-templates) (3 stars, HCL, pushed 2026-04-23): Collection of infrastructure as code templates to aid in customer onboarding to Cloudflare products that require customer-side resources.

## Templates and starters

Starter templates; many date from older Wrangler versions.
57 repos.

- [templates](https://github.com/cloudflare/templates) (2,140 stars, TypeScript, pushed 2026-09-30, 72 docs links, README mirrored): Templates for Cloudflare Workers. Starter templates usable from the dashboard or `create-cloudflare` (README).
- [worker-typescript-template](https://github.com/cloudflare/worker-typescript-template) (448 stars, TypeScript, pushed 2026-04-23, README mirrored): TypeScript template for Cloudflare Workers. README: "This template is no longer maintained".
- [rustwasm-worker-template](https://github.com/cloudflare/rustwasm-worker-template) (385 stars, Rust, pushed 2026-04-23): A template for kick starting a Cloudflare Worker project using workers-rs. Write your Cloudflare Worker entirely in Rust!
- [python-worker-hello-world](https://github.com/cloudflare/python-worker-hello-world) (276 stars, JavaScript, pushed 2026-04-23): Python hello world for Cloudflare Workers.
- [worker-template-router](https://github.com/cloudflare/worker-template-router) (240 stars, JavaScript, pushed 2026-04-23): No description.
- [worker-speedtest-template](https://github.com/cloudflare/worker-speedtest-template) (218 stars, JavaScript, pushed 2026-04-23): No description.
- [worker-template](https://github.com/cloudflare/worker-template) (217 stars, JavaScript, pushed 2026-04-23): a template to kickstart your Cloudflare worker!
- [websocket-template](https://github.com/cloudflare/websocket-template) (133 stars, JavaScript, pushed 2026-04-23): Example template for working with the WebSocketPair API in Cloudflare Workers.
- [php-worker-hello-world](https://github.com/cloudflare/php-worker-hello-world) (132 stars, PHP, pushed 2026-04-23): No description.
- [workers-aws-template](https://github.com/cloudflare/workers-aws-template) (128 stars, JavaScript, pushed 2026-04-23): Cloudflare Workers template for accessing AWS services such as DynamoDB and SQS.
- [vibesdk-templates](https://github.com/cloudflare/vibesdk-templates) (95 stars, TypeScript, pushed 2026-05-13): Official repository for templates catalog powering VibeSDK.
- [worker-template-postgres](https://github.com/cloudflare/worker-template-postgres) (94 stars, JavaScript, pushed 2026-04-23): Reference demo and modified PostgreSQL driver to connect Cloudflare Workers to a relational database.
- [worker-sites-template](https://github.com/cloudflare/worker-sites-template) (79 stars, HTML, pushed 2026-04-23): No description.
- [kotlin-worker-hello-world](https://github.com/cloudflare/kotlin-worker-hello-world) (70 stars, Kotlin, pushed 2026-04-23): No description.
- [worker-emscripten-template](https://github.com/cloudflare/worker-emscripten-template) (68 stars, JavaScript, pushed 2026-04-23): No description.
- [cobol-worker-template](https://github.com/cloudflare/cobol-worker-template) (64 stars, JavaScript, pushed 2026-04-23): A Cloudflare worker that runs COBOL.
- [template-registry](https://github.com/cloudflare/template-registry) (62 stars, TypeScript, pushed 2026-04-23): A simple API via a Worker that serves all the template content.
- [worker-template-mysql](https://github.com/cloudflare/worker-template-mysql) (61 stars, JavaScript, pushed 2026-04-23): Reference demo and modified MySQL driver to connect Cloudflare Workers to a relational database.
- [durable-objects-template](https://github.com/cloudflare/durable-objects-template) (60 stars, JavaScript, pushed 2026-04-23): No description.
- [workflows-starter](https://github.com/cloudflare/workflows-starter) (50 stars, TypeScript, pushed 2026-04-23): A starter template for Cloudflare Workflows.
- [react-workers-template](https://github.com/cloudflare/react-workers-template) (47 stars, JavaScript, pushed 2026-04-23): Example project showing how to deploy your React application to Cloudflare Workers Sites.
- [dart-worker-hello-world](https://github.com/cloudflare/dart-worker-hello-world) (41 stars, Dart, pushed 2026-04-23): Dart hello world for Cloudflare Workers.
- [durable-objects-rollup-esm](https://github.com/cloudflare/durable-objects-rollup-esm) (32 stars, JavaScript, pushed 2026-04-23): Template for durable objects, rollup, es modules.
- [scala-worker-hello-world](https://github.com/cloudflare/scala-worker-hello-world) (24 stars, Scala, pushed 2026-04-23): Scala hello world for Cloudflare Workers.
- [durable-objects-webpack-commonjs](https://github.com/cloudflare/durable-objects-webpack-commonjs) (22 stars, JavaScript, pushed 2026-04-23): Template for durable objects, webpack, commonjs.
- [reason-worker-hello-world](https://github.com/cloudflare/reason-worker-hello-world) (21 stars, Reason, pushed 2026-04-23): Reason hello world for Cloudflare Workers.
- [worker-template-fetch](https://github.com/cloudflare/worker-template-fetch) (20 stars, JavaScript, pushed 2026-04-23): No description.
- [react-router-hono-fullstack-template](https://github.com/cloudflare/react-router-hono-fullstack-template) (19 stars, TypeScript, pushed 2026-04-23): No description.
- [worker-template-static](https://github.com/cloudflare/worker-template-static) (16 stars, JavaScript, pushed 2026-04-23): No description.
- [access-crl-worker-template](https://github.com/cloudflare/access-crl-worker-template) (13 stars, JavaScript, pushed 2026-04-23): A worker that can be used for doing basic CRL checks. It assumes that the request has gone through Access MTLS.
- [pipelines-starter](https://github.com/cloudflare/pipelines-starter) (13 stars, TypeScript, pushed 2026-04-23): Starter template for Cloudflare Pipelines, which let you ingest real time data streams and load into R2.
- [llm-chat-app-template](https://github.com/cloudflare/llm-chat-app-template) (12 stars, JavaScript, pushed 2026-04-23): No description.
- [perl-worker-hello-world](https://github.com/cloudflare/perl-worker-hello-world) (12 stars, Perl, pushed 2026-04-23): No description.
- [worker-template-redirect](https://github.com/cloudflare/worker-template-redirect) (10 stars, JavaScript, pushed 2026-04-23): No description.
- [durable-chat-template](https://github.com/cloudflare/durable-chat-template) (9 stars, TypeScript, pushed 2026-04-23): No description.
- [service-worker-custom-build](https://github.com/cloudflare/service-worker-custom-build) (9 stars, JavaScript, pushed 2026-04-23): Template for webpack-based custom build of a service worker.
- [modules-rollup-esm](https://github.com/cloudflare/modules-rollup-esm) (8 stars, JavaScript, pushed 2026-04-23): Template for modules, rollup, es modules.
- [modules-webpack-commonjs](https://github.com/cloudflare/modules-webpack-commonjs) (5 stars, JavaScript, pushed 2026-04-23): Template for modules, webpack, commonjs.

Low-star template copies (19): these have 0 to 5 stars, mostly no description, and names with numeric or personal suffixes, which suggests test or generated copies rather than maintained templates.

- [vite-react-template-bray](https://github.com/cloudflare/vite-react-template-bray) (5 stars, TypeScript, pushed 2026-04-23): No description.
- [llm-chat-app-template-brayden](https://github.com/cloudflare/llm-chat-app-template-brayden) (4 stars, JavaScript, pushed 2026-04-23): No description.
- [r2-explorer-template123](https://github.com/cloudflare/r2-explorer-template123) (4 stars, TypeScript, pushed 2026-04-23): No description.
- [astro-blog-starter-template-brayden](https://github.com/cloudflare/astro-blog-starter-template-brayden) (3 stars, Astro, pushed 2026-04-23): No description.
- [astro-blog-starter-template-brayden1](https://github.com/cloudflare/astro-blog-starter-template-brayden1) (3 stars, Astro, pushed 2026-04-23): No description.
- [chanfana-openapi-template-11](https://github.com/cloudflare/chanfana-openapi-template-11) (2 stars, TypeScript, pushed 2026-04-23): No description.
- [to-do-list-kv-template-100](https://github.com/cloudflare/to-do-list-kv-template-100) (2 stars, TypeScript, pushed 2026-04-23): No description.
- [worker-sites-init](https://github.com/cloudflare/worker-sites-init) (2 stars, JavaScript, pushed 2026-04-23): tropical irradiation.
- [d1-template-333](https://github.com/cloudflare/d1-template-333) (1 star, TypeScript, pushed 2026-04-23): No description.
- [openauth-template-24](https://github.com/cloudflare/openauth-template-24) (1 star, TypeScript, pushed 2026-04-23): No description.
- [r2-explorer-template-9](https://github.com/cloudflare/r2-explorer-template-9) (1 star, TypeScript, pushed 2026-04-23): No description.
- [to-do-list-kv-template99](https://github.com/cloudflare/to-do-list-kv-template99) (1 star, TypeScript, pushed 2026-04-23): No description.
- [vite-react-template-brayden](https://github.com/cloudflare/vite-react-template-brayden) (1 star, TypeScript, pushed 2026-04-23): No description.
- [d1-template-123](https://github.com/cloudflare/d1-template-123) (0 stars, TypeScript, pushed 2026-04-23): No description.
- [d1-template-12344](https://github.com/cloudflare/d1-template-12344) (0 stars, TypeScript, pushed 2026-04-23): No description.
- [d1-template-666](https://github.com/cloudflare/d1-template-666) (0 stars, TypeScript, pushed 2026-04-23): No description.
- [d1-template-777](https://github.com/cloudflare/d1-template-777) (0 stars, TypeScript, pushed 2026-04-23): No description.
- [d1-template-888](https://github.com/cloudflare/d1-template-888) (0 stars, TypeScript, pushed 2026-04-23): No description.
- [to-do-list-kv-template-123](https://github.com/cloudflare/to-do-list-kv-template-123) (0 stars, TypeScript, pushed 2026-04-23): No description.

## Examples and demos

Demo apps and reference examples.
41 repos.

- [meet](https://github.com/cloudflare/meet) (2,314 stars, TypeScript, pushed 2026-04-23, 5 docs links, README mirrored): No description; README: Cloudflare Meet (formerly Orange Meets), a demo app built on Realtime SFU.
- [wildebeest](https://github.com/cloudflare/wildebeest) (2,113 stars, TypeScript, pushed 2026-04-23, README mirrored): Wildebeest is an ActivityPub and Mastodon-compatible server. README says the project is archived and no longer maintained.
- [serverless-registry](https://github.com/cloudflare/serverless-registry) (1,462 stars, TypeScript, pushed 2026-09-11, README mirrored): A container registry backed by Workers and R2. Supports push and pull plus username/password and JWT auth (README).
- [workers-chat-demo](https://github.com/cloudflare/workers-chat-demo) (1,120 stars, JavaScript, pushed 2026-04-23, 5 docs links, README mirrored): No description; README: Edge Chat Demo, one Durable Object per room over WebSockets, with history and per-IP rate limiting.
- [workers-graphql-server](https://github.com/cloudflare/workers-graphql-server) (794 stars, TypeScript, pushed 2026-04-23, README mirrored): Lightning-fast, globally distributed Apollo GraphQL server, deployed at the edge using Cloudflare Workers.
- [workers-for-platforms-example](https://github.com/cloudflare/workers-for-platforms-example) (451 stars, TypeScript, pushed 2026-04-23, README mirrored): A great place for platforms to get started on Cloudflare Workers! Minimal dynamic dispatch example (README).
- [doom-wasm](https://github.com/cloudflare/doom-wasm) (413 stars, C, pushed 2026-04-23, README mirrored): Chocolate Doom WebAssembly port with WebSockets support.
- [cobweb](https://github.com/cloudflare/cobweb) (402 stars, COBOL, pushed 2026-04-23): COBOL to WebAssembly compiler.
- [python-workers-examples](https://github.com/cloudflare/python-workers-examples) (335 stars, Python, pushed 2026-09-28, 9 docs links): No description.
- [turnstile-demo-workers](https://github.com/cloudflare/turnstile-demo-workers) (266 stars, HTML, pushed 2026-04-23): A simple demo with a Turnstile-protected form, using Cloudflare Workers.
- [argo-tunnel-examples](https://github.com/cloudflare/argo-tunnel-examples) (245 stars, HCL, pushed 2026-04-23): No description.
- [workers-web-experiments](https://github.com/cloudflare/workers-web-experiments) (222 stars, TypeScript, pushed 2026-04-23): Public web experiments by the Cloudflare Workers team.
- [containers-demos](https://github.com/cloudflare/containers-demos) (213 stars, TypeScript, pushed 2026-09-28): No description.
- [doom](https://github.com/cloudflare/doom) (201 stars, JavaScript, pushed 2026-05-27): Website and Message Router source code for the Multiplayer Doom on Cloudflare Workers tech demo.
- [dmarc-email-worker](https://github.com/cloudflare/dmarc-email-worker) (169 stars, TypeScript, pushed 2026-04-23): DMARC reports processor using Cloudflare Workers and Email Workers.
- [d1-northwind](https://github.com/cloudflare/d1-northwind) (159 stars, TypeScript, pushed 2026-06-11): Northwind Traders D1 Demo.
- [cloudflare-workers-wasm-demo](https://github.com/cloudflare/cloudflare-workers-wasm-demo) (154 stars, C, pushed 2026-04-23): No description.
- [realtime-examples](https://github.com/cloudflare/realtime-examples) (150 stars, TypeScript, pushed 2026-09-22, 54 docs links): No description; the `meet` README points to it for simpler Realtime examples.
- [images.pages.dev](https://github.com/cloudflare/images.pages.dev) (127 stars, TypeScript, pushed 2026-04-23): No description.
- [receipt-printer](https://github.com/cloudflare/receipt-printer) (97 stars, Python, pushed 2026-04-24): Code to drive the receipt printer in the Cloudflare London office that outputs randomness.
- [ecommerce-bundles-workers-example](https://github.com/cloudflare/ecommerce-bundles-workers-example) (90 stars, Vue, pushed 2026-04-23): No description.
- [miniflare-typescript-esbuild-jest](https://github.com/cloudflare/miniflare-typescript-esbuild-jest) (89 stars, TypeScript, pushed 2026-04-23): Example project using Miniflare, TypeScript, esbuild and Jest.
- [workers-react-pwa-example](https://github.com/cloudflare/workers-react-pwa-example) (86 stars, JavaScript, pushed 2026-04-23): No description.
- [workers-graphql-gateway-example](https://github.com/cloudflare/workers-graphql-gateway-example) (85 stars, JavaScript, pushed 2026-04-23): GraphQL running on Cloudflare Workers.
- [workers-airtable-form](https://github.com/cloudflare/workers-airtable-form) (75 stars, JavaScript, pushed 2026-04-23): Example codebase showing how to handle form data using Cloudflare Workers serverless functions - sending the data to Airtable.
- [js-rpc-and-entrypoints-demo](https://github.com/cloudflare/js-rpc-and-entrypoints-demo) (72 stars, TypeScript, pushed 2026-04-23): No description.
- [postgres-postgrest-cloudflared-example](https://github.com/cloudflare/postgres-postgrest-cloudflared-example) (71 stars, none, pushed 2026-04-23): Create a PostgreSQL database with a REST API, exposed to the internet securely with Cloudflare Tunnel.
- [realtimekit-web-examples](https://github.com/cloudflare/realtimekit-web-examples) (70 stars, TypeScript, pushed 2026-09-28, 22 docs links): Web examples for Cloudflare RealtimeKit.
- [cf-identity-dynamic](https://github.com/cloudflare/cf-identity-dynamic) (65 stars, JavaScript, pushed 2026-04-27): A highly customizable block page built in Cloudflare Workers that provides enriched Access Deny reasoning to end users.
- [cobol-worker](https://github.com/cloudflare/cobol-worker) (41 stars, COBOL, pushed 2026-04-23): No description.
- [workers-webpack-example](https://github.com/cloudflare/workers-webpack-example) (33 stars, JavaScript, pushed 2026-04-24): An example of building a Cloudflare Worker with Webpack.
- [workers-access-external-auth-example](https://github.com/cloudflare/workers-access-external-auth-example) (30 stars, JavaScript, pushed 2026-04-23): No description.
- [worker-performance-examples](https://github.com/cloudflare/worker-performance-examples) (27 stars, JavaScript, pushed 2026-04-24): Scripts which can be used to test the performance of various providers.
- [postgrest-worker-example](https://github.com/cloudflare/postgrest-worker-example) (21 stars, JavaScript, pushed 2026-04-23): Example Workers function for interfacing with a PostgreSQL database, using PostgREST.
- [binast-cf-worker](https://github.com/cloudflare/binast-cf-worker) (18 stars, JavaScript, pushed 2026-04-23): Serve BinAST via a Cloudflare Worker.
- [kv-worker-migrate](https://github.com/cloudflare/kv-worker-migrate) (18 stars, JavaScript, pushed 2026-04-23): No description.
- [custom-device-posture-integration-example-worker](https://github.com/cloudflare/custom-device-posture-integration-example-worker) (10 stars, JavaScript, pushed 2026-04-23): Example implementation of a worker for custom device posture integrations.
- [kubernetes-access-worker-example](https://github.com/cloudflare/kubernetes-access-worker-example) (7 stars, TypeScript, pushed 2026-04-23): Example implementation of an Access-protected private Kubernetes API.
- [matched-data-worker](https://github.com/cloudflare/matched-data-worker) (7 stars, TypeScript, pushed 2026-04-28): No description.
- [scala-worker-kv](https://github.com/cloudflare/scala-worker-kv) (5 stars, Scala, pushed 2026-04-23): Scala example of Workers KV.
- [msft-risky-user-ad-sync](https://github.com/cloudflare/msft-risky-user-ad-sync) (4 stars, JavaScript, pushed 2026-04-23): This repository deploys a Cloudflare Scheduled Worker which synchronises users flagged by Azure's Risky User API into Groups based on risk level. These groups can be applied to Cloudflare Zero Trust policies to isolate application access.

## Networking, proxies and protocols

Proxies, transports, tunnels and network measurement.
14 repos.

- [pingora](https://github.com/cloudflare/pingora) (27,585 stars, Rust, pushed 2026-09-11, 5 docs links, README mirrored): A library for building fast, reliable and evolvable network services. README: serving more than 40 million requests per second.
- [cloudflared](https://github.com/cloudflare/cloudflared) (16,032 stars, Go, pushed 2026-09-29, 98 docs links, README mirrored): Cloudflare Tunnel client.
- [quiche](https://github.com/cloudflare/quiche) (12,744 stars, Rust, pushed 2026-10-05, 5 docs links, README mirrored): Savoury implementation of the QUIC transport protocol and HTTP/3.
- [boringtun](https://github.com/cloudflare/boringtun) (7,207 stars, Rust, pushed 2026-06-29, README mirrored): Userspace WireGuard Implementation in Rust. README warns the master branch is being restructured; use the crates.io release.
- [wirefilter](https://github.com/cloudflare/wirefilter) (1,163 stars, Rust, pushed 2026-09-24, README mirrored): An execution engine for Wireshark-like filters.
- [speedtest](https://github.com/cloudflare/speedtest) (749 stars, TypeScript, pushed 2026-09-22, README mirrored): Component to perform network speed tests against Cloudflare's edge network. README: the public TURN server used for packet-loss tests is deprecated.
- [mmproxy](https://github.com/cloudflare/mmproxy) (518 stars, C, pushed 2026-04-24, README mirrored): mmproxy, the magical PROXY protocol gateway.
- [tubular](https://github.com/cloudflare/tubular) (338 stars, C, pushed 2026-04-23): BSD socket API on steroids.
- [pmtud](https://github.com/cloudflare/pmtud) (260 stars, C, pushed 2026-04-24): Path MTU daemon - broadcast lost ICMP packets on ECMP networks.
- [ipvs](https://github.com/cloudflare/ipvs) (185 stars, Go, pushed 2026-04-29): Package ipvs allows you to manage Linux IPVS services and destinations.
- [moq-rs](https://github.com/cloudflare/moq-rs) (171 stars, Rust, pushed 2026-09-29): Rust implementation of the IETF MoQ Transport protocol.
- [udpgrm](https://github.com/cloudflare/udpgrm) (155 stars, C, pushed 2026-07-15): UDP Graceful Restart Marshal.
- [slirpnetstack](https://github.com/cloudflare/slirpnetstack) (136 stars, Go, pushed 2026-04-23): slirp4netns implementation using gvisor/netstack.
- [networkquality-rs](https://github.com/cloudflare/networkquality-rs) (99 stars, Rust, pushed 2026-09-25): A collection of tools for measuring the quality of a network.

## Cryptography, TLS and privacy

PKI, TLS, cryptographic primitives and privacy protocols.
29 repos.

- [cfssl](https://github.com/cloudflare/cfssl) (9,480 stars, Go, pushed 2026-09-30, 5 docs links, README mirrored): CFSSL: Cloudflare's PKI and TLS toolkit.
- [gokey](https://github.com/cloudflare/gokey) (2,436 stars, Go, pushed 2026-07-10, README mirrored): A simple vaultless password manager in Go.
- [circl](https://github.com/cloudflare/circl) (1,725 stars, Go, pushed 2026-09-28, README mirrored): CIRCL: Cloudflare Interoperable Reusable Cryptographic Library. Post-quantum and elliptic-curve primitives; README carries an experimental-use security disclaimer.
- [sslconfig](https://github.com/cloudflare/sslconfig) (1,314 stars, none, pushed 2026-04-24, README mirrored): Cloudflare's Internet facing SSL configuration.
- [utahfs](https://github.com/cloudflare/utahfs) (813 stars, Go, pushed 2026-04-23, README mirrored): UtahFS is an encrypted storage system that provides a user-friendly FUSE drive backed by cloud storage.
- [boring](https://github.com/cloudflare/boring) (524 stars, Rust, pushed 2026-09-30, README mirrored): BoringSSL bindings for the Rust programming language.
- [gokeyless](https://github.com/cloudflare/gokeyless) (515 stars, Go, pushed 2026-07-25, 7 docs links, README mirrored): Go implementation of the keyless protocol.
- [pp-browser-extension](https://github.com/cloudflare/pp-browser-extension) (416 stars, TypeScript, pushed 2026-08-05, README mirrored): Client for Privacy Pass protocol providing unlinkable cryptographic tokens. Silk, the Privacy Pass browser client (README).
- [go](https://github.com/cloudflare/go) (372 stars, Go, pushed 2026-04-24): Go with Cloudflare experimental patches.
- [cfssl_trust](https://github.com/cloudflare/cfssl_trust) (322 stars, Go, pushed 2026-09-28, 6 docs links): CFSSL's CA trust store repository.
- [tls-tris](https://github.com/cloudflare/tls-tris) (301 stars, Go, pushed 2026-04-24): crypto/tls, now with 100% more 1.3. THE API IS NOT STABLE AND DOCUMENTATION IS NOT GUARANTEED.
- [certmgr](https://github.com/cloudflare/certmgr) (233 stars, Go, pushed 2026-04-24): Automated certificate management using a CFSSL CA.
- [odoh-rs](https://github.com/cloudflare/odoh-rs) (191 stars, Rust, pushed 2026-09-14): Oblivious DoH library in Rust.
- [lockbox](https://github.com/cloudflare/lockbox) (183 stars, Go, pushed 2026-09-28): Offline encryption of Kubernetes Secrets.
- [roughtime](https://github.com/cloudflare/roughtime) (177 stars, Go, pushed 2026-04-28, 6 docs links): A secure clock-synchronization protocol for when rough is enough.
- [web-bot-auth](https://github.com/cloudflare/web-bot-auth) (165 stars, Rust, pushed 2026-09-19): Sign and verify orchestrated HTTP requests. Topics: agents, cryptography.
- [bn256](https://github.com/cloudflare/bn256) (134 stars, Go, pushed 2026-09-09): Package bn256 implements a particular bilinear group.
- [opaque-ts](https://github.com/cloudflare/opaque-ts) (111 stars, TypeScript, pushed 2026-09-13): A TypeScript library for OPAQUE Asymmetric Password-Authenticated Key Exchange Protocol.
- [privacy-gateway-server-go](https://github.com/cloudflare/privacy-gateway-server-go) (89 stars, Go, pushed 2026-07-10): An Oblivious HTTP gateway.
- [pal](https://github.com/cloudflare/pal) (85 stars, Go, pushed 2026-04-24): PAL: A secret bootstrapping tool for Docker.
- [odoh-client-rs](https://github.com/cloudflare/odoh-client-rs) (74 stars, Rust, pushed 2026-04-23): Oblivious DoH client application written in Rust.
- [opaque-ea](https://github.com/cloudflare/opaque-ea) (66 stars, Go, pushed 2026-04-23): No description.
- [azul](https://github.com/cloudflare/azul) (62 stars, Rust, pushed 2026-10-02): Tiled transparency logs libraries and applications.
- [certinel](https://github.com/cloudflare/certinel) (56 stars, Go, pushed 2026-04-24): A sentry for zero-hit TLS certificate changes in Go.
- [dkim](https://github.com/cloudflare/dkim) (56 stars, Rust, pushed 2026-04-23): DKIM (RFC6376) implementation.
- [fourq](https://github.com/cloudflare/fourq) (54 stars, Go, pushed 2026-04-24): Package fourq implements FourQ, a high-speed elliptic curve at the 128-bit security level.
- [privacy-gateway-relay](https://github.com/cloudflare/privacy-gateway-relay) (41 stars, JavaScript, pushed 2026-04-23): A Oblivious HTTP ("OHTTP") Relay built on Cloudflare Workers.
- [crypto-discovery-prompts](https://github.com/cloudflare/crypto-discovery-prompts) (4 stars, none, pushed 2026-09-29): Prompts for AI-assisted discovery of cryptography in source code and post-quantum migration analysis. Linked from the blog post `ai-driven-cryptography-discovery`.
- [odoh-proxy-worker](https://github.com/cloudflare/odoh-proxy-worker) (2 stars, none, pushed 2026-04-23): No description.

## Linux, eBPF and observability

eBPF, Prometheus exporters and Linux tooling.
16 repos.

- [ebpf_exporter](https://github.com/cloudflare/ebpf_exporter) (2,651 stars, Go, pushed 2026-10-01, README mirrored): Prometheus exporter for custom eBPF metrics.
- [bpftools](https://github.com/cloudflare/bpftools) (1,230 stars, Python, pushed 2026-04-24, README mirrored): BPF Tools - packet analyst toolkit.
- [pint](https://github.com/cloudflare/pint) (1,046 stars, Go, pushed 2026-10-02, README mirrored): Prometheus rule linter/validator.
- [xdpcap](https://github.com/cloudflare/xdpcap) (790 stars, Go, pushed 2026-07-30, README mirrored): tcpdump like XDP packet capture.
- [sandbox](https://github.com/cloudflare/sandbox) (533 stars, C, pushed 2026-04-23, README mirrored): Simple Linux seccomp rules without writing any code.
- [alertmanager2es](https://github.com/cloudflare/alertmanager2es) (249 stars, Go, pushed 2026-04-24): Receives HTTP webhook notifications from AlertManager and inserts them into an Elasticsearch index for searching and analysis.
- [cbpfc](https://github.com/cloudflare/cbpfc) (218 stars, Go, pushed 2026-09-01): cBPF to C or eBPF compiler.
- [rakelimit](https://github.com/cloudflare/rakelimit) (212 stars, C, pushed 2026-04-23): A fair-share ratelimiter implemented in BPF.
- [sciuro](https://github.com/cloudflare/sciuro) (185 stars, Go, pushed 2026-07-07): Alertmanager to Kubernetes Node conditions bridge.
- [cloudflare-prometheus-exporter](https://github.com/cloudflare/cloudflare-prometheus-exporter) (184 stars, TypeScript, pushed 2026-09-21, 6 docs links): Export Cloudflare metrics to Prometheus. Built on Cloudflare Workers with Durable Objects for stateful metric accumulation.
- [linux](https://github.com/cloudflare/linux) (144 stars, none, pushed 2026-04-23): Cloudflare Linux Kernel Patches.
- [cloudflare-gcp](https://github.com/cloudflare/cloudflare-gcp) (88 stars, JavaScript, pushed 2026-04-24): Google Cloud Function to push json files from GC Storage to Big Query.
- [complainer](https://github.com/cloudflare/complainer) (81 stars, Go, pushed 2026-04-24): Complainer's job is to send notifications to different services when tasks fail on Mesos cluster.
- [kafka_zookeeper_exporter](https://github.com/cloudflare/kafka_zookeeper_exporter) (71 stars, Go, pushed 2026-04-24): Prometheus exporter for Kafka cluster state stored in ZooKeeper.
- [psi_exporter](https://github.com/cloudflare/psi_exporter) (71 stars, Rust, pushed 2026-04-23): Prometheus exporter for Pressure Stall Information (PSI) from Linux kernel.
- [filterforge](https://github.com/cloudflare/filterforge) (64 stars, Python, pushed 2026-04-23): Tool for solving BPF filters and crafting packets based on these.

## Systems libraries, data structures, Nginx and Lua

General-purpose libraries in Go, Rust, C and Lua.
29 repos.

- [tableflip](https://github.com/cloudflare/tableflip) (3,215 stars, Go, pushed 2026-04-23, README mirrored): Graceful process restarts in Go.
- [foundations](https://github.com/cloudflare/foundations) (1,690 stars, Rust, pushed 2026-10-01, README mirrored): Cloudflare's Rust service foundations library.
- [hellogopher](https://github.com/cloudflare/hellogopher) (1,145 stars, Makefile, pushed 2026-04-24, README mirrored): Hellogopher: "just clone and make" your conventional Go project.
- [ahocorasick](https://github.com/cloudflare/ahocorasick) (728 stars, Go, pushed 2026-04-24, README mirrored): A Golang implementation of the Aho-Corasick string matching algorithm.
- [zlib](https://github.com/cloudflare/zlib) (706 stars, C, pushed 2026-04-24, fork): Cloudflare fork of zlib with massive performance improvements.
- [mmap-sync](https://github.com/cloudflare/mmap-sync) (647 stars, Rust, pushed 2026-04-28, README mirrored): Rust library for concurrent data access, using memory-mapped files, zero-copy deserialization, and wait-free synchronization.
- [trie-hard](https://github.com/cloudflare/trie-hard) (616 stars, Rust, pushed 2026-04-23, README mirrored): Novel implementation of a Trie data structure optimized for small, sparse maps.
- [shellflip](https://github.com/cloudflare/shellflip) (535 stars, Rust, pushed 2026-04-23, README mirrored): Graceful process restarts in Rust.
- [lua-resty-logger-socket](https://github.com/cloudflare/lua-resty-logger-socket) (493 stars, Raku, pushed 2026-04-24, README mirrored): Raw-socket-based Logger Library for Nginx (based on ngx_lua).
- [golibs](https://github.com/cloudflare/golibs) (414 stars, Go, pushed 2026-04-24, README mirrored): Various small golang libraries.
- [ecdysis](https://github.com/cloudflare/ecdysis) (334 stars, Rust, pushed 2026-08-11): A library for graceful restarts in Rust.
- [sqlalchemy-clickhouse](https://github.com/cloudflare/sqlalchemy-clickhouse) (325 stars, Python, pushed 2026-04-24): No description.
- [semver_bash](https://github.com/cloudflare/semver_bash) (269 stars, Shell, pushed 2026-04-24): Semantic Versioning in Bash.
- [wildcard](https://github.com/cloudflare/wildcard) (219 stars, Rust, pushed 2026-08-27): Wildcard matching.
- [loom](https://github.com/cloudflare/loom) (180 stars, Lua, pushed 2026-04-24): Easier to read LuaJIT dumps.
- [lua-resty-json](https://github.com/cloudflare/lua-resty-json) (178 stars, C, pushed 2026-04-24): json lib for lua and C.
- [freighter](https://github.com/cloudflare/freighter) (154 stars, Rust, pushed 2026-09-18): A fast, modular, and operationally boring Rust private registry implementation.
- [lua-capnproto](https://github.com/cloudflare/lua-capnproto) (154 stars, Lua, pushed 2026-04-24, fork): Lua-capnp is a pure lua implementation of capnproto based on luajit.
- [lua-upstream-cache-nginx-module](https://github.com/cloudflare/lua-upstream-cache-nginx-module) (124 stars, C, pushed 2026-04-24): Nginx module for ngx_lua to provide Lua API to inspect upstream http cache meta-data.
- [raven-lua](https://github.com/cloudflare/raven-lua) (121 stars, Lua, pushed 2026-04-24): A Lua interface to Sentry.
- [bm](https://github.com/cloudflare/bm) (119 stars, Go, pushed 2026-04-24): A Golang implementation of Bentley/McIlroy long string compression.
- [ngx_brotli_module](https://github.com/cloudflare/ngx_brotli_module) (116 stars, C, pushed 2026-04-24): Brotli module for NGINX, including the encoder.
- [sliceslice-rs](https://github.com/cloudflare/sliceslice-rs) (106 stars, Rust, pushed 2026-04-23): A fast implementation of single-pattern substring search using SIMD acceleration.
- [golz4](https://github.com/cloudflare/golz4) (100 stars, C, pushed 2026-04-24): Golang interface to LZ4 compression.
- [golog](https://github.com/cloudflare/golog) (97 stars, Go, pushed 2026-04-24, fork): A high performance wrapper around Syslog.
- [buffer](https://github.com/cloudflare/buffer) (90 stars, Go, pushed 2026-04-24): Circular buffer backed by MMAPed file for golang.
- [recapn](https://github.com/cloudflare/recapn) (74 stars, Rust, pushed 2026-05-26): A WIP Cap'n Proto implementation in Rust written from the ground up.
- [lua-resty-shcache](https://github.com/cloudflare/lua-resty-shcache) (71 stars, Lua, pushed 2026-04-24, fork): shcache - simple cache object atop ngx.shared.DICT.
- [chrome-devtools-rs](https://github.com/cloudflare/chrome-devtools-rs) (67 stars, Rust, pushed 2026-04-23): Rust library for the Chrome Devtools Protocol.

## Frontend and web libraries

UI components and HTML or SVG processing.
10 repos.

- [kumo](https://github.com/cloudflare/kumo) (3,946 stars, TypeScript, pushed 2026-10-05, README mirrored): Cloudflare's component library for building modern web applications.
- [lol-html](https://github.com/cloudflare/lol-html) (2,072 stars, Rust, pushed 2026-07-29, README mirrored): Low output latency streaming HTML parser/rewriter with CSS selector-based API.
- [react-gateway](https://github.com/cloudflare/react-gateway) (576 stars, JavaScript, pushed 2026-04-24, README mirrored): Render React DOM into a new context (aka "Portal").
- [svg-hush](https://github.com/cloudflare/svg-hush) (435 stars, Rust, pushed 2026-08-25, README mirrored): Make it safe to serve untrusted SVG files.
- [json-schema-tools](https://github.com/cloudflare/json-schema-tools) (341 stars, JavaScript, pushed 2026-04-24): Packages for working with JSON Schema and JSON Hyper-Schema.
- [react-modal2](https://github.com/cloudflare/react-modal2) (275 stars, JavaScript, pushed 2026-04-24): Simple modal component for React.
- [lazyhtml](https://github.com/cloudflare/lazyhtml) (149 stars, Rust, pushed 2026-04-23): HTML5-compliant parser and serializer than enables building transformation pipeline in a pluggable manner.
- [webcm](https://github.com/cloudflare/webcm) (80 stars, TypeScript, pushed 2026-04-23): Components Manager for the Web. Free, open-source, and fast!
- [embed-box](https://github.com/cloudflare/embed-box) (77 stars, JavaScript, pushed 2026-04-24): Universal install guide for embed codes and CMS plugins.
- [color](https://github.com/cloudflare/color) (60 stars, JavaScript, pushed 2026-04-23): No description.

## Docs, websites and talks

Documentation sources, websites and talk material.
8 repos.

- [cloudflare-docs](https://github.com/cloudflare/cloudflare-docs) (5,279 stars, MDX, pushed 2026-10-05, 16931 docs links, README mirrored): Cloudflare’s documentation.
- [nimbus](https://github.com/cloudflare/nimbus) (1,413 stars, TypeScript, pushed 2026-10-05, README mirrored): Docs for humans and agents, built on Astro.
- [cloudflare-blog](https://github.com/cloudflare/cloudflare-blog) (1,225 stars, C, pushed 2026-04-24, README mirrored): Cloudflare Blog code samples.
- [cloudflare.github.io](https://github.com/cloudflare/cloudflare.github.io) (465 stars, CSS, pushed 2026-04-24, README mirrored): Cloudflare Open Source.
- [isbgpsafeyet.com](https://github.com/cloudflare/isbgpsafeyet.com) (330 stars, HTML, pushed 2026-09-09): Is BGP safe yet?
- [jgc-talks](https://github.com/cloudflare/jgc-talks) (97 stars, Go, pushed 2026-04-24): Code samples and data used in talk preparation by John Graham-Cumming.
- [goser](https://github.com/cloudflare/goser) (79 stars, Go, pushed 2026-04-24): Code for talk about Go Serialization.
- [.github](https://github.com/cloudflare/.github) (39 stars, none, pushed 2024-09-25): Cloudflare's template for open source community resources.

## Archived and legacy

Repos with `archived=true` in repos.tsv; only archived repos that match a keyword are in the selection.
9 repos.

- [miniflare](https://github.com/cloudflare/miniflare) (3,926 stars, TypeScript, pushed 2025-03-13): Fully-local simulator for Cloudflare Workers. For the latest version, see https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare.
- [queues-web-crawler](https://github.com/cloudflare/queues-web-crawler) (190 stars, TypeScript, pushed 2024-10-01): A web crawler built with Cloudflare Queues, Browser Rendering, and Workers KV.
- [workers.cloudflare.com](https://github.com/cloudflare/workers.cloudflare.com) (156 stars, JavaScript, pushed 2026-01-08): The Cloudflare Workers website.
- [db-connect](https://github.com/cloudflare/db-connect) (150 stars, TypeScript, pushed 2021-02-24): Connect your SQL database to Cloudflare Workers.
- [workers-ai-provider](https://github.com/cloudflare/workers-ai-provider) (113 stars, TypeScript, pushed 2025-03-18): A Workers AI provider for the vercel AI SDK.
- [workers-docs](https://github.com/cloudflare/workers-docs) (104 stars, none, pushed 2020-10-01): The documentation site for Cloudflare Workers.
- [securitytxt-worker](https://github.com/cloudflare/securitytxt-worker) (58 stars, JavaScript, pushed 2023-03-21): The worker that serves Cloudflare's security.txt!
- [cf-tls](https://github.com/cloudflare/cf-tls) (21 stars, Go, pushed 2024-10-16): A duplicate of Go's crypto/tls, with additional helper functions.
- [go-ipfs-blocklist](https://github.com/cloudflare/go-ipfs-blocklist) (1 star, Go, pushed 2024-01-23): No description.

## Notable repos outside the selection rule

These do not meet the rule (archived without a keyword match, or under 50 stars without one) but matter for context.
They are listed here for reference only and are not counted in the totals above.

* [flan](https://github.com/cloudflare/flan) (4,162 stars, Python, archived, pushed 2026-04-23): A pretty sweet vulnerability scanner.
* [wrangler-legacy](https://github.com/cloudflare/wrangler-legacy) (3,188 stars, Rust, archived, pushed 2023-08-03, 7 docs links): Home to Wrangler v1 (deprecated).
* [next-on-pages](https://github.com/cloudflare/next-on-pages) (1,491 stars, TypeScript, archived, pushed 2026-10-01): CLI to build and develop Next.js apps for Cloudflare Pages.
* [redoctober](https://github.com/cloudflare/redoctober) (1,415 stars, Go, archived, pushed 2026-05-04): Go server for two-man rule style file encryption and decryption.
* [production-saas](https://github.com/cloudflare/production-saas) (1,146 stars, TypeScript, archived, pushed 2024-09-25): (WIP) Example SaaS application built in public on the Cloudflare stack!
* [python-cloudflare](https://github.com/cloudflare/python-cloudflare) (692 stars, Python, archived, pushed 2024-11-22): Python wrapper for the Cloudflare Client API v4.
* [node-cloudflare](https://github.com/cloudflare/node-cloudflare) (337 stars, JavaScript, archived, pushed 2025-02-25): Node.js API for Client API.
* [dog](https://github.com/cloudflare/dog) (290 stars, TypeScript, archived, pushed 2025-04-04): Durable Object Groups.
* [cf-pgbouncer](https://github.com/cloudflare/cf-pgbouncer) (268 stars, C, archived, pushed 2026-04-23): lightweight connection pooler for PostgreSQL.
* [kv-asset-handler](https://github.com/cloudflare/kv-asset-handler) (259 stars, TypeScript, archived, pushed 2024-02-09): Routes requests to KV assets.
* [zkp-ecdsa](https://github.com/cloudflare/zkp-ecdsa) (228 stars, TypeScript, archived, pushed 2026-06-29): Proves knowledge of an ECDSA-P256 signature under one of many public keys that are stored in a list.
* [privacypass-ts](https://github.com/cloudflare/privacypass-ts) (48 stars, TypeScript, active, pushed 2026-10-02, 9 docs links): A TypeScript Library for the Privacy Pass Issuance Protocol.
* [dynamic-workflows](https://github.com/cloudflare/dynamic-workflows) (44 stars, TypeScript, active, pushed 2026-04-30, 8 docs links): No description.
* [langchain-cloudflare](https://github.com/cloudflare/langchain-cloudflare) (40 stars, Python, active, pushed 2026-10-03, 5 docs links): LangChain integrations for Cloudflare.
* [pubsub](https://github.com/cloudflare/pubsub) (40 stars, TypeScript, active, pushed 2026-04-23): A set of useful helper methods for writing functions to handle Cloudflare Pub/Sub messages (https://developers.cloudflare.com/pub-sub/).
* [tf-migrate](https://github.com/cloudflare/tf-migrate) (33 stars, Go, active, pushed 2026-09-17, 15 docs links): CLI tool for upgrading the terraform-provider-cloudflare to a new major version.
* [docs-examples](https://github.com/cloudflare/docs-examples) (21 stars, TypeScript, archived, pushed 2026-06-24, 81 docs links): Examples surfaced in the Cloudflare Docs.

## Gaps and contradictions

- `wildebeest`: the README opens with "This project has been archived and is no longer actively maintained", but repos.tsv lists it as `archived=false` with a push on 2026-04-23.
- `docs-examples` is archived, yet the docs mirror links it 81 times.
- `miniflare` is archived and its description points to `workers-sdk/packages/miniflare`; `workers-ai-provider` is archived while the `ai` README lists a `workers-ai-provider` package, so the live code appears to have moved into those monorepos.
- `workers-mcp` and `worker-typescript-template` are not archived, but their READMEs tell readers to use something else.
- 350 of 580 repos show a last push on 2026-04-23 or 2026-04-24, so a recent "pushed" date is not by itself evidence of active development.
- The docs mirror links two repo names that are not in repos.tsv: `orange` (the `meet` README says Meet was formerly Orange Meets) and `custom-headers-example`.
- Several high-relevance repos have no description in repos.tsv and no mirrored README (`cfweb3`, `mpp-proxy`, `claude-managed-agents`, `api-schemas`); their lines rely on docs pages or say nothing beyond the name.
- Only 80 READMEs are mirrored, so most lines rest on the one-line GitHub description alone.
- Cloudflare Wallets (blog, 2026-08-04) and the x402 Foundation (blog, 2025-09-23) have no matching public repo in the org; the x402 code in this org lives in the `agents` monorepo.
- The keyword rule catches the substring, so `worker` also matches `workerd`, and `crypto` matches "cryptographic"; `web-bot-auth` (topic `cryptography`) is included only through its star count.
