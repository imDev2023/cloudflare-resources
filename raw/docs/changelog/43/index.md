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

Jul 3, 2025

[<h2>Hyperdrive now supports configuring the amount of database connections</h2>](https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.

All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the [Hyperdrive limits of your Workers plan](https://developers.cloudflare.com/hyperdrive/platform/limits/).

This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.

Refer to the [Hyperdrive configuration documentation](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/) for more information.

Jul 1, 2025

[<h2>Access RDP securely from your browser — now in open beta</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-browser-based-rdp-open-beta/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) is now available in open beta for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.

With browser-based RDP, you can:

- **Control how users authenticate to internal RDP resources** with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.
- **Record who is accessing which servers and when** to support regulatory compliance requirements and to gain greater visibility in the event of a security event.
- **Eliminate the need to install and manage software on user devices**. You will only need a web browser.
- **Reduce your attack surface** by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.

![Example of a browsed-based RDP Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2132,height=1814,format=webp/_astro/browser-based-rdp-access-app.BNXce1JL.png)

To get started, see [Connect to RDP in a browser](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/).

Jul 1, 2025

[<h2>Introducing Pay Per Crawl (private beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-pay-per-crawl/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

We are introducing a new feature of [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) — Pay Per Crawl. [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/) enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.

![Pay per crawl](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2926,height=1516,format=webp/_astro/pay-per-crawl.B5bv2nwT.png)

**For Site Owners:**

- Set pricing and select which crawlers to charge for content access
- Manage payments via Stripe
- Monitor analytics on successful content deliveries

**For AI Crawler Owners:**

- Use HTTP headers to request and accept pricing
- Receive clear confirmations on charges for accessed content

Learn more in the [Pay Per Crawl documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/).

Jul 1, 2025

[<h2>AI Crawl Control refresh</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-refresh/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.

- From the new **AI Crawlers** tab: block specific AI crawlers.
- From the new **Metrics** tab: view AI Crawl Control metrics.

![Block AI crawlers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1323,height=798,format=webp/_astro/manage-ai-crawlers.6UgS8dSG.png) ![Analyze AI crawler activity](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=834,format=webp/_astro/analyze-metrics.C52pJZVg.png)

To get started, explore:

- [Manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/).
- [Analyze AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/).

Jul 1, 2025

[<h2>Bot & Crawler Insights in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-radar-bots-insights/)

[Radar](https://developers.cloudflare.com/radar/)

#### Web crawlers insights

[**Radar**](https://developers.cloudflare.com/radar/) now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.

We have introduced the following endpoints:

- [`/bots/crawlers/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/): Returns an overview of crawler HTTP request distributions across key dimensions.
- [`/bots/crawlers/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/): Provides time-series data on crawler request distributions across the same dimensions.

These endpoints allow analysis across the following dimensions:

- `user_agent`: Parsed data from the `User-Agent` header.
- `referer`: Parsed data from the `Referer` header.
- `crawl_refer_ratio`: Ratio of HTML page crawl requests to HTML page referrals by platform.

#### Broader bot insights

In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:

- [`/bots/`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/): Lists all bots.
- [`/bots/{bot_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get/): Returns detailed metadata for a specific bot.
- [`/bots/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries/): Time-series data for bot activity.
- [`/bots/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/summary/): Returns an overview of bot HTTP request distributions across key dimensions.
- [`/bots/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries_groups/): Provides time-series data on bot request distributions across the same dimensions.

These endpoints support filtering and breakdowns by:

- `bot`: Bot name.
- `bot_operator`: The organization or entity operating the bot.
- `bot_category`: Classification of bot type.

The previously available `verified_bots` endpoints have now been deprecated in favor of this set of bot insights APIs. While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.

Learn more about the new Radar bot and crawler insights in our [blog post ↗︎](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar).

Jul 1, 2025

[<h2>Enhanced support for static assets with the Cloudflare Vite plugin</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/)

[Workers](https://developers.cloudflare.com/workers/)

You can now use any of Vite's [static asset handling ↗︎](https://vite.dev/guide/assets) features in your Worker as well as in your frontend. These include importing assets as URLs, importing as strings and importing from the `public` directory as well as inlining assets.

Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.

Here is an example that fetches an imported asset using the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding) and modifies the response.

```ts
// Import the asset URL
// This returns the resolved path in development and production
import myImage from "./my-image.png";

export default {
	async fetch(request, env) {
		// Fetch the asset using the binding
		const response = await env.ASSETS.fetch(new URL(myImage, request.url));
		// Create a new `Response` object that can be modified
		const modifiedResponse = new Response(response.body, response);
		// Add an additional header
		modifiedResponse.headers.append("my-header", "imported-asset");

		// Return the modified response
		return modifiedResponse;
	},
};
```

Refer to [Static Assets](https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/) in the Cloudflare Vite plugin docs for more info.

Jun 30, 2025

[<h2>Cloudflare One Agent for Android (version 2.4.2)</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Android Cloudflare One Agent is now available in the [Google Play Store ↗︎](https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

- QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
- DNS over HTTPS traffic is now included in the WARP tunnel by default.
- The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).
- Fixed an issue that caused WARP connection failures on ChromeOS devices.

Jun 30, 2025

[<h2>Cloudflare One Agent for iOS (version 1.11)</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

- QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
- DNS over HTTPS traffic is now included in the WARP tunnel by default.
- The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).

Jun 30, 2025

[<h2>Mail authentication requirements for Email Routing</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/)

[Email Service](https://developers.cloudflare.com/email-service/)

The Email Routing platform supports [SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208) records and [DKIM (DomainKeys Identified Mail) ↗︎](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) signatures and honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them, we still forward the emails to upstream mailbox providers.

Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to forward them. We also strongly recommend that all senders implement the DMARC protocol.

If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where the forward action may fail due to missing authentication on the incoming email.

SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking bad emails. If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure you have them properly configured.

Jun 30, 2025

[<h2>Graceful withdrawal of BYOIP prefixes</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/)

[Magic Transit](https://developers.cloudflare.com/magic-transit/)

Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.

AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.

Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to [Advertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/).

Jun 30, 2025

[<h2>Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development</h2>](https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/)

[Workers](https://developers.cloudflare.com/workers/)

We [recently announced ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) our public beta for [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings), which allow you to connect to deployed resources running on your Cloudflare account (like [R2 buckets](https://developers.cloudflare.com/r2) or [D1 databases](https://developers.cloudflare.com/d1)) while running a local development session.

Now, you can use remote bindings with your Next.js applications through the [`@opennextjs/cloudflare` adaptor ↗︎](https://opennext.js.org/cloudflare/bindings#remote-bindings) by enabling the experimental feature in your `next.config.ts`:

```diff
- initOpenNextCloudflareForDev();
+ initOpenNextCloudflareForDev({
+  experimental: { remoteBindings: true }
+ });
```

Then, all you have to do is specify which bindings you want connected to the deployed resource on your Cloudflare account via the `experimental_remote` flag in your binding definition:

```jsonc
{
	"r2_buckets": [
		{
			"bucket_name": "testing-bucket",
			"binding": "MY_BUCKET",
			"experimental_remote": true,
		},
	],
}
```

```toml
[[r2_buckets]]
bucket_name = "testing-bucket"
binding = "MY_BUCKET"
experimental_remote = true
```

You can then run `next dev` to start a local development session (or start a preview with `opennextjs-cloudflare preview`), and all requests to `env.MY_BUCKET` will be proxied to the remote `testing-bucket` — rather than the [default local binding simulations](https://developers.cloudflare.com/workers/local-development/#bindings-during-local-development).

#### Remote bindings & ISR

Remote bindings are also used during the build process, which comes with significant benefits for pages using [Incremental Static Regeneration (ISR) ↗︎](https://opennext.js.org/aws/inner_workings/components/server/node#isrssg). During the build step for an ISR page, your server executes the page's code just as it would for normal user requests. If a page needs data to display (like fetching user info from [KV](https://developers.cloudflare.com/kv)), those requests are actually made. The server then uses this fetched data to render the final HTML.

Data fetching is a critical part of this process, as the finished HTML is only as good as the data it was built with. If the build process can't fetch real data, you end up with a pre-rendered page that's empty or incomplete.

**With remote bindings support in OpenNext,** your pre-rendered pages are built with real data from the start. The build process uses any configured remote bindings, and any data fetching occurs against the deployed resources on your Cloudflare account.

**Want to learn more?** Get started with [remote bindings and OpenNext ↗︎](https://opennext.js.org/cloudflare/bindings#remote-bindings).

**Have feedback?** Join the discussion in our [beta announcement ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) to share feedback or report any issues.

Jun 26, 2025

[<h2>Run and connect Workers in separate dev commands with the Cloudflare Vite plugin</h2>](https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/)

[Workers](https://developers.cloudflare.com/workers/)

Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with `vite dev` or `wrangler dev`.

Simply start each Worker in its own terminal:

```sh
# Terminal 1
vite dev

# Terminal 2
wrangler dev
```

This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.

Jun 25, 2025

[<h2>Run AI-generated code on-demand with Code Sandboxes (new)</h2>](https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing [Sandboxes ↗︎](https://www.npmjs.com/package/@cloudflare/sandbox), which let your Worker run actual processes in a secure, container-based environment.

```ts
import { getSandbox } from "@cloudflare/sandbox";
export { Sandbox } from "@cloudflare/sandbox";

export default {
	async fetch(request: Request, env: Env) {
		const sandbox = getSandbox(env.Sandbox, "my-sandbox");
		return sandbox.exec("ls", ["-la"]);
	},
};
```

#### Methods

- `exec(command: string, args: string[], options?: { stream?: boolean })`:Execute a command in the sandbox.
- `gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })`: Checkout a git repository in the sandbox.
- `mkdir(path: string, options: { recursive?: boolean; stream?: boolean })`: Create a directory in the sandbox.
- `writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })`: Write content to a file in the sandbox.
- `readFile(path: string, options: { encoding?: string; stream?: boolean })`: Read content from a file in the sandbox.
- `deleteFile(path: string, options?: { stream?: boolean })`: Delete a file from the sandbox.
- `renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })`: Rename a file in the sandbox.
- `moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })`: Move a file from one location to another in the sandbox.
- `ping()`: Ping the sandbox.

Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

You can try it today from your Worker, with just a few lines of code. Let us know what you build.

Jun 25, 2025

[<h2>@cloudflare/actors library - SDK for Durable Objects in beta</h2>](https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

The new [@cloudflare/actors ↗︎](https://www.npmjs.com/package/@cloudflare/actors) library is now in beta!

The `@cloudflare/actors` library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, `@cloudflare/actors` will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.

The name "actors" originates from the [actor programming model](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/#actor-programming-model), which closely ties to how Durable Objects are modelled.

The `@cloudflare/actors` library includes:

- Storage helpers for querying embeddeded, per-object SQLite storage
- Storage helpers for managing SQL schema migrations
- Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression
- `Actor` class for using Durable Objects with a defined pattern
- Durable Objects [Workers API ↗︎](https://developers.cloudflare.com/durable-objects/api/base/) is always available for your application as needed

Storage and alarm helper methods can be combined with [any Javascript class ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class) that defines your Durable Object, i.e, ones that extend `DurableObject` including the `Actor` class.

```js
import { Storage } from "@cloudflare/actors/storage";

export class ChatRoom extends DurableObject<Env> {
    storage: Storage;

    constructor(ctx: DurableObjectState, env: Env) {
        super(ctx, env)
        this.storage = new Storage(ctx.storage);
        this.storage.migrations = [{
            idMonotonicInc: 1,
            description: "Create users table",
            sql: "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)"
        }]
    }
    async fetch(request: Request): Promise<Response> {
        // Run migrations before executing SQL query
        await this.storage.runMigrations();

        // Query with SQL template
        let userId = new URL(request.url).searchParams.get("userId");
        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`
        return new Response(`${JSON.stringify(query)}`);
    }
}
```

`@cloudflare/actors` library introduces the `Actor` class pattern. `Actor` lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named "default".

```js
export class MyActor extends Actor<Env> {
    async fetch(request: Request): Promise<Response> {
        return new Response('Hello, World!')
    }
}

export default handler(MyActor);
```

You can [route](https://developers.cloudflare.com/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object) to different Durable Objects by name within your `Actor` class using [`nameFromRequest` ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name).

```js
export class MyActor extends Actor<Env> {
    static nameFromRequest(request: Request): string {
        let url = new URL(request.url);
        return url.searchParams.get("userId") ?? "foo";
    }

    async fetch(request: Request): Promise<Response> {
        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);
    }
}

export default handler(MyActor);
```

For more examples, check out the library [README ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started). `@cloudflare/actors` library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our [Discord channel ↗︎](https://discord.com/channels/595317990191398933/773219443911819284).

Jun 23, 2025

[<h2>Data Security Analytics in the Zero Trust dashboard</h2>](https://developers.cloudflare.com/changelog/post/cf1-data-security-analytics-v1/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust now includes **Data security analytics**, providing you with unprecedented visibility into your organization sensitive data.

The new dashboard includes:

- **Sensitive Data Movement Over Time:**
  - See patterns and trends in how sensitive data moves across your environment. This helps understand where data is flowing and identify common paths.
- **Sensitive Data at Rest in SaaS & Cloud:**
  - View an inventory of sensitive data stored within your corporate SaaS applications (for example, Google Drive, Microsoft 365) and cloud accounts (such as AWS S3).
- **DLP Policy Activity:**
  - Identify which of your Data Loss Prevention (DLP) policies are being triggered most often.
  - See which specific users are responsible for triggering DLP policies.

![Data Security Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3254,height=1580,format=webp/_astro/cf1-data-security-analytics-v1.BGl6fYXl.png)

To access the new dashboard, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Insights** on the sidebar.

Jun 23, 2025

[<h2>Cloudflare User Groups & SCIM User Groups are now in GA</h2>](https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're announcing the GA of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups**, strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.

**What's New**

**User Groups \[GA]**: [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups \[GA]**: Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

**Stability & Scale**: These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are now officially deprecated as of June 2, 2025. SCIM Virtual Groups end-of-life will take effect on December 2, 2025. We strongly recommend migrating to SCIM User Groups to ensure continued support for SCIM synchronization to the Cloudflare Dashboard. If you haven’t used Virtual Groups, no action is required.

For more info:

- [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
- [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

Jun 20, 2025

[<h2>CNI maintenance alerts</h2>](https://developers.cloudflare.com/changelog/post/2025-06-20-cni-maintenance-alerts/)

[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.

For more information, refer to [Monitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/).

Jun 20, 2025

[<h2>Increased blob size limits in Workers Analytics Engine</h2>](https://developers.cloudflare.com/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/)

[Workers](https://developers.cloudflare.com/workers/)

We’ve increased the total allowed size of [`blob`](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker) fields on data points written to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) from **5 KB to 16 KB**.

This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.

You can find full details on limits for queries, filters, payloads, and more [here in the Workers Analytics Engine limits documentation](https://developers.cloudflare.com/analytics/analytics-engine/limits/).

```js
export default {
	async fetch(request, env) {
		env.analyticsDataset.writeDataPoint({
			// The sum of all of the blob's sizes can now be 16 KB
			blobs: [
				// The URL of the request to the Worker
				request.url,
				// Some metadata about your application you'd like to store
				JSON.stringify(metadata),
				// The version of your Worker this datapoint was collected from
				env.versionMetadata.tag,
			],
			indexes: ["sample-index"],
		});
	},
};
```

*worker.tsts*

```ts
export default {
	async fetch(request, env) {
		env.analyticsDataset.writeDataPoint({
			// The sum of all of the blob's sizes can now be 16 KB
			blobs: [
				// The URL of the request to the Worker
				request.url,
				// Some metadata about your application you'd like to store
				JSON.stringify(metadata),
				// The version of your Worker this datapoint was collected from
				env.versionMetadata.tag,
			],
			indexes: ["sample-index"],
		});
	}
};
```

Jun 19, 2025

[<h2>View custom metadata in responses and guide AI-search with context in AutoRAG</h2>](https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-custom-metadata-and-context/)

[AI Search](https://developers.cloudflare.com/ai-search/)

In [AutoRAG](https://developers.cloudflare.com/ai-search/), you can now view your object's custom metadata in the response from [`/search`](https://developers.cloudflare.com/ai-search/api/search/workers-binding/) and [`/ai-search`](https://developers.cloudflare.com/ai-search/api/search/workers-binding/), and optionally add a `context` field in the custom metadata of an object to provide additional guidance for AI-generated answers.

You can add [custom metadata](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/#r2putoptions) to an object when uploading it to your R2 bucket.

#### Object's custom metadata in search responses

When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside `attributes` then `file` , and can be used for downstream processing.

For example, the `attributes` section of your search response may look like:

```json
{
	"attributes": {
		"timestamp": 1750001460000,
		"folder": "docs/",
		"filename": "launch-checklist.md",
		"file": {
			"url": "https://wiki.company.com/docs/launch-checklist",
			"context": "A checklist for internal launch readiness, including legal, engineering, and marketing steps."
		}
	}
}
```

#### Add a `context` field to guide LLM answers

When you include a custom metadata field named `context`, AutoRAG attaches that value to each chunk of the file. When you run an `/ai-search` query, this `context` is passed to the LLM and can be used as additional input when generating an answer.

We recommend using the `context` field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the `context` string.

For example:

```json
{
	"context": "summary: 'Checklist for internal product launch readiness, including legal, engineering, and marketing steps.'; url: 'https://wiki.company.com/docs/launch-checklist'"
}
```

This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.

Learn more in AutoRAG's [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

Jun 19, 2025

[<h2>Filter your AutoRAG search by file name</h2>](https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/)

[AI Search](https://developers.cloudflare.com/ai-search/)

In [AutoRAG](https://developers.cloudflare.com/ai-search/), you can now [filter](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) by an object's file name using the `filename` attribute, giving you more control over which files are searched for a given query.

This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.

For example, your search query may look like:

```js
const response = await env.AI.autorag("my-autorag").search({
	query: "what is the project deadline?",
	filters: {
		type: "eq",
		key: "filename",
		value: "project-alpha-roadmap.md",
	},
});
```

This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.

Learn more in AutoRAG's [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

Jun 19, 2025

[<h2>Account-level DNS analytics now available via GraphQL Analytics API</h2>](https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/)

[DNS](https://developers.cloudflare.com/dns/)

Authoritative DNS analytics are now available on the **account level** via the [Cloudflare GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

This allows users to query DNS analytics across multiple zones in their account, by using the `accounts` filter.

Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an `NXDOMAIN` response over a given time frame. Please replace `a30f822fcd7c401984bf85d8f2a5111c` with your actual account ID.

*GraphQL example for account-level DNS analyticsgraphql*

```graphql
query GetLatestNXDOMAINResponses {
	viewer {
		accounts(filter: { accountTag: "a30f822fcd7c401984bf85d8f2a5111c" }) {
			dnsAnalyticsAdaptive(
				filter: {
					date_geq: "2025-06-16"
					date_leq: "2025-06-18"
					responseCode: "NXDOMAIN"
				}
				limit: 10000
				orderBy: [datetime_DESC]
			) {
				zoneTag
				queryName
				responseCode
				queryType
				datetime
			}
		}
	}
}
```

To learn more and get started, refer to the [DNS Analytics documentation](https://developers.cloudflare.com/dns/additional-options/analytics/#analytics).

Jun 19, 2025

[<h2>Automate Worker deployments with a simplified SDK and more reliable Terraform provider</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/)

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/) [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

#### Simplified Worker Deployments with our SDKs

We've simplified the programmatic deployment of Workers via our [Cloudflare SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/). This update abstracts away the low-level complexities of the `multipart/form-data` upload process, allowing you to focus on your code while we handle the deployment mechanics.

This new interface is available in:

- [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (4.4.1)
- [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (4.3.1)

For complete examples, see our guide on [programmatic Worker deployments](https://developers.cloudflare.com/workers/platform/infrastructure-as-code).

#### The Old way: Manual API calls

Previously, deploying a Worker programmatically required manually constructing a `multipart/form-data` HTTP request, packaging your code and a separate `metadata.json` file. This was more complicated and verbose, and prone to formatting errors.

For example, here's how you would upload a Worker script previously with cURL:

```bash
curl https://api.cloudflare.com/client/v4/accounts/<account_id>/workers/scripts/my-hello-world-script \
  -X PUT \
  -H 'Authorization: Bearer <api_token>' \
  -F 'metadata={
        "main_module": "my-hello-world-script.mjs",
        "bindings": [
          {
            "type": "plain_text",
            "name": "MESSAGE",
            "text": "Hello World!"
          }
        ],
        "compatibility_date": "$today"
      };type=application/json' \
  -F 'my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module' <<EOF
export default {
  async fetch(request, env, ctx) {
    return new Response(env.MESSAGE, { status: 200 });
  }
};
EOF
```

#### After: SDK interface

With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.

This approach allows you to specify metadata like `main_module`, `bindings`, and `compatibility_date` as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.

Here's how you can now programmatically deploy a Worker via the [`cloudflare-typescript` SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript)

```js
import Cloudflare from "cloudflare";
import { toFile } from "cloudflare/index";

// ... client setup, script content, etc.

const script = await client.workers.scripts.update(scriptName, {
	account_id: accountID,
	metadata: {
		main_module: scriptFileName,
		bindings: [],
	},
	files: {
		[scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
			type: "application/javascript+module",
		}),
	},
});
```

```ts
import Cloudflare from 'cloudflare';
import { toFile } from 'cloudflare/index';

// ... client setup, script content, etc.

const script = await client.workers.scripts.update(scriptName, {
  account_id: accountID,
  metadata: {
    main_module: scriptFileName,
    bindings: [],
  },
  files: {
    [scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
      type: 'application/javascript+module',
    }),
  },
});
```

View the complete example here: [https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts ↗︎](https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts)

#### Terraform provider improvements

We've also made several fixes and enhancements to the [Cloudflare Terraform provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare):

- Fixed the [`cloudflare_workers_script` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) resource in Terraform, which previously was producing a diff even when there were no changes. Now, your `terraform plan` outputs will be cleaner and more reliable.
- Fixed the [`cloudflare_workers_for_platforms_dispatch_namespace` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace), where the provider would attempt to recreate the namespace on a `terraform apply`. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.
- The [`cloudflare_workers_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route) resource now allows for the `script` property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes [docs](https://developers.cloudflare.com/workers/configuration/routing/routes)). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.
- Using `primary_location_hint` in the [`cloudflare_d1_database` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database) resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.

#### API improvements

We've also properly documented the [Workers Script And Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings) in our public OpenAPI spec and SDKs.

Jun 18, 2025

[<h2>Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) will now evaluate [Network (Layer 4) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) **before** [HTTP (Layer 7) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.

This change will roll out progressively between **July 14–18, 2025**. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.

#### Updated order of enforcement

**Previous order:**

1. DNS policies
2. HTTP policies
3. Network policies

**New order:**

1. DNS policies
2. **Network policies**
3. **HTTP policies**

#### Action required: Review your Gateway HTTP policies

This change may affect block notifications. For example:

- You have an **HTTP policy** to block `example.com` and display a block page.
- You also have a **Network policy** to block `example.com` silently (no client notification).

With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.

To ensure users still receive a block notification, you can:

- Add a client notification to your Network policy, or
- Use only the HTTP policy for that domain.

---

#### Why we’re making this change

This update is based on user feedback and aims to:

- Create a more intuitive model by evaluating network-level policies before application-level policies.
- Minimize [526 connection errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context) by verifying the network path to an origin before attempting to establish a decrypted TLS connection.

---

To learn more, visit the [Gateway order of enforcement documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/).

Jun 18, 2025

[<h2>Log Explorer is GA</h2>](https://developers.cloudflare.com/changelog/post/2025-06-18-log-explorer-ga/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) is now GA, providing native observability and forensics for traffic flowing through Cloudflare.

Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.

![Log Explorer dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=208,format=webp/_astro/log-explorer-dash.CJSVLZ7Y.png)

With Log Explorer, you can now:

- **Monitor security and performance issues with custom dashboards** – use natural language to define charts for measuring response time, error rates, top statistics and more.
- **Investigate and troubleshoot issues with Log Search** – use data type-aware search filters or custom sql to investigate detailed logs.
- **Save time and collaborate with saved queries** – save Log Search queries for repeated use or sharing with other users in your account.
- **Access Log Explorer at the account and zone level** – easily find Log Explorer at the account and zone level for querying any dataset.

For help getting started, refer to [our documentation](https://developers.cloudflare.com/log-explorer/).

Jun 18, 2025

[<h2>Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development</h2>](https://developers.cloudflare.com/changelog/post/2025-06-18-remote-bindings-beta/)

[Workers](https://developers.cloudflare.com/workers/)

Today [we announced the public beta ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) of [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development. With remote bindings, you can now connect to deployed resources like [R2 buckets](https://developers.cloudflare.com/r2/) and [D1 databases](https://developers.cloudflare.com/d1/) while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.

#### Example configuration

To enable remote mode, add `"experimental_remote" : true` to each binding that you want to rely on a remote resource running on Cloudflare:

```jsonc
{
	"name": "my-worker",
	// Set this to today's date
	"compatibility_date": "2026-10-05",

	"r2_buckets": [
		{
			"bucket_name": "screenshots-bucket",
			"binding": "screenshots_bucket",
			"experimental_remote": true,
		},
	],
}
```

```toml
name = "my-worker"
# Set this to today's date
compatibility_date = "2026-10-05"

[[r2_buckets]]
bucket_name = "screenshots-bucket"
binding = "screenshots_bucket"
experimental_remote = true
```

When remote bindings are configured, your Worker **still executes locally**, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.

**You can try out remote bindings for local development today with:**

- [Wrangler v4.20.3](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Use the `wrangler dev --x-remote-bindings` command.
- The [Cloudflare Vite Plugin](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Refer to the documentation for how to enable in your Vite config.
- The [Cloudflare Vitest Plugin](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Refer to the documentation for how to enable in your Vitest config.

**Have feedback?** Join the discussion in our [beta announcement ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) to share feedback or report any issues.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/43/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/43/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
