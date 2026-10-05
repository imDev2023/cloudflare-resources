# Protect & Connect > Delivery & Performance

This file covers the six products in the docs sidebar under Protect & Connect > Delivery & Performance (Cache/CDN, Speed, Load Balancing, Waiting Room, Argo Smart Routing, Zaraz) plus four application-performance products that are listed in `raw/docs/llms.txt` but not in the sidebar (Automatic Platform Optimization, China Network, Google tag gateway for advertisers, Smart Shield).
Cache is available on every plan and is configured mainly through Cache Rules, Cache Response Rules, origin `Cache-Control`/`CDN-Cache-Control` headers and Workers; purge, invalidation (new on 2026-09-28), Tiered Cache and the R2-backed Cache Reserve control freshness and origin load.
Smart Shield is now the umbrella for origin-protection features (Smart Tiered Cache, connection reuse, Argo, Regional Tiered Cache, Cache Reserve, Health Checks, Dedicated CDN Egress IPs), so several older Cache and Argo pages carry a "now offered as part of Smart Shield" banner.
Load Balancing and Argo are paid add-ons with usage metering, Waiting Room is Business and Enterprise only (advanced features need the Enterprise Advanced Waiting Room add-on), Zaraz is free up to 1,000,000 events per account per month, Google tag gateway is free, and China Network is a separate Enterprise subscription operated with JD Cloud.
Everything below is taken from the mirror of developers.cloudflare.com made on 2026-10-05 and is dated "as of 2026-10-05" wherever it can move.

## Table of contents

1. [Sources and scope](#1-sources-and-scope)
2. [Cache / CDN](#2-cache--cdn)
3. [Speed](#3-speed)
4. [Load Balancing](#4-load-balancing)
5. [Waiting Room](#5-waiting-room)
6. [Argo Smart Routing](#6-argo-smart-routing)
7. [Smart Shield](#7-smart-shield)
8. [Zaraz](#8-zaraz)
9. [Automatic Platform Optimization (APO)](#9-automatic-platform-optimization-apo)
10. [China Network](#10-china-network)
11. [Google tag gateway for advertisers](#11-google-tag-gateway-for-advertisers)
12. [Plan availability cheat sheet](#12-plan-availability-cheat-sheet)
13. [Build hooks for Web3 projects](#13-build-hooks-for-web3-projects)
14. [Gaps and contradictions](#14-gaps-and-contradictions)

---

## 1. Sources and scope

- Raw sources: `raw/docs/cache/`, `raw/docs/speed/`, `raw/docs/load-balancing/`, `raw/docs/waiting-room/`, `raw/docs/argo-smart-routing/`, `raw/docs/zaraz/`, `raw/docs/automatic-platform-optimization/`, `raw/docs/china-network/`, `raw/docs/google-tag-gateway/`, `raw/docs/smart-shield/`, plus `raw/api/openapi.json` for Waiting Room and Load Balancing schema details, `raw/docs/billing/` for invoice examples, and `raw/blog/` and `raw/external/` for Web3 context.
- Page counts in the mirror (as of 2026-10-05): Cache 91, Speed 43, Load Balancing 63, Waiting Room 30, Argo Smart Routing 4, Zaraz 50, APO 16, China Network 11, Google tag gateway 1, Smart Shield 23.
- Every overview, get-started, concepts, limits, plans and pricing page was read; the remaining titles were skimmed from each product's `llms.txt`.
- Sidebar position: Protect & Connect > Delivery & Performance lists Cache, Speed, Load Balancing, Waiting Room, Argo Smart Routing and Zaraz (`raw/nav/home-sidebar.md`).
- In `raw/docs/llms.txt` all ten products sit in the "Application performance" group, except Zaraz which sits in "Developer platform".
- Health Checks (standalone) is in the Manage & Observe sidebar and is covered in `manage-observe.md`; it appears here only where Load Balancing and Smart Shield reference it.

---

## 2. Cache / CDN

### 2.1 What it is

- Cache stores copies of frequently accessed content in data centers close to users, reducing origin load; it is "Available on all plans" ([overview](https://developers.cloudflare.com/cache/)).
- Static content is cached by default by file extension; dynamic content such as HTML is not cached by default but can be cached with Cache Rules ([get started](https://developers.cloudflare.com/cache/get-started/)).
- Cloudflare only caches resources within the data center that serves the request, does not cache off-site or third-party resources, and does not cache content on DNS-only (unproxied) records ([get started](https://developers.cloudflare.com/cache/get-started/)).
- Since 2026-05-04 the changelog states that Pingora now powers Cloudflare's cache ([changelog](https://developers.cloudflare.com/cache/changelog/)).

### 2.2 Default cache behavior

Source: [Default cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/).

- Cloudflare does not cache a resource when `Cache-Control` is `private`, `no-store`, `no-cache` or `max-age=0`, when a `Set-Cookie` header exists, or when the method is anything other than `GET`.
- Cloudflare does cache when `Cache-Control` is `public` with `max-age` greater than 0, or when `Expires` is in the future; if both `max-age` and `Expires` are set, `max-age` wins.
- Caching is decided by file extension, not MIME type, and the CDN "does not cache HTML or JSON by default"; `robots.txt` is cached by default.
- Default cached extensions: 7Z, AVI, AVIF, APK, BIN, BMP, BZ2, CLASS, CSS, CSV, DOC, DOCX, DMG, EJS, EOT, EPS, EXE, FLAC, GIF, GZ, ICO, ISO, JAR, JPG, JPEG, JS, MID, MIDI, MKV, MP3, MP4, OGG, OTF, PDF, PICT, PLS, PNG, PPT, PPTX, PS, RAR, SVG, SVGZ, SWF, TAR, TIF, TIFF, TTF, WEBM, WEBP, WOFF, WOFF2, XLS, XLSX, ZIP, ZST.
- Default edge TTL when no `cache-control` or `expires` is present: 200, 206, 301 cached 120 minutes; 302, 303 cached 20 minutes; 404, 410 cached 3 minutes; all other status codes not cached.
- Request collapsing: when many requests for the same uncached asset arrive at one data center, a cache lock forwards only the first to the origin and streams the response to the waiting requests.
- If Cloudflare has started fetching from the origin, it keeps fetching and caching even if the visitor disconnects; if the visitor disconnects before the origin responds, nothing is cached.

Upload and cacheable size limits (as of 2026-10-05):

| | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Max upload size | 100 MB | 100 MB | 200 MB | Up to 5 GB (self-serve), more via account team |
| Max cacheable file size | 512 MB | 512 MB | 512 MB | 5 GB default, increase on request |

- Request bodies on `GET` are cached as part of the response context but are not part of the cache key, and should be treated as untrusted ([Avoid web cache poisoning](https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/)).

### 2.3 Origin headers: Cache-Control, CDN-Cache-Control and Origin Cache Control

- `CDN-Cache-Control` and `Cloudflare-CDN-Cache-Control` let the origin control CDN caching separately from browsers; precedence is `Cloudflare-CDN-Cache-Control` > `CDN-Cache-Control` > `Cache-Control` ([CDN-Cache-Control](https://developers.cloudflare.com/cache/concepts/cdn-cache-control/), [cache responses](https://developers.cloudflare.com/cache/concepts/cache-responses/)).
- `CDN-Cache-Control` is proxied downstream; `Cloudflare-CDN-Cache-Control` is not proxied downstream.
- If a Cache Response Rule sets `Cache-Control` directives with `set_cache_control`, those take precedence over origin `Cloudflare-CDN-Cache-Control` and `CDN-Cache-Control`.
- A present `Surrogate-Control` header makes Cloudflare ignore `Cache-Control` directives.
- The Edge Cache TTL cache rule overrides `CDN-Cache-Control` edge directives; the Browser Cache TTL rule only modifies `Cache-Control` and leaves `CDN-Cache-Control` alone.
- Origin Cache Control (strict RFC 7234 behaviour) is always on for Free, Pro and Business and cannot be disabled there; Enterprise can choose, and the cache-responses page says it is disabled by default on Enterprise ([Cache Rules settings](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/), [cache responses](https://developers.cloudflare.com/cache/concepts/cache-responses/)).
- With Origin Cache Control on, a request with an `Authorization` header is cacheable only if `Cache-Control` also includes `public`, `s-maxage` or `must-revalidate`.

### 2.4 `CF-Cache-Status` values

Source: [Cloudflare cache responses](https://developers.cloudflare.com/cache/concepts/cache-responses/).

| Status | Meaning |
| --- | --- |
| `HIT` | Found in cache. |
| `MISS` | Eligible for cache but not in cache; served from origin. |
| `NONE/UNKNOWN` | Not eligible; for example a Worker responded without a subrequest, a WAF custom rule blocked, or a redirect rule or Always Use HTTPS redirected before cache. |
| `EXPIRED` | Found but expired, served from origin. |
| `STALE` | Expired, served from cache because the origin could not be contacted. |
| `BYPASS` | Eligible at request time but the origin response was not cacheable (size limit, `no-store`/`private`, `Set-Cookie`, `Vary: *`, `Authorization` rules, etc.). |
| `REVALIDATED` | Origin confirmed unchanged via a conditional request (synchronous path). |
| `UPDATING` | Expired but served from cache while revalidating in the background (asynchronous `stale-while-revalidate`). |
| `DYNAMIC` | Not eligible at request time (for example HTML or JSON without a rule, a Bypass cache rule, or Development Mode). |

- The changelog entry of 2026-05-26 ("BYPASS status now returned for uncacheable responses") moved uncacheable-origin-response cases from `DYNAMIC` to `BYPASS` ([changelog](https://developers.cloudflare.com/cache/changelog/)).
- The `Age` header is set on `HIT`, `STALE` and `UPDATING`, and with Tiered Cache it reflects the age in Cloudflare's network-wide cache.

### 2.5 Cache Rules

Sources: [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/), [settings](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/), [order](https://developers.cloudflare.com/cache/how-to/cache-rules/order/), [Page Rules migration](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

- Cache Rules decide what is eligible to cache, for how long and where; they can be created in the dashboard, via the Rulesets API or with Terraform, and require proxied DNS records.
- Rules can be versioned with Version Management.
- Number of rules per zone (as of 2026-10-05): Free 10, Pro 25, Business 50, Enterprise 300.
- Matching fields include URI, path, query, cookie, hostname, referer, SSL, user agent, X-Forwarded-For, request headers, cookie values and file extension; through the expression editor also `cf.bot_management.*` fields (need a Bot Management subscription) and `ip.src.asnum`.
- The `is in list` operators on Hostname are Enterprise only.
- Settings and their API names:
  - Cache eligibility: Bypass cache or Eligible for cache (`"cache": true`).
  - Edge TTL (`edge_ttl`): modes `respect_origin`, `override_origin`, `bypass_by_default`, plus per-status-code TTLs (`status_code_ttl`, where `0` means no-cache and `-1` means no-store).
  - Browser TTL (`browser_ttl`): `respect_origin`, `override_origin`, `bypass_by_default`.
  - Cache key (`cache_key`): `ignore_query_strings_order`, `cache_deception_armor`, `cache_by_device_type`, and `custom_key` (header, cookie, host, query_string, user); the custom query string, header, cookie, host and user options are Enterprise, with Ignore query string also available to pay-as-you-go customers.
  - Maximum of 100 query string parameters in a custom cache key; no explicit key length limit beyond request limits.
  - Cache Reserve eligibility (`cache_reserve` with `eligible` and `minimum_file_size`), requires a Cache Reserve plan.
  - Caching on port (`additional_cacheable_ports`, Enterprise only).
  - Proxy read timeout (`read_timeout`, Enterprise only), used to reduce 524 errors.
  - Serve stale while revalidating (`serve_stale.disable_stale_while_updating`).
  - Origin range requests (`origin_range_requests.mode` on/off/default, added to the Rulesets API on 2026-09-02); not supported by Cache Reserve.
  - Respect strong ETags (`respect_strong_etags`).
  - Origin error page pass-through (`origin_error_page_passthru`).
  - Origin Cache Control (`origin_cache_control`, Enterprise only).
  - Vary (`vary`, added 2026-07-02): per-header actions `normalize`, `passthrough`, `bypass`; up to 50 header entries, `accept.media_types` up to 10, `accept-language.languages` up to 20, header names lowercase, no `cf-` prefix.
- Single-file purge from the dashboard may not work when a custom cache key includes headers or cookies, or when the rule matches only `GET` requests.
- Precedence: Workers settings override Cache Rules, which override Page Rules; within one level the last matching rule wins for conflicting settings ([Workers and Cache Rules](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/)).

### 2.6 Cache Response Rules

Source: [Cache Response Rules](https://developers.cloudflare.com/cache/how-to/cache-response-rules/).

- Announced 2026-03-24 and supporting zone versioning since 2026-04-27 ([changelog](https://developers.cloudflare.com/cache/changelog/)).
- They run in the `http_response_cache_settings` phase after the origin response arrives and before caching.
- They can modify origin `Cache-Control` directives, modify cache tags, and strip `ETag`, `Set-Cookie` and `Last-Modified` before caching; they apply to cached and non-cached responses.
- Cache Rules remain the only mechanism for eligibility, but a Cache Response Rule can make a cacheable asset non-cacheable with `no-store`; when the two conflict, Cache Response Rules win.
- Rules per zone: Free 10, Pro 25, Business 50, Enterprise 300 (as of 2026-10-05).

### 2.7 Cache keys, Vary and query strings

- The default cache key is the full URL (scheme, host, URI with query string), the client `Origin` header, the `x-http-method-override` family, and the `x-forwarded-host`, `x-host`, `x-forwarded-scheme`, `x-original-url`, `x-rewrite-url` and `forwarded` headers ([Cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/)).
- Custom cache keys give control but can shard the cache and lower hit rates; enabling "Normalize URLs to origin" is recommended alongside URL normalization.
- Caching levels: No Query String (API `basic`), Ignore Query String (API `simplified`), Standard (API `aggressive`, default) ([Caching levels](https://developers.cloudflare.com/cache/how-to/set-caching-levels/)).
- Vary in Cache Rules: when the origin sends `Vary`, listed request headers become part of the key according to the configured action; `Vary: *` always bypasses ([Vary](https://developers.cloudflare.com/cache/concepts/vary/)).
- Vary for images is a separate feature (Pro and above) that serves image format variants based on `Accept` ([Vary for images](https://developers.cloudflare.com/cache/advanced-configuration/vary-for-images/)).

### 2.8 Freshness, retention and revalidation

- Retention is how long an object stays before LRU eviction; it depends on popularity and cache size and is "not configurable" ([Retention vs Freshness](https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/)).
- Freshness (TTL) is set by origin headers, Cache Rules or Workers.
- Since 2026-02-26 revalidation with `stale-while-revalidate` is fully asynchronous: the first request after expiry gets stale content with `UPDATING` while the origin is contacted in the background ([Revalidation](https://developers.cloudflare.com/cache/concepts/revalidation/)).
- Stale serving during revalidation only happens if the origin sends `stale-while-revalidate`; `must-revalidate`, `proxy-revalidate`, `s-maxage` and `no-cache` disable it when Origin Cache Control is on.
- Minimum Edge Cache TTL by plan: Free 2 hours, Pro 1 hour, Business 1 second, Enterprise 1 second ([Edge and Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/)).
- Minimum Browser Cache TTL: 1 second on all plans, but 2 minutes (Free, Pro, Business) or 30 seconds (Enterprise) when set through Page Rules.
- Purging Cloudflare's cache does not affect assets stored in visitors' browsers.

### 2.9 Purge and invalidation

Sources: [Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/), [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/), [Purge by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

- Purge methods on every plan (since the 2025-04-03 changelog): single file (URL), hostname, cache tag, prefix, everything, plus cache-key resources, varied images and zone versions.
- A purge returns HTTP 200 when received; that does not confirm eviction, so verify that `CF-Cache-Status` is no longer `HIT`.
- Invalidation ("soft purge"), released 2026-09-28, uses the `invalidate_cache` endpoint with the same body as `purge_cache` (`files`, `tags`, `hosts`, `prefixes`, `purge_everything`); content is kept but marked stale, and an origin `304 Not Modified` lets Cloudflare reuse it.
- Invalidation needs the origin to send `ETag` or `Last-Modified` and support conditional requests; it does not affect Workers Cache, which is purged with `ctx.cache.purge()`.
- If the origin returns 5xx or is unreachable, invalidated content can be served stale for as long as it stays in cache unless `stale-if-error` limits it.
- Purge and invalidation share one set of per-account limits (as of 2026-10-05):

| Limit | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Hostname, tag, prefix, everything: request rate | 5 per minute | 5 per second | 10 per second | 50 per second |
| Token bucket size | 25 | 25 | 50 | 500 |
| Max operations per request | 100 | 100 | 100 | 100 |
| Single-file purge: URLs | 800 per second | 1,500 per second | 1,500 per second | 3,000 per second |
| Single-file purge: max operations per request | 100 | 100 | 100 | 500 |

- Limits are shared by all zones on the same plan in an account, and URL thresholds use a moving average.
- Cache tags come from the origin `Cache-Tag` response header, which Cloudflare strips before the visitor or a Worker sees it; tags are case-insensitive, contain no spaces, must be printable ASCII, and the aggregate header can be at most 16 KB (about 1,000 tags); an API purge tag can be at most 1,024 characters; the dashboard purges up to 100 tags at a time.
- With Tiered Cache, a purge by tag may produce `EXPIRED` instead of `MISS` as the lower tier revalidates with the upper tier.
- Purge events appear in Audit Logs since 2025-11-25.

### 2.10 Tiered Cache

Source: [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/).

- Tiered Cache splits data centers into lower and upper tiers; only upper tiers ask the origin, which raises hit ratios and concentrates origin connections in a few data centers.
- Topologies:
  - Smart Tiered Cache picks the single lowest-latency upper tier per origin (per Load Balancing pool when Load Balancing is used); since 2025-08-29 it falls back to Generic Global when the origin location cannot be determined.
  - Cloud region hints (AWS, GCP, Azure, Oracle Cloud), added 2026-04-17, let Smart Tiered Cache pick an upper tier for anycast or regional cloud origins; they are available on all plans at no cost.
  - Generic Global Tiered Cache uses a consistent hash of the cache key over regional upper-tier pools.
  - Regional Tiered Cache adds a regional hub between lower and upper tiers.
  - Custom Tiered Cache is configured with the account team.
- Availability (as of 2026-10-05): Tiered Cache and Smart topology on all plans; Generic Global, Regional and Custom topologies Enterprise only.
- Changing origin IPs or DNS while Smart Tiered Cache is on can move upper tiers and temporarily raise the `MISS` rate.
- Whether a request used Tiered Cache shows in the `CacheTieredFill` field of `http_requests` logs.
- The Workers Cache API (`caches.default.put/match`) only touches the local data center and does not use Tiered Cache, while `fetch()` subrequests do ([Workers and cache](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/)).
- Smart and Regional Tiered Cache now carry a Smart Shield banner (see section 7).

### 2.11 Cache Reserve

Source: [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/).

- Cache Reserve is a persistent cache implemented on R2 that acts as the ultimate upper tier; it is now also listed under Smart Shield.
- Retention starts at 30 days and resets each time the asset is requested.
- Eligibility: cacheable, freshness TTL of at least 10 hours, a `Content-Length` header; resized image variants are not eligible.
- Limits: R2 file limits apply on top of CDN limits; no Origin Range Requests; not compatible with Vary for images; not used for R2 public buckets linked to the zone; requests uncompressed content from the origin; bypassed in O2O setups.
- Since 2026-09-28 any purge forces a Cache Reserve miss (URL purge deletes, other purges leave the object billed until replaced or expired); invalidation keeps it and revalidates.
- Clearing all Cache Reserve data requires Cache Reserve to be off and can take up to 24 hours.
- Cache Reserve without Tiered Cache may raise operation costs, and the dashboard warns about it.
- Pricing (as of 2026-10-05), usage-based and requiring a paid plan:

| Item | Rate |
| --- | --- |
| Storage | $0.015 per GB-month |
| Class A operations (writes) | $4.50 per million |
| Class B operations (reads) | $0.36 per million |

- A Cache Reserve miss usually costs one Class A and one Class B operation; a hit costs one Class B; assets over 1 GB cost more operations; purge requests are free but invalidation can cause Class A operations.

### 2.12 Other cache features

| Feature | What it does | Availability (as of 2026-10-05) | Source |
| --- | --- | --- | --- |
| Always Online | When the origin is unreachable (not when it returns 5xx), serves pages archived by the Internet Archive; Cloudflare submits the most popular 200-status GET URLs of the last five hours. | All plans; crawl every 30 days (Free), 15 (Pro), 5 (Business, Enterprise). | [Always Online](https://developers.cloudflare.com/cache/how-to/always-online/) |
| Crawler Hints | Uses cache signals and IndexNow to tell search engines when content changed. | All plans. | [Crawler Hints](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/) |
| Early Hints | Caches and emits `103` responses with `Link` preload/preconnect headers for `.html`, `.htm`, `.php` or extensionless URIs on 200, 301, 302; HTTP/2 and HTTP/3 only; keyed by URI ignoring query strings. | All plans. | [Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/) |
| Development Mode | Suspends edge cache and Polish for three hours without purging. | All plans. | [Development Mode](https://developers.cloudflare.com/cache/reference/development-mode/) |
| Query String Sort | Sorts query parameters to improve hit rate. | Listed as a Cache Rules cache-key option. | [Query String Sort](https://developers.cloudflare.com/cache/advanced-configuration/query-string-sort/) |
| Cache Deception Armor | Protects against web cache deception. | Cache key option. | [Cache Deception Armor](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/) |
| Cache by device type | Adds device type to the cache key. | The get-started page labels it Enterprise only. | [Cache by device type](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-device-type/) |
| CSAM Scanning Tool | Scans cached content for CSAM. | Updated 2025-02-04. | [CSAM Scanning](https://developers.cloudflare.com/cache/reference/csam-scanning/) |
| Prefetch URLs | Pre-populates cache with URLs listed in a manifest. | Enterprise only. | [Prefetch URLs](https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/) |

- Features that rewrite cached copies at the edge: Rocket Loader, Polish, Hotlink Protection, Email address obfuscation and Bot Management JavaScript Detections ([get started](https://developers.cloudflare.com/cache/get-started/)).

### 2.13 Workers and cache

- A Worker sits in front of cache; `fetch()` subrequests go through cache and Tiered Cache and can be tuned with the `cf` object, while the Cache API works only on the local data center ([Workers and cache](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/)).
- The Cache API rejects `cache.put` for requests whose method is not `GET`, and `stale-while-revalidate` and `stale-if-error` are not supported by `cache.put` and `cache.match` ([Cache API](https://developers.cloudflare.com/workers/runtime-apis/cache/)).
- Workers override Cache Rules only with the right compatibility flags: `request_cf_overrides_cache_rules` (default for compatibility dates on or after 2025-04-02) for `fetch()`, and `cache_api_request_cf_overrides_cache_rules` (on or after 2025-05-19, needs `cache_api_compat_flags`) for the Cache API; without them the Worker's settings are silently ignored ([Workers and Cache Rules](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/)).
- "Workers Cache" is a separate cache in front of the Worker itself that returns cached responses without running the Worker.
- Snippets are an alternative for lightweight edits, included on all paid plans, limited to 5 ms execution and 32 KB package size.

### 2.14 Cache changelog highlights (2024-2026)

| Date | Change |
| --- | --- |
| 2026-09-28 | Invalidate instead of purge (`invalidate_cache`); purge now forces a Cache Reserve miss. |
| 2026-09-02 | Origin Range Requests configurable in the Rulesets API. |
| 2026-07-02 | Vary support in Cache Rules. |
| 2026-05-26 | `BYPASS` returned for uncacheable responses. |
| 2026-05-04 | Pingora now powers the cache. |
| 2026-04-27 | Cache Response Rules support zone versioning. |
| 2026-04-17 | Smart Tiered Cache cloud region hints for public cloud origins. |
| 2026-03-24 | Cache Response Rules. |
| 2026-02-26 | Asynchronous `stale-while-revalidate`. |
| 2025-11-25 | Audit Logs for purge events. |
| 2025-11-07 | Inspect cache keys with Cloudflare Trace. |
| 2025-08-29 | Smart Tiered Cache falls back to Generic. |
| 2025-04-04 | Workers `fetch()` can override Cache Rules. |
| 2025-04-03 | All purge methods available on all plans. |
| 2025-02-12 | Configurable HTTP/2 multiplexing to origin. |
| 2025-01-08 | Smart Tiered Cache optimizes Load Balancing pools. |

Source: [Cache changelog](https://developers.cloudflare.com/cache/changelog/).

### 2.15 Most useful Cache pages

- [Cache overview](https://developers.cloudflare.com/cache/) and [Get started](https://developers.cloudflare.com/cache/get-started/)
- [Default cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/)
- [Cache Rules settings](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/) and [Create via API](https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/)
- [Cache Response Rules](https://developers.cloudflare.com/cache/how-to/cache-response-rules/)
- [Cache responses (`CF-Cache-Status`)](https://developers.cloudflare.com/cache/concepts/cache-responses/)
- [Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/) and [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/)
- [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) and [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/)
- [Investigate uncached responses](https://developers.cloudflare.com/cache/troubleshooting/investigating-uncached-responses/)
- [Avoid web cache poisoning](https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/)
- [CDN reference architecture](https://developers.cloudflare.com/reference-architecture/architectures/cdn/)

---

## 3. Speed

### 3.1 What it is

- Speed assesses site performance and recommends Cloudflare products; it is "Available on all plans" and groups Observatory, Origin Analytics, optimization Settings and Aggregated Internet Measurement ([Speed](https://developers.cloudflare.com/speed/)).

### 3.2 Observatory

- Observatory combines synthetic tests and real user monitoring (RUM) and turns the results into recommendations; its `llms.txt` title is "Observatory (beta)" ([Observatory](https://developers.cloudflare.com/speed/observatory/)).
- Synthetic tests: a browser test runs Google Lighthouse in a headless browser; a network test breaks down network and back-end performance; two network tests can be compared side by side as histograms.
- RUM is enabled automatically for Free customers with EEA/UK/CH traffic excluded and can be switched off; other plans enable it as needed.
- Test quotas per month (as of 2026-10-05, "may change over time"): Pro 50 one-off and 5 recurring, Business 100 and 10, Enterprise 150 and 15, recurring tests daily ([Run test](https://developers.cloudflare.com/speed/observatory/run-speed-test/)).
- Tests can run from regions in the US, Europe and Asia (for example Iowa, Madrid, Tokyo, Singapore); IPv6 tests originate from ASN 15169 or 132892 and IPv4 tests from ASN 396982 with a `CloudflareObservatory/1.0` user agent.
- The RUM beacon is the Web Analytics JavaScript snippet, injected automatically on proxied sites or added manually ([RUM beacon](https://developers.cloudflare.com/speed/observatory/rum-beacon/)).

### 3.3 Origin Analytics

- Origin Analytics shows how the origin responds to Cloudflare from edge data, with no agent on the origin ([Origin Analytics](https://developers.cloudflare.com/speed/origin-analytics/)).
- Metrics: origin response time at p50, p95 and p99 with the zone's origin timeout as a reference line; origin status codes (`originResponseStatus`) next to edge status codes (`edgeResponseStatus`); and a top endpoints table ranked by p95, error rate, volume or TCP failure rate.
- An origin status of `0` means no HTTP response from the origin (connection failure, timeout, or served from cache or a Worker).
- It maps directly to 520, 522 and 524 diagnosis flows.

### 3.4 Optimization settings

| Feature | Summary | Availability / status (as of 2026-10-05) | Source |
| --- | --- | --- | --- |
| Speed Brain | Adds a `Speculation-Rules` header so Chromium 121+ prefetches likely next pages with conservative eagerness; prefetches only serve cached content, never reach the origin, skip routes that run Workers, and do not work on `pages.dev` or with strict CSP. | Enabled by default on Free; available on all plans; page mentions a beta phase. | [Speed Brain](https://developers.cloudflare.com/speed/optimization/content/speed-brain/) |
| Shared dictionaries | RFC 9842 delta compression (`dcb`/`dcz`) in passthrough mode; the origin builds dictionaries, Cloudflare forwards headers and varies cache. | All plans, beta. | [Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/) |
| Content compression | Gzip, Brotli and Zstandard to visitors; Brotli or Gzip from origin (`accept-encoding: br, gzip`); compresses only 200, 403 and 404 responses; Brotli and Zstandard need at least 50 bytes. | Default method: Zstandard on Free, Brotli on Pro and Business, Gzip on Enterprise. | [Compression](https://developers.cloudflare.com/speed/optimization/content/compression/) |
| Rocket Loader | Defers all JavaScript until after rendering. | All plans. | [Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/) |
| Cloudflare Fonts | Rewrites Google Fonts to be served from the site's own zone. | Google Fonts only. | [Fonts](https://developers.cloudflare.com/speed/optimization/content/fonts/) |
| Prefetch URLs | Prefetches URLs from a manifest into cache. | Enterprise only. | [Prefetch URLs](https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/) |
| Early Hints | See section 2.12. | All plans. | [Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/) |
| HTTP/2, HTTP/3 (QUIC) | Client to Cloudflare; HTTP/3 to origin is not supported. | All plans. | [HTTP/3](https://developers.cloudflare.com/speed/optimization/protocol/http3/) |
| HTTP/2 to Origin | On by default with multiplexing over long-lived connections. | All plans. | [HTTP/2 to Origin](https://developers.cloudflare.com/speed/optimization/protocol/http2-to-origin/) |
| 0-RTT Connection Resumption | Off by default; for GET, HEAD, OPTIONS only (not POST); adds `Early-Data: 1` to origin requests. | All plans. | [0-RTT](https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/) |
| Enhanced HTTP/2 Prioritization | Overrides browser resource ordering. | Pro and above. | [Enhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/) |
| Mirage | Mobile image lazy-loading. | Deprecated on 2025-09-15 and no longer available. | [Mirage](https://developers.cloudflare.com/speed/optimization/images/mirage/) |
| Auto Minify | Deprecated (see API deprecations of 2024-08-05); a page explains how to turn it off via `PATCH /zones/{zone_id}/settings/minify`. | Deprecated. | [Turn off Auto Minify](https://developers.cloudflare.com/speed/optimization/content/troubleshooting/disable-auto-minify/) |
| Polish, Image Resizing | Image optimization, documented under Images. | See Images docs. | [Polish](https://developers.cloudflare.com/images/polish/) |

- Aggregated Internet Measurement (AIM) scores latency, packet loss, download, upload, loaded latency and jitter into Bad/Poor/Average/Good/Great for streaming, gaming and real-time communication ([AIM](https://developers.cloudflare.com/speed/aim/)).
- The Recommendations tab can enable all recommended settings for the plan in one click ([Recommendations](https://developers.cloudflare.com/speed/optimization/recommendations/)).

---

## 4. Load Balancing

### 4.1 What it is and how it is sold

- Load Balancing distributes traffic across endpoints, with health monitoring, failover, intelligent steering, custom rules and analytics ([overview](https://developers.cloudflare.com/load-balancing/)).
- It is an "Add-on feature" for any account type and needs a billing profile; the overview points to the dashboard for pricing ([Enable](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/)).
- Enterprise customers can preview it as a non-contract service without metered fees.
- Billing docs (as of 2026-10-05) say DNS queries to load-balanced hostnames are metered with the first 500K included, and an example invoice shows "Basic Load Balancing" at $5.00 per month with sub-lines for pools, origins, health check intervals and regions ([Usage-based billing](https://developers.cloudflare.com/billing/understand/usage-based-billing/), [How billing works](https://developers.cloudflare.com/billing/understand/how-billing-works/)).
- Load balancing analytics are only on paid plans (Pro, Business, Enterprise) ([Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/)).

### 4.2 Components

Source: [Load Balancing components](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/).

- Load balancer: a public load balancer creates an LB DNS record for its hostname (the apex works too); private load balancers get a CGNAT or custom RFC 1918 IP instead of a hostname.
- Pool: a group of endpoints, often one pool per region.
- Endpoint: any origin, hostname, public or private IP, VIP or appliance.
- Monitor: issues health checks to the endpoints of a pool; monitors differ from standalone Health Checks.
- With Smart Tiered Cache, one upper tier is chosen per pool.

### 4.3 Proxy modes

Source: [Proxy status](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/).

- Layer 7 (proxied, orange cloud): hides endpoint IPs, fails over faster, integrates with cache, Workers and WAF, supports session affinity, endpoint drain and Private Network Load Balancing, and geolocates by the visitor's data center.
- DNS-only (grey cloud): returns endpoint IPs, exposes them, fails over at DNS cache speed, has no session affinity (use DNS persistence), geolocates by ECS or resolver, and is required for MX or SRV hostnames.
- Layer 4: only through Spectrum, without session affinity, custom rules or caching.

### 4.4 Traffic steering

Sources: [Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/), [steering policies](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/).

- Steering is decided by pool and endpoint health, pool sets, global steering (load balancer level) and local steering (pool level).
- Global policies:
  - Standard: Off (Failover by pool order, with fallback pool and automatic failback) and Random (optionally weighted via `random_steering`); these are "the only steering policies available to non-Enterprise customers who have not purchased Traffic steering" ([Standard](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/)).
  - Geo: pools per country or region, and per data center (PoP steering) for Enterprise via API only.
  - Dynamic: picks the pool with the lowest EWMA round-trip time from health probes; needs All Regions (or Enterprise All Data Centers) monitoring and about 10 minutes to build an RTT profile.
  - Proximity: routes to the nearest pool by geographic proximity.
  - Least Outstanding Requests: weights pools by in-flight requests; a no-op for DNS-only load balancers.
- EDNS Client Subnet support (`location_strategy` with `prefer_ecs` and `mode`) applies to DNS-only load balancers.
- Pool sets (announced 2026-08-31, API-managed) are an ordered, first-match list that supplies pools, a steering policy, weights and a per-location fallback pool, or returns a fixed HTTP response ([Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/)).
- Endpoint (local) steering: Random, Hash (by client IP distribution) and Least Outstanding Requests, with per-endpoint weights defaulting to 1 ([Endpoint steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/)).

### 4.5 Monitors and health

Sources: [Monitors](https://developers.cloudflare.com/load-balancing/monitors/), [Manage monitors](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/), [Health details](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/).

- Types: HTTP and HTTPS (public and private), TCP (public and private), ICMP Ping and UDP-ICMP (public and Tunnel), SMTP (public); non-Enterprise customers can choose HTTP, HTTPS or TCP only.
- HTTP monitor options: method (default `GET`), path, port, expected codes (for example `2xx`), case-insensitive response body substring (`expected_body`), request headers (User-Agent cannot be overridden), follow redirects, timeout, retries, interval, `consecutive_up` and `consecutive_down`.
- The OpenAPI schema documents no request-body field for monitors, so a JSON-RPC `POST` health check with a body is not described (see section 14).
- Retries fire immediately on timeout, so with 5 retries and a 20 s timeout an endpoint goes unhealthy after about 120 s.
- Regions: each selected region probes from three data centers and a majority decides; All Regions (13 regions, 39 probes) and All Data Centers are Enterprise only, and many regions or short intervals can send a lot of traffic to the origin.
- Probes use IPv4 unless the endpoint has only `AAAA` records.
- Monitor Groups combine several monitors into one health signal; Enterprise with the Load Balancing subscription, API since 2025-10-16 ([Monitor Groups](https://developers.cloudflare.com/load-balancing/monitors/monitor-groups/)).
- Health notifications resolve automatically since 2026-08-07.

### 4.6 Session affinity, adaptive routing and other options

- Session affinity (public load balancers only): by `__cflb` cookie (default TTL 23 hours, HttpOnly, Secure with Always Use HTTPS), by cookie with client IP fallback, or by HTTP header ([Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/)).
- Zero-Downtime Failover (None, Temporary, Sticky) retries once on another healthy endpoint only for 521, 522, 523, 525 and 526 errors; Failover across pools extends this to other pools ([Adaptive routing](https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/)).
- Load shedding diverts a share of default or session-affinity traffic away from an at-risk pool ([Load shedding](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/)).
- Custom load balancing rules: expression plus actions (fixed response, override session affinity, TTL, steering policy, fallback pool, pools, region pools, country pools, terminate); non-Enterprise get one rule per load balancer hostname; not usable with Spectrum; AS number steering added 2025-08-15 ([Custom rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/), [Actions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/)).
- Private Network Load Balancing: private and virtual IPs reached through Cloudflare Tunnel with a virtual network, or Cloudflare WAN ([Private Network LB](https://developers.cloudflare.com/load-balancing/private-network/)).
- MX and SRV load balancing and CNAME flattening for endpoints are Enterprise features ([DNS records](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/), [CNAME flattening](https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/)).
- Other pages: DNS persistence, Host header override, PagerDuty integration, planned maintenance (endpoint drain), Spectrum, China Network, and the Regions API.

### 4.7 Limits (as of 2026-10-05)

Source: [Limitations](https://developers.cloudflare.com/load-balancing/reference/limitations/).

| Item | Non-Enterprise | Enterprise |
| --- | --- | --- |
| Load balancers | 20 | Custom |
| Pools | 20 | Custom |
| Endpoints | 20 | Custom |
| Monitors | 1.5x the number of pools | 1.5x the number of pools |
| Monitor interval | 15 s min, 3600 s max | 10 s min, 3600 s max |

- Self-service customers raise capacity by buying more endpoints; Enterprise asks the account team ([Common error codes](https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/)).

### 4.8 Recent changes

- 2026-08-31 pool sets; 2026-08-17 analytics filter by pool name; 2026-08-07 auto-resolving health notifications; 2026-08-03 fallback pool traffic shown separately; 2025-06-04 account-level UI and private load balancers; 2025-05-06 UDP and ICMP monitors for private endpoints; 2025-04-15 orange-clouded origin resolution ([changelog](https://developers.cloudflare.com/load-balancing/changelog/)).
- GraphQL nodes `loadBalancingRequestsGroups` and `loadBalancingRequests` are deprecated in favour of the `Adaptive` variants ([migration](https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/)).

### 4.9 Most useful pages

- [Quickstart](https://developers.cloudflare.com/load-balancing/get-started/quickstart/)
- [Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)
- [Monitors](https://developers.cloudflare.com/load-balancing/monitors/)
- [Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/)
- [Limitations](https://developers.cloudflare.com/load-balancing/reference/limitations/)
- [API reference](https://developers.cloudflare.com/api/resources/load_balancers/methods/get/)
- [Reference architecture](https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/)

---

## 5. Waiting Room

### 5.1 What it is

- Waiting Room routes excess visitors to a branded virtual queue so legitimate surges do not overload the origin ([overview](https://developers.cloudflare.com/waiting-room/)).
- It is built on Workers running in every data center, with global state propagated through Durable Objects every few seconds ([About](https://developers.cloudflare.com/waiting-room/about/)).
- Each data center decides locally whether to queue, using admin thresholds and its snapshot of global state.
- Prerequisites: Cloudflare CDN, a proxied DNS record or proxied load balancer for the hostname (not created automatically), and visitors with cookies enabled.
- Order of products: DDoS, WAF, Bot Management and Page Rules run before Waiting Room; Workers run after it ([FAQ](https://developers.cloudflare.com/waiting-room/troubleshooting/)).

### 5.2 Availability and plans (as of 2026-10-05)

Source: [Plans](https://developers.cloudflare.com/waiting-room/plans/).

- Available to Business and Enterprise plans and to organisations qualified under Project Fair Shot; Enterprise can preview it as a non-contract service.
- One basic waiting room is included in Business and Enterprise; Enterprise can buy Advanced Waiting Room for more rooms and features; only one plan per zone.

| Feature | Business | Enterprise (default) | Enterprise with Advanced add-on |
| --- | --- | --- | --- |
| Rooms | 1 | 1 | Custom, purchasable |
| Queueing methods | FIFO | FIFO | FIFO, Random, Reject, Passthrough |
| Customized templates | No | No | Yes |
| Multiple hostnames and paths | No | No | Yes |
| Disable session renewal | No | No | Yes |
| JSON-friendly response | No | No | Yes |
| Customize queueing status code | Yes | Yes | Yes |
| Scheduled events | No | No | Yes |
| Waiting Room rules (bypass) | No | No | Yes |
| Session revocation | No | No | Yes |
| SEO crawler bypassing | Yes | Yes | Yes |
| Turnstile widget mode | Invisible only | Invisible | Invisible, Managed, Non Interactive |
| Turnstile fail action | Log only | Log only | Log only or Infinite queue |

- Free and Pro have no Waiting Room.
- No per-room price appears in the docs; the overview links to the plans page for pricing.

### 5.3 Core configuration

Sources: [Configuration settings](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/), OpenAPI `waitingroom_*` schemas in `raw/api/openapi.json`.

| Setting | API field | Notes (as of 2026-10-05) |
| --- | --- | --- |
| Hostname | `host` | Required, no wildcards. |
| Path | `path` | Case-sensitive, applies to all subpaths, no wildcards or query parameters. |
| Additional routes | `additional_routes` | Advanced; same zone; needs `cookie_suffix`. |
| Total active users | `total_active_users` | Target concurrent sessions; docs say "greater than 200", OpenAPI minimum is 200; best practice 75% of origin capacity. |
| New users per minute | `new_users_per_minute` | Threshold (not an admission rate), at least 200 and at most total active users; best practice 100% of expected peak. |
| Session duration | `session_duration` | 1 to 30 minutes, default 5. |
| Disable session renewal | `disable_session_renewal` | Advanced; caps time on site to one session duration. |
| Session revocation | `enabled_origin_commands: ["revoke"]` | Origin returns `Cf-Waiting-Room-Command: revoke` to free a slot. |
| Queueing method | `queueing_method` | `fifo` (default), `random`, `passthrough`, `reject`. |
| Queue-all | `queue_all` | Queues every new visitor and overrides all other settings including events. |
| Suspended | `suspended` | Disables the room. |
| Queueing status code | `queueing_status_code` | 200 (default), 202 or 429. |
| JSON response | `json_response_enabled` | Advanced; returns JSON for `Accept: application/json`. |
| Custom page | `custom_page_html`, `default_template_language` | Mustache-rendered template, 1 MB file limit when imported. |
| Cookie | `cookie_suffix`, `cookie_attributes.samesite`, `cookie_attributes.secure` | SameSite `auto`, `lax`, `none`, `strict`. |
| SEO bypass | `search_engine_crawler_bypass` | Verified crawlers (via Bot Management) skip the room entirely. |
| Turnstile | `turnstile_mode`, `turnstile_action` | Modes `off`, `invisible`, `visible_non_interactive`, `visible_managed`; actions `log`, `infinite_queue`. |

### 5.4 Queueing methods

Source: [Queueing methods](https://developers.cloudflare.com/waiting-room/reference/queueing-methods/).

- FIFO orders by the timestamp in the visitor's cookie, rewarding early arrivals.
- Random admits visitors at random when slots open, for "more equitable" distribution; earlier arrivals still get more draws.
- Passthrough lets everyone through while still collecting analytics; useful as a baseline or with events.
- Reject serves a static page and lets no one through; useful for event-only endpoints or maintenance.
- With `queue_all` on or during an event pre-queue, nobody is admitted regardless of method.
- Switching FIFO to Random to FIFO restores original order; switching Random to FIFO moves new users to the back.

### 5.5 Scheduled events, pre-queue and lottery

Source: [Create scheduled events](https://developers.cloudflare.com/waiting-room/additional-options/create-events/).

- Events (Advanced) override room settings for a time window: total active users, new users per minute (the two must be overridden together), session duration, session renewal, queueing method, template, Turnstile settings.
- API fields: `name`, `event_start_time`, `event_end_time` (start at least 1 minute before end), `prequeue_start_time` (at least 5 minutes before start), `shuffle_at_event_start`, `suspended`, `description`.
- Pre-queue sends all new users into a queue before the event starts; to also catch already-active users, make the pre-queue window longer than the session duration and disable session renewal.
- "Lottery": `prequeue_start_time` plus `shuffle_at_event_start` randomly orders everyone who arrived during the pre-queue at event start; later arrivals queue after them under FIFO.
- Limit: five events per waiting room; overlapping events need different rooms; the room itself must be enabled for an event to activate.
- Use the event details endpoint to preview the effective configuration before it starts.
- Maintenance page pattern: room in Passthrough plus an event in Reject.

### 5.6 Cookies, refresh and queue behaviour

Sources: [Cookies](https://developers.cloudflare.com/waiting-room/reference/waiting-room-cookie/), [FAQ](https://developers.cloudflare.com/waiting-room/troubleshooting/), [Monitor status](https://developers.cloudflare.com/waiting-room/how-to/monitor-waiting-room/).

- The encrypted `__cfwaitingroom` cookie tracks queue position, time on site and re-entry; visitors without cookies cannot pass an actively queueing room.
- In the queue, the cookie expires after five minutes but renews every 20 seconds as the page auto-refreshes; after admission it lasts `session_duration`.
- A manual refresh keeps the position; closing the tab holds the place for five minutes after the last refresh, after which the visitor goes to the back.
- The FIFO estimated wait uses a per-minute group ID and an `acceptedAt` value in the cookie.
- Rate limiting rules must allow at least one request every 20 seconds per visitor, or queued users get blocked.
- Bots that do not keep cookies count as many inactive users and keep slots from being used, which depresses `new users per minute`; the docs recommend Cloudflare security products for automated traffic.
- Thresholds are targets, not hard caps: data centers can queue early, and a spike of several thousand users in a minute takes about two minutes to propagate globally, so new users per minute can overshoot.
- Dashboard and API status values are estimates 20 to 50 seconds old.
- Do not host custom-template assets on the hostname the room covers, or those requests will be queued too.

### 5.7 Turnstile integration

- Waiting Room can run a Turnstile widget on the queue page; with `infinite_queue`, detected bots stay in a fake queue and never reach the origin ([Configuration settings](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/)).
- Custom templates need the `turnstile` variable; Turnstile is not enforced on JSON responses, only on HTML ([JSON response](https://developers.cloudflare.com/waiting-room/how-to/json-response/)).
- Analytics show challenges per minute split into Likely Human (solved), Likely Bots (unsolved) and Bots (failed), plus bot refreshes in the infinite queue ([Analytics](https://developers.cloudflare.com/waiting-room/waiting-room-analytics/)).
- Turnstile is not supported in Mainland China ([China Network FAQ](https://developers.cloudflare.com/china-network/faq/)).

### 5.8 JSON-friendly mode for apps and APIs

- With `json_response_enabled`, a request with exactly `Accept: application/json` gets `{"cfWaitingRoom": {"inWaitingRoom", "waitTime", "waitTimeKnown", "waitTimeFormatted", "queueIsFull", "queueAll", "lastUpdated", "refreshIntervalSeconds"}}` while queued, and the origin response once admitted ([JSON response](https://developers.cloudflare.com/waiting-room/how-to/json-response/)).
- The client must resend the latest cookie on every request and poll every `refreshIntervalSeconds`; a request without the cookie is treated as a new user at the back of the queue.

### 5.9 Bypass rules

- Waiting Room Bypass Rules (Advanced) use Ruleset Engine expressions with action `bypass_waiting_room`, except `cf.threat_score`, `cf.bot_management.*` and response fields ([Bypass rules](https://developers.cloudflare.com/waiting-room/additional-options/waiting-room-rules/bypass-rules/)).
- Bypassed traffic is not counted and ignores pre-queue, Reject and Queue-all.
- Typical uses: exclude paths and static asset extensions, admin IPs, countries or query strings.

### 5.10 API and analytics

- Endpoints (from `raw/api/endpoints.tsv`): `GET /accounts/{account_id}/waiting_rooms`; zone-level list, create, get, update, patch, delete under `/zones/{zone_id}/waiting_rooms`; `/preview` for templates; `/settings` (zone-level settings); `/events` and `/events/{event_id}/details`; `/rules`; and `/status` ([API commands](https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/)).
- `/status` returns `queueing` or `not_queueing` plus estimated queued users, estimated active users and max estimated wait.
- Token permissions: Waiting Rooms Read and Waiting Rooms Write.
- Analytics keep 30 days, with time in queue, time on origin, active versus queued users, new users per minute, Turnstile traffic, and per-event reports that can be downloaded or printed.
- GraphQL dataset: `waitingRoomAnalyticsAdaptive`, including `sessionsRevoked`.

### 5.11 Most useful pages

- [Get started](https://developers.cloudflare.com/waiting-room/get-started/)
- [Plans](https://developers.cloudflare.com/waiting-room/plans/)
- [Configuration settings](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/)
- [Queueing methods](https://developers.cloudflare.com/waiting-room/reference/queueing-methods/)
- [Scheduled events](https://developers.cloudflare.com/waiting-room/additional-options/create-events/)
- [JSON response](https://developers.cloudflare.com/waiting-room/how-to/json-response/)
- [Best practices](https://developers.cloudflare.com/waiting-room/reference/best-practices/)
- [Test a waiting room](https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/) (JMeter plan, run tests longer than 2 to 3 minutes)
- [API reference](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/list/)

---

## 6. Argo Smart Routing

Sources: [overview](https://developers.cloudflare.com/argo-smart-routing/), [get started](https://developers.cloudflare.com/argo-smart-routing/get-started/), [analytics](https://developers.cloudflare.com/argo-smart-routing/analytics/), [Argo for Packets](https://developers.cloudflare.com/argo-smart-routing/argo-for-packets/).

- Argo Smart Routing detects real-time network issues and routes traffic over the fastest path between Cloudflare data centers and the origin; benefits are largest for users far from the origin.
- It is an add-on that now carries the banner "This functionality is now offered as part of Cloudflare's origin server safeguard, Smart Shield".
- Enable it in the dashboard (Traffic) or with `PATCH` on the Argo smart routing setting (`"on"`/`"off"`); a billing profile is required; Enterprise can preview it as a non-contract service.
- Billing is usage-based; traffic mitigated by DDoS protection or WAF is not charged; the docs recommend usage-based billing notifications.
- Billing docs (as of 2026-10-05) say Argo data transfer is metered per GB between Cloudflare and the origin with the first 1 GB included, and an example invoice shows "Smart Shield Argo Zone Level Plan - Basic" at $5.00 and "Smart Shield Argo Accelerated Gigabytes" at $0.10 per GB ([How billing works](https://developers.cloudflare.com/billing/understand/how-billing-works/), [Usage-based billing](https://developers.cloudflare.com/billing/understand/usage-based-billing/)).
- Tiered Cache relation: the get-started page recommends enabling Tiered Cache, because Argo optimizes the path to the origin while Tiered Cache reduces how many requests reach it; the cache get-started page links "Enable Tiered Cache with Argo".
- Analytics (Analytics > Performance) compare origin TTFB with and without Argo as a histogram and a per-data-center map; detailed data needs at least 500 Argo-routed origin requests in 48 hours.
- Origin Analytics notes Argo can change the measured origin response time ([Origin Analytics](https://developers.cloudflare.com/speed/origin-analytics/)).
- Argo for Packets optimizes IP-layer routing to a Cloudflare Network Interconnect for Magic Transit and Cloudflare WAN; it is enabled through the account manager.
- Argo is available on the China Network ([available products](https://developers.cloudflare.com/china-network/reference/available-products/)).
- Cloudflare's own Ethereum gateway used Load Balancing, Argo Tunnel and Argo Smart Routing so that requests and responses travel from the Ethereum node to the edge over the best path ([blog: Cloudflare Ethereum gateway](https://blog.cloudflare.com/cloudflare-ethereum-gateway/), historical).

---

## 7. Smart Shield

Sources: [overview](https://developers.cloudflare.com/smart-shield/), [get started](https://developers.cloudflare.com/smart-shield/get-started/), [connection reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/).

- Smart Shield is "a bundle of origin protection and performance features that reduce the number of requests and connections between Cloudflare's network and your origin server"; it is opt-in for all customers and needs proxied records.
- Packages (as of 2026-10-05):

| Package | Includes | Who can buy |
| --- | --- | --- |
| Smart Shield | Smart Tiered Cache, Connection Reuse | Free, Pro, Business, Enterprise ("Get started for free" in the dashboard flow) |
| Smart Shield + Argo | Above plus Argo Smart Routing | Free, Pro, Business, Enterprise |
| Smart Shield Advanced | Above plus Regional Tiered Cache and Cache Reserve | Enterprise only for now |

- Health Checks are included for Pro, Business and Enterprise in all packages ([Health Checks setup](https://developers.cloudflare.com/smart-shield/configuration/health-checks/setup/)).
- Enterprise gets Regional Tiered Cache regardless of package, and can request Dedicated CDN Egress IPs.
- Connection reuse sends many requests from upper-tier data centers over a single connection and uses HTTP/2 connection coalescing when hostnames share IP, port and certificate.
- Dedicated CDN Egress IPs (formerly Cloudflare Aegis): Enterprise-only reserved egress IPs for layer 7 WAF and CDN and for Spectrum, usable across zones and accounts, drawn either from a BYOIP prefix or from Cloudflare-leased IPs (not mixed), so origins can allowlist a short list ([Dedicated CDN Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/)).
- Egress IP utilization can be queried in GraphQL in five-minute buckets ([IPs utilization](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/)).
- The Health Checks section also includes a guide to migrate from Zone Lockdown to WAF custom rules ([Zone Lockdown](https://developers.cloudflare.com/smart-shield/configuration/health-checks/zone-lockdown/)).
- After setup, Observatory is the place to watch origin performance and cache effectiveness.

---

## 8. Zaraz

Sources: [overview](https://developers.cloudflare.com/zaraz/), [get started](https://developers.cloudflare.com/zaraz/get-started/), [pricing](https://developers.cloudflare.com/zaraz/pricing-info/).

- Zaraz loads third-party tools (analytics, ad pixels, chat, marketing automation) in the cloud at Cloudflare's edge instead of in the browser, for speed, privacy and security; "Available on all plans".
- Proxying the site through Cloudflare is recommended; non-proxied sites can load Zaraz from a separate proxied subdomain ([Domains not proxied](https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/)).
- Model: events, triggers and actions; tools with Automatic Actions get Pageviews, Events and E-commerce actions out of the box, others use custom actions.
- Web API: `zaraz.track()`, `zaraz.set()`, `zaraz.ecommerce()`, plus debug mode ([Web API](https://developers.cloudflare.com/zaraz/web-api/)).
- HTTP Events API: disabled until you configure a path (choose a unique one); accepts `POST` JSON with an `events` array, reserved keys `__zarazTrack` and `__zarazEcommerce`, a `system` object for device, page and cookie data, and returns per-event `fetch`, `execute`, `return` and `cookies` results ([HTTP Events API](https://developers.cloudflare.com/zaraz/http-events-api/)).
- Consent management with a Consent API, IAB TCF compliance and Google Consent Mode support.
- Advanced: blocking triggers, Context Enricher (Workers), Worker Variables, custom Managed Components, data layer compatibility mode, JSONata, selective and manual loading, import and export, versions with preview mode, and Single Page Application support.
- Monitoring shows event usage and server-side request success; "Advanced Monitoring" (geography, user timeline, funnel, retention) arrived 2024-12-16, and a Monitoring API exists in GraphQL ([Monitoring](https://developers.cloudflare.com/zaraz/monitoring/)).
- Logpush of Zaraz events (dataset "Zaraz Events") was added 2025-02-11 and is "an Enterprise only feature" ([Zaraz Logpush](https://developers.cloudflare.com/zaraz/advanced/logpush/)).
- Pricing (as of 2026-10-05): 1,000,000 free Zaraz Events per account per month; Zaraz Paid costs $5 per month for each additional 1,000,000 events; without Paid, Zaraz sends warnings at 50%, 80% and 90% and is disabled until the next cycle when the free allocation is exceeded.
- A Zaraz Event is anything sent to Zaraz, such as a pageview or a `zaraz.track` call.
- The latest changelog entry in the mirror is 2025-02-11 ([changelog](https://developers.cloudflare.com/zaraz/changelog/)).
- In the dashboard Zaraz now sits under Delivery & Performance > Web tag management > Tag setup.

---

## 9. Automatic Platform Optimization (APO)

Sources: [overview](https://developers.cloudflare.com/automatic-platform-optimization/), [About](https://developers.cloudflare.com/automatic-platform-optimization/about/), [Activate the WordPress plugin](https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/).

- APO serves an entire WordPress site, including HTML, from the edge using Workers, and requires the Cloudflare for WordPress plugin.
- Content updates in WordPress purge the edge via the plugin; logged-in and admin users bypass the cache.
- APO caches HTML only when the method is `GET` or `HEAD`, the request is HTML-eligible, the origin returns 200 with `text/html`, the plugin's `cf-edge-cache` header allows caching, there are no bypass cookies or risky headers, the path is not excluded (checkout, `wp-cron.php`, feeds), query strings are absent or only supported marketing parameters, and no Page Rule sets Cache Level Bypass; otherwise it returns `DYNAMIC` with a reason in `cf-apo-via`.
- Plans (as of 2026-10-05): Free must purchase APO before installing the plugin; Pro and above go straight to installation; Bypass Cache on Cookie with APO is Business and Enterprise only; no price is stated in the docs.
- APO is not compatible with an Enterprise subdomain setup where `www` is in a different zone from the apex.
- Other pages: plugin compatibility, cache by device type, Page Rule integration, query parameters, subdomains and subdirectories, verify APO works (three headers).

---

## 10. China Network

Sources: [overview](https://developers.cloudflare.com/china-network/), [get started](https://developers.cloudflare.com/china-network/get-started/), [FAQ](https://developers.cloudflare.com/china-network/faq/), [available products](https://developers.cloudflare.com/china-network/reference/available-products/).

- China Network runs selected Cloudflare performance and security products in Mainland China data centers operated by partner JD Cloud, managed from the same dashboard.
- Availability: a separate subscription on top of an Enterprise plan, plus the China Service Supplemental Terms.
- Onboarding needs a valid ICP filing or license for each apex domain, the ICP number in the site footer, and JD Cloud content vetting (company, domain, ICP number, content description, signed self-attestation); first enablement takes about 24 to 48 hours.
- An ICP filing (Bei'An) covers informational sites and takes about 1 to 2 months; an ICP license is required for commercial or transactional sites and takes about 2 to 3 months and is limited to local companies or joint ventures with under 50% foreign ownership ([ICP](https://developers.cloudflare.com/china-network/concepts/icp/)).
- Neither Cloudflare nor JD Cloud applies for ICPs; if an ICP is revoked, JD Cloud may suspend service and Cloudflare reroutes traffic.
- IPv6 is mandatory and cannot be disabled.
- In-China authoritative DNS (via sales, recommended only when over 90% of traffic is from China) routes all DNS queries to JD Cloud, which can slow users elsewhere ([China DNS](https://developers.cloudflare.com/china-network/concepts/china-dns/)).
- Available: authoritative DNS, cache (static only, no Cache Reserve or Tiered Cache), Image Transformations, L7 DDoS, WAF managed, custom and rate limiting rules, content scanning, client-side security, Bot Management (some ML models), Argo, Rules, Load Balancing, Workers, KV, R2, static assets, Images, Workers for Platforms, SSL/TLS, HTTP/3 and WebSockets.
- Not available or not supported: Turnstile, and Pages (because `pages.dev` certificates are not in Mainland China).
- Global Acceleration add-ons (through partners such as CMI, CBC Tech and JD Cloud): CDN Global Acceleration for dynamic content, Cloudflare One Client and Cloudflare WAN acceleration, ICP and MLPS services, Travel SIM ([Global Acceleration](https://developers.cloudflare.com/china-network/concepts/global-acceleration/)).

---

## 11. Google tag gateway for advertisers

Source: [Google tag gateway for advertisers](https://developers.cloudflare.com/google-tag-gateway/) (single page).

- It loads Google measurement tags from the site's own domain at a reserved measurement path and forwards events to Google, for privacy and better signal recovery.
- Pricing (as of 2026-10-05): free, and requests through the gateway do not count toward CDN, WAF or Bot Management usage.
- Setup is either in Google Tag Manager or in the Cloudflare dashboard (roles Super Administrator, Administrator or Zaraz Admin, or Domain Administrator); it overrides an existing GTM script.
- It is configured per zone and applies to all hostnames including custom hostnames; it cannot be toggled per subdomain, and Configuration Rules cannot disable it, so per-subdomain logic belongs in GTM triggers.

---

## 12. Plan availability cheat sheet

As of 2026-10-05, from the pages cited above.

| Product or feature | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Cache, Cache Rules, purge (all methods), Tiered Cache Smart topology | Yes | Yes | Yes | Yes |
| Generic Global, Regional, Custom Tiered Cache | No | No | No | Yes |
| Custom cache key (headers, cookies, host, user) | No | No | No | Yes |
| Cache Reserve | Paid add-on (Smart Shield Advanced is Enterprise only, see section 14) | Paid add-on | Paid add-on | Yes |
| Vary for images | No | Yes | Yes | Yes |
| Prefetch URLs | No | No | No | Yes |
| Observatory tests | Not listed in quota table | 50 / 5 | 100 / 10 | 150 / 15 |
| Enhanced HTTP/2 Prioritization | No | Yes | Yes | Yes |
| Load Balancing | Paid add-on | Paid add-on | Paid add-on | Add-on, preview available |
| Waiting Room | No | No | 1 basic room | 1 room, Advanced add-on |
| Argo Smart Routing | Paid add-on | Paid add-on | Paid add-on | Add-on, preview available |
| Smart Shield / Smart Shield + Argo | Purchasable | Purchasable | Purchasable | Yes |
| Smart Shield Advanced, Dedicated CDN Egress IPs | No | No | No | Yes |
| Zaraz | 1M events free, then $5 per 1M | Same | Same | Same, plus Logpush |
| APO | Purchase | Included path | Included path | Included path |
| China Network | No | No | No | Separate subscription |
| Google tag gateway | Free | Free | Free | Free |

---

## 13. Build hooks for Web3 projects

These are concrete ways to use the products above for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2 with chain id 4663); each hook names the limit that constrains it.

### 13.1 Launch-day and mint traffic with Waiting Room

- Put the mint or launch page (for example `launch.example.xyz/mint`) behind a waiting room, sized with `total_active_users` at about 75% of what the backend and RPC quota can serve, and `new_users_per_minute` at expected peak, both at least 200.
- For a timed token launch or NFT mint, use a scheduled event with `prequeue_start_time` at least 5 minutes before `event_start_time` and `shuffle_at_event_start: true` to run a fair "lottery" among everyone who arrived early, so bots that hammer the URL at T-0 gain nothing over humans who arrived during the pre-queue; this needs Enterprise with Advanced Waiting Room.
- Use the Random queueing method instead of FIFO during the event for a more equitable draw, or Reject before the event and switch via the event to open the gate (Advanced).
- Turn on Turnstile with `infinite_queue` (Advanced) so detected bots sit in a fake queue and never touch the mint backend; on Business only invisible mode with log-only is available, which detects but does not block.
- Use origin session revocation (`Cf-Waiting-Room-Command: revoke` on the response after a mint transaction is submitted) to free the slot for the next user immediately.
- A trading UI that is a single-page app calling a JSON API should enable `json_response_enabled` and have the frontend send `Accept: application/json`, keep the `__cfwaitingroom` cookie and poll every `refreshIntervalSeconds`; Turnstile does not apply to JSON responses, so pair it with WAF and Bot Management on the API.
- Waiting Room only gates HTTP requests through the proxied hostname; it does not protect a public RPC endpoint or the on-chain contract, so a bot can still call the mint contract directly through any RPC; gate the allowlist or signature step (for example a server-issued signed mint voucher) behind the room, not just the page.
- Keep wallet adapter scripts, images and the template's assets on a different hostname or bypass them with a bypass rule for `.js`, `.css`, `.png`, since otherwise they queue too.
- Ensure rate limiting rules allow at least one request every 20 seconds per queued visitor.
- Expect overshoot of new users per minute for about two minutes during a spike of several thousand users per minute, and budget backend headroom accordingly.
- Use passthrough mode a week before launch to collect active-user and time-on-origin baselines, then load-test with the JMeter plan for more than 2 to 3 minutes.
- Without Business or Enterprise (Free and Pro have no Waiting Room), the equivalent has to be built with Workers and Durable Objects, which is how Waiting Room itself is built.

### 13.2 Cache rules for token lists, metadata and price APIs

- JSON is not cached by default, so add a Cache Rule (Eligible for cache) for read-only endpoints such as `/tokenlist.json`, `/api/tokens/*`, `/metadata/*.json` and chart history, and set Edge TTL with `override_origin` or send `Cloudflare-CDN-Cache-Control: max-age=...` from the origin so browsers can keep a shorter `Cache-Control`.
- For fast-moving data such as prices or pool reserves, use a short edge TTL with `stale-while-revalidate` so users get `UPDATING` responses instead of waiting; note the minimum Edge Cache TTL is 2 hours on Free and 1 hour on Pro, so second-level TTLs need Business or Enterprise or Workers with `cf.cacheTtl`.
- JSON-RPC uses `POST`, and Cloudflare only caches `GET` (the Workers Cache API also refuses non-`GET` `put`), so to cache idempotent reads such as `eth_getBlockByNumber` for finalized blocks, `eth_chainId`, Solana `getTokenSupply` or token metadata, expose them as `GET` REST routes in a Worker that calls the RPC provider, and include the chain id (1, 8453, 4663, or a Solana cluster) in the URL so caches for different chains never collide.
- Never cache responses that depend on a wallet address or session unless the address is in the URL or cache key; Enterprise custom cache keys can add a header, but high-cardinality keys shard the cache and should usually be `bypass` in the Vary configuration.
- Cache keys include the `Origin` header by default, so a public metadata API called from many dapp origins may cache once per origin; Enterprise custom keys can drop it, or the API can be served same-origin.
- Use `Cache-Tag` headers such as `collection-0xabc`, `token-4663-0xdef` or `mint-<pubkey>`, then purge or invalidate by tag when on-chain state changes (reveal, metadata update, delisting); Free accounts get only 5 tag or prefix purges per minute per account, while Pro gets 5 per second, so high-churn indexers need Pro or above.
- Prefer `invalidate_cache` over purge when an NFT collection may not have changed: with `ETag` on the metadata origin, unchanged items revalidate with `304` instead of refetching.
- Use Cache Response Rules to strip `Set-Cookie` from RPC-proxy or metadata responses that would otherwise be `BYPASS`, and to add cache tags without touching the origin.
- Turn on Tiered Cache (Smart topology is free) so a viral collection's images and metadata are fetched from IPFS gateways or the indexer once per upper tier rather than once per data center; for IPFS-pinned content with long TTLs, Cache Reserve keeps objects with at least a 10-hour TTL for 30 days since last access.
- Use Vary normalization or caching level settings carefully on token-list URLs that carry `?v=` or chain query strings; Standard caching level keys on the full query string.

### 13.3 Load Balancing across RPC providers

- Put two or three RPC providers per chain (for example a Helius and a second Solana provider, or several Base and Robinhood Chain 4663 endpoints) in separate pools behind a proxied load balancer on `rpc.example.xyz`, with Off (failover) steering for primary and backup, or Random with weights for active-active.
- Least Outstanding Requests steering suits RPC backends that fall over under concurrent spikes, but it is only meaningful for proxied load balancers.
- Load Balancing monitors only send a method, path, headers and expect a status code or body substring, and the docs do not describe a request body, so a JSON-RPC `POST` probe such as `eth_blockNumber` or Solana `getHealth` with a body cannot be expressed directly; point the monitor at a provider's HTTP health path, or at a small Worker route that does the JSON-RPC call and returns 200 only if the block height is fresh.
- Monitor intervals bottom out at 15 s for non-Enterprise per the limits page (the monitor page says 60 s on Pro), so a provider that stops producing fresh blocks can serve stale data for a while; add the freshness check in the Worker route.
- Provider API keys normally go in the URL or a header; endpoint Host header overrides and monitor headers can carry a header-based key, but key-in-URL providers are better fronted by a Worker proxy such as the Helius RPC proxy, a one-click Cloudflare Worker that hides the API key and supports JSON-RPC and WebSockets, with `CORS_ALLOW_ORIGIN` to lock it to the dapp origin (`raw/external/github.com_helius-labs_helius-rpc-proxy.md`).
- Zero-Downtime Failover retries only on 521, 522, 523, 525 and 526, not on JSON-RPC errors returned with HTTP 200 or on 429 rate limits, so provider rate limiting will not trigger failover by itself.
- DNS queries to load-balanced hostnames are metered after the first 500K, and short monitor intervals with many regions raise both cost and probe load on the provider.
- Session affinity by header (for example a session id header) can keep a trading session on one provider so nonce and pending-transaction views stay consistent.

### 13.4 Origin protection for RPC proxies and indexers

- Smart Shield (base package, purchasable on any plan) gives Smart Tiered Cache and connection reuse so a self-hosted indexer or node sees a few long-lived connections from upper tiers instead of one per data center.
- Set a cloud region hint (free on all plans) if the node or indexer runs on AWS, GCP, Azure or Oracle Cloud, so Smart Tiered Cache picks the right upper tier.
- Dedicated CDN Egress IPs (Enterprise) let a self-hosted node's firewall allow only a handful of Cloudflare IPs.
- Argo (Smart Shield + Argo) shortens the path from distant users to a single-region node; it is metered per GB of origin transfer, so it suits small JSON responses better than large media.
- Origin Analytics shows whether 524 timeouts come from slow RPC methods (for example `getProgramAccounts` or `eth_getLogs` over large ranges), using p95 origin response time by endpoint.
- For a launchpad's own backend, Speed Brain prefetches only cached pages and never reaches the origin or Workers, so it cannot trigger state-changing calls, but it does nothing for dynamic dapp pages.

### 13.5 Zaraz and Google tag gateway on dapp frontends

- Zaraz moves analytics and ad pixels off the main thread and out of the browser, which reduces third-party script exposure on pages where wallets sign transactions; the HTTP Events API can record server-side events such as "swap confirmed" or "mint succeeded" without client JavaScript.
- Do not send wallet addresses or transaction hashes to third-party tools unless the privacy policy covers it; Zaraz consent management and the "Hide Originating IP Address" option help.
- Zaraz is free up to 1M events per account per month and is disabled for the rest of the cycle if that is exceeded without Zaraz Paid, which can silently stop analytics on launch day; enable Paid before a launch.
- Google tag gateway is free and zone-wide; it cannot be disabled per subdomain, so a sensitive `app.` subdomain on the same zone as a marketing site will get tags too unless GTM triggers exclude it.

### 13.6 China and global reach

- A dapp that must serve Mainland China needs Enterprise plus China Network, an ICP filing or license per apex domain and JD Cloud content vetting, and Turnstile and Pages do not work there; plan alternative bot checks and Workers-based hosting.

---

## 14. Gaps and contradictions

Contradictions between pages (flagged, not resolved):

- Load Balancing monitor minimum interval: the limitations page says 15 s for all non-Enterprise customers ([limitations](https://developers.cloudflare.com/load-balancing/reference/limitations/)), while the monitor and quickstart pages say 60 s on Pro, 15 s on Business and 10 s on Enterprise ([create monitor](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/), [quickstart](https://developers.cloudflare.com/load-balancing/get-started/quickstart/)).
- Waiting Room `total_active_users` and `new_users_per_minute`: the configuration page says "must be greater than 200" while the OpenAPI schema sets `minimum: 200`, which allows exactly 200.
- Waiting Room cookie name: the configuration page says the suffix is added to `_cfwaitingroom` (one underscore), while the cookie page and JSON response page use `__cfwaitingroom` (two underscores).
- Waiting Room customization: the FAQ says "Only Enterprise customers can customize the appearance", while the plans table ties customized templates to the Advanced add-on, not to Enterprise in general.
- Waiting Room Analytics is labelled "(Beta)" on the test-a-waiting-room page but not on the analytics page itself.
- Cache Reserve availability: the Cache Reserve page says it needs "a paid Cache Reserve plan" and is usage-based, implying any paid plan, while Smart Shield pages say Cache Reserve is only in Smart Shield Advanced, which "is not currently available for Free, Pro, and Business customers".
- Custom cache keys: the cache get-started page labels "Configure custom cache keys (Enterprise only)", while the Cache Rules settings page lists cache deception armor, cache by device type and sort query string as cache key options for everyone and only the custom query string, header, cookie, host and user options as Enterprise (with Ignore query string also for pay-as-you-go).
- Cache by device type is labelled Enterprise only on the cache get-started page but appears as a general cache key toggle on the Cache Rules settings page and on the APO reference.
- Zstandard compression: the compression page says Free zones are compressed by default with Zstandard, but the same page also says customers "can enable Zstandard compression through Compression Rules", implying it is opt-in.
- RUM exclusions: the Observatory page says Free-plan RUM excludes EEA/UK/CH traffic, while the RUM beacon page says "EU traffic excluded".
- Observatory frequency: the run-test page says tests can run once, daily or weekly depending on plan, while the quota table lists only daily recurring tests.
- Zaraz pricing says "All Zaraz features and tools are always available on all accounts", while the Zaraz Logpush page says Logpush "is an Enterprise only feature".

Gaps (not documented in the mirror as of 2026-10-05):

- No list prices in the docs for Load Balancing, Argo Smart Routing, Smart Shield packages, Advanced Waiting Room, APO or China Network; the overview pages link to the dashboard or marketing site, and the only figures are example invoice lines in billing docs ($5.00 Basic Load Balancing, $5.00 Smart Shield Argo zone plan, $0.10 per Argo GB with first GB included).
- No documented request body for Load Balancing HTTP monitors, so JSON-RPC health probes need a helper endpoint.
- No documented way to cache `POST` responses at the CDN; caching JSON-RPC reads requires a `GET` facade in a Worker.
- Free plan Observatory quotas are not in the quota table, although Free has RUM on by default.
- Waiting Room limits beyond five events per room, a 1 MB template, 1 to 30 minute sessions and 200 minimum thresholds (for example maximum rooms per zone for Advanced, or rule counts) are not documented.
- The Zaraz changelog in the mirror stops at 2025-02-11, so recent Zaraz changes may be missing.
- Waiting Room docs pages are mostly dated 2026-04 and do not mention any 2026 changes, so the feature set may lag the API schema (which already includes `cookie_attributes`, `default_template_language` and zone-level `settings`).
- The relationship between the standalone Argo add-on and the "Smart Shield + Argo" package (whether existing Argo subscriptions are migrated or both coexist) is not explained.
