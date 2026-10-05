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

Sep 25, 2025

[<h2>Sign in with GitHub</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-sign-in-with-github/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare has launched sign in with GitHub as a log in option. This feature is available to all users with a verified email address who are not using SSO. To use it, simply click on the `Sign in with GitHub` button on the dashboard login page. You will be logged in with your primary GitHub email address.

#### For more information

- [Log in to Cloudflare](https://developers.cloudflare.com/fundamentals/user-profiles/login/)

Sep 25, 2025

[<h2>SSO for all</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-sso-for-all/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Single sign-on (SSO) streamlines the process of logging into Cloudflare for Enterprise customers who manage a custom email domain and manage their own identity provider. Instead of managing a password and two-factor authentication credentials directly for Cloudflare, SSO lets you reuse your existing login infrastructure to seamlessly log in. SSO also provides additional security opportunities such as device health checks which are not available natively within Cloudflare.

Historically, SSO was only available for Enterprise accounts. Today, we are announcing that we are making SSO available to all users for free. We have also added the ability to directly manage SSO configurations using the API. This removes the previous requirement to contact support to configure SSO.

#### For more information

- [Every Cloudflare feature, available to all ↗︎](https://blog.cloudflare.com/enterprise-grade-features-for-all/)
- [Configure Dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)

Sep 24, 2025

[<h2>WAF Release - 2025-09-24 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-09-24-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week highlights a critical vendor-specific vulnerability: a deserialization flaw in the License Servlet of Fortra’s GoAnywhere MFT. By forging a license response signature, an attacker can trigger deserialization of arbitrary objects, potentially leading to command injection.

**Key Findings**

- GoAnywhere MFT (CVE-2025-10035): Deserialization vulnerability in the License Servlet that allows attackers with a forged license response signature to deserialize arbitrary objects, potentially resulting in command injection.

**Impact**

GoAnywhere MFT (CVE-2025-10035): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...e08b39f3 | 100787 | Fortra GoAnywhere - Auth Bypass - CVE:CVE-2025-10035 | N/A | Block | This is a New Detection |

Sep 23, 2025

[<h2>Invalid Submissions Feedback</h2>](https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.

To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user [submission aliases](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/):

- **Email Notifications:** We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to **[Settings ↗︎](https://one.dash.cloudflare.com/?to=/:account/email-security/settings)** > **Invalid submission emails** and turn the feature off.

![EmailSec-Invalid-Submissions-Toggle](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=175,format=webp/_astro/EmailSec-Invalid-Submissions-Toggle.DXjbR6aX.png)

- **Invalid Submission dashboard:** You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.

![EmailSec-Invalid-Submissions-Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=511,format=webp/_astro/EmailSec-Invalid-Submissions-Dashboard.zuf1on2n.png)

Learn more about this feature on [invalid submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/invalid-submissions/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Sep 23, 2025

[<h2>Improved support for running multiple Workers with \`wrangler dev\`</h2>](https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/)

[Workers](https://developers.cloudflare.com/workers/)

You can run multiple Workers in a single dev command by passing multiple config files to `wrangler dev`:

```sh
wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc
```

Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use [Service Bindings ↗︎](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) and [Tail Workers ↗︎](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) in local development, when running separate wrangler dev sessions.

Now, the following works as expected:

```sh
# Terminal 1: Run your application that includes both Web and API workers
wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc

# Terminal 2: Run your auth worker separately
wrangler dev --config ./auth/wrangler.jsonc
```

These Workers can now communicate with each other across separate dev commands, regardless of your development setup.

*./api/src/index.tsjs*

```js
export default {
	async fetch(request, env) {
		// This service binding call now works across dev commands
		const authorized = await env.AUTH.isAuthorized(request);

		if (!authorized) {
			return new Response("Unauthorized", { status: 401 });
		}

		return new Response("Hello from API Worker!", { status: 200 });
	},
};
```

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.

Sep 22, 2025

[<h2>Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</h2>](https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.

Since we announced our [open beta](https://developers.cloudflare.com/changelog/access/#2025-06-30), we've made a few improvements:

- Support for targets with IPv6.
- Support for [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/) and [WARP Connector](https://developers.cloudflare.com/mesh/) as on-ramps.
- More robust error messaging on the login page to help you if you encounter an issue.
- Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.
- Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.

As a refresher, here are some benefits browser-based RDP provides:

- **Control how users authenticate to internal RDP resources** with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.
- **Record who is accessing which servers and when** to support regulatory compliance requirements and to gain greater visibility in the event of a security event.
- **Eliminate the need to install and manage software on user devices**. You will only need a web browser.
- **Reduce your attack surface** by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.

![Example of a browser-based RDP Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2132,height=1814,format=webp/_astro/browser-based-rdp-access-app.BNXce1JL.png)

To get started, refer to [Connect to RDP in a browser](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/).

Sep 22, 2025

[<h2>WAF Release - 2025-09-22</h2>](https://developers.cloudflare.com/changelog/post/2025-09-22-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week emphasizes two critical vendor-specific vulnerabilities: a full elevation-of-privilege in Microsoft Azure Networking (CVE-2025-54914) and a server-side template injection (SSTI) leading to remote code execution (RCE) in Skyvern (CVE-2025-49619). These are complemented by enhancements in generic detections (SQLi, SSRF) to improve baseline coverage.

**Key Findings**

- Azure (CVE-2025-54914): Vulnerability in Azure Networking allowing elevation of privileges.
- Skyvern (CVE-2025-49619): Skyvern ≤ 0.1.85 has a server-side template injection (SSTI) vulnerability in its Prompt field (workflow blocks) via Jinja2. Authenticated users with low privileges can get remote code execution (blind).
- Generic SQLi / SSRF improvements: Expanded rule coverage to detect obfuscated SQL injection patterns and SSRF across host, local, and cloud contexts.

**Impact**

These vulnerabilities allow attackers to escalate privileges or execute code under conditions where previously they could not:

- Azure CVE-2025-54914 enables an attacker from the network with no credentials to gain high-level access within Azure Networking; could lead to full compromise of networking components.
- Skyvern CVE-2025-49619 allows authenticated users with minimal privilege to exploit SSTI for remote code execution, undermining isolation of workflow components.
- The improvements for SQLi and SSRF reduce risk from common injection and request-based attacks.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...6a135cbf | 100146 | SSRF - Host - 2 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...57035abf | 100146B | SSRF - Local - 2 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...bbe18d50 | 100146C | SSRF - Cloud - 2 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...956c1961 | 100714 | Azure - Auth Bypass - CVE:CVE-2025-54914 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...c5ced231 | 100758 | Skyvern - Remote Code Execution - CVE:CVE-2025-49619 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...84a619a1 | 100773 | Next.js - SSRF | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...983ff2dd | 100774 | Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0380a1a6 | 100800\_BETA | SQLi - Obfuscated Boolean - Beta | Log | Block | This rule has been merged into the original rule (ID: ...5563445f) |

Sep 19, 2025

[<h2>New Metrics View in AutoRAG</h2>](https://developers.cloudflare.com/changelog/post/2025-09-19-autorag-metrics/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AutoRAG](https://developers.cloudflare.com/ai-search/) now includes a **Metrics** tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between `ai-search` and `search`, and see which files are retrieved most often.

![Metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2062,height=1765,format=webp/_astro/metrics.BBUwKIos.png)

You can find these metrics within each AutoRAG instance:

- Indexing: Track how files are ingested and see status changes over time.
- Search breakdown: Compare usage between `ai-search` and `search` endpoints.
- Top file retrievals: Identify which files are most frequently retrieved in a given period.

Try it today in [AutoRAG](https://developers.cloudflare.com/ai-search/get-started/).

Sep 19, 2025

[<h2>Rate Limiting in Workers is now GA</h2>](https://developers.cloudflare.com/changelog/post/2025-09-19-ratelimit-workers-ga/)

[Workers](https://developers.cloudflare.com/workers/)

[Rate Limiting within Cloudflare Workers](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) is now Generally Available (GA).

The `ratelimit` binding is now stable and recommended for all production workloads. Existing deployments using the unsafe binding will continue to function to allow for a smooth transition.

For more details, refer to [Workers Rate Limiting](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) documentation.

Sep 19, 2025

[<h2>Panic Recovery for Rust Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/)

[Workers](https://developers.cloudflare.com/workers/)

In [workers-rs ↗︎](https://github.com/cloudflare/workers-rs), Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.

Now, when a panic occurs, in-flight requests will throw 500 errors, but the Worker will automatically and instantly recover for future requests.

This ensures more reliable deployments. Automatic panic recovery is enabled for all new workers-rs deployments as of version 0.6.5, with no configuration required.

#### Fixing Rust Panics with Wasm Bindgen

Rust Workers are built with Wasm Bindgen, which treats panics as non-recoverable. After a panic, the entire Wasm application is considered to be in an invalid state.

We now attach a default panic handler in Rust:

```rust
std::panic::set_hook(Box::new(move |panic_info| {
  hook_impl(panic_info);
}));
```

Which is registered by default in the JS initialization:

```js
import { setPanicHook } from "./index.js";
setPanicHook(function (err) {
	console.error("Panic handler!", err);
});
```

When a panic occurs, we reset the Wasm state to revert the Wasm application to how it was when the application started.

#### Resetting VM State in Wasm Bindgen

We worked upstream on the Wasm Bindgen project to implement a new [`--experimental-reset-state-function` compilation option ↗︎](https://github.com/wasm-bindgen/wasm-bindgen/pull/4644) which outputs a new `__wbg_reset_state` function.

This function clears all internal state related to the Wasm VM, and updates all function bindings in place to reference the new WebAssembly instance.

One other necessary change here was associating Wasm-created JS objects with an instance identity. If a JS object created by an earlier instance is then passed into a new instance later on, a new "stale object" error is specially thrown when using this feature.

#### Layered Solution

Building on this new Wasm Bindgen feature, layered with our new default panic handler, we also added a proxy wrapper to ensure all top-level exported class instantiations (such as for Rust Durable Objects) are tracked and fully reinitialized when resetting the Wasm instance. This was necessary because the workerd runtime will instantiate exported classes, which would then be associated with the Wasm instance.

This approach now provides full panic recovery for Rust Workers on subsequent requests.

Of course, we never want panics, but when they do happen they are isolated and can be investigated further from the error logs - avoiding broader service disruption.

#### WebAssembly Exception Handling

In the future, full support for recoverable panics could be implemented without needing reinitialization at all, utilizing the [WebAssembly Exception Handling ↗︎](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md) proposal, part of the newly announced [WebAssembly 3.0 ↗︎](https://webassembly.org/news/2025-09-17-wasm-3.0/) specification. This would allow unwinding panics as normal JS errors, and concurrent requests would no longer fail.

**We're making significant improvements to the reliability of [Rust Workers ↗︎](https://github.com/cloudflare/workers-rs). Join us in `#rust-on-workers` on the [Cloudflare Developers Discord ↗︎](https://discord.gg/cloudflaredev) to stay updated.**

Sep 18, 2025

[<h2>Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</h2>](https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

You can now route private traffic to [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is **free for all Cloudflare One customers**.

Previously, Tunnel routes could only be defined by IP address or [CIDR range](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/). This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.

![Hostname-based routing in Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1990,height=530,format=webp/_astro/tunnel-hostname-routing.DSi8MP_7.webp)

**What’s new:**

- **Hostname & Domain Routing**: Create routes for individual hostnames (e.g., `payroll.acme.local`) or entire domains (e.g., `*.acme.local`) and direct their traffic to a specific Tunnel.
- **Simplified Zero Trust Policies**: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.
- **Precise Egress Control**: Route traffic for public hostnames (e.g., `bank.example.com`) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.
- **No More IP Lists**: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.

Get started in the Tunnels section of the Zero Trust dashboard with your first [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) or [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) route.

Learn more in our [blog post ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/).

Sep 18, 2025

[<h2>Increased vCPU for Workers Builds on paid plans</h2>](https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/)

[Workers](https://developers.cloudflare.com/workers/)

We recently [increased the available disk space](https://developers.cloudflare.com/changelog/2025-08-04-builds-increased-disk-size/) from 8 GB to 20 GB for **all** plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to **4 vCPU**.

These changes continue our focus on making [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) faster and more reliable.

| Metric | Free Plan | Paid Plans |
| --- | --- | --- |
| CPU | 2 vCPU | **4 vCPU** |

#### Performance Improvements

- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs
- **2x faster multi-threaded builds**: Tools like [esbuild ↗︎](https://esbuild.github.io/) and [webpack ↗︎](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling

All other [build limits](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) — including memory, build minutes, and timeout remain unchanged.

Sep 17, 2025

[<h2>Preview URLs now default to opt-in</h2>](https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/)

[Workers](https://developers.cloudflare.com/workers/)

To prevent the accidental exposure of applications, we've updated how [Worker preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.

#### One-Time Update for Workers with workers.dev Disabled

We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) was also disabled.

Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.

If your Worker was affected, its preview URL (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) will now direct to an informational page explaining this change.

**How to Re-enable Your Preview URL**

If your preview URL was disabled, you can re-enable it [via the Cloudflare dashboard](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable) by navigating to your Worker's Settings page and toggling on the Preview URL.

Alternatively, you can use Wrangler by adding the `preview_urls = true` setting to your Wrangler file and redeploying the Worker.

```jsonc
{
  "preview_urls": true
}
```

```toml
preview_urls = true
```

**Note:** You can set `preview_urls = true` with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults `preview_urls` to false, ensuring preview URLs are always enabled by explicit choice.

Sep 16, 2025

[<h2>New AI-Enabled Search for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.

![Example search results in the Zero Trust dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1750,height=1568,format=webp/_astro/searchexample.Di8yS8ju.png)

**Ask Cloudy** — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.

Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.

**Find Recents** — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.

Sep 16, 2025

[<h2>DNS Firewall Analytics — now in the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-09-16-DNSFW-Analytics-UI/)

[DNS](https://developers.cloudflare.com/dns/)

#### What's New

Access [GraphQL-powered DNS Firewall analytics](https://developers.cloudflare.com/dns/dns-firewall/analytics/) directly in the Cloudflare dashboard.

![DNS Firewall Analytics UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=284,format=webp/_astro/DNSFW_Analytics_UI.CgjmZFOO.png)

#### Explore Four Interactive Panels

- **Query summary**: Describes trends over time, segmented by dimensions.
- **Query statistics**: Describes totals, cached/uncached queries, and processing/response times.
- **DNS queries by data center**: Describes global view and the top 10 data centers.
- **Top query statistics**: Shows a breakdown by key dimensions, with search and expand options (up to top 100 items).

Additional features:

- Apply filters and time ranges once. Changes reflect across all panels.
- Filter by dimensions like query name, query type, cluster, data center, protocol (UDP/TCP), IP version, response code/reason, and more.
- Access up to 62 days of historical data with flexible intervals.

#### Availability

Available to all DNS Firewall customers as part of their existing subscription.

#### Where to Find It

- In the Cloudflare dashboard, go to the **DNS Firewall** page. [Go to **Analytics** ↗](https://dash.cloudflare.com/?to=/:account/dns-firewall/analytics)
- Refer to the [DNS Firewall Analytics](https://developers.cloudflare.com/dns/dns-firewall/analytics/) to learn more.

Sep 16, 2025

[<h2>Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development</h2>](https://developers.cloudflare.com/changelog/post/2025-09-16-remote-bindings-ga/)

[Workers](https://developers.cloudflare.com/workers/)

Three months ago [we announced the public beta](https://developers.cloudflare.com/changelog/2025-06-18-remote-bindings-beta/) of [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!

With remote bindings, you can now connect to deployed resources like [R2 buckets](https://developers.cloudflare.com/r2/) and [D1 databases](https://developers.cloudflare.com/d1/) while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.

#### Example configuration

To enable remote bindings, add `"remote" : true` to each binding that you want to rely on a remote resource running on Cloudflare:

```jsonc
{
	"name": "my-worker",
	// Set this to today's date
	"compatibility_date": "2026-10-05",

	"r2_buckets": [
		{
			"bucket_name": "screenshots-bucket",
			"binding": "screenshots_bucket",
			"remote": true,
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
remote = true
```

When remote bindings are configured, your Worker **still executes locally**, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.

**You can [try out remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development today with:**

- [Wrangler v4.37.0](https://developers.cloudflare.com/workers/wrangler/)
- The [Cloudflare Vite Plugin](https://developers.cloudflare.com/workers/vite-plugin/)
- The [Cloudflare Vitest Plugin](https://developers.cloudflare.com/workers/testing/vitest-integration/)

Sep 15, 2025

[<h2>WAF Release - 2025-09-15</h2>](https://developers.cloudflare.com/changelog/post/2025-09-15-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week's focus highlights newly disclosed vulnerabilities in DevOps tooling, data visualization platforms, and enterprise CMS solutions. These issues include sensitive information disclosure and remote code execution, putting organizations at risk of credential leakage, unauthorized access, and full system compromise.

**Key Findings**

- Argo CD (CVE-2025-55190): Exposure of sensitive information could allow attackers to access credential data stored in configurations, potentially leading to compromise of Kubernetes workloads and secrets.
- DataEase (CVE-2025-57773): Insufficient input validation enables JNDI injection and insecure deserialization, resulting in remote code execution (RCE). Successful exploitation grants attackers control over the application server.
- Sitecore (CVE-2025-53694): A sensitive information disclosure flaw allows unauthorized access to confidential information stored in Sitecore deployments, raising the risk of data breaches and privilege escalation.

**Impact**

These vulnerabilities expose organizations to serious risks, including credential theft, unauthorized access, and full system compromise. Argo CD's flaw may expose Kubernetes secrets, DataEase exploitation could give attackers remote execution capabilities, and Sitecore's disclosure issue increases the likelihood of sensitive data leakage and business impact.

Administrators are strongly advised to apply vendor patches immediately, rotate exposed credentials, and review access controls to mitigate these risks.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2ee2085f | 100646 | Argo CD - Information Disclosure - CVE:CVE-2025-55190s | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f5e20788 | 100874 | DataEase - JNDI injection - CVE:CVE-2025-57773 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...005a12fd | 100880 | Sitecore - Information Disclosure - CVE:CVE-2025-53694 | Log | Block | This is a New Detection |

Sep 11, 2025

[<h2>Regional Email Processing for Germany, India, or Australia</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: **MX**, **BCC**, and **Journaling**.

#### What’s new

Customers can now select where their email is processed. The following regions are supported:

- **Germany**
- **India**
- **Australia**

Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.

#### How to use it

When onboarding a domain with MX, BCC, or Journaling:

1. Select the desired processing location (Germany, India, or Australia).
2. The UI will display updated processing addresses specific to that region.
3. For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.

#### Availability

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

#### What’s next

We’re expanding the list of processing locations to match our [Data Localization Suite (DLS)](https://developers.cloudflare.com/data-localization/) footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.

Sep 11, 2025

[<h2>D1 automatically retries read-only queries</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/)

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned [response metadata](https://developers.cloudflare.com/d1/worker-api/return-object/#d1result) property `total_attempts`.

At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: `SELECT`, `EXPLAIN`, `WITH`. Queries containing any [SQLite keyword ↗︎](https://sqlite.org/lang_keywords.html) that leads to database writes are not retried.

The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).

The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying [retries in their own code](https://developers.cloudflare.com/d1/best-practices/retry-queries/) for queries that are not read-only but are idempotent according to the business logic of the application.

![D1 automatically query retries success ratio](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=946,format=webp/_astro/d1-auto-retry-success-ratio.yPw8B0tB.png)

D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.

The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.

Sep 11, 2025

[<h2>DNS filtering for private network onramps</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

[Magic WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering) and [WARP Connector](https://developers.cloudflare.com/mesh/features/routes/#dns-filtering) users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.

Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including [Internal DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#internal-dns) and [hostname-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites).

To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, `172.64.36.1` and `172.64.36.2`. Once you configure DNS resolution and filtering, you can use *Source Internal IP* as a traffic selector in your [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) for routing private DNS traffic to your [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/).

Sep 11, 2025

[<h2>Contextual pivots</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Directly from [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.

From the `http_requests` or `fw_events` dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.

![Investigate IP address](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1038,height=486,format=webp/_astro/investigate-ip-address.BMVSMzDi.png)

Easily learn about error codes by linking directly to our documentation from the **EdgeResponseStatus** or **OriginResponseStatus** fields.

![View documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1186,height=476,format=webp/_astro/view-documentation.Cem5QgeO.png)

From the `gateway_http` dataset, click on a **policyid** to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.

![View policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1274,height=498,format=webp/_astro/policyid.CVjEdahj.png)

Sep 11, 2025

[<h2>New results table view</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-new-results-table-view/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

The results table view of **Log Search** has been updated with additional functionality and a more streamlined user experience. Users can now easily:

- Remove/add columns.
- Resize columns.
- Sort columns.
- Copy values from any field.

![New results table view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1786,height=342,format=webp/_astro/new-table.C2Q8mWJ9.png)

Sep 11, 2025

[<h2>Worker version rollback limit increased from 10 to 100</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/)

[Workers](https://developers.cloudflare.com/workers/)

The number of recent versions available for a Worker rollback has been increased from 10 to 100.

This allows you to:

- Promote any of the 100 most recent versions to be the active deployment.
- Split traffic using [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/) between your latest code and any of the 100 most recent versions.

You can do this through the Cloudflare dashboard or with [Wrangler's rollback command](https://developers.cloudflare.com/workers/wrangler/commands/general/#rollback)

Learn more about [versioned deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) and [rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/).

Sep 10, 2025

[<h2>Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</h2>](https://developers.cloudflare.com/changelog/post/2025-09-03-agents-sdk-beta-v5/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

We've shipped a new release for the [Agents SDK ↗︎](https://github.com/cloudflare/agents) bringing full compatibility with [AI SDK v5 ↗︎](https://ai-sdk.dev/docs/introduction) and introducing automatic message migration that handles all legacy formats transparently.

This release includes improved streaming and tool support, tool confirmation detection (for "human in the loop" systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.

This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.

Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.

#### useAgentChat(options)

Creates a new chat interface with enhanced v5 capabilities.

```ts
// Basic chat setup
const { messages, sendMessage, addToolResult } = useAgentChat({
	agent,
	experimental_automaticToolResolution: true,
	tools,
});

// With custom tool confirmation
const chat = useAgentChat({
	agent,
	experimental_automaticToolResolution: true,
	toolsRequiringConfirmation: ["dangerousOperation"],
});
```

#### Automatic Tool Resolution

Tools are automatically categorized based on their configuration:

```ts
const tools = {
	// Auto-executes (has execute function)
	getLocalTime: {
		description: "Get current local time",
		inputSchema: z.object({}),
		execute: async () => new Date().toLocaleString(),
	},

	// Requires confirmation (no execute function)
	deleteFile: {
		description: "Delete a file from the system",
		inputSchema: z.object({
			filename: z.string(),
		}),
	},

	// Server-executed (no client confirmation)
	analyzeData: {
		description: "Analyze dataset on server",
		inputSchema: z.object({ data: z.array(z.number()) }),
		serverExecuted: true,
	},
} satisfies Record<string, AITool>;
```

#### Message Handling

Send messages using the new v5 format with parts array:

```ts
// Text message
sendMessage({
	role: "user",
	parts: [{ type: "text", text: "Hello, assistant!" }],
});

// Multi-part message with file
sendMessage({
	role: "user",
	parts: [
		{ type: "text", text: "Analyze this image:" },
		{ type: "image", image: imageData },
	],
});
```

#### Tool Confirmation Detection

Simplified logic for detecting pending tool confirmations:

```ts
const pendingToolCallConfirmation = messages.some((m) =>
	m.parts?.some(
		(part) => isToolUIPart(part) && part.state === "input-available",
	),
);

// Handle tool confirmation
if (pendingToolCallConfirmation) {
	await addToolResult({
		toolCallId: part.toolCallId,
		tool: getToolName(part),
		output: "User approved the action",
	});
}
```

#### Automatic Message Migration

Seamlessly handle legacy message formats without code changes.

```ts
// All these formats are automatically converted:

// Legacy v4 string content
const legacyMessage = {
	role: "user",
	content: "Hello world",
};

// Legacy v4 with tool calls
const legacyWithTools = {
	role: "assistant",
	content: "",
	toolInvocations: [
		{
			toolCallId: "123",
			toolName: "weather",
			args: { city: "SF" },
			state: "result",
			result: "Sunny, 72°F",
		},
	],
};

// Automatically becomes v5 format:
// {
//   role: "assistant",
//   parts: [{
//     type: "tool-call",
//     toolCallId: "123",
//     toolName: "weather",
//     args: { city: "SF" },
//     state: "result",
//     result: "Sunny, 72°F"
//   }]
// }
```

#### Tool Definition Updates

Migrate tool definitions to use the new `inputSchema` property.

```ts
// Before (AI SDK v4)
const tools = {
	weather: {
		description: "Get weather information",
		parameters: z.object({
			city: z.string(),
		}),
		execute: async (args) => {
			return await getWeather(args.city);
		},
	},
};

// After (AI SDK v5)
const tools = {
	weather: {
		description: "Get weather information",
		inputSchema: z.object({
			city: z.string(),
		}),
		execute: async (args) => {
			return await getWeather(args.city);
		},
	},
};
```

#### Cloudflare Workers AI Integration

Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.

#### Model Setup with Workers AI

Use Cloudflare Workers AI models directly in your agent workflows:

```ts
import { createWorkersAI } from "workers-ai-provider";
import { useAgentChat } from "agents/ai-react";

// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)
const model = createWorkersAI({
	binding: env.AI,
})("@cf/meta/llama-3.2-3b-instruct");
```

#### Enhanced File and Image Support

Workers AI models now support v5 file handling with automatic conversion:

```ts
// Send images and files to Workers AI models
sendMessage({
	role: "user",
	parts: [
		{ type: "text", text: "Analyze this image:" },
		{
			type: "file",
			data: imageBuffer,
			mediaType: "image/jpeg",
		},
	],
});

// Workers AI provider automatically converts to proper format
```

#### Streaming with Workers AI

Enhanced streaming support with automatic warning detection:

```ts
// Streaming with Workers AI models
const result = await streamText({
	model: createWorkersAI({ binding: env.AI })("@cf/meta/llama-3.2-3b-instruct"),
	messages,
	onChunk: (chunk) => {
		// Enhanced streaming with warning handling
		console.log(chunk);
	},
});
```

#### Import Updates

Update your imports to use the new v5 types:

```ts
// Before (AI SDK v4)
import type { Message } from "ai";
import { useChat } from "ai/react";

// After (AI SDK v5)
import type { UIMessage } from "ai";
// or alias for compatibility
import type { UIMessage as Message } from "ai";
import { useChat } from "@ai-sdk/react";
```

#### Resources

- [Migration Guide ↗︎](https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md) - Comprehensive migration documentation
- [AI SDK v5 Documentation ↗︎](https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0) - Official AI SDK migration guide
- [An Example PR showing the migration from AI SDK v4 to v5 ↗︎](https://github.com/cloudflare/agents-starter/pull/105)
- [GitHub Issues ↗︎](https://github.com/cloudflare/agents/issues) - Report bugs or request features

#### Feedback Welcome

We'd love your feedback! We're particularly interested in feedback on:

- **Migration experience** - How smooth was the upgrade process?
- **Tool confirmation workflow** - Does the new automatic detection work as expected?
- **Message format handling** - Any edge cases with legacy message conversion?

Sep 10, 2025

[<h2>Built with Cloudflare button</h2>](https://developers.cloudflare.com/changelog/post/2025-09-10-built-with-cloudflare-button/)

[Workers](https://developers.cloudflare.com/workers/)

We've updated our "Built with Cloudflare" button to make it easier to share that you're building on Cloudflare with the world. Embed it in your project's README, blog post, or wherever you want to let people know.

![Built with Cloudflare](https://workers.cloudflare.com/built-with-cloudflare.svg)

Check out the [documentation](https://developers.cloudflare.com/workers/platform/built-with-cloudflare) for usage information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/38/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/38/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
