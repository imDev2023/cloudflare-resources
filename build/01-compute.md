# Build > Compute

Synthesis of the docs sidebar's Build > Compute dropdown (Workers, Containers, Durable Objects, Queues, Workflows, Flagship, Browser Run, Workers VPC, Cloudflare for Platforms, Email Service) plus two compute products that have docs but no sidebar entry (Pages and Dynamic Workers).
Everything here is stated as of 2026-10-05 unless a different date is given, and every fact block cites its source page.

## Summary

Workers is the center of Cloudflare's compute stack: V8-isolate functions on Workers Free (100,000 requests per day, 10 ms CPU) or Workers Paid ($5 per month minimum, 10 million requests and 30 million CPU-ms included, then $0.30 per million requests and $0.02 per million CPU-ms, up to 5 minutes CPU and 10,000 to 10 million subrequests per invocation, no charge for wall time, egress or static asset requests), with Node.js compatibility on by default from compatibility date 2026-08-04, a new per-Worker response cache (Workers Cache), per-branch Previews, gradual deployments and Smart Placement or explicit cloud-region placement.
Everything else plugs into a Worker: Durable Objects (GA, SQLite-backed single-threaded objects with up to 10 GB each, 32,768 hibernatable WebSockets and alarms, on Free and Paid) handle coordination; Queues (GA, at-least-once, 5,000 messages per second per queue, 128 KB messages) and Workflows (GA, durable steps, sleeps up to a year, step billing since 2026-08-10) handle background work; Containers (Paid only, Firecracker microVMs from 1/16 to 4 vCPU, driven from a Durable Object, manual scaling, a new `durable_object` scheduling policy in beta) handle anything that needs a full Linux runtime; Dynamic Workers (Paid only) load sandboxed code at runtime; Workers for Platforms ($25 per month) and Cloudflare for SaaS host customer code and customer domains.
The newer pieces are mostly beta: Flagship feature flags (public beta since 2026-05-26, no published pricing), Workers VPC (beta, free, Tunnel/Mesh/WAN into private networks with `fetch()` and `connect()`), Email Sending (public beta since 2026-04-16, Paid only, 3,000 emails per month then $0.35 per 1,000) next to GA-like Email Routing, and Browser Run (renamed from Browser Rendering on 2026-04-15, headless Chrome on Free and Paid, 200 concurrent browsers on Paid since 2026-08-20, with a beta `/crawl` endpoint and the beta Kitesurf engine).
Pages still works but its own overview tells readers to "Start new projects with Workers", and the migration guide's matrix shows Workers ahead on gradual deployments, Cron Triggers, Durable Objects, queue consumers, rate limiting and observability.
For API proxies and bots the hard numbers are: six connections waiting for headers at once, no raw-IP `fetch()`, 32 MiB WebSocket messages, `waitUntil()` capped at 30 seconds after the response, 15-minute wall time for crons, queue consumers and alarms, TCP sockets (public beta) that cannot reach Cloudflare IPs, private IPs or port 25, and a per-location, eventually consistent rate-limiting binding.

## Table of contents

1. [Comparison: which compute product when](#1-comparison-which-compute-product-when)
2. [Workers](#2-workers)
3. [Containers](#3-containers)
4. [Durable Objects](#4-durable-objects)
5. [Queues](#5-queues)
6. [Workflows](#6-workflows)
7. [Flagship](#7-flagship)
8. [Browser Run (formerly Browser Rendering)](#8-browser-run-formerly-browser-rendering)
9. [Workers VPC](#9-workers-vpc)
10. [Cloudflare for Platforms](#10-cloudflare-for-platforms)
11. [Email Service](#11-email-service)
12. [Pages (not in the sidebar)](#12-pages-not-in-the-sidebar)
13. [Dynamic Workers (not in the sidebar)](#13-dynamic-workers-not-in-the-sidebar)
14. [Workers runtime limits that matter for API proxies and backends](#14-workers-runtime-limits-that-matter-for-api-proxies-and-backends)
15. [Build hooks for Web3 projects](#15-build-hooks-for-web3-projects)
16. [Gaps and contradictions](#16-gaps-and-contradictions)

## 1. Comparison: which compute product when

All values as of 2026-10-05, from the pages cited in sections 2 to 13.
"Use when" is the docs' own positioning unless marked (inference).

| Product | Status | Free plan | Paid entry price | Execution model | Max work per invocation | State | Use when |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Workers | GA | Yes (100k req/day, 10 ms CPU) | $5/month Workers Paid | Stateless V8 isolates, request-driven, cron, queue, email | CPU 5 min max (30 s default); HTTP wall time unlimited while client connected; crons 15 min | None in memory across requests; use bindings | APIs, proxies, SSR, full-stack apps, glue |
| Durable Objects | GA | Yes (SQLite only) | Included in Workers Paid, usage-billed | Single-threaded named object with storage, RPC, WebSockets, alarms | CPU 30 s default (5 min max) per request or message; wall time unlimited while caller connected | Strongly consistent SQLite, 10 GB per object | Coordination: chat rooms, games, collaborative docs, per-user state (order books and nonce locks are inference) |
| Containers | No beta label (default policy); `durable_object` policy in beta | No | Workers Paid plus per-10 ms usage | Firecracker microVM per instance, driven by a Durable Object | No fixed max runtime; host restarts possible | Ephemeral disk; snapshots (durable_object policy) | Any language or binary, heavy CPU/memory, existing images, sandboxes |
| Queues | GA | Yes (10k ops/day, 24 h retention) | $0.40 per million ops after 1M | Async messages, batched push or HTTP pull | Consumer wall 15 min, CPU up to 5 min | Messages retained up to 14 days | Decoupling, buffering, retries, rate-limited upstreams |
| Workflows | GA (Python open beta) | Yes | Workers rates plus steps and storage | Durable multi-step instances | CPU per step 5 min max; wall time unlimited; sleep up to 365 days | Step results persisted (1 GB per instance on Paid) | Multi-step jobs that must survive failures, wait for events or sleep |
| Flagship | Public beta | Not stated | Not published | Flag evaluation inside Workers or via OpenFeature SDKs | n/a | Flag config propagated globally | Feature flags, targeting, percentage rollouts |
| Browser Run | Available (crawl and Kitesurf beta) | Yes (10 browser-min/day) | $0.09 per browser-hour after 10 h, $2 per extra concurrent browser after 10 | Headless Chrome via REST Quick Actions or Puppeteer/Playwright/CDP sessions | Session lives while active; 60 s idle timeout (10 min with keep_alive) | Session reuse | Screenshots, PDFs, scraping, crawling, agent browsing |
| Workers VPC | Beta | Yes (free in beta) | Free in beta | Bindings that tunnel `fetch()` / `connect()` into private networks | Standard Workers limits | None | Reaching private APIs, services and databases in other clouds or on-premise |
| Workers for Platforms | GA | No | $25/month | Untrusted user Workers in dispatch namespaces behind your dispatch Worker | Per-tenant custom CPU and subrequest limits | Per-tenant bindings | Hosting customer code at scale, unlimited scripts |
| Cloudflare for SaaS | GA | 100 hostnames included | $0.10 per extra hostname | Custom hostnames and certificates on your zone | n/a | n/a | Customer vanity domains |
| Email Service | Sending beta (Paid only); Routing available on Free and Paid | Routing yes; sending only to verified addresses | 3,000 emails/month then $0.35 per 1,000 | `send_email` binding, REST, SMTP; `email()` handler | Email Workers use Workers limits | n/a | Transactional email, inbound mail processing |
| Pages | Available; new projects told to use Workers | Yes | Functions billed as Workers | Static hosting plus Pages Functions | As Workers | As Workers | Existing Pages projects only |
| Dynamic Workers | No beta label; Paid only | No | Workers rates plus $0.002 per Dynamic Worker per day beyond inclusion | Runtime-loaded sandboxed isolates via Worker Loader binding | Parent plan limits or lower custom limits | Facets give SQLite per loaded Durable Object | Running AI-generated or user code in a lightweight sandbox |

Rules of thumb drawn from the docs:
- Stateless request handling belongs in Workers; Durable Objects are for coordination, not stateless work (https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/).
- Work that cannot finish within 30 seconds after the response should go to Queues (https://developers.cloudflare.com/workers/runtime-apis/context/), and multi-step work that must survive failures to Workflows (https://developers.cloudflare.com/workers/best-practices/workers-best-practices/).
- WebSockets that need shared state belong in Durable Objects with the Hibernation API (https://developers.cloudflare.com/workers/runtime-apis/websockets/).
- Containers are for code that needs a full filesystem, specific runtime, many cores or lots of memory, or that ships as an image (https://developers.cloudflare.com/containers/); Dynamic Workers are described as "a lightweight alternative to containers for securely sandboxing code you don't trust" (https://developers.cloudflare.com/dynamic-workers/).
- New front ends and full-stack apps should use Workers static assets, not Pages (https://developers.cloudflare.com/pages/, https://developers.cloudflare.com/workers/best-practices/workers-best-practices/).

## 2. Workers

### What it is

Workers is Cloudflare's serverless platform for building, deploying and scaling apps across Cloudflare's global network, deployed with a single command and no infrastructure to manage.
It covers front-end apps (static assets on the CDN), back-end APIs (with Smart Placement near data stores), AI inference (Workers AI), background jobs (Cron Triggers, Workflows, Queues) and observability.
Languages are JavaScript, TypeScript, Python, Rust, and others through WebAssembly.
Workers is the base layer that every other product in this file builds on: Durable Objects, Containers, Workflows, Queues consumers, Browser Run bindings, Email handlers, Workers for Platforms and Dynamic Workers all run inside or are driven from a Worker.

Sources: https://developers.cloudflare.com/workers/

Pages now tells new users to start with Workers instead: "Workers supports most Pages use cases and offers a broader feature set. It is Cloudflare's primary platform for building applications. Start new projects with Workers." (see [Pages](#12-pages-not-in-the-sidebar)).

Sources: https://developers.cloudflare.com/pages/

### Status and plans

- Workers is generally available on two plans: Workers Free and Workers Paid (minimum $5 USD per month per account), as of 2026-10-05.
- The Workers Paid plan is separate from any Cloudflare zone plan (Free, Pro, Business).
- Legacy usage models Bundled and Unbound are deprecated and not available to new accounts; Paid accounts use the Standard usage model.
- The Workers "Betas" page lists only three public betas as of 2026-10-05: Email Workers, Green Compute and TCP Sockets.
- Other features marked beta on their own pages as of 2026-10-05: Smart Placement (the `cf-placement` header "may be removed before Smart Placement exits beta"), Workers tracing ("currently in beta"), Tail Workers (headed "Beta" on the observability overview), Issues (open beta, free during the beta), `cloudflare.config.ts` typed configuration (open beta), host-based Placement Hints ("experimental"), vinext for Next.js (beta), SolidStart support (beta), Secrets Store (beta).

Sources: https://developers.cloudflare.com/workers/platform/pricing/, https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/platform/betas/, https://developers.cloudflare.com/workers/configuration/placement/, https://developers.cloudflare.com/workers/observability/traces/, https://developers.cloudflare.com/workers/observability/, https://developers.cloudflare.com/workers/wrangler/configuration/, https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/

### Key concepts

- **Isolate**: Workers run in V8 isolates; memory (128 MB) is per isolate, and one isolate can serve many concurrent requests.
- **Handlers**: entry methods invoked from outside the Worker: `fetch`, `scheduled` (Cron Triggers), `queue` (Queues consumer), `email` (Email Routing), `tail` (Tail Workers), and `alarm` (Durable Objects).
In Python, handlers live on a class named `Default` that extends `WorkerEntrypoint`.
- **Bindings (`env`)**: capability plus API in one object; the underlying secret is never exposed to code.
`env` is a handler argument, a class property on `WorkerEntrypoint` / `DurableObject` / `Workflow`, or importable via `import { env } from "cloudflare:workers"`.
No I/O is allowed outside a request context, so binding methods (KV get, DO stub calls, service calls) fail at top level even though `env` is importable there.
- **Context (`ctx`)**: `waitUntil()`, `passThroughOnException()`, `props`, `exports` (loopback bindings, needs `enable_ctx_exports`), `tracing`.
- **Compatibility date and flags**: pin runtime behaviour; for compatibility dates on or after `2026-08-04`, `nodejs_compat` and `nodejs_compat_v2` are on by default.
- **Versions and deployments**: every upload is a version; a deployment points at one version (100%) or splits traffic between two (gradual deployment).
- **Service bindings and RPC**: Worker-to-Worker calls without a public URL, via `fetch()` or RPC methods on a `WorkerEntrypoint` class.
- **Static assets**: files uploaded with the Worker and served from the CDN; requests to them are free.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/runtime-apis/handlers/, https://developers.cloudflare.com/workers/runtime-apis/bindings/, https://developers.cloudflare.com/workers/runtime-apis/context/, https://developers.cloudflare.com/workers/runtime-apis/nodejs/

### Runtime API and binding surface

#### Bindings available (as of 2026-10-05)

| Binding | Points to |
| --- | --- |
| AI (Workers AI) | https://developers.cloudflare.com/workers-ai/get-started/workers-wrangler/ |
| AI Search | https://developers.cloudflare.com/ai-search/api/search/workers-binding/ |
| Analytics Engine | https://developers.cloudflare.com/analytics/analytics-engine/ |
| Analytics SQL | https://developers.cloudflare.com/workers/runtime-apis/bindings/analytics-sql/ |
| Assets | https://developers.cloudflare.com/workers/static-assets/binding/ |
| Browser Run | https://developers.cloudflare.com/browser-run/ |
| D1 | https://developers.cloudflare.com/d1/worker-api/ |
| Dispatcher (Workers for Platforms) | https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/ |
| Durable Objects | https://developers.cloudflare.com/durable-objects/api/ |
| Dynamic Worker Loaders | https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/ (page not in the mirror; see Dynamic Workers) |
| Environment variables | https://developers.cloudflare.com/workers/configuration/environment-variables/ |
| Hyperdrive | https://developers.cloudflare.com/hyperdrive/ |
| Images | https://developers.cloudflare.com/images/optimization/binding/ |
| KV | https://developers.cloudflare.com/kv/api/ |
| Media Transformations | https://developers.cloudflare.com/stream/transform-videos/bindings/ |
| mTLS | https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/ |
| Queues | https://developers.cloudflare.com/queues/configuration/javascript-apis/ |
| R2 | https://developers.cloudflare.com/r2/api/workers/workers-api-reference/ |
| Rate Limiting | https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/ |
| Secrets | https://developers.cloudflare.com/workers/configuration/secrets/ |
| Secrets Store | https://developers.cloudflare.com/secrets-store/integrations/workers/ |
| Service bindings | https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/ |
| Stream | https://developers.cloudflare.com/stream/manage-video-library/bindings/ |
| Vectorize | https://developers.cloudflare.com/vectorize/reference/client-api/ |
| Version metadata | https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/ |
| Workflows | https://developers.cloudflare.com/workflows/ |

The Wrangler configuration reference additionally documents `send_email` (Email bindings), Flagship and Agent Memory bindings (Flagship and Agent Memory are among the auto-provisioned resources).

Sources: https://developers.cloudflare.com/workers/runtime-apis/bindings/, https://developers.cloudflare.com/workers/wrangler/configuration/

When only bindings change on deploy (not code), Cloudflare may reuse running isolates, so clients built in global scope from a secret may keep the old value; construct such clients per request.
`withEnv()` (JS) and `patch_env()` (Python) override `env` values within a scope, mainly for tests.

Sources: https://developers.cloudflare.com/workers/runtime-apis/bindings/

#### Runtime API pages

The Runtime APIs section covers: Bindings, Cache, Console, Context, Encoding, EventSource, Fetch, Handlers (fetch, scheduled, tail), Headers, HTMLRewriter, MessageChannel, Node.js compatibility (assert, AsyncLocalStorage, Buffer, crypto, diagnostics_channel, dns, EventEmitter, fs, http, https, net, path, process, streams, string_decoder, test, timers, tls, url, util, zlib), Performance and timers, Request, Response, RPC (error handling, lifecycle, reserved methods, TypeScript, visibility), Scheduler, Streams (ReadableStream, BYOB reader, default reader, TransformStream, WritableStream, writer), TCP sockets, Web Crypto, Web standards, WebAssembly, WebSockets.

Sources: https://developers.cloudflare.com/workers/llms.txt

#### fetch() (outbound HTTP)

- `fetch()` must run inside a handler; calling it in global scope throws.
- Only `cache: 'no-store'` and `cache: 'no-cache'` are supported; other values throw `TypeError`.
- Worker-to-Worker `fetch` on the same zone needs a Service binding or the `global_fetch_strictly_public` compatibility flag; plain global `fetch()` to another Worker on the same zone fails, while requests to a Worker's Custom Domain are accepted.
- gzip and brotli are supported; requesting brotli from the origin needs the `brotli_content_encoding` flag; compressed bodies pass through untouched if you do not read them and keep `Content-Encoding`.
- Subrequests can only target URLs, not raw IP addresses; create an A/AAAA record and fetch the hostname instead.
- In a Partial (CNAME) zone setup, every hostname a Worker fetches must have a DNS record in Cloudflare DNS, or `fetch()` fails with 530 (1016).

Sources: https://developers.cloudflare.com/workers/runtime-apis/fetch/, https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/platform/known-issues/

#### WebSockets

- Server side: `new WebSocketPair()` returns `[client, server]`; call `server.accept()` and return the client in a 101 response.
- Client side: `fetch(url, { headers: { Upgrade: "websocket" } })` then `resp.webSocket.accept()`, or `new WebSocket(url)`.
- Incoming WebSocket messages are limited to 32 MiB (33,554,432 bytes); larger messages close the socket with `1009`.
- From compatibility date `2026-04-07` (`web_socket_auto_reply_to_close`) the runtime auto-replies to Close frames; pass `accept({ allowHalfOpen: true })` for proxying where you must coordinate close on both sides.
- From compatibility date `2026-03-17` (`websocket_standard_binary_type`) binary frames arrive as `Blob` by default; set `ws.binaryType = "arraybuffer"` before `accept()` or use `no_websocket_standard_binary_type` to keep `ArrayBuffer`.
- For coordinating many connections (chat rooms, games) the docs point to Durable Objects and their WebSocket Hibernation API.

Sources: https://developers.cloudflare.com/workers/runtime-apis/websockets/

#### TCP sockets (`connect()`)

```ts
import { connect } from "cloudflare:sockets";
const socket = connect({ hostname: "example-postgres-db.com", port: 5432 }, { secureTransport: "starttls" });
const secureSocket = socket.startTls();
```

- `connect(address, { secureTransport: "off" | "on" | "starttls", allowHalfOpen })` returns a `Socket` with `readable`, `writable`, `opened`, `closed`, `close()` and `startTls()`.
- TCP Sockets are listed as a public beta on the Workers Betas page as of 2026-10-05.
- Outbound connections to Cloudflare IP ranges, `localhost` and private network IPs are blocked; port 25 is prohibited; connecting back to the same Worker fails with `TCP Loop detected`.
- Sockets cannot be created in global scope or shared across requests.
- Each open socket counts toward the simultaneous open connections limit.
- In a Durable Object, an open socket keeps the object in memory (and billing duration) for up to 15 minutes per connection.
- Inbound TCP to a Worker is "coming soon" and not possible today.
- TCP outbound connections come from a prefix that is not on Cloudflare's published IP list.
- For PostgreSQL the docs recommend Hyperdrive instead.

Sources: https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/, https://developers.cloudflare.com/workers/platform/betas/, https://developers.cloudflare.com/workers/reference/protocols/

#### Context: waitUntil, passThroughOnException, props, exports

- `ctx.waitUntil(promise)` keeps work running after the response for up to 30 seconds after the response is sent or the client disconnects, shared across all `waitUntil()` calls in that request; unsettled promises are then cancelled.
- If work cannot finish in that window, the docs say to send it to a Queue.
- An async call that is neither awaited nor passed to `waitUntil()` can be cancelled when the invocation ends.
- `ctx.passThroughOnException()` fails open to the origin on uncaught exceptions, but cannot resend a body already consumed and does not help with CPU or memory limit errors.
- `ctx.props` carries trusted per-binding configuration set in the caller's service binding (`"props": {...}`); only someone who can deploy the callee's binding config can set it.
- `ctx.exports` (flag `enable_ctx_exports`) gives automatic loopback bindings for every top-level `WorkerEntrypoint`, `DurableObject` and `WorkflowEntrypoint` export, and lets the caller set `props` dynamically: `ctx.exports.Greeter({ props: { greeting: "Welcome" } })`.

Sources: https://developers.cloudflare.com/workers/runtime-apis/context/

#### Service bindings and RPC

```jsonc
{ "services": [ { "binding": "DOC_SERVICE", "service": "doc-worker", "entrypoint": "DocServiceApi", "props": { "clientId": "frontend-worker" } } ] }
```

- Two interfaces: RPC (`await env.BINDING.myMethod(arg)`, recommended) and HTTP (`env.BINDING.fetch(request)`).
- By default both Workers run on the same thread of the same server, with "zero overhead"; service-binding calls do not add request fees on the Standard model (one request billed, CPU summed across both Workers).
- Limits: a single request can have at most 32 Worker invocations, and each service binding call counts toward it; each call counts toward the subrequest limit; calls do not count toward simultaneous open connections; maximum serialized RPC payload is 32 MiB (use `ReadableStream` for more).
- Cloudflare Access does not propagate `ctx.access` from Worker A to Worker B.

Sources: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/, https://developers.cloudflare.com/workers/runtime-apis/rpc/, https://developers.cloudflare.com/workers/platform/pricing/

#### Rate Limiting binding

```jsonc
{ "ratelimits": [ { "name": "MY_RATE_LIMITER", "namespace_id": "1001", "simple": { "limit": 100, "period": 60 } } ] }
```

- `const { success } = await env.MY_RATE_LIMITER.limit({ key })`; `period` must be `10` or `60` seconds; `simple` is the only type; needs Wrangler 4.36.0 or later.
- Counters are local to each Cloudflare location, cached on the machine and synced asynchronously, so the limiter is "permissive, eventually consistent" and not an accounting system.
- Bindings sharing a `namespace_id` share counters, even across Workers.
- The docs recommend keys such as API keys, user IDs or routes, not IP addresses.
- Not available in Pages Functions.

Sources: https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/, https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/

#### Node.js compatibility

- For compatibility dates on or after `2026-08-04`, `nodejs_compat` and `nodejs_compat_v2` are enabled by default; for `2024-09-23` through `2026-08-03` add `"compatibility_flags": ["nodejs_compat"]`; to disable on new dates add both `no_nodejs_compat` and `no_nodejs_compat_v2`.
- Fully supported natively: assert, AsyncLocalStorage, Buffer, crypto, diagnostics_channel, events, fs, globals, http, https, net, path, process, punycode, querystring, stream, string_decoder, timers, url, util, Web Crypto, Web Streams, zlib.
- Partially supported: console, dns, module, os, perf_hooks, test runner, tls.
- Non-functional stubs (importable only) are enabled by date: `node:http2` (2025-09-01), `node:vm` (2025-10-01), cluster/domain/trace_events/wasi (2025-12-04), _stream_wrap/dgram/inspector/sqlite (2026-01-29), child_process/readline/repl/tty/v8/worker_threads (2026-03-17).
- Everything else is polyfilled by Wrangler through unenv; calling an unimplemented method throws `[unenv] <method> is not implemented yet!`.
- `nodejs_als` enables only AsyncLocalStorage.

Sources: https://developers.cloudflare.com/workers/runtime-apis/nodejs/

#### Web Crypto

The supported-algorithms table lists ECDSA, Ed25519, X25519 and the legacy non-standard `NODE-ED25519`; secp256k1 does not appear on the page (as of 2026-10-05).

Sources: https://developers.cloudflare.com/workers/runtime-apis/web-crypto/

### Configuration (Wrangler)

- Config file: `wrangler.jsonc` (recommended in examples), `wrangler.json` or `wrangler.toml`; `name`, `main` and `compatibility_date` are required (`main` is optional for assets-only Workers).
- A typed `cloudflare.config.ts` format exists and is in open beta (as of 2026-10-05).
- Top-level-only keys: `keep_vars`, `addresses` (Email Routing inbound addresses), `send_metrics`, `dependencies_instrumentation`, `site` (deprecated Workers Sites).
- Inheritable keys (overridable per environment): `name`, `main`, `compatibility_date`, `account_id`, `compatibility_flags`, `workers_dev`, `preview_urls`, `route`/`routes`, `tsconfig`, `triggers`, `rules`, `build`, `no_bundle`, `find_additional_modules`, `base_dir`, `preserve_file_names`, `minify`, `keep_names`, `logpush`, `limits`, `observability`, `assets`, `exports`, `migrations` (legacy), `placement`.
- Non-inheritable keys (must be repeated per environment): `define`, `vars`, `durable_objects`, `kv_namespaces`, `r2_buckets`, `analytics`, `ai_search_namespaces`, `ai_search`, `vectorize`, `services`, `queues`, `workflows`, `tail_consumers`, `secrets` (`required` list), `secrets_store_secrets`.
- Automatic provisioning: bindings declared without IDs are created on deploy for KV, R2, D1, Flagship, AI Search, Agent Memory, Dispatch Namespaces and Queues, with IDs written back to the config file.
- `exports` declares Durable Object classes and their lifecycle (`created`, `deleted`, `renamed`, `transferred`, `expecting-transfer`) and Workflows; for new Workers it is preferred over the legacy `migrations` key.
- Worker names: alphanumerics and dashes, up to 255 characters, 63 if used on `workers.dev`.

Sources: https://developers.cloudflare.com/workers/wrangler/configuration/

`limits` block (Standard usage model only, enforced only when deployed):

```jsonc
{ "limits": { "cpu_ms": 300000, "subrequests": 150 } }
```

`subrequests` defaults to 50 (Free) and 10,000 (Paid); maximum 50 on Free and 10,000,000 on Paid.

Sources: https://developers.cloudflare.com/workers/wrangler/configuration/, https://developers.cloudflare.com/workers/platform/limits/

#### Cron Triggers

```jsonc
{ "triggers": { "crons": ["*/3 * * * *", "0 15 1 * *", "59 23 LW * *"] } }
```

- Handler: `async scheduled(controller, env, ctx)`; `controller.cron`, `controller.scheduledTime` (ms), `controller.type === "scheduled"`, `controller.noRetry()`.
- Five-field cron with Quartz-like extensions (`L`, `W`, `#`); weekdays are 1 = Sunday to 7 = Saturday; times are UTC; finest granularity is one minute.
- Changes take up to 15 minutes to propagate; deploying with `crons: []` removes all; omitting `triggers` leaves existing ones.
- Cron Events shows the 100 most recent invocations; local testing via `curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"`.
- Crons run on underutilized machines; Green Compute (public beta) restricts them to renewable-powered data centers.
- Workflows can also be scheduled directly through `schedules` on the Workflow binding.
- Limits: 5 Cron Triggers per account on Free, 250 on Paid; CPU 10 ms (Free), 30 seconds for intervals under 1 hour and 15 minutes for intervals of 1 hour or more (Paid); 15 minutes wall time.

Sources: https://developers.cloudflare.com/workers/configuration/cron-triggers/, https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/, https://developers.cloudflare.com/workers/platform/limits/

#### Placement (Smart Placement and Placement Hints)

```jsonc
{ "placement": { "mode": "smart" } }   // or "region": "aws:us-east-1" | "host": "db.example.com:5432" | "hostname": "api.example.com"
```

- By default a Worker runs in the data center nearest the request; placement moves it near back ends.
- `mode: "smart"` analyzes request duration across locations (up to 15 minutes after deploy), only places in locations where the Worker already runs, keeps 1% of requests unrouted as a baseline, and reports `SUCCESS`, `INSUFFICIENT_INVOCATIONS` or `UNSUPPORTED_APPLICATION`.
- `region` accepts `aws:`, `gcp:` and `azure:` region IDs; `host` (TCP probe) and `hostname` (HTTP HEAD probe) target single-homed services and are "experimental".
- Placement only affects `fetch` handlers, not RPC methods or named entrypoints; static assets are still served nearest the user.
- A `cf-placement` header (`remote-LHR`, `local-EWR`) shows where the request ran.
- Smart Placement is available on all Workers plans.

Sources: https://developers.cloudflare.com/workers/configuration/placement/

#### Routes, custom domains and workers.dev

- Routing options are Custom Domains, Routes (zone patterns) and `workers.dev`.
- Limits: 1,000 routes per zone (50 when using `wrangler dev --remote` or the dashboard Quick Editor), 100 custom domains per zone, 1,000 routed zones per Worker.
- Above those limits the docs point to Workers for Platforms (routes) or wildcard routes (custom domains).
- Known issue: a trailing `/*` in route patterns may not match as expected (for example `example.com/images*` beats `example.com/images/*`).
- Free-plan daily request overage behaviour per route: fail open (bypass the Worker) or fail closed (Error 1027).

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/platform/known-issues/

### Static assets

```jsonc
{ "name": "my-spa", "main": "src/index.js", "compatibility_date": "2026-10-05",
  "assets": { "directory": "./dist", "binding": "ASSETS", "not_found_handling": "single-page-application" } }
```

- Assets and Worker code deploy together as one unit; the `ASSETS` binding lets code call `env.ASSETS.fetch(request)`.
- `run_worker_first` (default `false`) controls whether matching assets are served before the Worker; `true` (or a pattern list) runs the Worker first, for auth or middleware.
- `not_found_handling`: `single-page-application`, `404-page` or `none`; `html_handling`: `auto-trailing-slash`, `force-trailing-slash`, `drop-trailing-slash`, `none`.
- `_headers` and `_redirects` files are supported (limits below).
- Billing: requests to static assets are free and unlimited, and storing assets costs nothing; requests that invoke the Worker are billed normally.
- Free-plan caveat: requests matching `run_worker_first` always invoke the Worker and receive 429 once the free daily request limit is exceeded, instead of falling back to assets.
- Limits (as of 2026-10-05): 20,000 files per version on Free and 100,000 on Paid (Wrangler 4.34.0 or later), 25 MiB per file, 100 `_headers` rules, 2,000 characters per header line, 2,000 static plus 100 dynamic redirects (2,100 total), 1,000 characters per redirect rule.
- With Smart Placement, `run_worker_first=true` sends every asset request through the placed Worker (more latency); `false` keeps assets near users.
- Migration guides exist from Pages, Netlify and Vercel.

Sources: https://developers.cloudflare.com/workers/static-assets/, https://developers.cloudflare.com/workers/static-assets/binding/, https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/, https://developers.cloudflare.com/workers/platform/limits/

### Workers Cache

- Workers Cache returns cached HTTP responses from a Worker without running the Worker; it is enabled with `"cache": { "enabled": true }` (per entrypoint overrides possible under `exports`).
- The cache belongs to the Worker, not to a zone: zone Cache Rules, Page Rules and cache settings do not apply; the Worker controls caching through `Cache-Control` headers (RFC 9111) and programmatic purges.
- The cache key includes request path, entrypoint, `ctx.props` and, by default, the Worker version, but not the hostname.
- It is tiered by default (lower tier near the user, upper tier shared) and collapses concurrent requests per cache key per data center, unlike the Cache API.
- Only `GET` and `HEAD` are cached; WebSocket upgrades, custom RPC methods, cron, queue, Workflows, Tail Workers and Durable Object invocations bypass it; 520 to 526 and 206 responses are never stored; there is no purge by host and no pre-warming.
- Billing: cache hits are billed at the normal per-request rate (including hits for static assets and Worker-to-Worker invocations), but CPU time is billed only when the Worker runs.

Sources: https://developers.cloudflare.com/workers/cache/, https://developers.cloudflare.com/workers/cache/limitations/, https://developers.cloudflare.com/workers/platform/pricing/

### Languages

- **JavaScript and TypeScript**: first-class; `wrangler types` generates `env` and `ctx.exports` types; `@cloudflare/workers-types` v5 exposes only the latest runtime types (dated entrypoints removed).
- **Python**: runs on Pyodide (CPython compiled to WebAssembly) inside a V8 isolate; needs the `python_workers` compatibility flag; tooling is `pywrangler` (`uvx --from workers-py pywrangler init`, `uv run pywrangler dev`, `uv run pywrangler deploy`); supports pure-Python and PyEmscripten wheels from PyPI plus Pyodide's bundled packages (FastAPI, Langchain, Pydantic, Django, Flask are documented); a memory snapshot of top-level imports is taken at deploy time to cut cold starts; an FFI exposes JS APIs and bindings; new Pyodide versions arrive behind compatibility flags.
  The mirrored pages do not label Python Workers as beta (as of 2026-10-05).
- **Rust**: `workers-rs` crate, compiled to `wasm32-unknown-unknown` and built with `worker-build`; scaffold with `cargo generate cloudflare/workers-rs`; a supported-crates page lists what compiles.
- **WebAssembly**: other languages via Wasm modules.

Sources: https://developers.cloudflare.com/workers/languages/python/, https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/, https://developers.cloudflare.com/workers/languages/python/packages/, https://developers.cloudflare.com/workers/languages/rust/, https://developers.cloudflare.com/workers/languages/typescript/

### Frameworks

- Guides exist for React + Vite, Astro, React Router (formerly Remix), Next.js, OpenNext adapter, Vue, RedwoodSDK, TanStack Start, Microfrontends, SvelteKit, Vike, Analog, Angular, Docusaurus, Gatsby, Hono, Nuxt, Qwik, Solid (SolidStart in beta), Waku, plus Expo (mobile), FastAPI, Flask, Hono (APIs) and the Agents SDK and LangChain (AI).
- For Next.js, Cloudflare now recommends vinext (a Vite plugin reimplementing the Next.js API surface, in beta) as the default path; OpenNext remains documented as another path.
- "Deploy an existing project" covers automatic configuration of existing projects.

Sources: https://developers.cloudflare.com/workers/framework-guides/, https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/

### Local development and testing

- `wrangler dev` (Miniflare-based local simulation) and the Cloudflare Vite plugin are the two local dev paths; bindings are simulated locally by default or can use remote bindings against real resources; `wrangler dev --remote` runs on Cloudflare.
- Testing: `@cloudflare/vitest-plugin` (Vitest integration, including Vitest 4), Miniflare, an integration test harness, and `unstable_startWorker()`.
- Known issue: `wrangler dev --remote` adds a `cf-workers-preview-token` header to outgoing requests, which causes requests to other Cloudflare zones to be discarded unless you delete that header.

Sources: https://developers.cloudflare.com/workers/local-development/, https://developers.cloudflare.com/workers/testing/, https://developers.cloudflare.com/workers/platform/known-issues/

### Versions, deployments and Previews

- Gradual deployments split traffic between two versions by percentage (`wrangler versions upload` then `wrangler versions deploy`).
- Version affinity: send `Cloudflare-Workers-Version-Key: <key>` to pin a key to one version; users already moved to the new version stay on it as the percentage rises.
- Version overrides: `Cloudflare-Workers-Version-Overrides: my-worker="<version-id>"` targets a specific version for smoke tests.
- With Durable Objects, each object is assigned a version and keeps it until the deployment changes.
- Limits: deployments and gradual deployments only from the last 100 uploaded versions; rollbacks only to the 100 most recent versions; Wrangler lists the 100 most recent versions and deployments; only the 1,000 most recently deployed aliases are kept, and alias plus Worker name must fit in 63 characters.
- Previews (needs Wrangler 4.135.0 or later): `npx wrangler preview` creates an isolated, production-like environment per branch under the same Worker, with its own variables, secrets, bindings, URLs and observability; each Preview gets a fresh Durable Object namespace and container instances; Routes, Cron Triggers and queue consumers stay on production; limits are 100 Previews per Worker on Free and 500 on Paid.

Sources: https://developers.cloudflare.com/workers/versions-and-deployments/, https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/, https://developers.cloudflare.com/workers/versions-and-deployments/version-overrides/, https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/, https://developers.cloudflare.com/workers/previews/

### CI/CD (Workers Builds)

| Metric (as of 2026-10-05) | Free | Paid |
| --- | --- | --- |
| Build minutes | 3,000 per month | 6,000 per month, then $0.005 per minute |
| Concurrent builds | 1 | 6 |
| Build timeout | 20 minutes | 20 minutes |
| Deploy Hooks | 10/min per Worker, 100/min per account | same |
| CPU / memory / disk | 2 vCPU / 8 GB / 20 GB | 4 vCPU / 8 GB / 20 GB |
| Build env vars | 64, 5 KB each | 64, 5 KB each |

Git integrations exist for GitHub, GitLab, Cloudflare Artifacts and Cursor Origin; external CI guides cover GitHub Actions and GitLab CI/CD.

Sources: https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/, https://developers.cloudflare.com/workers/ci-cd/

### Observability

| Feature | Status / plan (as of 2026-10-05) | Pricing and retention |
| --- | --- | --- |
| Workers Logs | GA, Free and Paid | Free: 200,000 log events per day, 3 days retention; Paid: 20 million per month included, then $0.60 per million, 7 days retention; max 5 billion logs per account per day, then 1% head sampling |
| Traces (OpenTelemetry-compatible) | Beta | 7 days retention |
| OpenTelemetry export | Documented | `persist` defaults to `true` (also stored in Cloudflare) |
| Workers Logpush (Trace Events) | Paid only | 10 million per month included, then $0.05 per million |
| Tail Workers | Paid and Enterprise; labelled beta on the overview | Billed by CPU time, not requests |
| Real-time logs (`wrangler tail`) | Free and Paid | May enter sampling mode at high volume |
| Issues | Open beta | Free during beta |
| Metrics, Query Builder, source maps, DevTools CPU and memory profiling | Documented | Not priced separately |

- `head_sampling_rate` (0 to 1, default 1) samples logs and, separately, traces.
- Beginning December 1, 2026, Workers Logs, stored traces and persisted OTel data move to Cloudflare Observability pricing.
- Log data per request is capped at 256 KB.

Sources: https://developers.cloudflare.com/workers/platform/pricing/, https://developers.cloudflare.com/workers/observability/logs/workers-logs/, https://developers.cloudflare.com/workers/observability/traces/, https://developers.cloudflare.com/workers/observability/opentelemetry-export/, https://developers.cloudflare.com/workers/observability/logs/tail-workers/, https://developers.cloudflare.com/workers/observability/, https://developers.cloudflare.com/workers/platform/limits/

### Limits (as of 2026-10-05)

| Limit | Workers Free | Workers Paid |
| --- | --- | --- |
| Requests | 100,000 per day (resets 00:00 UTC; Error 1027 after) | No limit |
| CPU time per HTTP request | 10 ms | 5 min max, default 30 s (`limits.cpu_ms`) |
| CPU time per Cron Trigger | 10 ms | 30 s (interval under 1 h), 15 min (interval 1 h or more) |
| Memory per isolate | 128 MB | 128 MB |
| Subrequests per invocation | 50 | 10,000 default, configurable up to 10,000,000 |
| Subrequests to internal services | 1,000 | Matches configured limit (default 10,000) |
| Simultaneous outgoing connections waiting for headers | 6 | 6 |
| Environment variables (secrets plus text) | 64 per Worker | 128 per Worker |
| Environment variable size | 5 KB | 5 KB |
| Worker size (uncompressed) | 64 MiB | 64 MiB |
| Startup time (global scope) | 1 s | 1 s |
| Workers per account | 100 | 500 (more via Workers for Platforms) |
| Cron Triggers per account | 5 | 250 |
| Static asset files per version | 20,000 | 100,000 |
| Static asset file size | 25 MiB | 25 MiB |
| Cache API calls per request | 50 | 1,000 |
| Cache API max object size | 512 MB | 512 MB |
| Log data per request | 256 KB | 256 KB |
| URL size | 16 KB | 16 KB |
| Request / response headers | 128 KB total each | 128 KB total each |
| Response body | No enforced limit (CDN cache limit 512 MB, 5 GB Enterprise) | same |

Request body size depends on the zone plan: 100 MB (Free, Pro), 200 MB (Business), up to 5 GB self-serve (Enterprise); oversize returns 413.

Wall time by invocation type: HTTP requests unlimited while the client stays connected (plus up to 30 s of `waitUntil()`), Cron Triggers 15 min, Queue consumers 15 min, Durable Object alarms 15 min, Durable Object RPC/HTTP unlimited while the caller is connected, Workflows steps unlimited (CPU-limited).
Runtime updates give in-flight requests a 30-second grace period before termination.

Bundled-plan Workers (deprecated) keep 50 subrequests, 50 ms CPU and 50 Cache API calls per request.

Sources: https://developers.cloudflare.com/workers/platform/limits/

### Pricing (as of 2026-10-05)

| Item | Free | Paid (Standard) |
| --- | --- | --- |
| Base | $0 | $5 per month minimum per account |
| Requests | 100,000 per day | 10 million per month included, then $0.30 per million |
| CPU time | 10 ms per invocation | 30 million CPU-ms per month included, then $0.02 per million CPU-ms |
| Duration (wall time) | Not charged | Not charged |
| Subrequests | Not billed | Not billed |
| Static asset requests | Free, unlimited | Free, unlimited |
| WebSocket | Upgrade request billed once; messages through a Worker are not requests | same |
| Egress / bandwidth | No charge | No charge |

- Worked example from the docs: 15 million requests at 7 ms CPU average costs $8.00 per month ($5 + $1.50 requests + $1.50 CPU); 100 million requests at 7 ms costs $45.40.
- Service bindings: one billed request for the chain, CPU summed.
- The Workers Paid plan also covers Pages Functions, KV, Hyperdrive and Durable Objects usage; the pricing page also lists Queues, Workflows, D1, Vectorize, R2 and Containers rates (reproduced in each product section below).
- Custom CPU limits are the recommended guard against runaway bills and "denial-of-wallet" attacks.

Sources: https://developers.cloudflare.com/workers/platform/pricing/

### How it composes with other products

- Durable Objects, Workflows and Containers are classes exported from a Worker and reached through bindings.
- Queues producers are bindings; consumers are the `queue` handler of a Worker.
- Email Routing delivers to a Worker's `email` handler; Email Sending is a binding.
- Browser Run, Workers AI, D1, KV, R2, Hyperdrive, Vectorize, Images, Flagship and Analytics Engine are bindings.
- Workers for Platforms runs customer Workers in dispatch namespaces behind a dispatch Worker; Dynamic Workers load code at runtime through a Worker Loader binding.
- Workers VPC gives Workers access to private networks through VPC service bindings.

Sources: https://developers.cloudflare.com/workers/runtime-apis/bindings/, https://developers.cloudflare.com/workers/runtime-apis/handlers/

### Other platform features

- **Claim deployments**: deploy Workers before authenticating, into a temporary account, then claim it to keep the deployments and resources.
- **Infrastructure as code**: Terraform, Pulumi and the Cloudflare API SDKs can deploy and manage Workers.
- **Deploy to Cloudflare** and **Built with Cloudflare** buttons for repositories.
- **Workers Sites** is deprecated in Wrangler v4 ("Do not use Workers Sites for new projects"); use static assets.
- **Roles and permissions**: Developer Platform roles apply at platform, product and resource scopes, with pages for Workers and Durable Objects.
- **Local Explorer** browses and edits local binding data during development; **Prompting** covers building Workers with AI prompts and MCP servers.

Sources: https://developers.cloudflare.com/workers/platform/claim-deployments/, https://developers.cloudflare.com/workers/platform/infrastructure-as-code/, https://developers.cloudflare.com/workers/platform/deploy-buttons/, https://developers.cloudflare.com/workers/platform/built-with-cloudflare/, https://developers.cloudflare.com/workers/configuration/sites/, https://developers.cloudflare.com/workers/authorization/, https://developers.cloudflare.com/workers/local-development/local-explorer/, https://developers.cloudflare.com/workers/get-started/prompting/

### Best practices (the docs' checklist)

Configuration: keep the compatibility date current; enable `nodejs_compat`; generate binding types with `wrangler types`; store secrets with `wrangler secret`, not in source; configure environments deliberately; set up custom domains or routes correctly.
Requests: stream request and response bodies; use `waitUntil` for work after the response.
Architecture: use bindings rather than REST APIs; use Queues and Workflows for async work; use service bindings for Worker-to-Worker calls; use Hyperdrive for external databases; use Durable Objects for WebSockets; use Workers Static Assets for new projects.
Observability: enable Workers Logs and Traces.
Code: do not store request-scoped state in global scope; always await or `waitUntil` promises.
Security: use Web Crypto for token generation; do not use `passThroughOnException` as error handling.
Testing: use `@cloudflare/vitest-plugin`.

Sources: https://developers.cloudflare.com/workers/best-practices/workers-best-practices/

### Most useful pages

- [Workers overview](https://developers.cloudflare.com/workers/) - entry point
- [Limits](https://developers.cloudflare.com/workers/platform/limits/) - every runtime and account limit
- [Pricing](https://developers.cloudflare.com/workers/platform/pricing/) - Workers plus the bundled data products
- [Betas](https://developers.cloudflare.com/workers/platform/betas/) - what is still beta
- [Known issues](https://developers.cloudflare.com/workers/platform/known-issues/) - route matching, CNAME fetch, IP fetch
- [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) - full binding list and `env` rules
- [Context](https://developers.cloudflare.com/workers/runtime-apis/context/) - waitUntil, props, exports
- [Fetch](https://developers.cloudflare.com/workers/runtime-apis/fetch/) - outbound HTTP behaviour
- [WebSockets](https://developers.cloudflare.com/workers/runtime-apis/websockets/) - message size, close and binary behaviour
- [TCP sockets](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) - `connect()` and its restrictions
- [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) - supported modules and flags
- [RPC](https://developers.cloudflare.com/workers/runtime-apis/rpc/) - WorkerEntrypoint and RpcTarget
- [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) - Worker-to-Worker
- [Rate Limiting binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) - per-location limiter
- [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) - every config key
- [Compatibility flags](https://developers.cloudflare.com/workers/configuration/compatibility-flags/) - runtime behaviour switches
- [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/) - scheduling
- [Placement](https://developers.cloudflare.com/workers/configuration/placement/) - Smart Placement and region hints
- [Static assets](https://developers.cloudflare.com/workers/static-assets/) - hosting front ends
- [Migrate from Pages](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/) - migration and compatibility matrix
- [Workers Cache](https://developers.cloudflare.com/workers/cache/) - caching Worker responses
- [Versions and deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) - gradual rollouts
- [Previews](https://developers.cloudflare.com/workers/previews/) - per-branch environments
- [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) - logging and pricing
- [Builds limits and pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) - CI
- [Python Workers](https://developers.cloudflare.com/workers/languages/python/) - Pyodide-based Python
- [Rust](https://developers.cloudflare.com/workers/languages/rust/) - workers-rs
- [Best practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) - production checklist
- [Storage options](https://developers.cloudflare.com/workers/platform/storage-options/) - choosing a data product
- Examples most relevant to API backends (48 examples in total as of 2026-10-05): [CORS header proxy](https://developers.cloudflare.com/workers/examples/cors-header-proxy/), [Auth with headers](https://developers.cloudflare.com/workers/examples/auth-with-headers/), [Using timingSafeEqual](https://developers.cloudflare.com/workers/examples/protect-against-timing-attacks/), [Sign requests](https://developers.cloudflare.com/workers/examples/signing-requests/), [Aggregate requests](https://developers.cloudflare.com/workers/examples/aggregate-requests/), [Cache POST requests](https://developers.cloudflare.com/workers/examples/cache-post-request/), [Stream large JSON](https://developers.cloudflare.com/workers/examples/streaming-json/), [Using the WebSockets API](https://developers.cloudflare.com/workers/examples/websockets/), [Multiple Cron Triggers](https://developers.cloudflare.com/workers/examples/multiple-cron-triggers/), [Turnstile with Workers](https://developers.cloudflare.com/workers/examples/turnstile-html-rewriter/)
- Tutorials (18 in total as of 2026-10-05) include a real-time chat app, Express.js on Workers, PostgreSQL and MySQL connections, Turso, Prisma Postgres, R2 uploads, a Slackbot and Workers KV from Rust: [Tutorials](https://developers.cloudflare.com/workers/tutorials/)

## 3. Containers

### What it is

Containers run code in any language or runtime, packaged as a container image, as part of a Workers app, deployed to "Region:Earth" with `wrangler deploy`.
The docs target resource-heavy work (parallel CPU cores, large memory or disk), apps that need a full filesystem or Linux environment, and existing tools shipped as images.
Instances are started on demand and controlled from Worker code: every container instance is reached through its own Durable Object, which accesses it via `ctx.container`.

Sources: https://developers.cloudflare.com/containers/, https://developers.cloudflare.com/containers/concepts/architecture/

### Status

- Available on the Workers Paid plan only (no Free allowance), as of 2026-10-05.
- The overview carries no beta label; the `durable_object` scheduling policy is in public beta; built-in autoscaling for stateless apps is "not today" (planned).

Sources: https://developers.cloudflare.com/containers/, https://developers.cloudflare.com/containers/configuration/scheduling-policy/, https://developers.cloudflare.com/containers/faq/

### Key concepts

- **Container application**: a set of instances tied to a Durable Object class (`class_name`).
- **Scheduling policy** (immutable per application):
  - `default`: image, `instance_type` and `max_instances` are set in Wrangler config; changes roll out across the application.
  - `durable_object` (public beta): Durable Object code picks the image (or snapshot) and instance size in each `ctx.container.start()` call; aimed at sandboxes and agent environments.
- **Two APIs**: the Durable Object Container API (`this.ctx.container`, recommended for new apps) and the older `Container` class from `@cloudflare/containers` (helpers such as `sleepAfter`, `getRandom`).
- **Runtime**: each instance runs in a Firecracker microVM with its own kernel and network; images must be `linux/amd64`.
- **Lifecycle**: stopped, starting, running (not ready), ready, stopping, stopped; `ctx.container.running` turns true before the port is ready, so check port readiness first.
- **Shutdown**: on stop the platform sends `SIGTERM`, waits up to 15 minutes, then `SIGKILL`; there is no fixed maximum runtime, but host restarts can stop instances at any time.
- **Cold starts** are "often in the 1-3 second range", depending on image size and startup code.
- **Placement**: a starting instance picks the nearest location with a pre-fetched image; later requests go there while it lives; a Durable Object and its container are not guaranteed to be co-located.
- **Disk** is ephemeral; `durable_object`-policy apps can take snapshots (up to 20 GB, kept 30 days from creation or last restore); R2 can be mounted with FUSE.
- **Inbound**: only HTTP via a Worker; end users cannot open raw TCP or UDP to a container.
- **OOM**: the instance throws and restarts; there is no swap.

Sources: https://developers.cloudflare.com/containers/configuration/scheduling-policy/, https://developers.cloudflare.com/containers/concepts/architecture/, https://developers.cloudflare.com/containers/faq/, https://developers.cloudflare.com/containers/platform/limits/

### API and binding surface

Overview example (Durable Object Container API):

```js
import { DurableObject } from "cloudflare:workers";
export class MyContainer extends DurableObject {
  async fetch(request) {
    const container = this.ctx.container;
    await startAndWaitForPort(container, { port: 4000, inactivityTimeout: 10 * 60 * 1000 });
    return container.getTcpPort(4000).fetch(rewriteRequestForContainer(request));
  }
}
export default {
  async fetch(request, env) {
    const { "session-id": sessionId } = await request.clone().json();
    return env.MY_CONTAINER.getByName(sessionId).fetch(request);
  },
};
```

(`startAndWaitForPort` and `rewriteRequestForContainer` are helpers from the example's own `./utils`.)

- `ctx.container` members: `images` (durable_object policy), `running`, `start(options)`, `inspect()`, `exec()`, `snapshotContainer()` (durable_object policy), `destroy()`, `signal()`, `setInactivityTimeout()`, `getTcpPort(port)`, `monitor()`, `interceptOutboundHttp()`, `interceptAllOutboundHttp()`, `interceptOutboundHttps()`.
- `Container` class members: `onStart`, `onStop`, `onError`, `onActivityExpired`, `fetch`, `containerFetch`, `startAndWaitForPorts`, `start`, `waitForPort`, `stop`, `destroy`, `getState`, `renewActivityTimeout`, `schedule`; helpers `getContainer`, `getRandom`, `switchPort`; `sleepAfter` defaults to 10 minutes.
- Outbound control: `enableInternet = false` blocks the public internet (only ports 80 and 443 then, for allowed traffic); `allowedHosts` / `deniedHosts` with glob patterns; `outbound` / `outboundByHost` handlers can inject auth headers, reroute traffic or expose Workers bindings (KV, R2, Durable Objects) to the container; export `ContainerProxy` from the Worker for interception to work.
- Other guides: execute commands, SSH into instances, image management, local development, Workers Builds integration, rollouts.

Sources: https://developers.cloudflare.com/containers/, https://developers.cloudflare.com/containers/api/durable-object-container/, https://developers.cloudflare.com/containers/api/container-class/, https://developers.cloudflare.com/containers/configuration/outbound-traffic/, https://developers.cloudflare.com/containers/llms.txt

### Configuration

```jsonc
{ "containers": [ { "class_name": "ApiContainer", "scheduling_policy": "default",
    "image": "./api/Dockerfile", "instance_type": "standard-1", "max_instances": 5 } ] }
```

- Omitting `scheduling_policy` selects `default`; one config can hold applications with both policies.
- Custom instance types use `vcpu`, `memory_mib`, `disk_mb` in Wrangler (`vcpu`, `memoryMib`, `diskMb` in `ctx.container.start()`).
- Rollout step sizes are configurable (5, 10, 20, 25, 50 or 100 percent, or an ascending array).
- Worker code goes live on deploy before an application-wide container rollout finishes.
- Scaling today is manual: address instances by ID, or use `getRandom(env.NS, N)` to spread stateless traffic over N instances.

Sources: https://developers.cloudflare.com/containers/configuration/scheduling-policy/, https://developers.cloudflare.com/workers/wrangler/configuration/, https://developers.cloudflare.com/containers/configuration/scaling-and-routing/, https://developers.cloudflare.com/containers/concepts/architecture/

### Limits (as of 2026-10-05)

| Instance type | vCPU | Memory | Disk |
| --- | --- | --- | --- |
| lite (alias `dev`) | 1/16 | 256 MiB | 2 GB |
| basic | 1/4 | 1 GiB | 4 GB |
| standard-1 (alias `standard`) | 1/2 | 4 GiB | 8 GB |
| standard-2 | 1 | 6 GiB | 12 GB |
| standard-3 | 2 | 8 GiB | 16 GB |
| standard-4 | 4 | 12 GiB | 20 GB |

- Custom instance types: 1 to 4 vCPU, up to 12 GiB memory and 20 GB disk, at least 3 GiB memory per vCPU.
- Account limits: 6 TiB concurrent memory, 1,500 concurrent vCPU, 30 TB concurrent disk, image size up to the instance disk, 50 GB total image storage.
- Snapshots: 20 GB max, 30-day retention.

Sources: https://developers.cloudflare.com/containers/platform/limits/

### Pricing (as of 2026-10-05)

| Dimension | Included with Workers Paid | Overage |
| --- | --- | --- |
| Memory | 25 GiB-hours per month | $0.0000025 per GiB-second |
| CPU | 375 vCPU-minutes per month | $0.000020 per vCPU-second |
| Disk | 200 GB-hours per month | $0.00000007 per GB-second |
| Egress, North America and Europe | 1 TB per month | $0.025 per GB |
| Egress, Oceania, Korea, Taiwan | 500 GB per month | $0.05 per GB |
| Egress, everywhere else | 500 GB per month | $0.04 per GB |

- Billing is per 10 ms of active running; it starts when a request arrives or the instance is started and stops when the instance sleeps.
- Memory and disk are billed on provisioned size; CPU on active usage only.
- The fronting Worker and each container's Durable Object are billed separately at their own rates; container logs bill as Workers Logs.

Sources: https://developers.cloudflare.com/containers/platform/pricing/

### How it composes with other products

- Workers route requests; Durable Objects own each instance; Workers Logs captures container logs.
- Outbound handlers let containers use Workers bindings (KV, R2, Durable Objects).
- Workers VPC or outbound interception can reach private services.
- Previews provision separate container instances per Preview.
- The scheduling-policy page recommends the `durable_object` policy for "Sandboxes, agent environments, and other workloads that need per-instance configuration".

Sources: https://developers.cloudflare.com/containers/configuration/outbound-traffic/, https://developers.cloudflare.com/containers/configuration/scheduling-policy/, https://developers.cloudflare.com/workers/previews/

### Most useful pages

- [Containers overview](https://developers.cloudflare.com/containers/) - entry point
- [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) - cold starts, placement, shutdown
- [Scheduling policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/) - default vs durable_object
- [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) - `ctx.container`
- [Container class](https://developers.cloudflare.com/containers/api/container-class/) - helper class
- [Handle outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) - egress control
- [Scaling and routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/) - manual scaling, getRandom
- [Limits and instance types](https://developers.cloudflare.com/containers/platform/limits/) - sizes and caps
- [Pricing](https://developers.cloudflare.com/containers/platform/pricing/) - rates
- [FAQ](https://developers.cloudflare.com/containers/faq/) - autoscaling, OOM, runtime length
- [Use snapshots](https://developers.cloudflare.com/containers/guides/snapshots/) - persisting disk state
- [Cron container example](https://developers.cloudflare.com/containers/examples/cron/) - scheduled jobs
- [WebSocket to container example](https://developers.cloudflare.com/containers/examples/websocket/) - streaming
- [Mount R2 with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/) - durable files

## 4. Durable Objects

### What it is

A Durable Object is a special kind of Worker that combines compute with storage.
Each object has a globally unique name, so requests from anywhere reach the same single instance, and each object has its own strongly consistent durable storage that lives with it.
Objects are provisioned close to where they are first requested, start quickly and shut down when idle.
The docs target coordination workloads: collaborative editing, chat, multiplayer games, live notifications, AI agents and distributed systems.

Sources: https://developers.cloudflare.com/durable-objects/, https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/

### Status

- Durable Objects is generally available (as of 2026-10-05).
- SQLite storage and `sql.exec` moved from beta to GA on 2025-04-07, the same day Durable Objects became available on the Workers Free plan (SQLite-backed classes only).
- Billing for SQLite storage started per the 2026-01-07 release note.
- Declarative class lifecycle with `exports` arrived on 2026-06-30.
- The key-value storage backend is legacy: on Paid it is only available to accounts that already have a KV-backed namespace.
- The WebGPU API inside Durable Objects works only in local development (flags `experimental`, `webgpu`) and cannot be deployed.

Sources: https://developers.cloudflare.com/durable-objects/platform/known-issues/, https://developers.cloudflare.com/durable-objects/release-notes/, https://developers.cloudflare.com/durable-objects/platform/limits/, https://developers.cloudflare.com/durable-objects/api/webgpu/

### Key concepts

- **Namespace and class**: a class exported by a Worker; each object in the namespace is addressed by an ID.
- **IDs**: `idFromName(name)` (deterministic), `newUniqueId()`, `idFromString(hex)`; `getByName(name)` returns a stub directly (since 2025-08-21) without waiting for a round trip.
- **Stub**: client handle used to call RPC methods or `fetch()` on the object; every RPC method call on a stub is its own billed request.
- **Single-threaded**: each object processes events one at a time; input and output gates protect storage consistency; `blockConcurrencyWhile()` blocks other events (use sparingly).
- **Global uniqueness**: enforced when an event starts and when storage is accessed; an object can be replaced during a network partition or software update, and in-flight requests that touch storage after that fail.
- **Lifecycle**: active in memory, idle hibernateable (hibernates after 10 seconds with no `setTimeout`/`setInterval` pending and no request in flight), idle non-hibernateable (evicted after 70 to 140 seconds of inactivity), hibernated (memory discarded, WebSockets stay connected, constructor reruns on next event), inactive.
Each operation prevents eviction for up to 15 minutes from its start.
- **Location hints**: `get(id, { locationHint: "enam" })` with `wnam`, `enam`, `sam`, `weur`, `eeur`, `apac`, `apac-ne`, `apac-se`, `oc`, `afr`, `me`.
- **Jurisdictions**: `env.NS.jurisdiction("eu")` restricts objects to `eu`, `us` or `fedramp` (FedRAMP-Moderate) data centers.
- **Code updates** roll out globally in an eventually consistent way, so a new Worker version may call an old object version; keep the Worker-to-object API forward and backward compatible.

Sources: https://developers.cloudflare.com/durable-objects/api/namespace/, https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/, https://developers.cloudflare.com/durable-objects/reference/data-location/, https://developers.cloudflare.com/durable-objects/platform/known-issues/, https://developers.cloudflare.com/durable-objects/release-notes/

### API and binding surface

Configuration with the declarative `exports` field (preferred for new Workers; a Worker uses either `exports` or the legacy `migrations` array, not both):

```jsonc
{
  "durable_objects": { "bindings": [ { "name": "MY_DURABLE_OBJECT", "class_name": "MyDurableObject" } ] },
  "exports": { "MyDurableObject": { "type": "durable-object", "storage": "sqlite" } }
}
```

Deleting, renaming or transferring a class is done by changing the entry's `state` to a tombstone (`deleted`, `renamed`, `transferred`, `expecting-transfer`); a class that is only in code and not declared in `exports` is ignored.
Legacy Workers use `migrations` with `new_sqlite_classes`.

Sources: https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/, https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/, https://developers.cloudflare.com/workers/wrangler/configuration/

Class and handlers (`import { DurableObject } from "cloudflare:workers"`):

- Base class methods: `fetch(request)`, `alarm(alarmInfo)`, `webSocketMessage(ws, message)`, `webSocketClose(ws, code, reason, wasClean)`, `webSocketError(ws, error)`, plus any public RPC methods; properties `this.ctx` (DurableObjectState) and `this.env`.
- `DurableObjectState` (`this.ctx`): `exports`, `waitUntil()` (exists for compatibility, not needed to stay alive), `blockConcurrencyWhile()`, `acceptWebSocket(ws, tags?)`, `getWebSockets(tag?)`, `setWebSocketAutoResponse(pair)`, `getWebSocketAutoResponse()`, `getWebSocketAutoResponseTimestamp(ws)`, `setHibernatableWebSocketEventTimeout(ms)` (max 604,800,000 ms, 7 days), `getHibernatableWebSocketEventTimeout()`, `getTags(ws)`, `abort()`, `id`, `storage`.
- WebSocket attachment: `ws.serializeAttachment(value)` and `ws.deserializeAttachment()` persist per-connection state across hibernation.
- Tags: up to 10 per WebSocket, each up to 256 characters.

Sources: https://developers.cloudflare.com/durable-objects/api/base/, https://developers.cloudflare.com/durable-objects/api/state/, https://developers.cloudflare.com/durable-objects/best-practices/websockets/

WebSocket Hibernation example (from the docs, trimmed):

```js
async fetch(request) {
  const [client, server] = Object.values(new WebSocketPair());
  this.ctx.acceptWebSocket(server); // unlike ws.accept(), lets the object hibernate
  return new Response(null, { status: 101, webSocket: client });
}
async webSocketMessage(ws, message) {
  ws.send(`[Durable Object] message: ${message}, connections: ${this.ctx.getWebSockets().length}`);
}
```

The Hibernation API allows up to 32,768 WebSocket connections per Durable Object, with CPU and memory as the practical limit.
The hibernatable `webSocketMessage` handler always receives binary data as `ArrayBuffer`.

Sources: https://developers.cloudflare.com/durable-objects/best-practices/websockets/, https://developers.cloudflare.com/workers/runtime-apis/websockets/

Storage API (`this.ctx.storage`, SQLite-backed):

- SQL: `sql.exec(query, ...bindings)` returning a cursor, `sql.databaseSize`.
- Point-in-time recovery: `getCurrentBookmark()`, `getBookmarkForTime(time)`, `onNextSessionRestoreBookmark(bookmark)`; restore to any point in the past 30 days.
- Synchronous KV API: `ctx.storage.kv.get/put/delete/list`.
- Asynchronous KV API: `get`, `put`, `delete`, `list` (with options), stored in a hidden SQLite table and billed as rows.
- Alarms: `getAlarm()`, `setAlarm(time)`, `deleteAlarm()`.
- Other: `deleteAll()`, `transactionSync()`, `transaction()`, `sync()`.

Sources: https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/

Alarms:

- One alarm per object at a time; `setAlarm()` overrides an existing one; times have millisecond granularity and usually fire within a few milliseconds.
- At-least-once execution, retried on throw with exponential backoff from 2 seconds, up to 6 retries.
- Many events can be multiplexed by storing a schedule in storage and rescheduling from `alarm()`.
- Alarm handlers have a 15-minute wall time limit; make them idempotent.

Sources: https://developers.cloudflare.com/durable-objects/api/alarms/, https://developers.cloudflare.com/workers/platform/limits/

### Configuration

- CPU per invocation (request, WebSocket message, alarm) defaults to 30 seconds and can be raised to 5 minutes with `limits.cpu_ms` (300,000); each incoming request or WebSocket message resets the 30-second budget.
- Durable Objects run on Free and Paid; Free is SQLite-only.
- With gradual deployments, each object is pinned to one Worker version until the deployment changes; the docs advise deploying Durable Object lifecycle changes separately from other code.

Sources: https://developers.cloudflare.com/durable-objects/platform/limits/, https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/

### Limits (as of 2026-10-05)

| Limit | SQLite-backed | KV-backed (legacy) |
| --- | --- | --- |
| Number of objects | Unlimited | Unlimited |
| Classes per account | 500 (Paid) / 100 (Free) | 500 (Paid) / 100 (Free) |
| Storage per account | Unlimited (Paid) / 5 GB (Free) | 50 GB (raisable) |
| Storage per object | 10 GB | Unlimited |
| Key plus value | 2 MB combined | Key 2 KiB, value 128 KiB |
| WebSocket received message | 32 MiB | 32 MiB |
| CPU per request | 30 s default, up to 5 min | 30 s |
| Simultaneous outgoing connections per request | 6 | 6 |
| WebSockets per object (Hibernation API) | 32,768 | 32,768 |
| Throughput per object | Soft limit about 1,000 requests per second | same |

SQL limits: 100 columns per table, unlimited rows, 2 MB max string/BLOB/row, 100 KB max statement, 100 bound parameters, 32 arguments per SQL function, 50-byte `LIKE`/`GLOB` patterns.
When an object hits its storage cap, writes fail with `SQLITE_FULL` while reads and deletes keep working.
An overloaded object queues requests then returns an "overloaded" error.
The rules page gives throughput guidance of about 1,000 req/s for pass-through, 500 to 750 for moderate JSON work, 200 to 500 for storage-heavy work, and says to shard (for example 500 to 1,000 game-session objects for 500,000 req/s).

Sources: https://developers.cloudflare.com/durable-objects/platform/limits/, https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/, https://developers.cloudflare.com/durable-objects/best-practices/websockets/

### Pricing (as of 2026-10-05)

| Item | Free | Paid |
| --- | --- | --- |
| Requests (HTTP, RPC sessions, WebSocket messages, alarms) | 100,000 per day | 1 million per month, then $0.15 per million |
| Duration | 13,000 GB-s per day | 400,000 GB-s per month, then $12.50 per million GB-s |
| SQLite rows read | 5 million per day | 25 billion per month, then $0.001 per million |
| SQLite rows written | 100,000 per day | 50 million per month, then $1.00 per million |
| SQLite stored data | 5 GB total | 5 GB-month, then $0.20 per GB-month |
| KV backend reads (4 KB units) | n/a | 1 million, then $0.20 per million |
| KV backend writes (4 KB units) | n/a | 1 million, then $1.00 per million |
| KV backend deletes | n/a | 1 million, then $1.00 per million |
| KV backend storage | n/a | 1 GB, then $0.20 per GB-month |

- Duration is wall-clock time while the object is active or idle but not hibernateable, billed at 128 MB regardless of actual use; objects eligible for hibernation are not billed for duration even before they hibernate.
- Incoming WebSocket messages are billed at a 20:1 ratio (100 messages count as 5 requests); outgoing messages and protocol pings are free; `setWebSocketAutoResponse()` replies incur no duration.
- Calling `accept()` (non-hibernation API) bills duration for the whole time the socket is open; the docs recommend the Hibernation API.
- Each RPC method call on a stub is one billed request, but calls on an `RpcTarget` returned by that call are part of the same session.
- `setAlarm()` is billed as one row written; deletes count as rows written.
- Billable usage is rounded up to the next billing unit (for example 500,000 GB-s rounds to 1,000,000 GB-s).
- An open outbound TCP socket keeps an object billed for up to 15 minutes per connection.

Sources: https://developers.cloudflare.com/durable-objects/platform/pricing/, https://developers.cloudflare.com/workers/platform/pricing/, https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/

### Rules of Durable Objects (summary of the docs' guidance)

- Use Durable Objects for stateful coordination, not stateless request handling.
- Model objects around the "atom" of coordination (one per chat room, document, game session or user), use deterministic IDs, use parent-child relationships for related entities, and consider location hints for latency.
- Use SQLite-backed objects, run schema migrations in the constructor, index frequently queried columns, and know the difference between in-memory state and storage.
- Prefer RPC methods over `fetch()`, add an explicit `init()` method, and always `await` RPC calls.
- Use the Hibernation API and `serializeAttachment()` for WebSockets.
- Use alarms for per-entity schedules, make handlers idempotent, clean up with `deleteAll()`, and design for unexpected shutdowns.
- Do not use a single Durable Object as a global singleton.

Sources: https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/

### How it composes with other products

- Workers call objects through namespace bindings or `ctx.exports`.
- Containers are built on Durable Objects (each container instance is controlled by a Durable Object).
- The Agents SDK maps each agent to a unique Durable Object, which the docs say allows "tens of millions of Agents running concurrently" (see `build/02-ai.md`).
- D1 and Queues are themselves built on Durable Objects, per the storage chooser.
- Workers Cache never caches Durable Object invocations; put a caching Worker entrypoint in front.
- Pages Functions can bind to a Durable Object only by deploying it in a separate Worker.
- Each Preview gets its own Durable Object namespace.

Sources: https://developers.cloudflare.com/agents/platform/limits/, https://developers.cloudflare.com/workers/platform/storage-options/, https://developers.cloudflare.com/workers/cache/limitations/, https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/, https://developers.cloudflare.com/workers/previews/

### Code updates in practice (observed 2026-10-29)

- The lifecycle page says a deploy shuts down and restarts every Durable Object, eventually consistently, and the known-issues page puts the overlap with the previous version at "typically seconds to minutes".
- Observed in the Top-pad (Heat) project, issue #44: an indexer object kept alive by an outbound WebSocket (a `fetch()` upgrade to an RPC node) and a 15-second alarm went on running the previous version for over ten minutes and across a second deploy, while the Worker that called it ran the new one.
- `wrangler deploy` (and `wrangler versions deploy`) takes `--durable-objects-code-update-mode`, "immediate, or deferred followed by a maximum delay (for example, deferred 30s)"; deploying with `immediate` moved that object to the new version at once.
- A guard that does not depend on the deploy flag: bind `version_metadata` (`env.CF_VERSION_METADATA.id`), have the Worker pass its version on each call, and have the object call `this.ctx.abort()` when its own version differs, so the runtime restarts it on the current one.

Sources: https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/, https://developers.cloudflare.com/durable-objects/platform/known-issues/, https://developers.cloudflare.com/workers/wrangler/commands/workers/, https://developers.cloudflare.com/durable-objects/api/state/, https://github.com/imDev2023/top-pad/issues/44

### Most useful pages

- [Overview](https://developers.cloudflare.com/durable-objects/) - entry point
- [What are Durable Objects?](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/) - mental model
- [Lifecycle](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/) - hibernation and eviction timing
- [Rules of Durable Objects](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/) - design rules and throughput
- [Use WebSockets](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) - Hibernation API
- [SQLite storage API](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/) - SQL, KV, PITR, alarms
- [State](https://developers.cloudflare.com/durable-objects/api/state/) - `ctx` methods
- [Namespace](https://developers.cloudflare.com/durable-objects/api/namespace/) - IDs, getByName, jurisdiction
- [Alarms](https://developers.cloudflare.com/durable-objects/api/alarms/) - scheduling per object
- [Class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) - declarative lifecycle
- [Data location](https://developers.cloudflare.com/durable-objects/reference/data-location/) - hints and jurisdictions
- [Limits](https://developers.cloudflare.com/durable-objects/platform/limits/) - limits
- [Pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/) - billing rules
- [Known issues](https://developers.cloudflare.com/durable-objects/platform/known-issues/) - uniqueness and dev caveats
- [Error handling](https://developers.cloudflare.com/durable-objects/best-practices/error-handling/) - retry rules
- [Build a WebSocket server with Hibernation](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/) - example
- [Seat booking tutorial](https://developers.cloudflare.com/durable-objects/tutorials/build-a-seat-booking-app/) - SQLite example
- [Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/) - inspect stored data in the dashboard

## 5. Queues

### What it is

Queues is Cloudflare's message queue: Workers (or HTTP clients) send messages, and consumer Workers (or HTTP pull clients) receive them in batches, with guaranteed delivery and no egress charges.
It is used to offload work from a request, decouple services, buffer writes and absorb upstream rate limits.

Sources: https://developers.cloudflare.com/queues/, https://developers.cloudflare.com/queues/reference/how-queues-works/

### Status

- Generally available since 2024-09-26 ("Queues is GA, with higher throughput & consumer concurrency").
- Available on Free and Paid plans as of 2026-10-05 (Free retention fixed at 24 hours).
- Later additions: pull-based consumers (2024-03-25), message delays (2024-03-26), configurable retention (2025-02-14), pause and purge (2025-03-27), higher pull-consumer limits (2025-04-17).

Sources: https://developers.cloudflare.com/queues/platform/changelog/, https://developers.cloudflare.com/queues/platform/limits/

### Key concepts

- **Producer**: a Worker binding (or the REST endpoint) that writes messages.
- **Consumer**: either a push consumer (a Worker's `queue()` handler, auto-scaled) or a pull consumer (any HTTP client pulling with an API token).
- **Batching**: messages are delivered in batches, by size or timeout.
- **Delivery**: at least once by default; rare duplicates are possible, so the docs recommend an idempotency key per message.
- **Ordering**: not guaranteed ("best effort").
- **Retries and Dead Letter Queues**: failed messages are retried up to `max_retries` and then sent to a DLQ if configured, otherwise discarded.
- **Delays**: `delaySeconds` on send or retry, up to 24 hours; queue-level `--delivery-delay-secs`.
- **Event subscriptions**: Cloudflare products publish structured events into a queue; sources are Access, Artifacts, Browser Run, Email Sending, R2, Super Slurper, Vectorize, Workers AI, Workers Builds, Workers KV and Workflows.
- **Pause and purge**: stop delivery or drop all messages.

Sources: https://developers.cloudflare.com/queues/reference/delivery-guarantees/, https://developers.cloudflare.com/queues/configuration/javascript-apis/, https://developers.cloudflare.com/queues/event-subscriptions/, https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/, https://developers.cloudflare.com/queues/configuration/configure-queues/

### API and binding surface

```jsonc
{
  "queues": {
    "producers": [ { "binding": "MY_QUEUE", "queue": "my-queue" } ],
    "consumers": [ { "queue": "my-queue", "max_batch_size": 10, "max_batch_timeout": 5,
                     "max_retries": 3, "dead_letter_queue": "my-dlq", "max_concurrency": 10 } ]
  }
}
```

- Producer: `env.MY_QUEUE.send(body, { contentType, delaySeconds })`, `sendBatch(messages, { delaySeconds })`, `metrics()` returning `backlogCount`, `backlogBytes`, `oldestMessageTimestamp`.
- Content types: `json` is the default (changed from `v8` for compatibility with pull consumers, by compatibility date), plus `text`, `bytes`, `v8`.
- Consumer: `async queue(batch, env, ctx)`; `batch.queue`, `batch.messages`, `batch.ackAll()`, `batch.retryAll({ delaySeconds })`; per message `id`, `timestamp`, `body`, `attempts`, `ack()`, `retry({ delaySeconds })`.
- Consumer settings defaults: `max_batch_size` 10, `max_batch_timeout` 5 seconds, `max_retries` 3, `max_concurrency` unset (scale to the maximum); a named `dead_letter_queue` is created automatically if it does not exist.
- Queue settings: retention 60 seconds to 14 days (default 4 days on Paid), delivery delay 0 to 86,400 seconds.
- HTTP publish: `POST https://api.cloudflare.com/client/v4/accounts/<account>/queues/<queue_id>/messages` with a bearer token.
- HTTP pull: `POST .../queues/<queue_id>/messages/pull` with `{ "visibility_timeout_ms", "batch_size" }`, then acknowledge; tokens need Queues read and write permissions.
- Consumer concurrency autoscales on backlog size and growth and on the failure ratio; explicit `retry()` / `retryAll()` do not count as failures.

Sources: https://developers.cloudflare.com/queues/configuration/javascript-apis/, https://developers.cloudflare.com/queues/configuration/configure-queues/, https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/, https://developers.cloudflare.com/queues/configuration/pull-consumers/, https://developers.cloudflare.com/queues/configuration/consumer-concurrency/

### Limits (as of 2026-10-05, Free and Paid unless noted)

| Limit | Value |
| --- | --- |
| Queues per account | 10,000 |
| Message size | 128 KB (1 KB = 1,000 bytes, about 100 bytes metadata included) |
| Retries per message | 100 |
| Consumer batch size | 100 messages max |
| `sendBatch` | 100 messages or 256 KB total |
| Batch wait time | 60 seconds max |
| Throughput per queue | 5,000 messages per second (above that `send()` throws Too Many Requests) |
| Retention | Free: 24 hours fixed; Paid: 4 days default, up to 14 days |
| Backlog per queue | 25 GB (then `Storage Limit Exceeded`) |
| Concurrent consumer invocations | 250 (push consumers) |
| Consumer wall time | 15 minutes |
| Consumer CPU time | 30 seconds default, configurable to 5 minutes |
| `visibilityTimeout` (pull) | 12 hours |
| `delaySeconds` | 24 hours |

Sources: https://developers.cloudflare.com/queues/platform/limits/

### Pricing (as of 2026-10-05)

| Item | Workers Free | Workers Paid |
| --- | --- | --- |
| Standard operations | 10,000 per day | 1,000,000 per month included, then $0.40 per million |
| Retention | 24 hours | 4 days default, up to 14 days |

- One operation per 64 KB written, read or deleted; billing is per message, not per batch.
- A normal delivery costs 3 operations (write, read, delete); estimate as `((messages * 3) - 1,000,000) / 1,000,000 * $0.40`.
- Each retry adds a read; a DLQ write adds a write; expired messages incur a write and a delete.
- No egress or bandwidth charges.

Sources: https://developers.cloudflare.com/queues/platform/pricing/, https://developers.cloudflare.com/workers/platform/pricing/

### How it composes with other products

- Producers: Workers, Durable Objects, Pages Functions (producer only), HTTP clients, and event subscriptions from other products (including R2 and Workflows).
- Consumers: Workers (push), anything off-Cloudflare (pull); Pages cannot host consumers; Previews cannot be queue consumers.
- `ctx.waitUntil()` docs recommend Queues for work that cannot finish within 30 seconds after the response.
- Tutorials pair Queues with Browser Run (web crawler) and with external API rate limits.

Sources: https://developers.cloudflare.com/queues/llms.txt, https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/, https://developers.cloudflare.com/workers/previews/, https://developers.cloudflare.com/workers/runtime-apis/context/

### Most useful pages

- [Queues overview](https://developers.cloudflare.com/queues/) - entry point
- [How Queues works](https://developers.cloudflare.com/queues/reference/how-queues-works/) - producers, consumers, ordering
- [JavaScript APIs](https://developers.cloudflare.com/queues/configuration/javascript-apis/) - send, batch, ack, retry
- [Configure Queues](https://developers.cloudflare.com/queues/configuration/configure-queues/) - consumer settings
- [Batching, retries and delays](https://developers.cloudflare.com/queues/configuration/batching-retries/) - retry semantics
- [Dead Letter Queues](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/) - failure routing
- [Consumer concurrency](https://developers.cloudflare.com/queues/configuration/consumer-concurrency/) - autoscaling
- [Pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) - consume outside Workers
- [Delivery guarantees](https://developers.cloudflare.com/queues/reference/delivery-guarantees/) - at least once
- [Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) - platform events
- [Handle rate limits of external APIs](https://developers.cloudflare.com/queues/tutorials/handle-rate-limits/) - upstream throttling
- [Limits](https://developers.cloudflare.com/queues/platform/limits/) and [Pricing](https://developers.cloudflare.com/queues/platform/pricing/)

## 6. Workflows

### What it is

Workflows is a durable execution engine on Workers: a Workflow is a class whose `run()` method is split into named steps that persist their results, retry automatically, sleep for up to a year and wait for external events, resuming where they left off even if the isolate is recycled.
It suits multi-step jobs such as onboarding, payments and invoicing, data pipelines, human-in-the-loop approval and durable AI agents.

Sources: https://developers.cloudflare.com/workflows/, https://developers.cloudflare.com/workflows/reference/limits/

### Status

- Generally available since 2025-04-07.
- Python Workflows open beta since 2025-08-22.
- Available on Free and Paid plans; step and storage billing began on August 10, 2026 (as of 2026-10-05).
- Workflows cannot be deployed to Workers for Platforms namespaces.

Sources: https://developers.cloudflare.com/workflows/reference/changelog/, https://developers.cloudflare.com/workflows/reference/pricing/, https://developers.cloudflare.com/workflows/reference/limits/

### Key concepts

- **Workflow** (definition, the class) vs **instance** (one execution with its own ID and params).
- **Steps**: `step.do()` units whose return values are persisted (non-stream results up to 1 MiB; JavaScript steps can return a `ReadableStream<Uint8Array>` for larger binary output).
- **States** (`InstanceStatus`): `queued`, `running`, `paused`, `waitingForPause`, `waiting` (sleeping, waiting for a retry or an event), `complete`, `errored`, `terminated`, `unknown`; waiting instances do not count toward concurrency.
- **Retries**: default `{ retries: { limit: 5, delay: 10000, backoff: "exponential" }, timeout: "10 minutes" }`; `delay` may be a function of the error; throw `NonRetryableError` to fail immediately.
- **Rollback handlers**: optional per-step compensation (`rollback`, `rollbackConfig`).
- **Events**: `step.waitForEvent(name, { type, timeout })` (default timeout 24 hours) paired with `instance.sendEvent({ type, payload })`.
- **Schedules**: cron expressions on the Workflow binding start instances directly.

Sources: https://developers.cloudflare.com/workflows/build/workers-api/, https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/, https://developers.cloudflare.com/workflows/build/trigger-workflows/, https://developers.cloudflare.com/workflows/reference/limits/

### API and binding surface

```jsonc
{ "workflows": [ { "name": "workflows-tutorial", "binding": "MY_WORKFLOW", "class_name": "MyWorkflow", "schedules": ["0 * * * *"] } ] }
```

```ts
import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from "cloudflare:workers";
export class MyWorkflow extends WorkflowEntrypoint<Env> {
  async run(event: WorkflowEvent<unknown>, step: WorkflowStep) {
    await step.do("initial work", async () => (await fetch("https://api.cloudflare.com/client/v4/ips")).json());
    await step.sleep("wait 30 days", "30 days");
    await step.do("write", { retries: { limit: 5, delay: "5 seconds", backoff: "exponential" }, timeout: "15 minutes" }, async () => { /* ... */ });
  }
}
```

- Step API: `step.do(name, [config], callback, [rollbackOptions])`, `step.sleep(name, duration)`, `step.sleepUntil(name, timestamp)`, `step.waitForEvent(name, { type, timeout })`; `WorkflowStepContext` exposes step metadata such as `count`.
- Binding API: `create({ id?, params?, retention? })`, `createBatch([...])`, `get(id)`, `deleteBatch`.
- Instance API: `id`, `status()`, `pause()`, `resume()`, `restart({ from: { name, count, type } })`, `terminate()`, `delete`, `sendEvent({ type, payload })`, `subscribe()`.
- Retention: `default_retention` on the binding (`success_retention`, `error_retention`) or `retention` per instance.
- Workflows can be declared in `exports` and called through `ctx.exports` (needs `@cloudflare/vite-plugin` 1.61.0+ / `@cloudflare/vitest-plugin` 1.3.0+ for local tooling); cross-script calls and binding from Pages are documented.
- Python Workflows use `from workers import WorkflowEntrypoint`, including DAG-style workflows.
- Instance lifecycle events can be published to Queues via event subscriptions.

Sources: https://developers.cloudflare.com/workflows/build/workers-api/, https://developers.cloudflare.com/workflows/build/trigger-workflows/, https://developers.cloudflare.com/workflows/python/, https://developers.cloudflare.com/workflows/reference/event-subscriptions/

### Rules of Workflows (the docs' list)

Make API and binding calls idempotent; make steps granular; do not rely on state outside a step; avoid side effects outside `step.do`; do not mutate incoming events; name steps deterministically; take care with `Promise.race()` and `Promise.any()`; instance IDs are unique; always `await` steps; use conditional logic carefully; batch multiple invocations; keep step timeouts at 30 minutes or less (use `waitForEvent` beyond that); keep non-stream step return values under 1 MiB.

Sources: https://developers.cloudflare.com/workflows/build/rules-of-workflows/

Observed in practice (2026-10-29, Top-pad #44, wrangler 4.154): `step.sleepUntil()` with a time already past throws ("You can't sleep until a time in the past"), so a Workflow started late must skip the sleep; `wrangler dev` runs Workflows locally and lists their instances at `/cdn-cgi/local/explorer/api/workflows/<name>/instances`; deployed instances list with `wrangler workflows instances list <name>`.

### Limits (as of 2026-10-05)

| Limit | Workers Free | Workers Paid |
| --- | --- | --- |
| CPU per step | 10 ms | 30 s default, up to 5 min |
| Wall time per step | Unlimited | Unlimited |
| Step result (non-stream) | 1 MiB | 1 MiB |
| Event payload | 1 MiB | 1 MiB |
| State per instance | 100 MB | 1 GB |
| `step.sleep` max | 365 days | 365 days |
| Steps per Workflow (sleep excluded) | 1,024 | 10,000 default, up to 25,000 |
| Executions | 100,000 per day (shared with Workers) | Unlimited |
| Concurrent running instances per account | 100 | 50,000 |
| Instance creation rate | 100 per second | 300 per second per account, 100 per second per workflow (HTTP 429 above) |
| Queued instances | 100,000 | 2,000,000 |
| Completed state retention | 3 days | 30 days |
| Workflow name / instance ID length | 64 / 100 characters | 64 / 100 characters |
| Subrequests per instance | 50 | 10,000 default, up to 10 million |
| Retries per step | 10,000 | 10,000 |
| `schedules` per account | 100 cron expressions (256 characters each) | same |

On Workers Paid, schedule-created instances get up to one hour per cron firing without using a concurrency slot.

Sources: https://developers.cloudflare.com/workflows/reference/limits/

### Pricing (as of 2026-10-05)

| Unit | Workers Free | Workers Paid |
| --- | --- | --- |
| Requests (instance creations) | 100,000 per day (shared with Workers) | 10 million per month, then $0.30 per million |
| CPU time | 10 ms per invocation | 30 million CPU-ms per month, then $0.02 per million |
| Storage | 1 GB-month | 1 GB-month, then $0.20 per GB-month |
| Steps | 3,000 per day | 500,000 per month, then $0.80 per additional 100,000 |

- Steps exclude retries and rollback handlers; subrequests are not billed; sleeping or waiting incurs no CPU.
- Storage is averaged peak-per-day over 30 days across all instances, including completed ones until retention expires.

Sources: https://developers.cloudflare.com/workflows/reference/pricing/

### How it composes with other products

- Triggered from Workers, Pages Functions, `ctx.exports`, cron `schedules`, the REST API and Wrangler.
- Steps call any binding (D1, R2, KV, Workers AI, Browser Run, Queues, service bindings).
- Dynamic Workers can run Workflows defined at runtime ("Dynamic Workflows").
- Workflow bindings in Previews use the existing Workflows, not Preview-specific ones.

Sources: https://developers.cloudflare.com/workflows/build/trigger-workflows/, https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/, https://developers.cloudflare.com/workers/previews/

### Most useful pages

- [Workflows overview](https://developers.cloudflare.com/workflows/) - entry point
- [Build your first Workflow](https://developers.cloudflare.com/workflows/get-started/guide/) - tutorial
- [Workers API](https://developers.cloudflare.com/workflows/build/workers-api/) - full API
- [Sleeping and retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/) - retry defaults
- [Events and parameters](https://developers.cloudflare.com/workflows/build/events-and-parameters/) - waitForEvent and sendEvent
- [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/) - bindings, schedules, REST
- [Rules of Workflows](https://developers.cloudflare.com/workflows/build/rules-of-workflows/) - determinism rules
- [Build a Durable AI Agent](https://developers.cloudflare.com/workflows/get-started/durable-agents/) - agent pattern
- [Python Workflows](https://developers.cloudflare.com/workflows/python/) - open beta
- [Limits](https://developers.cloudflare.com/workflows/reference/limits/) and [Pricing](https://developers.cloudflare.com/workflows/reference/pricing/)

## 7. Flagship

### What it is

Flagship is Cloudflare's feature flag service: define flags with variants, targeting rules and percentage rollouts, then evaluate them inside Workers through a native binding, or from servers and browsers through OpenFeature SDKs, without redeploying code.
Flag configuration propagates across Cloudflare's network "within seconds", evaluation happens locally with no round trip to a central server, and it keeps working on the last propagated configuration if the dashboard is unavailable.
The launch note says configuration is "backed by Workers KV and Durable Objects"; the overview says Flagship uses KV infrastructure to deliver flag configurations.

Sources: https://developers.cloudflare.com/flagship/, https://developers.cloudflare.com/flagship/concepts/, https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/

### Status

- Public beta since 2026-05-26 (as of 2026-10-05); later changelog entries add an API reference (2026-06-10), Wrangler commands (2026-07-16) and app-scoped API tokens (2026-08-26).
- No pricing page and no plan availability statement exist in the mirrored Flagship docs.

Sources: https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/, https://developers.cloudflare.com/changelog/product/flagship/

### Key concepts

- **App**: top-level group of flags, usually one per project or service.
- **Flag**: key, variants, targeting rules, enabled/disabled state; a disabled flag always returns its default variant.
- **Variants**: boolean, string, number or JSON; all variants on a flag share one type; one is the default.
- **Targeting rules**: evaluated in order, with 11 operators (`equals`, `not_equals`, `greater_than`, `less_than`, `greater_than_or_equals`, `less_than_or_equals`, `contains`, `starts_with`, `ends_with`, `in`, `not_in`) and AND/OR groups nested up to 5 levels.
- **Percentage rollouts**: consistent hashing on a bucketing attribute (default `targetingKey`) so a user always gets the same value.
- **Evaluation reasons and error codes** are documented for debugging.

Sources: https://developers.cloudflare.com/flagship/concepts/, https://developers.cloudflare.com/flagship/targeting/operators/, https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/, https://developers.cloudflare.com/flagship/reference/limits/

### API and binding surface

```jsonc
{ "flagship": [ { "binding": "FLAGS", "app_id": "<APP_ID>" } ] }
```

```js
const enabled = await env.FLAGS.getBooleanValue("dark-mode", false, { userId: "user-42" });
```

- Binding methods: `get()`, `getBooleanValue()`, `getStringValue()`, `getNumberValue()`, `getObjectValue()`, and `get*Details()` variants returning value plus reason; every method takes `(flagKey, defaultValue, context?)` and falls back to the default on failure or type mismatch.
- OpenFeature SDKs: TypeScript server and client providers (`@cloudflare/flagship`), Python (`pip install cloudflare-flagship`), Go (`go get github.com/cloudflare/flagship/sdks/go`).
- Management: dashboard, REST API, `wrangler flagship` commands; Flagship bindings can be auto-provisioned by Wrangler.
- Best practices: choose the right evaluation path, evaluate once per request, pass context consistently, choose safe defaults, use details for observability, roll out progressively, clean up stale flags.

Sources: https://developers.cloudflare.com/flagship/binding/methods/, https://developers.cloudflare.com/flagship/configuration/, https://developers.cloudflare.com/flagship/sdk/, https://developers.cloudflare.com/flagship/best-practices/, https://developers.cloudflare.com/workers/wrangler/configuration/

### Limits (as of 2026-10-05)

| Limit | Value |
| --- | --- |
| Apps per account | 10,000 (soft) |
| Flags per app | 5,000 (soft) |
| Flag, app and variant keys | 64 characters |
| Condition attribute names | 64 characters |
| Condition string values | 256 characters |
| Variant value size | 10 KB |
| Condition nesting depth | 5 levels |
| Flag description | 512 characters |
| Flag configuration per app | 25 MB |

Sources: https://developers.cloudflare.com/flagship/reference/limits/

### Pricing

Not documented in the mirrored Flagship pages as of 2026-10-05.

### How it composes with other products

Flagship is a Workers binding built on KV (and, per the launch note, Durable Objects); it complements Workers gradual deployments (code-level traffic splits) with runtime feature toggles.

Sources: https://developers.cloudflare.com/flagship/, https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/

### Most useful pages

- [Flagship overview](https://developers.cloudflare.com/flagship/) - entry point
- [Get started](https://developers.cloudflare.com/flagship/get-started/) - first flag
- [Concepts](https://developers.cloudflare.com/flagship/concepts/) - apps, flags, variants
- [Binding methods](https://developers.cloudflare.com/flagship/binding/methods/) - evaluation API
- [OpenFeature SDK](https://developers.cloudflare.com/flagship/sdk/) - non-Worker clients
- [Targeting rules](https://developers.cloudflare.com/flagship/targeting/) and [Percentage rollouts](https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/)
- [Limits](https://developers.cloudflare.com/flagship/reference/limits/)

## 8. Browser Run (formerly Browser Rendering)

### What it is

Browser Run runs headless Chrome on Cloudflare's network for browser automation, scraping, testing and content generation.
It was renamed from Browser Rendering on 2026-04-15: "We are renaming Browser Rendering to Browser Run. The name Browser Rendering never fully captured what the product does."
Two integration styles exist: Quick Actions (stateless one-request REST tasks, no deployment) and Browser Sessions (direct control with Puppeteer, Playwright, CDP or Stagehand, from a Worker or from anywhere over CDP).
A second engine, Kitesurf, is a stateless browser built on Workers for AI agents, lighter than Chromium.

Sources: https://developers.cloudflare.com/browser-run/, https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/, https://developers.cloudflare.com/browser-run/kitesurf/

### Status

- Available on Free and Paid plans, as of 2026-10-05.
- The `/crawl` endpoint is marked beta; Kitesurf is in beta and free behind per-account limits.
- Recent additions: CDP and MCP client support (2026-04-10), Live View, Human in the Loop, Session Recordings and WebMCP (2026-04-15), Quick Actions from Workers via `quickAction()` (2026-05-28), `/accessibilityTree` (2026-07-07), typed binding session and DevTools methods (2026-09-21).
- Paid concurrency rose from 30 to 120 at the rename and from 120 to 200 on 2026-08-20.

Sources: https://developers.cloudflare.com/browser-run/, https://developers.cloudflare.com/browser-run/changelog/, https://developers.cloudflare.com/browser-run/kitesurf/, https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/

### Key concepts

- **Browser hours**: billed browser time, shared by all methods; sessions close after 60 seconds of inactivity by default, extendable to 10 minutes with `keep_alive`; there is no fixed maximum session lifetime while active, but sessions close on Browser Run releases.
- **Concurrent browsers**: Browser Sessions only, averaged monthly for billing.
- **Session reuse**: keep a browser open and reconnect from later requests, or hold it in a Durable Object.
- **Close reasons** such as `BrowserIdle` vs `NormalClosure` explain unexpected usage; always `browser.close()` in `try/finally`.
- **Features**: custom fonts, guardrails, Human in the Loop, Live View, outbound Workers (route browser traffic through a Worker), reuse sessions, session recording, WebMCP, automatic request headers, robots.txt handling.

Sources: https://developers.cloudflare.com/browser-run/limits/, https://developers.cloudflare.com/browser-run/pricing/, https://developers.cloudflare.com/browser-run/llms.txt

### API and binding surface

Quick Actions (REST, `POST https://api.cloudflare.com/client/v4/accounts/<id>/browser-run/<action>`; each response carries `X-Browser-Ms-Used`):

| Endpoint | Purpose |
| --- | --- |
| `/content` | Fetch fully rendered HTML |
| `/screenshot` | Capture a screenshot |
| `/pdf` | Render a PDF |
| `/markdown` | Extract Markdown |
| `/snapshot` | Capture multiple formats at once |
| `/scrape` | Scrape elements by CSS selector |
| `/json` | Structured data via AI prompt |
| `/links` | Retrieve links |
| `/crawl` | Async multi-page crawl to HTML, Markdown or JSON (beta; jobs time out after 7 days; `render: false` runs on Workers) |
| `/accessibilityTree` | Capture the accessibility tree |

Sessions also use `/devtools` (CDP over WebSocket) and `/recording` endpoints.

Sources: https://developers.cloudflare.com/browser-run/quick-actions/, https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/, https://developers.cloudflare.com/browser-run/pricing/, https://developers.cloudflare.com/browser-run/cdp/

Workers binding:

```jsonc
{ "browser": { "binding": "MYBROWSER" } }
```

```js
import puppeteer from "@cloudflare/puppeteer";
const browser = await puppeteer.launch(env.MYBROWSER, { keep_alive: 600000 });
```

- Libraries: `@cloudflare/puppeteer`, `@cloudflare/playwright` (v1.3.0 switched to standard CDP internally), Stagehand, Playwright MCP.
- Binding session methods: `acquire()`, `connectSession()`, `launch()`, `getLiveView()`, `listSessions()`, `history()`, `limits()`, `getSession()`, `closeSession()`, plus a nested `devtools` binding and `quickAction()`.
- CDP endpoints let MCP clients, local Playwright/Puppeteer, CI or external servers drive Browser Run over WebSocket.

Sources: https://developers.cloudflare.com/browser-run/puppeteer/, https://developers.cloudflare.com/browser-run/reference/browser-binding-api/, https://developers.cloudflare.com/browser-run/changelog/, https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/

### Limits (as of 2026-10-05)

| Limit | Workers Free | Workers Paid (defaults, raisable) |
| --- | --- | --- |
| Browser hours | 10 minutes per day | No limit (billed) |
| Concurrent browsers (sessions) | 3 per account | 200 per account |
| New browser instances | 1 every 20 seconds | 3 per second |
| Browser inactivity timeout | 60 s (up to 10 min with `keep_alive`) | same |
| Quick Actions requests | 1 every 10 seconds | 30 per second |
| `/crawl` jobs | 5 per day, 100 pages per crawl | not listed |

Excess requests get HTTP 429 with `Retry-After`.

Sources: https://developers.cloudflare.com/browser-run/limits/

### Pricing (as of 2026-10-05)

| Item | Workers Free | Workers Paid |
| --- | --- | --- |
| Browser hours | 10 minutes per day | 10 hours per month, then $0.09 per hour |
| Concurrent browsers (sessions only) | 3 | 10 (monthly average), then $2.00 per additional browser |

- Quick Actions are charged for browser hours only; sessions for hours plus concurrency.
- Docs example: 50 hours of sessions with 10 then 20 browsers over a month costs $3.60 (hours) + $10.00 (concurrency) = $13.60.
- `/crawl` with `render: false` runs on Workers instead of a browser.

Sources: https://developers.cloudflare.com/browser-run/pricing/, https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/

### How it composes with other products

- Workers (binding), Durable Objects (persist sessions), Queues (web crawler tutorial), Workflows, the Agents SDK (Playwright MCP, Stagehand), Workers AI (`/json`), and Queues event subscriptions (crawl events since 2026-09-25).

Sources: https://developers.cloudflare.com/browser-run/, https://developers.cloudflare.com/queues/tutorials/web-crawler-with-browser-run/, https://developers.cloudflare.com/changelog/product/browser-run/

### Most useful pages

- [Browser Run overview](https://developers.cloudflare.com/browser-run/) - entry point and method chooser
- [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) - REST endpoints
- [/crawl](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) - site crawling
- [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/) and [Playwright](https://developers.cloudflare.com/browser-run/playwright/) - session libraries
- [CDP](https://developers.cloudflare.com/browser-run/cdp/) - drive from anywhere
- [Browser binding API](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) - session methods
- [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/) - cut cold starts
- [Deploy with Durable Objects](https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/) - persistent browsers
- [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) - lightweight agent browser
- [Limits](https://developers.cloudflare.com/browser-run/limits/) and [Pricing](https://developers.cloudflare.com/browser-run/pricing/)
- [FAQ](https://developers.cloudflare.com/browser-run/faq/) - session lifetime and usage questions

## 9. Workers VPC

### What it is

Workers VPC connects Workers to private APIs, services and databases in external clouds (AWS, Azure, GCP, on-premise) that are not reachable from the public Internet.
Two binding types exist: VPC Services bind to one registered host and port reached through a Cloudflare Tunnel; VPC Networks bind to a whole Cloudflare Tunnel, Cloudflare Mesh network or Cloudflare WAN on-ramp (GRE, IPsec, CNI), with Mesh and WAN traffic passing through Cloudflare Gateway policies and logs.

Sources: https://developers.cloudflare.com/workers-vpc/

### Status

- Beta as of 2026-10-05 ("Features and APIs may change before general availability").
- Free to all Workers plans during the beta; standard Workers request and CPU pricing applies.

Sources: https://developers.cloudflare.com/workers-vpc/, https://developers.cloudflare.com/workers-vpc/platform/pricing/

### API and binding surface

```jsonc
{ "vpc_services": [ { "binding": "PRIVATE_API", "service_id": "ENTER_SERVICE_ID", "remote": true } ],
  "vpc_networks": [ { "binding": "MY_VPC", "tunnel_id": "550e8400-e29b-41d4-a716-446655440000", "remote": true } ] }
```

- `env.BINDING.fetch(absoluteUrl, init)` on both types; URLs must be absolute (protocol, host, path).
- For a VPC Service the registered target always wins: the URL host only sets the `Host` header and TLS SNI, and the URL port is ignored.
- For a VPC Network the URL or address decides the destination among routes announced through the tunnel, Mesh or WAN.
- `connect()` opens a raw TCP connection to a private destination, on VPC Network bindings only.
- VPC Services can also be managed with Terraform and Wrangler commands (`wrangler vpc`).

Sources: https://developers.cloudflare.com/workers-vpc/api/, https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/, https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/, https://developers.cloudflare.com/workers/wrangler/commands/vpc/

### Limits and pricing (as of 2026-10-05)

- 1,000 VPC Services per account.
- Standard Workers limits apply for request size, timeout and subrequests.
- Free during the beta beyond normal Workers usage.

Sources: https://developers.cloudflare.com/workers-vpc/platform/limits/, https://developers.cloudflare.com/workers-vpc/platform/pricing/

### How it composes with other products

Workers VPC sits on Cloudflare Tunnel (`cloudflared`), Cloudflare Mesh, Cloudflare WAN and Gateway; examples cover private APIs, private databases, private S3 buckets and routing across private services.
This makes it the fit for a Worker that must reach a self-hosted node or database with no public endpoint (inference).

Sources: https://developers.cloudflare.com/workers-vpc/, https://developers.cloudflare.com/workers-vpc/examples/private-database/

### Most useful pages

- [Workers VPC overview](https://developers.cloudflare.com/workers-vpc/) - entry point
- [Get started](https://developers.cloudflare.com/workers-vpc/get-started/) - first binding
- [Workers Binding API](https://developers.cloudflare.com/workers-vpc/api/) - fetch and connect
- [VPC Services](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/) - single-target bindings
- [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) - network-wide bindings
- [Cloudflare Tunnel](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/) - on-ramp setup and hardware requirements
- [Connect to a private database](https://developers.cloudflare.com/workers-vpc/examples/private-database/) - example
- [Limits](https://developers.cloudflare.com/workers-vpc/platform/limits/) and [Pricing](https://developers.cloudflare.com/workers-vpc/platform/pricing/)

## 10. Cloudflare for Platforms

### What it is

Cloudflare for Platforms is for building a platform where your customers deploy code, each with their own subdomain or custom domain: app builders, AI "vibe coding" platforms, user-scriptable products, per-customer databases and per-customer subdomains.
It has two parts: Workers for Platforms (run untrusted customer code as isolated user Workers behind your dispatch Worker) and Cloudflare for SaaS (custom hostnames and certificates for customers' vanity domains).
Starter templates are the Platform Starter Kit (each snippet becomes a Worker at `example.com/{app-name}`) and VibeSDK (AI code generation, sandboxed execution, previews and deployment).

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/, https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/

### Status

- Both parts are generally available (no beta label) as of 2026-10-05.
- Workers for Platforms is a separate paid plan ($25 per month) purchased in the dashboard.
- Cloudflare for SaaS is available on Free, Pro and Business zone plans with 100 hostnames included; Enterprise is by contract, and eligible Enterprise customers can preview it as a non-contract service.

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/, https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/

### Workers for Platforms

#### Key concepts

- **Dispatch namespace**: holds all customer Workers (use one namespace such as `production`, plus `staging`; not one per customer); no per-account script limit applies inside it.
- **Dynamic dispatch Worker**: your entry Worker that routes each request (by hostname, path, header), runs auth and rate limiting, sets per-customer limits and sanitizes responses.
- **User Workers**: customer code uploaded through the API into a namespace; run in untrusted mode by default (no shared cache, no `request.cf`, `caches.default` disabled); trusted mode can be enabled for a namespace you fully control.
- **Outbound Workers** (optional): intercept every `fetch()` a user Worker makes, to allow, deny, log or rewrite egress.
- **Tags**: up to eight per script, for bulk operations.
- **Static assets** for user Workers are uploaded through a manifest of file hashes then the files.
- Hostname routing: the recommended setup is a wildcard route `*/*` on the SaaS zone pointing at the dispatch Worker, which avoids per-route limits and handles both subdomains and custom hostnames.

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/limits/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/

#### API and binding surface

```jsonc
{ "dispatch_namespaces": [ { "binding": "DISPATCHER", "namespace": "my-dispatch-namespace",
    "outbound": { "service": "<SERVICE_NAME>", "parameters": ["params_object"] } } ] }
```

```js
export default {
  async fetch(request, env) {
    const customerName = new URL(request.url).hostname.split(".")[0];
    return env.DISPATCHER.get(customerName).fetch(request);
  },
};
```

- Custom limits per call: `env.DISPATCHER.get(name, {}, { limits: { cpuMs: 10, subRequests: 5 } })`.
- User Workers can be given bindings (KV, D1, R2, Durable Objects and others) so customers get storage "without API tokens, keys, or external dependencies".
- Management through the REST API and Wrangler (`wrangler dispatch-namespace create|delete|get|list|rename`); observability through Workers Logs, Workers Trace Events Logpush, Tail Workers, Workers Analytics Engine and the GraphQL Analytics API.

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/, https://developers.cloudflare.com/cloudflare-for-platforms/, https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/observability/

#### Limits (as of 2026-10-05)

- Scripts: unlimited (billed beyond 1,000).
- Durable Object namespaces: no limit.
- Tags: 8 per script.
- Gradual deployments are not supported for user Workers (every change deploys to 100%).
- Workflows cannot be deployed to Workers for Platforms namespaces.
- Cloudflare API rate limits: 1,200 requests per 5 minutes per user/token, 200 per second per IP, GraphQL up to 320 per 5 minutes; 50 user tokens per user and 500 account tokens per account.

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/limits/, https://developers.cloudflare.com/workflows/reference/limits/

#### Pricing (as of 2026-10-05)

| Item | Included in $25 per month | Overage |
| --- | --- | --- |
| Requests | 20 million per month | $0.30 per million |
| CPU time | 60 million CPU-ms per month | $0.02 per million CPU-ms |
| Scripts | 1,000 | $0.02 per additional script |
| Duration | No charge | No charge |

- Only one request is billed across the dispatch Worker to user Worker (to outbound Worker) chain; subrequests are not billed.
- Docs example: 100 million requests, 10 ms CPU, 1,200 scripts costs $71.80 per month.

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/

### Cloudflare for SaaS

- Lets customers point vanity domains (for example `app.customer.com`) at your SaaS zone via CNAME; Cloudflare issues and renews certificates per custom hostname (HTTP, TXT or delegated DCV) and routes traffic to a fallback origin, which can be a Worker.
- Setup: create a fallback origin (proxied), optionally a CNAME target, then create a custom hostname per customer, validate, and have the customer add the CNAME.
- Features: custom metadata per hostname, WAF for SaaS, Cache, Argo and Early Hints for SaaS, apex proxying, Access protection, mTLS (Enterprise), custom certificates (Enterprise).
- Quotas are soft (create calls return a billing warning), but non-Enterprise plans hit an API enforcement threshold (`hard_cap` in the quota API).

| Cloudflare for SaaS (as of 2026-10-05) | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Hostnames included | 100 | 100 | 100 | Custom |
| Max hostnames | 50,000 | 50,000 | 50,000 | Unlimited (contact sales above 50,000) |
| Price per additional hostname | $0.10 | $0.10 | $0.10 | Custom |
| Wildcard custom hostnames, custom certificates, mTLS, selectable CA | No | No | No | Yes |

Sources: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/, https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/, https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/, https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/

### How it composes with other products

- Workers for Platforms is Workers plus dispatch namespaces; Cloudflare for SaaS supplies the custom domains in front of it.
- Workers docs point to Workers for Platforms when an account needs more than 500 Workers, more than 1,000 routes or more than 1,000 routed zones; Pages docs point to it beyond 100 projects.
- Dynamic Workers are the lighter, code-at-runtime alternative for running untrusted code.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/pages/platform/limits/, https://developers.cloudflare.com/dynamic-workers/

### Most useful pages

- [Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/) - overview and templates
- [How Workers for Platforms works](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/) - architecture
- [Get started](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/) - first namespace
- [Dynamic dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/) - routing code
- [Custom limits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/) - per-tenant CPU caps
- [Outbound Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/) - egress control
- [Hostname routing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/) - wildcard routing
- [Worker isolation](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/) - trusted vs untrusted
- [Workers for Platforms pricing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/) and [limits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/limits/)
- [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) - custom hostnames
- [SaaS plans](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/) - hostname pricing
- [Workers as your fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/)

## 11. Email Service

### What it is

Email Service combines Email Sending (outbound transactional email from Workers, a REST API or SMTP) and Email Routing (inbound mail routed to addresses or to a Worker's `email()` handler).
Use cases listed: transactional mail, magic links and verification, notifications, custom addresses (support@, orders@), and email as an interface for agents.

Sources: https://developers.cloudflare.com/email-service/

### Status

- Email Sending: beta (public beta since 2026-04-16), Workers Paid plan only, as of 2026-10-05.
- Email Routing: available on Free and Paid plans; the Workers Betas page still lists "Email Workers" (the `email()` handler) as a public beta.
- Sending to verified destination addresses in your own account is free on all plans, even with only Email Routing configured.
- Recent changelog items: SMTP submission (2026-06-08), event subscriptions (2026-07-15), routing rules in Wrangler (2026-09-04), sending-domain suppressions (2026-09-25).

Sources: https://developers.cloudflare.com/email-service/, https://developers.cloudflare.com/workers/platform/betas/, https://developers.cloudflare.com/changelog/product/email-service/

### API and binding surface

```jsonc
{ "send_email": [ { "name": "EMAIL" },
                  { "name": "NOTIFY_OPS", "destination_address": "ops@yourdomain.com" } ] }
```

```ts
await env.EMAIL.send({ to: "user@example.com", from: "welcome@yourdomain.com",
  subject: "Welcome!", html: "<h1>Welcome!</h1>", text: "Welcome!" });
```

- Send bindings can be unrestricted, fixed to one `destination_address`, or limited to an allowlist.
- REST: `POST https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send`.
- SMTP: `smtp.mx.cloudflare.net:465` with implicit TLS only (no STARTTLS on 587, no relay on 25).
- Inbound handler: `async email(message, env, ctx)` with `ForwardableEmailMessage`: `from`, `to`, `headers`, `raw` (ReadableStream of MIME), `rawSize`, `canBeForwarded`, `setReject(reason)`, `forward(rcptTo, headers?)`, `reply(message)`.
- Inbound addresses can be declared in Wrangler with the top-level `addresses` key (literal or `*@domain`).
- Supporting concepts: deliverability, SPF/DKIM/DMARC authentication, suppression lists, MTA-STS, subdomains, email logs, metrics, event subscriptions to Queues.

Sources: https://developers.cloudflare.com/email-service/configuration/send-bindings/, https://developers.cloudflare.com/email-service/api/send-emails/rest-api/, https://developers.cloudflare.com/email-service/api/send-emails/smtp/, https://developers.cloudflare.com/email-service/api/route-emails/email-handler/, https://developers.cloudflare.com/workers/wrangler/configuration/

### Limits (as of 2026-10-05)

| Limit | Value |
| --- | --- |
| Daily sending quota | Starts conservative per account, grows with reputation |
| Recipients per email (to, cc, bcc) | 50 |
| Subject | 998 characters |
| Message size (sending) | 5 MiB including attachments (25 MiB to verified destination addresses) |
| Custom headers | 16 KB total |
| Domains per zone (routing plus sending) | 30 |
| Routing rules per domain | 200 |
| Destination addresses per account | 200 |
| Inbound message size | 25 MiB |
| Reply `References` entries | 100 (`reply()` throws above) |
| Suppression bulk import | 1,000 items per request, 10 requests per minute |

- Before onboarding a sending domain you can only send to verified destination addresses.
- Email Workers count against normal Workers CPU and memory limits (Free-plan handlers can fail with `EXCEEDED_CPU`).
- Mail sent via `send_email` shows as "dropped" in the Email Routing summary even when delivered.
- Workers cannot open outbound TCP to port 25; use Email Service instead.

Sources: https://developers.cloudflare.com/email-service/platform/limits/, https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/

### Pricing (as of 2026-10-05)

| Item | Workers Free | Workers Paid |
| --- | --- | --- |
| Outbound (Email Sending) | Not available (except to verified addresses) | 3,000 per month included, then $0.35 per 1,000 |
| Inbound (Email Routing) | Unlimited | Unlimited |

Hard bounces count toward the quota; sends rejected at the API boundary (for example by the suppression list) do not; Email Workers are billed as Workers.

Sources: https://developers.cloudflare.com/email-service/platform/pricing/

### Most useful pages

- [Email Service overview](https://developers.cloudflare.com/email-service/) - both halves
- [Send emails](https://developers.cloudflare.com/email-service/get-started/send-emails/) and [Route emails](https://developers.cloudflare.com/email-service/get-started/route-emails/) - get started
- [Workers send API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) - binding
- [Email handler](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) - inbound Workers
- [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) and [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/)
- [Configure send bindings](https://developers.cloudflare.com/email-service/configuration/send-bindings/)
- [Email authentication](https://developers.cloudflare.com/email-service/concepts/email-authentication/) and [deliverability](https://developers.cloudflare.com/email-service/concepts/deliverability/)
- [Magic link example](https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/)
- [Limits](https://developers.cloudflare.com/email-service/platform/limits/) and [Pricing](https://developers.cloudflare.com/email-service/platform/pricing/)

## 12. Pages (not in the sidebar)

### What it is

Pages deploys full-stack sites to Cloudflare's network from a Git repository, by Direct Upload of prebuilt assets, or with the C3 CLI, with serverless Pages Functions for dynamic code.
Pages is not in the docs sidebar (as of 2026-10-05), and its overview opens with a redirect to Workers: "Are you sure you want to use Pages? Workers supports most Pages use cases and offers a broader feature set. It is Cloudflare's primary platform for building applications. Start new projects with Workers."

Sources: https://developers.cloudflare.com/pages/, https://developers.cloudflare.com/pages/get-started/git-integration/

### Status

- Available on all plans; no deprecation or end-of-life date is stated anywhere in the mirrored Pages docs, but new projects are steered to Workers (as of 2026-10-05).
- Build images: v1 projects move to v3 automatically on September 15, 2026 and v2 projects on February 23, 2027; v3 updates default tools to their LTS versions as of May 2025.

Sources: https://developers.cloudflare.com/pages/, https://developers.cloudflare.com/pages/configuration/build-image/

### Key concepts

- **Deployment methods**: Git integration (GitHub, GitLab) with automatic builds, Direct Upload (Wrangler or dashboard), C3.
- **Preview deployments**: every branch or pull request gets a unique preview URL on `pages.dev`; unlimited previews per project; branch deployment controls and custom branch aliases.
- **Rollbacks** to previous production deployments.
- **Serving**: Pages auto-detects SPA vs custom 404 behaviour from `index.html` / `404.html`; `_headers` and `_redirects` files.
- **Pages Functions**: file-based routing under `/functions` (`[id]` and `[[path]]` dynamic segments), `_middleware.js` (including in front of static files), handlers `onRequest`, `onRequestGet`, `onRequestPost` and the other method variants, `EventContext` with `request`, `env`, `params`, `data`, `functionPath`, `waitUntil()`, `passThroughOnException()`, `next()`; `env.ASSETS.fetch()` serves static files.
- **Advanced mode**: a single `_worker.js` (module syntax) replaces the `/functions` directory entirely.
- **`_routes.json`** controls which paths invoke Functions (at most 100 include/exclude rules combined); excluding static paths keeps those requests free.
- **Pages Plugins**: Cloudflare Access, Google Chat, GraphQL, hCaptcha, Honeycomb, Sentry, Static Forms, Stytch, Turnstile, vercel/og, community plugins.
- Smart Placement works for Pages Functions.

Sources: https://developers.cloudflare.com/pages/functions/api-reference/, https://developers.cloudflare.com/pages/functions/routing/, https://developers.cloudflare.com/pages/functions/middleware/, https://developers.cloudflare.com/pages/functions/advanced-mode/, https://developers.cloudflare.com/pages/configuration/preview-deployments/, https://developers.cloudflare.com/pages/llms.txt

### Limits (as of 2026-10-05)

| Limit | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Concurrent builds | 1 | 5 | 20 | not listed |
| Builds per month | 500 | 5,000 | 20,000 | not listed |
| Build timeout | 20 minutes | 20 minutes | 20 minutes | 20 minutes |
| Custom domains per project | 100 | 250 | 500 | 500 (more via account team) |
| Files per site | 20,000 | 100,000 (set `PAGES_WRANGLER_MAJOR_VERSION=4`) | 100,000 | 100,000 |

- File size 25 MiB; `_headers` 100 rules, 2,000 characters per header; `_redirects` 2,000 static plus 100 dynamic (2,100 total); unlimited preview deployments; 100 projects per account ("not routinely increased"; the docs point to Workers for Platforms or Workers static assets beyond that); new accounts are throttled on project creation in their first 48 hours.
- Concurrent builds are counted per account.

Sources: https://developers.cloudflare.com/pages/platform/limits/

### Pricing (as of 2026-10-05)

- Static asset requests are free and unlimited on all plans (a request is static if it does not invoke Functions).
- Pages Functions are billed exactly as Workers (Free: shared 100,000 requests per day with Workers; Paid: Standard usage model), including requests from Functions to KV or Durable Object bindings.

Sources: https://developers.cloudflare.com/pages/functions/pricing/, https://developers.cloudflare.com/workers/platform/pricing/

### Relation to Workers and migration

The migration guide says Workers supports full-stack apps (static assets, APIs, SSR) with a similar cost structure, and "a distinctly broader set of features (including Durable Objects, Cron Triggers, and more comprehensive Observability)".
Migration steps: swap Pages-specific framework adapters for Workers ones; create a Wrangler config with `name` and `compatibility_date`; replace `pages_build_output_dir` with `assets.directory`; set `not_found_handling` explicitly (`single-page-application` or `404-page`); compile a `/functions` folder into a Worker with Wrangler or port `_worker.js`; move bindings, variables and secrets; replace Pages-only Wrangler commands; move builds to Workers Builds; map preview environments to Previews or version URLs; keep `_headers` and `_redirects`; handle `pages.dev` and custom domains; roll out gradually.

Sources: https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/

Compatibility matrix (from the migration guide, as of 2026-10-05; "Partial" means unsupported with a workaround):

| Feature | Workers | Pages |
| --- | --- | --- |
| Cloudflare Vite plugin | Yes | No |
| Rollbacks | Yes | Yes |
| Gradual deployments | Yes | No |
| Preview URLs | Yes | Yes |
| Testing tools, local development | Yes | Yes |
| Remote development (`--remote`), dashboard Quick Editor | Yes | No |
| Early Hints | Partial (zone setting plus `Link` headers) | Yes |
| Custom headers, redirects, Smart Placement | Yes | Yes |
| Middleware | Yes (via `run_worker_first`, billed as invocations) | Yes |
| Serve assets on a path | Yes | No |
| Workers Logs, Logpush, Tail Workers, Source Maps | Yes | No |
| Real-time logs | Yes | Yes |
| Node.js compatibility | Yes | Yes |
| Durable Objects | Yes | Partial (separate Worker plus binding) |
| Cron Triggers | Yes | No |
| Bindings: AI, Analytics Engine, Assets, Browser Run, D1, env vars, Hyperdrive, KV, mTLS, Queue producers, R2, Secrets, Service bindings, Vectorize | Yes | Yes |
| Email Workers, Image Resizing, Queue consumers, Rate Limiting | Yes | No |
| Monorepos, build watch paths, build caching, Deploy Hooks | Yes | Yes |
| Branch deploy controls | Partial (preview builds) | Yes |
| Custom branch aliases | Coming soon | Yes |
| File-based routing, Pages Plugins | Partial (frameworks or Wrangler-compiled `functions/`) | Yes |
| Custom domains and subdomains | Yes | Yes |
| Custom domains outside Cloudflare zones | No | Yes |
| Non-root routes | Yes | No |

Sources: https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/

### How it composes with other products

Pages Functions can bind to KV, D1, R2, Durable Objects (defined in a separate Worker), Queues (producer only), Workers AI, Vectorize, Hyperdrive, service bindings and can call Workflows; Pages builds can trigger via Deploy Hooks; Zaraz and Web Analytics integrate.

Sources: https://developers.cloudflare.com/pages/functions/bindings/, https://developers.cloudflare.com/workflows/build/call-workflows-from-pages/, https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/

### Most useful pages

- [Pages overview](https://developers.cloudflare.com/pages/) - including the "use Workers" note
- [Migrate from Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/) - migration and compatibility matrix
- [Pages Functions](https://developers.cloudflare.com/pages/functions/) and [routing](https://developers.cloudflare.com/pages/functions/routing/)
- [Functions API reference](https://developers.cloudflare.com/pages/functions/api-reference/) - EventContext
- [Advanced mode](https://developers.cloudflare.com/pages/functions/advanced-mode/) - `_worker.js`
- [Functions pricing](https://developers.cloudflare.com/pages/functions/pricing/)
- [Limits](https://developers.cloudflare.com/pages/platform/limits/)
- [Build image](https://developers.cloudflare.com/pages/configuration/build-image/) - v1/v2 to v3 dates
- [Preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
- [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)
- [Known issues](https://developers.cloudflare.com/pages/platform/known-issues/)

## 13. Dynamic Workers (not in the sidebar)

### What it is

Dynamic Workers spin up Workers at runtime to run arbitrary code in a sandboxed isolate, as "a lightweight alternative to containers for securely sandboxing code you don't trust".
They are "the lowest-level primitive for spinning up a Worker": the parent Worker decides the code, the bindings the child receives, whether it can reach the network, and its limits.
Use cases listed: AI agent "Code Mode", running AI-generated apps, fast previews and playgrounds, custom automations, and platforms running user-uploaded code.
Dynamic Workers are not in the docs sidebar (as of 2026-10-05) but have their own docs section.

Sources: https://developers.cloudflare.com/dynamic-workers/, https://developers.cloudflare.com/workers/runtime-apis/bindings/

### Status

- Workers Paid plan only, as of 2026-10-05; no beta label appears on its pages.
- Billing of "Dynamic Workers created daily" started May 26, 2026; dashboard usage data goes back to June 1, 2026.

Sources: https://developers.cloudflare.com/dynamic-workers/pricing/

### API and binding surface

```jsonc
{ "worker_loaders": [ { "binding": "LOADER" } ] }
```

```js
const worker = env.LOADER.load({
  compatibilityDate: "2026-10-05",
  mainModule: "src/index.js",
  modules: { "src/index.js": `export default { fetch() { return new Response("Hello from a dynamic Worker"); } };` },
  globalOutbound: null, // block all outbound network access
});
```

- `env.LOADER.load(code)` creates a one-off Dynamic Worker; `env.LOADER.get(id, async () => code)` reuses a cached Worker for a stable ID.
- `WorkerCode` fields: `compatibilityDate`, `compatibilityFlags`, `allowExperimental`, `mainModule`, `modules`, `globalOutbound` (a service stub to intercept egress, or `null` to block), `env` (bindings and structured data passed in), `tails` (Tail Workers), and `limits: { cpuMs, subRequests }`.
- Extras: static assets for Dynamic Workers, Durable Object Facets (run loaded code as a child Durable Object with its own isolated SQLite database), and Dynamic Workflows (durable Workflows defined by runtime-loaded code, for example per-tenant automations).

Sources: https://developers.cloudflare.com/dynamic-workers/getting-started/, https://developers.cloudflare.com/dynamic-workers/api-reference/, https://developers.cloudflare.com/dynamic-workers/usage/limits/, https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/, https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/

### Limits (as of 2026-10-05)

| Context | Concurrent distinct Dynamic Workers with in-flight requests |
| --- | --- |
| Worker request | 4 |
| Durable Object | 10 (previously 4) |

By default each Dynamic Worker uses the parent plan's CPU and subrequest limits; custom limits can only lower them, and hitting one throws immediately.

Sources: https://developers.cloudflare.com/dynamic-workers/platform/limits/, https://developers.cloudflare.com/dynamic-workers/usage/limits/

### Pricing (as of 2026-10-05)

| Dimension | Included | Overage |
| --- | --- | --- |
| Dynamic Workers created daily | 1,000 unique Dynamic Workers per month | $0.002 per Dynamic Worker per day |
| Requests | 10 million per month | $0.30 per million (Workers Standard rate) |
| CPU time | 30 million CPU-ms per month | $0.02 per million CPU-ms (Workers Standard rate) |

- A Dynamic Worker is unique per Worker ID plus code; `load()` or no ID counts one per invocation, so use `get()` with a stable ID.
- Each `fetch()` and each RPC call on a stub is a request (RPC sessions billed as in Durable Objects).
- CPU time includes isolate startup and code parsing, not only execution.

Sources: https://developers.cloudflare.com/dynamic-workers/pricing/

### How it composes with other products

Dynamic Workers relate to Workers for Platforms (platforms running user code), Durable Objects (facets), Workflows (dynamic workflows), Tail Workers (observability) and the Agents SDK (Code Mode); `ctx.exports` loopback bindings with custom `props` can be passed into a Dynamic Worker's `env`.

Sources: https://developers.cloudflare.com/dynamic-workers/, https://developers.cloudflare.com/workers/runtime-apis/context/

### Most useful pages

- [Dynamic Workers overview](https://developers.cloudflare.com/dynamic-workers/) - entry point
- [Getting started](https://developers.cloudflare.com/dynamic-workers/getting-started/) - Worker Loader binding
- [API reference](https://developers.cloudflare.com/dynamic-workers/api-reference/) - load, get, WorkerCode
- [Egress control](https://developers.cloudflare.com/dynamic-workers/usage/egress-control/) - globalOutbound
- [Bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/) - passing capabilities
- [Custom resource limits](https://developers.cloudflare.com/dynamic-workers/usage/limits/) - cpuMs, subRequests
- [Durable Object Facets](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) - per-tenant storage
- [Dynamic Workflows](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/) - durable runtime code
- [Pricing](https://developers.cloudflare.com/dynamic-workers/pricing/) and [Limits](https://developers.cloudflare.com/dynamic-workers/platform/limits/)

## 14. Workers runtime limits that matter for API proxies and backends

All values as of 2026-10-05; Durable Objects, Workflows and Queues consumers inherit these unless their own section says otherwise.

### CPU time and wall time

- CPU time counts only active execution, not time waiting on `fetch()`, KV, databases or other I/O; the docs put the average Worker at about 2.2 ms per request and heavy auth, SSR or parsing at 10 to 20 ms.
- Free: 10 ms per HTTP request and per cron; exceeding returns Error 1102 ("Worker exceeded resource limits", outcome `exceededCpu`).
- Paid: default 30 seconds, configurable up to 5 minutes with `"limits": { "cpu_ms": 300000 }` or in the dashboard; a lower custom `cpu_ms` is the documented guard against runaway bills and "denial-of-wallet" attacks.
- Isolates get "some built-in flexibility" for occasional overruns, but consistent overruns are terminated.
- Wall time: HTTP requests have no limit while the client stays connected (streaming responses keep the Worker alive); `ctx.waitUntil()` adds at most 30 seconds after the response or disconnect, shared by all `waitUntil()` calls; Cron Triggers, Queue consumers and Durable Object alarms are capped at 15 minutes; Durable Object RPC/HTTP and Workflows steps are unlimited.
- Runtime updates (a few times per week) give in-flight requests a 30-second grace period, so very long requests can be cut.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/runtime-apis/context/, https://developers.cloudflare.com/workers/platform/pricing/

### Subrequests and outbound connections

- Subrequests (any `fetch()` or call to R2, KV, D1 and other Cloudflare services) are limited to 50 per invocation on Free and 10,000 by default on Paid, raisable to 10,000,000 with `limits.subrequests`; internal-service subrequests are capped at 1,000 on Free.
- Each hop in a redirect chain counts; subrequests have no individual time limit; subrequests are not billed.
- Only six connections per invocation may be waiting for response headers at the same time; a seventh `fetch()`, KV/R2/Cache/Queues call, TCP `connect()` or outbound WebSocket is queued until one of the six receives headers.
- The connection limit is measured from the top-level request, and Workers invoked through service bindings share it.
- Call `response.body.cancel()` on bodies you do not read.
- Service binding calls do not count toward the six-connection limit but do count toward subrequests, and a request can chain at most 32 Worker invocations.
- `fetch()` cannot target raw IP addresses (use a DNS record); with a Partial (CNAME) zone setup every fetched hostname needs a Cloudflare DNS record.
- The Rate Limiting binding (`limit({ key })`, periods 10 or 60 seconds) is per Cloudflare location and eventually consistent, so it protects upstream keys roughly, not exactly.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/, https://developers.cloudflare.com/workers/platform/known-issues/, https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/, https://developers.cloudflare.com/workers/wrangler/configuration/

### Memory, size and startup

- 128 MB per isolate (JS heap plus Wasm), shared by concurrent requests in that isolate; exceeding it returns Error 1102 (`exceededMemory`), and buffering a too-large body fails with `Memory limit would be exceeded before EOF`; the docs say to stream bodies and to use Zod 4.5.0 or later.
- Worker bundle up to 64 MiB uncompressed on both plans; global scope must finish within 1 second (error 10021 on deploy).
- 64 (Free) or 128 (Paid) environment variables plus secrets per Worker, 5 KB each.

Sources: https://developers.cloudflare.com/workers/platform/limits/

### Request and response size

- Request body: 100 MB on Free and Pro zones, 200 MB on Business, up to 5 GB self-serve on Enterprise (413 above); URL 16 KB; request and response headers 128 KB each.
- Response bodies are not limited, but cacheable objects are capped at 512 MB (5 GB Enterprise) and Cache API objects at 512 MB.
- RPC payloads over service bindings are limited to 32 MiB serialized (stream larger data).
- Log data per request is capped at 256 KB.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/

### WebSockets

- Inbound WebSocket messages are limited to 32 MiB (close code 1009 above); the same 32 MiB applies to Durable Objects.
- A WebSocket connection to a Worker is billed as one request (the Upgrade); messages through a plain Worker are not billed.
- Outbound WebSockets count toward the six-connection limit while connecting.
- For many long-lived client connections, the docs route you to Durable Objects with the Hibernation API: up to 32,768 sockets per object, no duration billing while hibernated, incoming messages billed at 20:1 and auto-responses free.
- Behaviour changed by compatibility date: auto-reply to Close frames from 2026-04-07 (`allowHalfOpen` for proxies) and `Blob` binary messages from 2026-03-17.

Sources: https://developers.cloudflare.com/workers/runtime-apis/websockets/, https://developers.cloudflare.com/durable-objects/platform/limits/, https://developers.cloudflare.com/workers/platform/pricing/, https://developers.cloudflare.com/durable-objects/best-practices/websockets/

### TCP sockets

- `connect()` from `cloudflare:sockets` is a public beta as of 2026-10-05, with TLS (`secureTransport: "on"`) or StartTLS.
- Blocked: Cloudflare IP ranges, `localhost`, private network IPs, port 25, and loops back to the same Worker; sockets must be created inside a handler.
- Each socket counts toward the six-connection limit while connecting.
- Outbound TCP comes from a prefix outside Cloudflare's published IP list.
- In a Durable Object, an open socket keeps the object alive and billed for up to 15 minutes per connection.
- Inbound TCP is not supported; Workers VPC Network bindings add `connect()` into private networks.

Sources: https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/, https://developers.cloudflare.com/workers/platform/betas/, https://developers.cloudflare.com/workers-vpc/api/

### Daily request cap on Free

On Workers Free, 100,000 requests per day (reset 00:00 UTC) are shared by Workers, Pages Functions and Workflows instance creations; over the cap a route either fails open (bypasses the Worker) or fails closed (Error 1027), and assets behind `run_worker_first` return 429.

Sources: https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workflows/reference/pricing/, https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/

## 15. Build hooks for Web3 projects

These are suggestions for dapps, token launchpads, trading UIs, bots and indexers on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663), mapped to documented features; the chain-specific framing is this knowledge base's, not Cloudflare's, and every item is an (inference) built on the cited facts.
Chain details live in the owner's Robinhood Chain and Jupiter + Meteora knowledge bases, and launch sequencing in `web3-launch-playbook.md`.

### Workers as an RPC key-hiding proxy

- Put the paid RPC URL (Helius, Alchemy, QuickNode or a Robinhood Chain provider) in a Worker secret and expose a `/rpc` route that forwards JSON-RPC, so browser bundles never contain the key; bindings and secrets keep credentials out of code (https://developers.cloudflare.com/workers/configuration/secrets/, https://developers.cloudflare.com/workers/runtime-apis/bindings/).
- Allowlist JSON-RPC methods (for example block `eth_sendRawTransaction` from anonymous callers, or only allow `getAccountInfo`, `getLatestBlockhash` and `sendTransaction` on Solana) and cap body size before forwarding.
- Use the Rate Limiting binding keyed on wallet address or API key (the docs advise against IP keys) as a cheap first filter, remembering it is per location and approximate (https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/).
- Keep `limits.cpu_ms` low on the proxy to cap denial-of-wallet risk; waiting on the upstream RPC costs no CPU (https://developers.cloudflare.com/workers/platform/pricing/).
- Batch JSON-RPC calls or fan out carefully: only six upstream connections can be waiting for headers at once per request, so fan-out of dozens of calls serializes (https://developers.cloudflare.com/workers/platform/limits/).
- RPC endpoints must be hostnames, not raw IPs; a self-hosted node on a private network can be reached through a Workers VPC Service or Network binding instead of exposing it publicly (https://developers.cloudflare.com/workers/platform/known-issues/, https://developers.cloudflare.com/workers-vpc/).
- Cache idempotent reads (token lists, metadata, `eth_chainId`, historical blocks) with Workers Cache using `Cache-Control`; only `GET` and `HEAD` are cached, so expose cached reads as GET routes rather than JSON-RPC POSTs (https://developers.cloudflare.com/workers/cache/limitations/).
- Use Smart Placement or a `placement.region` hint near the RPC provider's region when one request makes several sequential RPC calls (https://developers.cloudflare.com/workers/configuration/placement/).
- With compatibility dates from 2026-08-04, `nodejs_compat` is on by default, which helps npm SDKs that expect Buffer, crypto, streams or http; Web Crypto lists Ed25519 (Solana signatures) and ECDSA but not secp256k1, so EVM signing needs a JS library (https://developers.cloudflare.com/workers/runtime-apis/nodejs/, https://developers.cloudflare.com/workers/runtime-apis/web-crypto/).

### Cron Triggers and alarms as keepers

- Cron Triggers run at one-minute granularity with up to 15 minutes wall time and (Paid) 30 seconds CPU for sub-hourly schedules: enough for price-oracle pokes, liquidation checks, vesting releases or launchpad state sweeps on Base, Ethereum or Robinhood Chain (https://developers.cloudflare.com/workers/configuration/cron-triggers/, https://developers.cloudflare.com/workers/platform/limits/).
- Cron accounts are limited to 5 (Free) or 250 (Paid) triggers per account, so one cron should dispatch many jobs (for example into a Queue).
- For per-market or per-launch timers, a Durable Object alarm gives millisecond-granularity, at-least-once, retried scheduling per object (one alarm per object, multiplexed via storage) (https://developers.cloudflare.com/durable-objects/api/alarms/).
- Keep a hot-wallet signer behind a single Durable Object per wallet so nonce assignment is serialized by the object's single-threaded execution and stored transactionally in SQLite (https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/).

### Durable Objects for price feeds, order books and live UIs

- One Durable Object per trading pair or per launch can hold the order book or bonding-curve state in SQLite and push updates to browsers over hibernatable WebSockets (up to 32,768 per object, no duration billing while idle) (https://developers.cloudflare.com/durable-objects/best-practices/websockets/, https://developers.cloudflare.com/durable-objects/platform/limits/).
- Respect the roughly 500 to 1,000 requests per second per object: shard hot markets (for example one object per pair plus fan-out objects per region of subscribers), and never use one global singleton (https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/).
- An upstream feed (a Solana WebSocket subscription, an EVM `eth_subscribe` stream) can be held by a Durable Object as an outbound WebSocket, but the object then stays active and billed while connected; inbound messages above 32 MiB close the socket (https://developers.cloudflare.com/durable-objects/platform/pricing/, https://developers.cloudflare.com/workers/runtime-apis/websockets/).
- Use `locationHint` (`enam`, `weur`, `apac` and others) to place a market's object near its matching engine or RPC provider (https://developers.cloudflare.com/durable-objects/reference/data-location/).
- Point-in-time recovery (30 days) gives a rollback path for order-book state after a bad deploy (https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/).

### Queues for transaction pipelines

- Accept user intents (swap, claim, mint) in a Worker, enqueue them, and let a consumer sign and broadcast with retries and a dead letter queue; messages are up to 128 KB and a queue takes 5,000 messages per second (https://developers.cloudflare.com/queues/platform/limits/).
- Delivery is at least once and unordered, so key every message by an idempotency key (client nonce, transaction hash or intent ID) and keep per-wallet ordering in a Durable Object (https://developers.cloudflare.com/queues/reference/delivery-guarantees/).
- Use `delaySeconds` (up to 24 hours) for "check confirmation in N seconds" retries, and `max_concurrency` to stay under RPC provider rate limits (https://developers.cloudflare.com/queues/configuration/javascript-apis/, https://developers.cloudflare.com/queues/tutorials/handle-rate-limits/).
- Pull consumers let an off-Cloudflare signer (for example an HSM-backed service) drain the same queue over HTTPS (https://developers.cloudflare.com/queues/configuration/pull-consumers/).

### Workflows for multi-step launches

- Model a token launch as one Workflow instance: create mint or deploy contract, wait for confirmations (`step.sleep`), seed liquidity (for example a Meteora pool on Solana or a Uniswap pool on an EVM chain), verify, then announce; each `step.do` result is persisted and retried with backoff (https://developers.cloudflare.com/workflows/build/workers-api/, https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).
- Use the launch ID as the instance ID (instance IDs are unique), throw `NonRetryableError` for permanent failures such as an invalid mint authority, and make every on-chain step idempotent because a step can re-run after a failure (https://developers.cloudflare.com/workflows/build/rules-of-workflows/).
- `step.waitForEvent()` (default timeout 24 hours) can wait for an off-chain approval or an indexer callback that calls `instance.sendEvent()` (https://developers.cloudflare.com/workflows/build/events-and-parameters/).
- Vesting or unlock schedules can sleep up to 365 days per step, and sleeping instances do not count toward concurrency (https://developers.cloudflare.com/workflows/reference/limits/).
- Workflows cannot run inside Workers for Platforms namespaces, which matters for a launchpad that hosts creator code there (https://developers.cloudflare.com/workflows/reference/limits/).

### Containers for heavier indexers and tools

- Run code that does not fit an isolate (a Rust or Go indexer, a Solana geyser or Yellowstone gRPC consumer, an EVM log indexer using native libraries, Foundry or Anchor CLIs) in a Container, reached from a Worker through its Durable Object (https://developers.cloudflare.com/containers/).
- Instances have no fixed maximum runtime but can be stopped by host restarts (SIGTERM, up to 15 minutes, then SIGKILL), so checkpoint the indexed block or slot to D1, R2 or the owning Durable Object (https://developers.cloudflare.com/containers/faq/).
- Disk is ephemeral; persist with R2 (FUSE mount) or snapshots on the `durable_object` policy (https://developers.cloudflare.com/containers/concepts/architecture/).
- Scaling is manual (`getRandom` or explicit IDs), and egress beyond the included 1 TB (North America and Europe) is billed per GB, which matters for chatty RPC indexing (https://developers.cloudflare.com/containers/configuration/scaling-and-routing/, https://developers.cloudflare.com/containers/platform/pricing/).
- `outbound` handlers can inject RPC API keys into container traffic so the image never holds them (https://developers.cloudflare.com/containers/configuration/outbound-traffic/).

### Browser Run, Email, Flagship and platforms

- Browser Run can render OG images or share cards for tokens and pre-render SPA dapp pages for crawlers (https://developers.cloudflare.com/browser-run/how-to/og-images-astro/, https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/).
- Email Service can send magic-link sign-in or launch alerts (Paid, beta) and an `email()` handler can turn inbound support mail into tickets (https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/).
- Flagship can gate risky trading-UI features per wallet or region with percentage rollouts while it is in public beta (https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/).
- A launchpad that lets creators deploy custom pages or code can host them as user Workers in Workers for Platforms with per-tenant CPU caps and outbound Workers that block unapproved RPC hosts, plus Cloudflare for SaaS for creators' own domains (https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/).
- An AI trading assistant that writes and runs code can execute it in a Dynamic Worker with `globalOutbound: null` or an interceptor, so generated code cannot exfiltrate keys (https://developers.cloudflare.com/dynamic-workers/usage/egress-control/).
- New dapp front ends should be Workers with static assets (asset requests are free) rather than Pages (https://developers.cloudflare.com/pages/, https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/).

## 16. Gaps and contradictions

Pages that disagree with each other or leave something out, as of 2026-10-05; neither side is preferred.

### Cross-product

- CPU caps for Cron Triggers and Queue consumers are stated three ways: Workers limits (Cron 30 s under hourly, 15 min hourly or slower), Workers and Workers for Platforms pricing ("Max of 15 minutes of CPU time per Cron Trigger or Queue Consumer invocation"), and Queues limits (consumer CPU "Configurable to 5 minutes"). https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/platform/pricing/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/, https://developers.cloudflare.com/queues/platform/limits/
- Cron Trigger counts: 5 / 250 per account (Workers limits), "per Worker" wording (Cron Triggers page), and "up to three Cron Triggers" per Worker (Durable Objects alarms page). https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workers/configuration/cron-triggers/, https://developers.cloudflare.com/durable-objects/api/alarms/
- Script size: Workers limits say 64 MiB on both plans; Workflows limits say 3 MB (Free) and 10 MB (Paid) "per Worker size limits". https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/workflows/reference/limits/
- Max CPU per invocation: Workers Paid allows 5 minutes; the Workers for Platforms pricing table says "Max of 30 seconds". https://developers.cloudflare.com/workers/platform/limits/, https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/
- Static asset billing: "free and unlimited" vs billed per request when served from Workers Cache. https://developers.cloudflare.com/workers/platform/pricing/
- Beta labels live in different places: the Workers Betas page lists only Email Workers, Green Compute and TCP Sockets, while Smart Placement, Tail Workers, tracing, Workers VPC, Flagship, Email Sending, Secrets Store, the Containers `durable_object` policy, Browser Run `/crawl` and Kitesurf are marked beta only on their own pages or in the changelog. https://developers.cloudflare.com/workers/platform/betas/
- Mirror gap: `/workers/runtime-apis/bindings/worker-loader/` is linked from the bindings page but missing from the 2026-10-05 mirror.

### Workers

- Outbound WebSockets: the Protocols table leaves "Outbound" WebSockets blank, while the WebSockets and limits pages document outbound WebSockets via `fetch()` with `Upgrade: websocket` and `new WebSocket(url)`. https://developers.cloudflare.com/workers/reference/protocols/ vs https://developers.cloudflare.com/workers/runtime-apis/websockets/
- The Vectorize section of the Workers pricing page says Vectorize "is currently only available on the Workers paid plan" but its table shows Free-plan allowances. https://developers.cloudflare.com/workers/platform/pricing/
- The `fetch` page says brotli support will "soon" be on by default "past an upcoming compatibility date" with no date given. https://developers.cloudflare.com/workers/runtime-apis/fetch/
- Inbound TCP to Workers is "coming soon", linking a blog post. https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/

### Containers

- The scaling page says "Today, Containers are scaled manually" and promises "built-in autoscaling and routing features in the near future", with no date, while `max_instances` exists in config. https://developers.cloudflare.com/containers/configuration/scaling-and-routing/
- The pricing table's Free row reads "N/A" for memory and CPU and leaves disk blank. https://developers.cloudflare.com/containers/platform/pricing/
- No page gives a maximum number of instances per application beyond the account-wide concurrency caps.

### Durable Objects

- Per-object storage on Free: the limits table lists "Storage per Durable Object: 10 GB" with a footnote that Free accounts have 5 GB total, while the FAQ on the same page says the per-object maximum is "10 GB on Workers Paid, or 1 GB on the Free plan". https://developers.cloudflare.com/durable-objects/platform/limits/
- Throughput: the limits FAQ states "a soft limit of 1,000 requests per second", while the rules page states "approximately 500-1,000 requests per second for simple operations". https://developers.cloudflare.com/durable-objects/platform/limits/ vs https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/
- The Workers pricing page still says SQLite storage billing "will be enabled in January 2026", while the release notes record billing as of 2026-01-07. https://developers.cloudflare.com/workers/platform/pricing/

### Queues

- The limits page says the limits "apply to both Workers Paid and Workers Free plans with the exception of Message Retention", but Free operations are capped at 10,000 per day on the pricing page, which the limits page does not mention. https://developers.cloudflare.com/queues/platform/limits/ vs https://developers.cloudflare.com/queues/platform/pricing/
- The `contentType` option is described as "for internal use" in one paragraph of the JavaScript APIs page while other paragraphs document `json`, `text`, `bytes` and `v8` for producers. https://developers.cloudflare.com/queues/configuration/javascript-apis/

### Workflows

- Concurrency: the limits table says 50,000 concurrent instances on Paid, while the text below it says "only actively running instances count toward the 10,000 concurrent instance limit". https://developers.cloudflare.com/workflows/reference/limits/
- Billing start: the Workers pricing page says Cloudflare "will not bill step and storage usage before the start date announced in the Workflows billing changelog", while the Workflows pricing page names August 10th, 2026. https://developers.cloudflare.com/workers/platform/pricing/ vs https://developers.cloudflare.com/workflows/reference/pricing/
- The Workflows pricing table labels the requests row "Requests (millions)" while listing Free as "100,000 per day". https://developers.cloudflare.com/workflows/reference/pricing/

### Flagship

- No pricing or plan-availability page, and the docs pages themselves never say "beta"; the beta status comes only from the 2026-05-26 changelog post. https://developers.cloudflare.com/flagship/, https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/
- The overview mentions only KV as the backing infrastructure, while the launch post says "backed by Workers KV and Durable Objects". https://developers.cloudflare.com/flagship/ vs https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/

### Browser Run (formerly Browser Rendering)

- Older changelog entries state Browser Rendering "is now out of beta and available to all customers with Workers Paid Plan" and that the REST API was "Available to all customers with a Workers Paid Plan", while current pages say "Available on Free and Paid plans". https://developers.cloudflare.com/browser-run/changelog/ vs https://developers.cloudflare.com/browser-run/
- The rename post lists Paid concurrency as 120, superseded by 200 on the limits page and the 2026-08-20 changelog. https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/ vs https://developers.cloudflare.com/browser-run/limits/
- Two code samples still call the old `/browser-rendering/screenshot` REST path instead of `/browser-run/`. https://developers.cloudflare.com/browser-run/get-started/, https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/
- Paid `/crawl` limits (jobs per day, pages per crawl) are not listed.

### Workers VPC

- The overview says "currently in beta", while the pricing page says "Free during Open Beta"; neither gives a GA date or post-beta price. https://developers.cloudflare.com/workers-vpc/, https://developers.cloudflare.com/workers-vpc/platform/pricing/

### Email Service

- The Workers Betas page lists Email Workers as a public beta, while the Email Service overview presents Email Routing (including Worker routing) without a beta label and marks only Email Sending as beta. https://developers.cloudflare.com/workers/platform/betas/ vs https://developers.cloudflare.com/email-service/
- The daily sending quota for new accounts is not stated numerically. https://developers.cloudflare.com/email-service/platform/limits/

### Pages (not in the sidebar)

- The Pages changelog's latest entry is from 2025-04-18, while the build-image page (and the overview's Workers note) carry later dates, so the changelog looks unmaintained. https://developers.cloudflare.com/pages/platform/changelog/ vs https://developers.cloudflare.com/pages/configuration/build-image/
- The Pages Functions pricing page links "Standard usage model" to an anchor (`#example-pricing-standard-usage-model`) that no longer exists on the Workers pricing page. https://developers.cloudflare.com/pages/functions/pricing/
- No page states a deprecation date for Pages; the only signal is the "Start new projects with Workers" note. https://developers.cloudflare.com/pages/

### Dynamic Workers (not in the sidebar)

- The pricing table's "Dynamic Workers created daily" row gives the inclusion as "1,000 unique Dynamic Workers per month" but the overage as "+$0.002 per Dynamic Worker per day", and the text says "The count resets daily", so the unit of the included amount is unclear. https://developers.cloudflare.com/dynamic-workers/pricing/
