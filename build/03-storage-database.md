# Build > Storage & Database

This file covers the developers.cloudflare.com sidebar dropdown Build > Storage & Database as mirrored on 2026-10-05: R2, Basin (with its sub-dropdown Basin Pipelines, Basin Catalog and Basin SQL), K2, D1, KV, Hyperdrive and Artifacts, plus Secrets Store, which is not in this dropdown but is where apps keep keys.
Source: `raw/nav/home-sidebar.md` lines 43 to 54 and the per-product `raw/docs/<product>/` trees.
The big moves as of 2026-10-05 are that Cloudflare Data Platform was renamed Basin and went GA on 2026-10-01 (Pipelines, R2 Data Catalog and R2 SQL became Basin Pipelines, Basin Catalog and Basin SQL), that K2 is a new durable log in public beta, and that Artifacts (Git-compatible versioned storage) went to open beta on 2026-10-01 with billing starting 2026-10-14.
R2 remains the zero-egress object store underneath Basin, D1 is the serverless SQLite database (10 GB per database), KV is the eventually consistent edge key-value cache, and Hyperdrive pools and caches connections to existing Postgres and MySQL databases (MySQL GA on 2026-08-07).
Every price, limit and status below is a snapshot as of 2026-10-05 and cites the page it came from; contradictions between pages are collected at the end rather than resolved.

## Table of contents

1. [Sidebar map and status at a glance](#1-sidebar-map-and-status-at-a-glance)
2. [R2 object storage](#2-r2-object-storage)
3. [Basin (overview)](#3-basin-overview)
4. [Basin Pipelines](#4-basin-pipelines)
5. [Basin Catalog](#5-basin-catalog)
6. [Basin SQL](#6-basin-sql)
7. [K2 durable log](#7-k2-durable-log)
8. [D1 serverless SQL](#8-d1-serverless-sql)
9. [Workers KV](#9-workers-kv)
10. [Hyperdrive](#10-hyperdrive)
11. [Artifacts](#11-artifacts)
12. [Secrets Store](#12-secrets-store)
13. [Comparison table across all storage products](#13-comparison-table-across-all-storage-products)
14. [How Cloudflare says to choose](#14-how-cloudflare-says-to-choose)
15. [Build hooks for Web3 projects](#15-build-hooks-for-web3-projects)
16. [Gaps and contradictions](#16-gaps-and-contradictions)

## 1. Sidebar map and status at a glance

The sidebar lists, in order: R2, Basin (Overview, Basin Pipelines, Basin Catalog, Basin SQL), K2, D1, KV, Hyperdrive, Artifacts (`raw/nav/home-sidebar.md`).
Secrets Store is not in this dropdown.

| Product | Docs root | Pages mirrored | Status as of 2026-10-05 | Plan |
| --- | --- | --- | --- | --- |
| R2 | https://developers.cloudflare.com/r2/ | 84 | GA (no beta label on the overview); Local Uploads announced as open beta 2026-02-03 | Free tier plus paid usage |
| Basin overview | https://developers.cloudflare.com/basin/ | 7 | GA since 2026-10-01 | Workers Paid plus R2 |
| Basin Pipelines | https://developers.cloudflare.com/basin-pipelines/ | 39 | GA (formerly Cloudflare Pipelines) | Workers Paid |
| Basin Catalog | https://developers.cloudflare.com/basin-catalog/ | 17 | GA (formerly R2 Data Catalog) | R2 subscription plus payment card |
| Basin SQL | https://developers.cloudflare.com/basin-sql/ | 15 | GA (formerly R2 SQL) | R2 subscription plus payment card |
| K2 | https://developers.cloudflare.com/k2/ | 9 | Public beta, 10 GB per account | Workers Paid only |
| D1 | https://developers.cloudflare.com/d1/ | 54 | GA (read replication announced as public beta 2025-04-10) | Free and Paid |
| KV | https://developers.cloudflare.com/kv/ | 32 | GA; namespace jurisdictions GA 2026-10-02 | Free and Paid |
| Hyperdrive | https://developers.cloudflare.com/hyperdrive/ | 64 | GA; MySQL GA 2026-08-07 | Free and Paid |
| Artifacts | https://developers.cloudflare.com/artifacts/ | 32 | Open beta since 2026-10-01; billing from 2026-10-14 | Workers Paid only |
| Secrets Store | https://developers.cloudflare.com/secrets-store/ | 7 | Open beta | All accounts see it; roles gate use |

Status sources: https://developers.cloudflare.com/basin/, https://developers.cloudflare.com/k2/, https://developers.cloudflare.com/artifacts/platform/changelog/, https://developers.cloudflare.com/secrets-store/, https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/, https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/, https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/, https://developers.cloudflare.com/d1/platform/release-notes/.

## 2. R2 object storage

### What it is

R2 is S3-compatible object storage with no egress fees, strongly consistent and designed for eleven nines of durability (https://developers.cloudflare.com/r2/how-r2-works/).
The overview pitches it for cloud-native app storage, web content, podcast episodes, data lakes and ML artifacts (https://developers.cloudflare.com/r2/).

### Architecture

R2 is built from four components (https://developers.cloudflare.com/r2/how-r2-works/):
- **R2 Gateway**: the entry point for every API request, deployed across the network as Workers, handling auth and routing.
- **Metadata Service**: built on Durable Objects, stores object metadata (key, checksum) and enforces strong consistency, with its own cache layer.
- **Tiered Read Cache**: uses Cloudflare Tiered Cache in front of storage to serve reads closer to clients.
- **Distributed Storage Infrastructure**: persists encrypted object data.

A write is acknowledged with HTTP 200 only after data is replicated within the region and the Metadata Service commits the metadata (https://developers.cloudflare.com/r2/how-r2-works/).
Reads check metadata, then the tiered read cache, then regional storage (same page).

### Key concepts

- **Consistency**: read-after-write, metadata updates, deletes and list operations are strongly consistent globally; IAM permission changes are eventually consistent and can take up to a minute; concurrent writers to one key are last-writer-wins (https://developers.cloudflare.com/r2/reference/consistency/).
- **Caching caveat**: when a custom domain with caching fronts the bucket, consistency is relaxed: deleted objects stay cached, 404s are cached, and overwritten objects keep serving the old version until TTL or purge; Workers bindings and the S3 API bypass the cache (same page).
- **Durability**: 99.999999999% annual durability via replication and/or erasure coding across several data centers in a region, with synchronous writes; availability SLA is 99.9% (https://developers.cloudflare.com/r2/reference/durability/).
- **Storage classes**: Standard (default) and Infrequent Access, which has a 30-day minimum storage duration and retrieval fees; once an object is in Infrequent Access, lifecycle rules cannot move it back to Standard, but `CopyObject` with `x-amz-storage-class` can switch between `STANDARD` and `STANDARD_IA` (https://developers.cloudflare.com/r2/buckets/storage-classes/).
- **Data location**: Automatic placement by default, optional Location Hints (`wnam`, `enam`, `weur`, `eeur`, `apac`, `oc`) that are best effort and only honored the first time a bucket name is created, and Jurisdictional Restrictions (`eu`, `us`, `fedramp`) that are guaranteed and cannot be changed after creation (https://developers.cloudflare.com/r2/reference/data-location/).
- The `us` jurisdiction was added on 2026-08-17 (https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/).
- Jurisdictional buckets must be reached through `https://<ACCOUNT_ID>.<JURISDICTION>.r2.cloudflarestorage.com`, and the docs note most S3 clients then need one client per jurisdiction (https://developers.cloudflare.com/r2/api/tokens/).
- Logpush does not write to jurisdictional buckets directly; the documented workaround is a Logpush job targeting the S3-compatible endpoint (https://developers.cloudflare.com/r2/reference/data-location/).

### API and binding surface

R2 has three client interfaces: the Workers binding, the S3-compatible API and the Cloudflare REST API (which powers the dashboard and Wrangler) (https://developers.cloudflare.com/r2/how-r2-works/).

**Workers binding** (https://developers.cloudflare.com/r2/api/workers/workers-api-usage/):

```jsonc
{
  "r2_buckets": [
    { "binding": "MY_BUCKET", "bucket_name": "<YOUR_BUCKET_NAME>" }
  ]
}
```

For a jurisdictional bucket, add `"jurisdiction": "<JURISDICTION>"` to the binding (https://developers.cloudflare.com/r2/reference/data-location/).

Bucket methods documented in https://developers.cloudflare.com/r2/api/workers/workers-api-reference/:
- `head(key)` returns `Promise<R2Object | null>`.
- `get(key, options?)` returns `Promise<R2ObjectBody | R2Object | null>`, with `onlyIf` conditionals, `range` (offset, length, suffix) and `ssecKey`.
- `put(key, value, options?)` accepts `ReadableStream | ArrayBuffer | ArrayBufferView | string | null | Blob`, with `onlyIf`, `httpMetadata`, `customMetadata`, checksums (`md5`, `sha1`, `sha256`, `sha384`, `sha512`), `storageClass` and `ssecKey`.
- `delete(key | key[])`.
- `list(options?)` with `limit`, `prefix`, `cursor`, `delimiter`, `include`, returning `objects`, `truncated`, `cursor`, `delimitedPrefixes`; the docs warn to loop on `truncated`, not on a count.
- `createMultipartUpload(key, options?)` and `resumeMultipartUpload(key, uploadId)`, with `uploadPart`, `abort` and `complete` on the upload object.
- `R2Object` exposes `key`, `version`, `size`, `etag`, `httpEtag`, `uploaded`, `httpMetadata`, `customMetadata`, `range`, `checksums`, `storageClass` and `ssecKeyMd5`, plus `writeHttpMetadata(headers)`.

**S3-compatible API** (https://developers.cloudflare.com/r2/api/s3/api/):
- Endpoint `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`; region is `auto`, and an empty region or `us-east-1` aliases to `auto`.
- Implemented bucket operations include `ListBuckets`, `HeadBucket`, `CreateBucket`, `DeleteBucket`, the CORS, lifecycle, location and encryption get/put calls.
- Implemented object operations include `HeadObject`, `ListObjects`, `ListObjectsV2` (recommended over V1), `GetObject`, `PutObject`, `DeleteObject`, `DeleteObjects`, the multipart set (`CreateMultipartUpload`, `UploadPart`, `UploadPartCopy`, `CompleteMultipartUpload`, `AbortMultipartUpload`, `ListMultipartUploads`, `ListParts`) and `CopyObject`, with conditional headers and SSE-C.
- Not implemented: ACLs, bucket policies, versioning, replication, object lock configuration, tagging (`Get/Put/DeleteObjectTagging`), website hosting, notifications via the S3 API, inventory, analytics and intelligent tiering, plus `x-amz-expected-bucket-owner` and `x-amz-request-payer` everywhere.
- Uploading to the same part number replaces the previous part, and if the replacement fails the original part is lost.
- Checksums: CRC-64/NVME supports `FULL_OBJECT`; CRC32, CRC32C, SHA-1 and SHA-256 support `COMPOSITE` (same page); CRC-64/NVME arrived 2025-07-03 (https://developers.cloudflare.com/r2/platform/release-notes/).
- R2 extensions to S3 include Unicode metadata, `cf-create-bucket-if-missing` on `PutObject` and `CreateMultipartUpload`, a `MERGE` metadata directive on `CopyObject`, paginated `ListBuckets` headers, and destination conditional operations on `CopyObject`, the last one marked beta (https://developers.cloudflare.com/r2/api/s3/extensions/).

**Presigned URLs** (https://developers.cloudflare.com/r2/api/s3/presigned-urls/):
- Generated client-side with SigV4 and no call to R2, for `GET`, `HEAD`, `PUT` or `DELETE` on one object, valid from 1 second to 7 days (604,800 seconds).
- HTML form `POST` uploads are not supported.
- They only work on the S3 API domain, not on custom domains; for custom domains the docs point to WAF HMAC validation (Pro plan or above).
- Restricting `Content-Type` in the signature makes uploads with another type fail with `403 SignatureDoesNotMatch`.

**Temporary credentials** grant several S3 operations scoped to a bucket, a set of actions and optionally paths, with a `ttlSeconds`, either through the Temporary Credentials API or by local signing (https://developers.cloudflare.com/r2/api/s3/temporary-credentials/).

**API tokens and permissions** (https://developers.cloudflare.com/r2/api/tokens/):
- Account API tokens or User API tokens, created under R2 > Manage API tokens; you must purchase R2 first.
- Permission levels: Admin Read & Write, Admin Read only, Object Read & Write, Object Read only; object-level tokens can be scoped to buckets and only work with the S3 API, not the Cloudflare REST API.
- Basin Catalog needs an Admin level token (read-only works for reads).
- API permission groups include `Workers R2 Storage Write`, `Workers R2 Storage Read`, and bucket item groups; bucket resources are written as `com.cloudflare.edge.r2.bucket.<ACCOUNT_ID>_<JURISDICTION>_<BUCKET_NAME>` with `default` for non-jurisdictional buckets.

**REST API**: rate limited to 1,200 requests per five minutes per account across all R2 REST operations, so high-throughput object work should use S3 or the binding (https://developers.cloudflare.com/r2/platform/limits/).

### Public access

- Buckets are private by default; public access is via a custom domain (a zone in the same account, full or partial CNAME setup) or a managed `r2.dev` subdomain (https://developers.cloudflare.com/r2/buckets/public-buckets/).
- `r2.dev` is for development only, is rate limited ("hundreds of requests/second" before 429s) and may be bandwidth throttled; WAF, caching, Access and Bot Management only work behind a custom domain (https://developers.cloudflare.com/r2/platform/limits/).
- Disable `r2.dev` when protecting a bucket with WAF or Access, otherwise it stays public there (https://developers.cloudflare.com/r2/buckets/public-buckets/).
- Only some file types are cached by default; a Cache Everything rule caches all; Smart Tiered Cache gives a single upper tier next to the bucket (same page).
- Public buckets do not list contents at the domain root (same page).
- Minimum TLS version and cipher suites of a custom domain are set through the custom domain API (same page).
- Up to 100 custom domains per bucket (https://developers.cloudflare.com/r2/platform/limits/).

### Event notifications and event subscriptions

- Event notifications push messages to a Queue when objects change; consume with a Worker or HTTP pull (https://developers.cloudflare.com/r2/buckets/event-notifications/).
- Event types: `object-create` (`PutObject`, `CopyObject`, `CompleteMultipartUpload`) and `object-delete` (`DeleteObject`, `LifecycleDeletion`).
- Rules can filter on `prefix` and `suffix`; up to 100 rules per bucket; overlapping rules that would fire twice for one event are rejected.
- Message body fields: `account`, `action`, `bucket`, `object.key`, `object.size`, `object.eTag` (size and eTag absent on deletes), `eventTime`, and `copySource` for copies.
- Queues throughput is 5,000 messages per second per queue, so the docs recommend splitting rules across queues above that rate.
- Setup: `npx wrangler r2 bucket notification create <BUCKET_NAME> --event-type <EVENT_TYPE> --queue <QUEUE_NAME> [--prefix ...] [--suffix ...]`.
- Event notifications went GA on 2024-09-26 (https://developers.cloudflare.com/r2/platform/release-notes/).
- Separately, account-level event subscriptions publish `bucket.created` and `bucket.deleted`, and Super Slurper job events (`job.started`, `job.paused`, `job.resumed`, `job.completed`, `job.aborted`, `job.object.migrated`) (https://developers.cloudflare.com/r2/platform/event-subscriptions/).

### Bucket features

- **Object lifecycles**: up to 1,000 rules; delete by age or date, transition to Infrequent Access, abort incomplete multipart uploads; objects are usually removed within 24 hours of expiry; every bucket has a default rule aborting multipart uploads after seven days; a transition costs a Class A operation; delete wins over transition when both land within 24 hours (https://developers.cloudflare.com/r2/buckets/object-lifecycles/).
- **Bucket locks**: up to 1,000 prefix rules locking objects for an age (`maxAgeSeconds`) or indefinitely, preventing deletion and overwrite; jurisdictional buckets need a `cf-r2-jurisdiction` header on the API call (https://developers.cloudflare.com/r2/buckets/bucket-locks/).
- **CORS**: configurable per bucket, including for presigned URL use from browsers (https://developers.cloudflare.com/r2/buckets/cors/).
- **Local Uploads**: writes `PutObject` and `UploadPart` data near the client and replicates asynchronously, keeping objects immediately readable and strongly consistent; no extra cost beyond normal Class A operations; not supported on jurisdictional buckets; reads from the bucket's region can see cross-region latency until replication completes (https://developers.cloudflare.com/r2/buckets/local-uploads/).
- The Local Uploads announcement reports up to 75% lower time to last byte in Cloudflare's tests (https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/).
- **Data Access Logs**: per-request logs for object operations with status below 400, from the S3, API, Workers and Public interfaces, viewed in Workers Observability with seven-day retention; best effort, not a complete record; not available for jurisdictional buckets; Cloudflare Observability pricing applies from 2026-12-01 (https://developers.cloudflare.com/r2/buckets/data-access-logs/).
- **Audit logs** cover configuration changes, and **metrics** cover storage, operations and, since 2026-09-24, upload and download bandwidth (https://developers.cloudflare.com/r2/platform/audit-logs/, https://developers.cloudflare.com/changelog/post/2026-09-24-r2-bandwidth-metrics/).
- **Encryption**: AES-256 at rest and TLS in transit (https://developers.cloudflare.com/r2/reference/data-security/); SSE-C (customer-provided keys) has been available through the binding and S3 API since 2024-12-03 (https://developers.cloudflare.com/r2/examples/ssec/).
- **Unicode**: key names are NFC-normalized by default (https://developers.cloudflare.com/r2/reference/unicode-interoperability/).

### Data migration

- **Super Slurper** does one-off bulk copies from other clouds; objects over 1 TB are skipped (https://developers.cloudflare.com/r2/data-migration/super-slurper/).
- **Sippy** copies objects on demand when they are first requested, so migration egress rides on traffic you already pay for; GA since 2024-08-21 (https://developers.cloudflare.com/r2/data-migration/sippy/, https://developers.cloudflare.com/r2/platform/release-notes/).
- Sippy sources expanded to Azure Blob Storage and any S3-compatible provider on 2026-07-24, in addition to S3 and GCS (https://developers.cloudflare.com/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/).
- Both tools are free; you pay R2 Class A operations (Super Slurper single-operation uploads below 100 MiB, Sippy below 200 MiB) and whatever the source charges (https://developers.cloudflare.com/r2/pricing/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/r2/platform/limits/:

| Limit | Value |
| --- | --- |
| Storage per bucket | Unlimited |
| Objects per bucket | Unlimited |
| Buckets per account | 1,000,000 |
| Bucket management operations per bucket | 50 per second |
| Custom domains per bucket | 100 |
| Object key length | 1,024 bytes |
| Object metadata size | 8,192 bytes |
| Object size | 5 TiB per object in the table, 4.995 TiB per the footnote |
| Single-part upload | 5 GiB in the table, 4.995 GiB per the footnote |
| Multipart upload | 4.995 TiB, up to 10,000 parts |
| Concurrent writes to the same key | 1 per second (higher rates return 429) |
| REST API | 1,200 requests per 5 minutes per account |

A Worker's inbound request body is further limited by Workers request limits (same page).

### Pricing and egress (as of 2026-10-05)

From https://developers.cloudflare.com/r2/pricing/:

| | Standard | Infrequent Access |
| --- | --- | --- |
| Storage | $0.015 per GB-month | $0.01 per GB-month |
| Class A operations | $4.50 per million | $9.00 per million |
| Class B operations | $0.36 per million | $0.90 per million |
| Data retrieval | None | $0.01 per GB |
| Egress to Internet | Free | Free |

- Monthly free tier (Standard only): 10 GB-month storage, 1 million Class A, 10 million Class B.
- Class A includes `ListBuckets`, `PutBucket`, `ListObjects`, `PutObject`, `CopyObject`, the multipart calls, `LifecycleStorageTierTransition` and bucket config puts.
- Class B includes `HeadBucket`, `HeadObject`, `GetObject`, `UsageSummary` and bucket config gets.
- `DeleteObject`, `DeleteBucket` and `AbortMultipartUpload` are free.
- Usage is rounded up to the next billing unit (one million and one operations bills as two million).
- GB-month averages peak daily storage over 30 days.
- Egress through the binding, S3 API and `r2.dev` is free; other metered Cloudflare services in front of R2 may charge.
- Requests that fail with 401 Unauthorized are not billed.
- The page's asset-hosting example (100,000 files, 10 million reads per day) costs $104.40 per month, all of it Class B reads.

### Data catalog

There is no longer a data catalog section inside the R2 tree; `raw/docs/r2/llms.txt` lists "Basin Catalog" and "Basin SQL" and links out to https://developers.cloudflare.com/basin-catalog/ and https://developers.cloudflare.com/basin-sql/.
The R2 pricing page also defers catalog pricing to Basin Catalog (https://developers.cloudflare.com/r2/pricing/).
See sections 5 and 6.

### Most useful R2 pages

- Overview: https://developers.cloudflare.com/r2/
- How R2 works: https://developers.cloudflare.com/r2/how-r2-works/
- Get started (dashboard, CLI, S3, Workers): https://developers.cloudflare.com/r2/get-started/
- Workers API reference: https://developers.cloudflare.com/r2/api/workers/workers-api-reference/
- S3 API compatibility: https://developers.cloudflare.com/r2/api/s3/api/
- Presigned URLs: https://developers.cloudflare.com/r2/api/s3/presigned-urls/
- Temporary credentials: https://developers.cloudflare.com/r2/api/s3/temporary-credentials/
- Tokens: https://developers.cloudflare.com/r2/api/tokens/
- Public buckets: https://developers.cloudflare.com/r2/buckets/public-buckets/
- Event notifications: https://developers.cloudflare.com/r2/buckets/event-notifications/
- Consistency: https://developers.cloudflare.com/r2/reference/consistency/
- Data location: https://developers.cloudflare.com/r2/reference/data-location/
- Limits: https://developers.cloudflare.com/r2/platform/limits/
- Pricing: https://developers.cloudflare.com/r2/pricing/
- SDK examples (aws CLI, aws-sdk-js-v3, boto3, Go, Java, Kotlin, .NET, PHP, Ruby, Rust, aws4fetch, s3mini, rclone, Terraform): https://developers.cloudflare.com/r2/examples/

## 3. Basin (overview)

### What it is

Basin is a serverless analytics data platform that ingests, transforms, manages and queries Apache Iceberg tables stored in R2 (https://developers.cloudflare.com/basin/).
It was formerly called Cloudflare Data Platform, and Cloudflare Pipelines, R2 Data Catalog and R2 SQL are now Basin Pipelines, Basin Catalog and Basin SQL; existing resources and configurations keep working (same page).
Basin became generally available on 2026-10-01 (https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/).
The data flow is Basin Pipelines (ingest and transform) into Basin Catalog (Iceberg tables in R2), queried by Basin SQL or any compatible external Iceberg engine (https://developers.cloudflare.com/basin/).

### Entry commands

```sh
npx wrangler basin pipelines setup
npx wrangler basin catalog enable YOUR_BUCKET_NAME
npx wrangler basin sql query YOUR_WAREHOUSE_NAME "SELECT * FROM default.events LIMIT 10"
```

Source: https://developers.cloudflare.com/basin/.

### Get-started path

The CLI guide builds `Worker -> Basin Pipelines -> Basin Catalog -> Basin SQL` for request analytics: create a Worker with C3, run `wrangler basin pipelines setup --name request_events`, bind the **stream ID** (not the pipeline ID) as a `pipelines` binding, call `env.EVENTS.send([{ path }])`, then query with `wrangler basin sql query` after setting `WRANGLER_BASIN_SQL_AUTH_TOKEN` (https://developers.cloudflare.com/basin/get-started/guide/).
Prerequisites are Workers Paid, R2 enabled, and an R2 Account API token with Admin Read & Write (same page).
There is also a page of agent prompts for building with Basin (https://developers.cloudflare.com/basin/get-started/prompting/).

### Combined pricing (as of 2026-10-05)

From https://developers.cloudflare.com/basin/platform/pricing/ (R2 storage and operations are billed separately):

| Product | Dimension | Monthly included | Over included |
| --- | --- | --- | --- |
| Pipelines | Stream ingress | Unlimited | Free |
| Pipelines | SQL transforms | 50 GB | $0.04 per GB |
| Pipelines | Sink delivery, JSON | 50 GB shared sink allowance | $0.03 per GB |
| Pipelines | Sink delivery, Parquet or Iceberg | 50 GB shared sink allowance | $0.06 per GB |
| Catalog | Catalog operations | 1 million | $9 per million |
| Catalog | Compaction data processed | 10 GB | $0.005 per GB |
| Catalog | Compaction objects processed | 1 million | $2 per million |
| SQL | Compressed data scanned | 10 GB | $0.0025 per GB ($2.50 per TB), 10 MB minimum per query |

The worked example (500 GB ingested, 300 GB to Iceberg, 500,000 catalog operations, 20 GB compaction, 50 GB scanned) totals $33.15 before R2 (same page).
Billing for all three was switched on for non-enterprise accounts on 2026-08-03 (https://developers.cloudflare.com/basin/ "What's new").

### Limits

Basin's platform page points to the Pipelines limits, SQL limitations and Catalog limitations rather than stating its own (https://developers.cloudflare.com/basin/platform/).

## 4. Basin Pipelines

### What it is

Basin Pipelines ingests events, transforms them with SQL and delivers them to R2 as Iceberg tables (via Basin Catalog) or as Parquet and JSON files, with durable ingestion and exactly-once delivery to R2 (https://developers.cloudflare.com/basin-pipelines/).
It requires the Workers Paid plan (same page).

### Key concepts

- **Streams** are durable, buffered queues that receive JSON events over HTTP or a Worker binding; one stream can feed several pipelines; a schema, if set, is validated (https://developers.cloudflare.com/basin-pipelines/streams/).
- Events that do not match a structured stream's schema are **accepted but dropped**, and unstructured streams store everything in a single `value` column (https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/).
- **Pipelines** connect streams to sinks with SQL (`INSERT INTO <sink> SELECT ... FROM <stream>`) to filter, enrich and restructure; multiple statements let one stream fan out to several tables (https://developers.cloudflare.com/basin-pipelines/pipelines/, https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/).
- **Sinks** write to Basin Catalog as Iceberg tables or to R2 as JSON or Parquet files, with exactly-once delivery and a configurable rolling policy (https://developers.cloudflare.com/basin-pipelines/sinks/).
- **Logpush as a source**: Logpush can deliver `http_requests`, `firewall_events`, `dns_logs` (zone) and `workers_trace_events` (account) into Pipelines, which auto-creates the stream, sink and SQL (https://developers.cloudflare.com/basin-pipelines/streams/logpush/).
- **Legacy pipelines** created before 2025-09-25 through the legacy API are on a deprecation path, JSON-only and without SQL; migrate by creating a new pipeline (https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/).

### API and binding surface

Binding (https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/):

```jsonc
{
  "pipelines": [
    { "binding": "STREAM", "stream": "<STREAM_ID>" }
  ]
}
```

```js
await env.STREAM.send(events); // array of JSON-serializable records
```

- The binding field `pipeline` was renamed to `stream` on 2026-05-27; the old field still works with a deprecation warning (https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/).
- `wrangler types` generates a typed record (for example `EcommerceStreamRecord`) from the stream schema, falling back to `Pipeline<PipelineRecord>` when not logged in, the stream is missing, or the stream is unstructured (https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/).
- HTTP ingest: `POST https://{stream-id}.ingest.cloudflare.com` with a JSON array; if auth is enabled, send `Authorization: Bearer` with a token holding **Basin Pipelines Send** (same page).
- Basin Catalog sink creation: `npx wrangler basin pipelines sinks create my-sink --type basin-catalog --bucket my-bucket --namespace my_namespace --table my_table --catalog-token ...`; the legacy type value `r2-data-catalog` still works; sinks create the table and cannot target an existing Iceberg table; Catalog sinks are Parquet only with `zstd` (default), `snappy`, `gzip`, `lz4` or no compression; roll interval default 300 seconds, minimum 60 seconds; roll size in MB; token needs R2 Admin Read & Write (https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/).
- SQL reference covers `SELECT` (WITH, FROM, WHERE, UNNEST, multiple statements), primitive, list and struct types, and scalar function families: array, binary string, conditional, hashing, JSON, math, regex, string, struct, time and date, other (https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/).
- Wrangler commands live under `wrangler basin pipelines` (`setup`, `list`, `streams ...`, `sinks ...`) (https://developers.cloudflare.com/basin-pipelines/reference/wrangler-commands/); Terraform and the REST API (`/api/resources/pipelines/`) are also documented.
- Metrics are queryable from the dashboard and GraphQL, including user error metrics for dropped events (https://developers.cloudflare.com/basin-pipelines/observability/metrics/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/basin-pipelines/platform/limits/:

| Limit | Value |
| --- | --- |
| Streams per account | 20 |
| Payload per ingestion request | 5 MB |
| Ingest rate per stream | 1 GB/s (raised from 5 MB/s on 2026-10-01) |
| Sinks per account | 20 |
| Pipelines per account | 20 |

### Pricing (as of 2026-10-05)

Ingress is free and unlimited; SQL transforms have 50 GB included then $0.04 per GB; sinks have 50 GB included then $0.03 per GB for JSON or $0.06 per GB for Parquet and Iceberg, measured on uncompressed data (https://developers.cloudflare.com/basin-pipelines/platform/pricing/).
Any query counts as a transform; future stateful operations (aggregations, joins, windows) "may be priced separately" (same page).

### Most useful pages

- https://developers.cloudflare.com/basin-pipelines/getting-started/
- https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/
- https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/
- https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2/
- https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/
- https://developers.cloudflare.com/basin-pipelines/platform/limits/

## 5. Basin Catalog

### What it is

Basin Catalog is a managed Apache Iceberg REST catalog built into an R2 bucket, so engines like Spark, Snowflake, Trino, DuckDB, PyIceberg, StarRocks and Basin SQL can read and write the same tables (https://developers.cloudflare.com/basin-catalog/).
It was formerly R2 Data Catalog; existing configurations and APIs "continue to work and will be deprecated in the future" (same page).

### Key concepts

- Enabling the catalog on a bucket yields a **Catalog URI** and **Warehouse name** for Iceberg clients (https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
- Disabling it immediately stops the catalog interface and makes table references inaccessible until re-enabled (same page).
- **Authentication**: engines need a Cloudflare API token with both Basin Catalog and R2 storage permissions; the catalog vends SigV4 credentials that inherit the token's R2 permissions, so a token with read-only catalog access but read-write R2 access can still write objects (same page).
- Read-only tokens have been supported since 2026-07-09 (https://developers.cloudflare.com/basin/ "What's new").
- **Table maintenance**: automatic **compaction** (binpacking Parquet files, target size 64 MB to 512 MB, default 128 MB, compacted files prefixed `compacted-`) and **snapshot expiration** (`--older-than-days`, default 30, and `--retain-last`, default 5; both conditions must hold) (https://developers.cloudflare.com/basin-catalog/table-maintenance/).
- Catalog-level maintenance needs an API token as a service credential; table-level does not (https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
- The dashboard **Maintenance** tab shows schedules and run history and can queue compaction manually (errors `40903` executor conflict, `42901` daily request limit) (https://developers.cloudflare.com/basin-catalog/table-maintenance/).
- Compaction also rewrites and clusters manifest files since 2026-07-13 (https://developers.cloudflare.com/basin/ "What's new").
- **Deleting data** must go through catalog transactions; deleting metadata or data files directly can corrupt the catalog; `DROP TABLE` keeps files, `DROP TABLE ... PURGE` deletes them irreversibly; copy-on-write and merge-on-read trade-offs are tabulated (https://developers.cloudflare.com/basin-catalog/deleting-data/).
- **R2 Local Uploads** can cut write latency for Iceberg clients outside the bucket region (https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

### API surface

```sh
npx wrangler basin catalog enable <BUCKET_NAME>
npx wrangler basin catalog get <BUCKET_NAME>
npx wrangler basin catalog compaction enable <BUCKET_NAME> [<NAMESPACE> <TABLE>] --target-size 128 --token <API_TOKEN>
npx wrangler basin catalog snapshot-expiration enable <BUCKET_NAME> --token <API_TOKEN> --older-than-days 7 --retain-last 10
```

Sources: https://developers.cloudflare.com/basin-catalog/manage-catalogs/, https://developers.cloudflare.com/basin-sql/query-data/.
Snapshot expiration commands need Wrangler 4.56.0 or later (https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
PyIceberg connects with `RestCatalog(name=..., warehouse=WAREHOUSE, uri=CATALOG_URI, token=TOKEN)` (https://developers.cloudflare.com/basin-catalog/get-started/).
Engine setup pages exist for DuckDB, PyIceberg, Snowflake, Spark (PySpark and Scala), StarRocks and Trino (https://developers.cloudflare.com/basin-catalog/config-examples/).
Metrics for REST operations and maintenance jobs come through the GraphQL Analytics API (https://developers.cloudflare.com/basin-catalog/observability/metrics/).

### Limits

- Buckets in a non-default jurisdiction are not supported (https://developers.cloudflare.com/basin-catalog/manage-catalogs/).
- Compaction only handles Parquet data files and does not clean up orphan files never referenced by a snapshot (https://developers.cloudflare.com/basin-catalog/table-maintenance/).

### Pricing (as of 2026-10-05)

Requires an active R2 subscription and a linked payment card; catalog operations 1 million included then $9 per million; compaction 10 GB included then $0.005 per GB processed and 1 million objects included then $2 per million; snapshot expiration is free (https://developers.cloudflare.com/basin-catalog/platform/pricing/).
The streaming example (20 MB/s for a month, about 50,625 GB) costs $1,012.31, of which R2 storage is $759.23 (same page).

## 6. Basin SQL

### What it is

Basin SQL is a serverless, distributed, read-only analytics query engine over Iceberg tables in Basin Catalog, using file pruning and Cloudflare's distributed compute; formerly R2 SQL, whose APIs "continue to work and will be deprecated in the future" (https://developers.cloudflare.com/basin-sql/).

### API surface

- Wrangler: `npx wrangler basin sql query <WAREHOUSE> "SELECT ..."`, reading the token from `WRANGLER_BASIN_SQL_AUTH_TOKEN` (https://developers.cloudflare.com/basin-sql/query-data/).
- HTTP: `POST https://api.sql.cloudflarestorage.com/api/v1/accounts/{ACCOUNT_ID}/basin-sql/query/{BUCKET_NAME}` with body `{"query": "..."}` and a bearer token (same page).
- Token: Basin SQL, Basin Catalog and R2 storage permissions; the example policy uses the groups `Workers R2 SQL Read`, `Workers R2 Data Catalog Write` and `Workers R2 Storage Write` (same page).
- Querying from the dashboard was added on 2026-07-08 (changelog post `2026-07-08-query-r2-sql-from-dashboard`).

### Supported SQL (as of 2026-10-05)

From https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/:
- Supported: `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, aliases, CASE/CAST/LIKE/BETWEEN/IN, `EXPLAIN` (text or JSON), scalar and aggregate function families, approximate aggregates (`approx_distinct`, `approx_median`, `approx_percentile_cont`, `approx_top_k`), struct, array and map columns, CTEs, all standard JOINs, subqueries (`IN`, `EXISTS`, scalar, derived tables), window functions with inline `OVER`, `QUALIFY`, `DISTINCT ON`, set operations, `GROUPING SETS`, `ROLLUP`, `CUBE`.
- Not supported: `OFFSET`, named `WINDOW`, any writes or DDL, `UNNEST`, `PIVOT`, `UNPIVOT`, wildcard modifiers, parenthesized joins, `LATERAL`, `PERCENTILE_DISC`, and `NOT IN` on nullable columns.
- Parquet only; `now()` is quantized to 10 ms in UTC.
- Memory-heavy functions (`MEDIAN`, `PERCENTILE_CONT`, `ARRAY_AGG`, `STRING_AGG`, any `DISTINCT` aggregate, window functions) are budget-gated and rejected up front with a 400 if they would scan too much.
- Error codes: 40003 syntax, 40004 invalid query, 80001 edge connection failure (retry).

### Pricing (as of 2026-10-05)

10 GB of compressed data scanned included per month, then $0.0025 per GB ($2.50 per TB), with a 10 MB minimum per query; failed queries and `EXPLAIN`, `SHOW`, `DESCRIBE` are free of scan charges; file reads count as R2 Class B operations (https://developers.cloudflare.com/basin-sql/platform/pricing/).

### Most useful pages

- https://developers.cloudflare.com/basin-sql/query-data/
- https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/
- https://developers.cloudflare.com/basin-sql/sql-reference/
- https://developers.cloudflare.com/basin-sql/tutorials/end-to-end-pipeline/ (a fraud-detection style transaction pipeline)
- https://developers.cloudflare.com/basin-sql/troubleshooting/

## 7. K2 durable log

### What it is

K2 is a serverless durable log: produce records to a stream, keep them for a configurable retention period, and consume them from one or more independent subscriptions (https://developers.cloudflare.com/k2/).
It is in **public beta** as of 2026-10-05, requires Workers Paid, and caps each account at 10 GB stored during the beta (same page).

### Key concepts

From https://developers.cloudflare.com/k2/concepts/ and https://developers.cloudflare.com/k2/get-started/:
- **Stream**: an ordered, durable, append-only log; reads advance an offset rather than removing items, so slow readers never block writes, many readers can consume everything, and history can be replayed until the TTL removes it.
- **Record**: binary `content` (base64 over HTTP) plus optional string `headers`, up to 1 MB combined.
- **Batch**: producers append in batches, written atomically (all or nothing); timestamps are set by the server and cannot be overridden.
- **Subscription**: tracks a position, starts at `earliest` or `latest`, and is immutable once created; several consumers can share a subscription (each gets a subset) or use separate subscriptions (each gets everything).
- **Lease**: `/consume` leases a batch to a `worker_id` for five minutes; the consumer must `ack` or `nack` before expiry, or the records are redelivered, giving **at-least-once** delivery.
- K2 does **not** deduplicate, so retried produces can store duplicates, and ordering is not guaranteed across workers that share a subscription (https://developers.cloudflare.com/k2/features/consume/).

### API and binding surface

Control plane (needs `K2 Config Write` to create, update, delete, `K2 Config Read` to get or list) (https://developers.cloudflare.com/k2/configuration/):

```sh
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/k2/streams" \
  --request POST --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"name":"orders","http":{"enabled":true,"authentication":true}}'
```

- Stream settings: `name` (1 to 128 letters, digits, underscores, case-insensitive, not renamable), `retention_seconds` (3,600 to 2,592,000, default 604,800), `http` (`enabled`, `authentication`, `cors.origins` up to five or `*`) and `worker_binding` (default enabled); at least one input must stay enabled; `PATCH` replaces whole input objects (same page).
- If `http.authentication` is not true, anyone who knows the stream ID can produce (same page).
- Data plane base URL: `https://<STREAM_ID>.k2.cloudflarestorage.com` (https://developers.cloudflare.com/k2/get-started/).
- Produce over HTTP: `POST /produce` with `{"records":[{"content":"<base64>","headers":{...}}]}`; standard padded base64 only; gzip with `Content-Encoding: gzip` allowed; token needs `K2 Produce` (https://developers.cloudflare.com/k2/features/produce/).
- Browser producers must use an unauthenticated stream plus CORS, because tokens in browser code are readable; validate records in consumers (same page).
- Worker binding: `"k2": [{ "binding": "ORDERS", "stream": "<STREAM_ID>" }]`, then `await env.ORDERS.send([{ content: Uint8Array, headers }])`; `send()` returns `{ success, error: { code, message, retryable } }` instead of throwing; string content is not accepted (same page).
- Deploy-time binding errors: `10399` bad stream field, `10400` stream not in account, `10401` no permission, `10402` validation failed (same page).
- Consume (token needs `K2 Consume`): `POST /subscriptions` (`name`, `start_at.type`), `POST /subscriptions/<id>/consume` (`worker_id`, `max_records` 1 to 10,000), `POST /subscriptions/<id>/batches/<batch_id>/ack`, `/nack` and `/extend`; list, get by name, get and delete subscriptions with `GET` and `DELETE` (https://developers.cloudflare.com/k2/features/consume/).
- Retry produce only when `retryable` is true; `10212` means the outcome is unknown; retry consume errors `10211`, `10214`, `10216`, `10217` with backoff (https://developers.cloudflare.com/k2/features/produce/, https://developers.cloudflare.com/k2/features/consume/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/k2/platform/limits/:

| Limit | Value |
| --- | --- |
| Account storage during beta | 10 GB across all streams |
| Streams per account | 20 |
| Retention | 1 hour minimum, 30 days maximum, 7 days default (longer by request) |
| Request size | 5 MB (before and after gzip decompression) |
| Record size | about 1 MB (content plus headers) |
| Headers per record | 32 (name 256 bytes, value 8 KiB, total 64 KiB) |
| `max_records` per consume | 10,000 |
| Data per consume response | 10 MB |
| Active leases per subscription | 128 |
| Subscriptions per stream | 100 |

### Pricing

No K2 pricing page exists in the mirror (`raw/docs/k2/llms.txt` lists only overview, get started, concepts, configuration, consume, produce and limits).

## 8. D1 serverless SQL

### What it is

D1 is Cloudflare's managed serverless database with SQLite SQL semantics, built-in disaster recovery, and Worker and HTTP API access, priced only on queries and storage so you can create many small databases (https://developers.cloudflare.com/d1/).
Each database is backed by a single Durable Object and is single-threaded, so throughput is roughly the inverse of query duration (1 ms queries give about 1,000 queries per second) (https://developers.cloudflare.com/d1/platform/limits/).

### Key concepts

- **Horizontal scale-out**: D1 is designed for many 10 GB databases (per user, tenant or entity), and the 10 GB per-database limit cannot be raised (https://developers.cloudflare.com/d1/platform/limits/).
- **Global read replication**: read-only replicas in every supported region, used only through the **Sessions API** (`withSession()`), which gives sequential consistency within a session via bookmarks; writes always go to the primary; no extra charge for replicas (https://developers.cloudflare.com/d1/best-practices/read-replication/).
- Session start modes: `withSession()` or `"first-unconstrained"` (any instance), `"first-primary"` (latest data), or a stored bookmark (at least as fresh as a previous session); `meta.served_by_region` and `meta.served_by_primary` report where a query ran (same page).
- Enable replication in the dashboard or with `PUT /accounts/{account_id}/d1/database/{database_id}` and `{"read_replication":{"mode":"auto"}}` (needs `D1:Edit`); disabling can take up to 24 hours to drain (same page).
- **Time Travel**: point-in-time restore to any minute in the retention window using bookmarks (https://developers.cloudflare.com/d1/reference/time-travel/).
- **Data location**: location hints (`wnam`, `enam`, `weur`, `eeur`, `apac`, `oc`) and jurisdictions (`eu`, `us`, `fedramp`); jurisdictions are set at creation only and override hints (https://developers.cloudflare.com/d1/configuration/data-location/).
- **Retries**: since 2025-09-11 D1 retries read-only queries (`SELECT`, `EXPLAIN`, `WITH`) up to twice; writes should still be retried in your own code (https://developers.cloudflare.com/d1/platform/release-notes/, https://developers.cloudflare.com/d1/best-practices/retry-queries/).

### API and binding surface

```jsonc
"d1_databases": [
  { "binding": "DB", "database_name": "prod-d1-tutorial", "database_id": "<unique-ID-for-your-database>" }
]
```

Source (binding name adapted from the tutorial's `prod_d1_tutorial`): https://developers.cloudflare.com/d1/get-started/.

- `D1Database` methods: `prepare()`, `batch()`, `exec()`, `dump()`, `withSession()`; `D1DatabaseSession` adds `getBookmark()`, `prepare()`, `batch()` (https://developers.cloudflare.com/d1/worker-api/d1-database/).
- Prepared statement methods: `bind()`, `run()`, `raw()`, `first()` (https://developers.cloudflare.com/d1/worker-api/prepared-statements/).
- Every result carries a `meta` object with `duration`, `rows_read`, `rows_written`, `size_after` and the served-by fields, which is how you estimate billing (https://developers.cloudflare.com/d1/platform/pricing/).
- Wrangler: `wrangler d1 create`, `list`, `info`, `delete`, `execute`, `export`, `insights`, `migrations create|list|apply`, `time-travel info|restore` (https://developers.cloudflare.com/d1/wrangler-commands/).
- REST API: database CRUD and `/query` and `/raw` endpoints (https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/create/); REST authentication moved to the nearest data center on 2025-05-30, cutting 50 to 500 ms (https://developers.cloudflare.com/d1/platform/release-notes/).
- SQL surface: SQLite statements, PRAGMAs and extensions, JSON functions, foreign keys, generated columns (https://developers.cloudflare.com/d1/sql-api/sql-statements/).
- Use `STRICT` tables to avoid type mismatches, since D1 converts JavaScript parameter types one way (https://developers.cloudflare.com/d1/worker-api/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/d1/platform/limits/:

| Limit | Workers Paid | Free |
| --- | --- | --- |
| Databases per account | 50,000 (raisable to millions) | 10 |
| Database size | 10 GB | 500 MB |
| Storage per account | 1 TB (raisable) | 5 GB |
| Time Travel window | 30 days | 7 days |
| Queries per Worker invocation | 1,000 | 50 |
| Columns per table | 100 | 100 |
| String, BLOB or row size | 2 MB | 2 MB |
| SQL statement length | 100 KB | 100 KB |
| Bound parameters per query | 100 | 100 |
| Query duration | 30 seconds | 30 seconds |
| `d1 execute` file import | 5 GB | 5 GB |
| Simultaneous connections per Worker invocation | 6 | 6 |

Per-statement limits apply to each statement inside `batch()` (same page).

### Pricing (as of 2026-10-05)

From https://developers.cloudflare.com/d1/platform/pricing/:

| | Workers Free | Workers Paid |
| --- | --- | --- |
| Rows read | 5 million per day | 25 billion per month included, then $0.001 per million |
| Rows written | 100,000 per day | 50 million per month included, then $1.00 per million |
| Storage | 5 GB total | 5 GB included, then $0.75 per GB-month |

- Rows read counts rows scanned, not returned, so indexes cut cost; indexes add a written row per indexed write.
- No egress or compute charge from D1 itself; dashboard and Wrangler queries are billable; an empty database uses about 12 KB.
- Since 2026-09-01, Free plan queries fail once daily row limits are exceeded (https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/).

### Most useful pages

- https://developers.cloudflare.com/d1/get-started/
- https://developers.cloudflare.com/d1/worker-api/
- https://developers.cloudflare.com/d1/best-practices/read-replication/
- https://developers.cloudflare.com/d1/best-practices/use-indexes/
- https://developers.cloudflare.com/d1/reference/migrations/
- https://developers.cloudflare.com/d1/reference/time-travel/
- https://developers.cloudflare.com/d1/platform/limits/
- https://developers.cloudflare.com/d1/platform/pricing/
- https://developers.cloudflare.com/workflows/examples/backup-d1/ (export to R2 with Workflows)

## 9. Workers KV

### What it is

Workers KV is a global, low-latency key-value store optimized for very high read volumes: data lives in a few central stores and is cached in Cloudflare data centers after access (https://developers.cloudflare.com/kv/, https://developers.cloudflare.com/kv/concepts/how-kv-works/).

### Key concepts

- **Eventual consistency**: changes are usually visible immediately in the location that wrote them (not guaranteed) and can take 60 seconds or more elsewhere; negative lookups are cached too (https://developers.cloudflare.com/kv/concepts/how-kv-works/).
- Hot reads typically see 500 µs to 10 ms latency (https://developers.cloudflare.com/workers/platform/storage-options/).
- **Not for** atomic operations, transactions, or Redis-style hot keys written many times per second; the docs suggest routing writes through a Durable Object, or using Durable Objects instead (https://developers.cloudflare.com/kv/concepts/how-kv-works/).
- **cacheTtl**: integer of at least 30 seconds, default 60 (https://developers.cloudflare.com/kv/api/read-key-value-pairs/); the minimum dropped from 60 to 30 on 2026-01-30 (https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/).
- **Expiration**: `expiration` (epoch seconds) or `expirationTtl` (seconds from now), minimum 60 seconds in the future (https://developers.cloudflare.com/kv/api/write-key-value-pairs/).
- **Jurisdictions** (`eu`, `us`, `fedramp`) control only where data is durably stored; data can still be cached and read worldwide; set only at namespace creation; GA since 2026-10-02 (https://developers.cloudflare.com/kv/reference/data-location/, https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/).
- **Event subscriptions** publish `cf.kv.namespace.created` and `cf.kv.namespace.deleted` to a Queue (https://developers.cloudflare.com/kv/platform/event-subscriptions/).

### API and binding surface

```jsonc
"kv_namespaces": [ { "binding": "KV", "id": "<YOUR_BINDING_ID>" } ]
```

```ts
await env.KV.put('KEY', 'VALUE');
const value = await env.KV.get('KEY');
const allKeys = await env.KV.list();
await env.KV.delete('KEY');
```

Source: https://developers.cloudflare.com/kv/.

- `get(key, type | { cacheTtl, type })` with types `text`, `json`, `arrayBuffer`, `stream`; `get(keys[])` reads up to 100 keys (text or json) into a `Map`, with a 25 MB response cap (https://developers.cloudflare.com/kv/api/read-key-value-pairs/).
- `getWithMetadata()` has the same shapes and returns `{ value, metadata }` (same page).
- `put(key, value, { expiration, expirationTtl, metadata })` (https://developers.cloudflare.com/kv/api/write-key-value-pairs/).
- `list({ prefix, limit, cursor })` returns up to 1,000 keys per call with `list_complete` and `cursor` (https://developers.cloudflare.com/kv/api/list-keys/).
- `delete(key)`; bulk writes and deletes are not available on the binding, only via Wrangler or the REST API, which accepts up to 10,000 pairs per call (https://developers.cloudflare.com/kv/api/delete-key-value-pairs/).
- REST routes live under `/accounts/{account_id}/storage/kv/namespaces/*`; the legacy `/accounts/{account_id}/workers/namespaces/*` routes were deprecated on 2026-07-15 and **stop working on 2026-10-15** (https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/kv/platform/limits/:

| Limit | Free | Paid |
| --- | --- | --- |
| Reads | 100,000 per day | Unlimited |
| Writes to different keys | 1,000 per day | Unlimited |
| Writes to the same key | 1 per second | 1 per second |
| Operations per Worker invocation | 1,000 | 1,000 |
| Namespaces per account | 1,000 | 1,000 |
| Storage per account and per namespace | 1 GB | Unlimited |
| Key size | 512 bytes | 512 bytes |
| Key metadata | 1,024 bytes | 1,024 bytes |
| Value size | 25 MiB | 25 MiB |
| Minimum cacheTtl | 30 seconds | 30 seconds |

### Pricing (as of 2026-10-05)

From https://developers.cloudflare.com/kv/platform/pricing/:

| | Free (daily) | Paid (monthly included, then) |
| --- | --- | --- |
| Keys read | 100,000 | 10 million, then $0.50 per million |
| Keys written | 1,000 | 1 million, then $5.00 per million |
| Keys deleted | 1,000 | 1 million, then $5.00 per million |
| List requests | 1,000 | 1 million, then $5.00 per million |
| Stored data | 1 GB | 1 GB, then $0.50 per GB-month |

Billing is per key, bulk reads bill each key, reads of missing keys are billed, dashboard and Wrangler operations are billed, and there is no egress charge (same page).

### Most useful pages

- https://developers.cloudflare.com/kv/get-started/
- https://developers.cloudflare.com/kv/concepts/how-kv-works/
- https://developers.cloudflare.com/kv/api/read-key-value-pairs/
- https://developers.cloudflare.com/kv/api/write-key-value-pairs/
- https://developers.cloudflare.com/kv/platform/limits/
- https://developers.cloudflare.com/kv/platform/pricing/
- https://developers.cloudflare.com/api/resources/kv/

## 10. Hyperdrive

### What it is

Hyperdrive makes existing regional Postgres and MySQL databases fast from Workers by doing connection setup at the edge, pooling connections near the database, and caching read query results (https://developers.cloudflare.com/hyperdrive/, https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
It works with existing drivers and ORMs, supports PostgreSQL 9.0 to 18.x and MySQL 5.7 to 8.x (including MariaDB), and Postgres-compatible systems such as CockroachDB, Timescale and Materialize; SQL Server and MongoDB are not supported (https://developers.cloudflare.com/hyperdrive/reference/supported-databases-and-features/).
MySQL support went GA on 2026-08-07 at the same pricing as Postgres (https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/).

### Key concepts

- **Pooling mode** is transaction mode; `SET` applies only within a transaction or query; named prepared statements are supported for `postgres.js` and `node-postgres` (https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
- **Placement**: with several sequential queries per request, place the Worker near the database (`"placement": { "region": "aws:us-east-1" }`), because each round trip is 20 to 30 ms from far away versus 1 to 3 ms nearby (same page).
- **Query caching** is on by default with `max_age` 60 seconds and `stale_while_revalidate` 15 seconds, `max_age` up to 1 hour; only read queries using `IMMUTABLE` functions are cached; `STABLE` functions such as `NOW()` and `CURRENT_TIMESTAMP` became uncacheable on 2026-02-23 (https://developers.cloudflare.com/hyperdrive/concepts/query-caching/, https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/).
- **No invalidation on writes**: for read-after-write needs, create a second configuration with `--caching-disabled` and bind both (https://developers.cloudflare.com/hyperdrive/concepts/query-caching/).
- Function names inside SQL comments can make a query uncacheable, while other comment text does not change the cache key (same page).
- **Private databases**: connect through Workers VPC (recommended since 2026-04-29) or Cloudflare Tunnel; Hyperdrive egresses from Cloudflare's published IP ranges (https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/, https://developers.cloudflare.com/hyperdrive/platform/release-notes/).
- **TLS**: Postgres `require` (default), `verify-ca`, `verify-full`; MySQL `REQUIRED` (default), `VERIFY_CA`, `VERIFY_IDENTITY`; plaintext is never allowed (https://developers.cloudflare.com/hyperdrive/reference/supported-databases-and-features/).
- **PlanetScale partnership**: create PlanetScale Postgres or MySQL (Vitess) databases from the Cloudflare dashboard, billed on the Cloudflare invoice at PlanetScale's prices, billed daily whether used or not; `wrangler hyperdrive planetscale signature | pscale database create ... --cloudflare-billing @-` is experimental; Hyperdrive connection setup is quoted at p90 4 ms (https://developers.cloudflare.com/hyperdrive/planetscale/).
- Python Workers can use Hyperdrive since 2026-09-16 (https://developers.cloudflare.com/changelog/post/2026-09-16-hyperdrive-python-workers/).
- Pool metrics (`waitingClients`, `currentPoolSize`, `availablePoolSlots`, `maxPoolSize`) since 2026-05-15, and a dashboard restart (drain pool) action since 2026-08-07 (changelog posts `2026-05-15-hyperdrive-pool-size-metrics`, `2026-08-07-hyperdrive-restart-configuration-dashboard`).

### API and binding surface

```jsonc
"compatibility_flags": ["nodejs_compat"],
"hyperdrive": [
  { "binding": "HYPERDRIVE", "id": "<YOUR_HYPERDRIVE_ID>", "localConnectionString": "<LOCAL_CONNECTION_STRING>" }
]
```

```ts
const client = new Client({ connectionString: env.HYPERDRIVE.connectionString }); // pg
// mysql2: createConnection({ host: env.HYPERDRIVE.host, user, password, database, port, disableEval: true })
```

Source: https://developers.cloudflare.com/hyperdrive/.
Create clients inside the handler per request, not in global scope (https://developers.cloudflare.com/hyperdrive/concepts/query-caching/).
Wrangler: `npx wrangler hyperdrive create <name> --connection-string="..."`, `update <ID> --caching-disabled`, plus TLS and CA options (https://developers.cloudflare.com/hyperdrive/reference/wrangler-commands/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/hyperdrive/platform/limits/:

| Limit | Free | Paid |
| --- | --- | --- |
| Configured databases | 10 per account | 25 per account |
| Username and database name length | 63 bytes | 63 bytes |
| Initial connection timeout | 15 seconds | 15 seconds |
| Idle connection timeout | 10 minutes | 10 minutes |
| Origin connections per configuration | about 20 | about 100 (soft) |
| Query duration | 60 seconds | 60 seconds |
| Cached response size | 50 MB | 50 MB |

Configurable connection counts have a minimum of 5 (https://developers.cloudflare.com/hyperdrive/platform/release-notes/).

### Pricing (as of 2026-10-05)

Free plan: 100,000 database queries per day; Paid plan: unlimited queries, with pooling and caching included and no egress charge; cached and uncached queries count the same (https://developers.cloudflare.com/hyperdrive/platform/pricing/).

### Most useful pages

- https://developers.cloudflare.com/hyperdrive/get-started/
- https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/
- https://developers.cloudflare.com/hyperdrive/concepts/query-caching/
- https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/
- https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/ (Neon, Supabase, RDS, PlanetScale, Prisma, Drizzle and more)
- https://developers.cloudflare.com/hyperdrive/platform/limits/

## 11. Artifacts

### What it is

Artifacts is "versioned storage that speaks Git": create Git repositories programmatically, import existing ones, and access them from Workers, the REST API or any Git client (https://developers.cloudflare.com/artifacts/).
It targets versioned file trees, platforms storing customer code at scale, agent sessions and handoffs, and fork-and-merge workflows, with a repo per project, user, session or task (same page).
It went from private beta (2026-04-16) to open beta on 2026-10-01, Workers Paid only, with billing from 2026-10-14 (https://developers.cloudflare.com/artifacts/platform/changelog/, https://developers.cloudflare.com/artifacts/platform/pricing/).

### Key concepts

- **Namespaces** are top-level containers (per environment, tenant or shard), created implicitly on first repo or explicitly to set a jurisdiction (`eu` or `us`) that cannot be changed later (https://developers.cloudflare.com/artifacts/concepts/namespaces/, https://developers.cloudflare.com/artifacts/guides/data-localization/).
- **Repositories** are isolated Git services, each with its own history, refs, remote URL, tokens and durable state, addressed by namespace plus name and also given an opaque ID (https://developers.cloudflare.com/artifacts/concepts/repositories/).
- Like a Durable Object, a repo is one logical instance routable from any region; data is replicated synchronously across data centers and copied asynchronously to object storage and snapshots (https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/).
- **Tokens** are repo-scoped `read` or `write`, formatted `art_v1_<40 hex>?expires=<unix_seconds>` (https://developers.cloudflare.com/artifacts/api/git-protocol/).
- The binding and REST API are the control plane; Git smart HTTP is the data plane (https://developers.cloudflare.com/artifacts/concepts/repositories/).
- **Best practices**: one repo per agent or session, unique names like `${agentName}-${sessionId}-${repoName}`, fork from a reviewed baseline, short-lived least-privilege tokens, `git notes` for prompts and model output, and split namespaces when one gets hot (https://developers.cloudflare.com/artifacts/concepts/best-practices/).

### API and binding surface

```jsonc
"artifacts": [ { "binding": "ARTIFACTS", "namespace": "default" } ]
```

Workers binding (Wrangler 4.145.0 or later for types and Blob methods with remote bindings) (https://developers.cloudflare.com/artifacts/api/workers-binding/):
- Namespace methods: `create(name, { readOnly, description, setDefaultBranch })`, `get(name)` returning a disposable `ArtifactsRepo` handle (use `using`), `list({ limit, cursor })` with status `ready`, `importing` or `forking`, `import({ source: { url, branch, depth }, target: { name, opts } })`, `delete(name)`.
- `create()` and `import()` return `name`, `remote`, `defaultBranch` and an initial token.
- Repo handle methods: `info()`, `createToken(scope = "write", ttl)` returning `{ plaintext, expiresAt }`, `listTokens()`, `revokeToken()`, `fork(name, { defaultBranchOnly, readOnly, description })`, `log({ ref, limit up to 1,000, offset })`, `readCommit(hash)`, `readTree(hash)`, `readBlob(hash)`, `readFile({ ref, path })` returning a MIME-typed Blob.

REST API: base `https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$NAMESPACE`, Cloudflare API token with Artifacts Read or Edit; routes for namespaces (create with `jurisdiction`, list, get), repos (create, list with `limit` up to 200, `search`, `sort`), file and blob reads returning raw bytes, forks, imports and tokens (https://developers.cloudflare.com/artifacts/api/rest-api/, https://developers.cloudflare.com/artifacts/guides/authentication/).

Git: remote `https://<ACCOUNT_ID>.artifacts.cloudflare.net/git/<namespace>/<repo>.git`, authenticated with `git -c http.extraHeader="Authorization: Bearer $ARTIFACTS_TOKEN"` (recommended) or Basic auth with the token as password; protocol v1 and v2 for clone and fetch, v1 only for push, some optional v1 capabilities like `filter` and `include-tag` unsupported (https://developers.cloudflare.com/artifacts/api/git-protocol/).

Other pieces:
- Wrangler `artifacts namespaces list|get` and `artifacts repos create|list|get|delete|issue-token` since 2026-05-18 (https://developers.cloudflare.com/artifacts/platform/changelog/).
- **Event subscriptions**: account-level `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`; repo-level `pushed`, `cloned`, `fetched`, `token.created`, `token.revoked` (https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).
- **Build and deploy on push**: Workers Builds integration deploys production pushes and makes Worker Previews for other branches; for custom CI, a `cf.artifacts.repo.pushed` trigger starts a Workflow using the `@cloudflare/ci` SDK with sandboxed `runner()` steps and lockfile-keyed caches, deploying to a Worker or a Workers for Platforms User Worker (https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/).
- **ArtifactFS** (`go install github.com/cloudflare/artifact-fs/cmd/artifact-fs@latest`) mounts a blobless clone through FUSE and hydrates files on demand, for large repos in sandboxes (https://developers.cloudflare.com/artifacts/guides/artifact-fs/).
- Examples cover Git clients, isomorphic-git from Workers, and Sandbox SDK (https://developers.cloudflare.com/artifacts/examples/).

### Limits (as of 2026-10-05)

From https://developers.cloudflare.com/artifacts/platform/limits/:

| Limit | Value |
| --- | --- |
| Control-plane requests | 2,000 per 10 seconds per namespace |
| Git requests | 2,000 per 10 seconds per artifact |
| Storage per repository | 1 GB |
| File or blob size | 32 MB |
| Storage per account | 1 TB (raisable) |
| Repositories and namespaces | Unlimited |
| Namespace name length | 2 to 63 characters |

### Pricing (as of 2026-10-05, billing starts 2026-10-14)

Workers Free: unavailable; Workers Paid: 10,000 operations per month included then $0.15 per 1,000, and 1 GB-month included then $0.50 per GB-month; operations include `create`, `push`, `pull` and `clone`; replicas are not billed; repos persist until deleted (https://developers.cloudflare.com/artifacts/platform/pricing/).
A "build the next GitHub on Cloudflare" competition with $25,000 in credits for first place closes 2026-10-14 (https://developers.cloudflare.com/artifacts/platform/changelog/).

## 12. Secrets Store

### What it is

Secrets Store is an account-level, encrypted store of secrets reusable across Workers and AI Gateway, in open beta, unavailable on the China Network (https://developers.cloudflare.com/secrets-store/).
It differs from per-Worker secrets, which are defined per script (https://developers.cloudflare.com/secrets-store/integrations/workers/).

### Key concepts

- A secret is any string up to 65,536 bytes; once stored it cannot be decrypted or read back through the API or dashboard, only by the bound service (https://developers.cloudflare.com/secrets-store/manage-secrets/).
- **Access needs two checks**: a role or token permission, and the secret's **scope** list (`workers`, `ai-gateway`) including the consuming service (https://developers.cloudflare.com/secrets-store/access-control/).
- Roles: Super Administrator (everything), Secrets Store Admin (create, edit, duplicate, delete, view metadata), Secrets Store Deployer (view metadata, bind to Workers, associate with AI Gateway), Secrets Store Reporter (view metadata only) (same page).
- Token permissions: Account Secrets Store Read (metadata only) and Account Secrets Store Edit (create, edit, delete and also **bind**); CI deploys of Workers with a Secrets Store binding need Edit (same page).
- Audit logs record access, create (duplicates carry `duplicated_from_id`), update (`value_modified: true`) and delete (https://developers.cloudflare.com/secrets-store/audit-logs/).

### API and binding surface

```sh
npx wrangler secrets-store store create <name> --remote
npx wrangler secrets-store secret create <STORE_ID> --name MY_SECRET_NAME --scopes workers --remote
```

```jsonc
"secrets_store_secrets": [
  { "binding": "<BINDING_VARIABLE>", "store_id": "<STORE_ID>", "secret_name": "<MY_SECRET_NAME>" }
]
```

```js
const apiKey = await env.<BINDING_VARIABLE>.get();
```

Source: https://developers.cloudflare.com/secrets-store/integrations/workers/.
Production secrets cannot be read from local dev; use `secrets-store secret` commands without `--remote` for local secrets (same page).
REST: `POST /accounts/$ACCOUNT_ID/secrets_store/stores/$STORE_ID/secrets` (array of `{name, value, scopes, comment}`), plus duplicate, `PATCH` and `DELETE` routes (https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/).
Related Workers features: a `secrets` property in Wrangler config declares required secrets (2026-03-24) and a bulk per-Worker secrets endpoint exists (2026-06-03) (changelog posts `2026-03-24-secrets-config-property`, `2026-06-03-bulk-secrets-api`).

### Limits and pricing (as of 2026-10-05)

One store per account and 100 production secrets per account during the open beta; local-only secrets do not count (https://developers.cloudflare.com/secrets-store/manage-secrets/).
No pricing page exists in the mirror.

## 13. Comparison table across all storage products

All values as of 2026-10-05, from the pages cited in sections 2 to 12.
"Latency" quotes only figures the docs give; blank means the docs give none.

| Product | Data model | Consistency model | Latency (documented) | Size limits | Pricing (Workers Paid unless noted) | Status | Best use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R2 | Objects in buckets, S3 API | Strong global read-after-write, list and delete; IAM eventual (about 1 min); relaxed behind a caching custom domain | Not quantified; Local Uploads up to 75% lower TTLB in tests | 4.995 TiB per object, 5 GiB single PUT, 8 KB metadata, 1 write per second per key | $0.015 per GB-month, $4.50 per M Class A, $0.36 per M Class B, zero egress; free 10 GB, 1 M A, 10 M B | GA | Media, token metadata, datasets, backups, Iceberg data |
| Basin Pipelines | JSON event streams into Parquet, JSON or Iceberg | Exactly-once delivery to sinks; invalid events dropped | Data lands per roll interval (Catalog sink minimum 60 s) | 5 MB per request, 1 GB/s per stream, 20 streams | Ingress free; $0.04 per GB transform; $0.03 or $0.06 per GB sink after 50 GB | GA | Event and log ingestion for analytics |
| Basin Catalog | Iceberg REST catalog over R2 | Iceberg ACID snapshots | Not quantified | No non-default jurisdictions; compaction 64 to 512 MB files | $9 per M ops after 1 M; compaction $0.005 per GB, $2 per M objects | GA | Lakehouse tables shared with Spark, DuckDB, Snowflake |
| Basin SQL | Read-only distributed SQL | Reads committed Iceberg snapshots | Heavy queries may time out | Parquet only, no writes | $2.50 per TB scanned after 10 GB, 10 MB minimum per query | GA | Ad hoc and dashboard analytics over Iceberg |
| K2 | Append-only log with subscriptions | Atomic batches; at-least-once; no dedupe; no cross-worker order | 5-minute leases | 1 MB records, 5 MB requests, 30-day max retention, 10 GB per account in beta | No pricing page | Public beta | Event backbone with replay and fan-out |
| D1 | SQLite relational DB | Primary is single-threaded and serial; replicas async with sequential consistency per Session | Indexed point read under 1 ms SQL time | 10 GB per DB (fixed), 2 MB row, 100 bound params, 30 s query | Reads $0.001 per M after 25 B; writes $1 per M after 50 M; $0.75 per GB-month after 5 GB | GA (read replication announced public beta) | Relational app data, many small per-tenant DBs |
| KV | Key-value with metadata | Eventual; up to 60 s or more to propagate | Hot reads about 500 µs to 10 ms | 25 MiB value, 512 B key, 1 write per second per key | Reads $0.50 per M after 10 M; writes, deletes, lists $5 per M after 1 M; $0.50 per GB-month after 1 GB | GA | Config, token lists, sessions, caches |
| Hyperdrive | Proxy for your Postgres or MySQL | Your database's model; cached reads stale up to `max_age` plus SWR | Connection setup p90 4 ms; 1 to 3 ms per query when placed near the DB | 60 s query, 50 MB cached response, about 100 origin connections | Free 100k queries per day; Paid unlimited, no extra charge | GA (MySQL GA 2026-08-07) | Existing or large SQL databases, existing indexers |
| Artifacts | Git repositories | Synchronous multi-DC replication per repo | Not quantified | 1 GB per repo, 32 MB per file, 1 TB per account | $0.15 per 1,000 ops after 10,000; $0.50 per GB-month after 1 GB (from 2026-10-14) | Open beta | Versioned code and file trees per user, agent or launch |
| Secrets Store | Named secret strings | Not documented | Not documented | 65,536 bytes per secret, 100 secrets, 1 store per account | No pricing page | Open beta | API keys and credentials shared across Workers |

Durable Objects, Queues, Vectorize and Analytics Engine also appear in Cloudflare's storage chooser but live elsewhere in the sidebar (https://developers.cloudflare.com/workers/platform/storage-options/).

## 14. How Cloudflare says to choose

From https://developers.cloudflare.com/workers/platform/storage-options/:
- KV for configuration, routing metadata, personalization and session data read at high rates and rarely written.
- R2 for user-facing assets, images, ML and analytics datasets, and log data.
- Hyperdrive for an existing Postgres or MySQL database, very large single databases (1 TB, 100 TB or more), or existing tooling; works with PlanetScale or Neon.
- D1 for lightweight, read-heavy serverless apps with global users that benefit from read replication; split data over 10 GB into several databases.
- Durable Objects for stateful coordination and per-user SQL state; D1 and Queues are built on Durable Objects.
- Basin Pipelines for streaming ingestion; Analytics Engine for time-series metrics; Vectorize for embeddings.
- Applications commonly combine several, for example KV for sessions, R2 for media and Hyperdrive for a hosted Postgres.
- SQL query pricing and limits are intended to be identical between D1 and SQLite in Durable Objects.

## 15. Build hooks for Web3 projects

These are suggestions for dapps, launchpads, indexers and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663), mapped to documented features; the chain-specific framing is this knowledge base's, not Cloudflare's.

### R2 for token metadata, images and launch assets

- Host token metadata JSON (Solana Metaplex-style JSON, EVM `tokenURI` JSON) and logos in R2 behind a custom domain, so reads are cached, WAF-protected and egress-free (https://developers.cloudflare.com/r2/buckets/public-buckets/, https://developers.cloudflare.com/r2/pricing/).
- Never point production metadata URIs at `r2.dev`, which is rate limited and for development only (https://developers.cloudflare.com/r2/platform/limits/).
- Let launchpad creators upload logos directly with short-lived presigned `PUT` URLs that pin `Content-Type`, and configure CORS for the launchpad origin (https://developers.cloudflare.com/r2/api/s3/presigned-urls/).
- Use bucket locks with an `Indefinite` rule on a `metadata/` prefix so metadata cannot be overwritten after a launch, which mirrors on-chain immutability promises (https://developers.cloudflare.com/r2/buckets/bucket-locks/).
- Because cached custom-domain objects keep serving old versions, version metadata keys (for example `metadata/<mint-or-address>/v2.json`) instead of overwriting, or purge the cache (https://developers.cloudflare.com/r2/reference/consistency/).
- Wire `object-create` event notifications on an `uploads/` prefix to a Queue consumer that validates images, resizes them with Images, and writes the final metadata (https://developers.cloudflare.com/r2/buckets/event-notifications/).
- R2 is location-addressed, not content-addressed; projects that need IPFS CIDs should look at Cloudflare's Web3 gateways, covered elsewhere in this knowledge base (https://developers.cloudflare.com/web3/).

### KV for token lists and chain config

- Cache token lists (Jupiter verified lists on Solana, Uniswap-style lists for Ethereum, Base and Robinhood Chain), RPC endpoint maps per chain id (for example 4663), contract address books and feature flags in KV, since a whole list fits in a 25 MiB value and hot reads are sub-10 ms (https://developers.cloudflare.com/kv/platform/limits/, https://developers.cloudflare.com/workers/platform/storage-options/).
- Do not put prices, balances or order books in KV: one write per second per key and up to 60 seconds of staleness make it wrong for tick data (https://developers.cloudflare.com/kv/concepts/how-kv-works/).
- Read many token entries at once with `get(keys[])` (up to 100 keys) (https://developers.cloudflare.com/kv/api/read-key-value-pairs/).
- Migrate any script still calling `/accounts/{id}/workers/namespaces/*` before 2026-10-15 (https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/).

### D1 for indexed trades, launches and candles

- Keep an indexer's trades, launches and holders in D1, sharded by chain or by launchpad so each database stays under the fixed 10 GB cap (https://developers.cloudflare.com/d1/platform/limits/).
- Index on `(token, block_time)` or `(pool, slot)`, because D1 bills rows scanned, not rows returned (https://developers.cloudflare.com/d1/platform/pricing/).
- Batch inserts within 100 bound parameters per statement and break large backfills into chunks of about 1,000 rows, as the limits FAQ advises (https://developers.cloudflare.com/d1/platform/limits/).
- Use read replication with Sessions bookmarks so a trader who just submitted a swap reads their own indexed fill (`first-primary` or a bookmark) while anonymous chart viewers read nearby replicas (https://developers.cloudflare.com/d1/best-practices/read-replication/).
- A single database processes queries one at a time, so a hot-path writer (one indexer Worker) plus many readers via replicas is the documented-friendly shape.
- Time Travel (30 days on Paid) is a safety net for a bad indexer migration; it is not a reorg tool, since it restores the whole database (https://developers.cloudflare.com/d1/reference/time-travel/).

### Hyperdrive for an existing Postgres indexer

- Front an existing Postgres or MySQL indexer database (self-hosted, Neon, Supabase, RDS or PlanetScale) with Hyperdrive so Workers-based APIs and trading UIs reuse pooled connections (https://developers.cloudflare.com/hyperdrive/).
- Use the cached binding for public reads such as top tokens and volume charts, and a `--caching-disabled` binding for wallet positions, order status and anything read right after a write (https://developers.cloudflare.com/hyperdrive/concepts/query-caching/).
- Pass block heights or timestamps as parameters instead of `NOW()` so chart queries stay cacheable (same page).
- Put the indexer database in a private network and reach it through Workers VPC (https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/).

### K2 and Basin for event pipelines and analytics

- Push decoded chain events (swaps, mints, launches, graduations) from an ingest Worker into a K2 stream, then give the UI notifier, the D1 indexer and the analytics loader their own subscriptions so each can replay independently for up to 30 days (https://developers.cloudflare.com/k2/concepts/).
- Make consumers idempotent on `(tx signature or hash, log index)`, because K2 is at-least-once and never deduplicates (https://developers.cloudflare.com/k2/features/produce/).
- Do not let browsers produce to K2 for anything trusted, since browser produce requires an unauthenticated stream (same page).
- Stream every trade into Basin Pipelines as an Iceberg table and run leaderboards, PnL and volume reports with Basin SQL at $2.50 per TB scanned, or open the same tables from DuckDB or Snowflake (https://developers.cloudflare.com/basin/platform/pricing/, https://developers.cloudflare.com/basin-catalog/config-examples/).
- The Bluesky firehose fan-out example is a direct template for splitting one chain firehose into per-event-type tables (https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/).

### Artifacts for per-launch sites and agent-built pages

- Give each token launch or each creator its own Artifacts repo for its landing page, forked from a reviewed template, and deploy it through Workers Builds on push (https://developers.cloudflare.com/artifacts/concepts/best-practices/, https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/).
- Git history gives an auditable record of metadata and site changes, and `pushed` events can trigger review agents (https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

### Secrets Store for keys

- Keep RPC provider keys, Jupiter or other aggregator API keys and webhook secrets in Secrets Store scoped to `workers`, bound into each Worker that needs them (https://developers.cloudflare.com/secrets-store/integrations/workers/).
- The docs say stored values cannot be read back via API or dashboard, but they say nothing about hardware-backed key custody or signing, so treat storing hot-wallet private keys there as an unverified design choice (https://developers.cloudflare.com/secrets-store/manage-secrets/).
- Give CI tokens Account Secrets Store Edit only where deploys need to bind secrets (https://developers.cloudflare.com/secrets-store/access-control/).

## 16. Gaps and contradictions

1. **Basin Catalog sink roll interval.** The sink page says the Basin Catalog sink roll interval minimum is 60 seconds to avoid compaction conflicts (https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/), but the Pipelines getting-started page says Advanced mode allows a 10-second minimum and has the dashboard flow set 10 seconds for a Catalog sink (https://developers.cloudflare.com/basin-pipelines/getting-started/), and the Basin SQL get-started sets 10 seconds for a Data Catalog table (https://developers.cloudflare.com/basin-sql/get-started/), while the Basin CLI guide uses 60 seconds (https://developers.cloudflare.com/basin/get-started/guide/).
2. **Basin SQL token scope.** Basin Catalog recommends read-only tokens for Basin SQL and other readers (https://developers.cloudflare.com/basin-catalog/manage-catalogs/), but the Basin SQL query page asks for R2 storage Admin read/write and its example policy uses `Workers R2 Data Catalog Write` and `Workers R2 Storage Write` (https://developers.cloudflare.com/basin-sql/query-data/).
3. **Old names persist.** Permission groups are still `Workers R2 Data Catalog Read/Write` and `Workers R2 SQL Read`, the sink type value `r2-data-catalog` and the wizard label "Data Catalog (Iceberg)" remain, and changelog titles still say R2 Data Catalog, R2 SQL and Pipelines; Basin Catalog and Basin SQL say the old APIs "will be deprecated in the future" with no date (https://developers.cloudflare.com/basin-catalog/, https://developers.cloudflare.com/basin-sql/).
4. **Schema type spelling.** Basin get-started schemas use `"type": "float64"` in the CLI file but `"type": "f64"` in the dashboard JSON on the Basin SQL get-started page (https://developers.cloudflare.com/basin-sql/get-started/).
5. **Storage chooser is stale.** https://developers.cloudflare.com/workers/platform/storage-options/ does not mention K2, Artifacts, Basin Catalog or Basin SQL, and still lists "(Future) Transform and aggregate data during ingestion" for Basin Pipelines although SQL transforms are live.
6. **Basin Catalog and jurisdictions.** Basin Catalog does not support non-default jurisdiction buckets (https://developers.cloudflare.com/basin-catalog/manage-catalogs/), while R2, D1, KV and Artifacts all offer jurisdictions, so EU-resident lakehouse data is not documented as possible.
7. **Legacy pipeline cutoff date.** The legacy page says pipelines created before 2025-09-25 are legacy, while the llms.txt summary says "before September 2025" (https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/).
8. **Artifacts endpoints.** The Git protocol page gives `https://<ACCOUNT_ID>.artifacts.cloudflare.net/git/<namespace>/<repo>.git`, but the 2026-04-16 beta changelog clones `https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git` and calls the REST API at `https://artifacts.cloudflare.net/v1/api/namespaces/...` instead of `https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/...` (https://developers.cloudflare.com/artifacts/api/git-protocol/, https://developers.cloudflare.com/artifacts/platform/changelog/, https://developers.cloudflare.com/artifacts/api/rest-api/); the docs say to use the exact `remote` returned by the API.
9. **Artifacts status and dates.** The changelog says open beta from 2026-10-01, but its 2026-06-17 entry still asks users to join the beta by form, and the changelog page header says "Last updated Apr 21, 2026" despite October entries (https://developers.cloudflare.com/artifacts/platform/changelog/); "How Artifacts works" says namespaces are not provisioned separately, while the namespaces page and REST API offer explicit creation (https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/, https://developers.cloudflare.com/artifacts/concepts/namespaces/).
10. **Secrets Store permission names.** The access-control page names token permissions "Account Secrets Store Read" and "Account Secrets Store Edit", while the how-to and Workers integration pages list "Secrets Store Write" (https://developers.cloudflare.com/secrets-store/access-control/, https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/).
11. **Secrets Store sample bug.** The Workers integration example assigns `const APIkey = await env.<BINDING_VARIABLE>.get()` and then uses `${APIKey}`, which would throw (https://developers.cloudflare.com/secrets-store/integrations/workers/).
12. **Missing pricing pages.** K2 and Secrets Store have no pricing pages in the mirror, and K2 is Workers Paid only, so their eventual cost is unknown as of 2026-10-05.
13. **D1 Time Travel window.** The D1 overview says restore "to any minute within the last 30 days" (https://developers.cloudflare.com/d1/), but the limits page gives 30 days on Paid and 7 days on Free (https://developers.cloudflare.com/d1/platform/limits/).
14. **D1 read replication status.** Release notes announced read replication as public beta on 2025-04-10, but the read replication page carries no beta label (https://developers.cloudflare.com/d1/platform/release-notes/, https://developers.cloudflare.com/d1/best-practices/read-replication/).
15. **Release notes lag the changelog.** D1 release notes stop at 2025-11-05, Hyperdrive's at 2025-12-04 and R2's at 2026-04-27, while 2026 changes (D1 free-tier enforcement, Hyperdrive MySQL GA, R2 `us` jurisdiction, Data Access Logs, Local Uploads) appear only in https://developers.cloudflare.com/changelog/; the R2 and D1 release-note pages also say "Last updated Apr 21, 2026" despite later entries.
16. **R2 Local Uploads status.** The 2026-02-03 changelog calls Local Uploads "open beta", but the Local Uploads page has no beta label (https://developers.cloudflare.com/changelog/post/2026-02-03-r2-local-uploads/, https://developers.cloudflare.com/r2/buckets/local-uploads/).
17. **R2 size limits.** The limits table lists 5 TiB per object and 5 GiB per single upload, while its footnotes say the real values are 4.995 TiB and 4.995 GiB (https://developers.cloudflare.com/r2/platform/limits/).
18. **KV staleness wording.** Pages say changes take "up to 60 seconds (or the value of `cacheTtl`)" to propagate, while the minimum `cacheTtl` is now 30 seconds and how-kv-works says "60 seconds or more" (https://developers.cloudflare.com/kv/api/read-key-value-pairs/, https://developers.cloudflare.com/kv/concepts/how-kv-works/).
19. **Hyperdrive connection caps are soft.** The limits page gives about 20 and about 100 origin connections and warns counts can exceed them because new pools may be created (https://developers.cloudflare.com/hyperdrive/platform/limits/), so origin `max_connections` needs headroom.
20. **No consistency or latency documentation for Secrets Store or Artifacts propagation.** Neither product documents how fast a rotated secret or a pushed ref is visible globally.
21. **Name collision.** Searching the changelog for "K2" mostly returns Kimi K2 Workers AI model posts, not the K2 durable log, which has no changelog entries in the mirror.
