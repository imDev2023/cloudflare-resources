# Cloudflare API reference

This file explains how the Cloudflare REST API works and maps all of it, as mirrored on 2026-10-05.
The API is one versioned JSON API at `https://api.cloudflare.com/client/v4`, authenticated with scoped API tokens (`Authorization: Bearer`) or, for legacy use, a Global API Key sent as `X-Auth-Email` plus `X-Auth-Key`; resources are scoped under `/accounts/{account_id}/...`, `/zones/{zone_id}/...` or `/user/...`, responses use a common `success`/`errors`/`messages`/`result` envelope, lists paginate with `page`/`per_page` or cursors, and a global limit of 1,200 requests per five minutes applies per user or token.
The official OpenAPI spec mirrored today has 3,647 operations on 2,287 paths; the published reference lists 128 top-level resources and 2,824 method entries, and the official clients exist for TypeScript, Python, Go and Terraform (HTTP is the fifth "language" of the reference).
Below are the auth, scoping, envelope, pagination and rate-limit rules, a table of every top-level resource with its operation counts, a second table grouping every spec operation by path, the Web3-relevant endpoints, and copy-paste recipes for looking up any endpoint in the local mirror.
Tooling that calls the API (SDKs, Terraform, Pulumi, `cf`, Wrangler, MCP) is covered in `platform-and-tooling.md`; this file sticks to the API contract, and it flags rather than resolves disagreements between sources.

## Table of contents

1. [Sources and how the local copy is laid out](#1-sources-and-how-the-local-copy-is-laid-out)
2. [Base URL and versioning](#2-base-url-and-versioning)
3. [Authentication](#3-authentication)
4. [Account, zone and user scoping](#4-account-zone-and-user-scoping)
5. [Request conventions](#5-request-conventions)
6. [Response envelope and errors](#6-response-envelope-and-errors)
7. [Pagination](#7-pagination)
8. [Rate limits](#8-rate-limits)
9. [Availability, plan and deprecation metadata in the spec](#9-availability-plan-and-deprecation-metadata-in-the-spec)
10. [Headline counts](#10-headline-counts)
11. [Every top-level resource with operation counts](#11-every-top-level-resource-with-operation-counts)
12. [Every spec operation grouped by path](#12-every-spec-operation-grouped-by-path)
13. [Endpoints worth knowing for app builders](#13-endpoints-worth-knowing-for-app-builders)
14. [SDK languages and reference URL structure](#14-sdk-languages-and-reference-url-structure)
15. [Looking up any endpoint locally](#15-looking-up-any-endpoint-locally)
16. [Build hooks for Web3 projects](#16-build-hooks-for-web3-projects)
17. [Gaps and contradictions](#17-gaps-and-contradictions)

---

## 1. Sources and how the local copy is laid out

| Local path | What it is | Source URL |
| --- | --- | --- |
| `raw/api/llms.txt` | Index of all API reference pages (128 top-level resources, 1,110 resource and subresource pages) | https://developers.cloudflare.com/api/llms.txt |
| `raw/api/overview/index.md` | The short API overview page | https://developers.cloudflare.com/api/overview/ |
| `raw/api/resources/<resource>/**/index.md` | One page per resource and subresource, listing each method's HTTP method and path plus object models | https://developers.cloudflare.com/api/resources/ |
| `raw/docs/api/index.md` | The API reference root, with library versions and every method grouped by resource (640 KB) | https://developers.cloudflare.com/api/ |
| `raw/api/openapi.json` | The full OpenAPI 3.0.3 spec (26 MB) | https://github.com/cloudflare/api-schemas |
| `raw/api/endpoints.tsv` | One line per spec operation: `method`, `path`, `operationId`, `tags`, `summary`, `deprecated` | derived from the spec by `scripts/fetch-api.py` |
| `raw/docs/fundamentals/api/**` | Token, key, limits, permissions, SDK and deprecation pages | https://developers.cloudflare.com/fundamentals/api/ |

Per-method pages (`.../methods/<name>/`) are not mirrored; the spec carries every parameter and schema they show (per the header of `scripts/fetch-api.py`).

## 2. Base URL and versioning

Sources: https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/ and the spec's `servers` block

- "Every Cloudflare API element is fixed to a version number."
- "The latest version is Version 4."
- The stable base URL for all Version 4 HTTPS endpoints is `https://api.cloudflare.com/client/v4/`.
- The spec declares one server, `https://api.cloudflare.com/client/v4` ("Client API"), `info.version` 4.0.0, license BSD-3-Clause, OpenAPI 3.0.3.
- The `cf` CLI exposes `CLOUDFLARE_COMPLIANCE_REGION` (`public` or `fedramp-high`) and `CLOUDFLARE_API_BASE_URL` to change the endpoint (https://developers.cloudflare.com/cf/environment-variables/); a Gateway policy table lists `api.fed.cloudflare.com` next to `api.cloudflare.com`, but no page in the mirror documents the FedRAMP base URL as an API base.
- The analytics GraphQL API is at `https://api.cloudflare.com/client/v4/graphql` (https://developers.cloudflare.com/analytics/graphql-api/) and is not part of the OpenAPI spec.
- The spec's description says Cloudflare is "experimenting with an updated version of our API documentation" at https://developers.cloudflare.com/api-next/.

## 3. Authentication

Sources: https://developers.cloudflare.com/api/overview/, https://developers.cloudflare.com/fundamentals/api/get-started/create-token/, https://developers.cloudflare.com/fundamentals/api/get-started/keys/, https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/, https://developers.cloudflare.com/fundamentals/api/reference/deprecations/

### 3.1 Schemes in the spec

| Scheme name | How it is sent | Status (as of 2026-10-05) |
| --- | --- | --- |
| `api_token` | `Authorization: Bearer <API_TOKEN>` (RFC 6750) | Recommended |
| `api_email` + `api_key` | `X-Auth-Email: <EMAIL>` and `X-Auth-Key: <GLOBAL_API_KEY>` | Legacy; "not recommended for new customers" |
| `user_service_key` | `X-Auth-User-Service-Key: <ORIGIN_CA_KEY>` | Deprecated; end of life September 30, 2026 |

Per-operation `security` in the spec (counted 2026-10-05): 3,383 operations accept `api_token`, 220 list only the email plus key pair, 83 also accept `user_service_key`, 4 have an empty security list (two alerting unsubscribe routes, `GET /api/v4/health`, `GET /zones/{zone_id}/hold/{zone_name}`), and 40 (all under `/accounts/{account_id}/workers/observability/...`) set no `security` and so inherit the spec's top-level default (`api_email`+`api_key`, or `api_token`, or `user_service_key`).
The 220 key-only operations cluster in `cloudforce-one` (23), `intel` (22), `shares` (20), `custom_pages` (18), `pay-per-crawl` (17, account and zone paths combined), `mnm` (16), `pay-per-use` (16, combined), `organizations` (15), `secrets_store` (12), `iam` (10), `tags` (10) and `user` (9); no page says whether tokens are actually rejected there.

### 3.2 Token types

| Credential | Prefix (new or rolled) | Who it acts as | Limit | Notes |
| --- | --- | --- | --- | --- |
| User API token | `cfut_` + 40 chars + checksum | A user, with a subset of their permissions | 50 per user | Created at My Profile > API Tokens |
| Account API token | `cfat_` + 40 chars + checksum | The account as a service principal | 500 per account | Created at Manage Account > API Tokens; GA; some products unsupported (see `platform-and-tooling.md` section 12.3) |
| Global API Key | `cfk_` + 40 chars + checksum | The user, with full permissions | 1 per user | Requires a verified email; cannot be scoped, IP-limited or time-limited |
| Origin CA key (Service Key) | starts with `v1.0-` | The user, across every account they can access | n/a | Deprecated; replace with a token holding Zone SSL and Certificates Edit |

Older unprefixed tokens keep working; leaked tokens in either format are scanned for (GitHub Secret Scanning, auto-revocation for public repos).
`cf` does not support the Global API Key at all (https://developers.cloudflare.com/cf/get-started/).

### 3.3 Verifying a token

```bash
curl "https://api.cloudflare.com/client/v4/user/tokens/verify" \
  --header "Authorization: Bearer <API_TOKEN>"
```

A valid token returns `"status": "active"` with message code 10000 "This API Token is valid and active", and may include `not_before` and `expires_on`.
Account-owned tokens have `GET /accounts/{account_id}/tokens/verify` (operationId `account-api-tokens-verify-token`).
Client IP filtering is not applied to the verify endpoint (https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/).

### 3.4 Token policies, permissions and OAuth

- A token holds policies with `effect` (`allow`/`deny`), `resources` and `permission_groups`; explicit DENY wins over ALLOW, and anything unmatched is denied (https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/).
- Resource keys: `com.cloudflare.api.account.<ACCOUNT_ID>`, `com.cloudflare.api.account.zone.<ZONE_ID>`, wildcards `com.cloudflare.api.account.*` and `com.cloudflare.api.account.zone.*`, nested "all zones in one account", and `com.cloudflare.api.user.<USER_TAG>`.
- Permission groups (6 user, 173 account, 74 zone on 2026-10-05) are listed at https://developers.cloudflare.com/fundamentals/api/reference/permissions/ and live from `GET /user/tokens/permission_groups` or `GET /accounts/{account_id}/tokens/permission_groups`; `Edit` (or `Write`) means full CRUDL and `Read` means read and list.
- The Account Roles API is deprecated in favor of the IAM Permission Groups API (deprecations entry of 2026-07-21).
- Third-party apps can instead use OAuth 2.0 Authorization Code (with secret or PKCE `S256`) at `https://dash.cloudflare.com/oauth2/auth` and `/oauth2/token`, with scopes named after token permissions and listed by `GET /oauth/scopes` (https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/).
- The Cloudflare API MCP server accepts OAuth or a user or account API token as a bearer token (https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/).

## 4. Account, zone and user scoping

Sources: https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/, `raw/api/endpoints.tsv`

Account-level products (Workers, Pages, R2, D1, KV, Queues, Zero Trust, and so on) live under `/accounts/{account_id}/...`; zone-level settings (DNS, cache, WAF, SSL, rules) live under `/zones/{zone_id}/...`; personal settings live under `/user/...`.
Split of the 3,647 spec operations by path root (counted 2026-10-05):

| Root | Operations |
| --- | --- |
| `/accounts...` | 2,565 |
| `/zones...` | 697 |
| `/user...` | 56 |
| `/radar...` | 279 |
| `/organizations...` | 18 |
| `/tenants...` | 8 |
| `/certificates` (Origin CA) | 4 |
| `/memberships` | 4 |
| `/analytics/sql...` | 3 |
| `/pages/assets/...` | 3 |
| `/billing/...` | 2 |
| `/ips`, `/oauth/scopes`, `/workers/builds/deploy_hooks/{uuid}`, `/api/v4/health`, `/internal/submit`, `/live`, `/ready`, `/signed-url` | 1 each |

Many Zero Trust and Access methods exist in both forms; the published reference prints them once as `/{accounts_or_zones}/{account_or_zone_id}/...` (194 such method entries on the reference root), while the spec lists the `/accounts/{account_id}/...` and `/zones/{zone_id}/...` variants separately.
Find IDs in the dashboard: search "Copy account ID", or the API section of a domain's Overview page for the zone ID (https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
`GET /zones?account.id=$ACCOUNT_ID` lists zones of one account (https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/).

## 5. Request conventions

Source: https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/

- Send JSON bodies with `Content-Type: application/json` (as in the docs' examples, for example the OAuth client and R2 bucket calls).
- Quote URLs that contain query strings, and use double quotes in shells so `$ACCOUNT_ID` and `$CLOUDFLARE_API_TOKEN` expand.
- Keep the zone ID, account ID and token in environment variables scoped to the session or user; never commit tokens.
- Windows Command Prompt needs double quotes and `""` escaping; PowerShell uses `Invoke-RestMethod` with a headers hashtable.
- Example:

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?per_page=100&page=2" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" | jq .
```

## 6. Response envelope and errors

Sources: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/ (example response), the spec's `*_api-response-common` and `*_messages` schemas (counted 2026-10-05)

Successful responses look like:

```json
{
  "success": true,
  "errors": [],
  "messages": [],
  "result": { },
  "result_info": { "page": 1, "per_page": 20, "count": 1, "total_count": 200, "total_pages": 10 }
}
```

- `success` is `true` or `false`; failure schemas require `success`, `errors`, `messages` and `result` (with `result: null`).
- Each message or error object has an integer `code` (minimum 1000) and a `message`; 51 of the spec's 94 `*_messages` schemas also allow `documentation_url` and `source.pointer`.
- A spec example failure is `{"code": 7003, "message": "No route for the URI"}`.
- `result_info` carries list metadata; some newer APIs return `count` and a `cursor` instead of page numbers (for example the audit logs v2 schema).
- HTTP 429 "Too Many Requests" signals rate limiting (section 8).
- API errors (JSON envelopes from `api.cloudflare.com`) are different from Cloudflare edge errors on your own sites (1xxx, 52x), which can also be returned as JSON or Markdown when the client sends `Accept: application/json` or `text/markdown` (https://developers.cloudflare.com/fundamentals/reference/error-responses/).
- Product-specific error code pages exist for the 10xxx list and redirect validation errors (https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/).
- Common token problems (inactive token, missing permission group, using the key syntax with a token, exceeding your own role) are listed at https://developers.cloudflare.com/fundamentals/api/troubleshooting/.

## 7. Pagination

Sources: https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/, spec parameter counts (2026-10-05)

- Page-based: `page=x` selects a page and `per_page=xx` sets its size; too large a `per_page` "may" time out.
- Ordering: `order` (attribute) and `direction` (`ASC` or `DESC`); available options are listed in each endpoint's `result_info` documentation.
- The default page size in the docs' example is 20.
- Spec operations that declare each parameter: `per_page` 282, `page` 258, `limit` 146, `direction` 103, `order` 69, `cursor` 66, `offset` 38.
- So pagination is not uniform: page/per_page dominates, but cursor and limit/offset styles exist (for example audit logs v2 and several newer products).
- The `cf` CLI returns one page per list call and notes that paging options differ between commands (https://developers.cloudflare.com/cf/agents/).

## 8. Rate limits

Source: https://developers.cloudflare.com/fundamentals/api/reference/limits/ (last updated Aug 25, 2026)

| Limit | Value (as of 2026-10-05) |
| --- | --- |
| Client API per user or account token | 1,200 requests per 5 minutes |
| Client API per IP | 200 requests per second |
| GraphQL | Varies by query cost, maximum 320 per 5 minutes |
| User API tokens per user | 50 |
| Account API tokens per account | 500 |

- The 1,200 per five minutes limit is cumulative per user across dashboard, API key and API token traffic.
- Exceeding it blocks all API calls for the next five minutes with HTTP 429.
- Separately documented limits exist for Cache Purge, GraphQL, Rulesets, Lists and Gateway Lists APIs.
- Enterprise customers can ask Support to raise the per-user, GraphQL or token-count limits.
- Response headers: `Ratelimit` (for example `"default";r=50;t=30`, remaining quota and reset time), `Ratelimit-Policy` (for example `"burst";q=100;w=60`, quota and window) and, only when throttled, `retry-after` in seconds.
- The official SDKs read these headers and back off automatically.

## 9. Availability, plan and deprecation metadata in the spec

Counted from `raw/api/openapi.json` on 2026-10-05.

| Field | Counts |
| --- | --- |
| `x-fern-availability` | `generally-available` 2,682; `beta` 428; `deprecated` 360; `alpha` 7; not set 170 |
| `deprecated: true` | 336 operations (the `deprecated` column of `endpoints.tsv`) |
| `x-cfPlanAvailability` | all plans 975; Enterprise only 274; Pro, Business and Enterprise 100; Business and Enterprise 42; other combinations 4; not set on the rest |
| HTTP methods | GET 1,792; POST 770; DELETE 461; PUT 352; PATCH 272 |
| Tags | 578 distinct tags; the largest are Email Security Settings 53, dos-flowtrackd-api_other 45, Radar HTTP 41, Event 35, R2 Bucket 34, Brand Protection 33 |
| `x-fern-sdk-group-name` | 1,248 distinct SDK groups (for example `dns.records`, `ai-search`, `agent-memory`) |
| `x-forge-commands` | A top-level extension with 74 command groups and descriptions (for example `d1`, `r2`, `zones`, `zero-trust`, `k2`, `mcp`); 1,826 operations carry `x-forge-hidden`; the spec does not say which tool consumes it |
| Components | 6,993 schemas, 269 shared parameters, 145 shared responses |

The reference root marks 296 of its method entries as Deprecated (301 "Deprecated" markers in the page).
The recent deprecation timeline (Radar summaries, Zone Settings Batch API, Service Keys, Account Roles API, KV legacy routes and others) is tabulated in `platform-and-tooling.md` section 12.7 and lives at https://developers.cloudflare.com/fundamentals/api/reference/deprecations/ (RSS: `.../deprecations/index.xml`).

## 10. Headline counts

All counted on 2026-10-05 from the local mirror.

| Measure | Count | Source |
| --- | --- | --- |
| Spec operations | 3,647 | `raw/api/openapi.json`, `raw/api/endpoints.tsv` |
| Spec paths | 2,287 | same |
| Top-level resources in the reference | 128 | `raw/api/llms.txt` |
| Reference pages (resources and subresources) | 1,110 | `raw/api/llms.txt` |
| Method entries on the reference root | 2,824 (2,800 unique method plus path pairs) | `raw/docs/api/index.md` |
| Spec operations matched to a reference method (after expanding `{accounts_or_zones}`) | 2,911 | computed |
| Spec operations with no reference method | 736 | computed |
| Endpoints claimed for the API MCP server | "over 2,500"; table says 2,594 tools | https://developers.cloudflare.com/docs-for-agents/, https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/ |
| `cf` CLI commands | "more than 2,900" | https://developers.cloudflare.com/cf/ |

The 736 unmatched spec operations are concentrated in tags such as Brand Protection (48 across two tag spellings), Rules (25), Zone Settings (20), Artifacts (19), Priority Intelligence Requirements (15), Cloudflare Images Sourcing Kit (15), Issues (15), Event (14), Collections (13), Workflows (13), Memory (10), Workers (10), Monetization (10), Vectorize Beta (Deprecated) (10) and Load Balancer Pools (10).
In practice this means Agent Memory, Artifacts, K2, Monetization, pay-per-crawl and pay-per-use operations exist in the spec but have no top-level resource in the published reference (section 11).

## 11. Every top-level resource with operation counts

Sources: `raw/api/llms.txt` (resource list and page counts), `raw/docs/api/index.md` (method entries and Deprecated markers), `raw/api/endpoints.tsv` (spec matches).
Rows are in the order the reference root prints them.
"Pages" counts the resource page plus its subresource pages in `llms.txt`.
"Methods" counts method entries listed on https://developers.cloudflare.com/api/ for that resource, and "Deprecated" counts those marked Deprecated.
"Spec ops" counts distinct spec operations whose method and path match one of that resource's reference methods, after expanding `{accounts_or_zones}/{account_or_zone_id}` into the account and zone variants; it can exceed "Methods" because of that expansion, and can fall below it when the reference lists a path the spec spells differently.
Each resource's page is `https://developers.cloudflare.com/api/resources/<key>/`.

| # | Resource key | Title | Pages | Methods | Deprecated | Spec ops |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `accounts` | Accounts | 23 | 50 | 2 | 50 |
| 2 | `organizations` | Organizations | 8 | 15 | 0 | 15 |
| 3 | `tenants` | Tenants | 5 | 5 | 0 | 5 |
| 4 | `origin_ca_certificates` | Origin CA Certificates | 1 | 4 | 0 | 4 |
| 5 | `ips` | IPs | 1 | 1 | 0 | 1 |
| 6 | `memberships` | Memberships | 1 | 4 | 0 | 4 |
| 7 | `user` | User | 15 | 24 | 5 | 24 |
| 8 | `zones` | Zones | 19 | 43 | 4 | 43 |
| 9 | `load_balancers` | Load Balancers | 12 | 35 | 0 | 41 |
| 10 | `cache` | Cache | 6 | 32 | 8 | 32 |
| 11 | `ssl` | SSL | 10 | 16 | 1 | 16 |
| 12 | `acm` | ACM | 3 | 7 | 0 | 6 |
| 13 | `analytics_query` | Analytics Query | 4 | 6 | 0 | 6 |
| 14 | `argo` | Argo | 3 | 4 | 0 | 4 |
| 15 | `certificate_authorities` | Certificate Authorities | 2 | 2 | 0 | 2 |
| 16 | `client_certificates` | Client Certificates | 1 | 5 | 0 | 5 |
| 17 | `custom_certificates` | Custom Certificates | 2 | 6 | 0 | 6 |
| 18 | `custom_csrs` | Custom Csrs | 1 | 4 | 0 | 8 |
| 19 | `custom_hostnames` | Custom Hostnames | 5 | 11 | 0 | 11 |
| 20 | `custom_nameservers` | Account Custom Nameservers | 1 | 3 | 0 | 3 |
| 21 | `tenant_custom_nameservers` | Tenant Custom Nameservers | 1 | 3 | 0 | 3 |
| 22 | `dns_firewall` | DNS Firewall | 5 | 9 | 2 | 9 |
| 23 | `dns` | DNS | 23 | 62 | 3 | 62 |
| 24 | `email_security` | Email Security | 24 | 66 | 2 | 66 |
| 25 | `email_auth` | Email Auth | 4 | 3 | 0 | 3 |
| 26 | `email_routing` | Email Routing | 6 | 23 | 3 | 23 |
| 27 | `email_sending` | Email Sending | 4 | 14 | 0 | 14 |
| 28 | `filters` | Filters | 1 | 7 | 7 | 7 |
| 29 | `firewall` | Firewall | 10 | 37 | 22 | 41 |
| 30 | `healthchecks` | Healthchecks | 2 | 9 | 0 | 9 |
| 31 | `keyless_certificates` | Keyless Certificates | 1 | 5 | 0 | 5 |
| 32 | `logpush` | Logpush | 11 | 22 | 0 | 34 |
| 33 | `logs` | Logs | 12 | 15 | 0 | 22 |
| 34 | `origin_tls_client_auth` | Origin TLS Client Auth | 5 | 16 | 4 | 12 |
| 35 | `page_rules` | Page Rules | 1 | 6 | 0 | 6 |
| 36 | `rate_limits` | Rate Limits | 1 | 5 | 5 | 5 |
| 37 | `smart_shield` | Smart Shield | 3 | 10 | 0 | 10 |
| 38 | `waiting_rooms` | Waiting Rooms | 7 | 23 | 0 | 24 |
| 39 | `web3` | Web3 | 5 | 12 | 0 | 12 |
| 40 | `workers` | Workers | 27 | 70 | 0 | 70 |
| 41 | `kv` | KV | 5 | 16 | 3 | 13 |
| 42 | `durable_objects` | Durable Objects | 3 | 2 | 0 | 2 |
| 43 | `containers` | Containers | 8 | 15 | 1 | 15 |
| 44 | `queues` | Queues | 5 | 25 | 0 | 25 |
| 45 | `api_gateway` | API Gateway | 22 | 42 | 14 | 42 |
| 46 | `managed_transforms` | Managed Transforms | 1 | 3 | 0 | 3 |
| 47 | `page_shield` | Page Shield | 5 | 13 | 0 | 13 |
| 48 | `rulesets` | Rulesets | 5 | 15 | 0 | 30 |
| 49 | `url_normalization` | URL Normalization | 1 | 3 | 0 | 3 |
| 50 | `spectrum` | Spectrum | 9 | 9 | 0 | 9 |
| 51 | `addressing` | Addressing | 13 | 38 | 2 | 38 |
| 52 | `dls` | Data Localization Suite | 4 | 7 | 0 | 7 |
| 53 | `audit_logs` | Audit Logs | 1 | 1 | 0 | 1 |
| 54 | `billing` | Billing | 9 | 18 | 3 | 15 |
| 55 | `brand_protection` | Brand Protection | 10 | 17 | 0 | 17 |
| 56 | `diagnostics` | Diagnostics | 3 | 6 | 0 | 6 |
| 57 | `images` | Images | 8 | 17 | 1 | 17 |
| 58 | `intel` | Intel | 19 | 33 | 4 | 33 |
| 59 | `magic_transit` | Magic Transit | 23 | 96 | 0 | 96 |
| 60 | `ddos_protection` | DDoS Protection | 17 | 39 | 0 | 39 |
| 61 | `magic_network_monitoring` | Magic Network Monitoring | 7 | 14 | 0 | 14 |
| 62 | `magic_cloud_networking` | Magic Cloud Networking | 7 | 33 | 0 | 33 |
| 63 | `network_interconnects` | Network Interconnects | 5 | 15 | 0 | 15 |
| 64 | `mtls_certificates` | MTLS Certificates | 2 | 5 | 0 | 5 |
| 65 | `pages` | Pages | 8 | 24 | 0 | 24 |
| 66 | `registrar` | Registrar | 8 | 16 | 3 | 16 |
| 67 | `registrar_sandbox` | Registrar Sandbox | 5 | 10 | 0 | 10 |
| 68 | `request_tracers` | Rules Trace | 2 | 1 | 0 | 1 |
| 69 | `rules` | Rules Lists | 4 | 11 | 0 | 11 |
| 70 | `stream` | Stream | 17 | 43 | 0 | 43 |
| 71 | `alerting` | Alerting | 9 | 22 | 0 | 22 |
| 72 | `d1` | D1 | 3 | 12 | 0 | 12 |
| 73 | `r2` | R2 | 17 | 43 | 0 | 43 |
| 74 | `r2_data_catalog` | R2 Data Catalog | 6 | 12 | 12 | 12 |
| 75 | `basin_catalog` | Basin Catalog | 6 | 12 | 0 | 12 |
| 76 | `workers_for_platforms` | Workers For Platforms | 10 | 21 | 0 | 21 |
| 77 | `zero_trust` | Zero Trust | 176 | 467 | 21 | 503 |
| 78 | `turnstile` | Turnstile | 2 | 6 | 0 | 6 |
| 79 | `connectivity` | Connectivity | 3 | 5 | 0 | 5 |
| 80 | `hyperdrive` | Hyperdrive | 2 | 7 | 0 | 7 |
| 81 | `rum` | RUM | 3 | 10 | 0 | 10 |
| 82 | `vectorize` | Vectorize | 3 | 14 | 0 | 14 |
| 83 | `url_scanner` | URL Scanner | 3 | 8 | 0 | 8 |
| 84 | `vulnerability_scanner` | Vulnerability Scanner | 5 | 21 | 0 | 21 |
| 85 | `radar` | Radar | 120 | 281 | 131 | 278 |
| 86 | `bot_management` | Bot Management | 2 | 4 | 0 | 4 |
| 87 | `fraud` | Fraud | 1 | 2 | 0 | 2 |
| 88 | `precursor` | Precursor | 1 | 2 | 0 | 2 |
| 89 | `origin_post_quantum_encryption` | Origin Post Quantum Encryption | 1 | 2 | 2 | 2 |
| 90 | `origin_tls_compliance_modes` | Origin TLS Compliance Modes | 1 | 4 | 0 | 4 |
| 91 | `google_tag_gateway` | Google Tag Gateway | 2 | 2 | 0 | 2 |
| 92 | `zaraz` | Zaraz | 8 | 10 | 0 | 10 |
| 93 | `speed` | Speed | 5 | 10 | 0 | 10 |
| 94 | `dcv_delegation` | DCV Delegation | 1 | 1 | 0 | 1 |
| 95 | `hostnames` | Hostnames | 3 | 4 | 0 | 4 |
| 96 | `snippets` | Snippets | 3 | 9 | 0 | 8 |
| 97 | `realtime_kit` | Realtime Kit | 10 | 55 | 0 | 54 |
| 98 | `calls` | Calls | 3 | 10 | 0 | 10 |
| 99 | `moq` | MoQ | 3 | 8 | 0 | 8 |
| 100 | `managed_defense` | Cloudflare Managed Defense | 5 | 8 | 0 | 8 |
| 101 | `cloudforce_one` | Cloudforce One | 49 | 109 | 11 | 109 |
| 102 | `ai_gateway` | AI Gateway | 13 | 50 | 1 | 50 |
| 103 | `flagship` | Flagship | 5 | 12 | 0 | 12 |
| 104 | `iam` | IAM | 8 | 31 | 0 | 31 |
| 105 | `cloud_connector` | Cloud Connector | 2 | 2 | 0 | 2 |
| 106 | `botnet_feed` | Botnet Feed | 4 | 4 | 0 | 4 |
| 107 | `security_txt` | Security TXT | 1 | 3 | 0 | 3 |
| 108 | `workflows` | Workflows | 5 | 14 | 0 | 14 |
| 109 | `workers_builds` | Workers Builds | 10 | 28 | 0 | 28 |
| 110 | `resource_sharing` | Resource Sharing | 3 | 14 | 0 | 14 |
| 111 | `resource_tagging` | Resource Tagging | 6 | 10 | 0 | 10 |
| 112 | `leaked_credential_checks` | Leaked Credential Checks | 2 | 7 | 0 | 7 |
| 113 | `content_scanning` | Content Scanning | 3 | 10 | 0 | 8 |
| 114 | `ai_security` | AI Security | 2 | 4 | 0 | 4 |
| 115 | `csam_scanner` | Csam Scanner | 1 | 2 | 0 | 2 |
| 116 | `abuse_reports` | Abuse Reports | 4 | 8 | 0 | 8 |
| 117 | `ai` | AI | 9 | 11 | 0 | 11 |
| 118 | `ai_audit` | AI Audit | 2 | 2 | 0 | 2 |
| 119 | `ai_search` | AI Search | 8 | 46 | 12 | 46 |
| 120 | `autorag` | AutoRAG | 2 | 7 | 7 | 7 |
| 121 | `security_center` | Security Center | 8 | 9 | 0 | 17 |
| 122 | `browser_rendering` | Browser Rendering | 16 | 24 | 0 | 24 |
| 123 | `custom_pages` | Custom Pages | 2 | 8 | 0 | 16 |
| 124 | `secrets_store` | Secrets Store | 4 | 12 | 0 | 12 |
| 125 | `pipelines` | Pipelines | 3 | 14 | 0 | 19 |
| 126 | `schema_validation` | Schema Validation | 4 | 13 | 0 | 13 |
| 127 | `token_validation` | Token Validation | 4 | 14 | 0 | 14 |
| 128 | `field_extractors` | Field Extractors | 1 | 3 | 0 | 3 |

## 12. Every spec operation grouped by path

Source: `raw/api/endpoints.tsv` (3,647 operations, counted 2026-10-05).
Each row groups operations by scope and the first path segment after `/accounts/{account_id}/` or `/zones/{zone_id}/` (or by the root segment for other paths); "Deprecated" counts operations with the spec's `deprecated` flag.
This table covers every operation, including the 736 that the reference does not list.

| Scope:path segment | Operations | Deprecated |
| --- | --- | --- |
| `account:cloudforce-one` | 282 | 15 |
| `other:/radar` | 279 | 127 |
| `account:magic` | 177 | 0 |
| `account:workers` | 136 | 0 |
| `account:access` | 131 | 5 |
| `account:dlp` | 93 | 2 |
| `account:email-security` | 75 | 2 |
| `account:devices` | 74 | 9 |
| `account:ai-gateway` | 67 | 1 |
| `account:realtime` | 61 | 0 |
| `account:gateway` | 57 | 1 |
| `user:user` | 56 | 6 |
| `zone:settings` | 54 | 2 |
| `account:ai-search` | 49 | 13 |
| `account:stream` | 49 | 0 |
| `zone:access` | 44 | 0 |
| `zone:api_gateway` | 44 | 14 |
| `account:brand-protection` | 39 | 0 |
| `zone:email` | 38 | 11 |
| `account:builds` | 37 | 0 |
| `zone:firewall` | 37 | 23 |
| `account:addressing` | 36 | 2 |
| `account:data-security` | 36 | 1 |
| `account:load_balancers` | 36 | 0 |
| `account:r2` | 36 | 0 |
| `account:images` | 35 | 3 |
| `account:intel` | 35 | 5 |
| `account:dex` | 31 | 0 |
| `account:browser-rendering` | 27 | 0 |
| `account:email` | 26 | 8 |
| `account:alerting` | 25 | 0 |
| `account:vectorize` | 24 | 10 |
| `account:pages` | 23 | 0 |
| `account:queues` | 23 | 2 |
| `account:workflows` | 23 | 0 |
| `zone:cache` | 23 | 10 |
| `zone:waiting_rooms` | 23 | 0 |
| `account:vuln_scanner` | 22 | 0 |
| `account:logpush` | 20 | 0 |
| `account:shares` | 20 | 0 |
| `account:artifacts` | 19 | 0 |
| `account:pipelines` | 19 | 5 |
| `account:security-center` | 18 | 0 |
| `other:/organizations` | 18 | 0 |
| `account:iam` | 17 | 0 |
| `account:scim` | 17 | 0 |
| `account:basin-catalog` | 16 | 0 |
| `account:cni` | 16 | 0 |
| `account:logs` | 16 | 1 |
| `account:mnm` | 16 | 0 |
| `account:r2-catalog` | 16 | 16 |
| `account:registrar` | 16 | 3 |
| `account:rulesets` | 16 | 0 |
| `zone:rulesets` | 16 | 0 |
| `account:ai` | 15 | 0 |
| `account:containers` | 15 | 1 |
| `account:secondary_dns` | 15 | 0 |
| `account:zerotrust` | 15 | 0 |
| `zone:schema_validation` | 15 | 0 |
| `zone:security-center` | 15 | 0 |
| `zone:token_validation` | 15 | 0 |
| `account:agent-memory` | 14 | 0 |
| `account:flagship` | 14 | 0 |
| `account:storage` | 14 | 1 |
| `account:teamnet` | 14 | 3 |
| `account:urlscanner` | 14 | 6 |
| `zone:dns_records` | 14 | 1 |
| `zone:logpush` | 14 | 0 |
| `account:pay-per-crawl` | 13 | 0 |
| `account:rum` | 13 | 0 |
| `zone:logs` | 13 | 1 |
| `zone:origin_tls_client_auth` | 13 | 0 |
| `zone:page_shield` | 13 | 0 |
| `zone:secondary_dns` | 13 | 0 |
| `account:cfd_tunnel` | 12 | 0 |
| `account:d1` | 12 | 0 |
| `account:secrets_store` | 12 | 0 |
| `account:slurper` | 12 | 0 |
| `zone:ssl` | 12 | 1 |
| `zone:web3` | 12 | 0 |
| `account:billing` | 11 | 0 |
| `account:dns_settings` | 11 | 0 |
| `account:one` | 11 | 0 |
| `account:rules` | 11 | 0 |
| `account:warp_connector` | 11 | 0 |
| `account:zt_risk_scoring` | 11 | 0 |
| `zone:custom_hostnames` | 11 | 0 |
| `account:abuse-reports` | 10 | 0 |
| `account:calls` | 10 | 0 |
| `account:registrar-sandbox` | 10 | 0 |
| `zone:smart_shield` | 10 | 0 |
| `zone:speed_api` | 10 | 0 |
| `account:accounts (root)` | 9 | 0 |
| `account:custom_pages` | 9 | 0 |
| `account:dns_firewall` | 9 | 2 |
| `account:infrastructure` | 9 | 1 |
| `account:pay-per-use` | 9 | 0 |
| `account:pcaps` | 9 | 0 |
| `account:subscriptions` | 9 | 0 |
| `zone:custom_pages` | 9 | 0 |
| `zone:healthchecks` | 9 | 0 |
| `zone:spectrum` | 9 | 0 |
| `account:hyperdrive` | 8 | 0 |
| `account:managed-defense` | 8 | 0 |
| `account:moq` | 8 | 0 |
| `account:tokens` | 8 | 0 |
| `other:/tenants` | 8 | 0 |
| `zone:content-upload-scan` | 8 | 0 |
| `zone:environments` | 8 | 0 |
| `zone:monetization` | 8 | 0 |
| `zone:snippets` | 8 | 0 |
| `account:autorag` | 7 | 0 |
| `account:browser-extension` | 7 | 0 |
| `account:dls` | 7 | 0 |
| `account:oauth_clients` | 7 | 0 |
| `account:resource-library` | 7 | 0 |
| `account:tags` | 7 | 0 |
| `zone:zones (root)` | 7 | 2 |
| `zone:filters` | 7 | 7 |
| `zone:leaked-credential-checks` | 7 | 0 |
| `zone:origin` | 7 | 0 |
| `zone:pagerules` | 7 | 1 |
| `zone:pay-per-use` | 7 | 0 |
| `account:analytics` | 6 | 0 |
| `account:challenges` | 6 | 0 |
| `account:diagnostics` | 6 | 0 |
| `account:k2` | 6 | 0 |
| `account:payment-methods` | 6 | 0 |
| `account:reporting` | 6 | 0 |
| `account:sso_connectors` | 6 | 0 |
| `zone:acm` | 6 | 0 |
| `zone:custom_certificates` | 6 | 0 |
| `zone:load_balancers` | 6 | 0 |
| `zone:observability` | 6 | 0 |
| `account:connectivity` | 5 | 0 |
| `account:event_subscriptions` | 5 | 0 |
| `account:firewall` | 5 | 0 |
| `account:members` | 5 | 0 |
| `account:mtls_certificates` | 5 | 0 |
| `zone:addressing` | 5 | 0 |
| `zone:client_certificates` | 5 | 0 |
| `zone:hold` | 5 | 0 |
| `zone:keyless_certificates` | 5 | 0 |
| `zone:rate_limits` | 5 | 5 |
| `zone:workers` | 5 | 0 |
| `account:botnet_feed` | 4 | 0 |
| `account:custom_csrs` | 4 | 0 |
| `account:event_notifications` | 4 | 0 |
| `account:triggers` | 4 | 0 |
| `other:/certificates` | 4 | 0 |
| `other:/memberships` | 4 | 0 |
| `zone:ai-security` | 4 | 0 |
| `zone:argo` | 4 | 0 |
| `zone:bot_management` | 4 | 0 |
| `zone:custom_csrs` | 4 | 0 |
| `zone:dnssec` | 4 | 0 |
| `zone:hostnames` | 4 | 0 |
| `zone:intel` | 4 | 0 |
| `zone:pay-per-crawl` | 4 | 0 |
| `zone:subscription` | 4 | 0 |
| `account:billable` | 3 | 0 |
| `account:custom_ns` | 3 | 0 |
| `account:field_extractors` | 3 | 0 |
| `account:settings` | 3 | 0 |
| `other:/analytics` | 3 | 0 |
| `other:/pages` | 3 | 0 |
| `zone:managed_headers` | 3 | 0 |
| `zone:subscriptions` | 3 | 0 |
| `zone:tags` | 3 | 0 |
| `zone:url_normalization` | 3 | 0 |
| `account:analytics_engine` | 2 | 0 |
| `account:billable-usage` | 2 | 0 |
| `account:monetization` | 2 | 0 |
| `account:profile` | 2 | 0 |
| `account:roles` | 2 | 2 |
| `other:/billing` | 2 | 0 |
| `zone:ai-audit` | 2 | 0 |
| `zone:analytics` | 2 | 0 |
| `zone:available_plans` | 2 | 0 |
| `zone:certificate_authorities` | 2 | 0 |
| `zone:cloud_connector` | 2 | 0 |
| `zone:ct` | 2 | 0 |
| `zone:custom_ns` | 2 | 2 |
| `zone:devices` | 2 | 0 |
| `zone:dns_analytics` | 2 | 2 |
| `zone:dns_settings` | 2 | 0 |
| `zone:fraud_detection` | 2 | 0 |
| `zone:images` | 2 | 0 |
| `zone:precursor` | 2 | 0 |
| `account:argo` | 1 | 0 |
| `account:audit_logs` | 1 | 0 |
| `account:bulk` | 1 | 0 |
| `account:client-secret` | 1 | 0 |
| `account:dns_records` | 1 | 0 |
| `account:entitlements` | 1 | 0 |
| `account:invoices` | 1 | 0 |
| `account:media` | 1 | 0 |
| `account:move` | 1 | 0 |
| `account:organizations` | 1 | 0 |
| `account:pay-bad-debt` | 1 | 0 |
| `account:pay-invoice` | 1 | 0 |
| `account:receipts` | 1 | 0 |
| `account:request-tracer` | 1 | 0 |
| `account:tunnels` | 1 | 0 |
| `account:waiting_rooms` | 1 | 0 |
| `other:/api` | 1 | 0 |
| `other:/internal` | 1 | 0 |
| `other:/ips` | 1 | 0 |
| `other:/live` | 1 | 0 |
| `other:/oauth` | 1 | 0 |
| `other:/ready` | 1 | 0 |
| `other:/signed-url` | 1 | 0 |
| `other:/workers` | 1 | 0 |
| `zone:activation_check` | 1 | 0 |
| `zone:available_rate_plans` | 1 | 0 |
| `zone:dcv_delegation` | 1 | 0 |
| `zone:entitlements` | 1 | 0 |
| `zone:invalidate_cache` | 1 | 0 |
| `zone:media` | 1 | 0 |
| `zone:purge_cache` | 1 | 0 |
| `zone:rate_limit_analytics` | 1 | 1 |
| `zone:stream` | 1 | 0 |

## 13. Endpoints worth knowing for app builders

All from `raw/api/endpoints.tsv` (2026-10-05); availability values are the spec's `x-fern-availability`.

### 13.1 Tokens, identity and access

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/user/tokens/verify` | Verify a user token |
| GET | `/accounts/{account_id}/tokens/verify` | Verify an account token |
| GET | `/user/tokens/permission_groups` | Permission groups for user tokens |
| GET | `/accounts/{account_id}/tokens/permission_groups` | Permission groups for account tokens |
| POST | `/accounts/{account_id}/tokens` | Create an account-owned token (reference: https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/create/) |
| GET, POST | `/accounts/{account_id}/oauth_clients` | List or create OAuth clients (PATCH, DELETE and `rotate_secret` on `/{oauth_client_id}`) |
| GET | `/oauth/scopes` | List OAuth scopes |
| GET | `/accounts` | List accounts the credential can access |
| GET | `/zones` | List zones (filter `account.id`, `name`) |

### 13.2 Web3 gateways

| Method | Path | Notes |
| --- | --- | --- |
| GET, POST | `/zones/{zone_id}/web3/hostnames` | List or create Web3 hostnames; GA, available on all plans per `x-cfPlanAvailability` |
| GET, PATCH, DELETE | `/zones/{zone_id}/web3/hostnames/{identifier}` | Hostname details, edit, delete |
| GET, PUT | `/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list` | IPFS Universal Path gateway content list |
| GET, POST, PUT, DELETE | `.../ipfs_universal_path/content_list/entries[/{content_list_entry_identifier}]` | Content list entries |

The `target` field of a Web3 hostname accepts `ethereum`, `ipfs` or `ipfs_universal_path` (spec schema `web3_target`); the zone permission groups "Web3 Hostnames Read" and "Web3 Hostnames Write" cover these calls (https://developers.cloudflare.com/fundamentals/api/reference/permissions/).

### 13.3 Monetization, pay-per-crawl and pay-per-use

| Method | Path | Notes |
| --- | --- | --- |
| GET, POST | `/accounts/{account_id}/monetization` | Get or check Monetization Gateway eligibility (pending, approved or rejected); beta |
| GET, POST | `/zones/{zone_id}/monetization` | Zone eligibility; beta |
| GET, PUT, DELETE | `/zones/{zone_id}/monetization/rules` | Read, replace (desired state) or clear the zone's "Payment Required" ruleset; beta; GET returns 404 when no ruleset exists |
| GET, PATCH, DELETE | `/zones/{zone_id}/monetization/rules/{rule_id}` | One payment rule |
| various | `/accounts/{account_id}/pay-per-crawl/...`, `/zones/{zone_id}/pay-per-crawl/...` | Crawler and publisher Stripe configs, terms, zone config (13 account plus 4 zone operations) |
| various | `/accounts/{account_id}/pay-per-use/...`, `/zones/{zone_id}/pay-per-use/...` | Operator configuration, price proposals, usage reports and stats (9 account plus 7 zone operations) |

None of these appear as a top-level resource in the published reference (section 10).
No `wallet`, `wallets` or `x402` path exists in the spec (searched 2026-10-05).

### 13.4 Bot defense and edge config

| Method | Path | Notes |
| --- | --- | --- |
| GET, POST | `/accounts/{account_id}/challenges/widgets` | List or create Turnstile widgets |
| GET, PUT, DELETE | `/accounts/{account_id}/challenges/widgets/{sitekey}` | Widget details, update, delete |
| POST | `/accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret` | Rotate a widget secret |
| PATCH | `/zones/{zone_id}/settings/content_converter` | Turn on Markdown for Agents (`{"value":"on"}`) per https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ |
| GET, PATCH | `/zones/{zone_id}/settings/{setting_id}` | Per-setting reads and edits that replace the deprecated batch endpoints |

### 13.5 Developer platform

| Area | Example paths |
| --- | --- |
| D1 | `GET/POST /accounts/{account_id}/d1/database`, `POST .../d1/database/{database_id}/query`, `.../raw`, `.../export`, `.../import` |
| Workers | `/accounts/{account_id}/workers/scripts/...`, `/accounts/{account_id}/workers/...` (136 operations under `workers`) |
| Builds | `/accounts/{account_id}/builds/...` (37) and `POST /workers/builds/deploy_hooks/{deploy_hook_uuid}`, whose spec security accepts either a token or an empty requirement (no credentials) |
| R2 | `/accounts/{account_id}/r2/...` (36) |
| KV | `/accounts/{account_id}/storage/kv/namespaces/...` (14 operations under `storage`) |
| Queues, Workflows, Vectorize, Hyperdrive, Pipelines | `/accounts/{account_id}/queues`, `/workflows`, `/vectorize`, `/hyperdrive`, `/pipelines` |
| AI | `/accounts/{account_id}/ai/...`, `/ai-gateway/...`, `/ai-search/...`, `/agent-memory/...` |
| Temporary accounts | `api.cloudflare.com/client/v4/provisioning/previews` is documented at https://developers.cloudflare.com/workers/platform/claim-deployments/ but is not in the spec |

## 14. SDK languages and reference URL structure

Sources: `raw/api/llms.txt`, https://developers.cloudflare.com/api/, https://developers.cloudflare.com/fundamentals/api/reference/sdks/

The reference index says the links point to "language-neutral HTTP documentation".
It says SDK-specific docs "follow the same URL structure with the language inserted after the base path: `/{language}/resources/...`".
It lists "Available languages: http, typescript, python, go, terraform."

| Language | Reference root | Package (version as of 2026-10-05) |
| --- | --- | --- |
| http | https://developers.cloudflare.com/api/resources/... | curl examples |
| typescript | https://developers.cloudflare.com/api/typescript | `npm install cloudflare` (7.3.0) |
| python | https://developers.cloudflare.com/api/python | `pip install cloudflare` (5.9.0) |
| go | https://developers.cloudflare.com/api/go | `github.com/cloudflare/cloudflare-go/v7` (v7.12.0) |
| terraform | https://developers.cloudflare.com/api/terraform | `cloudflare/cloudflare` provider (5.26.0, `~> 5.0`) |

Method page URLs follow `https://developers.cloudflare.com/api/resources/<resource>/subresources/<sub>/methods/<method>/`, for example `.../api/resources/dns/subresources/records/methods/create/`.
The fundamentals SDKs page lists only Go, TypeScript and Python as SDKs and treats Terraform separately.
The libraries are generated from the OpenAPI spec, and minor releases may contain breaking renames (https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/).
Other clients of the same API: the `cf` CLI (`cf schema <command>` prints the operationId, method and path a command calls), Pulumi, and the Code Mode MCP server; see `platform-and-tooling.md`.

## 15. Looking up any endpoint locally

Run these from the repository root; all were tested on 2026-10-05, and a jq query takes about 1 second on the 26 MB spec.

Find operations by keyword:

```sh
grep -i 'turnstile' raw/api/endpoints.tsv | cut -f1-5
grep -P '\td1-' raw/api/endpoints.tsv            # by operationId prefix
awk -F'\t' '$1=="DELETE" && $2 ~ /\/r2\//' raw/api/endpoints.tsv
awk -F'\t' 'NR>1 && $6!=""' raw/api/endpoints.tsv | cut -f1-2   # deprecated operations
```

Count operations and paths:

```sh
awk -F'\t' 'NR>1' raw/api/endpoints.tsv | wc -l                    # 3647
awk -F'\t' 'NR>1{print $2}' raw/api/endpoints.tsv | sort -u | wc -l # 2287
```

Inspect one operation in the spec:

```sh
jq '.paths["/accounts/{account_id}/d1/database"].post | {operationId, summary, security, "x-fern-availability", "x-cfPlanAvailability"}' raw/api/openapi.json
jq -r '.paths["/accounts/{account_id}/d1/database"].post.requestBody' raw/api/openapi.json
```

List every beta operation:

```sh
jq -r '.paths | to_entries[] | .key as $p | .value | to_entries[] | select(.value|type=="object") | select(.value["x-fern-availability"]=="beta") | "\(.key|ascii_upcase) \($p)"' raw/api/openapi.json
```

Resolve a schema reference:

```sh
jq '.components.schemas["web3_target"]' raw/api/openapi.json
```

Find the reference page that documents a path (the resource pages print `METHOD/path` with escaped underscores):

```sh
grep -rl 'POST/accounts/{account\\_id}/d1/database$' raw/api/resources
```

Read a resource's models and methods: open `raw/api/resources/<key>/index.md` or the live URL `https://developers.cloudflare.com/api/resources/<key>/index.md` (Markdown), and the SDK view at `https://developers.cloudflare.com/api/<language>/resources/<key>/`.
Python, for bulk questions:

```python
import json
spec = json.load(open("raw/api/openapi.json"))
ops = [(m.upper(), p, o) for p, v in spec["paths"].items() for m, o in v.items()
       if m in ("get", "post", "put", "patch", "delete")]
print(len(ops))  # 3647
```

From the CLI side, `cf cli search "<task>"` then `cf schema <command>` maps a task to the exact operation without the spec (https://developers.cloudflare.com/cf/agents/).

## 16. Build hooks for Web3 projects

How the API itself can help launch dapps and token projects on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
The API spec has no chain-specific endpoints beyond the Web3 hostname gateways (targets `ethereum`, `ipfs`, `ipfs_universal_path`); everything else is chain-agnostic infrastructure.

- **Launch-day automation in one script.** A single account token can create the zone records (`/zones/{zone_id}/dns_records`), deploy the Worker (`/accounts/{account_id}/workers/scripts/...`), create the D1 allowlist database (`/d1/database`) and R2 media bucket (`/r2/buckets`), and create a Turnstile widget (`/challenges/widgets`), so a token or NFT launch can be reproduced per chain from CI.
- **Least privilege per chain or per environment.** Use token policies with explicit `deny` and per-zone resources so the Solana launch site's token cannot touch the Base site's zone; add client IP filtering for CI runners and a `notAfter` for launch-week tokens (section 3.4).
- **Respect rate limits in bots and indexers.** Automation that writes many DNS records or KV keys around a launch draws on the 1,200 per five minutes budget, which the limits note says is cumulative per user across dashboard and API traffic; read `Ratelimit` and `retry-after`, back off on 429, and test whether separate account tokens get separate budgets before relying on that (section 8 and section 17).
- **Ethereum and IPFS gateways via the API.** Create a Web3 hostname with target `ethereum` or `ipfs`/`ipfs_universal_path` to serve dapp frontends or metadata from a custom domain, and manage the IPFS universal path content list (blocklist or allowlist entries) programmatically (section 13.2).
  The spec offers no Solana, Base or Robinhood Chain gateway target.
- **Paywalled APIs and agent payments.** The beta Monetization endpoints manage a zone's "Payment Required" rules, which pairs with the x402 material in the Agents docs (Base, Ethereum, Solana and other networks listed; Robinhood Chain not listed) for charging agents per call to a token-data or analytics API (section 13.3; https://developers.cloudflare.com/agents/tools/payments/x402/).
- **Agent-operated infrastructure.** Because the Code Mode MCP server wraps this same API in about 1,000 tokens, a launch agent can answer "which DNS records point at the old RPC proxy" or "rotate the Turnstile secret" through `search()` and `execute()` with a scoped token (https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/).
- **Verify before you trust.** Scripts should call `/user/tokens/verify` or `/accounts/{account_id}/tokens/verify` at start, fail fast on `success: false`, and log `errors[].code` and `documentation_url` (sections 3.3 and 6).

## 17. Gaps and contradictions

- **Counts disagree across sources.** The spec has 3,647 operations on 2,287 paths, the reference root lists 2,824 method entries, Docs for agents says "over 2,500 endpoints", the MCP catalog says 2,594 tools, and `cf` says "more than 2,900 commands"; none of the pages say which inventory they count.
- **736 spec operations are not in the reference.** After expanding combined account-or-zone paths, 736 spec operations match no reference method, including whole products (Agent Memory, Artifacts, K2, Monetization, pay-per-crawl, pay-per-use) that have docs pages but no API reference resource.
- **Reference paths the spec spells differently.** For `kv` (16 methods, 13 matches), `billing` (18, 15), `origin_tls_client_auth` (16, 12), `content_scanning` (10, 8), `snippets` (9, 8), `acm` (7, 6) and `radar` (281, 278) some reference paths have no exact spec match, so either the reference or the spec carries a path the other lacks.
- **Deprecated counts differ.** The spec flags 336 operations `deprecated`, `x-fern-availability` says 360, and the reference root marks 296 method entries (301 markers).
- **Service Key auth after its end of life.** The deprecations page removes Service Key auth on September 30, 2026, but on 2026-10-05 the spec still lists `user_service_key` on 83 operations and the Origin CA keys page still documents it.
- **Key-only security on 220 operations.** The spec lists only email plus Global API Key for 220 operations (including `secrets_store`, `iam`, `organizations`, `pay-per-crawl`), while the overview says to use tokens "whenever possible"; whether tokens work there is not stated.
- **Workers Observability operations have no security block.** Forty operations under `/accounts/{account_id}/workers/observability/` declare no `security` and fall back to the spec default.
- **Internal and test routes in the public spec.** `/internal/submit` ("Internal route for testing URL submissions"), `/live`, `/ready` and `/signed-url` ("Internal route for testing signed URLs") are in the spec under brand protection and logo match tags.
- **GraphQL not in the spec.** The analytics GraphQL endpoint and its 320 per five minutes limit are documented in the docs but absent from the OpenAPI spec.
- **Provisioning API not in the spec.** The temporary-account provisioning endpoint `/provisioning/previews` is documented for claim deployments but has no spec operation.
- **SDK list differs.** The fundamentals SDKs page lists Go, TypeScript and Python, while the reference lists five languages including http and terraform, and the "Make API calls" page lists Go, TypeScript, Python and Terraform as first-party libraries.
- **Broken links in the spec description.** The spec and the overview page link to `/fundamentals/basic-tasks/interact-with-cloudflare/` and send rate-limit readers to a Workers for Platforms limits page; neither page exists in the 2026-10-05 mirror, and the canonical limits page is https://developers.cloudflare.com/fundamentals/api/reference/limits/.
- **Rate limit unit is ambiguous.** The limits table says 1,200 per 5 minutes "per user/account token", while the note under it says the limit is 1,200 per five minutes "per user" and applies cumulatively regardless of dashboard, API key or API token (https://developers.cloudflare.com/fundamentals/api/reference/limits/).
- **Pagination is inconsistent.** Page and per_page, limit and offset, and cursor styles all appear; the docs describe only page and per_page.
- **Edit versus Write permission names.** The permissions page prints each group twice with "Edit" and "Write" names, and the OAuth page says scope names match token permission names without saying which spelling.
- **FedRAMP API base.** `cf` supports a `fedramp-high` compliance region and a Gateway table lists `api.fed.cloudflare.com`, but no API page documents an alternative base URL.
- **`x-forge-commands` is undocumented.** The spec ships a 74-group command tree under `x-forge-commands` with no description of its consumer; it does not match the `cf` CLI's groups one to one (for example it has no `dns` or `workers` group).
