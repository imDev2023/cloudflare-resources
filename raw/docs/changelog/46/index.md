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

May 8, 2025

[<h2>Improved memory efficiency for WebAssembly Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/)

[Workers](https://developers.cloudflare.com/workers/)

[FinalizationRegistry ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry) is now available in Workers. You can opt-in using the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag.

This can reduce memory leaks when using WebAssembly-based Workers, which includes [Python Workers](https://developers.cloudflare.com/workers/languages/python/) and [Rust Workers](https://developers.cloudflare.com/workers/languages/rust/). The FinalizationRegistry works by enabling toolchains such as [Emscripten ↗︎](https://emscripten.org/) and [wasm-bindgen ↗︎](https://wasm-bindgen.github.io/wasm-bindgen/) to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using [memory profiling](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/), you may want to enable the FinalizationRegistry.

For more information refer to the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag documentation.

May 7, 2025

[<h2>Send forensic copies to storage without DLP profiles</h2>](https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now [send DLP forensic copies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination) to third-party storage for any HTTP policy with an `Allow` or `Block` action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.

By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1324,height=636,format=webp/_astro/forensic-copies-for-all.fxeFrCY4.png)

May 6, 2025

[<h2>UDP and ICMP Monitor Support for Private Load Balancing Endpoints</h2>](https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports **UDP (Layer 4)** and **ICMP (Layer 3)** health monitors for **private endpoints**. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.

#### What you can do:

- Set up **ICMP ping monitors** to check if your private endpoints are reachable.
- Use **UDP monitors** for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.
- Gain better visibility and uptime guarantees for services running behind **Private Network Load Balancing**, without requiring public IP addresses.

This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with [**Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [**WARP**](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), and [**Magic WAN**](https://developers.cloudflare.com/cloudflare-wan/) to create a secure and observable private network.

Learn more about [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) or view the full list of [supported health monitor protocols](https://developers.cloudflare.com/load-balancing/monitors/#supported-protocols).

May 6, 2025

[<h2>Terraform v5.4.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-05-06-terraform-v5.4.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Removes the `worker_platforms_script_secret` resource from the provider (see [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret) for alternatives—applicable to both Workers and Workers for Platforms)
- Removes duplicated fields in `cloudflare_cloud_connector_rules` resource
- Fixes `cloudflare_workers_route` id issues [#5134 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134) [#5501 ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501)
- Fixes issue around refreshing resources that have unsupported response types<details><summary>Affected resources</summary>

  - <code>cloudflare_certificate_pack</code>
  - <code>cloudflare_registrar_domain</code>
  - <code>cloudflare_stream_download</code>
  - <code>cloudflare_stream_webhook</code>
  - <code>cloudflare_user</code>
  - <code>cloudflare_workers_kv</code>
  - <code>cloudflare_workers_script</code></details>
- Fixes `cloudflare_workers_kv` state refresh issues
- Fixes issues around configurability of nested properties without computed values for the following resources<details><summary>Affected resources</summary>

  - <code>cloudflare_account</code>
  - <code>cloudflare_account_dns_settings</code>
  - <code>cloudflare_account_token</code>
  - <code>cloudflare_api_token</code>
  - <code>cloudflare_cloud_connector_rules</code>
  - <code>cloudflare_custom_ssl</code>
  - <code>cloudflare_d1_database</code>
  - <code>cloudflare_dns_record</code>
  - <code>email_security_trusted_domains</code>
  - <code>cloudflare_hyperdrive_config</code>
  - <code>cloudflare_keyless_certificate</code>
  - <code>cloudflare_list_item</code>
  - <code>cloudflare_load_balancer</code>
  - <code>cloudflare_logpush_dataset_job</code>
  - <code>cloudflare_magic_network_monitoring_configuration</code>
  - <code>cloudflare_magic_transit_site</code>
  - <code>cloudflare_magic_transit_site_lan</code>
  - <code>cloudflare_magic_transit_site_wan</code>
  - <code>cloudflare_magic_wan_static_route</code>
  - <code>cloudflare_notification_policy</code>
  - <code>cloudflare_pages_project</code>
  - <code>cloudflare_queue</code>
  - <code>cloudflare_queue_consumer</code>
  - <code>cloudflare_r2_bucket_cors</code>
  - <code>cloudflare_r2_bucket_event_notification</code>
  - <code>cloudflare_r2_bucket_lifecycle</code>
  - <code>cloudflare_r2_bucket_lock</code>
  - <code>cloudflare_r2_bucket_sippy</code>
  - <code>cloudflare_ruleset</code>
  - <code>cloudflare_snippet_rules</code>
  - <code>cloudflare_snippets</code>
  - <code>cloudflare_spectrum_application</code>
  - <code>cloudflare_workers_deployment</code>
  - <code>cloudflare_zero_trust_access_application</code>
  - <code>cloudflare_zero_trust_access_group</code></details>
- Fixed defaults that made `cloudflare_workers_script` fail when using Assets
- Fixed Workers Logpush setting in `cloudflare_workers_script` mistakenly being readonly
- Fixed `cloudflare_pages_project` broken when using "source"

The detailed [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0) is available on GitHub.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare), or by opening a [support ticket ↗︎](https://www.support.cloudflare.com/s/?language=en_US).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare ↗︎](https://developers.cloudflare.com/terraform/)

May 5, 2025

[<h2>WAF Release - 2025-05-05</h2>](https://developers.cloudflare.com/changelog/post/2025-05-05-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.

**Key Findings**

GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.

The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.

**Impact**

Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:

- GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE
- SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances
- XWiki (CVE-2025-24893) - High priority for development environments
- Langflow (CVE-2025-3248) - Important for AI workflow platforms
- MinIO (CVE-2025-31489) - Important for object storage implementations

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d0b7a392 | 100724 | GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...717a9e42 | 100748 | XWiki - Remote Code Execution - CVE:CVE-2025-24893 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...e9cf745d | 100750 | SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040, CVE:CVE-2021-20041, CVE:CVE-2021-20042 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d29da333 | 100751 | Langflow - Remote Code Execution - CVE:CVE-2025-3248 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...caa7b208 | 100752 | MinIO - Auth Bypass - CVE:CVE-2025-31489 | Log | Block | This is a New Detection |

May 1, 2025

[<h2>Browser Isolation Overview page for Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/2025-05-01-browser-isolation-overview-page/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

A new **Browser Isolation Overview** page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) deployments, providing:

- **Streamlined Onboarding:** Easily set up and manage isolation policies from one location.
- **Quick Testing:** Validate [clientless web application isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) with ease.
- **Simplified Configuration:** Configure [isolated access applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/) and policies efficiently.
- **Centralized Monitoring:** Track aggregate usage and blocked actions.

This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.

![Browser Isolation Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1717,height=1286,format=webp/_astro/browser-isolation-overview.Ljd5ax_O.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and find Browser Isolation in the side navigation bar.

May 1, 2025

[<h2>R2 Dashboard experience gets new updates</h2>](https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/)

[R2](https://developers.cloudflare.com/r2/)

We're excited to announce several improvements to the [Cloudflare R2](https://developers.cloudflare.com/r2/) dashboard experience that make managing your object storage easier and more intuitive:

![Cloudflare R2 Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2286,height=1600,format=webp/_astro/r2-dashboard-updates.B7WXxzMk.png)

#### All-new settings page

We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.

#### Improved navigation and sharing

- Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.
- Objects as clickable links: Objects are now proper links that you can copy or `CMD + Click` to open in a new tab.

#### Clearer public access controls

- Renamed "r2.dev domain" to "Public Development URL" for better clarity when exposing bucket contents for non-production workloads.
- Public Access status now clearly displays "Enabled" when your bucket is exposed to the internet (via Public Development URL or Custom Domains).

We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.

Apr 30, 2025

[<h2>Dark Mode for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-04-30-zero-trust-dashboard-dark-mode/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The [Cloudflare Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) now supports Cloudflare's native dark mode for all accounts and plan types.

Zero Trust Dashboard will automatically accept your user-level preferences for system settings, so if your Dashboard appearance is set to 'system' or 'dark', the Zero Trust dashboard will enter dark mode whenever the rest of your Cloudflare account does.

![Zero Trust dashboard supports dark mode](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3456,height=1596,format=webp/_astro/dark-mode.DfLeS20d.png)

To update your view preference in the Zero Trust dashboard:

1. Log into the [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/).
2. Select your user icon.
3. Select **Dark Mode**.

To update your view preference in the Core dashboard:

1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
2. Go to **My Profile**
3. For **Appearance**, choose **Dark**.

Apr 30, 2025

[<h2>Cloudflare One Appliance supports multiple DNS server IPs</h2>](https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.

Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.

For configuration details, refer to [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/).

Apr 28, 2025

[<h2>FQDN Filtering For Gateway Egress Policies</h2>](https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.

- Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.
- During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
  - For WARP client support, additional configuration is required. For more information, refer to the [WARP client configuration documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#limitations).

![Egress by FQDN and Hostname](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=841,height=1045,format=webp/_astro/Gateway-Egress-FQDN-Policy-preview.Civon5p8.png)

This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.

Apr 26, 2025

[<h2>WAF Release - 2025-04-26 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-04-26-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...19fcc883 | 100755 | React.js - Router and Remix Vulnerability - CVE:CVE-2025-43864, CVE:CVE-2025-43865 | Block | Block | This is a New Detection |

Apr 24, 2025

[<h2>Custom Errors are now Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2025-04-24-custom-errors-ga/)

[Rules](https://developers.cloudflare.com/rules/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.

You can now manage **Custom Error Rules**, **Custom Error Assets**, and redesigned **Error Pages** directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.

What's new:

- **Custom Errors are now GA** – Available on all paid plans and ready for production traffic.
- **UI for Custom Error Rules and Assets** – Manage your zone-level rules from the Rules > Overview and your zone-level assets from the Rules > Settings tabs.
- **Define inline content or upload assets** – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.
- **Refreshed UI and new name for Error Pages** – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.
- **Powered by Ruleset Engine** – Custom Error Rules support [conditional logic](https://developers.cloudflare.com/ruleset-engine/rules-language/) and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or [other Cloudflare products](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/). You can also configure [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) to add, change, or remove HTTP headers from responses returned by Custom Error Rules.

Learn more in the [Custom Errors documentation](https://developers.cloudflare.com/rules/custom-errors/).

Apr 24, 2025

[<h2>Cron triggers are now supported in Python Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/)

[Workers](https://developers.cloudflare.com/workers/)

You can now create Python Workers which are executed via a cron trigger.

This is similar to how it's done in JavaScript Workers, simply define a scheduled event listener in your Worker:

```python
from workers import handler

@handler
async def on_scheduled(event, env, ctx):
  print("cron processed")
```

Define a cron trigger configuration in your Wrangler configuration file:

```jsonc
{
	"triggers": {
		// Schedule cron triggers:
		// - At every 3rd minute
		// - At 15:00 (UTC) on first day of the month
		// - At 23:59 (UTC) on the last weekday of the month
		"crons": [
			"*/3 * * * *",
			"0 15 1 * *",
			"59 23 LW * *"
		]
	}
}
```

```toml
[triggers]
crons = [ "*/3 * * * *", "0 15 1 * *", "59 23 LW * *" ]
```

Then test your new handler by using Wrangler with the `--test-scheduled` flag and making a request to `/cdn-cgi/local/scheduled?cron=*+*+*+*+*`:

```sh
npx wrangler dev --test-scheduled

curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"
```

Consult the [Workers Cron Triggers page](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for full details on cron triggers in Workers.

Apr 23, 2025

[<h2>Metadata filtering and multitenancy support in AutoRAG</h2>](https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/)

[AI Search](https://developers.cloudflare.com/ai-search/)

You can now filter [AutoRAG](https://developers.cloudflare.com/ai-search/) search results by `folder` and `timestamp` using [metadata filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) to narrow down the scope of your query.

This makes it easy to build [multitenant experiences](https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/) where each user can only access their own data. By organizing your content into per-tenant folders and applying a `folder` filter at query time, you ensure that each tenant retrieves only their own documents.

**Example folder structure:**

```bash
customer-a/logs/
customer-a/contracts/
customer-b/contracts/
```

**Example query:**

```js
const response = await env.AI.autorag("my-autorag").search({
	query: "When did I sign my agreement contract?",
	filters: {
		type: "eq",
		key: "folder",
		value: "customer-a/contracts/",
	},
});
```

You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select **Sync index**. Metadata filtering is available for all data indexed on or after **April 21, 2025**.

If you are new to AutoRAG, get started with the [Get started AutoRAG guide](https://developers.cloudflare.com/ai-search/get-started/).

Apr 22, 2025

[<h2>WAF Release - 2025-04-22</h2>](https://developers.cloudflare.com/changelog/post/2025-04-22-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.

When deciding which exploits to tackle, Cloudflare tunes into the attackers' areas of focus. Cloudflare's network intelligence provides a unique lens into attacker activity – for instance, through the volume of blocked requests related with CVE exploits after updating WAF Managed Rules with new detections.

From this week's releases, one indicator that RCE is a "hot topic" attack type is the fact that the Oracle PeopleSoft RCE rule accounts for half of all of the new rule matches. This rule patches CVE-2023-22047, a high-severity vulnerability in the Oracle PeopleSoft suite that allows unauthenticated attackers to access PeopleSoft Enterprise PeopleTools data through remote code execution. This is particularly concerning because of the nature of the data managed by PeopleSoft – this can include payroll records or student profile information. This CVE, along with five others, are addressed with the latest detection update to WAF Managed Rules.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a5be3327 | 100738 | GitLab - Auth Bypass - CVE:CVE-2023-7028 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...6c9531fa | 100740 | Splunk Enterprise - Remote Code Execution - CVE:CVE-2025-20229 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f40bbc2b | 100741 | Oracle PeopleSoft - Remote Code Execution - CVE:CVE-2023-22047 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5462167c | 100742 | CrushFTP - Auth Bypass - CVE:CVE-2025-31161 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...caa7b208 | 100743 | Ivanti - Buffer Error - CVE:CVE-2025-22457 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d52139a8 | 100744 | Oracle Access Manager - Remote Code Execution - CVE:CVE-2021-35587 | Log | Disabled | This is a New Detection |

Apr 21, 2025

[<h2>Access bulk policy tester</h2>](https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

The [Access bulk policy tester](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application) is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).

![Example policy tester](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1531,height=693,format=webp/_astro/example-policy-tester.DCY8hQvx.png)

Apr 18, 2025

[<h2>Custom fields raw and transformed values support</h2>](https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/)

[Logs](https://developers.cloudflare.com/logs/)

Custom Fields now support logging both **raw and transformed values** for request and response headers in the HTTP requests dataset.

These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.

By default:

- Request headers are logged as raw values
- Response headers are logged as transformed values

These defaults can be overridden to suit your logging needs.

Note

Transformed and raw values for request and response headers are available **only via the API** and cannot be set through the UI.

For more information refer to [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/) documentation

Apr 17, 2025

[<h2>Increased limits for Queues pull consumers</h2>](https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) can now pull and acknowledge up to **5,000 messages / second per queue**. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.

Pull consumers allow you to consume messages over HTTP from any environment—including outside of [Cloudflare Workers](https://developers.cloudflare.com/workers). They’re also useful when you need fine-grained control over how quickly messages are consumed.

To setup a new queue with a pull based consumer using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:

*Create a queue with a pull based consumersh*

```sh
npx wrangler queues create my-queue
npx wrangler queues consumer http add my-queue
```

You can also configure a pull consumer using the [REST API](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/create/) or the Queues dashboard.

Once configured, you can pull messages from the queue using any HTTP client. You'll need a [Cloudflare API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `queues_read` and `queues_write` permissions. For example:

*Pull messages from a queuebash*

```bash
curl "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull" \
--header "Authorization: Bearer ${API_TOKEN}" \
--header "Content-Type: application/json" \
--data '{ "visibility_timeout": 10000, "batch_size": 2 }'
```

To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the [pull consumer documentation](https://developers.cloudflare.com/queues/configuration/pull-consumers).

As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the [existing rate](https://developers.cloudflare.com/queues/platform/pricing), of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

Apr 17, 2025

[<h2>Read multiple keys from Workers KV with bulk reads</h2>](https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/)

[KV](https://developers.cloudflare.com/kv/)

You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.

This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by [Workers simultaneous connection limits](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections).

```js
// Read single key
const key = "key-a";
const value = await env.NAMESPACE.get(key);

// Read multiple keys
const keys = ["key-a", "key-b", "key-c", ...] // up to 100 keys
const values : Map<string, string?> = await env.NAMESPACE.get(keys);

// Print the value of "key-a" to the console.
console.log(`The first key is ${values.get("key-a")}.`)
```

Consult the [Workers KV Read key-value pairs API](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) for full details on Workers KV's new bulk reads support.

Apr 15, 2025

[<h2>Cloudflare Registrar API is now in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/)

[Registrar](https://developers.cloudflare.com/registrar/)

Cloudflare Registrar API is now in beta.

You can now use the Cloudflare API to:

- Search for domain names.
- Check real-time availability and pricing.
- Register supported domains programmatically.

This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.

Because the Registrar API is part of the Cloudflare API, it can also be used in [Cloudflare MCP ↗︎](https://github.com/cloudflare/mcp) and other agent-driven workflows.

If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:

- `Search for domain ideas for a coffee shop based in Evergreen, Colorado.`
- `Check whether example.com is available and show me the current price.`
- `Register example.com`

For supported operations, extension availability, and workflow details, refer to:

- [Registrar API guide ↗︎](https://developers.cloudflare.com/registrar/registrar-api/)
- [Registrar API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar)

Apr 15, 2025

[<h2>Fixed and documented Workers Routes and Secrets API</h2>](https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/)

[Workers](https://developers.cloudflare.com/workers/) [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

#### Workers Routes API

Previously, a request to the Workers [Create Route API](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/create/) always returned `null` for "script" and an empty string for "pattern" even if the request was successful.

*Example requestbash*

```bash
curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \
-X PUT \
-H "Authorization: Bearer $CF_API_TOKEN" \
-H 'Content-Type: application/json' \
--data '{ "pattern": "example.com/*", "script": "hello-world-script" }'
```

*Example bad responsejson*

```json
{
	"result": {
		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
		"pattern": "",
		"script": null,
		"request_limit_fail_open": false
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

Now, it properly returns all values!

*Example good responsejson*

```json
{
	"result": {
		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
		"pattern": "example.com/*",
		"script": "hello-world-script",
		"request_limit_fail_open": false
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

#### Workers Secrets API

The [Workers](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/) and [Workers for Platforms](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/) secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (>4.2.0) and [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (>4.1.0).

Note the `cloudflare_workers_secret` and `cloudflare_workers_for_platforms_script_secret` [Terraform resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:

- [Secrets Store](https://developers.cloudflare.com/api/resources/secrets_store/) with the "Secrets Store Secret" binding on Workers and Workers for Platforms Script Upload
- "Secret Text" Binding on [Workers Script Upload](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update/) and [Workers for Platforms Script Upload](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/)
- Workers (and WFP) Secrets API

Apr 14, 2025

[<h2>New predefined detection entry for ICD-11</h2>](https://developers.cloudflare.com/changelog/post/2025-04-14-icd11-support/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You now have access to the World Health Organization (WHO) 2025 edition of the [International Classification of Diseases 11th Revision (ICD-11) ↗︎](https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29) as a predefined detection entry. The new dataset can be found in the [Health Information](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information) predefined profile.

ICD-10 dataset remains available for use.

Apr 14, 2025

[<h2>WAF Release - 2025-04-14</h2>](https://developers.cloudflare.com/changelog/post/2025-04-14-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d6b2d36c | 100739A | Next.js - Auth Bypass - CVE:CVE-2025-29927 - 2 | Log | Disabled | This is a New Detection |

Apr 11, 2025

[<h2>HTTP redirect and custom block page redirect</h2>](https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now use more flexible redirect capabilities in Cloudflare One with Gateway.

- A new **Redirect** action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.
- For **Block** actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.

Learn more in our documentation for [HTTP Redirect](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#redirect) and [Block page redirect](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page).

Apr 11, 2025

[<h2>Signed URLs and Infrastructure Improvements on Stream Live WebRTC Beta</h2>](https://developers.cloudflare.com/changelog/post/2025-04-14-webrtc-beta-signed-urls/)

[Stream](https://developers.cloudflare.com/stream/)

Cloudflare [Stream](https://developers.cloudflare.com/stream/) has completed an infrastructure upgrade for our [Live WebRTC beta](https://developers.cloudflare.com/stream/webrtc-beta/) support which brings increased scalability and improved playback performance to all customers. WebRTC allows broadcasting directly from a browser (or supported WHIP client) with ultra-low latency to tens of thousands of concurrent viewers across the globe.

Additionally, as part of this upgrade, the WebRTC beta now supports Signed URLs to protect playback, just like our standard live stream options (HLS/DASH).

For more information, learn about the [Stream Live WebRTC beta](https://developers.cloudflare.com/stream/webrtc-beta/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/46/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/46/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
