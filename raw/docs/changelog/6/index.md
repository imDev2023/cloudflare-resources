---
title: Changelogs
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

Aug 28, 2026

[<h2>Cloudflare One Client for Linux (version 2026.7.1377.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 28, 2026

[<h2>Improved dataset configuration in Log Explorer</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-dataset-configuration/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.

- **Grouped field selection** organizes fields by category and shows the number selected in each group.
- **Field details** identify each field's data type and mark required or deprecated fields.
- **Bulk controls** let you select all fields or reset the selection to the dataset defaults.
- **Ingestion filters** let you ingest all events or only events that match your conditions.

These controls are available when you add a dataset or select **Actions** > **Edit** for an enabled dataset.

For more information, refer to [Configure fields and filters](https://developers.cloudflare.com/log-explorer/manage-datasets/#configure-fields-and-filters).

Aug 28, 2026

[<h2>Z.ai GLM-5.3 now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/zai-org/glm-5.3`](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.

GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: [Z.ai reports ↗︎](https://huggingface.co/zai-org/GLM-5.3) a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).

The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.

GLM-5.3 requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 28, 2026

[<h2>Durable Objects can use up to ten Dynamic Workers concurrently</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/)

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) can have up to ten distinct [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.

Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.

For more information, refer to [Dynamic Workers limits](https://developers.cloudflare.com/dynamic-workers/platform/limits/).

Aug 27, 2026

[<h2>Increased limits for JWT validation configurations</h2>](https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/)

[API Shield](https://developers.cloudflare.com/api-shield/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports 32 token configurations per zone by default. Each token configuration can contain up to 16 keys.

These increased limits support more JWT configurations and provide additional capacity for key rotation.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) for configuration details.

Aug 27, 2026

[<h2>APO caches more crawler and bot traffic again</h2>](https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/)

[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)

We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit `Accept: text/html` header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (`cf-cache-status: DYNAMIC`) instead of the cache.

APO now caches these requests again. No action is needed. If you added a Transform Rule to set `Accept: text/html` as a workaround, you can remove it.

For details on how APO decides what to cache, refer to [About APO](https://developers.cloudflare.com/automatic-platform-optimization/about/).

Aug 26, 2026

[<h2>Access service token secrets use a scannable format</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.

Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same `CF-Access-Client-Id` and `CF-Access-Client-Secret` authentication headers.

For more information, refer to [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Aug 26, 2026

[<h2>New Workers AI text generation models in AI Search</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports six additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models for text generation:

| Model | Context window (tokens) |
| --- | --- |
| `@cf/deepseek-ai/deepseek-v4-flash-0731` | 1,048,576 |
| `@cf/deepseek-ai/deepseek-v4-pro-0813` | 1,048,576 |
| `@cf/openai/gpt-oss-120b` | 128,000 |
| `@cf/openai/gpt-oss-20b` | 128,000 |
| `@cf/qwen/qwen3.8-27b` | 262,144 |
| `@cf/moonshotai/kimi-k2.7-code` | 262,144 |

These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

Aug 26, 2026

[<h2>Create app-scoped API tokens for Flagship</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/)

[Flagship](https://developers.cloudflare.com/flagship/)

You can now create **app-scoped API tokens** for [Flagship](https://developers.cloudflare.com/flagship/). These tokens grant access only to the Flagship apps you select, instead of every app in the account.

When you create a custom token, open the resource dropdown (it defaults to **Entire Account**) and select **Specified Flagship apps**. Then choose the app and a **Flagship App** permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.

Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.

To create a token, refer to [API tokens](https://developers.cloudflare.com/flagship/api-tokens/) or [open the app-scoped token form ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&scope=specified_flagship_app) in the dashboard.

Aug 26, 2026

[<h2>Delete Log Explorer datasets</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete**, and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.

Aug 26, 2026

[<h2>Azure Functions-based Microsoft Sentinel connector deprecation</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/)

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) [Logs](https://developers.cloudflare.com/logs/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

- [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
- [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
- [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)

For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).

Aug 26, 2026

[<h2>Radar Researcher adds richer sources and URL Scanner explanations</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-radar-researcher-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) expands the [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) beta with richer sources and new ways to investigate Internet data.

#### Connected insights

Radar Researcher responses can now link to relevant Radar pages, reports, and Cloudflare Blog posts.

![Radar Researcher response linking to the IP Address Information and Network Quality Test pages](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=798,height=668,format=webp/_astro/radar-researcher-page-links.D74GzYoL.png)

#### URL Scanner report explanations

Select **Explain with AI** on a [URL Scanner report ↗︎](https://radar.cloudflare.com/scan) to have Radar Researcher explain its findings and answer follow-up questions about the scanned site.

![Radar Researcher explaining findings from an example.com URL Scanner report](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=696,height=1250,format=webp/_astro/radar-researcher-url-scanner-explanation.BBCehcJx.png)

#### Improved shared sessions

Shared conversations now open in fullscreen, while the share URL remains available until you close the panel or start a new conversation.

Open [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) to explore these improvements.

Aug 26, 2026

[<h2>WAF Release - 2026-08-26 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.

**Key Findings**

- CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.
- GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.

**Impact**

Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2ca6cce3 | N/A | Next.js - Remote Code Execution - CVE:CVE-2026-75604 | Block | N/A | Rule metadata description refined. Detection unchanged. |
| Cloudflare Managed Ruleset | ...80256efe | N/A | Next.js - Image Optimizer Remote Code Execution via Crafted AVIF | N/A | Block | This is a new detection. |

Aug 26, 2026

[<h2>Z.ai GLM-5.3 Flash now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/zai-org/glm-5.3-flash`](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.

GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3 Flash requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 Flash through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 25, 2026

[<h2>Grace periods for service token rotation</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.

The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.

For configuration instructions, refer to [Rotate service token secrets](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets).

Aug 25, 2026

[<h2>Temporarily turn off Access service tokens</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.

Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.

For configuration instructions, refer to [Turn a service token on or off](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off).

Aug 25, 2026

[<h2>Store larger custom metadata values in AI Search</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.

For details, refer to [Metadata attributes](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

Aug 25, 2026

[<h2>Symmetric key support for JWT validation</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/)

[API Shield](https://developers.cloudflare.com/api-shield/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports symmetric keys that use the `HS256`, `HS384`, and `HS512` algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.

Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#credentials) for supported key formats and credential requirements.

Aug 25, 2026

[<h2>MCP server portals support MCP 2026-07-28 specification</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support the stateless MCP `2026-07-28` specification for client and upstream server connections.

The portal's `/mcp` endpoint automatically accepts stateless MCP `2026-07-28` requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP `2026-07-28` support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.

SSE connections continue to use the legacy protocol. For details, refer to [MCP server portal transport and protocol compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport).

Aug 25, 2026

[<h2>Prevent Durable Object alarm retries when using \`ctx.abort()\`</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

By default, an alarm interrupted by `ctx.abort()` retries after the Durable Object resets. Pass `{ retryAlarm: false }` when the alarm should stop instead:

*src/index.jsjs*

```js
import { DurableObject } from "cloudflare:workers";

export class CleanupTask extends DurableObject {
	async alarm() {
		await this.ctx.storage.deleteAll();

		this.ctx.abort("Cleanup complete", { retryAlarm: false });
	}
}
```

*src/index.tsts*

```ts
import { DurableObject } from "cloudflare:workers";

export class CleanupTask extends DurableObject {
	async alarm(): Promise<void> {
		await this.ctx.storage.deleteAll();

		this.ctx.abort("Cleanup complete", { retryAlarm: false });
	}
}
```

For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.

Alarms can run concurrently with other requests to the same Durable Object. If another request calls `ctx.abort()` while an alarm is running, the `retryAlarm` option on that call also controls whether the alarm retries.

The default retry prevents an unrelated request from permanently canceling the alarm. Set `retryAlarm: false` on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to `ctx.abort()` keep retrying alarms.

For local development, `retryAlarm` requires Wrangler 4.126.0 or later.

For more information, refer to [`ctx.abort()`](https://developers.cloudflare.com/durable-objects/api/state/#abort).

Aug 25, 2026

[<h2>WAF Release - 2026-08-25</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.

**Key Findings**

- Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.
- The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.
- A Generic Rules - Remote Code Execution detection is added in Block mode.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...1489d892 | N/A | HTTP/2 Request Smuggling - Request Body Anomaly | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...20646260 | N/A | XSS - JavaScript Event Handler Coercion - Headers | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...d706d517 | N/A | XSS - JavaScript Event Handler Coercion - Body | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...660886c8 | N/A | XSS - JavaScript Event Handler Coercion - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...c293b926 | N/A | XSS, HTML Injection - Script Tag - Beta | Log | Block | This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID: ...7b58420b). |
| Cloudflare Managed Ruleset | ...2ca6cce3 | N/A | Generic Rules - Remote Code Execution | N/A | Block | This is a new detection. |

Aug 24, 2026

[<h2>Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-24-virtual-appliance-self-serve-download/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

When you register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/), you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.

![Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2813,height=1241,format=webp/_astro/2026-08-24-virtual-appliance-self-serve-download.Ca2YGpCA.png)

- On the **Connectors** page, select **Add an appliance**, choose **Virtual appliance**, then select your hypervisor: **VMware ESXi**, **Proxmox**, or **libvirt/KVM**.
- Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.
- Use **View setup guide** to open deployment instructions for your platform.

This complements the existing self-serve [registration and license key generation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) in the dashboard.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine).

Aug 24, 2026

[<h2>RPKI ASPA path validation on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2026-08-24-radar-aspa-validation/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) adds an [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) to its [Routing section ↗︎](https://radar.cloudflare.com/routing). Enter a BGP `AS_PATH` and the tool checks it against the [Autonomous System Provider Authorization (ASPA) ↗︎](https://blog.cloudflare.com/aspa-secure-internet/) records currently published in the RPKI, returning a verdict of `Valid`, `Invalid`, or `Unknown`. An `Invalid` verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.

Validation follows [draft-ietf-sidrops-aspa-verification ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/), so verdicts match those produced by validators implementing the same draft. The draft is still a work in progress and not yet an RFC.

#### Enter a path

Paths are read in BGP wire order: the rightmost AS is the origin, and the leftmost AS is the one closest to the collector or router that observed the route. AS numbers can be separated by spaces, commas, or hyphens, with or without an `AS` prefix. The full ASPA snapshot is loaded into the browser once, so the verdict, graph, and trace update as the path is edited, with no further requests. A set of example paths covers the interesting cases, including a route leak with an AS0 ASPA, where an AS declares that it has no providers at all.

#### Choose an algorithm

The draft defines two verification algorithms that differ only in whether a down-ramp is permitted:

- **Upstream** ([section 5.4 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.4)) — for routes received from a customer, peer, route server client, or route server. Only an up-ramp is permitted.
- **Downstream** ([section 5.5 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.5)) — for routes received from a provider. Both an up-ramp and a down-ramp are permitted.

An **up-ramp** is the run of consecutive customer-to-provider hops from the origin to the apex of the path, and a **down-ramp** is the equivalent run from the announcing neighbor back to that apex. The tool evaluates both algorithms at once and labels each with its verdict, so a path that is legitimate when received from one session type and a leak when received from another is visible without switching modes. Selecting an algorithm drives the graph and the trace.

#### Read the result

The **ASPA validation graph** draws the path hop by hop, labeling each AS with its role, whether it publishes an ASPA, and how many providers that ASPA authorizes. Every hop is marked `Provider+`, `Not Provider+`, or `No attestation`, and the maximum and minimum bounds of each ramp are drawn against the length of the path. Hops that no ramp reaches are highlighted, because a path the ramps cannot cover end to end is `Invalid`. The accompanying **ASPA records** table lists every AS in the path with its ASPA status and its authorized providers, each linked to its Radar AS page.

![ASPA validation graph for the path 1003 6939 1299 553, showing a Valid verdict under the downstream algorithm, the Provider+, Not Provider+, and No attestation outcome on each hop, and the up-ramp and down-ramp bounds that together cover the path](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1222,format=webp/_astro/aspa-validation-graph.DQUq8KCm.png)

#### Follow the algorithm

The **Algorithm step by step** section shows the derivation rather than just the answer. Two columns run the same scans under different stopping rules: the upper bounds, which test for `Invalid` and stop only on `Not Provider+`, and the lower bounds, which test for `Unknown` and also stop on `No Attestation`. A hop is `Not Provider+` when the AS publishes an ASPA that does not list the next AS as a provider, and `No Attestation` when the AS publishes no ASPA at all. Each column lists the outcome for every hop scanned, marks where the scan stopped, gives the resulting ramp length, and then evaluates the verdict rule with the numbers filled in.

![Step-by-step trace for the same path, with the upper-bound and lower-bound columns each listing the up-ramp and down-ramp scans, the ramp lengths they produce, and the verdict rule that neither Invalid nor Unknown satisfies, leaving a Valid verdict](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1392,height=586,format=webp/_astro/aspa-validation-algorithm-trace.Bb8SM4wT.png)

#### Share a validation

The path and the selected algorithm are kept in the URL, so a link reproduces a result exactly — for example, this [route leak with an AS0 ASPA ↗︎](https://radar.cloudflare.com/routing/aspa-validation?path=22652-1299-9498-149765-14789). Appending `&mode=upstream` pins the link to the upstream algorithm. The graph is a standard Radar widget, so it can also be embedded or shared as an image.

The records behind the tool are the same ones served by the [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) endpoint of the [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API, and the number of records loaded and the snapshot timestamp are shown alongside the input.

Try the [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) with a path of your own.

Aug 24, 2026

[<h2>Preserve exception details in console logs</h2>](https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/)

[Workers](https://developers.cloudflare.com/workers/)

Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.

For example, your Worker can catch and log an exception:

```js
try {
	throw new Error("Deliberately created exception");
} catch (error) {
	console.error("caught exception:", error);
}
```

```ts
try {
	throw new Error("Deliberately created exception");
} catch (error) {
	console.error("caught exception:", error);
}
```

If you use [Workers Observability](https://developers.cloudflare.com/workers/observability/), your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:

![Workers Observability log entry showing a caught exception and its stack trace](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=212,format=webp/_astro/2026-08-24-error-info.Be4rAN4i.png)

The exception's stack trace appears directly in the log message.

If you send telemetry to a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers/), the Tail Worker now receives a log entry with an `errorInfo` array:

```json
{
	"message": ["Request failed:", "RangeError: Value out of range"],
	"errorInfo": [
		null,
		{
			"name": "RangeError",
			"message": "Value out of range",
			"stack": "RangeError: Value out of range\n    at ..."
		}
	],
	"level": "error",
	"timestamp": 1784851200000
}
```

Each `errorInfo` item corresponds to the console argument at the same index in `message`. Arguments that are not exceptions have a `null` entry.

Aug 22, 2026

[<h2>Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</h2>](https://developers.cloudflare.com/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Wrangler and the [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.

The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:

![OAuth consent dialog with an Edit Permissions button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1368,height=1008,format=webp/_astro/oauth-optional-scopes-review.BMp1De1d.png)

You can then choose which specific permissions to grant:

![OAuth permission editor with controls for individual scopes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=1312,format=webp/_astro/oauth-optional-scopes-edit.BXIdjwS7.png)

Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.

If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.

For more information, refer to [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login) and [Edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/6/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
