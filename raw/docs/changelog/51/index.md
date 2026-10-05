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

Feb 6, 2025

[<h2>Request timeouts and retries with AI Gateway</h2>](https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway adds additional ways to handle requests - [Request Timeouts](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) and [Request Retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries), making it easier to keep your applications responsive and reliable.

Timeouts and retries can be used on both the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) or directly to a [supported provider](https://developers.cloudflare.com/ai-gateway/usage/providers/).

**Request timeouts** A [request timeout](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) allows you to trigger [fallbacks](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/) or a retry if a provider takes too long to respond.

To set a request timeout directly to a provider, add a `cf-aig-request-timeout` header.

*Provider-specific endpoint examplebash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \
 --header 'Authorization: Bearer {cf_api_token}' \
 --header 'Content-Type: application/json' \
 --header 'cf-aig-request-timeout: 5000'
 --data '{"prompt": "What is Cloudflare?"}'
```

**Request retries** A [request retry](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) automatically retries failed requests, so you can recover from temporary issues without intervening.

To set up request retries directly to a provider, add the following headers:

- cf-aig-max-attempts (number)
- cf-aig-retry-delay (number)
- cf-aig-backoff ("constant" | "linear" | "exponential)

Feb 5, 2025

[<h2>AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</h2>](https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) has added three new providers: [Cartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/), [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/), and [ElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/), giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:

- [Cartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/) provides text-to-speech models that produce natural-sounding speech with low latency.
- [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/) delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.
- [ElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/) offers text-to-speech models with human-like voices in 32 languages.

![Example of Cerebras log in AI Gateway](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2278,height=1020,format=webp/_astro/cerebras2.qHYP0ZnF.png)

To get started with AI Gateway, just update the base URL. Here's how you can send a request to [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/) using cURL:

*Example fetch requestbash*

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer CEREBRAS_TOKEN' \
 --data '{
    "model": "llama-3.3-70b",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

Feb 4, 2025

[<h2>Fight CSAM More Easily Than Ever</h2>](https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now implement our **child safety tooling**, the **[CSAM Scanning Tool](https://developers.cloudflare.com/cache/reference/csam-scanning/)**, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.

**How It Works**

When enabled, the tool automatically [hashes images for enabled websites as they enter the Cloudflare cache ↗︎](https://blog.cloudflare.com/the-csam-scanning-tool/). These hashes are then checked against a database of **known abusive images**.

- **Potential match detected?**
  - The **content URL is blocked**, and
  - **Cloudflare will notify you** about the found matches via the provided email address.

**Updated Service-Specific Terms**

We have also made updates to our **[Service-Specific Terms ↗︎](https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms)** to reflect these changes.

Feb 4, 2025

[<h2>Expanded AI insights in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-02-04-radar-ai-insights/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its AI insights with new API endpoints for Internet services rankings, robots.txt analysis, and AI inference data.

#### Internet services ranking

Radar now provides [rankings for Internet services](https://developers.cloudflare.com/radar/glossary/#internet-services-ranking), including Generative AI platforms, based on anonymized 1.1.1.1 resolver data. Previously limited to the annual Year in Review, these insights are now available daily via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/), through the following endpoints:

- [`/ranking/internet_services/top`](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/) show service popularity at a specific date.
- [`/ranking/internet_services/timeseries_groups`](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups/) track ranking trends over time.

#### Robots.txt

Radar now analyzes [robots.txt](https://developers.cloudflare.com/radar/glossary/#robotstxt) files from the top 10,000 domains, identifying AI bot access rules. AI-focused user agents from [ai.robots.txt ↗︎](https://github.com/ai-robots-txt/ai.robots.txt) are categorized as:

- **Fully allowed/disallowed** if directives apply to all paths ( `*`).
- **Partially allowed/disallowed** if restrictions apply to specific paths.

These insights are now available weekly via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/), through the following endpoints:

- [`/robots_txt/top/user_agents/directive`](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive/) to get the top AI user agents by directive.
- [`/robots_txt/top/domain_categories`](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories/) to get the top domain categories by robots.txt files.

#### Workers AI

Radar now provides insights into public AI inference models from [Workers AI](https://developers.cloudflare.com/workers-ai/), tracking usage trends across **models** and **tasks**. These insights are now available via the [API](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/), through the following endpoints:

- [`/ai/inference/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/) to view aggregated `model` and `task` popularity.
- [`/ai/inference/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/) to track changes over time for `model` or `task`.

Learn more about the new Radar AI insights in our [blog post ↗︎](https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/).

Feb 4, 2025

[<h2>Updated leaked credentials database</h2>](https://developers.cloudflare.com/changelog/post/2025-02-04-updated-leaked-credentials-database/)

[WAF](https://developers.cloudflare.com/waf/)

Added new records to the leaked credentials database from a third-party database.

Feb 3, 2025

[<h2>Block files that are password-protected, compressed, or otherwise unscannable.</h2>](https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.

These unscannable files are now matched with the [Download and Upload File Types traffic selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) for HTTP policies:

- Password-protected Microsoft Office document
- Password-protected PDF
- Password-protected ZIP archive
- Unscannable ZIP archive

To get started inspecting and modifying behavior based on these and other rules, refer to [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/).

Feb 3, 2025

[<h2>Terraform v5 Provider is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2025-02-03-terraform-v5-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

![Screenshot of Terraform defining a Zone](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1330,height=296,format=webp/_astro/2024-02-03-terraform-v5-screenshot.mW8OaFoS.png)

Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.

The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the [upgrade guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade) for best practices, or the [blog post on automatically generating Cloudflare's Terraform Provider ↗︎](https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/) for more information about the approach.

For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

Feb 3, 2025

[<h2>Revamped Workers Metrics</h2>](https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/)

[Workers](https://developers.cloudflare.com/workers/)

We've revamped the [Workers Metrics dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/).

![Workers Metrics dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3032,height=1756,format=webp/_astro/workers-metrics.IxYk9yF0.png)

Now you can easily compare metrics across Worker versions, understand the current state of a [gradual deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/), and review key Workers metrics in a single view. This new interface enables you to:

- Drag-and-select using a graphical timepicker for precise metric selection.

![Workers Metrics graphical timepicker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1944,height=932,format=webp/_astro/metrics-graphical-timepicker.tzLlEF5U.png)

- Use histograms to visualize cumulative metrics, allowing you to bucket and compare rates over time.
- Focus on Worker versions by directly interacting with the version numbers in the legend.

![Workers Metrics legend selector](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2308,height=1068,format=webp/_astro/metrics-legend-selector.B2GY90Hn.png)

- Monitor and compare active gradual deployments.
- Track error rates across versions with grouping both by version and by invocation status.
- Measure how [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) improves request duration.

Learn more about [metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics).

Feb 2, 2025

[<h2>Removed unused meta fields from DNS records</h2>](https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/)

[DNS](https://developers.cloudflare.com/dns/)

Cloudflare is removing five fields from the `meta` object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.

The affected fields are:

- the `auto_added` boolean
- the `managed_by_apps` boolean and corresponding `apps_install_id`
- the `managed_by_argo_tunnel` boolean and corresponding `argo_tunnel_id`

An example record returned from the API would now look like the following:

*Updated API Responsejson*

```json
{
	"result": {
		"id": "<ID>",
		"zone_id": "<ZONE_ID>",
		"zone_name": "example.com",
		"name": "www.example.com",
		"type": "A",
		"content": "192.0.2.1",
		"proxiable": true,
		"proxied": false,
		"ttl": 1,
		"locked": false,
		"meta": {
			"auto_added": false,
			"managed_by_apps": false,
			"managed_by_argo_tunnel": false,
			"source": "primary"
		},
		"comment": null,
		"tags": [],
		"created_on": "2025-03-17T20:37:05.368097Z",
		"modified_on": "2025-03-17T20:37:05.368097Z"
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

For more guidance, refer to [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/).

Jan 31, 2025

[<h2>Workers for Platforms now supports Static Assets</h2>](https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.

This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.

#### What you can build

**Static Sites:** Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.

**Full-Stack Applications:** Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.

*index.jsjs*

```js
export default {
	async fetch(request, env) {
		const url = new URL(request.url);

		// Check real-time inventory
		if (url.pathname === "/api/inventory/check") {
			const product = url.searchParams.get("product");
			const inventory = await env.INVENTORY_KV.get(product);
			return new Response(inventory);
		}

		// Serve static assets (HTML, CSS, images)
		return env.ASSETS.fetch(request);
	},
};
```

*index.tsts*

```ts
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Check real-time inventory
    if (url.pathname === '/api/inventory/check') {
      const product = url.searchParams.get('product');
      const inventory = await env.INVENTORY_KV.get(product);
      return new Response(inventory);
    }

    // Serve static assets (HTML, CSS, images)
    return env.ASSETS.fetch(request);
  }
};
```

**Get Started:** Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our [Workers for Platforms documentation. ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/)

Jan 31, 2025

[<h2>Transform HTML quickly with streaming content</h2>](https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/)

[Workers](https://developers.cloudflare.com/workers/)

You can now transform HTML elements with streamed content using [`HTMLRewriter`](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter).

Methods like `replace`, `append`, and `prepend` now accept [`Response`](https://developers.cloudflare.com/workers/runtime-apis/response/) and [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/) values as [`Content`](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/#global-types).

This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin, and want to replace an element with content from a different source. Prior to this change, you would have to load all of the content from the upstream URL and convert it into a string before replacing the element. This slowed down overall response times.

Now, you can pass the `Response` object directly into the `replace` method, and HTMLRewriter will immediately start replacing the content as it is streamed in. This makes responses faster.

*index.jsjs*

```js
class ElementRewriter {
	async element(element) {
		// able to replace elements while streaming content
		// the fetched body is not buffered into memory as part
		// of the replace
		let res = await fetch("https://upstream-content-provider.example");
		element.replace(res);
	}
}

export default {
	async fetch(request, env, ctx) {
		let response = await fetch("https://site-to-replace.com");
		return new HTMLRewriter()
			.on("[data-to-replace]", new ElementRewriter())
			.transform(response);
	},
};
```

*index.tsts*

```ts
class ElementRewriter {
	async element(element: any) {
		// able to replace elements while streaming content
		// the fetched body is not buffered into memory as part
		// of the replace
		let res = await fetch('https://upstream-content-provider.example');
		element.replace(res);
	}
}

export default {
	async fetch(request, env, ctx): Promise<Response> {
		let response = await fetch('https://site-to-replace.com');
		return new HTMLRewriter().on('[data-to-replace]', new ElementRewriter()).transform(response);
	},
} satisfies ExportedHandler<Env>;
```

For more information, see the [`HTMLRewriter` documentation](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter).

Jan 30, 2025

[<h2>AI Gateway Introduces New Worker Binding Methods</h2>](https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

We have released new [Workers bindings API methods](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.

To add an AI binding to your Worker, include the following in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):

![Add an AI binding to your Worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=754,height=135,format=webp/_astro/add-binding.BoYTiyon.png)

With the new AI Gateway binding methods, you can now:

- Send feedback and update metadata with `patchLog`.
- Retrieve detailed log information using `getLog`.
- Execute [universal requests](https://developers.cloudflare.com/ai-gateway/usage/universal/) to any AI Gateway provider with `run`.

For example, to send feedback and update metadata using `patchLog`:

![Send feedback and update metadata using patchLog:](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=736,height=235,format=webp/_astro/send-feedback.BGRzKmd9.png)

Jan 30, 2025

[<h2>Increased Browser Rendering limits!</h2>](https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/)

[Workers](https://developers.cloudflare.com/workers/) [Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) now supports 10 concurrent browser instances per account *and* 10 new instances per minute, up from the previous limits of 2.

This allows you to launch more browser tasks from [Cloudflare Workers](https://developers.cloudflare.com/workers).

To manage concurrent browser sessions, you can use [Queues](https://developers.cloudflare.com/queues/) or [Workflows](https://developers.cloudflare.com/workflows/):

*index.jsjs*

```js
export default {
	async queue(batch, env) {
		for (const message of batch.messages) {
			const browser = await puppeteer.launch(env.BROWSER);
			const page = await browser.newPage();

			try {
				await page.goto(message.url, {
					waitUntil: message.waitUntil,
				});
				// Process page...
			} finally {
				await browser.close();
			}
		}
	},
};
```

*index.tsts*

```ts
interface QueueMessage {
	url: string;
	waitUntil: number;
}

export interface Env {
	BROWSER_QUEUE: Queue<QueueMessage>;
	BROWSER: Fetcher;
}

export default {
	async queue(batch: MessageBatch<QueueMessage>, env: Env): Promise<void> {
		for (const message of batch.messages) {
			const browser = await puppeteer.launch(env.BROWSER);
			const page = await browser.newPage();

			try {
				await page.goto(message.url, {
					waitUntil: message.waitUntil,
				});
				// Process page...
			} finally {
				await browser.close();
			}
		}
	},
};
```

Jan 30, 2025

[<h2>Expanded language support for Stream AI Generated Captions</h2>](https://developers.cloudflare.com/changelog/post/2025-01-30-stream-generated-captions-new-languages/)

[Stream](https://developers.cloudflare.com/stream/)

Stream's [generated captions](https://developers.cloudflare.com/stream/edit-videos/adding-captions/#generate-a-caption) leverage Workers AI to automatically transcribe audio and provide captions to the player experience. We have added support for these languages:

- `cs` - Czech
- `nl` - Dutch
- `fr` - French
- `de` - German
- `it` - Italian
- `ja` - Japanese
- `ko` - Korean
- `pl` - Polish
- `pt` - Portuguese
- `ru` - Russian
- `es` - Spanish

For more information, learn about [adding captions to videos](https://developers.cloudflare.com/stream/edit-videos/adding-captions/).

Jan 29, 2025

[<h2>New Snippets Code Editor</h2>](https://developers.cloudflare.com/changelog/post/2025-01-29-snippets-code-editor/)

[Rules](https://developers.cloudflare.com/rules/)

The new [Snippets](https://developers.cloudflare.com/rules/snippets/) code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.

![New Snippets code editor](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3446,height=1690,format=webp/_astro/snippets-new-editor.CaoIu2_-.png)

What’s new:

- **Single-page editing for code and rule** – No need to jump between screens.
- **Auto-complete & syntax highlighting** – Get suggestions and avoid mistakes.
- **Code formatting & refactoring** – Write cleaner, more readable code.

Try it now in [Rules > Snippets ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets).

Jan 28, 2025

[<h2>Automatic configuration for private databases on Hyperdrive</h2>](https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.

![Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1814,height=922,format=webp/_astro/hyperdrive-private-database-automatic-configuration.BT4_KLwW.png)

When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.

To create a Hyperdrive for a private database, you can follow the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/). You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.

This feature is available from the Cloudflare dashboard.

Jan 28, 2025

[<h2>Workers KV namespace limits increased to 1000</h2>](https://developers.cloudflare.com/changelog/post/2025-01-27-kv-increased-namespaces-limits/)

[KV](https://developers.cloudflare.com/kv/)

You can now have up to 1000 Workers KV namespaces per account.

Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.

Consult the [Workers KV limits documentation](https://developers.cloudflare.com/kv/platform/limits/) for the rest of the limits. This increased limit is available for both the Free and Paid [Workers plans](https://developers.cloudflare.com/workers/platform/pricing/).

Jan 28, 2025

[<h2>Support for Node.js DNS, Net, and Timer APIs in Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-01-28-nodejs-compat-improvements/)

[Workers](https://developers.cloudflare.com/workers/)

When using a Worker with the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag enabled, you can now use the following Node.js APIs:

- [`node:net`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/)
- [`node:dns`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/)
- [`node:timers`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/)

#### node:net

You can use [`node:net` ↗︎](https://nodejs.org/api/net.html) to create a direct connection to servers via a TCP sockets with [`net.Socket` ↗︎](https://nodejs.org/api/net.html#class-netsocket).

*index.jsjs*

```js
import net from "node:net";

const exampleIP = "127.0.0.1";

export default {
	async fetch(req) {
		const socket = new net.Socket();
		socket.connect(4000, exampleIP, function () {
			console.log("Connected");
		});

		socket.write("Hello, Server!");
		socket.end();

		return new Response("Wrote to server", { status: 200 });
	},
};
```

*index.tsts*

```ts
import net from "node:net";

const exampleIP = "127.0.0.1";

export default {
  async fetch(req): Promise<Response> {
    const socket = new net.Socket();
    socket.connect(4000, exampleIP, function () {
      console.log("Connected");
    });

    socket.write("Hello, Server!");
    socket.end();

    return new Response("Wrote to server", { status: 200 });
  },
} satisfies ExportedHandler;
```

Additionally, you can now use other APIs including [`net.BlockList` ↗︎](https://nodejs.org/api/net.html#class-netblocklist) and [`net.SocketAddress` ↗︎](https://nodejs.org/api/net.html#class-netsocketaddress).

Note that [`net.Server` ↗︎](https://nodejs.org/api/net.html#class-netserver) is not supported.

#### node:dns

You can use [`node:dns` ↗︎](https://nodejs.org/api/dns.html) for name resolution via [DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) using [Cloudflare DNS ↗︎](https://www.cloudflare.com/application-services/products/dns/) at 1.1.1.1.

*index.jsjs*

```js
import dns from "node:dns";

let response = await dns.promises.resolve4("cloudflare.com", "NS");
```

*index.tsts*

```ts
import dns from 'node:dns';

let response = await dns.promises.resolve4('cloudflare.com', 'NS');
```

All `node:dns` functions are available, except `lookup`, `lookupService`, and `resolve` which throw "Not implemented" errors when called.

#### node:timers

You can use [`node:timers` ↗︎](https://nodejs.org/api/timers.html) to schedule functions to be called at some future period of time.

This includes [`setTimeout` ↗︎](https://nodejs.org/api/timers.html#settimeoutcallback-delay-args) for calling a function after a delay, [`setInterval` ↗︎](https://nodejs.org/api/timers.html#setintervalcallback-delay-args) for calling a function repeatedly, and [`setImmediate` ↗︎](https://nodejs.org/api/timers.html#setimmediatecallback-args) for calling a function in the next iteration of the event loop.

*index.jsjs*

```js
import timers from "node:timers";

console.log("first");
timers.setTimeout(() => {
	console.log("last");
}, 10);

timers.setTimeout(() => {
	console.log("next");
});
```

*index.tsts*

```ts
import timers from "node:timers";

console.log("first");
timers.setTimeout(() => {
  console.log("last");
}, 10);

timers.setTimeout(() => {
  console.log("next");
});
```

Jan 21, 2025

[<h2>WAF Release - 2025-01-21</h2>](https://developers.cloudflare.com/changelog/post/2025-01-21-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...b090ba9a | 100303 | Command Injection - Nslookup | Log | Block | This was released as ...b8d152f4 |
| Cloudflare Managed Ruleset | ...49e6b538 | 100534 | Web Shell Activity | Log | Block | This was released as ...82fe4e7f |

Jan 20, 2025

[<h2>Detect source code leaks with Data Loss Prevention</h2>](https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.

The following programming languages are validated with natural language processing (NLP).

- C
- C++
- C#
- Go
- Haskell
- Java
- JavaScript
- Lua
- Python
- R
- Rust
- Swift

DLP also supports confidence level for [source code profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code).

For more details, refer to [DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/).

Jan 15, 2025

[<h2>Export SSH command logs with Access for Infrastructure using Logpush</h2>](https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Availability

Only available on Enterprise plans.

Cloudflare now allows you to send SSH command logs to storage destinations configured in [Logpush](https://developers.cloudflare.com/logs/logpush/), including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the [SSH logs dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/).

To set up a Logpush job, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

Jan 15, 2025

[<h2>Increased Workflows limits and improved instance queueing.</h2>](https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) (beta) now allows you to define up to 1024 [steps](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstep). `sleep` steps do not count against this limit.

We've also added:

- `instanceId` as property to the [`WorkflowEvent`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowevent) type, allowing you to retrieve the current instance ID from within a running Workflow instance
- Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.
- Support for [`pause` and `resume`](https://developers.cloudflare.com/workflows/build/workers-api/#pause) for Workflow instances in a queued state.

We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new `waitForEvent` API over the coming weeks.

Jan 13, 2025

[<h2>WAF Release - 2025-01-13</h2>](https://developers.cloudflare.com/changelog/post/2025-01-13-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...f49e5840 | 100704 | Cleo Harmony - Auth Bypass - CVE:CVE-2024-55956, CVE:CVE-2024-55953 | Log | Block | New Detection |
| Cloudflare Managed Ruleset | ...a6d43bc2 | 100705 | Sentry - SSRF | Log | Block | New Detection |
| Cloudflare Managed Ruleset | ...ce6311bb | 100706 | Apache Struts - Remote Code Execution - CVE:CVE-2024-53677 | Log | Block | New Detection |
| Cloudflare Managed Ruleset | ...2233da1f | 100707 | FortiWLM - Remote Code Execution - CVE:CVE-2023-48782, CVE:CVE-2023-34993, CVE:CVE-2023-34990 | Log | Block | New Detection |
| Cloudflare Managed Ruleset | ...e31d972a | 100007C\_BETA | Command Injection - Common Attack Commands |  | Disabled | |

Jan 9, 2025

[<h2>New Rules Overview Interface</h2>](https://developers.cloudflare.com/changelog/post/2025-01-09-rules-overview/)

[Rules](https://developers.cloudflare.com/rules/)

**Rules Overview** gives you a single page to manage all your [Cloudflare Rules](https://developers.cloudflare.com/rules/).

What you can do:

- **See all your rules in one place** – No more clicking around.
- **Find rules faster** – Search by name.
- **Understand execution order** – See how rules run in sequence.
- **Debug easily** – Use [Trace](https://developers.cloudflare.com/rules/trace-request/) without switching tabs.

Check it out in [Rules > Overview ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview).

Jan 8, 2025

[<h2>Smart Tiered Cache optimizes Load Balancing Pools</h2>](https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now achieve higher cache hit rates and reduce origin load when using [Load Balancing](https://developers.cloudflare.com/load-balancing/) with [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/). Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.

#### How it works

When you use [Load Balancing](https://developers.cloudflare.com/load-balancing/) with [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/), Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:

- **Consistent cache location**: All origins in the pool share the same Upper Tier cache.
- **Higher HIT rates**: Requests for the same content hit the cache more frequently.
- **Reduced origin requests**: Fewer requests reach your origin servers.
- **Improved performance**: Faster response times for cache HITs.

#### Example workflow

```txt
Load Balancing Pool: api-pool
├── Origin 1: api-1.example.com
├── Origin 2: api-2.example.com
└── Origin 3: api-3.example.com
    ↓
Selected Upper Tier: [Optimal data center based on pool performance]
```

#### Get started

To get started, enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) on your zone and configure your [Load Balancing Pool](https://developers.cloudflare.com/load-balancing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/51/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/51/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
