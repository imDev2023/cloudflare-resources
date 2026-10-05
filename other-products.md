# Other Cloudflare products (outside the docs sidebar)

This file covers the products listed in the docs product index (`raw/docs/llms.txt`, 113 entries as of 2026-10-05) that do not appear in the developers.cloudflare.com sidebar (`raw/nav/home-sidebar.md`) and are not covered by another file in this knowledge base.
After the exclusions below, fourteen products remain: Rules, Ruleset Engine, Billing (including USDC stablecoin payments), Network, Randomness Beacon (drand), Time Services, Radar (including its API and URL Scanner), Resource Tagging, Tenant, Version Management, Privacy Pass, Privacy Proxy, Cloudflare OHTTP Relay and Style Guide.
The most Web3-relevant facts are that Cloudflare bills USDC on Base and Polygon through a Stripe-hosted permit flow, that the Randomness Beacon is the League of Entropy drand network whose quicknet beacon publishes publicly verifiable BLS randomness every 3 seconds at `drand.cloudflare.com`, that the Rules language now exposes per-request random bytes (`cf.random_seed`) and a `hash_in_range()` sampler for traffic splitting, and that Radar data is licensed CC BY-NC 4.0, which limits commercial reuse.
Everything below is dated as of 2026-10-05 unless a page date is given, and states only what the mirrored sources say.

## Contents

- [Scope and how the leftover list was derived](#scope-and-how-the-leftover-list-was-derived)
- [Rules](#rules)
- [Ruleset Engine](#ruleset-engine)
- [Billing](#billing)
- [Network](#network)
- [Randomness Beacon (drand)](#randomness-beacon-drand)
- [Time Services](#time-services)
- [Radar](#radar)
- [Resource Tagging](#resource-tagging)
- [Tenant](#tenant)
- [Version Management](#version-management)
- [Privacy Pass](#privacy-pass)
- [Privacy Proxy](#privacy-proxy)
- [Cloudflare OHTTP Relay](#cloudflare-ohttp-relay)
- [Style Guide](#style-guide)
- [Pointers: Security Center and docs folders outside llms.txt](#pointers-security-center-and-docs-folders-outside-llmstxt)
- [Build hooks for Web3 projects](#build-hooks-for-web3-projects)
- [Gaps and contradictions](#gaps-and-contradictions)

## Scope and how the leftover list was derived

`raw/docs/llms.txt` lists 113 product entries grouped as Application performance, Application security, Cloudflare One, Consumer services, Core platform, Developer platform, Docs collections, Network security and Other.
Comparing it with the sidebar gives 38 entries that are not in the sidebar: Automatic Platform Optimization, China Network, Google tag gateway, Smart Shield, Web3, Challenges, Firewall Rules (deprecated), Key Transparency Auditor, Secrets Store, Cloudflare Network Firewall, Data Localization Suite, Multi-Cloud Networking, Radar, WARP Client, Billing, Cloudflare Fundamentals, Network, Notifications, Randomness Beacon, Resource Tagging, Rules, Ruleset Engine, Tenant, Time Services, Version Management, Agent Lee, Cloudflare OHTTP Relay, Dynamic Workers, MoQ, Pages, Privacy Pass, Privacy Proxy, Network Error Logging, Network Flow, Docs for agents, Migration Guides, Security dashboard and Style Guide.
The brief assigns 24 of those to other files (Web3, Challenges, Firewall Rules, Key Transparency, Secrets Store, Network Firewall, Data Localization Suite, Multi-Cloud Networking, WARP Client, the four application-performance products, Notifications, Fundamentals, Agent Lee, Dynamic Workers, MoQ, Pages, Network Error Logging, Network Flow, Docs for agents, Migration Guides and Security dashboard).
The remaining 14 are covered here.
Registrar and Security Center are in the sidebar (Domains & DNS and Application Security), so they are not leftovers; Security Center gets a short pointer below only because Radar's URL Scanner lives inside it.
Workers is also in the sidebar, although the brief lists it as excluded.

Page counts in the mirror for the covered products: Rules 188, Ruleset Engine 235 (191 of them are field reference pages), Style Guide 156, Billing 33, Radar 26, Version Management 14, Privacy Proxy 14, Tenant 11, Randomness Beacon 9, Time Services 9, Resource Tagging 9, Network 8, Privacy Pass 7, OHTTP Relay 7.

## Rules

**What it is.**
Cloudflare Rules lets you redirect visitors, rewrite URLs, override where requests are sent, and customize Cloudflare settings for specific requests; it is "Available on all plans" and every Rules feature requires the hostname's DNS records to be proxied through Cloudflare.
Source: https://developers.cloudflare.com/rules/

**Sub-products and plan quotas (as of 2026-10-05).**

| Feature | Status | Free | Pro | Business | Enterprise | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Configuration Rules | GA | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/configuration-rules/ |
| Transform Rules (active rules) | GA | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/transform/ |
| Transform Rules regex support | | No | No | Yes | Yes | same |
| Single Redirects | GA | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/url-forwarding/ |
| Single Redirects regex support | | No | No | Yes | Yes | same |
| Bulk Redirect Rules (per account) | GA | 15 | 15 | 15 | 50 | same |
| Bulk Redirect Lists (per account) | | 5 | 5 | 5 | 25 | same |
| URL redirects across lists | | 10,000 | 25,000 | 50,000 | 1,000,000 (default; "several million" on request) | same |
| Origin Rules | GA | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/origin-rules/ |
| Origin Rules Host header, SNI and DNS record override | | No | No | No | Yes | same |
| Origin Rules destination port override | | Yes | Yes | Yes | Yes | same |
| Snippets | GA | 0 (not available) | 25 | 50 | 300 | https://developers.cloudflare.com/rules/snippets/ |
| Snippet subrequests | | 0 | 2 | 3 | 5 | same |
| Cloud Connector | Beta | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/cloud-connector/ |
| Custom Errors (rules / assets) | GA | 0 / 0 | 25 / 25 | 50 / 50 | 300 / 300 | https://developers.cloudflare.com/rules/custom-errors/ |
| Custom Errors Origin Error Pages | | No | No | No | Yes | same |
| Compression Rules | GA | 10 | 25 | 50 | 300 | https://developers.cloudflare.com/rules/compression-rules/ |
| Page Rules | Deprecated per llms.txt | 3 | 20 | 50 | 125 | https://developers.cloudflare.com/rules/page-rules/ |
| URL normalization | GA | all plans | | | | https://developers.cloudflare.com/rules/normalization/ |
| Cloudflare Trace | Beta | all plans | | | | https://developers.cloudflare.com/rules/trace-request/ |

Bulk Redirects quotas are per account and follow the highest plan on the account, while Single Redirects quotas are per zone and follow the zone plan.
Source: https://developers.cloudflare.com/rules/url-forwarding/

**Execution order.**
The documented order of Rules features is Single Redirects, URL Rewrite Rules, Configuration Rules, Origin Rules, Bulk Redirects, Managed Transforms, Request Header Transform Rules, Cache Rules, Snippets, Cloud Connector, and all of these take precedence over Page Rules.
For non-terminating actions the last change in a phase wins, while for terminating actions (Block, Redirect, challenges) evaluation stops at the first match, so Single Redirects beat Bulk Redirects when both match.
Request and response fields are immutable within a phase, so later rules in the same phase see original values; `raw.*` fields stay immutable across the whole request.
Sources: https://developers.cloudflare.com/rules/snippets/ and https://developers.cloudflare.com/ruleset-engine/about/rules/

**Configuration Rules.**
They change zone settings per request; documented settings are Automatic HTTPS Rewrites, Browser Integrity Check, Disable Real User Monitoring, Disable Zaraz, Email Obfuscation, Fonts, Hotlink Protection, I'm Under Attack, Markdown for Agents (`content_converter`), Opportunistic Encryption, Polish, Request Body Buffering, Response Body Buffering, Rocket Loader and SSL.
A configuration rule that disables Web Analytics wins over a Web Analytics rule that enables it.
Source: https://developers.cloudflare.com/rules/configuration-rules/settings/

**Transform Rules.**
Four kinds exist: URL Rewrite Rules (path and query only, never hostname), Request Header Transform Rules, Response Header Transform Rules and Managed Transforms (pre-built header changes that do not count against quotas and apply zone-wide).
A user needs the Firewall role or an Administrator role to access Transform Rules.
Request header rules cannot modify `cf-*` or `x-cf-*` headers (except removing `cf-connecting-ip`), cannot change `x-forwarded-for`, `true-client-ip`, `x-real-ip` or `x-forwarded-proto`, and cannot set `cookie`, only remove it; Cloudflare re-adds `x-forwarded-for` after all rule phases.
Response header rules cannot touch `cf-*` headers, cannot reference IP lists, and changing `cache-control` or `CDN-Cache-Control` in a response rule does not change Cloudflare caching (use Cache Rules).
Sources: https://developers.cloudflare.com/rules/transform/ , https://developers.cloudflare.com/rules/transform/request-header-modification/ , https://developers.cloudflare.com/rules/transform/response-header-modification/ , https://developers.cloudflare.com/rules/transform/managed-transforms/

**Redirects.**
Single Redirects are zone-level static or dynamic redirects with a wildcard interface; Bulk Redirects are account-level, essentially static lists (CSV import supported) that run after the WAF, so a WAF block prevents the redirect.
Source: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/

**Origin Rules.**
They override the Host header, SNI, resolved DNS record and destination port (1 to 65,535); a Host override also changes SNI unless an SNI override is added, and DNS or SNI targets must be hostnames on the same Cloudflare account.
An origin rule's Host override takes precedence over a load balancer header override, and it is ignored when evaluating Workers routes.
Source: https://developers.cloudflare.com/rules/origin-rules/features/

**Snippets.**
Snippets run short JavaScript on the Workers runtime for matching requests, with limits of 5 ms execution time, 2 MB memory and 32 KB total package size on all plans, and they are included at no additional cost on paid plans.
Each redirect in a subrequest chain counts as a subrequest, and Version Management does not support Snippets.
The "when to use" guide positions Snippets for free, unlimited lightweight request and response logic and Workers for state, bindings, logs, Smart Placement and heavy compute.
Sources: https://developers.cloudflare.com/rules/snippets/ and https://developers.cloudflare.com/rules/snippets/when-to-use/
The examples gallery includes JWT validation, HMAC request signing, bot-score honeypots, CORS headers, A/B testing, maintenance pages and custom cache: https://developers.cloudflare.com/rules/snippets/examples/

**Cloud Connector (beta).**
Routes matching traffic to public buckets on Cloudflare R2 (custom domain only, not `r2.dev`), AWS S3, Google Cloud Storage, Azure Blob Storage and Oracle Cloud Object Storage (Oracle added 2026-08-13 per the Rules changelog), rewriting the Host header and, for S3 website endpoints, the SSL mode.
It runs last and wins over other rules that set the same settings, but it does not configure caching or URL rewrites for you.
Sources: https://developers.cloudflare.com/rules/cloud-connector/ and https://developers.cloudflare.com/rules/cloud-connector/providers/

**Custom Errors.**
Error Pages (zone or account level, paid plans) customize Cloudflare error and challenge pages but do not apply to status codes 500, 501, 503 or 505; Custom Error Rules serve inline or fetched "assets" for status codes 400 and above from the origin or custom WAF responses, and take priority over Error Pages.
If the request lacks an `accept-encoding` header, Cloudflare returns its default error page instead of a custom Error Page.
Source: https://developers.cloudflare.com/rules/custom-errors/

**Compression Rules.**
Select gzip, Brotli or Zstandard per content type or extension; the first algorithm the browser supports is used, and `cache-control: no-transform` from the origin disables them.
Source: https://developers.cloudflare.com/rules/compression-rules/

**Page Rules.**
Only the highest-priority matching page rule applies, they need a proxied DNS record, and every newer Rules product overrides them; a migration guide maps each Page Rules setting to its modern replacement.
Sources: https://developers.cloudflare.com/rules/page-rules/ and https://developers.cloudflare.com/rules/reference/page-rules-migration/

**URL normalization and Trace.**
URL normalization rewrites incoming URLs to a canonical form before WAF, Workers and Access see them, and some baseline normalization (such as collapsing `//`) always applies.
Cloudflare Trace (beta) simulates a request through your configuration, is limited to Administrator or Super Administrator users, and does not show Load Balancing, IP Access rules, Firewall Rules, legacy rate limiting or legacy WAF, DLS hostnames or Spectrum.
Sources: https://developers.cloudflare.com/rules/normalization/ , https://developers.cloudflare.com/rules/trace-request/ , https://developers.cloudflare.com/rules/trace-request/limitations/

**Recent changes (Rules changelog).**
2026-10-02: `hash_in_range()` is GA for HTTP products on all plans.
2026-10-01: `coalesce()` and dynamic values on both sides of comparisons.
2026-09-22: `concat()` accepts up to 32 arguments (was 16).
2026-09-17: rulesets can be validated before deployment (`dry_run=true`).
2026-07-16: bot management fields and ASN in Cache Rules.
2026-01-27: request and response body buffering in Configuration Rules.
2026-01-22: `encode_base64()` and `sha256()` functions.
Source: https://developers.cloudflare.com/rules/changelog/

**Most useful pages.**
https://developers.cloudflare.com/rules/ , https://developers.cloudflare.com/rules/snippets/ , https://developers.cloudflare.com/rules/url-forwarding/ , https://developers.cloudflare.com/rules/origin-rules/features/ , https://developers.cloudflare.com/rules/reference/troubleshooting/ , https://developers.cloudflare.com/rules/examples/

## Ruleset Engine

**What it is.**
The engine behind WAF, DDoS, Rules, Cache Rules, Network Firewall and others, with an expression language based on Wireshark display filters, versioned rulesets and a shared Rulesets API.
Source: https://developers.cloudflare.com/ruleset-engine/

**Key concepts.**
A phase is a Cloudflare-defined stage of request handling; each phase has at most one entry point ruleset per account (`kind: root`) and per zone (`kind: zone`), and account-level rules run before zone-level rules in the same phase.
Account-level phases are Enterprise-only.
Rulesets are versioned, and deploying one means adding an `execute` rule to the phase entry point ruleset.
Managed rulesets are maintained by Cloudflare (WAF, DDoS Protection, Network Firewall) and customized with overrides, plus exceptions that only the WAF supports and that take priority over overrides.
Custom rulesets are currently supported only by the WAF.
Sources: https://developers.cloudflare.com/ruleset-engine/about/phases/ , https://developers.cloudflare.com/ruleset-engine/about/rulesets/ , https://developers.cloudflare.com/ruleset-engine/managed-rulesets/

**Phase order.**
Network layer: `ddos_l4`, `magic_transit`, `magic_transit_managed`, `magic_transit_ratelimit`, `magic_transit_ids_managed`.
HTTP request: `http_request_dynamic_redirect`, `http_request_sanitize`, `http_request_transform`, Waiting Room Rules (internal), API Shield detection (internal), `http_config_settings`, `http_request_origin`, `ddos_l7` (configuration only), `http_request_firewall_custom`, `http_ratelimit`, API Shield mitigation (internal), `http_request_firewall_managed`, `http_request_sbfm`, Access application check (internal), `http_request_redirect`, Managed Transforms (internal), `http_request_late_transform`, `http_request_cache_settings`, `http_request_snippets`, `http_request_cloud_connector`.
HTTP response: `http_custom_errors`, Managed Transforms (internal), `http_response_headers_transform`, `http_ratelimit` (response-based), `http_response_compression`, `http_response_firewall_managed` (Sensitive Data Detection), `http_log_custom_fields`.
Updating Super Bot Fight Mode rules via the Rulesets API is no longer supported.
Source: https://developers.cloudflare.com/ruleset-engine/reference/phases-list/

**Actions.**
`js_challenge`, `managed_challenge`, `challenge`, `block` (terminating), `skip`, `log` (Enterprise only), `execute`, `rewrite`, `redirect`, `route`, `set_config`, `compress_response`, `set_cache_settings`, `serve_error`, `log_custom_field`.
Source: https://developers.cloudflare.com/ruleset-engine/rules-language/actions/

**Limits.**
Maximum expression length 4,096 characters, maximum 64 regular expressions per rule on any plan, rule descriptions up to 4,096 bytes, and rate limits against concurrent updates of the same ruleset whose exact values "depend on the size of the ruleset and volume of requests".
The account-wide Cloudflare API limit of 1,200 requests per 5 minutes per user or token also applies.
Sources: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/ , https://developers.cloudflare.com/ruleset-engine/rulesets-api/ , https://developers.cloudflare.com/fundamentals/api/reference/limits/

**Functions and randomness fields.**
Documented functions: `any`, `all`, `encode_base64`, `cidr`, `cidr6`, `coalesce`, `concat`, `decode_base64`, `ends_with`, `hash_in_range`, `join`, `has_key`, `has_value`, `is_jwt_present`, `is_jwt_valid`, `len`, `lookup_json_integer`, `lookup_json_string`, `lower`, `regex_replace`, `remove_bytes`, `remove_query_args`, `sha256`, `split`, `starts_with`, `substring`, `to_string`, `upper`, `url_decode`, `uuidv4`, `wildcard_replace`, `bit_slice`.
`cf.random_seed` returns per-request random bytes; `hash_in_range(0, 100, cf.random_seed) < 10` selects about 10% of requests, the hash algorithm "may change at any time without prior notice", and `uuidv4(cf.random_seed)` works only in Transform Rules rewrite expressions.
Sources: https://developers.cloudflare.com/ruleset-engine/rules-language/functions/ and https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.random_seed/

**Dry run.**
Rulesets API `POST`, `PUT`, `PATCH` and `DELETE` accept `dry_run=true`, which runs the same authorization, syntax, quota and entitlement checks without persisting; a normal `200` returns `result: null`.
Source: https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/

## Billing

**What it is.**
Account billing: plans are billed per domain every 30 days (monthly) or yearly, add-ons separately, and some products are usage-based; subdomains are not billable domains and Free domains still produce $0 invoices.
Sources: https://developers.cloudflare.com/billing/ and https://developers.cloudflare.com/billing/understand/billing-policy/

**Payment methods.**
Billing policy lists Visa, Mastercard, American Express, Discover, PayPal, Apple Pay, Google Pay, Stripe Link and UnionPay, with ACH for Enterprise; gift and prepaid cards may be rejected.
Instant Bank Payments via Link are available to US-based self-serve accounts and show as payment method `link` with last four `0000`.
Sources: https://developers.cloudflare.com/billing/understand/billing-policy/ and https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/

**Stablecoin payments (page updated May 29, 2026).**
You can pay for Cloudflare services with USDC at checkout, for one-time charges and recurring billing including usage-based products.
Flow: choose **Crypto** at checkout, connect a wallet on a Stripe-hosted page at `crypto.stripe.com`, sign a one-time smart contract permit that authorizes the initial charge and future automatic charges, and the subscription activates after on-chain confirmation, "typically within seconds".
Supported: USDC on Base and Polygon; MetaMask, Phantom, Coinbase Wallet and 400+ wallets via WalletConnect; invoices stay in USD.
Chargebacks and disputes are not available, and stablecoin payments are final once confirmed on-chain.
The permit covers renewals, usage-based charges "billed at threshold for Workers, R2, and Stream", and prorated upgrade charges.
Failures are insufficient USDC (subscription enters dunning), a revoked or reduced permit (reconnect the wallet), or pre-transaction wallet screening (use another wallet or method); a card on file is used as fallback.
Refunds go back as USDC to the paying wallet, "typically within minutes".
Gas is paid by your wallet, Cloudflare adds no markup, and the USDC amount equals the USD invoice; payments sit in a `processing` state until confirmation and show as payment method `crypto` on invoices.
The permit is scoped to the specific subscription and can be revoked from the wallet at any time.
Source: https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/
Related but separate: AI Gateway "Machine Payments" (beta, changelog 2026-09-30) lets clients pay for eligible inference with x402 from a stablecoin wallet; that is covered with AI Gateway and x402 elsewhere in this knowledge base.
Source: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/

**Billing lifecycle.**
Invoices combine flat-rate charges for the upcoming period with usage charges for the period just ended; billing dates use UTC and the first paid purchase sets the monthly billing date.
A failed payment starts a 5-day grace period with up to 5 retries, blocks new purchases and billing-profile changes, and then downgrades the account to Free (sites stay up); paid services must be re-subscribed one by one after paying.
Upgrades are immediate and prorated; downgrades and cancellations take effect at period end with no refunds.
For usage-based services Cloudflare may preauthorize the card; if it fails, those services can be suspended (R2 requests return errors) and data may be deleted after 30 days without a valid payment method.
Sources: https://developers.cloudflare.com/billing/understand/how-billing-works/ and https://developers.cloudflare.com/billing/understand/billing-policy/

**Usage-based billing and threshold billing.**
Metered products with documented included usage: Workers (10M requests and 30M CPU-ms), R2 (10 GB storage, 1M Class A, 10M Class B), Argo Smart Routing (first 1 GB), Load Balancing (first 500K DNS queries), Cache Reserve, Spectrum and Log Explorer (none), and Observability, Stream, Images, Rate Limiting, Zero Trust, Vectorize and Analytics Engine ("varies by plan").
Threshold billing raises a mid-cycle invoice when combined usage across all usage-based products reaches a Cloudflare-set threshold that cannot be changed; it fires once per account, then the account returns to end-of-cycle billing; it applies to self-serve accounts but not Enterprise or startup program accounts; failed threshold payments retry over 5 days and can end in restriction.
Sources: https://developers.cloudflare.com/billing/understand/usage-based-billing/ and https://developers.cloudflare.com/billing/threshold-billing/

**Monitoring and controls.**
The Billable Usage dashboard (Pay-as-you-go only, Billing read permission) shows daily per-product overage costs from the same data source as invoices.
Budget alerts (Pay-as-you-go only) email recipients once per period when account-wide usage spend crosses a USD threshold, and they never pause or cap usage.
Per-product usage notifications (Pro plan and above) are set under Notifications as "Billable Usage".
Additional payment methods are auto-retried in sequence for renewals only (not one-time or initial payments), and the "Backup payment method" label was renamed "Additional payment method".
Roles: Super Administrator can do everything; Billing can pay and manage payment methods but not change subscriptions; Administrator can change subscriptions but not payment methods.
Contracted customers can enable preview services for 30 days (ACM, API Shield, Argo, Bot Management, Cloudflare for SaaS, Images, Load Balancing, Advanced Rate Limiting, Stream, Waiting Room, Web3, Workers, Zero Trust), shown as **NOT IN CONTRACT**.
Sources: https://developers.cloudflare.com/billing/manage/billable-usage/ , https://developers.cloudflare.com/billing/manage/budget-alerts/ , https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/ , https://developers.cloudflare.com/billing/understand/billing-permissions/ , https://developers.cloudflare.com/billing/understand/preview-services/

**Most useful pages.**
https://developers.cloudflare.com/billing/understand/how-charges-accrue/ walks one request through DNS, TLS, cache, Argo, Workers, R2, Cache Reserve and Image Resizing and states that Cloudflare does not charge for bandwidth or origin egress.
https://developers.cloudflare.com/billing/troubleshoot/error-reference/ lists billing errors.

## Network

**What it is.**
Zone-level network settings, "Available on all plans", configured on the zone's **Network** page or via `PATCH /zones/{zone_id}/settings/{setting}`.
Source: https://developers.cloudflare.com/network/

| Setting | Plans | Key facts | Source |
| --- | --- | --- | --- |
| gRPC | All | Endpoint must listen on 443 with TLS and HTTP/2 over ALPN, proxied, SSL mode at least Full; WAF inspects headers only; Access does not support proxied gRPC; without gRPC enabled Cloudflare answers gRPC with 403 | https://developers.cloudflare.com/network/grpc-connections/ |
| IP geolocation | All | Adds `CF-IPCountry`; database updated multiple times per week; no accuracy SLA; corrections via form | https://developers.cloudflare.com/network/ip-geolocation/ |
| IPv6 compatibility | All (only Enterprise can turn it off) | On by default; Cloudflare prefers the IPv4 origin when both exist | https://developers.cloudflare.com/network/ipv6-compatibility/ |
| Onion Routing | All | Serves Tor users via `.onion` alt-svc without exit nodes | https://developers.cloudflare.com/network/onion-routing/ |
| Pseudo IPv4 | All | Class E addresses in `Cf-Pseudo-IPv4` or overwriting `Cf-Connecting-IP` and `X-Forwarded-For` | https://developers.cloudflare.com/network/pseudo-ipv4/ |
| True-Client-IP | Enterprise only | Prefer the Managed Transform | https://developers.cloudflare.com/network/true-client-ip-header/ |
| WebSockets | All | Only the upgrade request counts as a request; bandwidth counted Cloudflare to client; Argo not compatible; WAF inspects only the initial 101 request; idle connections are closed (custom idle timeout for Enterprise); deploys can terminate connections | https://developers.cloudflare.com/network/websockets/ |
| Maximum upload size | 100 MB Free and Pro, 200 MB Business, up to 5 GB Enterprise | Listed under Network but documented on the Cache page | https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits |

## Randomness Beacon (drand)

**What it is.**
drand (pronounced "dee-rand") is a distributed randomness beacon daemon written in Go; linked servers produce collective, publicly verifiable, unbiased, unpredictable random values at fixed intervals using bilinear pairings and threshold cryptography, intended as Internet infrastructure "similar to how NTP provides timing information".
The Cloudflare docs defer to drand.love for current user and operator documentation (https://drand.love/developer/ and https://drand.love/operator/).
All Cloudflare pages in this section were last updated Apr 24, 2026.
Source: https://developers.cloudflare.com/randomness-beacon/

**History and status.**
The protocol grew out of Yale and EPFL DEDIS research (IEEE S&P 2017), coding began in September 2017, and organisations including NIST, Cloudflare, Kudelski Security, the University of Chile and Protocol Labs formed a network; Protocol Labs took it to production in spring 2020 (drand v1.0).
Source: https://developers.cloudflare.com/randomness-beacon/about/background/
The docs call it production-ready since spring 2020 and list future goals of more partners, post-quantum public randomness and protocol standardization.
Source: https://developers.cloudflare.com/randomness-beacon/about/future/
Cloudflare co-founded the League of Entropy in 2019 with seven other organizations, contributes LavaRand entropy to it, and the League had grown to 18 organizations across four continents as of the March 2024 blog post.
Source: https://blog.cloudflare.com/harnessing-office-chaos/ (published 2024-03-08)

**Cryptography.**
Setup: a `t-of-n` distributed key generation (Pedersen DKG built on Feldman verifiable secret sharing over Shamir shares) gives each node a share of a collective private key that no node knows, plus the collective public key; resharing lets members join or leave while keeping the same public key.
Beacon: each round, nodes publish partial BLS signatures; any `t` valid partials recover the unique group signature via Lagrange interpolation, so fewer than `t` signers can neither predict nor bias it, and BLS determinism prevents forked values.
drand "currently uses" the BLS12-381 curve.
Chained beacons sign `H(r || sigma_{r-1})` (each value depends on all previous ones); unchained beacons sign `H(r)`, so messages are precomputable.
First-generation chains put signatures on G2 (96 bytes) and public keys on G1 (48 bytes); "G1/G2 swap" beacons put signatures on G1 for smaller signatures and a larger public key.
Sources: https://developers.cloudflare.com/randomness-beacon/cryptographic-background/setup-phase/ and https://developers.cloudflare.com/randomness-beacon/cryptographic-background/randomness-generation/

**Using Cloudflare's endpoint (from the blog, not the docs).**
Cloudflare serves mainnet beacons at `https://drand.cloudflare.com`; `https://drand.cloudflare.com/chains` lists all beacons its nodes support.
The quicknet beacon has chain hash `52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971`, `period: 3` seconds, `genesis_time: 1692803367`, `schemeID: bls-unchained-g1-rfc9380`, and its group info is at `/{chainhash}/info`.
A round is fetched at `/{chainhash}/public/{round}` (or `/public/latest`) and returns `round`, `randomness` (the SHA-256 of the signature) and `signature`.
The randomness is unpredictable as long as a threshold (at least a majority, configurable higher) of nodes is honest and does not collude, and anyone can verify a round with the group public key; Cloudflare recommends verifying every value with the drand client libraries or CLI.
Unchained randomness (introduced by drand in 2022, used by quicknet) lets clients verify any round with only the round number and group public key, without following the chain, and enables timelock encryption (tlock): encrypt to a future round, and anyone can decrypt once that round's signature is published.
Each round maps to a timestamp of roughly genesis plus round times period, "modulo small delays".
Cloudflare published a demo tlock Worker (`https://tlock-worker.crypto-team.workers.dev`, source https://github.com/thibmeu/tlock-worker).
Public randomness "should not be used for generating cryptographic keys"; for private randomness the post points to `crypto.getRandomValues` in Workers.
Source: https://blog.cloudflare.com/harnessing-office-chaos/

**LavaRand context.**
LavaRand mixes camera images of lava lamps (San Francisco), double pendulums (London), rainbow mobiles (Austin) and, since March 2025, 50 wave machines (Lisbon) into a KDF-seeded CSPRNG exposed by an internal API; per the 2025 post, part of `Math.random()` randomness in Workers and Cloudflare's drand API both draw on it.
Sources: https://blog.cloudflare.com/harnessing-office-chaos/ and https://blog.cloudflare.com/chaos-in-cloudflare-lisbon-office-securing-the-internet-with-wave-motion/ (published 2025-03-17)
A September 2025 post adds that quantum random number generators are not needed against quantum attacks, since a CSPRNG with a secret seed is what matters.
Source: https://blog.cloudflare.com/you-dont-need-quantum-hardware/

**Pricing, limits, SLA.**
None of the mirrored Cloudflare pages state pricing, rate limits, an SLA or plan availability for `drand.cloudflare.com`.

**Most useful pages.**
https://developers.cloudflare.com/randomness-beacon/cryptographic-background/randomness-generation/ , https://blog.cloudflare.com/harnessing-office-chaos/ , https://drand.love/developer/

## Time Services

**What it is.**
Free time services on Cloudflare's anycast network at `time.cloudflare.com`: NTP, NTS and Roughtime, governed by Cloudflare's Website and Online Services Terms of Use.
Sources: https://developers.cloudflare.com/time-services/ and https://developers.cloudflare.com/time-services/tos/

**NTP.**
Point clients at `time.cloudflare.com` (chrony and ntpd `server time.cloudflare.com iburst`, systemd-timesyncd `NTP=time.cloudflare.com`); Cloudflare's servers are also in `pool.ntp.org` at 162.159.200.1, 162.159.200.123, 2606:4700:f1::1 and 2606:4700:f1::123.
Cloudflare does not leap-smear, and mixing smearing and non-smearing servers "may lead to unpredictable and anomalous results".
Sources: https://developers.cloudflare.com/time-services/ntp/ and https://developers.cloudflare.com/time-services/ntp/usage/

**NTS.**
Network Time Security (RFC 8915) authenticates NTP: a TLS key exchange, then authenticated NTPv4 extension fields; supported clients include Chrony, NTPsec and ntpd-rs.
Source: https://developers.cloudflare.com/time-services/nts/

**Roughtime (beta).**
Authenticated "accurate, not precise" time (for example within 10 seconds) over UDP at `roughtime.cloudflare.com:2003` with Ed25519 public key `0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=`, also published in a DNS TXT record; the root key "may change" during the beta.
The old server `roughtime.cloudflare.com:2002` and its key were deprecated on 2024-06-30.
Responses are signed via a root-key delegation to an online key, chaining queries across servers produces a cryptographic proof of ordering, and Cloudflare's Go package is at https://github.com/cloudflare/roughtime.
Sources: https://developers.cloudflare.com/time-services/roughtime/usage/ , https://developers.cloudflare.com/time-services/roughtime/recipes/ , https://developers.cloudflare.com/time-services/roughtime/deprecation/

## Radar

**What it is.**
A public hub of Internet traffic, attack and technology trends built from Cloudflare's network and anonymized 1.1.1.1 resolver data, "Available on all plans", with a free API at `https://api.cloudflare.com/client/v4/radar/`.
Data from the Radar API is licensed CC BY-NC 4.0.
An MCP server and Python notebooks are linked.
Source: https://developers.cloudflare.com/radar/

**API access.**
Create a Custom Token with **Account > Radar > Read**; responses support `format=json` or `csv`.
Error codes: 2000 (500 internal), 2001 (400 validation), 2002 (422 "Query is above max cost"), 1015 (429 too many requests), 7003 (404).
No Radar-specific numeric rate limit is documented; the general API limits (1,200 requests per 5 minutes per user or token, 200 per second per IP) apply.
Sources: https://developers.cloudflare.com/radar/get-started/first-request/ , https://developers.cloudflare.com/radar/get-started/error-codes/ , https://developers.cloudflare.com/fundamentals/api/reference/limits/

**Concepts.**
Radar returns normalized values (`PERCENTAGE`, `PERCENTAGE_CHANGE`, `OVERLAPPED_PERCENTAGE`, `MIN_MAX`, `MIN0_MAX`, `RAW_VALUES`), so min-max data must be compared within one multi-series request.
Aggregation intervals are `15m`, `1h`, `1d`, `1w` (default 15 minutes for one day, one day for more than a month).
`meta.confidenceInfo.level` runs 1 to 5, with 5 meaning no known data quality issues.
Bot classes: `LIKELY_AUTOMATED` is bot score 1 to 29 and `LIKELY_HUMAN` is 30 to 99 (the default on the website).
Radar covers end-user traffic only unless stated (origin fetches excluded), and all timestamps are UTC.
Sources: https://developers.cloudflare.com/radar/concepts/normalization/ , https://developers.cloudflare.com/radar/concepts/aggregation-intervals/ , https://developers.cloudflare.com/radar/concepts/confidence-levels/ , https://developers.cloudflare.com/radar/concepts/bot-classes/ , https://developers.cloudflare.com/radar/get-started/making-comparisons/

**API surface.**
The mirrored OpenAPI index has 279 Radar endpoints: attacks (45), http (41), email (38), dns (25), bgp (19), as112 (19), ai (13), entities (9), ct (7), bots (7), ranking, quality, netflows and leaked_credential_checks (6 each), origins (5), tlds and annotations (4 each), traffic_anomalies, post_quantum and datasets (3 each), verified_bots, tcp_resets_timeouts, robots_txt and geolocations (2 each), search and agent_readiness (1 each).
Source: `raw/api/endpoints.tsv`; reference at https://developers.cloudflare.com/api/resources/radar/

**Investigate guides.**
Outages (`/radar/annotations/outages`) give location, ASN, type, scope, cause and start and end times.
Domain rankings come from 1.1.1.1 queries: an ordered daily top 100 (global and per country) and weekly unordered buckets from 200 to 1,000,000 domains via the datasets endpoints.
BGP anomaly APIs list origin hijacks (filter `minConfidence`) and provider-customer-provider route leaks, with a worked Worker plus Cron Trigger plus KV alerting example that "should work with a free-tier Cloudflare account".
NetFlows include all router traffic, not only CDN traffic.
Radar Alerts (anomaly, outage, route hijack, route leak by location or ASN) are delivered by email, webhook or PagerDuty and included on all plans.
Sources: https://developers.cloudflare.com/radar/investigate/outages/ , https://developers.cloudflare.com/radar/investigate/domain-ranking-datasets/ , https://developers.cloudflare.com/radar/investigate/bgp-anomalies/ , https://developers.cloudflare.com/radar/investigate/netflows/ , https://developers.cloudflare.com/radar/get-started/configure-alerts/

**URL Scanner.**
Available in Radar (https://radar.cloudflare.com/scan), the Security Center and the API at `/accounts/{account_id}/urlscanner/` (token **Account > URL Scanner > Edit**).
Scans default to Public visibility (listed in recent scans) or can be Unlisted; up to 100 URLs per bulk call; custom headers and user agents are allowed; poll results every 10 to 30 seconds (404 until done).
Reports include requests, cookies, console, globals, detected technologies, phishing verdicts, Radar rank, screenshot and DOM-structure hashes and certificates, and search uses an ElasticSearch-like query syntax.
Successful scans are kept 12 months and failed scans are deleted after 30 days; scanning from a chosen country is Enterprise-only.
Plan limits: Free or Radar keeps the last 50 scans, 5,000 public per month, no unlisted, 1 scan per 10 seconds; self-serve keeps 30 days, 5,000 public and 500 unlisted; Enterprise keeps 12 months, 10,000 public, 5,000 unlisted, 12 per second; Cloudforce One allows 75,000 public and 20,000 unlisted.
Sources: https://developers.cloudflare.com/radar/investigate/url-scanner/ and https://developers.cloudflare.com/security-center/investigate/scan-limits/

**Recent release notes.**
2026-08-07 AS-level connectivity and upstream provider widgets plus new BGP endpoints; 2026-05-29 TLS bug detection in the post-quantum checker; 2026-05-04 routing widgets and RPKI ROA timeseries; 2026-04-24 `signatureAgentUrl` for Web Bot Auth agents; 2026-03-06 region filtering and AS and location dimensions; 2026-02-27 Post-Quantum API and Key Transparency page; 2026-02-25 ASPA endpoints.
Source: https://developers.cloudflare.com/radar/release-notes/

## Resource Tagging

**What it is.**
Key-value metadata attached to Cloudflare resources for organization, access control and billing attribution, stored separately from the resources; "Available on all plans" and in **public beta** ("The API is stable, but behavior may change").
Source: https://developers.cloudflare.com/resource-tagging/

**Configuration.**
Account endpoints `/accounts/{account_id}/tags` (and `/tags/keys`, `/tags/values/{key}`, `/tags/resources`) and zone endpoints `/zones/{zone_id}/tags`; `PUT` replaces the full tag set (no `PATCH`), `DELETE` removes all tags, so single-tag edits use GET, merge, PUT.
Callers need Super Administrator, Workers Admin or Tag Admin, and Account Owned Tokens are recommended; the dashboard (Manage Account > Resource Tagging) is beta.
Filters: `tag=key`, `tag=key=value`, `tag=key=v1,v2` (OR, max 10), `tag=!key`, `tag=key!=value`, multiple `tag` params AND together (max 20); use `=` even though error 1007 still says `:`.
Account-level types include `account`, `worker`, `worker_version` (needs `worker_id`), `d1_database`, `kv_namespace`, `r2_bucket`, `queue`, `durable_object_namespace`, `vectorize_index`, `ai_gateway`, `pages_project`, `cloudflared_tunnel`, `load_balancer_pool`, `load_balancer_monitor`, `alerting_policy`, `alerting_webhook`, Access and Gateway objects, images and Stream objects; zone-level types include `zone`, `dns_record`, `custom_hostname`, `load_balancer`, `healthcheck`, `worker_route`, `zone_ruleset` and `access_application_policy` (needs `access_application_id`).
Sources: https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/ , https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/ , https://developers.cloudflare.com/resource-tagging/reference/resource-types/

**Limits (beta).**
10,000 tags per account, keys up to 256 characters (Unicode letters, digits, `_`, `.`, `-`, case-sensitive), values up to 1,024 characters, page size fixed at 100 with cursor pagination.
GET on a never-tagged resource returns `500` instead of `404`, a known beta limitation.
Sources: https://developers.cloudflare.com/resource-tagging/reference/limits/ and https://developers.cloudflare.com/resource-tagging/reference/error-codes/

## Tenant

**What it is.**
A provisioning API for Channel and Alliance partners (MSP, Agency and Enterprise reseller programs) to create and manage customer accounts, users, zones and subscriptions; a Tenant is a special account that contains other accounts, and Tenant admins become default Super Administrators of every contained account.
Sources: https://developers.cloudflare.com/tenant/ and https://developers.cloudflare.com/tenant/structure/

**Configuration.**
Requires a signed partner agreement, after which Cloudflare adds entitlements (contact `partners@cloudflare.com` or `agency@cloudflare.com`).
Create accounts with `POST /accounts` (`type` `standard` or `enterprise`, optional `unit.id` from `GET /user/tenants`, optional KYC fields up to 120 characters), list them with `GET /tenants/{tenant_id}/accounts`, invite members (Administrator role ID `05784afa30c1afe1440e79d9351c7430`) or create service users (not enabled by default), create zones, then add zone subscriptions (`POST /zones/{zone_id}/subscription`) and account subscriptions (`POST /accounts/{account_id}/subscriptions`), defaulting to monthly renewal.
Deleting an account deletes its zones but not Logpush jobs or Zero Trust Gateway configurations, which keep running unless deleted first.
Sample rate plans: `PARTNERS_FREE/PRO/BIZ/ENT` for resellers, `CF_FREE`, `CF_PRO_20_20`, `CF_BIZ` for agencies, `msp_biz` for MSPs; add-ons include `WAITING_ROOMS_BASIC`, `WAITING_ROOMS_ADV`, `WEB3_ETHEREUM_ENT`, `WEB3_IPFS_ENT` (and `_CONTRACT`, `_PAYGO` variants), `PARTNERS_WORKERS_ENT`, `WORKERS_PAID`, `PARTNERS_LOAD_BALANCING` and more; a missing entitlement returns error 1225.
Sources: https://developers.cloudflare.com/tenant/get-started/ , https://developers.cloudflare.com/tenant/how-to/manage-accounts/ , https://developers.cloudflare.com/tenant/reference/subscriptions/

## Version Management

**What it is.**
Enterprise-only zone configuration versioning with environments (Development, Staging, Production by default), promotion and rollback.
Source: https://developers.cloudflare.com/version-management/

**Key concepts.**
Enabling it creates Version Zero (the current config, always editable, restored if you disable versioning) and a Global Configuration holding unsupported settings, whose changes hit live traffic at once.
Environments are reached by traffic filters (Development: zone name plus an edge server IP plus cookie `development=true`; Staging: zone name plus edge IP; Production: zone name, not editable), versions are immutable and cannot be deleted, and promoting into a read-only environment (Production by default) makes the version permanently read-only.
Not versionable: DNS, Spectrum, Load Balancing, Waiting Rooms, Health Checks, Zero Trust and Access, SSL certificates, Snippets, Compression Rules and Client-side security.
Limitations include: Authenticated Origin Pull fails (520 from allowlisted IPs), Workers Cache API misbehaves, purging production purges all environments, China Network traffic always uses the root zone, Terraform is unsupported ("use either Terraform or Version Management"), Waiting Room users can lose their place and traffic may exceed limits, and Wrangler deploys can drop Worker routes in a version.
Requirements: Enterprise zone, active, WAF managed rules and custom rules (not Firewall Rules), new WAF, Super Administrator or Administrator with an API key and API access.
Changelog: Bot Management support (2023-09-20), API Shield no longer blocks enablement (2024-02-26), Cache Response Rules support (2026-04-27).
Sources: https://developers.cloudflare.com/version-management/about/ , https://developers.cloudflare.com/version-management/reference/available-configurations/ , https://developers.cloudflare.com/version-management/troubleshooting/ , https://developers.cloudflare.com/version-management/changelog/

## Privacy Pass

**What it is.**
An IETF standard (RFC 9576, 9577, 9578) that Cloudflare helped pioneer in 2017, letting users prove a claim (passed a CAPTCHA, of age, subscriber) without revealing an identifier or being tracked across requests.
Source: https://developers.cloudflare.com/privacy-pass/ (updated Jun 12, 2026)

**Key concepts.**
Four roles: Client, Origin (issues `WWW-Authenticate` token challenges and verifies tokens), Attester (deployment-specific verification) and Issuer (signs blinded requests; Cloudflare issuers use publicly verifiable Blind RSA, token type `2`).
Unlinkability depends on role separation and on a large anonymity set.
Deployments include Apple Private Access Tokens (fully split; Apple attests, Cloudflare and Fastly issue) and attribute attestation (joint Attester-Issuer run by Cloudflare); Privacy Pass is also a signal in Turnstile and the auth layer for Privacy Proxy and OHTTP Relay.
Rate limiting with tokens is listed as "still in development" (batched tokens, ARC and reverse-flow drafts).
Sources: https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/ and https://developers.cloudflare.com/privacy-pass/concepts/deployment-models/

**Availability.**
Not self-serve: a production deployment is a managed engagement; Cloudflare provisions an issuer with `/.well-known/private-token-issuer-directory` and `/token-request`, and you run the Attester (mTLS client certificate to the issuer; reference Workers attester using Turnstile at https://github.com/cloudflare/privacypass-attester).
A demo issuer and browser tool are open for testing (https://privacypass-demo.cloudflare.app/ with directory `https://demo-pat.issuer.cloudflare.com/.well-known/private-token-issuer-directory`), and `@cloudflare/privacypass-ts` runs the full flow locally.
Sources: https://developers.cloudflare.com/privacy-pass/getting-started/ and https://developers.cloudflare.com/privacy-pass/production-deployment-testing/

## Privacy Proxy

**What it is.**
An Enterprise-only managed MASQUE forward proxy (HTTP CONNECT for TCP, CONNECT-UDP for UDP, over HTTP/2 or HTTP/3) that hides client IPs while preserving geolocation; it powers Microsoft Edge Secure Network (single-hop) and is the second hop of iCloud Private Relay (double-hop).
Source: https://developers.cloudflare.com/privacy-proxy/ (updated Oct 2, 2026)

**Key concepts.**
Authentication via `Proxy-Authorization`: pre-shared key (testing only, linkable), Privacy Pass `PrivateToken` (production) or mTLS (server to server).
Geolocation via `sec-ch-geohash: <geohash>-<country>` (typically 4 to 5 characters), choosing egress IPs from pools in hundreds of cities, with better precision over IPv6.
Double-hop splits identity (your Proxy A) from destination (Cloudflare Proxy B).
Observability: four GraphQL nodes (`privacyProxyRequestMetricsAdaptiveGroups`, ingress, egress and auth), aggregate and sampled only, plus OTLP export with traces sampled at about 1%, and a `Server-Timing: proxy;dur=` header; observability excludes user IPs and tokens.
Sources: https://developers.cloudflare.com/privacy-proxy/concepts/authentication/ , https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/ , https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/ , https://developers.cloudflare.com/privacy-proxy/reference/metrics/opentelemetry/

## Cloudflare OHTTP Relay

**What it is.**
Formerly Privacy Gateway; an Enterprise-only, closed-beta managed relay implementing Oblivious HTTP so an application backend never sees client IPs and the relay never sees request content.
You run the application gateway (sample Go server at https://github.com/cloudflare/privacy-gateway-server-go) and client, and Cloudflare relays at `https://privacy-relay.cloudflare.com/<GATEWAY_SERVER_NAME>`.
Cloudflare sees the client IP, the target service and request metadata, and keeps these logs about 124 days.
Cache, WAF content rules and API Shield schema validation or discovery are incompatible because traffic is end-to-end encrypted.
Metrics come from GraphQL nodes `ohttpMetricsAdaptive` and `ohttpMetricsAdaptiveGroups`.
Sources: https://developers.cloudflare.com/ohttp-relay/ , https://developers.cloudflare.com/ohttp-relay/get-started/ , https://developers.cloudflare.com/ohttp-relay/reference/legal/ , https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/ , https://developers.cloudflare.com/ohttp-relay/reference/metrics/

## Style Guide

The Style Guide (156 pages) tells contributors how to write, structure and build Cloudflare docs and dashboard content, and is irrelevant to building products: https://developers.cloudflare.com/style-guide/

## Pointers: Security Center and docs folders outside llms.txt

Security Center is in the sidebar (Application Security) and belongs to that file; it is noted here only because it hosts the URL Scanner, Investigate, Brand Protection (beta), Security Insights (scans every 7 days on Free, Pro and Business, every 3 days on Enterprise) and Threat Intelligence APIs (100 calls per month on Free, Pro and Business, 2,500 on Enterprise).
Sources: https://developers.cloudflare.com/security-center/ and https://developers.cloudflare.com/security-center/intel-apis/limits/
The mirror also holds folders that are not products in llms.txt: `glossary/` (a term table across products), `videos/` (31 video pages), `sponsorships/` (open-source projects Cloudflare sponsors), `contributors/`, `directory/`, `resources/`, `use-cases/`, `changelog/` and `api/`.

## Build hooks for Web3 projects

These are concrete uses for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (EVM L2, chain id 4663).
Statements marked "(inference)" are this knowledge base's reasoning from the cited facts, not Cloudflare claims.

**Randomness for raffles, allowlist draws and NFT reveals (drand).**
Use quicknet (3-second rounds, unchained, `bls-unchained-g1-rfc9380`) for publicly verifiable draws: publish the target round number before it is produced, then derive the winner from that round's `randomness`, so anyone can re-verify with the group public key.
Because unchained rounds are signatures over the round number only, a verifier needs just the round number and the public key, not the whole chain.
Limits for on-chain use: the value is unpredictable only while a threshold of League of Entropy members stays honest and non-colluding; it must be verified on every use; and it is public the moment it is produced, so a contract must commit to a future round before that round exists (inference).
On-chain BLS12-381 verification cost and support on Solana, Ethereum, Base or chain 4663 are not covered by these sources, so an oracle or off-chain verifier design needs separate research (inference).
Cloudflare documents no SLA, rate limit or price for `drand.cloudflare.com`, so a production dapp should be able to fall back to other League endpoints listed by drand.love (inference).
Never use drand output as a private key or secret; use `crypto.getRandomValues` in a Worker for secrets.

**Timelock reveals (tlock).**
Encrypt sealed bids, blind-auction orders or launch parameters to a future quicknet round so they open automatically for everyone at a known time, as Cloudflare's tlock Worker demo does.

**Edge-side sampling and canaries.**
Use `hash_in_range(0, 100, cf.random_seed) < N` in Rules to send N% of trading-UI traffic to a new RPC backend (with an Origin Rule, Enterprise for Host or DNS override) or to tag requests for logging; this is load splitting, not fair on-chain randomness, and the hash algorithm can change without notice.
`uuidv4(cf.random_seed)` in a request header Transform Rule gives each request a correlation ID for RPC-proxy logs.

**RPC proxy and API hygiene with Rules and Snippets.**
Use Snippets (Pro and above, 5 ms, 2 MB, 32 KB, 2 to 5 subrequests) for HMAC-signed requests, JWT checks or pre-shared-key headers in front of a private RPC or token-list API, then strip internal headers with Response Header Transform Rules.
Use Single Redirects and Bulk Redirects (up to 10,000 URLs on Free) to retire old launchpad or mint URLs, and Custom Errors (paid plans) for a branded "sale paused" page instead of raw 5xx during launch incidents.
Use Configuration Rules to switch off Rocket Loader or Email Obfuscation on wallet-connect pages where script rewriting can break wallet injection (inference), and Cloud Connector (beta) to serve token metadata or NFT images from an R2 or S3 bucket under your domain.
Validate every rules change with `dry_run=true` before a launch.

**WebSockets and gRPC for live prices.**
WebSockets are on for all plans but are not compatible with Argo, are only WAF-inspected at the upgrade, close on idle and can be cut by Cloudflare deploys, so trading UIs need heartbeats and reconnect logic.
gRPC needs port 443, TLS, HTTP/2 and SSL mode Full, and Access does not protect proxied gRPC.

**Paying Cloudflare in USDC.**
A Web3 team can pay Cloudflare plans and usage in USDC on Base or Polygon with MetaMask, Phantom or Coinbase Wallet; payments are final with no chargebacks, the permit covers future renewals and threshold charges, and a card on file is the fallback.
Revoking the permit stops future charges and puts subscriptions into dunning, so treasury wallets must hold enough USDC through usage spikes such as launch days.
Robinhood Chain and Solana USDC are not listed as supported networks.

**Cost control around launches.**
Set a budget alert and per-product usage notifications before a mint, because threshold billing can raise a mid-cycle invoice and budget alerts never cap spend.
Contracted customers can trial Waiting Room, Load Balancing, Web3 gateways and Workers as 30-day preview services.

**Monitoring and phishing defence (Radar and URL Scanner).**
Use Radar outage and BGP hijack or leak alerts (all plans; email, webhook, PagerDuty) for the ASNs and countries hosting your RPC nodes and validators.
Use URL Scanner to screen lookalike mint or claim sites (phishing verdicts, favicon and DOM hashes, similar screenshots) and Security Center Brand Protection for impersonating domains.
Radar data is CC BY-NC 4.0, so showing Radar charts or rankings inside a commercial trading product may need separate permission (inference from the license).

**Time.**
Use NTS or Roughtime (`roughtime.cloudflare.com:2003`) to sanity-check server clocks on keepers, bots and sale schedulers that compare wall-clock time with block timestamps; Roughtime is still beta and its key may change.

**Multi-tenant launchpads.**
Resource Tagging (beta, 10,000 tags per account) can label Workers, D1, KV, R2 and DNS records per token project or customer for cost attribution; the Tenant API applies only if you sign a Cloudflare partner agreement; Version Management is Enterprise-only and conflicts with Terraform and with Waiting Room queues.

**Privacy-preserving gating.**
Privacy Pass, Privacy Proxy and OHTTP Relay are managed or Enterprise-only engagements, but Privacy Pass tokens (already a Turnstile signal) are the documented route to prove "passed a check" or "is a subscriber" without linking wallet sessions (inference for the wallet use case).

## Gaps and contradictions

- **Billing payment-method lists omit crypto.** The Billing overview and Billing policy list cards, PayPal, Apple Pay, Google Pay, Stripe Link and UnionPay only, and the Payment methods index does not link the Stablecoin payments page, which says USDC is selectable at checkout (https://developers.cloudflare.com/billing/ , https://developers.cloudflare.com/billing/understand/billing-policy/ , https://developers.cloudflare.com/billing/payment-methods/ versus https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/).
- **Threshold billing wording.** Threshold billing "fires once per account" and then returns to end-of-cycle billing, while the stablecoin page says the permit covers "usage-based charges billed at threshold for Workers, R2, and Stream" as a recurring item (https://developers.cloudflare.com/billing/threshold-billing/ versus the stablecoin page).
- **Number of payment methods.** The Billing FAQ says "You can add up to two payment methods", while the auto-retry page says all additional methods are tried in sequence and "the more payment methods you have on file, the more chances" (https://developers.cloudflare.com/billing/understand/faq/ versus https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/).
- **Add-on billing period.** Billing policy says add-on services "are billed monthly only", while How billing works describes separate monthly and annual subscription cycles (https://developers.cloudflare.com/billing/understand/billing-policy/ versus https://developers.cloudflare.com/billing/understand/how-billing-works/).
- **Who can change plans.** Change domain plan says "Only Super Administrators can manage changes to domain plans", while Billing permissions lets the Administrator role change or cancel subscriptions (https://developers.cloudflare.com/billing/manage/change-plan/ versus https://developers.cloudflare.com/billing/understand/billing-permissions/).
- **Page Rules status.** llms.txt and the page description say Page Rules are deprecated, but the Page Rules page body has no deprecation notice or date and still shows quotas for every plan (https://developers.cloudflare.com/rules/page-rules/).
- **Rules order versus phases list.** The Rules execution order lists Bulk Redirects directly after Origin Rules and omits URL normalization, while the phases list puts `http_request_sanitize` (URL normalization) between Single Redirects and URL rewrites and places WAF, rate limiting, Super Bot Fight Mode and Access checks between Origin Rules and Bulk Redirects (https://developers.cloudflare.com/rules/snippets/#execution-order versus https://developers.cloudflare.com/ruleset-engine/reference/phases-list/).
- **Version Management API.** Requirements say "You must use the dashboard to manage versioning", while the Cloudflare API limitation says environments, routing expressions and version assignments can be managed through the public Environments API, and the disable procedure itself uses API calls (https://developers.cloudflare.com/version-management/).
- **Version Management Production environment.** About says Production cannot be deleted and has read-only enabled, while Read-only environments says you can change that by editing the environment and the disable procedure says "When deleting the production environment, all traffic will default to Version 0" (https://developers.cloudflare.com/version-management/about/ , https://developers.cloudflare.com/version-management/reference/read-only-environments/ , https://developers.cloudflare.com/version-management/how-to/enable/).
- **Privacy Proxy auth privacy levels.** The authentication table rates mTLS privacy "Higher" than Privacy Pass ("High"), while the mTLS section says certificates identify the client and reduce privacy compared to Privacy Pass (https://developers.cloudflare.com/privacy-proxy/concepts/authentication/).
- **Privacy Proxy `proxyStatus` empty value.** The GraphQL page says `proxyStatus` is `null` when no proxy error occurred, and the proxy status reference says it is an empty string (https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/ versus https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/).
- **Privacy Proxy geohash length.** The geolocation page says typically four to five characters, while the HTTP headers page says typically 4 to 8 and shows an 11-character example (https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/ versus https://developers.cloudflare.com/privacy-proxy/reference/http-headers/).
- **What OHTTP Relay learns.** The overview says the relay learns nothing "beyond the length of the encrypted message and the server", while the legal page says Cloudflare sees the client IP plus browser type, OS, hardware configuration and timestamps; the docs also cite OHTTP Internet-Drafts (`draft-thomson-http-oblivious-01`, `draft-ietf-ohai-ohttp-05`) rather than a final RFC (https://developers.cloudflare.com/ohttp-relay/ versus https://developers.cloudflare.com/ohttp-relay/reference/legal/).
- **Resource Tagging availability and auth.** The overview says "Available on all plans", while Get started says a 403 mentioning a feature gate means tagging is not enabled and you must contact support; the overview says authentication uses Account Owned Tokens, while Manage tags also accepts user API tokens (https://developers.cloudflare.com/resource-tagging/ , https://developers.cloudflare.com/resource-tagging/get-started/ , https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/).
- **drand curve and staleness.** The randomness generation page says drand uses BLS12-381, while the background page says Cloudflare's BN256 implementation "is now integrated in both Kyber and drand"; the background page also says "there is no service deployed" and the only option is NIST's prototype, which predates the production network it describes later on the same page (https://developers.cloudflare.com/randomness-beacon/cryptographic-background/randomness-generation/ versus https://developers.cloudflare.com/randomness-beacon/about/background/).
- **drand docs gap.** The Cloudflare user and operator guides are one-line redirects to drand.love; the endpoint `drand.cloudflare.com`, the quicknet parameters, verification steps and any SLA appear only in a 2024 blog post, and the League size (18 organizations) is a 2024 figure not refreshed in the docs.
- **Radar rate limits.** Radar documents error 1015 (429) and 2002 (query above max cost) but gives no numeric limit or cost model for its API.
- **True-Client-IP link.** The True-Client-IP page links "retrieve it from the True-Client-IP header" to the `#cf-ipcountry` anchor (https://developers.cloudflare.com/network/true-client-ip-header/).
- **WebSocket idle timeout.** The WebSockets page says idle connections are closed "for a period of time" but does not state the value (https://developers.cloudflare.com/network/websockets/).
- **Sidebar oddities.** The sidebar's "Page Shield" entry points to `/page-shield/`, which has no folder in the mirror (the product is now Client-side security), and "Email Routing" points to `/email-service/` (`raw/nav/home-sidebar.md`).
- **Tenant auth style.** Tenant guides use the legacy `X-Auth-Email` and `X-Auth-Key` global API key for account calls but bearer tokens for subscription calls, without explaining when each is required (https://developers.cloudflare.com/tenant/get-started/).
