---
title: Developer platform Changelog
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

Jan 2, 2025

[<h2>AI Gateway adds DeepSeek as a Provider</h2>](https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

[**AI Gateway**](https://developers.cloudflare.com/ai-gateway/) now supports [**DeepSeek**](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/), including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or [Workers AI](https://developers.cloudflare.com/workers-ai/), AI Gateway empowers you to:

- **Monitor**: Gain actionable insights with analytics and logs.
- **Control**: Implement caching, rate limiting, and fallbacks.
- **Optimize**: Improve performance with feedback and evaluations.

![AI Gateway adds DeepSeek as a provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=131,format=webp/_astro/deepseek.hirkr3rv.png)

To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:

*Example fetch requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
 --data '{
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

For detailed setup instructions, see our [DeepSeek provider documentation](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/).

Dec 29, 2024

[<h2>Faster Workers Builds with Build Caching and Watch Paths</h2>](https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/)

[Workers](https://developers.cloudflare.com/workers/)

![Build caching settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1494,height=140,format=webp/_astro/workers-build-caching.DWEh3Tj1.png)![Build watch path settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1494,height=190,format=webp/_astro/workers-build-watch-paths.ClqD-iNq.png)

[**Workers Builds**](https://developers.cloudflare.com/workers/ci-cd/builds/), the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.

- **[Build Caching](https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/)**: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.
- **[Build Watch Paths](https://developers.cloudflare.com/workers/ci-cd/builds/build-watch-paths/)**: Define paths to include or exclude from the build process, ideal for [monorepos](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#monorepos) to target only the files that need to be rebuilt per Workers project.

To get started, select your Worker on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) then go to **Settings** > **Builds**, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.

Dec 19, 2024

[<h2>Troubleshoot tunnels with diagnostic logs</h2>](https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

The latest `cloudflared` build [2024.12.2 ↗︎](https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2) introduces the ability to collect all the diagnostic logs needed to troubleshoot a `cloudflared` instance.

A diagnostic report collects data from a single instance of `cloudflared` running on the local machine and outputs it to a `cloudflared-diag` file.

For more information, refer to [Diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

Dec 11, 2024

[<h2>Up to 10x faster cached queries for Hyperdrive</h2>](https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.

When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.

This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.

![Hyperdrive edge caching improves average session duration for database queries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1746,height=734,format=webp/_astro/hyperdrive-edge-caching-metrics.BR7svphB.png)

*P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.*

This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.

For more details on how Hyperdrive performs query caching, refer to the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching).

Nov 11, 2024

[<h2>Bypass caching for subrequests made from Cloudflare Workers, with Request.cache</h2>](https://developers.cloudflare.com/changelog/post/2024-11-11-cache-no-store/)

[Workers](https://developers.cloudflare.com/workers/)

You can now use the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface to bypass [Cloudflare's cache](https://developers.cloudflare.com/workers/reference/how-the-cache-works/) when making subrequests from [Cloudflare Workers](https://developers.cloudflare.com/workers), by setting its value to `no-store`.

*index.jsjs*

```js
export default {
	async fetch(req, env, ctx) {
		const request = new Request("https://cloudflare.com", {
			cache: "no-store",
		});
		const response = await fetch(request);
		return response;
	},
};
```

*index.tsts*

```ts
export default {
  async fetch(req, env, ctx): Promise<Response> {
		const request = new Request("https://cloudflare.com", { cache: 'no-store'});
		const response = await fetch(request);
    return response;
  }
} satisfies ExportedHandler<Environment>
```

When you set the value to `no-store` on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the `Cache-Control` HTTP header that otherwise indicate that the response is cacheable.

This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property, which is a cross-platform standard part of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface. Previously, if you set the `cache` property on `Request`, the Workers runtime threw an exception.

If you've tried to use `@planetscale/database`, `redis-js`, `stytch-node`, `supabase`, `axiom-js` or have seen the error message `The cache field on RequestInitializerDict is not implemented in fetch` — you should try again, making sure that the [Compatibility Date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of your Worker is set to on or after `2024-11-11`, or the [`cache_option_enabled` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api) is enabled for your Worker.

- Learn [how the Cache works with Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
- Enable [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) for your Cloudflare Worker
- Explore [Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) and [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available in Cloudflare Workers

Oct 24, 2024

[<h2>Workflows is now in open beta</h2>](https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/)

[Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

Workflows is now in open beta, and available to any developer a free or paid Workers plan.

Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.

#### Get started

You can get started with Workflows by [following our get started guide](https://developers.cloudflare.com/workflows/get-started/guide/) and/or using `npm create cloudflare` to pull down the starter project:

```sh
npm create cloudflare@latest workflows-starter -- --template "cloudflare/workflows-starter"
```

You can open the `src/index.ts` file, extend it, and use `wrangler deploy` to deploy your first Workflow. From there, you can:

- Learn the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/)
- [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/) via your Workers apps.
- Understand the [Rules of Workflows](https://developers.cloudflare.com/workflows/build/rules-of-workflows/) and how to adopt best practices

Feb 26, 2024

[<h2>Easily Exclude EU Visitors from RUM</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.

![RUM Enablement UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1101,height=1061,format=webp/_astro/2025-02-26-rum-eu.X0ZtbXWA.png)

Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.

To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.

You can learn more about what metrics are reported by Web Analytics and how it is collected [in the Web Analytics documentation](https://developers.cloudflare.com/web-analytics/data-metrics/). You can enable Web Analytics on any hostname by going to the [Web Analytics ↗︎](https://dash.cloudflare.com/?to=/:account/web-analytics/sites) section of the dashboard, selecting "Manage Site" for the hostname you want to monitor, and choosing the appropriate enablement option.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/25/#page","headline":"Developer platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/25/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
