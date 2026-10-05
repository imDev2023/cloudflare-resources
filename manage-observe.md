# Manage & Observe: Observe (Observability, Analytics, Logs, Alerts)

This file covers the "Manage & Observe > Observe" section of the Cloudflare docs sidebar plus Notifications (now titled "Alerts" in the docs), as mirrored on 2026-10-05 under `raw/docs/`.
Cloudflare's observability stack has three layers.
Analytics are aggregated and usually adaptively sampled (dashboard, GraphQL Analytics API, the newer SQL API, Workers Analytics Engine, Web Analytics).
Logs are per-event records that leave Cloudflare through Logpush (now on every plan with usage-based pricing since 2026-09-30), stream live through Instant Logs, or are stored and queried inside Cloudflare through Log Explorer and the Cloudflare Observability "Logs" view.
Alerts (Notifications) fire on built-in conditions or, in the new Custom Alerts beta, on any SQL API query, and deliver to email, webhooks or PagerDuty.
The biggest moves as of 2026-10-05 are: Logpush on Free, Pro and Business with 25 GB of included exports per account; a unified Cloudflare Observability pricing model for logs and traces starting 2026-12-01; at least 31 days of adaptive analytics retention on every plan since 2026-10-02; a new Analytics SQL API (`/client/v4/analytics/sql`) with a Workers binding; and Cloudflare Traces (per-domain request tracing with OpenTelemetry export).
Standalone Health Checks (Pro and above) monitor origins from up to 13 regions and are now presented as part of Smart Shield.

## Table of contents

1. [Scope and source pages](#scope-and-source-pages)
2. [Cloudflare Observability (umbrella, Logs view, Traces, Export, pricing)](#cloudflare-observability)
3. [Analytics](#analytics)
   - [Types of analytics and dashboards](#types-of-analytics-and-dashboards)
   - [Sampling (ABR)](#sampling-abr)
   - [Account and zone analytics](#account-and-zone-analytics)
   - [Custom dashboards](#custom-dashboards)
   - [Network Analytics](#network-analytics)
   - [GraphQL Analytics API](#graphql-analytics-api)
   - [Analytics SQL API](#analytics-sql-api)
   - [Workers Analytics Engine](#workers-analytics-engine)
   - [Analytics integrations](#analytics-integrations)
4. [Web Analytics](#web-analytics)
5. [Logs](#logs)
   - [Logpush](#logpush)
   - [Logpush datasets](#logpush-datasets)
   - [Logpush destinations](#logpush-destinations)
   - [Job configuration, filters, output options, Transformers](#job-configuration-filters-output-options-transformers)
   - [Logpush health, retries, alerts](#logpush-health-retries-alerts)
   - [Logpush pricing and plan availability](#logpush-pricing-and-plan-availability)
   - [Edge Log Delivery](#edge-log-delivery)
   - [Instant Logs](#instant-logs)
   - [Logpull (legacy)](#logpull-legacy)
   - [Logs Engine (being replaced)](#logs-engine-being-replaced)
   - [Workers Trace Events](#workers-trace-events)
6. [Log Explorer](#log-explorer)
7. [Health Checks](#health-checks)
8. [Notifications (Alerts)](#notifications-alerts)
9. [Build hooks for Web3 projects](#build-hooks-for-web3-projects)
10. [Gaps and contradictions](#gaps-and-contradictions)

## Scope and source pages

Products covered, with mirrored page counts under `raw/docs/` as of 2026-10-05:

| Product | Docs root | Pages mirrored | Sidebar location |
| --- | --- | --- | --- |
| Cloudflare Observability | https://developers.cloudflare.com/observability/ | 14 | Manage & Observe > Observe |
| Analytics (incl. GraphQL API, SQL API, Workers Analytics Engine, Network Analytics) | https://developers.cloudflare.com/analytics/ | 117 | Manage & Observe > Observe |
| Web Analytics | https://developers.cloudflare.com/web-analytics/ | 17 | Manage & Observe > Observe |
| Logs (Logpush, Instant Logs, Logpull, Logs Engine) | https://developers.cloudflare.com/logs/ | 110 | Manage & Observe > Observe |
| Log Explorer | https://developers.cloudflare.com/log-explorer/ | 9 | Manage & Observe > Observe |
| Health Checks | https://developers.cloudflare.com/health-checks/ | 8 | Manage & Observe > Observe |
| Notifications (Alerts) | https://developers.cloudflare.com/notifications/ | 10 | Not in sidebar; listed under Core platform in `raw/docs/llms.txt` |

Workers-specific observability (Workers Logs, Workers Traces, Workers Issues, tail Workers) lives under `/workers/observability/` and is covered with Workers in `build/01-compute.md`; this file only touches it where the Observability umbrella pages and pricing do.
Every page in each product's `llms.txt` was title-skimmed; overview, get-started, concepts, limits, pricing and availability pages were read in full.

## Cloudflare Observability

### What it is

Cloudflare Observability is the umbrella product at https://developers.cloudflare.com/observability/ (dashboard section **Observability**) that groups logs, traces, Workers Issues, analytics, alerts, telemetry export and custom dashboards.
The landing page routes to: Investigate logs, Trace a request, Monitor errors (Workers Issues), Analyze trends (Analytics), Create alerts (Notifications), Export telemetry, and Build dashboards (Custom dashboards).
Source: https://developers.cloudflare.com/observability/ (updated 2026-10-02).

### Logs view

The Observability **Logs** view queries structured events from supported products, filters by time and field values, and charts or inspects matching events.
Use cases listed: inspect HTTP requests and security actions, debug Workers and Containers, audit R2 bucket access, investigate AI Gateway errors, latency, token usage and costs, and query Zero Trust and network events.
You can query with a filter query language or with SQL against the selected dataset, and filter on a Ray ID to inspect one request.
Chart types include Stat, Percentage, Timeseries, Bar, Stacked Area, Categorical/Horizontal/Vertical Bar, Doughnut, Top List, Choropleth Country Map, Proportional Symbol Map, Sankey Diagram and Table, with intervals from one minute to one day, plain-language chart creation, and anomaly highlighting.
Charts can be added to a custom dashboard.
Source: https://developers.cloudflare.com/observability/logs/.

Supported datasets (https://developers.cloudflare.com/observability/logs/datasets/), as of 2026-10-05:

| Dataset group | Identifiers | Enablement | Default retention |
| --- | --- | --- | --- |
| Developer platform | `workers` (4.84 KB avg event), `containers` (1.88 KB), `r2` data access logs (1.55 KB), `ai-gateway` (2 KB), `real-time-issues` (Workers Issues, 2.64 KB) | On the Worker, bucket or gateway | 7 days |
| Unsampled security datasets (formerly Log Explorer) | `http_requests` (1.56 KB), `firewall_events` (1.36 KB), `dns_logs` (199 B), `nel_reports`, `page_shield_events`, `spectrum_events`, `zaraz_events` (7.30 KB), `access_requests`, `audit_logs`, `audit_logs_v2`, `biso_user_actions`, `casb_findings`, `dex_application_tests`, `dex_device_state_events`, `device_posture_results`, `dns_firewall_logs`, `email_security_alerts`, `gateway_dns`, `gateway_http`, `gateway_network`, `ipsec_logs`, `magic_bgp_logs`, `magic_ids_detections`, `network_analytics_logs`, `sinkhole_http_logs`, `warp_toggle_changes`, `zero_trust_network_sessions` | On the account, through Log Explorer dataset management | 30 days |

Datasets enabled through Log Explorer appear in Logs once the account has Log Explorer and that dataset turned on.

### Traces (Cloudflare Traces)

Cloudflare Traces record traces from real production traffic on a domain, with spans for Rules, request routing, Cache, Workers and origin connections.
They answer questions such as which security rule blocked or challenged a request, whether a Transform Rule rewrote the URL, which Page Rules, Snippets or Workers handled the request, whether the response came from cache, and whether behavior was isolated to one Cloudflare location.
Tracing is enabled per domain.
Cloudflare Trace (https://developers.cloudflare.com/rules/trace-request/) is a different tool that simulates how configuration would handle a request and does not show production traffic.
Source: https://developers.cloudflare.com/observability/traces/.

Configuration per domain (https://developers.cloudflare.com/observability/traces/configuration/):

- **Head sampling**: a default sample rate in percent.
- **Trace rules**: override the sample rate for requests matching a Rules-language expression; first match wins, rules can be saved as drafts or deployed.
- **Persist to Cloudflare**: stores traces for the dashboard; from 2026-12-01 persisted traces count toward Observability ingestion and storage.
- **Export destinations**: send traces to account-level OpenTelemetry destinations; persist and export can both be on.
- **Trace context propagation**: W3C Trace Context; incoming context defaults to *Reject*; Cloudflare does not verify incoming context, so accepted context should be treated as untrusted; **Forward to origin** adds context to origin requests so an instrumented origin can join the trace.

Span reference (https://developers.cloudflare.com/observability/traces/spans/): `cloudflare_request` (root), `response`, `workers_routing`, `page_rules`, `cache` (includes the full response body, not just the lookup), `dynamic` (uncached fetch including connection setup and full body), `upstream` (Tiered Cache fetch from another Cloudflare location), plus ruleset phase spans such as `http_request_firewall_custom`, `http_request_firewall_managed`, `http_request_cache_settings`, `http_request_origin`, `http_request_transform`, `http_request_snippets`, `http_response_compression`.
Workers runtime spans appear only when Workers tracing is enabled.
No beta or GA label for Cloudflare Traces appears in the mirrored pages as of 2026-10-05.

### Export (OpenTelemetry and Logpush)

Logpush exports logs generated by Cloudflare products; OpenTelemetry export sends Cloudflare Traces, Workers Traces and Workers Logs to OTLP destinations (https://developers.cloudflare.com/observability/export/).
OTLP destinations are created at the account level under **Observability** > **Destinations** with a name, type (Traces or Logs), OTLP endpoint and custom headers.
Cloudflare does not support the binary protobuf OTLP encoding.
Creating a destination does not start export: Workers need OpenTelemetry export configured and redeployed, and Cloudflare Traces need the destination added in the domain's trace settings.
Destination status shows "Last: n minutes ago", "Never run" or "Error".
Documented endpoints (https://developers.cloudflare.com/observability/export/opentelemetry/): Honeycomb, Grafana Cloud, Firetiger, Axiom, Sentry, Sematext, PostHog (logs only), Datadog, New Relic, Splunk Observability (traces only), Splunk Platform and SigNoz.
Guides exist for Axiom, Grafana Cloud, Honeycomb, PostHog and Sentry under https://developers.cloudflare.com/observability/export/opentelemetry/.

### Observability pricing (from 2026-12-01)

Source: https://developers.cloudflare.com/observability/pricing/ (updated 2026-10-02).
Beginning 2026-12-01 all Cloudflare logs and traces use one pricing model, and queries, dashboards, alerts and analytics carry no extra charge.
Included in the pooled model: Cloudflare Traces, Workers Logs, Workers Traces, Containers logs, R2 Data Access Logs, AI Gateway logs and Issues.

| Plan | Included ingestion | Included storage | Additional ingestion | Additional storage |
| --- | --- | --- | --- | --- |
| Free | 0.5 GB per day | Seven-day retention included | Not available | Not separately metered |
| Paid | 50 GB per billing cycle | 12 GB-month per billing cycle | $0.25 per GB | $0.10 per GB-month |

- Free stops ingesting at the daily limit and resumes at 00:00 UTC; stored data stays queryable for seven days.
- Ingestion is measured pre-compression and includes the event body, default enriched attributes and custom attributes; dropped events do not count; sampling before storage reduces both meters.
- Storage is GB-month = sum of each day's maximum queryable GB / 30.
- Ingestion and storage are separate meters and allowances do not roll over.
- Default retention in the pooled allowance is seven days; configurable 30, 90 and 365-day retention is "planned".
- Existing Workers Observability customers on Free, Pro and Business move automatically on 2026-12-01; Enterprise moves at contract renewal.
- Worked example on the page: 75 GB ingestion and 20 GB-month storage on Paid costs $6.25 + $0.80 = $7.05.
- Unsampled security datasets (legacy Log Explorer) cost $1 per GB ingested with 30-day retention and no query charge, and do not consume the pooled allowance.

## Analytics

Docs root: https://developers.cloudflare.com/analytics/ (117 pages).

### Types of analytics and dashboards

Source: https://developers.cloudflare.com/analytics/types-of-analytics/.

- **Account Analytics (beta)**: traffic overview for all domains in the account, under **Observability** > **Analytics** > **Account analytics**.
- **Network Analytics**: L3/L4 traffic and DDoS visibility (see below).
- **Web Analytics**: privacy-first RUM analytics, formerly Browser Insights (see below).
- **Carbon Impact Report**: carbon savings report.
- **Domain analytics** under the zone's **Analytics**: HTTP Traffic, Security, Performance, Edge Reachability (NEL, Enterprise), Workers, Logs and Instant Logs.
- **Product analytics**: Bot Analytics, Cache Analytics, DNS Analytics, Load Balancing Analytics, Security Events and Security Analytics.
- The GraphQL Analytics API "replaces and expands on the previous Zone Analytics API".

How data is captured (https://developers.cloudflare.com/analytics/faq/about-analytics/): metrics reflect proxied (orange-clouded) traffic only; unproxied records are not counted except DNS metrics when Cloudflare is authoritative; CNAME (partial) setups get no DNS metrics; country comes from the request IP.
Cloudflare counts a unique IP as a visit, so its visitor numbers are usually higher than JavaScript-based tools such as Google Analytics.
The Overview page counts all traffic including subrequests, while **Analytics** > **Traffic** filters to `requestSource = eyeball`, so the two can differ.
Large traffic from ASN 13335 is usually Workers subrequests, WARP, iCloud Private Relay, Privacy Proxy or Health Checks rather than a DDoS (https://developers.cloudflare.com/analytics/faq/other-faqs/).

### Sampling (ABR)

Source: https://developers.cloudflare.com/analytics/sampling/ and https://developers.cloudflare.com/analytics/graphql-api/sampling/.
Cloudflare uses Adaptive Bit Rate (ABR) sampling: data is stored at 100%, 10% and 1% resolutions and each query reads the resolution that fits its complexity, row count, time range and current load.
Aggregates (totals, averages, percentiles) are extrapolated from the sample, and very rare events may be missed.
Nodes with `Adaptive` in the name are adaptively sampled; the dashboard shows an icon with the sampled percentage.
Fixed-rate exceptions: `firewallRulePreviewGroups` at 1%, and Network Analytics v1 `ipFlows*` nodes at 0.012% (1 of every 8,192 packets).
Enterprise customers get raw unsampled data via Cloudflare Logs.
The same query can return slightly different numbers between runs; the FAQ advises shorter windows (daily or weekly), `Groups` nodes, explicit `orderBy`, and confidence intervals (https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/).
GraphQL confidence intervals: `confidence(level: 0.95) { count { estimate lower upper sampleSize } }` on `sum` and `count` fields of adaptive datasets only (https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/).

### Account and zone analytics

- **Zone analytics** (https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/): tabs Traffic, Performance, Security, Cache, Origin, DNS and Visitors share one time range and filter set; every plan can view at least the last 30 days, with longer periods depending on plan; paths and URIs are case sensitive.
- Free plan HTTP Traffic shows Requests, Bandwidth and Unique Visitors with a country map.
- Pro, Business and Enterprise get "privacy-first HTTP Traffic Analytics" built from edge logs: Requests, Data Transfer, Page views (successful HTML responses), Visits (page views whose referer differs from the host) and API Requests, filterable by cache status, data center, source ASN, country, device type, source IP, referer host, host, method, HTTP version, path, query string, content type, edge and origin status, security action and source, browser, OS, user agent and X-Requested-With.
- JA3 and JA4 fingerprint filters are limited to Enterprise Bot Management customers.
- Workers subrequests are excluded from zone traffic analytics and shown under the Workers tab; requests served by a Worker always show as cached (https://developers.cloudflare.com/analytics/account-and-zone-analytics/analytics-with-workers/).
- **Status codes by data center** are Enterprise only; edge-generated blank 502/503/504 pages are not reported (https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/).
- **Threat types** and **Total threats stopped** explain the security panels; the legacy threat score "is always 0" now (https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/).
- **Security reports**: monthly Application Security reports for Enterprise zones, with industry benchmarks and an API under `/accounts/{account_id}/reporting/...`; status is closed beta for Enterprise as of 2026-10-05 (https://developers.cloudflare.com/analytics/account-and-zone-analytics/app-security-reports/).
- Retention change: since 2026-10-02 adaptive datasets (HTTP requests, security events, DNS analytics) retain at least 31 days on every plan and a single query can span 30 days; before that Free and Pro saw 24 hours to 8 days depending on dataset (https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/).
- Free plan metrics can be delayed 24 hours for newly signed-up domains (https://developers.cloudflare.com/analytics/faq/about-analytics/).

### Custom dashboards

Source: https://developers.cloudflare.com/analytics/custom-dashboards/.
Account-owned dashboards built from three source types: over 100 GraphQL datasets, Workers Observability logs and traces, and Log Explorer datasets (Log Explorer customers only, raw and unsampled).
Charts can be created from natural-language prompts or configured manually (dataset, metric, dimensions, filters), with Timeseries, Bar, Donut, Map, Stat, Percentage and Top N types and dashboard-wide filters.
Templates: Bot monitoring, API Security, Account takeover, API Performance, Performance monitoring.
Availability as of 2026-10-05: all customers, "up to 100 dashboards" per account (see contradictions).
Workers Observability datasets follow the underlying Workers Observability retention.

### Network Analytics

Source: https://developers.cloudflare.com/analytics/network-analytics/.
Network Analytics v2 gives near-real-time L3/L4 packet and bit-level visibility and DDoS insight, the same data as the GraphQL Network Analytics nodes.
Requirements (as listed on the page): an Enterprise plan, Magic Transit or Spectrum, and Cloudflare WAN (see contradictions for the BYOIP wording elsewhere).
Retention is 16 weeks, and data older than eight weeks may have lower resolution on narrow time frames.
Sampling varies by mitigation service: `dosd` 1/100 to 1/10,000 packets, Network Firewall 1/100 to 1/1,000,000, `flowtrackd` 1/10,000; main nodes sample 1/10,000 packets.
Main nodes: `spectrumNetworkAnalyticsAdaptiveGroups` and `magicTransitNetworkAnalyticsAdaptiveGroups`; attack nodes include `dosdAttackAnalyticsGroups`, `dosdNetworkAnalyticsAdaptiveGroups`, `advancedTcpProtectionNetworkAnalyticsAdaptiveGroups`, `advancedDnsProtectionNetworkAnalyticsAdaptiveGroups` and `magicFirewallNetworkAnalyticsAdaptiveGroups` (https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/).
Network Analytics v1 is deprecated; it used 1-minute, 1-hour and 1-day roll-ups with 30-day, 6-month and 1-year retention.
Network Analytics GraphQL queries require an `accountTag` filter.
Users with only the Analytics role see IDs but not tunnel names, prefix names, Network Firewall rules, DDoS managed rulesets or override names.

### GraphQL Analytics API

Docs: https://developers.cloudflare.com/analytics/graphql-api/.

**Endpoint and request shape.**
A single endpoint, `https://api.cloudflare.com/client/v4/graphql`, takes `POST` requests with a JSON body `{"query": "...", "variables": {}}`, where the query must be a single-line string.
Queries start at `viewer`, select `zones` or `accounts` scope, then one or more dataset nodes and their fields.
A `200` response can still carry errors in the `errors` array (https://developers.cloudflare.com/analytics/graphql-api/errors/).
If one dataset in a multi-dataset request fails, the whole query is terminated.
GraphQL is not a billing measure: it includes all measurable traffic, while billable traffic excludes things like DDoS traffic.

**Authentication** (https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/): API tokens are recommended, created as a custom token with *Account* > *Account Analytics* > *Read* plus zone resources, optional client IP filtering and TTL; header `Authorization: Bearer <token>`.
Legacy API key auth uses `X-AUTH-EMAIL` and `X-AUTH-KEY` with the Global API Key.
A `403` usually means the token lacks **Analytics: Read** for the zone or account.

**Datasets.**
The API exposes "more than 70 datasets" per the limits and settings pages, while the custom dashboards page says "over 100 datasets" (see contradictions).
Naming: `Adaptive` suffix means adaptive sampling, `Groups` suffix means aggregated data returned as group objects with `count`, `sum`, `avg`, `uniq` and `dimensions`, and no suffix means raw rows (https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/).
`workersInvocationsAdaptive` (beta) is an exception to the naming rule.
Core nodes named in the docs include `httpRequestsAdaptiveGroups`, `httpRequests1mGroups`, `httpRequests1hGroups`, `firewallEventsAdaptive`, `firewallEventsAdaptiveGroups`, `loadBalancingRequestsAdaptive(Groups)`, `workersInvocationsAdaptive`, `logpushHealthAdaptiveGroups`, `mnmFlowDataAdaptiveGroups`, the Network Analytics nodes above, and four `privacyProxy*AdaptiveGroups` nodes added 2026-04-15.
`httpRequests1mByColoGroups` and `httpRequests1dByColoGroups` are deprecated in favor of `httpRequestsAdaptiveGroups` (https://developers.cloudflare.com/analytics/graphql-api/migration-guides/graphql-api-analytics/).
The REST Zone Analytics API and its colos endpoint are described as "deprecated (and soon to be sunset)" with migration guides (https://developers.cloudflare.com/analytics/graphql-api/migration-guides/zone-analytics-colos/).
Introspection shows every node and field with descriptions, beta flags and deprecation status (https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/).

**Filtering, sorting, pagination** (https://developers.cloudflare.com/analytics/graphql-api/features/filtering/):

- Zone filter forms: `zoneTag`, `zoneTag_gt`, `zoneTag_in`; compound zone filters are not supported; the account filter is analogous and you cannot query multiple accounts at once.
- Table filters support implicit `AND`, explicit `OR`, scalar operators `gt`, `lt`, `geq`, `leq`, `neq`, `in`, string `like` with `%`, and array operators `has`, `hasall`, `hasany`.
- Time filters match on event start time.
- Add `requestSource: "eyeball"` to exclude Cloudflare-generated traffic such as cache purge, health checks and Workers subrequests.
- Subqueries are not supported.
- Pagination has no cursors: use `limit`, `orderBy` and a filter that excludes the last row of the previous page (https://developers.cloudflare.com/analytics/graphql-api/features/pagination/).

**Limits** (https://developers.cloudflare.com/analytics/graphql-api/limits/), as of 2026-10-05:

| Layer | Limit |
| --- | --- |
| Global | Up to 10 zones per zone-scoped query; exactly 1 account per account-scoped query; total queries per request = scopes x nodes |
| User (default) | 300 GraphQL queries per 5-minute window per user or token (at least 1 per second, or a burst of 300 then wait), on top of general Cloudflare API rate limits |
| Account-based (opt-in) | Header `X-Rate-Limit-Type: account-based`; 1 request per second (300 per 5 minutes) per account and per zone; Enterprise defaults 15 rps per account and 10 rps per zone; increases on request |
| Node | Per dataset: `notOlderThan` (how far back), `maxDuration` (widest time range), `maxNumberOfFields`, `maxPageSize`; tied to the plan of the requested zone or account |

Under account-based limits, a list or range of zones at the `viewer` level must be nested inside one `accounts` block; throttled requests return `extensions.code = "budget"` and a five-minute retry hint (https://developers.cloudflare.com/analytics/graphql-api/account-based-rate-limiting/).
Adaptive datasets retain at least 31 days on every plan; aggregated datasets like `httpRequests1hGroups` keep per-plan limits.
Query a dataset's exact limits with the `settings` node, for example `zones { settings { firewallEventsAdaptive { enabled maxDuration maxNumberOfFields maxPageSize notOlderThan availableFields } } }`; the documented sample response shows `maxDuration` 259200 s (3 days), `maxNumberOfFields` 30, `maxPageSize` 10000 and `notOlderThan` 2678400 s (31 days) (https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/).
Error classes: `503` service unavailable or too many queries in progress; `400` dataset limits exceeded (too old, too many fields, limit too large, time range too large) or parse errors; `429` "rate limiter budget depleted", too many nodes/zones/accounts, or excessive resources; `401` and `403` auth.
Workers metrics via `workersInvocationsAdaptive` can query up to one month of data for dates up to three months ago (https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/).
When Customer Metadata Boundary is enabled, querying from the wrong region can show a "data unavailable" message (https://developers.cloudflare.com/analytics/graphql-api/getting-started/).
Tutorials cover per-hostname HTTP analytics, Access logins, Containers metrics, Email Routing, Firewall Events, Magic Transit health checks and tunnel bandwidth, Network Firewall samples and IDS, Workers metrics, and capturing dashboard queries with Chrome DevTools.

### Analytics SQL API

Docs: https://developers.cloudflare.com/analytics/sql-api/ (all pages updated 2026-10-02; no beta or GA label stated).
The SQL API queries Cloudflare analytics and observability datasets with a deliberately limited SQL dialect at `https://api.cloudflare.com/client/v4/analytics/sql` (`GET` or `POST`).
Every query needs an account or zone scope, a lower time bound, and one schema-qualified dataset.
Dataset prefixes: `events.` (unique events, often sampled; e.g. `events.httpRequests`), `states.` (point-in-time system state, e.g. `states.d1Storage`, with per-dataset `valid_aggregations`), `logs.` (log entries, typically unsampled, includes Log Explorer datasets and `logs.workersLogs`) (https://developers.cloudflare.com/analytics/sql-api/datasets/).
Sample weights are applied automatically to `COUNT`, `SUM` and `AVG` on sampled datasets.
Workers Analytics Engine datasets are queryable as `events.analyticsEngine.<DATASET>` (account scope only).
Discovery: `GET /client/v4/analytics/sql/introspection?account_tag=...` with optional `dataset_name`, `include_columns`, `include_custom_attributes` (scans the last seven days, capped at 1,000 silently), `include_wae`, `include_lex`; the catalog is dynamic, so do not hard-code dataset names.
CLI: `cf sql query '<SQL>' --scope-account <tag> --time-since <ts>` and `cf sql datasets --account-tag <tag>` (https://developers.cloudflare.com/analytics/sql-api/get-started/).
Permissions: **Account Analytics Read** for account scope; a query with `zoneTag` needs **Zone Analytics Read** on every named zone or Account Analytics Read on the owner.
JSON request fields: `query`, `params` (positional `$1` or named `$name`), `scope` (exactly one of `accountTag` or `zoneTag`), `time_range` (`start` required, `end` optional, both inclusive); tenancy or time in both SQL and request fields returns `422` (https://developers.cloudflare.com/analytics/sql-api/query-api/).
Formats: default JSON with `data`, `rows`, `statistics`; `FORMAT JSON`, `JSONEachRow`, `TabSeparated`/`TSV`.

Limits (https://developers.cloudflare.com/analytics/sql-api/limits/), as of 2026-10-05:

| Limit | Value |
| --- | --- |
| Statements per request | 1 |
| Statement length | 10 KiB |
| Parser nesting depth | 10 |
| Datasets per statement | 1 |
| Accounts per statement | 1 |
| Time constraint | Lower timestamp bound required |
| `ORDER BY` | Requires `LIMIT`, except Workers Analytics Engine datasets |
| Operational | Rate, concurrency, queue, execution-time and resource limits, adjustable by Cloudflare; errors `429`, `507`, `503`, honor `Retry-After` |

Workers binding (https://developers.cloudflare.com/analytics/sql-api/workers-binding/): add `"analytics": { "binding": "ANALYTICS_SQL" }` (Wrangler 4.145.0 or later) and call `env.ANALYTICS_SQL.query({ query, params })`.
The binding supplies the Worker's account scope (do not add `accountTag`), takes no `time_range` or `FORMAT`, does not support Log Explorer datasets, and throws errors with a boolean `retryable`.
The SQL API also powers Custom Alerts (see Notifications).

### Workers Analytics Engine

Docs: https://developers.cloudflare.com/analytics/analytics-engine/.
Workers Analytics Engine (WAE) stores unlimited-cardinality time-series data written from Workers and queried with SQL; uses include per-customer analytics, usage-based billing and instrumenting hot code paths.
Configure a binding with `analytics_engine_datasets: [{ binding, dataset }]`; the dataset is created on first write.
Write with `env.BINDING.writeDataPoint({ blobs: [...], doubles: [...], indexes: [one] })`; it is non-blocking and need not be awaited.
Blobs are string dimensions, doubles are numeric values, and the single index is the sampling key.
Query via the WAE SQL API at `https://api.cloudflare.com/client/v4/accounts/<account_id>/analytics_engine/sql` with a token holding Account Analytics Read, via the GraphQL API, from Grafana, from a Worker with `fetch`, or via the Analytics SQL API as `events.analyticsEngine.<name>`.
Table columns: `dataset`, `timestamp`, `_sample_interval`, `index1`, `blob1..blob20`, `double1..double20`.
Sampling is equitable per index at write time plus ABR at read time; always weight with `_sample_interval` (`SUM(_sample_interval)` for counts, `quantileExactWeighted` for quantiles) (https://developers.cloudflare.com/analytics/analytics-engine/sampling/).
The FAQ says roughly 100 data points per second per index value is where sampling becomes noticeable for CDN-like workloads, and that a UUID per row as index is not recommended (https://developers.cloudflare.com/analytics/faq/wae-faqs/).

Limits (https://developers.cloudflare.com/analytics/analytics-engine/limits/), as of 2026-10-05:

- Up to 20 blobs, 20 doubles and 1 index per `writeDataPoint` call.
- Blobs total at most 16 KB per data point.
- Index at most 96 bytes.
- Up to 250 data points per Worker invocation.
- Data retained for three months.

Pricing (https://developers.cloudflare.com/analytics/analytics-engine/pricing/), as of 2026-10-05:

| Plan | Data points written | Read queries |
| --- | --- | --- |
| Workers Paid | 10 million per month included, then $0.25 per million | 1 million per month included, then $1.00 per million |
| Workers Free | 100,000 per day | 10,000 per day |

The pricing page says "Currently, you will not be billed for your use of Workers Analytics Engine" and that billing starts "in the coming months" (page updated 2026-04-23).

### Analytics integrations

Source: https://developers.cloudflare.com/analytics/analytics-integrations/.
The overview says integrations are for Enterprise customers and mostly built on Logpush to S3 or GCS, covering Datadog, Prometheus, Graylog, New Relic, Splunk and Microsoft Sentinel.
The Prometheus integration is different: the open-source Cloudflare Prometheus Exporter runs as a Worker with Durable Objects, is built on the GraphQL and REST APIs, exports 90+ metrics, and is available on all plans with limited metrics on Free (https://developers.cloudflare.com/analytics/analytics-integrations/prometheus/).
An Azure Functions-based Sentinel connector deprecation was announced 2026-08-26 in the Logs changelog.

## Web Analytics

Docs: https://developers.cloudflare.com/web-analytics/ (17 pages).

### What it is

Cloudflare Web Analytics is free, privacy-first real-user monitoring (RUM) that needs neither Cloudflare DNS nor the proxy, "Available on all plans".
A JavaScript beacon (`https://static.cloudflareinsights.com/beacon.min.js`) uses the browser Performance API and does not use cookies, `localStorage`, or fingerprinting by IP or user agent, and Cloudflare says it does not collect visitors' personal data (https://developers.cloudflare.com/web-analytics/about/, https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/).
Beacons post to `https://<your-domain>/cdn-cgi/rum` for proxied sites or `https://cloudflareinsights.com/cdn-cgi/rum` otherwise; the endpoint only accepts `POST` and custom integrations directly against it are not supported.

### Key concepts and metrics

- Metrics: Visits, Page views, Page load time, and Core Web Vitals (LCP, INP, CLS) with a debug view of the top five offending elements and P50/P75/P90/P99 (https://developers.cloudflare.com/web-analytics/data-metrics/).
- CLS is only supported in Chromium browsers.
- Page load breakdown: DNS, TCP, Request, Response, Processing, Load Event, First Paint, First Contentful Paint.
- Dimensions: Country, Host, Path, Referer (referer path via GraphQL only), Device type, Browser, OS, Site, Exclude Bots, Navigation type (including Soft Navigation and Routing APIs for SPAs).
- SPA tracking uses the Soft Navigations API, then the Navigation API, then History API patching; disable with `"spa": false` (https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/).
- No UTM parameters (query strings are not logged) and no custom events, as of 2026-10-05 (https://developers.cloudflare.com/web-analytics/faq/).

### Configuration

Source: https://developers.cloudflare.com/web-analytics/get-started/.

- **Not proxied**: add a hostname, copy the snippet, paste before `</body>`.
- **Proxied**: pick the hostname and automatic injection is on by default, with options "Enable, excluding visitor data in the EU", "Enable with JS Snippet installation" (manual) or "Disable".
- **Pages projects**: one-click enable under the project's **Metrics**.
- Automatic injection fails if the origin sends `Cache-Control: public, no-transform` or invalid HTML.
- Hostnames match by postfix, so `example.com` also accepts `www.example.com` and `fooexample.com`.
- CSP needs `script-src https://static.cloudflareinsights.com/beacon.min.js` and `connect-src 'self'` (automatic) or `connect-src cloudflareinsights.com` (manual).
- SRI is added automatically only for automatic injection; manual embeds cannot be version-pinned.
- Google Tag Manager users pass the token in the script URL query string.
- Rules (include or exclude hostnames and paths) only work for proxied sites, and Configuration Rules override them (https://developers.cloudflare.com/web-analytics/configuration-options/rules/).
- Notifications: a weekly summary email on all plans (https://developers.cloudflare.com/web-analytics/get-started/notifications/).
- The beacon is blocked by ad-blockers; edge analytics on proxied zones are not.

### Limits, retention, sampling

Source: https://developers.cloudflare.com/web-analytics/limits/ and FAQ, as of 2026-10-05.

| Item | Value |
| --- | --- |
| Sites not proxied through Cloudflare | 10 per account |
| Sites proxied through Cloudflare | No limit |
| Dashboard aggregate view | 1,000 websites in parallel |
| Rules | Free 0, Pro 5, Business 20, Enterprise 100 |
| Data access window | Previous six months |
| Raw data | Unsampled for 7 days, then aggregated to about 10% |
| Query-time sampling | Between 0.0001% and 100%, exposed as `sampleInterval` in GraphQL |

Status: generally available; the beacon changelog shows frequent 2026 releases, latest 2026-10-05 (web-vitals 6.2.2, `__cfBeacon` override) (https://developers.cloudflare.com/web-analytics/changelog/).

## Logs

Docs: https://developers.cloudflare.com/logs/ (110 pages).
Features: Logpush, Instant Logs and Logpull (legacy), with Log Explorer and Audit Logs as related products.
Requests are logged only after they reach the proxy, so TCP or TLS handshake failures are not logged (https://developers.cloudflare.com/logs/faq/general-faq/).
Cloudflare Logs only output JSON-family formats; other formats are not offered.

### Logpush

Source: https://developers.cloudflare.com/logs/logpush/ (updated 2026-09-30).
Logpush pushes logs in batches as soon as possible with no minimum batch size, sometimes more than once per minute; push frequency cannot be adjusted, only batch size.
Logpush cannot backfill: if a job is disabled or failing, logs from that period are lost permanently.
Logpush offers no storage or search.
Limit: 4 Logpush jobs per zone (`exceeded max jobs allowed`).
Since May 2022 multiple jobs may write to the same destination.
Volume estimate for `http_requests`: about 100 to 250 bytes per request compressed, so 1M requests/day is about 100 to 250 MB/day; a separate table on the same page gives 250 to 500 MB/day for 1M req/day (see contradictions).
Configuration changes (destination or fields) take about 10 to 15 minutes to propagate (https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/).

### Logpush datasets

Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/ and `raw/docs/logs/llms.txt`, as of 2026-10-05.

**Zone-scoped**: `http_requests`, `firewall_events`, `dns_logs`, `nel_reports`, `page_shield_events`, `spectrum_events`, `websocket_analytics`, `zaraz_events`, `account_abuse_protection_events`.

**Account-scoped**: `access_requests`, `account_abuse_protection_events`, `audit_logs`, `audit_logs_v2`, `biso_user_actions`, `casb_findings`, `device_posture_results`, `dex_application_tests`, `dex_device_state_events`, `dlp_forensic_copies`, `dns_firewall_logs`, `email_security_alerts`, `email_security_post_delivery_events`, `firewall_events` (account-scoped, added 2026-06-30), `gateway_dns`, `gateway_http`, `gateway_network`, `ipsec_logs`, `magic_bgp_logs`, `magic_ids_detections`, `mcp_portal_logs`, `mnm_flow_logs`, `network_analytics_logs`, `sinkhole_http_logs`, `ssh_logs`, `turnstile_events`, `warp_config_changes`, `warp_toggle_changes`, `websocket_analytics`, `workers_trace_events`, `zero_trust_network_sessions`.

Field lists come from `GET /client/v4/zones/{zone_id}/logpush/datasets/<DATASET>/fields` (or `/accounts/...`).
Field availability depends on plan; zone `http_requests` is the only dataset also available through Logpull; custom fields only work in Logpush.
`http_requests` has 124 documented fields, including `ClientIP`, `ClientASN`, `ClientCountry`, `ClientRequestHost`, `ClientRequestPath`, `ClientRequestURI`, `ClientRequestMethod`, `ClientRequestUserAgent`, `ClientRequestSource`, `ClientTCPRTTMs`, `ClientTLSKeyExchangeGroup` (post-quantum visibility, 2026-08-20), `BotScore`, `BotTags`, `BotDetectionIDs`, `VerifiedBotCategory`, `JA3Hash`, `JA4`, `JA4Signals`, `JSDetectionPassed`, `CacheCacheStatus`, `EdgeResponseStatus`, `EdgeTimeToFirstByteMs`, `OriginResponseStatus`, `OriginResponseDurationMs`, `SecurityAction`, `SecurityActions`, `SecurityRuleID`, `WAFAttackScore`, `LeakedCredentialCheckResult`, `FraudDetectionIDs`, `WorkerSubrequest`, `ParentRayID`, `Subrequests`, `RayID`, and `RequestHeaders`/`ResponseHeaders`/`Cookies` for custom fields (https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/).
Deprecated fields stay present but may become empty; the `FirewallForAI*` fields are deprecated in favor of `AISecurity*`.
Data Localization: CMB support differs by dataset (https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/).

### Logpush destinations

Source: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/.
Destinations: Cloudflare R2, Basin Pipelines (added 2026-04-20; can write Parquet or Iceberg tables in Basin Catalog), HTTP endpoints, Amazon S3, S3-compatible endpoints, Datadog, Elastic, Google Cloud Storage, Google BigQuery (added 2026-04-02), Microsoft Azure Blob Storage, New Relic, SentinelOne (added 2025-12-11), Splunk HEC, Sumo Logic, Amazon Kinesis, IBM QRadar, IBM Cloud Logs, other providers and third-party integrations.
`destination_conf` schemes: `r2`, `gs`, `s3`, `sumo`, `https`, `azure`, `splunk`, `sentinelone`, `datadog`.
Formats: `r2://<BUCKET_PATH>?account-id=...&access-key-id=...&secret-access-key=...`; `s3://bucket/[dir]?region=<REGION>[&sse=AES256]`; `datadog://<URL>?header_DD-API-KEY=...&ddsource=cloudflare&service=...&host=...&ddtags=...`; New Relic uses `https://log-api.newrelic.com/log/v1?Api-Key=...&format=cloudflare` (https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/).
`{DATE}` in R2, S3, GCS and Azure paths becomes `YYYYMMDD` daily folders.
Ownership challenge: storage destinations require writing a challenge file and passing its token when creating a job; HTTP and Datadog destinations do not.
R2 offers an automatic setup in which Cloudflare creates the bucket, or a custom setup with your own R2 API token (https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/).
HTTP destination (https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/http/): HTTPS with a trusted certificate, accepts `POST`; you authenticate pushes yourself, e.g. with `header_Authorization=...` URL parameters, which become request headers; `max_upload_bytes` 5 MB to 1 GB and `max_upload_records` 1,000 to 1,000,000; the validation upload is a gzipped `test.txt.gz` containing `{"content":"tests"}`.
Datadog limits are hard-coded: 5 MB uncompressed per payload, 1 MB per log, 1,000 entries per array; Logpush does not drop unsent logs but ingestion can lag after spikes.
Destinations must allowlist Cloudflare IPs; a fixed egress IP requires Smart Shield Advanced with Dedicated CDN Egress IPs and proxying Logpush through a zone, secured with a secret `header_` plus a WAF rule, optionally ASN filtering on 13335, 132892 and 202623, or Access Service Tokens (https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/).

### Job configuration, filters, output options, Transformers

- **API**: create, get, list, update and delete jobs under `/zones/{zone_id}/logpush/jobs` or `/accounts/{account_id}/logpush/jobs`; validate destination, ownership and options endpoints exist; all Logpush API calls need **Logs: Write** (https://developers.cloudflare.com/logs/logpush/permissions/).
- Zone datasets need a zone-scoped token and account datasets an account-scoped token.
- Zero Trust datasets need both Logs Edit and Zero Trust: PII Read.
- **Filters** (https://developers.cloudflare.com/logs/logpush/logpush-job/filters/): JSON `{"where":{"and":[{"key":"ClientRequestPath","operator":"startsWith","value":"/rpc"}]}}` with operators `eq`, `!eq`, `lt`, `leq`, `gt`, `geq`, `startsWith`, `endsWith`, `!startsWith`, `!endsWith`, `contains`, `!contains`, `in`, `!in`; nested `and`/`or`; roughly 30 operators and 1,000 bytes maximum; filters include matching logs rather than exclude them; objects and `array[object]` cannot be filtered.
- **DDoS attack traffic**: `filter_attack_traffic: true` excludes identified DDoS traffic for `http_requests`, `firewall_events` and `network_analytics_logs` (changelog 2026-09-18).
- **Sampling**: `sample_rate` 0.0 (exclusive) to 1.0, applied on top of filtering and on top of any upstream `SampleInterval`.
- **Output options** (https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/): `output_options` replaces `logpull_options`, with `field_names` (no "all fields" option), `output_type` `ndjson` (default) or `csv`, batch and record prefix/suffix/delimiter, `record_template` (restricted Go text/template), `timestamp_format` `unixnano` (API default), `unix`, `rfc3339` (dashboard default), `rfc3339ms`, `rfc3339ns`, `sample_rate`, and `CVE-2021-44228` redaction of `${`.
- A `PUT` replaces `output_options` entirely and resets omitted keys to defaults.
- **Batch size**: `max_upload_bytes`, `max_upload_records` (default 100,000), `max_upload_interval_seconds`; they shape batches, not latency, and catch-up uploads are capped at 2 minutes of data each.
- **Custom fields** (https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/): configured per zone via a `log_custom_field` rule in the `http_log_custom_fields` ruleset phase, logging request headers (raw by default), response headers (transformed by default) and cookies; up to 100 headers per field type; header names lower case; `Range` unsupported; `preserve_duplicates` for repeated headers like `set-cookie`.
- **Subrequest merging** (https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/): opt-in `merge_subrequests: true` on `http_requests` nests up to 50 Worker subrequests completing within 5 minutes into a `Subrequests` array; gradual rollout as of 2026-10-05; otherwise correlate with `ParentRayID` = parent `RayID` and `ClientRequestSource == "edgeWorkerFetch"`.
- **Transformers** (https://developers.cloudflare.com/logs/logpush/transformers/): GA as of 2026-09-30, a single SQL query per job (Basin Pipelines dialect) run on each NDJSON batch to filter, rename, redact, compute or nest fields; `FROM` must name the job's dataset; no joins, subqueries, aggregation, window functions or `ORDER BY`; 250 KB query limit and 1,000-row batch chunks; a job has either filters or a transformer, not both; a failing transformer fails the batch with no raw fallback.

### Logpush health, retries, alerts

Source: https://developers.cloudflare.com/logs/logpush/logpush-health/ (updated 2026-10-01).

- The Health tab shows up to 30 days per job: Upload Health (successful vs failed batches, uploaded vs dropped log lines, compressed and uncompressed volume) and Upload Reliability (status codes, upload duration, destination availability, retries).
- Raw metrics live in the GraphQL dataset `logpushHealthAdaptiveGroups`.
- Cloudflare error codes: `1101` ConnectionError, `1102` ConnectionTimeout, `1103` InternalLogpushError, `1104` ConfigError, `1105` DNSError, `1106` Timeout, `1107` RequestError, `1108` TransferError, `1201` FlushMaxLag (batch aged out and dropped).
- Timeouts: 5 s TCP dial, 5 s TLS handshake, 10 s no-progress watchdog, 2 min overall HTTP client timeout for HTTP-family destinations, HTTP/2 15 s ping; S3, GCS and Azure use their own client libraries.
- Retries continue until success or the buffer ages out; after 24 hours with no successful delivery the job is disabled.
- When a destination is slow, Logpush automatically increases parallel uploads.
- Alert **Failing Logpush Job Disabled** (email or webhook, at most one per job per 24 hours) is listed as "Enterprise plans" (https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/; see contradictions).

### Logpush pricing and plan availability

Source: https://developers.cloudflare.com/logs/logpush/pricing/ (updated 2026-10-02) and https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/.
Since 2026-09-30 Logpush is available on Free, Pro, Business and Enterprise; Free, Pro and Business self-serve, Enterprise works with the account team.

| Usage | Included monthly per account | Rate |
| --- | --- | --- |
| Exports to internal destinations (R2, Pipelines) | 25 GB | $0.03 per additional GB |
| Exports to external destinations (everything else) | 25 GB | $0.10 per additional GB |
| Logs transformed (Transformers input) | 1 GB | $0.04 per additional GB |

- Export usage is measured on uncompressed bytes successfully delivered; transformation on uncompressed input bytes.
- Worked example: 40 GB internal + 60 GB external + 5 GB transformed = $0.45 + $3.50 + $0.16 = $4.11.
- Destination charges (for example R2 storage and operations) are separate.
- Existing Enterprise contracts keep their pricing through renewal.
- Workers Trace Events Logpush stays on the Workers Paid plan at 10 million requests per month included, then $0.05 per million.
- OpenTelemetry destinations are not in the GB pricing and keep event-based Workers Observability pricing.
- The "Export" area of Cloudflare Observability is meant to unify Logpush and OTLP, and Cloudflare "plans to align" export pricing over time.

### Edge Log Delivery

Edge Log Delivery sends `http_requests` logs directly from the edge with lower latency, more often and in smaller batches than Logpush; the maximum batch interval is configurable from 30 seconds to five minutes (https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/).
It is created with `"kind": "edge"` on job creation only.
Plan availability is not stated on the page.

### Instant Logs

Source: https://developers.cloudflare.com/logs/instant-logs/ (updated 2026-08-14).
Instant Logs streams live `http_requests` traffic for a zone in the dashboard or over a WebSocket, with no setup.
Availability: Business and Enterprise only (not Free or Pro), as of 2026-10-05.
CLI flow: `POST /zones/$ZONE_ID/logpush/edge/jobs` with `fields`, `sample` (an integer where 10 means 10%), `filter` and `"kind": "instant-logs"`, then connect to the returned `wss://logs.cloudflare.com/instant-logs/ws/sessions/<id>` (for example with `websocat`, piping into Angle Grinder).
High-volume zones are server-side sampled, indicated by `sampleInterval`.
Limits: one active session per zone, 60-minute maximum session, and the stream stops if you stop listening for more than five minutes.
Needs Logs Read, or the Super Administrator, Administrator, Log Share or Log Share Reader role.
The dashboard view can export the table as JSON.

### Logpull (legacy)

Source: https://developers.cloudflare.com/logs/logpull/.
Logpull is a REST API (`/zones/{zone_id}/logs/received`) for `http_requests` logs, Enterprise only, described as legacy with Logpush or Logs Engine recommended instead.
Retention must be enabled first via `POST /zones/{zone_id}/logs/control/retention/flag`.
Logs are available about one to five minutes after the request, can be queried from 1 minute in the past back at least 3 days and up to 7 days, and are ordered by time received so pulls are deterministic.
Limits: 15 requests/min per zone, 180 requests/min per user, 1-hour maximum `start`/`end` span, 10 GiB response maximum, 10-minute timeout, 30-second idle stream timeout (frequent timeouts block for 1 hour) (https://developers.cloudflare.com/logs/logpull/additional-details/).
Logpull does not work when Customer Metadata Boundary is set to EU only.

### Logs Engine (being replaced)

Logs Engine (https://developers.cloudflare.com/logs/r2-log-retrieval/) lets you query Logpush-to-R2 logs via `GET /accounts/{id}/logs/list`, `/logs/retrieve`, and a Ray ID lookup that first indexes a time range (indexes expire after seven days unused; requires the beta "Logpull RayID Lookup" subscription).
The page says Logs Engine "is going to be replaced by Log Explorer".

### Workers Trace Events

`workers_trace_events` is an account-scoped Logpush dataset with `ScriptName`, `ScriptVersion`, `ScriptTags`, `DispatchNamespace`, `Entrypoint`, `EventType` (fetch, scheduled, alarm, queue, email, worker_rpc, hibernatable_web_socket), `Outcome`, `CPUTimeMs`, `WallTimeMs`, `EventTimestampMs`, `Event`, `Exceptions` and `Logs` (console messages) (https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/).
It requires the Workers Paid plan and has request-based pricing (above).

## Log Explorer

Docs: https://developers.cloudflare.com/log-explorer/ (9 pages).

### What it is

Log Explorer stores Cloudflare logs inside Cloudflare (in per-customer, single-tenant R2 buckets you cannot see in your own R2) and lets you search them in the dashboard or via a SQL API, without forwarding to a SIEM (https://developers.cloudflare.com/log-explorer/, https://developers.cloudflare.com/log-explorer/faq/).
Status: GA since 2025-06-18 (https://developers.cloudflare.com/log-explorer/changelog/).
Features: Log Search (filter builder or custom SQL, saved queries, tabs and pivots, query cancellation, result distribution chart, contextual pivots to Investigate and Zero Trust), custom dashboards from unsampled data, dataset management, and an API.
Log Explorer is for actual traffic; Cloudflare Trace is for simulated "what-if" requests.

### Datasets

Zone level: `http_requests`, `firewall_events`, `dns_logs`, `nel_reports`, `page_shield_events`, `spectrum_events`, `zaraz_events`.
Account level: `access_requests`, `casb_findings`, `device_posture_results`, `gateway_dns`, `gateway_http`, `gateway_network`, `zero_trust_network_sessions`, `audit_logs`, `audit_logs_v2`, `biso_user_actions`, `dns_firewall_logs`, `email_security_alerts`, `magic_bgp_logs`, `magic_ids_detections`, `network_analytics_logs`, `sinkhole_http_logs`, `ipsec_logs` (https://developers.cloudflare.com/log-explorer/manage-datasets/).
Enable per dataset in the dashboard or with `POST /zones/{zone_id}/logs/explorer/datasets` (or `/accounts/...`) and `{"dataset":"http_requests"}`.
Since 2026-03-11 you can choose ingested fields (Timestamp mandatory), and since 2026-08-28 ingestion filters; since 2026-08-26 datasets can be deleted (deletion protection on by default; deletion is irreversible and asynchronous).
Ingestion starts when the dataset is enabled; there is no backfill.
Header and cookie fields require Logpush custom fields configured on the zone.

### Querying

- API: `GET .../logs/explorer/query/sql?query=...` at zone or account scope (https://developers.cloudflare.com/log-explorer/api/).
- SQL support (https://developers.cloudflare.com/log-explorer/sql-queries/): `SELECT`, `FROM`, `WHERE` (up to 25 predicates), `SELECT DISTINCT`, `GROUP BY`, `ORDER BY`, `LIMIT` (default 10,000 when omitted), `OFFSET`; functions `ARRAY_CONTAINS`, `SUBSTRING`, `LOWER`, `UPPER`, `SUM`, `MIN`, `MAX`, `COUNT`, `COUNT(DISTINCT)`, `AVG`; `CASE WHEN`, `LIKE`, `IN`, `BETWEEN`, arithmetic, comparison, logical, bitwise and `||` operators.
- Every table has a `date` column (`YYYY-MM-DD`) that narrows scans; narrow time frames, select only needed columns, and probe with `COUNT(*)` (https://developers.cloudflare.com/log-explorer/log-search/).
- Example queries cover CDN usage, security action distribution, IPs that triggered challenges, bandwidth by URI, RTT by country, cache status with TTFB, and slowest paths (https://developers.cloudflare.com/log-explorer/example-queries/).
- Log Explorer datasets are also reachable from the Analytics SQL API as `logs.` datasets, and from Custom Alerts with a 10-minute minimum execution interval.

### Limits, pricing, availability

As of 2026-10-05:

- Availability: "a paid add-on for any Application Services or Zero Trust purchase", with no free version or trial (https://developers.cloudflare.com/log-explorer/pricing/).
- Billing: by GB ingested and stored, with no query charges; attack traffic counts, but L7 DDoS attack logs are not ingested by default.
- The Log Explorer pages do not state a per-GB price; the Observability pricing page states $1 per GB ingested with 30-day retention for "Unsampled security datasets (legacy Log Explorer)".
- Contract customers can extend retention up to two years at $0.10 per GB per month.
- Ingestion rate up to 50,000 records per second; contact the account team beyond that.
- Customer Metadata Boundary is not supported.
- Permissions: Logs Edit (manage datasets), Logs Read (search), Logs Write (save queries), Analytics Read (custom dashboards).
- Usage alerts via the **Usage-based Billing** notification.
- Turning it off requires disabling every account and zone dataset and cancelling the subscription in Billing.
- Per-dataset average record sizes are listed for estimates, e.g. `http_requests` 1.56 kB average and 9.76 kB maximum.

## Health Checks

Docs: https://developers.cloudflare.com/health-checks/ (8 pages); the same feature is also documented under Smart Shield at https://developers.cloudflare.com/smart-shield/configuration/health-checks/.

### What it is

Standalone Health Checks monitor an IP or hostname (origin server or application) from Cloudflare's edge and notify you in near real time, even with a single origin and no load balancer.
Every page now carries the banner "This functionality is now offered as part of Cloudflare's origin server safeguard, Smart Shield".
They are separate from Load Balancing health monitors (https://developers.cloudflare.com/load-balancing/monitors/).

### Configuration

Configure in the dashboard under **Traffic** > **Health Checks** (or **Speed** > **Smart Shield** > Health Checks) or with the API under `/zones/{zone_id}/healthchecks` (with a `preview` sub-resource) and `/zones/{zone_id}/smart_shield/healthchecks` (`raw/api/endpoints.tsv`).
API schema fields and defaults (`raw/api/openapi.json`, `healthchecks_*` schemas), as of 2026-10-05:

| Field | Meaning | Default |
| --- | --- | --- |
| `type` | `HTTP`, `HTTPS` or `TCP` | `HTTP` |
| `address` | Hostname or IP to check | none |
| `interval` | Seconds between checks | 60 |
| `timeout` | Seconds before a check fails | 5 |
| `retries` | Immediate retries on timeout | 2 |
| `consecutive_fails` / `consecutive_successes` | Fails or successes before a status change | 1 / 1 |
| `check_regions` | `WNAM`, `ENAM`, `WEU`, `EEU`, `NSAM`, `SSAM`, `OC`, `ME`, `NAF`, `SAF`, `IN`, `SEAS`, `NEAS`, or `ALL_REGIONS` (Business and Enterprise) | Cloudflare picks |
| `http_config.method` | `GET` or `HEAD` only | `GET` |
| `http_config.path` | Path to check | `/` |
| `http_config.expected_codes` | Codes or ranges such as `2xx` | `200` |
| `http_config.expected_body` | Case-insensitive substring in the first 10 KB | empty |
| `http_config.header` | Request headers (set `Host`; User-Agent cannot be overridden) | none |
| `http_config.follow_redirects`, `allow_insecure`, `port` | Redirects, skip cert validation, port (80 for HTTP, 443 for HTTPS) | false, false, 80 |
| `suspended` | Stop sending checks | false |

Each selected region runs checks from three data centers, so more regions and shorter intervals add origin load (https://developers.cloudflare.com/health-checks/concepts/health-checks-regions/).
Analytics are regional or global aggregates only, not per data center.
Authenticated Origin Pulls are not supported by standalone Health Checks.
Health Checks send the user agent `Mozilla/5.0 (compatible;Cloudflare-Healthchecks/1.0;+https://www.cloudflare.com/; healthcheck-id: XXX)` with the first 16 characters of the check ID, which you can use in a WAF skip rule to bypass Zone Lockdown (https://developers.cloudflare.com/health-checks/how-to/zone-lockdown/).
If the hostname is proxied through Cloudflare, the check probes Cloudflare's edge rather than the origin; use the origin IP or an unproxied hostname to monitor the origin directly (https://developers.cloudflare.com/health-checks/health-checks-analytics/).

### Analytics and notifications

Health Check Analytics shows uptime, failure reasons, latency (RTT) and an event log with waterfall, and documents failure reasons such as TCP connection failed, HTTP timeout, response code or body mismatch, TLS errors, no route to host, DNS unknown host, DNS internal (non-public IP) and connection reset (https://developers.cloudflare.com/health-checks/health-checks-analytics/).
The "Health Checks status notification" fires on unhealthy, healthy or either, is included with Pro and higher, and is sent only after a majority of selected regions change (2 of 3 data centers for one region, 7 of 13 regions with all selected) (https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/).
Health Checks notifications are stateful (a recovery resolves the earlier incident), per the Load Balancing changelog of 2026-08-07.

### Plan availability

As of 2026-10-05 (https://developers.cloudflare.com/health-checks/):

| | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Availability | No | Yes | Yes | Yes |
| Number of checks | 0 | 10 | 50 | 1,000 |
| Analytics | No | Yes | Yes | Yes |

## Notifications (Alerts)

Docs: https://developers.cloudflare.com/notifications/ (10 pages; the docs now title the product "Alerts" and the dashboard path is **Alerts**).

### What it is and delivery

Alerts notify you about DDoS attacks, certificate expirations, origin failures, billing spikes and more, via built-in alert types or Custom Alerts (https://developers.cloudflare.com/notifications/).
Delivery methods, as of 2026-10-05:

- **Email**: all plans; up to 20 recipients per Custom Alert.
- **Webhooks**: all plans; accounts without a paid zone can configure up to 100 webhook destinations.
- **PagerDuty**: needs at least one Business-or-higher zone; connected via OAuth under **Alerts** > **Destinations**, not as a webhook (https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/).
- **Connected services**, "including coding agents" (no further detail on the page).

### Webhooks

Source: https://developers.cloudflare.com/notifications/get-started/configure-webhooks/.
Preset services: Slack, Google Chat, Discord, Feishu, Microsoft Teams (secret in the URL), Datadog events, OpsGenie, Splunk HEC (three endpoints only, port 443 with SSL or 8088 without, indexer acknowledgement disabled), ServiceNow, and generic webhooks.
Generic webhooks send your secret in the `cf-webhook-auth` header, which you should verify; they only go to publicly resolvable IPs on port 80 or 443, so private targets need a Worker relay or Cloudflare Tunnel (example relay: https://github.com/cloudflare/cf-webhook-relay/).
Webhooks come from Cloudflare IP ranges, which you may need to allowlist.
Terraform resource: `cloudflare_notification_policy_webhooks`.
Payload schema (https://developers.cloudflare.com/notifications/reference/webhook-payload-schema/): `name`, `text`, `data` (alert-specific), `ts` (unix seconds), `account_id`, `policy_id`, `policy_name`, `alert_type` (e.g. `http_alert_origin_error`, `advanced_ddos_attack_l7_alert`), `alert_correlation_id`, `alert_event` (`ALERT_STATE_EVENT_START` or `ALERT_STATE_EVENT_END`); some fields may be absent.

### Configuration and management

Creating alerts needs Super Administrator, Administrator, Account edit, or an API token with Notifications Read/Write (https://developers.cloudflare.com/notifications/get-started/).
Each alert can be edited, disabled, tested, muted (1h, 12h, 24h or custom; muted alerts still appear in history as silenced) or deleted; silences are managed under **Alerts** > **Silences**.
Alert history: `GET /accounts/{account_id}/alerting/v3/history`, 30 days on Free, Pro and Business, 90 days on Enterprise, nothing before 2021-10-11 (https://developers.cloudflare.com/notifications/notification-history/).
Removing a member does not remove their email from existing alerts.

### Custom Alerts (beta)

Source: https://developers.cloudflare.com/notifications/notification-available/ (updated 2026-10-02).
Custom Alerts run a SQL API query on a schedule and notify when the result meets detection criteria; dataset availability follows plan and permissions.
The query (builder or custom SQL) must return one numeric column named `value`, read one schema-qualified dataset, include an account or zone filter, and omit a trailing semicolon.
Time modes: Automatic (recommended, Cloudflare supplies the window) or Manual (fixed relative range in SQL).
Detection methods:

- **Threshold**: comparison operators `<`, `>`, `<=`, `>=`, `==`, `!=` against a fixed value over an evaluation window.
- **Anomaly detection**: z-score against a baseline window at least six times the evaluation window and at most 24h; spikes, drops or both; optional minimum event count; needs 30 minutes of history first.
- **Service-level objective**: bad-events and total-events queries, short and long windows, triggers when `(1 - bad/total) x 100` is below target in both.

Execution interval defaults to the fastest the dataset supports (most SQL API datasets 1 minute; Log Explorer datasets 10 minutes); repeat notification interval 1 minute to 168h, default 1h.

### Built-in alerts and plan availability

Selected from https://developers.cloudflare.com/notifications/notification-available/, as of 2026-10-05:

| Product | Alert | Included with |
| --- | --- | --- |
| Billing | Usage Based Billing | Pro or higher; Pay-as-you-go accounts only, most Enterprise contracts unsupported |
| Bots | Bot Detection Alert, Custom Bot Detection Alert | Accounts with at least one Enterprise zone |
| Client-side security | New Domain, New Resources, URL length alerts | Business or higher |
| Client-side security | New Code Change, Malicious Domain/Script/URL | Client-Side Security Advanced |
| Cloudflare Status | Maintenance Notification, Incident Alerts | All plans |
| DDoS Protection | HTTP DDoS Attack Alert | All plans |
| DDoS Protection | Layer 3/4 DDoS Attack Alert | Magic Transit and/or BYOIP |
| DDoS Protection | Advanced HTTP DDoS Attack Alert | Enterprise with Advanced DDoS Protection add-on |
| Health Checks | Health Checks status notification | Pro or higher |
| Load Balancing | Pool Enablement, Load Balancing Health Alert | Load Balancing purchase |
| Logpush | Failing Logpush Job Disabled | Enterprise plans |
| Pages | Project updates | All plans |
| Radar | Radar Alerts (traffic anomalies, outages, route hijacks and leaks for countries, regions or ASNs) | All plans |
| Route Leak Detection | Route Leak Detection Alert | BYOIP |
| SSL/TLS | Universal SSL Alert | All plans |
| SSL/TLS | Advanced Certificate, AOP and mTLS certificate expiry, SSL for SaaS custom hostnames | Respective products |
| Security Center | Security Insights, Abuse report | All plans |
| Security Center | Brand Protection Alerts and Digest | Pro or higher |
| Traffic Monitoring | Origin Error Rate, Advanced Error Rate, Traffic Anomalies | Enterprise plans |
| Trust and Safety | New Blocks, Removed Blocks, Block Review Rejection | All plans |
| Tunnel | Tunnel Creation or Deletion, Tunnel Health Alert | All Zero Trust plans |
| Web Analytics | Weekly summary | All plans |
| WAF | Security Events Alert | Business and Enterprise |
| WAF | Advanced Security Events Alert | Enterprise |

Other groups on the page: Cloudflare Access (expiring service tokens), Images, DEX, Secondary DNS, Magic Transit and Network Flow, Network Interconnect, Stream.
HTTP Traffic Alerts details (https://developers.cloudflare.com/notifications/reference/traffic-alerts/): Origin Error Rate counts 5xx plus edge 521, 522 and 523 and uses multi-window burn rates (5 minutes and 1 hour) against a chosen SLO; Advanced Error Rate can target edge or origin codes and group by status code; Traffic Anomalies need a z-score above 3.5 or below -3.5 and more than 200 requests, comparing the current 5 minutes to the past 4 hours every 5 minutes.
Traffic alerts are per zone, cannot target a path or hostname, only see proxied hostnames, and their trigger conditions cannot be customized.
Budget alerts: eligible Pay-as-you-go accounts get a default $10 account-level budget alert (rolled out from 2026-07-20); usage is processed daily so alerts fire the day after; subscriptions are excluded; informational only (https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/).

## Build hooks for Web3 projects

Concrete uses of the products above for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
Each hook names the documented capability it relies on; anything beyond the docs is marked as a design suggestion.

1. **RPC-proxy abuse detection with Logpush + Transformers.**
   Put your public JSON-RPC proxy (for example a Worker in front of Helius for Solana, or an Ethereum, Base or chain 4663 node) on a proxied hostname such as `rpc.example.xyz`.
   Create a zone `http_requests` Logpush job to R2 (internal rate, 25 GB/month included, $0.03/GB after) with a filter `{"key":"ClientRequestHost","operator":"eq","value":"rpc.example.xyz"}`.
   Ship `ClientIP`, `ClientASN`, `ClientCountry`, `ClientRequestPath`, `ClientRequestUserAgent`, `JA4`, `BotScore`, `VerifiedBotCategory`, `EdgeResponseStatus`, `SecurityAction`, `RayID`.
   Alternatively, attach a Transformer that drops `2xx` noise and keeps only `429`, `403` and challenged requests, so the export stays small.
   JSON-RPC method names live in the POST body, which Logpush does not log; add a request header such as `x-rpc-method` from your Worker and capture it with a custom field (`request_fields`), or log methods to Workers Analytics Engine instead (design suggestion).
2. **Per-method and per-key RPC metering with Workers Analytics Engine.**
   In the RPC Worker call `writeDataPoint({ indexes: [apiKeyOrIpBucket], blobs: [chain, method, country], doubles: [latencyMs, responseBytes] })`.
   Use the API key or a client bucket as the index, because sampling is equitable per index, and never a UUID.
   Query with `SUM(_sample_interval)` grouped by `blob2` for calls per method per chain, for usage dashboards or usage-based billing; limits are 250 data points per invocation and three months of retention, and WAE billing is announced but not yet charged as of 2026-10-05.
3. **Per-path request counts for token-list and metadata APIs via GraphQL or SQL.**
   GraphQL `httpRequestsAdaptiveGroups` with `dimensions { metric: clientRequestPath }` and `orderBy: [count_DESC]`, filtered with `clientRequestHTTPHost: "api.example.xyz"` and `requestSource: "eyeball"`, gives top paths such as `/tokenlist.json` or `/metadata/{mint}`.
   To check whether token metadata is actually served from cache, use the Logpush or Log Explorer `CacheCacheStatus` field (the Log Explorer example "Summarize CDN traffic by cache status" does exactly this), or find the cache-status dimension of `httpRequestsAdaptiveGroups` through introspection.
   The SQL API equivalent is `SELECT ... FROM events.httpRequests WHERE timestamp >= $start GROUP BY ...`, and from inside a Worker the `ANALYTICS_SQL` binding needs no token.
   Stay under 300 GraphQL queries per 5 minutes per token, or opt into account-based limits with `X-Rate-Limit-Type: account-based` if you poll many zones.
4. **Launch-day alerting with Custom Alerts.**
   A Threshold Custom Alert on `SELECT COUNT(*) AS value FROM events.httpRequests WHERE zoneTag = ... AND edgeResponseStatus >= 500` warns when a mint page or launchpad API starts failing.
   An Anomaly Custom Alert on request counts to `/api/quote` or `/api/swap` catches bot surges during a token launch; an SLO Custom Alert with bad = 5xx and total = all requests mirrors the Enterprise-only Origin Error Rate alert on any plan where the dataset is available (availability of Custom Alerts by plan is not stated).
   Deliver to a Discord or Slack webhook (all plans) or PagerDuty (Business zone or higher), and verify `cf-webhook-auth` on generic webhooks.
5. **RPC node health with Health Checks.**
   Standalone Health Checks (Pro and above, 10 checks on Pro) can watch a self-hosted Solana validator RPC, a Geth or Reth node, a Base node or a chain 4663 node from up to 13 regions.
   Health Checks only send `GET` or `HEAD`, so they cannot POST a JSON-RPC `eth_blockNumber` or `getHealth` body; expose a small HTTP health route (for example `/health` that returns `200` and a body containing `ok` only when the node is synced) and use `expected_body` (design suggestion).
   Check the origin IP or an unproxied hostname, otherwise you are probing Cloudflare's edge.
   Route the Health Checks status notification to a webhook so a Worker can flip traffic or a feature flag when a node goes unhealthy (design suggestion).
6. **Live incident triage with Instant Logs.**
   On Business or Enterprise, open an Instant Logs session filtered to `ClientRequestPath` `startsWith` `/rpc` during a launch and pipe it through Angle Grinder to rank `ClientIP` or `ClientASN` by volume.
   Sessions last at most 60 minutes and one per zone.
7. **Forensics on a drained-wallet or phishing incident with Log Explorer.**
   If you buy Log Explorer, `http_requests` and `firewall_events` become searchable by Ray ID, IP, JA4 and path without a SIEM, for 30 days by default (up to two years on contract).
   It does not backfill, so enable it before launch day.
8. **Frontend RUM without cookies with Web Analytics.**
   For a dapp or trading UI, Web Analytics needs no cookies or `localStorage`, tracks SPA route changes, and gives Core Web Vitals per path, which matters for wallet-connect flows.
   It does not log query strings (so wallet addresses in query parameters are not collected), has no custom events, and is blocked by ad-blockers, so pair it with edge analytics.
   With a strict CSP, allow `static.cloudflareinsights.com` in `script-src` and `cloudflareinsights.com` (manual) or `'self'` (automatic) in `connect-src`.
9. **Tracing slow quote or swap requests with Cloudflare Traces.**
   Add a trace rule that samples 100% of `/api/swap` and a low default rate elsewhere, export to Grafana, Honeycomb or Sentry, and turn on **Forward to origin** so your quote service's spans join the trace.
   From 2026-12-01 persisted traces count toward the Observability allowance (Paid: 50 GB ingestion and 12 GB-month included).
10. **Cost guardrails.**
    Keep the default $10 budget alert or set a Usage Based Billing alert for Argo, Load Balancing or Logpush before a launch, because Logpush export and Observability ingestion are now metered on self-serve plans.

## Gaps and contradictions

Flagged as found in the 2026-10-05 mirror; no side is picked.

1. **Logpush plan availability.**
   https://developers.cloudflare.com/logs/logpush/ and the 2026-09-30 changelog say Logpush is on Free, Pro, Business and Enterprise.
   https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/ still says "Customers in the Enterprise plan can enable the Cloudflare Logs Logpush service", and https://developers.cloudflare.com/analytics/types-of-analytics/ describes Logs as "for Enterprise customers".
   https://developers.cloudflare.com/analytics/analytics-integrations/ says integrations are for Enterprise customers.
2. **Failing Logpush Job Disabled alert.**
   Listed as "Enterprise plans" on both https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/ and https://developers.cloudflare.com/notifications/notification-available/, while Logpush itself is now on all plans and the health dashboard page tells everyone to configure health notifications.
3. **Logpush volume estimates.**
   The same page (https://developers.cloudflare.com/logs/logpush/) gives about 100 to 250 MB/day for 1M requests/day in one list and 250 to 500 MB/day for 1M req/day in the next.
4. **Logpush timestamp default.**
   Dashboard default `rfc3339` and API default `unixnano` per https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/; the older `logpull_options` text on the API configuration page lists `unixnano` as default; consistent but easy to trip on.
5. **Custom dashboards limit.**
   https://developers.cloudflare.com/analytics/custom-dashboards/ says every account can have up to 100 dashboards, while the Log Explorer changelog entry of 2026-04-22 says Log Explorer customers get 100 "up from 25 for standard customers".
6. **Number of GraphQL datasets.**
   "More than 70 datasets" on https://developers.cloudflare.com/analytics/graphql-api/limits/ and the settings page, versus "over 100 datasets" on https://developers.cloudflare.com/analytics/custom-dashboards/ and the 2026-04-22 changelog.
7. **Network Analytics requirements.**
   https://developers.cloudflare.com/analytics/types-of-analytics/ says Enterprise customers using Spectrum, Magic Transit or BYOIP.
   https://developers.cloudflare.com/analytics/network-analytics/ lists Enterprise plan, Magic Transit or Spectrum, and Cloudflare WAN, without BYOIP and without saying whether WAN is required in addition.
8. **Confidence intervals "planned" versus shipped.**
   https://developers.cloudflare.com/analytics/sampling/ and the WAE FAQ say Cloudflare plans to expose confidence intervals or margins of error "in the near future", while https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/ documents them as available for adaptive GraphQL datasets (WAE still has no documented equivalent).
9. **Workers Analytics Engine billing.**
   https://developers.cloudflare.com/analytics/analytics-engine/pricing/ (updated 2026-04-23) says usage is not billed yet and billing starts "in the coming months"; no later page confirms a start date.
10. **Log Explorer price.**
    The Log Explorer pricing page states GB-based billing but no rate; the only rate is "$1 per GB ingested" for "unsampled security datasets (legacy Log Explorer)" on https://developers.cloudflare.com/observability/pricing/.
    The FAQ says "There is no free version", while the Observability datasets page presents the same datasets as enabled "On Account" inside the general Logs view.
11. **Log Explorer dataset lists differ.**
    https://developers.cloudflare.com/observability/logs/datasets/ lists `dex_application_tests`, `dex_device_state_events` and `warp_toggle_changes`, which https://developers.cloudflare.com/log-explorer/manage-datasets/ does not list, though the Log Explorer pricing page gives record sizes for them.
12. **Logs Engine versus Logpull recommendation.**
    https://developers.cloudflare.com/logs/logpull/ recommends Logs Engine as a Logpull replacement, while https://developers.cloudflare.com/logs/r2-log-retrieval/ says Logs Engine is itself being replaced by Log Explorer.
13. **Web Analytics site limits and page labels.**
    https://developers.cloudflare.com/web-analytics/limits/ gives 10 non-proxied sites and no limit for proxied sites, while the FAQ says "a soft limit of ten sites per account" without the proxied exception.
    The `llms.txt` describes the limits page as "Rate limits and data retention", but the page has neither; retention (six months) is only in the FAQ.
14. **Mislabeled `llms.txt` descriptions.**
    In `raw/docs/analytics/llms.txt`, the WAE "Get started" page is described as "Set up and access Network Analytics", the WAE "Limits" page as "Review GraphQL Analytics API query limits", and the GraphQL "Get started" as "Set up and access Network Analytics".
    The Logs `llms.txt` "FAQ" entry is described as "Log Explorer questions" but the page is the Logs FAQ index.
15. **Health Checks home.**
    Health Checks pages say the feature "is now offered as part of Smart Shield" and duplicate pages exist under `/smart-shield/configuration/health-checks/`; the plan table (Pro 10, Business 50, Enterprise 1,000) appears only on the Health Checks overview, and the Smart Shield index just says "Pro plans and above".
16. **Health check method versus JSON-RPC.**
    The API schema allows only `GET` and `HEAD`; no page says how to health-check POST-only APIs.
17. **Status labels missing.**
    No beta or GA label is given for Cloudflare Traces, the Observability Logs view, the Analytics SQL API, or Edge Log Delivery plan availability; Custom Alerts are labeled beta; Account Analytics is beta; Security reports are closed beta.
18. **Free-plan delay versus 30-day retention.**
    https://developers.cloudflare.com/analytics/faq/about-analytics/ says Free plan metrics are delayed 24 hours for new sign-ups, a statement not repeated in the 2026-10-02 retention changelog; it may be stale.
19. **Network Analytics v1 sample rate wording.**
    The GraphQL sampling page lists NAv1 `ipFlows*` nodes at a fixed 0.012% (1 in 8,192) as if current, while the migration guide says NAv1 is deprecated.
20. **Pricing pages not mirrored.**
    The Logs overview links plan and price pages on www.cloudflare.com that are not in `raw/`, so marketing-site prices could not be cross-checked.
