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

Jun 16, 2026

[<h2>Pay Per Crawl advanced configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

You can now configure advanced Pay Per Crawl settings for your zone, including:

- **Disable Pay Per Crawl by URI pattern** using [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) to offer free access to specific pages while charging for others.
- **Dynamic pricing** by having your origin return a `crawler-price` response header, or by using a [Cloudflare Worker](https://developers.cloudflare.com/workers/) to set prices based on request properties.

When dynamic pricing is enabled, Pay Per Crawl adds a `cf-pay-per-crawl` request header to origin requests so your origin or Worker can determine the appropriate price.

Refer to the [Advanced configuration documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/) for details.

Jun 16, 2026

[<h2>New optimization features in Images</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

These updates introduce new features for optimizing and manipulating with Images:

- **New `composite` option:** Control how [overlays are blended](https://developers.cloudflare.com/images/optimization/draw-overlays/#composite) with the base image.
- **Percentage widths:** Set the dimensions of an overlay as [a fraction of the dimensions](https://developers.cloudflare.com/images/optimization/draw-overlays/#width-and-height) of the base image.
- **New `fit` modes:** Use [`aspect-crop`](https://developers.cloudflare.com/images/optimization/features/#aspect-crop) to always preserve the target aspect ratio or [`scale-up`](https://developers.cloudflare.com/images/optimization/features/#scale-up) to always enlarge images.
- **New `upscale` parameter:** Apply [AI upscaling](https://developers.cloudflare.com/images/optimization/features/#upscale) to produce sharper, more detailed results when enlarging images.

Jun 16, 2026

[<h2>Introducing GLM-5.2 on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/)

[Workers](https://developers.cloudflare.com/workers/) [Agents](https://developers.cloudflare.com/agents/) [Workers AI](https://developers.cloudflare.com/workers-ai/)

We are excited to announce **GLM-5.2** on Workers AI, Z.ai's flagship agentic coding model.

[`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.

**Key features and use cases:**

- **Agentic coding**: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows
- **Large context window**: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future
- **Function calling**: Build agents that invoke tools and APIs across multiple conversation turns
- **Reasoning**: Tackles complex problem-solving and step-by-step reasoning tasks

Use GLM-5.2 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

Pricing is available on the [model page](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Jun 16, 2026

[<h2>TCP connections via connect() over VPC Networks</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now support the [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via `fetch()`.

This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "vpc_networks": [
    {
      "binding": "PRIVATE_NETWORK",
      "network_id": "cf1:network",
      "remote": true
    }
  ]
}
```

```toml
[[vpc_networks]]
binding = "PRIVATE_NETWORK"
network_id = "cf1:network"
remote = true
```

At runtime, use `connect()` on the binding to open a TCP socket to a private destination:

```ts
export default {
	async fetch(request: Request, env: Env) {
		// Open a TCP connection to a private Redis instance
		const socket = await env.PRIVATE_NETWORK.connect("10.0.1.50:6379");

		// Write a Redis PING command
		const writer = socket.writable.getWriter();
		await writer.write(new TextEncoder().encode("PING\r\n"));
		await writer.close();

		return new Response(socket.readable);
	},
};
```

Note

`connect()` over VPC Networks currently supports plaintext TCP only.

For more details, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and the [Workers Binding API](https://developers.cloudflare.com/workers-vpc/api/).

Jun 16, 2026

[<h2>Workers tracing now supports custom spans</h2>](https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/)

[Workers](https://developers.cloudflare.com/workers/)

You can now create custom trace spans in your Workers code using `tracing.enterSpan()`. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.

The API is available via `import { tracing } from "cloudflare:workers"` or through the handler context as `ctx.tracing`:

```ts
import { tracing } from "cloudflare:workers";

export default {
  async fetch(request, env, ctx) {
    return tracing.enterSpan("handleRequest", async (span) => {
      span.setAttribute("url.path", new URL(request.url).pathname);
      const data = await env.MY_KV.get("key");
      return new Response(data);
    });
  },
};
```

Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The `Span` object provides `setAttribute(key, value)` for attaching metadata and an `isTraced` property to check whether the current request is being sampled.

![Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1988,height=670,format=webp/_astro/wobs_custom_spans_screenshot.B-hsHjyv.png)

[Tracing must be enabled](https://developers.cloudflare.com/workers/observability/traces/#how-to-enable-tracing) in your Wrangler configuration for spans to be recorded.

For full API details and examples, refer to [Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

Jun 15, 2026

[<h2>Use Cloudforce One threat intelligence in WAF rules</h2>](https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/)

[WAF](https://developers.cloudflare.com/waf/)

You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates `cf.intel.ip.*` fields that you can use in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/).

The detection populates the following fields. Use the [`any()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#any) function with the `[*]` wildcard to match array values:

- `cf.intel.ip.datasets` — the dataset that flagged the IP address ( `ddos` or `waf`).
- `cf.intel.ip.target_industries` — industries the IP address has targeted.
- `cf.intel.ip.attacker_names` — known threat actors associated with the IP address.
- `cf.intel.ip.attacker_countries` — source countries of the threat activity.
- `cf.intel.ip.target_countries` — countries the IP address has targeted.

For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:

```txt
any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")
```

These fields work with the Cloudflare API and Terraform. Matches are logged in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/).

The threat intelligence detection is available to customers with an active [Cloudforce One](https://developers.cloudflare.com/security-center/cloudforce-one/) subscription. For more information, refer to [Threat intelligence](https://developers.cloudflare.com/waf/detections/threat-intelligence/).

Jun 15, 2026

[<h2>WAF Release - 2026-06-15</h2>](https://developers.cloudflare.com/changelog/post/2026-06-15-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.

**Key Findings**

- CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...b4c29bc6 | N/A | Ghost CMS - SQLi - CVE:CVE-2026-26980 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...b56f403f | N/A | SQLi - Obfuscated Boolean - URI | Log | Disabled | This is a new detection. |

Jun 12, 2026

[<h2>View the user agent of requests in AI Gateway logs</h2>](https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from `openai-python` versus a custom application or a Cloudflare Worker.

The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.

For more information, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

Jun 12, 2026

[<h2>Filter Durable Objects metrics by object ID or name</h2>](https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

You can now filter the **Metrics** tab for a Durable Objects namespace by an individual Durable Object's [ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name) in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.

[Go to **Durable Objects** ↗](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) ![The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2936,height=1482,format=webp/_astro/durable-objects-metrics-dashboard.BFZTyhWU.png)

Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.

Metrics are powered by the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/), so standard analytics behavior such as ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) applies.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/).

Jun 12, 2026

[<h2>Terraform v5.20.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2026-06-12-terraform-v5.20.0-provider/)

[Terraform](https://developers.cloudflare.com/terraform/)

Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every [2-3 weeks ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.

#### New resources

- **cloudflare\_ai\_search\_namespace:** Manage AI Search namespaces
- **cloudflare\_custom\_csr:** Manage custom certificate signing requests
- **cloudflare\_dls\_prefix\_binding:** Manage DLS regional service prefix bindings
- **cloudflare\_flagship\_app:** Manage Flagship feature flag apps
- **cloudflare\_flagship\_flag:** Manage Flagship feature flags
- **cloudflare\_google\_tag\_gateway:** Manage Google Tag Gateway
- **cloudflare\_load\_balancer\_monitor\_group:** Manage load balancer monitor groups
- **cloudflare\_oauth\_client:** Manage IAM OAuth clients
- **cloudflare\_origin\_cloud\_region:** Manage origin cloud regions (v2 endpoints)
- **cloudflare\_secrets\_store:** Manage Secrets Store instances
- **cloudflare\_secrets\_store\_secret:** Manage Secrets Store secrets
- **cloudflare\_share:** Manage resource shares
- **cloudflare\_share\_recipient:** Manage share recipients
- **cloudflare\_share\_resource:** Manage shared resources
- **cloudflare\_zero\_trust\_device\_deployment\_groups:** Manage Zero Trust device deployment groups
- **cloudflare\_zero\_trust\_dlp\_data\_class:** Manage DLP data classes
- **cloudflare\_zero\_trust\_dlp\_data\_tag:** Manage DLP data tags
- **cloudflare\_zero\_trust\_dlp\_data\_tag\_category:** Manage DLP data tag categories
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_group:** Manage DLP sensitivity groups
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_level:** Manage DLP sensitivity levels
- **cloudflare\_zero\_trust\_dlp\_sensitivity\_level\_order:** Manage DLP sensitivity level ordering
- **cloudflare\_zero\_trust\_resource\_library\_application:** Manage Zero Trust resource library applications
- **cloudflare\_zero\_trust\_resource\_library\_category:** Manage Zero Trust resource library categories
- **cloudflare\_zero\_trust\_tunnel\_warp\_connector\_config:** Manage WARP connector tunnel configurations

#### Features

- **cache:** add create (POST) method for smart\_tiered\_cache
- **cache:** update OPCR config to v2 endpoints
- **dlp:** promote classification Stainless config to main
- **dlp:** add custom prompt topics endpoint
- **email\_security\_block\_sender:** state upgrader for v4 to v5 migration
- **email\_security\_impersonation\_registry:** state upgrader for v4 to v5 migration
- **email\_security\_trusted\_domains:** state upgrader for v4 to v5 migration
- **snippets:** add Terraform `id_property` annotations for snippet and snippet\_rules
- bump Go SDK to cloudflare-go v7

#### Bug fixes

- **account\_member:** missing upgrade path from v5.0–v5.15
- **authenticated\_origin\_pulls\_settings:** nil pointer panic
- **bot\_management:** restore `content_bots_protection` handling in model.go
- **dns\_record:** prevent FQDN normalization from swallowing name shortening changes
- **list:** nullify empty nested objects to prevent inconsistent result after apply
- **load\_balancer\_pool:** accept early-v5 object-shape state at schema\_version=0
- **load\_balancer\_pool:** add `UseStateForUnknown` for `load_shedding` attribute to prevent drift
- **r2\_custom\_domain:** restore degraded-response handling in resource.go
- **regional\_hostname:** update cloudflare-go imports from v6 to v7
- **secrets\_store:** fix model/schema parity and guard acceptance tests
- **spectrum\_application:** accept early-v5 object-shape state at schema\_version=0
- **worker:** preserve `observability.traces.propagation_policy` across reads
- **worker:** add `propagation_policy` to observability defaults
- **worker\_version:** restore handwritten D1 `database_id` handling
- **workers\_custom\_domain:** missing `CertId` field in state migration
- **workers\_script:** restore annotations Read workaround stripped by codegen
- **zero\_trust\_access\_identity\_provider:** change `read_only` from computed to optional
- **zero\_trust\_access\_identity\_provider:** add `UseStateForUnknown` to SAML-only config fields
- **zero\_trust\_access\_identity\_provider:** use `UseNonNullStateForUnknown` on scim\_config fields
- **zero\_trust\_access\_policy:** populate `account_id` when migrating zone-scoped v4 state
- **zero\_trust\_access\_policy:** missing `common_names` transform in migration
- gracefully handle nil pointer dereference when config has `attributes_flat` during migration
- set initial schema version to 500 for all new resources

#### Refactors

Extracted `MoveState` nil guard into shared helper

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

Jun 12, 2026

[<h2>Moonshot AI Kimi K2.7 Code now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.

#### Improved coding and agent performance

K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:

- **+21.8%** on Kimi Code Bench v2
- **+11.0%** on Program Bench
- **+31.5%** on MLS Bench Lite

#### Reasoning efficiency

K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.

#### Key capabilities

- **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
- **Long-horizon coding** with improved instruction following and higher end-to-end coding task success rates
- **Vision inputs** for processing images alongside text
- **Thinking mode** with configurable reasoning depth via `chat_template_kwargs.thinking`
- **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns
- **Structured outputs** with JSON schema support

#### Differences from Kimi K2.6

If you are migrating from Kimi K2.6, note the following:

- K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency
- Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)
- API usage is identical — no parameter changes required

#### Get started

Use Kimi K2.7 Code through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.7 Code model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Jun 11, 2026

[<h2>New formats parameter for the Browser Run /snapshot endpoint</h2>](https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/)'s [`/snapshot` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) now supports a `formats` parameter that lets you return multiple page formats in a single API call. Previously, `/snapshot` returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.

These formats are particularly useful for AI agent workflows:

- Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.
- The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.

The following example returns a screenshot, Markdown, and the accessibility tree in one call:

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/",
    "formats": ["screenshot", "markdown", "accessibilityTree"]
  }'
```

```typescript
import Cloudflare from "cloudflare";

const client = new Cloudflare({
	apiToken: process.env["CLOUDFLARE_API_TOKEN"],
});

const snapshot = await client.browserRendering.snapshot.create({
	account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
	url: "https://example.com/",
	formats: ["screenshot", "markdown", "accessibilityTree"],
});

console.log(snapshot.markdown);
console.log(snapshot.accessibilityTree);
```

```typescript
interface Env {
	BROWSER: BrowserRun;
}

export default {
	async fetch(request, env): Promise<Response> {
		return await env.BROWSER.quickAction("snapshot", {
			url: "https://example.com/",
			formats: ["screenshot", "markdown", "accessibilityTree"],
		});
	},
} satisfies ExportedHandler<Env>;
```

You must request at least two formats. If you only need one, use the respective single-format endpoint such as [`/screenshot`](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) or [`/markdown`](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/).

Refer to the [`/snapshot` documentation](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) for the full list of accepted values.

Jun 11, 2026

[<h2>Define custom topics for AI prompt protection</h2>](https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now define custom topics for AI prompt protection. Predefined [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.

You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a [custom wordlist or pattern entry](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets) instead.

Custom topics run through the same [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls) path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.

#### Create a custom AI prompt topic

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Data loss prevention** > **Detection entries**.
2. Select **AI prompt topics**, then select **Custom Prompt Topic**.
3. Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.
4. Add this detection entry to an existing DLP profile, or [create a new DLP profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile).
5. Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.

Note

Write the description as a concept to classify, not a list of keywords. For example, describe "internal financial forecasts and unreleased revenue figures" rather than listing specific document names.

For more information, refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

Jun 11, 2026

[<h2>Track Dynamic Workers usage from the dashboard and GraphQL API</h2>](https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/)

[Workers](https://developers.cloudflare.com/workers/)

![Dynamic Workers usage on the Workers overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=1102,format=webp/_astro/dynamic-workers-count.BcGsgQ0m.png)

Customers can now view the number of [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) invoked during their billing period from the Workers overview page in the Cloudflare dashboard.

This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.

You can also query this count through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) by using `workersInvocationsByOwnerAndScriptGroups` and selecting `distinctDynamicWorkerCount`:

```graphql
query getDynamicWorkersCount(
	$accountTag: string!
	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject
) {
	viewer {
		accounts(filter: { accountTag: $accountTag }) {
			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {
				uniq {
					distinctDynamicWorkerCount
				}
			}
		}
	}
}
```

Use variables to set the account and billing-period date range:

```json
{
	"accountTag": "<ACCOUNT_ID>",
	"filter": {
		"date_geq": "2026-06-01",
		"date_leq": "2026-06-30"
	}
}
```

For more information, refer to [Dynamic Workers pricing](https://developers.cloudflare.com/dynamic-workers/pricing/).

Jun 10, 2026

[<h2>Manage AI Search namespaces with Wrangler CLI</h2>](https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports namespace-level Wrangler commands, making it easier to manage [namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/) from your terminal, scripts, and agent workflows.

The following commands are available:

| Command | Description |
| --- | --- |
| `wrangler ai-search namespace list` | List AI Search namespaces |
| `wrangler ai-search namespace create` | Create a new AI Search namespace |
| `wrangler ai-search namespace get` | Get details for a namespace |
| `wrangler ai-search namespace update` | Update a namespace description |
| `wrangler ai-search namespace delete` | Delete an AI Search namespace |

Create a namespace for a new application or tenant directly from the CLI:

```sh
wrangler ai-search namespace create docs-production --description "Production documentation search"
```

List namespaces with pagination or filter by name or description:

```sh
wrangler ai-search namespace list --search docs --page 1 --per-page 10
```

Use `--json` with `list`, `create`, `get`, and `update` to return structured output that automation and AI agents can parse directly.

Instance-level commands also now support a `--namespace` flag, so you can interact with instances inside a specific namespace from the CLI:

```sh
wrangler ai-search list --namespace docs-production
```

For full usage details, refer to the [AI Search Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).

Jun 10, 2026

[<h2>Account-level DNS records quota</h2>](https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/)

[DNS](https://developers.cloudflare.com/dns/)

Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.

Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.

For more details, refer to [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).

Jun 10, 2026

[<h2>Flagship API reference now available</h2>](https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/)

[Flagship](https://developers.cloudflare.com/flagship/)

The **[Flagship API reference](https://developers.cloudflare.com/api/resources/flagship/)** is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.

For example, create a new boolean flag with the API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -d '{
    "key": "new-checkout",
    "enabled": true,
    "default_variation": "off",
    "variations": {
      "off": false,
      "on": true
    },
    "rules": []
  }'
```

To create an API token, go to [Account API Tokens ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens) in the Cloudflare dashboard and search for Flagship.

The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the [Flagship reference in the Cloudflare skill ↗︎](https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship) to create and manage Flagship resources.

Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/) to learn more about evaluating feature flags from your applications.

Jun 10, 2026

[<h2>Manage hosted images with the Images binding</h2>](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.

The `env.IMAGES.hosted` namespace supports the following storage and management operations:

- [`.upload(image, options)`](https://developers.cloudflare.com/images/storage/binding/#uploadimage-options) — Upload a new image to your account.
- [`.list(options)`](https://developers.cloudflare.com/images/storage/binding/#listoptions) — List images with pagination.
- [`.image(imageId).details()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddetails) — Get image metadata.
- [`.image(imageId).bytes()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidbytes) — Stream the original image bytes.
- [`.image(imageId).update(options)`](https://developers.cloudflare.com/images/storage/binding/#imageimageidupdateoptions) — Update metadata or access controls.
- [`.image(imageId).delete()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete) — Delete an image.

For example, you can upload an image from a request body and return its metadata:

```ts
const image = await env.IMAGES.hosted.upload(request.body, {
	filename: "upload.jpg",
	metadata: { source: "worker" },
});

return Response.json(image);
```

Or retrieve and serve the original bytes of a hosted image:

```ts
const bytes = await env.IMAGES.hosted.image("IMAGE_ID").bytes();
return new Response(bytes);
```

For more information, refer to the [Images binding](https://developers.cloudflare.com/images/storage/binding/).

Jun 10, 2026

[<h2>Automated Cease and Desist templates for Brand Protection</h2>](https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/)

[Security Center](https://developers.cloudflare.com/security-center/)

**TL;DR:** Brand Protection now features an **Automated Cease & Desist (C&D)** workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.

#### Why this matters

This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:

- **Instant WHOIS and Recipient Lookup:** We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent
- **Smart Template Automation:** We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.
- **Tailored Enforcement Tones:** Choose from three default layout strategies depending on the severity of the infrastructure match:
  - *Exact Match:* A formal demand for identical trademark infringements
  - *Similar Match:* A standard notice optimized for typosquatting (one-character distance matches)
  - *Friendly Tone:* An amicable initial outreach for potential unintentional or accidental infringements
- **Full Editing Control:** Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards

#### How it works

When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:

1. **On the Cloudflare Network:** If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.
2. **Hosted Elsewhere:** If the domain is hosted on an external provider, click the **Generate C&D Letter** option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.

You can manage your templates and enforce matches by going to the **Cloudflare Dashboard > Application Security > Brand Protection** and selecting your detected Brand Protection matches. For more information, read the [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

> **Note:** Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.

Jun 9, 2026

[<h2>Deprecating Sandbox SDK features</h2>](https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Sandbox SDK 1.0 preview

A preview of **Sandbox SDK 1.0** is available on `@cloudflare/sandbox@next`. For new projects, or to move past these deprecations in one migration, refer to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/).

Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.

We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/), or move to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) when you can.

#### HTTP and WebSocket transports

In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.

To migrate, update the `SANDBOX_TRANSPORT` variable to `rpc` or set the `transport` option when calling `getSandbox()`. For more information, refer to the [transport configuration documentation](https://developers.cloudflare.com/sandbox/configuration/transport/).

#### Desktop

The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same *computer-use* shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in `0.10.2`. If you need that capability again, you can build it on top of the sandbox with [extensions](https://developers.cloudflare.com/sandbox/1-0-preview/extensions/) rather than a built-in `sandbox.desktop` API.

#### Expose ports

We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to `workers.dev` domains. To migrate from `exposePort()` to tunnels, refer to the [tunnels API documentation](https://developers.cloudflare.com/sandbox/api/tunnels/) and the [expose services guide](https://developers.cloudflare.com/sandbox/guides/expose-services/).

#### Default sessions

By default, the `exec()` method in the Sandbox SDK maintains a default session across all calls, so a `cd` in one call is honored in the next. This convenience helped developers writing `exec` statements by hand, but confused agents and caused hard-to-trace bugs. As of `0.10.3`, we have introduced the [`enableDefaultSession`](https://developers.cloudflare.com/sandbox/configuration/sandbox-options/) flag on the `getSandbox()` interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.

We recommend setting `enableDefaultSession: false` today and using the [`sandbox.createSession()` API](https://developers.cloudflare.com/sandbox/api/sessions/) when you need the previous behavior.

#### Other changes

We are also consolidating all APIs that buffer data to support streaming by default. This includes [`readFile`, `writeFile`](https://developers.cloudflare.com/sandbox/api/files/), and [`exec`](https://developers.cloudflare.com/sandbox/api/commands/). The stream equivalents will be removed.

We are exploring moving non-core features like the [code interpreter](https://developers.cloudflare.com/sandbox/guides/code-execution/), [terminal](https://developers.cloudflare.com/sandbox/api/terminal/), and [git APIs](https://developers.cloudflare.com/sandbox/guides/git-workflows/) into helpers. These features will retain their existing APIs, so migration should be simple.

#### Next steps

If you use any of these features on the **current stable** package, refer to the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/). Coding agents can use the **`sandbox-stable`** skill for stable-package work and that guide for cleanup ([Agent setup](https://developers.cloudflare.com/agent-setup/) · [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)).

If you are moving to **Sandbox SDK 1.0** (`@next`), use the [1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/) guides instead — or the **`sandbox-migrate-to-next`** skill after installing Cloudflare Skills. New projects should prefer **`sandbox-next`** on `@next`.

For any questions, ask in the [Cloudflare Developers Discord ↗︎](https://discord.gg/cloudflaredev).

Jun 9, 2026

[<h2>WAF Release - 2026-06-09</h2>](https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.

**Key Findings**

- CVE-2026-9082: A database abstraction vulnerability affects Drupal sites configured with a PostgreSQL backend. Remote, unauthenticated attackers can exploit this flaw via crafted inputs to inject malicious SQL commands and access or manipulate backend data.
- CVE-2026-45247: A PHP Object Injection vulnerability exists in the Mirasvit Cache Warmer extension for Magento and Adobe Commerce. This flaw stems from unsafe deserialization of untrusted user input, enabling unauthenticated attackers to execute arbitrary code on the hosting server.
- CVE-2026-40175: A prototype pollution vulnerability affects the Axios HTTP client library. Attackers can exploit this to inject malicious properties into the global JavaScript object prototype, potentially causing application crashes (Denial of Service) or executing unauthorized code depending on the application structure.

**Impact**

Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, manipulate database contents, or induce application crashes, leading to severe operational disruption or complete server compromise. These newly deployed signatures intercept these advanced malicious payloads at the edge before they can interact with vulnerable software configurations.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...387cf935 | N/A | Axios - Prototype Pollution - CVE:CVE-2026-40175 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...417eb9e0 | N/A | Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - Body | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...fd3857fd | N/A | Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - URI | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...aee241d2 | N/A | SQLi - Obfuscated Boolean - Body | N/A | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...d8620070 | N/A | SQLi - Obfuscated Boolean - Headers | N/A | Disabled | This is a new detection. |
| Cloudflare Managed Ruleset | ...e0be4d47 | N/A | Mirasvit Cache Warmer - PHP Object Injection - CVE:CVE-2026-45247 | N/A | Block | This is a new detection. |

Jun 8, 2026

[<h2>R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT</h2>](https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports set operations (`UNION`, `INTERSECT`, `EXCEPT`) and `SELECT DISTINCT`, expanding the range of analytical queries you can run directly on [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### Set operations

Combine the results of multiple `SELECT` statements:

- **`UNION`** — returns all rows from both queries, removing duplicates
- **`UNION ALL`** — returns all rows from both queries, including duplicates
- **`INTERSECT`** — returns only rows that appear in both queries
- **`EXCEPT`** — returns rows from the first query that do not appear in the second

```sql
-- Find zones that had either firewall blocks OR high-risk requests
SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
UNION
SELECT zone_id FROM my_namespace.http_requests WHERE risk_score > 0.8
```

```sql
-- Find zones with both firewall blocks AND high traffic
SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
INTERSECT
SELECT zone_id FROM my_namespace.http_requests
GROUP BY zone_id
HAVING COUNT(*) > 10000
```

```sql
-- Find enterprise zones that have not been compacted
SELECT zone_id FROM my_namespace.zones WHERE plan = 'enterprise'
EXCEPT
SELECT zone_id FROM my_namespace.compaction_history
```

#### Select distinct

Eliminate duplicate rows from query results:

```sql
SELECT DISTINCT region, department
FROM my_namespace.sales_data
WHERE total_amount > 1000
ORDER BY region, department
LIMIT 100
```

For large datasets where approximate results are acceptable, `approx_distinct()` remains a faster alternative for counting unique values.

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

Jun 8, 2026

[<h2>Authenticated SMTP submission now available in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/)

[Email Service](https://developers.cloudflare.com/email-service/)

You can now send emails through **Cloudflare Email Service** using authenticated [SMTP submission](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) on `smtp.mx.cloudflare.net:465`. SMTP joins the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) and the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, `smtplib`, PHPMailer, JavaMail).

| Setting | Value |
| --- | --- |
| Host | `smtp.mx.cloudflare.net` |
| Port | `465` (implicit TLS) |
| AUTH | `PLAIN` or `LOGIN` |
| Username | `api_token` |
| Password | A Cloudflare API token (account-owned or user-owned) with **Email Sending: Edit** |

Submissions enter the same delivery pipeline as the REST API and Workers binding: identical [limits](https://developers.cloudflare.com/email-service/platform/limits/), automatic DKIM and ARC signing, and shared dashboard logs.

Send your first email with a single command:

```sh
curl --ssl-reqd \
  --url "smtps://smtp.mx.cloudflare.net:465" \
  --user "api_token:<API_TOKEN>" \
  --mail-from "welcome@yourdomain.com" \
  --mail-rcpt "user@example.com" \
  --upload-file mail.txt
```

Refer to the [SMTP reference](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) for authentication details, response codes, and language-specific examples.

Jun 8, 2026

[<h2>Post-meeting transcriptions are now Generally Available in RealtimeKit</h2>](https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/)

[Realtime](https://developers.cloudflare.com/realtime/)

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's [global WebRTC infrastructure](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/).

[Post-meeting transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-transcription) is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power [AI-generated summaries](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) for meeting notes, review workflows, and follow-up tasks after the transcript is available.

Post-meeting transcription is a managed service powered by [Workers AI](https://developers.cloudflare.com/workers-ai/) using [Whisper Large v3 Turbo](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/). RealtimeKit handles transcription processing and can return transcript and summary files through [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/) or the REST API, so you do not need to run your own transcription infrastructure.

#### Generate transcripts and summaries

To generate a transcript after a meeting ends, set `transcribe_on_end: true` when [creating a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/). To also generate an AI summary automatically after the transcript is available, set `summarize_on_end: true`:

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Weekly product review",
    "transcribe_on_end": true,
    "summarize_on_end": true,
    "ai_config": {
      "transcription": {
        "language": "en"
      },
      "summarization": {
        "word_limit": 500,
        "text_format": "markdown",
        "summary_type": "team_meeting"
      }
    }
  }'
```

#### Consume results

When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if `summarize_on_end` is set, the summary. You can receive those URLs automatically with [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/), or fetch them later for a specific session with the [REST API](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/#rest-api).

To receive results as soon as they are ready, configure the `meeting.transcript` and `meeting.summary` webhook events:

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI results webhook",
    "url": "https://example.com/webhook",
    "events": ["meeting.transcript", "meeting.summary"],
    "enabled": true
  }'
```

To fetch results later, call the [transcript](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/) or [summary](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/) endpoint for the session:

```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

Use the [Generate summary of transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/) API only if `summarize_on_end` was not set and you want to generate a summary manually after the transcript is available:

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

Post-meeting transcription supports [CSV, JSON, SRT, and VTT transcript outputs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#output-formats), [automatic language detection and Whisper language codes](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages). RealtimeKit also supports [real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#real-time-transcription) with [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) for live captions, in-meeting accessibility, and real-time note-taking.

Learn more in the [RealtimeKit transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) and [summary docs](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/).

Jun 8, 2026

[<h2>Create WAF rules directly from Threat Events saved views</h2>](https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/)

[Security Center](https://developers.cloudflare.com/security-center/)

Cloudforce One users can now turn [Threat Events indicators](https://developers.cloudflare.com/security-center/cloudforce-one/#analyze-threat-events) into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their **Saved Views**.

#### Why this matters

Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules. This new integration bridges the gap between threat discovery and threat mitigation:

- When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.
- Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.
- Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.

#### How to use it

You can implement these rules through both the dashboard UI and via the API / Terraform.

Go to **Cloudflare Dashboard** > **Application Security** > **Threat Intelligence** > **Manage Views**, select your desired view, and select **Create WAF Rule**.

This will automatically pre-populate the [WAF rule builder](https://developers.cloudflare.com/firewall/cf-dashboard/create-edit-delete-rules/) with the matching threat event IP indicators.

You can also automate this workflow by utilizing the [**WAF Rule Builder API**](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/) alongside your [Threat Events saved views endpoints](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/15/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/15/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
