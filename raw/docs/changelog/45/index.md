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

May 29, 2025

[<h2>50-500ms Faster D1 REST API Requests</h2>](https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/)

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

Users using Cloudflare's [REST API](https://developers.cloudflare.com/api/resources/d1/) to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.

Latency improvements range from 50-500 ms depending on request location and [database location](https://developers.cloudflare.com/d1/configuration/data-location/) and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.

D1 query endpoints like `/query` and `/raw` have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.

May 28, 2025

[<h2>Playwright MCP server is now compatible with Browser Rendering</h2>](https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

We're excited to share that you can now use the [Playwright MCP ↗︎](https://github.com/cloudflare/playwright-mcp) server with Browser Rendering.

Once you [deploy the server](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/#deploying), you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.

![Access Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1420,height=914,format=webp/_astro/playground-ai-screenshot.v44jFMBu.png)

Playwright MCP is available as an npm package at [`@cloudflare/playwright-mcp` ↗︎](https://www.npmjs.com/package/@cloudflare/playwright-mcp). To install it, type:

npmyarnpnpmbun

```
npm i -D @cloudflare/playwright-mcp
```

```
yarn add -D @cloudflare/playwright-mcp
```

```
pnpm add -D @cloudflare/playwright-mcp
```

```
bun add -d @cloudflare/playwright-mcp
```

Deploying the server is then as easy as:

```ts
import { env } from "cloudflare:workers";
import { createMcpAgent } from "@cloudflare/playwright-mcp";

export const PlaywrightMCP = createMcpAgent(env.BROWSER);
export default PlaywrightMCP.mount("/sse");
```

Check out the full code at [GitHub ↗︎](https://github.com/cloudflare/playwright-mcp).

Learn more about Playwright MCP in our [documentation](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/).

May 28, 2025

[<h2>Updated attack score model</h2>](https://developers.cloudflare.com/changelog/post/2025-05-28-updated-attack-score-model/)

[WAF](https://developers.cloudflare.com/waf/)

We have deployed an updated attack score model focused on enhancing the detection of multiple false positives (FPs).

As a result of this improvement, some changes in observed attack scores are expected.

May 27, 2025

[<h2>Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</h2>](https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/)

[SSL/TLS](https://developers.cloudflare.com/ssl/) [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) [Secrets Store](https://developers.cloudflare.com/secrets-store/)

With upgraded limits to [all free and paid plans ↗︎](https://www.cloudflare.com/plans/), you can now scale more easily with [Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and [Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/).

[Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the [limit for custom hostnames ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/) on a Cloudflare for SaaS Pay-as-you-go plan has been **raised from 5,000 custom hostnames to 50,000 custom hostnames.**

With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. [Custom origin server ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/) is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.

You can enable custom origin server on a per-custom hostname basis [via the API ↗︎](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) or the UI:

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1896,height=1636,format=webp/_astro/custom-origin-server.B-BXcG-1.png)

Currently [in beta with a Workers integration ↗︎](https://blog.cloudflare.com/secrets-store-beta/), [Cloudflare Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/) allows you to store, manage, and deploy account level secrets from a secure, centralized platform your [Cloudflare Workers ↗︎](https://developers.cloudflare.com/workers/). Now, you can create and deploy **100 secrets per account**. Try it out [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), with [Wrangler ↗︎](https://developers.cloudflare.com/secrets-store/integrations/workers/), or [via the API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/) today.

May 27, 2025

[<h2>Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</h2>](https://developers.cloudflare.com/changelog/post/2025-05-27-Protocol-Detection-availability/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.

With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.

This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).

May 27, 2025

[<h2>WAF Release - 2025-05-27</h2>](https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.

**Key Findings**

- Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.
- GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.
- Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.
- F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.
- AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.
- NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.
- SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.
- Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.
- Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.

**Impact**

These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.

GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d127592a | 100746 | Vercel - Information Disclosure | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...95442495 | 100754 | AJ-Report - Remote Code Execution - CVE:CVE-2024-15077 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...dfee7ae4 | 100756 | NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...1c52f6d0 | 100757 | Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...95442495 | 100759 | SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5366ccc1 | 100760 | Craft CMS - Remote Code Execution - CVE:CVE-2025-32432 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...eb40686b | 100761 | GitHub Action - Remote Code Execution - CVE:CVE-2025-30066 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...60fc041c | 100762 | Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...ebafdfe6 | 100763 | F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644 | Log | Disabled | This is a New Detection |

May 23, 2025

[<h2>New GraphQL Analytics API Explorer and MCP Server</h2>](https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/)

[Analytics](https://developers.cloudflare.com/analytics/)

We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:

#### GraphQL API Explorer

The new [GraphQL API Explorer ↗︎](https://graphql.cloudflare.com/explorer) helps you build, test, and run queries directly in your browser. Features include:

- In-browser schema documentation to browse available datasets and fields
- Interactive query editor with autocomplete and inline documentation
- A "Run in GraphQL API Explorer" button to execute example queries from our docs
- Seamless OAuth authentication — no manual setup required

![GraphQL API Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2626,height=974,format=webp/_astro/graphql-api-explorer.CPUNZZ5B.png)

#### GraphQL Model Context Protocol (MCP) Server

MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our [blog post ↗︎](https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/) for details on how they work and which servers are available. The new [GraphQL MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql) helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:

- Explore what data is available to query
- Generate and refine queries using natural language, with one-click links to run them in the API Explorer
- Build dashboards and visualizations from structured query outputs

Example prompts include:

- “Show me HTTP traffic for the last 7 days for example.com”
- “What GraphQL node returns firewall events?”
- “Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”

We’re continuing to expand these tools, and your feedback helps shape what’s next. [Explore the documentation](https://developers.cloudflare.com/analytics/graphql-api/) to learn more and get started.

May 22, 2025

[<h2>Handle incoming request cancellation in Workers with Request.signal</h2>](https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/)

[Workers](https://developers.cloudflare.com/workers/)

In Cloudflare Workers, you can now attach an event listener to [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) objects, using the [`signal` property ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Request/signal). This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the [`enable_request_signal`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests) compatibility flag.

You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:

*index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		// This sets up an event listener that will be called if the client disconnects from your
		// worker.
		request.signal.addEventListener("abort", () => {
			console.log("The request was aborted!");
		});

		const { readable, writable } = new IdentityTransformStream();
		sendPing(writable);
		return new Response(readable, {
			headers: { "Content-Type": "text/plain" },
		});
	},
};

async function sendPing(writable) {
	const writer = writable.getWriter();
	const enc = new TextEncoder();

	for (;;) {
		// Send 'ping' every second to keep the connection alive
		await writer.write(enc.encode("ping\r\n"));
		await scheduler.wait(1000);
	}
}
```

*index.tsts*

```ts
export default {
  async fetch(request, env, ctx): Promise<Response> {
    // This sets up an event listener that will be called if the client disconnects from your
    // worker.
    request.signal.addEventListener('abort', () => {
      console.log('The request was aborted!');
    });

    const { readable, writable } = new IdentityTransformStream();
    sendPing(writable);
    return new Response(readable, { headers: { 'Content-Type': 'text/plain' } });
  },
} satisfies ExportedHandler<Env>;

async function sendPing(writable: WritableStream): Promise<void> {
	const writer = writable.getWriter();
	const enc = new TextEncoder();

	for (;;) {
		// Send 'ping' every second to keep the connection alive
		await writer.write(enc.encode('ping\r\n'));
		await scheduler.wait(1000);
	}
}
```

For more information see the [`Request` documentation](https://developers.cloudflare.com/workers/runtime-apis/request).

May 19, 2025

[<h2>Terraform v5.5.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-05-19-terraform-v5.5.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Broad fixes across resources with recurring diffs, including, but not limited to:
  - `cloudflare_zero_trust_gateway_policy`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_tunnel_cloudflared_route`
  - `cloudflare_zone_setting`
  - `cloudflare_ruleset`
  - `cloudflare_page_rule`
- Zone settings can be re-applied without client errors
- Page rules conversion errors are fixed
- Failure to apply changes to `cloudflare_zero_trust_tunnel_cloudflared_route`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0) in GitHub.

#### Issues Closed

- [#5304: Importing cloudflare\_zero\_trust\_gateway\_policy invalid attribute filter value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare\_page\_rule import does not set values for all of the fields in terraform state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare\_page\_rule Page rule creation with redirect fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare\_turnstile\_wwidget not able to update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare\_cloud\_connector\_rules: Provider returned invalid result object after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare\_zone\_setting: "Invalid value for zone setting always\_use\_https" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

May 19, 2025

[<h2>WAF Release - 2025-05-19</h2>](https://developers.cloudflare.com/changelog/post/2025-05-19-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in *Block* mode.

**Key Findings**

- Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.
- BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.
- Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.
- Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured `mod_proxy` behavior. While not RCE, this is useful for pre-attack recon.

**Impact**

These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.

Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...75129820 | 100745 | Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...26a517f1 | 100747 | Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d7619ccb | 100749 | BentoML - Remote Code Execution - CVE:CVE-2025-27520 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f15bfda4 | 100753 | Craft CMS - Remote Code Execution - CVE:CVE-2024-56145 | Log | Block | This is a New Detection |

May 18, 2025

[<h2>New Applications Added to Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/new-applications-71825/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

42 new applications have been added for Zero Trust support within the Application Library and Gateway policy enforcement, giving you the ability to investigate or apply inline policies to these applications.

33 of the 42 applications are Artificial Intelligence applications. The others are Human Resources (2 applications), Development (2 applications), Productivity (2 applications), Sales & Marketing, Public Cloud, and Security.

To view all available applications, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), navigate to the **App Library** under **My Team**.

For more information on creating Gateway policies, see our [Gateway policy documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

May 16, 2025

[<h2>New Access Analytics in the Cloudflare One Dashboard</h2>](https://developers.cloudflare.com/changelog/post/access-analytics-v2/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

A new Access Analytics dashboard is now available to all Cloudflare One customers. Customers can apply and combine multiple filters to dive into specific slices of their Access metrics. These filters include:

- Logins granted and denied
- Access events by type (SSO, Login, Logout)
- Application name (Salesforce, Jira, Slack, etc.)
- Identity provider (Okta, Google, Microsoft, onetimepin, etc.)
- Users ( `chris@cloudflare.com`, `sally@cloudflare.com`, `rachel@cloudflare.com`, etc.)
- Countries (US, CA, UK, FR, BR, CN, etc.)
- Source IP address
- App type (self-hosted, Infrastructure, RDP, etc.)

![Access Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2030,height=1720,format=webp/_astro/accessanalytics.DYXgwZCl.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and find Analytics in the side navigation bar.

May 16, 2025

[<h2>Durable Objects are now supported in Python Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/)

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

You can now create [Durable Objects](https://developers.cloudflare.com/durable-objects/) using [Python Workers](https://developers.cloudflare.com/workers/languages/python/). A Durable Object is a special kind of Cloudflare Worker which uniquely combines compute with storage, enabling stateful long-running applications which run close to your users. For more info see [here](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/).

You can define a Durable Object in Python in a similar way to JavaScript:

```python
from workers import DurableObject, Response, WorkerEntrypoint

from urllib.parse import urlparse

class MyDurableObject(DurableObject):
    def __init__(self, ctx, env):
        self.ctx = ctx
        self.env = env

    def fetch(self, request):
        result = self.ctx.storage.sql.exec("SELECT 'Hello, World!' as greeting").one()
        return Response(result.greeting)

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = urlparse(request.url)
        id = env.MY_DURABLE_OBJECT.idFromName(url.path)
        stub = env.MY_DURABLE_OBJECT.get(id)
        greeting = await stub.fetch(request.url)
        return greeting
```

Define the Durable Object in your Wrangler configuration file:

```jsonc
{
	"durable_objects": {
		"bindings": [
			{
				"name": "MY_DURABLE_OBJECT",
				"class_name": "MyDurableObject"
			}
		]
	}
}
```

```toml
[[durable_objects.bindings]]
name = "MY_DURABLE_OBJECT"
class_name = "MyDurableObject"
```

Then define the storage backend for your Durable Object:

```jsonc
{
	"migrations": [
		{
			"tag": "v1", // Should be unique for each entry
			"new_sqlite_classes": [ // Array of new classes
				"MyDurableObject"
			]
		}
	]
}
```

```toml
[[migrations]]
tag = "v1"
new_sqlite_classes = [ "MyDurableObject" ]
```

Then test your new Durable Object locally by running `wrangler dev`:

```bash
npx wrangler dev
```

Consult the [Durable Objects documentation](https://developers.cloudflare.com/durable-objects/) for more details.

May 15, 2025

[<h2>Open email attachments with Browser Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open email attachments to view and investigate them.

What this means is that messages now have a **Attachments** section. Here, you can view processed attachments and their classifications (for example, *Malicious*, *Suspicious*, *Encrypted*). Next to each attachment, a **Browser Isolation** icon allows your team to safely open the file in a **clientless, isolated browser** with no risk to the analyst or your environment.

![Attachment-RBI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=517,height=155,format=webp/_astro/Attachment-RBI.U9Dp8dJO.png)

To use this feature, you must:

- Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
- Have **Browser Isolation (BISO)** seats assigned.

For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

May 14, 2025

[<h2>Domain Categories improvements</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-domain-category-improvements/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

**New categories added**

| Parent ID | Parent Name | Category ID | Category Name |
| --- | --- | --- | --- |
| 1 | Ads | 66 | Advertisements |
| 3 | Business & Economy | 185 | Personal Finance |
| 3 | Business & Economy | 186 | Brokerage & Investing |
| 21 | Security Threats | 187 | Compromised Domain |
| 21 | Security Threats | 188 | Potentially Unwanted Software |
| 6 | Education | 189 | Reference |
| 9 | Government & Politics | 190 | Charity and Non-profit |

**Changes to existing categories**

| Original Name | New Name |
| --- | --- |
| Religion | Religion & Spirituality |
| Government | Government/Legal |
| Redirect | URL Alias/Redirect |

Refer to [Gateway domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/) to learn more.

May 14, 2025

[<h2>Hyperdrive achieves FedRAMP Moderate-Impact Authorization</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-hyperdrive-fedramp/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive has been approved for FedRAMP Authorization and is now available in the [FedRAMP Marketplace ↗︎](https://marketplace.fedramp.gov/products/FR2000863987).

FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update, Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.

For detailed information regarding FedRAMP and its implications, please refer to the [official FedRAMP documentation for Cloudflare ↗︎](https://marketplace.fedramp.gov/products/FR2000863987).

May 14, 2025

[<h2>Introducing Origin Restrictions for Media Transformations</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/)

[Stream](https://developers.cloudflare.com/stream/)

We are adding [source origin restrictions](https://developers.cloudflare.com/stream/transform-videos/sources/) to the Media Transformations beta. This allows customers to restrict what sources can be used to fetch images and video for transformations. This feature is the same as --- and uses the same settings as --- [Image Transformations sources](https://developers.cloudflare.com/images/optimization/transformations/sources/).

When transformations is first enabled, the default setting only allows transformations on images and media from the same website or domain being used to make the transformation request. In other words, by default, requests to `example.com/cdn-cgi/media` can only reference originals on `example.com`.

![Enable allowed origins from the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1664,height=872,format=webp/_astro/allowed-origins.4hu5lHws.png)

Adding access to other sources, or allowing any source, [is easy to do](https://developers.cloudflare.com/images/optimization/transformations/sources/) in the **Transformations** tab under **Stream**. Click each domain enabled for Transformations and set its sources list to match the needs of your content. The user making this change will need permission to edit zone settings.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

May 13, 2025

[<h2>SAML HTTP-POST bindings support for RBI</h2>](https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused `405` errors during login and improves compatibility with multi-factor authentication (MFA) flows.

With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to [set up Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/).

May 13, 2025

[<h2>New Applications Added for DNS Filtering</h2>](https://developers.cloudflare.com/changelog/post/2025-05-13-new-applications-added/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now create DNS policies to manage outbound traffic for an expanded list of applications. This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.

With this update, you can:

- Create DNS policies for a wider range of applications
- Manage outbound traffic more effectively
- Improve your organization's security and compliance posture

For more information on creating DNS policies, see our [DNS policy documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/).

May 12, 2025

[<h2>Case Sensitive Custom Word Lists</h2>](https://developers.cloudflare.com/changelog/post/2025-05-12-case-sensitive-cwl/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now configure [custom word lists](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets) to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.

![dlp](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1289,height=910,format=webp/_astro/case-sesitive-cwl.MPuOc_3r.png)

May 9, 2025

[<h2>Publish messages to Queues directly via HTTP</h2>](https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/)

[Queues](https://developers.cloudflare.com/queues/)

You can now publish messages to [Cloudflare Queues](https://developers.cloudflare.com/queues/) directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within [Cloudflare Workers](https://developers.cloudflare.com/workers/). You can already consume from queues via Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/), and now publishing is just as flexible.

Publishing via HTTP requires a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Queues Edit` permissions for authentication. Here's a simple example:

```bash
curl "https://api.cloudflare.com/client/v4/accounts/<account_id>/queues/<queue_id>/messages" \
  -X POST \
  -H 'Authorization: Bearer <api_token>' \
  --data '{ "body": { "greeting": "hello", "timestamp":  "2025-07-24T12:00:00Z"} }'
```

You can also use our [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) for TypeScript, Python, and Go.

To get started with HTTP publishing, check out our [step-by-step example](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/) and the full API documentation in our [API reference](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push/).

May 9, 2025

[<h2>More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</h2>](https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/)

[Rules](https://developers.cloudflare.com/rules/)

You can now use IP, Autonomous System (AS), and Hostname [custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) to route traffic to [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/), giving you greater precision and control over how you match and process requests at the edge.

In Snippets, you can now also match on [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/), unlocking smarter edge logic for everything from request filtering and mitigation to [tarpitting](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/) and logging.

**What’s new:**

- [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or [Lists API](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/list/). Great for shared logic across zones.
- [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.

![New fields in Snippets](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1383,height=1351,format=webp/_astro/snippets-lists-scores.D05l6zgc.png)

These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.

Learn more in the [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.

May 8, 2025

[<h2>Open email links with Browser Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open links in emails to view and investigate them.

![Open links with Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=558,height=204,format=webp/_astro/investigate-links.pYbpGkt5.jpg)

From **Investigation**, go to **View details**, and look for the **Links identified** section. Next to each link, the Cloudflare dashboard will display an **Open in Browser Isolation** icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links) to learn more about this feature.

To use this feature, you must:

- Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
- Have **Browser Isolation (RBI)** seats assigned.

For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

May 8, 2025

[<h2>URL Scanner now supports geo-specific scanning</h2>](https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/)

[Security Center](https://developers.cloudflare.com/security-center/)

Enterprise customers can now choose the geographic location from which a URL scan is performed — either via [Security Center](https://developers.cloudflare.com/security-center/investigate/) in the Cloudflare dashboard or via the [URL Scanner API](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create/).

This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.

**What’s new:**

- Location Picker: Select a location for the scan via **Security Center → Investigate** in the dashboard or through the API.
- Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.
- Default behavior: If no location is set, scans default to the user’s current geographic region.

Learn more in the [Security Center documentation](https://developers.cloudflare.com/security-center/).

May 8, 2025

[<h2>Improved Payload Logging for WAF Managed Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/)

[WAF](https://developers.cloudflare.com/waf/)

We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:

- **Targeted logging**: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.
- **Visual highlighting**: Matched content is visually highlighted in the UI for faster identification.
- **Enhanced context**: Logs now include surrounding context to make diagnostics more effective.

![Log entry showing payload logging details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=751,format=webp/_astro/2025-05-payload-logging-update.1M29LjNm.png)

Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can [get started](https://developers.cloudflare.com/waf/managed-rules/payload-logging/).

**Note:** The structure of the `encrypted_matched_data` field in Logpush has changed from `Map<Field, Value>` to `Map<Field, {Before: bytes, Content: Value, After: bytes}>`. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/45/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/45/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
