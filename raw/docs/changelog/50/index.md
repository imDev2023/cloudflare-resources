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

Feb 25, 2025

[<h2>Use DLP Assist for M365</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-dlp-assist-for-m365/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security customers who have Microsoft 365 environments can quickly deploy an Email DLP (Data Loss Prevention) solution for free.

Simply deploy our add-in, create a DLP policy in Cloudflare, and configure Outlook to trigger behaviors like displaying a banner, alerting end users before sending, or preventing delivery entirely.

Refer to [Outbound Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) to learn more about this feature.

In GUI alert:

![DLP-Alert](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1357,height=212,format=webp/_astro/DLP-Alert.5s-fbKn3.png)

Alert before sending:

![DLP-Pop-up](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1362,height=479,format=webp/_astro/DLP-Pop-up.0gkYy7o5.png)

Prevent delivery:

![DLP-Blocked](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1353,height=329,format=webp/_astro/DLP-Blocked.CmQkGrnM.png)

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Feb 25, 2025

[<h2>Introducing the Agents SDK</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

We've released the [Agents SDK ↗︎](http://blog.cloudflare.com/build-ai-agents-on-cloudflare/), a package and set of tools that help you build and ship AI Agents.

You can get up and running with a [chat-based AI Agent ↗︎](https://github.com/cloudflare/agents-starter) (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:

```sh
npm create cloudflare@latest agents-starter -- --template="cloudflare/agents-starter"
# open up README.md and follow the instructions
```

You can also add an Agent to any existing Workers application by installing the `agents` package directly

```sh
npm i agents
```

... and then define your first Agent:

```ts
import { Agent } from "agents";

export class YourAgent extends Agent<Env> {
	// Build it out
	// Access state on this.state or query the Agent's database via this.sql
	// Handle WebSocket events with onConnect and onMessage
	// Run tasks on a schedule with this.schedule
	// Call AI models
	// ... and/or call other Agents.
}
```

Head over to the [Agents documentation](https://developers.cloudflare.com/agents/) to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.

Feb 25, 2025

[<h2>Workers AI now supports structured JSON outputs.</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Workers AI now supports structured JSON outputs with [JSON mode](https://developers.cloudflare.com/workers-ai/features/json-mode/), which allows you to request a structured output response when interacting with AI models.

This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.

JSON mode in Workers AI is compatible with the OpenAI SDK's [structured outputs ↗︎](https://platform.openai.com/docs/guides/structured-outputs) `response_format` API, which can be used directly in a Worker:

```js
import { OpenAI } from "openai";

// Define your JSON schema for a calendar event
const CalendarEventSchema = {
	type: "object",
	properties: {
		name: { type: "string" },
		date: { type: "string" },
		participants: { type: "array", items: { type: "string" } },
	},
	required: ["name", "date", "participants"],
};

export default {
	async fetch(request, env) {
		const client = new OpenAI({
			apiKey: env.OPENAI_API_KEY,
			// Optional: use AI Gateway to bring logs, evals & caching to your AI requests
			// https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
			// baseUrl: "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai"
		});

		const response = await client.chat.completions.create({
			model: "gpt-4o-2024-08-06",
			messages: [
				{ role: "system", content: "Extract the event information." },
				{
					role: "user",
					content: "Alice and Bob are going to a science fair on Friday.",
				},
			],
			// Use the `response_format` option to request a structured JSON output
			response_format: {
				// Set json_schema and provide ra schema, or json_object and parse it yourself
				type: "json_schema",
				schema: CalendarEventSchema, // provide a schema
			},
		});

		// This will be of type CalendarEventSchema
		const event = response.choices[0].message.parsed;

		return Response.json({
			calendar_event: event,
		});
	},
};
```

```ts
import { OpenAI } from "openai";

interface Env {
	OPENAI_API_KEY: string;
}

// Define your JSON schema for a calendar event
const CalendarEventSchema = {
	type: "object",
	properties: {
		name: { type: "string" },
		date: { type: "string" },
		participants: { type: "array", items: { type: "string" } },
	},
	required: ["name", "date", "participants"],
};

export default {
	async fetch(request: Request, env: Env) {
		const client = new OpenAI({
			apiKey: env.OPENAI_API_KEY,
			// Optional: use AI Gateway to bring logs, evals & caching to your AI requests
			// https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
			// baseUrl: "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai"
		});

		const response = await client.chat.completions.create({
			model: "gpt-4o-2024-08-06",
			messages: [
				{ role: "system", content: "Extract the event information." },
				{
					role: "user",
					content: "Alice and Bob are going to a science fair on Friday.",
				},
			],
			// Use the `response_format` option to request a structured JSON output
			response_format: {
				// Set json_schema and provide ra schema, or json_object and parse it yourself
				type: "json_schema",
				schema: CalendarEventSchema, // provide a schema
			},
		});

		// This will be of type CalendarEventSchema
		const event = response.choices[0].message.parsed;

		return Response.json({
			calendar_event: event,
		});
	},
};
```

To learn more about JSON mode and structured outputs, visit the [Workers AI documentation](https://developers.cloudflare.com/workers-ai/features/json-mode/).

Feb 25, 2025

[<h2>Concurrent Workflow instances limits increased.</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-workflows-concurrency-increased/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) now supports up to 4,500 concurrent (running) instances, up from the previous limit of 100. This limit will continue to increase during the Workflows open beta. This increase applies to all users on the Workers Paid plan, and takes effect immediately.

Review the Workflows [limits documentation](https://developers.cloudflare.com/workflows/reference/limits) and/or dive into the [get started guide](https://developers.cloudflare.com/workflows/get-started/guide/) to start building on Workflows.

Feb 24, 2025

[<h2>Bind the Images API to your Worker</h2>](https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now [interact with the Images API](https://developers.cloudflare.com/images/optimization/binding/) directly in your Worker.

This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.

The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:

```jsonc
{
	"images": {
		"binding": "IMAGES", // i.e. available in your Worker on env.IMAGES
	},
}
```

```toml
[images]
binding = "IMAGES"
```

Within your Worker code, you can interact with this binding by using `env.IMAGES`.

Here's how you can rotate, resize, and blur an image, then output the image as AVIF:

```ts
const info = await env.IMAGES.info(stream);
// stream contains a valid image, and width/height is available on the info object

const response = (
	await env.IMAGES.input(stream)
		.transform({ rotate: 90 })
		.transform({ width: 128 })
		.transform({ blur: 20 })
		.output({ format: "image/avif" })
).response();

return response;
```

For more information, refer to [Images Bindings](https://developers.cloudflare.com/images/optimization/binding/).

Feb 24, 2025

[<h2>Super Slurper now supports migrations from all S3-compatible storage providers</h2>](https://developers.cloudflare.com/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/)

[R2](https://developers.cloudflare.com/r2/)

[Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) can now migrate data from any S3-compatible object storage provider to [Cloudflare R2](https://developers.cloudflare.com/r2/). This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.

![Super Slurper S3-Compatible Source](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=757,height=348,format=webp/_astro/super-slurper-s3-compat-screenshot-border.D8Gd5eye.png)

For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our [documentation](https://developers.cloudflare.com/r2/data-migration/super-slurper/).

Feb 24, 2025

[<h2>WAF Release - 2025-02-24</h2>](https://developers.cloudflare.com/changelog/post/2025-02-24-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...4916911e | 100718A | SonicWall SSLVPN 2 - Auth Bypass - CVE:CVE-2024-53704 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...c382fdec | 100720 | Palo Alto Networks - Auth Bypass - CVE:CVE-2025-0108 | Log | Block | This is a New Detection |

Feb 24, 2025

[<h2>Workers AI larger context windows</h2>](https://developers.cloudflare.com/changelog/post/2025-02-24-context-windows/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.

This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.

Our [catalog page](https://developers.cloudflare.com/workers-ai/models/) provides more information about each model's supported context window.

Feb 24, 2025

[<h2>Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-02-24-zaraz-dash-placement/)

[Zaraz](https://developers.cloudflare.com/zaraz/)

![Zaraz at zone level to Tag management at account level](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1920,height=480,format=webp/_astro/zaraz-account-level.L5Bz9oN0.jpg)

Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the [Tag Management ↗︎](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz) section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.

These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the [Tag Setup ↗︎](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz) section of the dashboard, and select the zone you'd like to edit.

Feb 20, 2025

[<h2>Workers for Platforms - Instant dispatch for newly created User Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

[Workers for Platforms ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/) is an architecture wherein a centralized [dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) processes incoming requests and routes them to isolated sub-Workers, called [User Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers).

![Workers for Platforms Requests](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=711,format=webp/_astro/wfp-request.CZmZLaYf.png)

Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.

**With this update, first-time uploads of User Workers are now deployed synchronously**. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.

Feb 20, 2025

[<h2>Workers AI updated pricing</h2>](https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We've updated the Workers AI [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) to include the latest models and how model usage maps to Neurons.

- Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale
- Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.
- You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.

Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) page to learn more about Workers AI pricing.

Feb 20, 2025

[<h2>Autofix Worker name configuration errors at build time</h2>](https://developers.cloudflare.com/changelog/post/2025-02-20-builds-name-conflict/)

[Workers](https://developers.cloudflare.com/workers/)

![Auto-fixing Workers Name in Git Repo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2416,height=1128,format=webp/_astro/gh-auto-pr-name.BHTtigEg.png)

Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.

Here's how it works:

1. Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.
2. Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.
3. Once you merge this pull request, Cloudflare will run another build.

We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.

This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, [#workers-and-pages-feature-suggestions ↗︎](https://discord.com/channels/595317990191398933/1064502845061210152).

Feb 18, 2025

[<h2>WAF Release - 2025-02-18</h2>](https://developers.cloudflare.com/changelog/post/2025-02-18-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a2ffa4b8 | 100715 | FortiOS - Auth Bypass - CVE:CVE-2024-55591 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5a883e12 | 100716 | Ivanti - Auth Bypass - CVE:CVE-2021-44529 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...958094d3 | 100717 | SimpleHelp - Auth Bypass - CVE:CVE-2024-57727 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...3b66df22 | 100718 | SonicWall SSLVPN - Auth Bypass - CVE:CVE-2024-53704 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...9184699f | 100719 | Yeti Platform - Auth Bypass - CVE:CVE-2024-46507 | Log | Block | This is a New Detection |

Feb 14, 2025

[<h2>Customize queue message retention periods</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/)

[Queues](https://developers.cloudflare.com/queues/)

You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.

![Customize a queue's message retention period](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1898,height=986,format=webp/_astro/customize-retention-period.CpK7s10q.png)

You can customize the retention period on the settings page for your queue, or using Wrangler:

*Update message retention periodbash*

```bash
$ wrangler queues update my-queue --message-retention-period-secs 600
```

This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

Feb 14, 2025

[<h2>Build AI Agents with Example Prompts</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

We've added an [example prompt](https://developers.cloudflare.com/workers/get-started/prompting/) to help you get started with building AI agents and applications on Cloudflare [Workers](https://developers.cloudflare.com/workers/), including [Workflows](https://developers.cloudflare.com/workflows/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Workers KV](https://developers.cloudflare.com/kv/).

You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the `<user_prompt></user_prompt>` tags.

```sh
{paste_prompt_here}
<user_prompt>
user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label 'help' or 'bug', and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.
</user_prompt>
```

This prompt is still experimental, but we encourage you to try it out and [provide feedback ↗︎](https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml).

Feb 14, 2025

[<h2>Configure your Magic WAN Connector to connect via static IP assignment</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now locally configure your [Magic WAN Connector](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) to work in a static IP configuration.

This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.

For more details, refer to [WAN with a static IP address](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console).

Feb 14, 2025

[<h2>Super Slurper now transfers data to R2 up to 5x faster</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/)

[R2](https://developers.cloudflare.com/r2/)

[Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to [Cloudflare R2](https://developers.cloudflare.com/r2/) up to 5x faster than it did before.

We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using [Cloudflare Workers](https://developers.cloudflare.com/workers/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Queues](https://developers.cloudflare.com/queues/) — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)

![Super Slurper Objects Migrated](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=974,height=493,format=webp/_astro/slurper-objects-over-time-border.BFDkMQUw.png)

*Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)*

For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our [documentation](https://developers.cloudflare.com/r2/data-migration/super-slurper/).

Feb 14, 2025

[<h2>Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.

Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.

```plaintext
curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \
    -H 'Content-Type: application/json' \
    -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    -H "X-Auth-Key: $CLOUDFLARE_API_KEY" \
    -d '{
    "hostname": "hostname",
    "ssl": {
        "custom_cert_bundle": [
            {
                "custom_certificate": "RSA Cert",
                "custom_key": "RSA Key"
            },
            {
                "custom_certificate": "ECDSA Cert",
                "custom_key": "ECDSA Key"
            }
        ],
        "bundle_method": "force",
        "wildcard": false,
        "settings": {
            "min_tls_version": "1.0"
        }
    }
}’
```

You can also:

- [Upload](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/) an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.
- [Replace](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/) the RSA or ECDSA certificate with a certificate of its same type.
- [Delete](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/) the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).

This feature is available for Business and Enterprise customers who have purchased custom certificates.

Feb 14, 2025

[<h2>Rewind, Replay, Resume: Introducing DVR for Stream Live</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/)

[Stream](https://developers.cloudflare.com/stream/)

Previously, all viewers watched "the live edge," or the latest content of the broadcast, synchronously. If a viewer paused for more than a few seconds, the player would automatically "catch up" when playback started again. Seeking through the broadcast was only available once the recording was available after it concluded.

Starting today, customers can make a small adjustment to the player embed or manifest URL to enable the DVR experience for their viewers. By offering this feature as an opt-in adjustment, our customers are empowered to pick the best experiences for their applications.

When building a player embed code or manifest URL, just add `dvrEnabled=true` as a query parameter. There are some things to be aware of when using this option. For more information, refer to [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/).

Feb 12, 2025

[<h2>Configurable multiplexing HTTP/2 to Origin</h2>](https://developers.cloudflare.com/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.

#### How it works

HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:

1. **Control concurrent streams**: Adjust the maximum number of concurrent streams per connection.
2. **Optimize connection reuse**: Fine-tune connection pooling behavior for your origin infrastructure.
3. **Reduce connection overhead**: Minimize the number of TCP connections required between Cloudflare and your origin.
4. **Improve cache performance**: Better connection management can enhance cache fetch efficiency.

#### Benefits

- **Customizable performance**: Tailor multiplexing settings to your origin's capabilities.
- **Reduced latency**: Fewer connection handshakes improve response times.
- **Lower origin load**: More efficient connection usage reduces server resource consumption.
- **Enhanced scalability**: Better connection management supports higher traffic volumes.

#### Get started

Enterprise customers can configure HTTP/2 multiplexing settings in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/) or through our [API](https://developers.cloudflare.com/api/).

Important consideration

This setting needs to be tuned carefully for your origin infrastructure. Setting the concurrent stream limit too high can negatively impact performance by saturating the shared TCP connection and overwhelming server processing capacity, leading to increased latency for individual requests.

Feb 12, 2025

[<h2>Increased Cloudflare Rules limits</h2>](https://developers.cloudflare.com/changelog/post/2025-02-12-rules-upgraded-limits/)

[Rules](https://developers.cloudflare.com/rules/)

We have upgraded and streamlined [Cloudflare Rules](https://developers.cloudflare.com/rules/) limits across all plans, simplifying rule management and improving scalability for everyone.

**New limits by product:**

- [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)
  - Free: **20** → **10,000** URL redirects across lists
  - Pro: **500** → **25,000** URL redirects across lists
  - Business: **500** → **50,000** URL redirects across lists
  - Enterprise: **10,000** → **1,000,000** URL redirects across lists
- [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  - Free: **5** → **10** connectors
  - Enterprise: **125** → **300** connectors
- [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)
  - Pro: **5** → **25** error assets and rules
  - Business: **20** → **50** error assets and rules
  - Enterprise: **50** → **300** error assets and rules
- [Snippets](https://developers.cloudflare.com/rules/snippets/)
  - Pro: **10** → **25** code snippets and rules
  - Business: **25** → **50** code snippets and rules
  - Enterprise: **50** → **300** code snippets and rules
- [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/), [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), [Compression Rules](https://developers.cloudflare.com/rules/compression-rules/), [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/), [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/), and [Transform Rules](https://developers.cloudflare.com/rules/transform/)
  - Enterprise: **125** → **300** rules

Gradual rollout

Limits are updated gradually. Some customers may still see previous limits until the rollout is fully completed in the first half of 2025.

Feb 11, 2025

[<h2>Custom Errors (beta): Stored Assets & Account-level Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-02-11-custom-errors-beta/)

[Rules](https://developers.cloudflare.com/rules/)

We're introducing [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.

This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.

This brings the following new capabilities:

- **Custom error assets** – Fetch and store external error pages at the edge for use in error responses.
- **Account-Level custom errors** – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.

You can use Cloudflare API to upload your existing assets for use with Custom Errors:

```bash
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "name": "maintenance",
  "description": "Maintenance template page",
  "url": "https://example.com/"
}'
```

You can then reference the stored asset in a Custom Error rule:

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint" \
--header "Authorization: Bearer <API_TOKEN>" \
--header 'Content-Type: application/json' \
--data '{
  "rules": [
		{
			"action": "serve_error",
			"action_parameters": {
				"asset_name": "maintenance",
				"content_type": "text/html",
				"status_code": 503
			},
			"enabled": true,
			"expression": "http.request.uri.path contains \"error\""
		}
	]
}'
```

Feb 11, 2025

[<h2>WAF Release - 2025-02-11</h2>](https://developers.cloudflare.com/changelog/post/2025-02-11-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...483b4c26 | 100708 | Aviatrix Network - Remote Code Execution - CVE:CVE-2024-50603 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...7e924ca3 | 100709 | Next.js - Remote Code Execution - CVE:CVE-2024-46982 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...83a7d8ff | 100710 | Progress Software WhatsUp Gold - Directory Traversal - CVE:CVE-2024-12105 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...baa8eb34 | 100711 | WordPress - Remote Code Execution - CVE:CVE-2024-56064 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...87f5d34e | 100712 | WordPress - Remote Code Execution - CVE:CVE-2024-9047 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...bf72cf8a | 100713 | FortiOS - Auth Bypass - CVE:CVE-2022-40684 | Log | Block | This is a New Detection |

Feb 7, 2025

[<h2>Open email links with Security Center</h2>](https://developers.cloudflare.com/changelog/post/2025-02-07-open-links-security-center/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now investigate links in emails with Cloudflare Security Center to generate a report containing a myriad of technical details: a phishing scan, SSL certificate data, HTTP request and response data, page performance data, DNS records, what technologies and libraries the page uses, and more.

![Open links in Security Center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1118,height=402,format=webp/_astro/Open-Links-Security-Center.b-LJU4YB.png)

From **Investigation**, go to **View details**, and look for the **Links identified** section. Select **Open in Security Center** next to each link. **Open in Security Center** allows your team to quickly generate a detailed report about the link with no risk to the analyst or your environment.

For more details, refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Feb 7, 2025

[<h2>Create and deploy Workers from Git repositories</h2>](https://developers.cloudflare.com/changelog/post/2025-02-07-new-ways-to-get-started-on-workers/)

[Workers](https://developers.cloudflare.com/workers/)

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3607,height=1312,format=webp/_astro/choose-template-import-repo.Ci4KQPnT.png)

You can now create a Worker by:

- **Importing a Git repository**: Choose an existing Git repo on your GitHub/GitLab account and set up [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/) to deploy your Worker.
- **Deploying a template with Git**: Choose from a brand new selection of production ready [examples ↗︎](https://github.com/cloudflare/templates) to help you get started with popular frameworks like [Astro ↗︎](https://astro.build/), [Remix ↗︎](https://remix.run/) and [Next ↗︎](https://nextjs.org/) or build stateful applications with Cloudflare resources like [D1 databases](https://developers.cloudflare.com/d1/), [Workers AI](https://developers.cloudflare.com/workers-ai/) or [Durable Objects](https://developers.cloudflare.com/durable-objects/)! When you're ready to deploy, Cloudflare will set up your project by cloning the template to your GitHub/GitLab account, provisioning any required [resources](https://developers.cloudflare.com/workers/runtime-apis/bindings/) and deploying your Worker.

With every push to your chosen branch, Cloudflare will automatically build and deploy your Worker.

To get started, go to the [Workers dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create).

These new features are available today in the Cloudflare dashboard to a subset of Cloudflare customers, and will be coming to all customers in the next few weeks. Don't see it in your dashboard, but want early access? Add your Cloudflare Account ID to [this form ↗︎](https://forms.gle/U1qhkF2snNJDGJJa9).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/50/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/50/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
