---
title: Core platform Changelog
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

Apr 21, 2026

[<h2>Introducing Billable Usage dashboard and Budget alerts</h2>](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/)

Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.

#### Billable Usage dashboard

The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.

The dashboard displays:

- A bar chart showing daily usage charges for your billing period
- A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs
- Ability to view previous billing periods

Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.

To access the dashboard, go to **Manage Account** > **Billing** > **Billable Usage**.

![Screenshot of the Billable Usage dashboard in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1033,height=757,format=webp/_astro/billable-usage-dashboard.CQvMdtrp.png)

#### Budget alerts

Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.

To configure a budget alert:

1. Go to **Manage Account** > **Billing** > **Billable Usage**.
2. Select **Set Budget Alert**.
3. Enter a budget threshold amount greater than $0.
4. Select **Create**.

Alternatively, configure alerts via **Notifications** > **Add** > **Budget Alert**.

![Create Budget Alert modal in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=315,height=374,format=webp/_astro/budget-alert-modal.BjIzGOLV.png)

You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.

Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.

For more information, refer to the [Usage based billing documentation](https://developers.cloudflare.com/billing/understand/usage-based-billing/).

Apr 21, 2026

[<h2>Logpush subrequest merging for HTTP requests</h2>](https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/)

[Logs](https://developers.cloudflare.com/logs/)

When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.

#### What's new

- New subrequest\_merging field on Logpush jobs — Set "merge\_subrequests": true when creating or updating an http\_requests Logpush job to enable the feature.
- New Subrequests log field — When subrequest merging is enabled, a Subrequests field ( `array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http\_requests fields for that subrequest.

#### Limitations

- Applies to the http\_requests (zone-scoped) dataset only.
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
- Subrequests that do not qualify appear as separate log entries — no data is lost.
- Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
- For more information, refer to [Subrequests](https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/).

Apr 20, 2026

[<h2>Cloudflare Pipelines as a Logpush destination</h2>](https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/)

[Logs](https://developers.cloudflare.com/logs/) [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)

Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.

With this release, you can now send your logs directly to [Pipelines](https://developers.cloudflare.com/basin-pipelines/) to ingest, transform, and store your logs in [R2](https://developers.cloudflare.com/r2/) as Parquet files or Apache Iceberg tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This makes the data footprint more compact and more efficient at querying your logs instantly with [R2 SQL](https://developers.cloudflare.com/basin-sql/) or any other query engine that supports Apache Iceberg or Parquet.

#### Transform logs before storage

Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:

```sql
INSERT INTO http_logs_sink
SELECT
  ClientIP,
  EdgeResponseStatus,
  to_timestamp_micros(EdgeStartTimestamp) AS event_time,
  upper(ClientRequestMethod) AS method,
  sha256(ClientIP) AS hashed_ip
FROM http_logs_stream
WHERE EdgeResponseStatus >= 400;
```

Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the [Pipelines SQL reference](https://developers.cloudflare.com/basin-pipelines/sql-reference/).

#### Get started

To configure Pipelines as a Logpush destination, refer to [Enable Cloudflare Pipelines](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/).

Apr 17, 2026

[<h2>Introducing Redirects for AI Training</h2>](https://developers.cloudflare.com/changelog/post/2026-04-17-redirects-for-ai-training/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via **AI Crawl Control** > **Quick Actions**, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.

This feature leverages your existing `<link rel="canonical">` tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.

Refer to the [Redirects for AI Training documentation](https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/) for details.

Apr 17, 2026

[<h2>Tools to prepare your site for the agentic Internet</h2>](https://developers.cloudflare.com/changelog/post/2026-04-17-tools-for-agentic-internet/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control now includes new tools to help you prepare your site for the agentic Internet—a web where AI agents are first-class citizens that discover and interact with content differently than human visitors.

#### Content Format insights

The **Metrics** tab now includes a **Content Format** chart showing what content types AI systems request versus what your origin serves. Understanding these patterns helps you optimize content delivery for both human and agent consumption.

#### Directives tab (formerly Robots.txt)

The **Robots.txt** tab has been renamed to **Directives** and now includes a link to check your site's [Agent Readiness ↗︎](https://isitagentready.com) score.

Refer to our [blog post on preparing for the agentic Internet ↗︎](https://blog.cloudflare.com/agent-readiness/) for more on why these capabilities matter.

Apr 15, 2026

[<h2>New TenantID and Firewall for AI fields in Logpush datasets</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has added new fields to multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### TenantID field

The following Gateway and Zero Trust datasets now include a `TenantID` field:

- **[Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid)**: Identifies the tenant ID of the DNS request, if it exists.
- **[Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid)**: Identifies the tenant ID of the HTTP request, if it exists.
- **[Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid)**: Identifies the tenant ID of the network session, if it exists.
- **[Zero Trust Network Sessions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid)**: Identifies the tenant ID of the network session, if it exists.

#### Firewall for AI fields

The following datasets now include [Firewall for AI](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/#firewall-for-ai) fields:

- **[Firewall Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/)**:
  - `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
  - `FirewallForAIPIICategories`: List of PII categories detected in the request.
  - `FirewallForAITokenCount`: The number of tokens in the request.
  - `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.
- **[HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/)**:
  - `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
  - `FirewallForAIPIICategories`: List of PII categories detected in the request.
  - `FirewallForAITokenCount`: The number of tokens in the request.
  - `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Apr 14, 2026

[<h2>Improved OAuth experience for consent and management</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-oauth-consent-and-revoke/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have **granular control** over which accounts these applications can access, plus the ability to revoke access anytime.

#### What's new

#### Choose which accounts to authorize

When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:

- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler This gives you precise control who can access your data.

#### Clear consent screens

The OAuth consent screen now shows:

- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information
- **Which accounts you're authorizing** — Checkboxes for account selection

#### Revoke access anytime

Manage authorized OAuth applications from your profile:

- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications ↗︎](https://dash.cloudflare.com/profile/access-management/authorization)**.

#### Why this matters

These updates give you:

- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed

#### Learn more

Read more about these improvements in our blog post: [Improving the OAuth consent experience ↗︎](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).

Apr 14, 2026

[<h2>Logpush to BigQuery — Cloudflare dashboard support</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.

Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the **Logpush** page in the Cloudflare dashboard by selecting **Google BigQuery** as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.

For more information, refer to [Enable Logpush to Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/).

Apr 10, 2026

[<h2>API tokens now detectable by secret scanning tools</h2>](https://developers.cloudflare.com/changelog/post/2026-04-10-secret-scanning-support/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare API tokens now include **identifiable patterns** that enable secret scanning tools to automatically detect them when leaked in code repositories, configuration files, or other public locations.

#### What changed

API tokens generated by Cloudflare now follow a standardized format that secret scanning tools can recognize. When a Cloudflare token is accidentally committed to GitHub, GitLab, or another platform with secret scanning enabled, the tool will flag it and alert you.

#### Why this matters

Leaked credentials are a common security risk. By making Cloudflare tokens detectable by scanning tools, you can:

- **Detect leaks faster** — Get notified immediately when a token is exposed.
- **Reduce risk window** — Exposed tokens are deactivated immediately, before they can be exploited.
- **Automate security** — Leverage existing secret scanning infrastructure without additional configuration.

#### What happens when a leak is detected

When a third-party secret scanning tool detects a leaked Cloudflare API token:

1. **Cloudflare immediately deactivates the token** to prevent unauthorized access.
2. **The token creator receives an email notification** alerting them to the leak.
3. **The token is marked as "Exposed"** in the Cloudflare dashboard.
4. **You can then roll or delete the token** from the token management pages.

#### Supported platforms

- **GitHub Secret Scanning** — Automatically enabled for public repositories

For more information on token formats and secret scanning, refer to [API token formats](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/).

Apr 7, 2026

[<h2>Redesigned Support Portal for faster, personalized help</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/)

[Support](https://developers.cloudflare.com/support/)

#### Redesigned "Get Help" Portal for faster, personalized help

Cloudflare has officially launched a redesigned "Get Help" Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.

The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as "Ask AI", "Chat with a human", or "Community" — without the manual triage.

#### What's New

- **One Page, Clear Choices**: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.
- **A Radically Simpler Support Form**: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.
- **AI-Driven Triage**: Using [Cloudflare Workers AI ↗︎](https://developers.cloudflare.com/workers-ai/) and [Vectorize ↗︎](https://developers.cloudflare.com/vectorize/), the portal now automatically generates case subjects and predicts product categories.

#### Moving complexity to the backend

Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.

By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.

To learn more, refer to the [Support documentation](https://developers.cloudflare.com/support/contacting-cloudflare-support/) or select **Get Help** directly in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/).

Apr 6, 2026

[<h2>Organizations is now in public beta for enterprises</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

We're announcing the public beta of **Organizations** for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.

**What's New**

**Organizations \[BETA]**: [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.

**Self-serve onboarding**: Enterprise customers can [create an Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/) in the dashboard and assign accounts where they are already Super Administrators.

**Centralized Account Management**: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly. **Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) policies across multiple accounts within your Organization to simplify centralized policy management. **Implicit access**: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.

**Unified analytics**: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.

**Terraform provider support**: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization).

**Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policies across multiple accounts within your Organization to simplify centralized policy management.

Note

Organizations is in Public Beta. You must have an Enterprise account to create an organization, but once created, you can add accounts of any plan type where you are a Super Administrator.

For more info:

- [Get started with Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
- [Set up your Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/)
- [Review limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/)

Apr 6, 2026

[<h2>New ResponseTimeMs field in Gateway DNS Logpush dataset</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-gateway-dns-response-time-ms/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has added a new field to the [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems) Logpush dataset:

- **ResponseTimeMs**: Total response time of the DNS request in milliseconds.

For the complete field definitions, refer to [Gateway DNS dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/).

Apr 2, 2026

[<h2>BigQuery as Logpush destination</h2>](https://developers.cloudflare.com/changelog/post/2026-04-02-bigquery-destination/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports **BigQuery** as a native destination.

Logs from Cloudflare can be sent to [Google Cloud BigQuery ↗︎](https://cloud.google.com/bigquery) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

For more information, refer to the [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/) documentation.

Apr 1, 2026

[<h2>New QUIC RTT and delivery rate fields</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/)

[Rules](https://developers.cloudflare.com/rules/)

Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing [`cf.timings.client_tcp_rtt_msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.

Previously, QUIC RTT and delivery rate data was only available via the `Server-Timing: cfL4` response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.timings.client_quic_rtt_msec` | Integer | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns `0` for TCP connections. |
| `cf.edge.l4.delivery_rate` | Integer | The most recent data delivery rate estimate for the client connection, in bytes per second. Returns `0` when L4 statistics are not available for the request. |

#### Example: Route slow connections to a lightweight origin

Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:

**Rule expression:**

```txt
cf.timings.client_tcp_rtt_msec > 200 or cf.timings.client_quic_rtt_msec > 200
```

**Header modifications:**

| Operation | Header name | Value |
| --- | --- | --- |
| Set | `X-High-Latency` | `true` |

#### Example: Match low-bandwidth connections

```txt
cf.edge.l4.delivery_rate > 0 and cf.edge.l4.delivery_rate < 100000
```

For more information, refer to [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/) and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

Mar 25, 2026

[<h2>Logpush — More granular timestamps</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

- `rfc3339ms` — `2024-02-17T23:52:01.123Z`
- `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`

Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.

Mar 25, 2026

[<h2>New mTLS certificate fields for Transform Rules</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized `Client-Cert` and `Client-Cert-Chain` header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.

Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, `:MIIDsT...Vw==:`. A chain of intermediates is expressed as a comma-separated list of such values.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.tls_client_auth.cert_rfc9440` | String | The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented. |
| `cf.tls_client_auth.cert_rfc9440_too_large` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be `false`. |
| `cf.tls_client_auth.cert_chain_rfc9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB. |
| `cf.tls_client_auth.cert_chain_rfc9440_too_large` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted. |

The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.

#### Example: Forwarding client certificate headers to your origin server

Add a request header transform rule to set the `Client-Cert` and `Client-Cert-Chain` headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:

**Rule expression:**

```txt
cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked
```

**Header modifications:**

| Operation | Header name | Value |
| --- | --- | --- |
| Set | `Client-Cert` | `cf.tls_client_auth.cert_rfc9440` |
| Set | `Client-Cert-Chain` | `cf.tls_client_auth.cert_chain_rfc9440` |

To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates `cf.tls_client_auth.cert_verified` and `cf.tls_client_auth.cert_revoked`.

Prevent header injection

You should ensure that `Client-Cert` and `Client-Cert-Chain` headers received by your origin server can only originate from this transform rule — any client could send these headers directly.

- **If you use WAF custom rules to block requests with invalid mTLS connections:** The transform rule is sufficient. For all requests that reach your origin server, the rule will overwrite any existing `Client-Cert` and `Client-Cert-Chain` headers.
- **If you do not enforce mTLS at the WAF:** Add another transform rule that removes any incoming `Client-Cert` and `Client-Cert-Chain` headers from all requests (use expression `true`), ordered before the rule above. This ensures your origin server cannot receive client-supplied values for these HTTP headers.

For more information, refer to [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/), [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/), and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

Mar 24, 2026

[<h2>Advanced WAF customization for AI Crawl Control blocks</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.

If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the **Crawlers** page with a link to view the rule directly in WAF.

For more information, refer to [WAF rule management](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management).

Mar 20, 2026

[<h2>Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</h2>](https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) of that tunnel and supports streaming logs from multiple replicas at once.

![View replicas and stream logs from multiple connectors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1040,format=webp/_astro/tunnel-multiconn.DEOEaLlu.gif)

Previously, you could only stream logs from one replica at a time. With this update:

- **Replicas on the tunnel overview** — All active replicas for the selected tunnel now appear on that tunnel's overview page under **Connectors**. Select any replica to stream its logs.
- **Multi-connector log streaming** — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Networks** > **Connectors** > **Cloudflare Tunnels**. Select **View logs** next to the tunnel you want to monitor.

For more information, refer to [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) and [Deploy replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/).

Mar 19, 2026

[<h2>Service Key authentication deprecated</h2>](https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.

[API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) replace Service Keys with fine-grained permissions, expiration, and revocation.

#### What you need to do

Replace any use of the `X-Auth-User-Service-Key` header with an [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) scoped to the permissions your integration requires.

If you use `cloudflared`, update to a version from November 2022 or later. These versions already use API Tokens.

If you use [origin-ca-issuer ↗︎](https://github.com/cloudflare/origin-ca-issuer), update to a version that supports API Token authentication.

For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

Mar 19, 2026

[<h2>Manage Cloudflare Tunnels with Wrangler</h2>](https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Workers](https://developers.cloudflare.com/workers/)

You can now manage [Cloudflare Tunnels](https://developers.cloudflare.com/tunnel/) directly from [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for the Cloudflare Developer Platform. The new [`wrangler tunnel`](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/) commands let you create, run, and manage tunnels without leaving your terminal.

![Wrangler tunnel commands demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1094,format=webp/_astro/wrangler-tunnel.DOqrtGGg.gif)

Available commands:

- `wrangler tunnel create` — Create a new remotely managed tunnel.
- `wrangler tunnel list` — List all tunnels in your account.
- `wrangler tunnel info` — Display details about a specific tunnel.
- `wrangler tunnel delete` — Delete a tunnel.
- `wrangler tunnel run` — Run a tunnel using the cloudflared daemon.
- `wrangler tunnel quick-start` — Start a free, temporary tunnel without an account using [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

Wrangler handles downloading and managing the [cloudflared](https://developers.cloudflare.com/tunnel/downloads/) binary automatically. On first use, you will be prompted to download `cloudflared` to a local cache directory.

These commands are currently experimental and may change without notice.

To get started, refer to the [Wrangler tunnel commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/).

Mar 18, 2026

[<h2>SCIM provisioning for Authentik is now Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare dashboard SCIM provisioning now supports [Authentik ↗︎](https://goauthentik.io/) as an identity provider, joining Okta and Microsoft Entra ID as explicitly supported providers.

Customers can now sync users and group information from Authentik to Cloudflare, apply Permission Policies to those groups, and manage the lifecycle of users & groups directly from your Authentik Identity Provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

- [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)
- [Provision with Authentik](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/)

Mar 18, 2026

[<h2>SCIM audit logging Support</h2>](https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare dashboard SCIM provisioning operations are now captured in [Audit Logs v2](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/), giving you visibility into user and group changes made by your identity provider.

![SCIM audit logging](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2556,height=1332,format=webp/_astro/2026-03-18-scim-audit-logging.DPKMiE8X.png)

**Logged actions:**

| Action Type | Description |
| --- | --- |
| Create SCIM User | User provisioned from IdP |
| Replace SCIM User | User fully replaced (PUT) |
| Update SCIM User | User attributes modified (PATCH) |
| Delete SCIM User | Member deprovisioned |
| Create SCIM Group | Group provisioned from IdP |
| Update SCIM Group | Group membership or attributes modified |
| Delete SCIM Group | Group deprovisioned |

For more details, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

Mar 18, 2026

[<h2>Worker execution timing field now available in Rules</h2>](https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/)

[Rules](https://developers.cloudflare.com/rules/)

The `cf.timings.worker_msec` field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.

You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.

#### Field details

| Field | Type | Description |
| --- | --- | --- |
| `cf.timings.worker_msec` | Integer | The time spent executing a Cloudflare Worker in milliseconds. Returns `0` if no Worker was invoked. |

Example filter expression:

```plaintext
cf.timings.worker_msec > 500
```

For more information, refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/).

Mar 12, 2026

[<h2>Retry-After HTTP header for retryable 1xxx errors</h2>](https://developers.cloudflare.com/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare-generated 1xxx error responses now include a standard `Retry-After` HTTP header when the error is retryable. Agents and HTTP clients can read the recommended wait time from response headers alone — no body parsing required.

#### Changes

Seven retryable error codes now emit `Retry-After`:

| Error code | Retry-After (seconds) | Error name |
| --- | --- | --- |
| 1004 | 120 | DNS resolution error |
| 1005 | 120 | Banned zone |
| 1015 | 30 | Rate limited |
| 1033 | 120 | Argo Tunnel error |
| 1038 | 60 | HTTP headers limit exceeded |
| 1200 | 60 | Cache connection limit |
| 1205 | 5 | Too many redirects |

The header value matches the existing `retry_after` body field in JSON and Markdown responses.

If a WAF rate limiting rule has already set a dynamic `Retry-After` value on the response, that value takes precedence.

#### Availability

Available for all zones on all plans.

#### Verify

Check for the header on any retryable error:

```bash
curl -s --compressed -D - -o /dev/null -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | grep -i retry-after
```

References:

- [RFC 9110 section 10.2.3 - Retry-After ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-10.2.3)
- [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)

Mar 11, 2026

[<h2>JSON responses and RFC 9457 support for Cloudflare 1xxx errors</h2>](https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare-generated 1xxx errors now return structured JSON when clients send `Accept: application/json` or `Accept: application/problem+json`. JSON responses follow [RFC 9457 (Problem Details for HTTP APIs) ↗︎](https://www.rfc-editor.org/rfc/rfc9457), so any HTTP client that understands Problem Details can parse the base members without Cloudflare-specific code.

#### Breaking change

The Markdown frontmatter field `http_status` has been renamed to `status`. Agents consuming Markdown frontmatter should update parsers accordingly.

#### Changes

**JSON format.** Clients sending `Accept: application/json` or `Accept: application/problem+json` now receive a structured JSON object with the same operational fields as Markdown frontmatter, plus RFC 9457 standard members.

**RFC 9457 standard members (JSON only):**

- `type` — URI pointing to Cloudflare documentation for the specific error code
- `status` — HTTP status code (matching the response status)
- `title` — short, human-readable summary
- `detail` — human-readable explanation specific to this occurrence
- `instance` — Ray ID identifying this specific error occurrence

**Field renames:**

- `http_status` -> `status` (JSON and Markdown)
- `what_happened` -> `detail` (JSON only — Markdown prose sections are unchanged)

**Content-Type mirroring.** Clients sending `Accept: application/problem+json` receive `Content-Type: application/problem+json; charset=utf-8` back; `Accept: application/json` receives `application/json; charset=utf-8`. Same body in both cases.

#### Negotiation behavior

| Request header sent | Response format |
| --- | --- |
| `Accept: application/json` | JSON (`application/json` content type) |
| `Accept: application/problem+json` | JSON (`application/problem+json` content type) |
| `Accept: application/json, text/markdown;q=0.9` | JSON |
| `Accept: text/markdown` | Markdown |
| `Accept: text/markdown, application/json` | Markdown (equal `q`, first-listed wins) |
| `Accept: */*` | HTML (default) |

#### Availability

Available now for Cloudflare-generated 1xxx errors.

#### Get started

```bash
curl -s --compressed -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | jq .
```

```bash
curl -s --compressed -H "Accept: application/problem+json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | jq .
```

References:

- [RFC 9457 — Problem Details for HTTP APIs ↗︎](https://www.rfc-editor.org/rfc/rfc9457)
- [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/4/#page","headline":"Core platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
