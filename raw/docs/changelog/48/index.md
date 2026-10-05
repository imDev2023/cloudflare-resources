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

Apr 4, 2025

[<h2>Workers Fetch API can override Cache Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-04-04-workers-fetch-api-override-cache-rules/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now programmatically override Cache Rules using the `cf` object in the `fetch()` command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.

#### How it works

Using the `cf` object in `fetch()`, you can override specific Cache Rules settings by:

1. **Setting custom cache options**: Pass cache properties in the `cf` object as the second argument to `fetch()` to override default Cache Rules.
2. **Dynamic cache control**: Apply different caching strategies based on request headers, cookies, or other runtime conditions.
3. **Per-request customization**: Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.
4. **Programmatic cache management**: Implement complex caching logic that adapts to your application's needs.

#### What can be configured

Workers can override the following Cache Rules settings through the `cf` object:

- **`cacheEverything`**: Treat all content as static and cache all file types beyond the default cached content.
- **`cacheTtl`**: Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.
- **`cacheTtlByStatus`**: Set different TTLs based on the response status code (for example, `{ "200-299": 86400, 404: 1, "500-599": 0 }`).
- **`cacheKey`**: Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).
- **`cacheTags`**: Append additional cache tags for targeted cache purging operations.

#### Benefits

- **Enhanced flexibility**: Customize cache behavior without modifying zone-level Cache Rules.
- **Dynamic optimization**: Adjust caching strategies in real-time based on request context.
- **Simplified configuration**: Reduce the number of Cache Rules needed by handling edge cases programmatically.
- **Improved performance**: Fine-tune cache behavior for specific use cases to maximize hit rates.

#### Get started

To get started, refer to the [Workers Fetch API documentation](https://developers.cloudflare.com/workers/runtime-apis/fetch/) and the [cf object properties documentation](https://developers.cloudflare.com/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties).

Apr 3, 2025

[<h2>All cache purge methods now available for all plans</h2>](https://developers.cloudflare.com/changelog/post/2025-04-01-purge-for-all/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now access all Cloudflare cache purge methods — no matter which plan you’re on. Whether you need to update a single asset or instantly invalidate large portions of your site’s content, you now have the same powerful tools previously reserved for Enterprise customers.

**Anyone on Cloudflare can now:**

1. [Purge Everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/): Clears all cached content associated with a website.
2. [Purge by Prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/): Targets URLs sharing a common prefix.
3. [Purge by Hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/): Invalidates content by specific hostnames.
4. [Purge by URL (single-file purge)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/): Precisely targets individual URLs.
5. [Purge by Tag](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/): Uses Cache-Tag response headers to invalidate grouped assets, offering flexibility for complex cache management scenarios.

Want to learn how each purge method works, when to use them, or what limits apply to your plan? Dive into our [purge cache documentation](https://developers.cloudflare.com/cache/how-to/purge-cache/) and [API reference ↗︎](https://developers.cloudflare.com/api/resources/cache/methods/purge/) for all the details.

Apr 2, 2025

[<h2>WAF Release - 2025-04-02</h2>](https://developers.cloudflare.com/changelog/post/2025-04-02-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...622f0483 | 100732 | Sitecore - Code Injection - CVE:CVE-2025-27218 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0f101cca | 100733 | Angular-Base64-Upload - Remote Code Execution - CVE:CVE-2024-42640 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...1bbcd247 | 100734 | Apache Camel - Remote Code Execution - CVE:CVE-2025-29891 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...90aea1ca | 100735 | Progress Software WhatsUp Gold - Remote Code Execution - CVE:CVE-2024-4885 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d9d8c5f2 | 100737 | Apache Tomcat - Remote Code Execution - CVE:CVE-2025-24813 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...a28a42c4 | 100659 | Common Payloads for Server-side Template Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...daa4b037 | 100659 | Common Payloads for Server-side Template Injection - Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...48f6a9cf | 100642 | LDAP Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...e0713e9f | 100642 | LDAP Injection Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...1bc977d1 | 100005 | DotNetNuke - File Inclusion - CVE:CVE-2018-9126, CVE:CVE-2011-1892, CVE:CVE-2022-31474 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...bb70a463 | 100527 | Apache Struts - CVE:CVE-2021-31805 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...0c99546a | 100702 | Command Injection - CVE:CVE-2022-24108 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...9a5581d0 | 100622C | Ivanti - Command Injection - CVE:CVE-2023-46805, CVE:CVE-2024-21887, CVE:CVE-2024-22024 | N/A | Block | N/A |
| Cloudflare Managed Ruleset | ...06d0b009 | 100536C | GraphQL Command Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...1651d0c8 | 100536 | GraphQL Injection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...af00f61d | 100536A | GraphQL Introspection | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...a41e5b67 | 100536B | GraphQL SSRF | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...433e5b3d | 100559A | Prototype Pollution - Common Payloads | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...4816b26f | 100559A | Prototype Pollution - Common Payloads - Base64 | N/A | Disabled | N/A |
| Cloudflare Managed Ruleset | ...fcea5ed2 | 100734 | Apache Camel - Remote Code Execution - CVE:CVE-2025-29891 | N/A | Disabled | N/A |

Apr 1, 2025

[<h2>CASB and Email security</h2>](https://developers.cloudflare.com/changelog/post/2025-04-01-casb-email-security/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

With Email security, you get two free CASB integrations.

Use one SaaS integration for Email security to sync with your directory of users, take actions on delivered emails, automatically provide EMLs for reclassification requests for clean emails, discover CASB findings and more.

With the other integration, you can have a separate SaaS integration for CASB findings for another SaaS provider.

Refer to [Add an integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) to learn more about this feature.

![CASB-EmailSecurity](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=727,height=502,format=webp/_astro/CASB-EmailSecurity.B1wd9be2.png)

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Mar 27, 2025

[<h2>New Pause & Purge APIs for Queues</h2>](https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues](https://developers.cloudflare.com/queues/) now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:

- Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug
- You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog
- Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed

To pause a queue using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run the `pause-delivery` command. Paused queues continue to receive messages. And you can easily unpause a queue using the `resume-delivery` command.

*Pause and resume a queuebash*

```bash
$ wrangler queues pause-delivery my-queue
Pausing message delivery for queue my-queue.
Paused message delivery for queue my-queue.

$ wrangler queues resume-delivery my-queue
Resuming message delivery for queue my-queue.
Resumed message delivery for queue my-queue.
```

Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:

*Purge a queuebash*

```bash
$ wrangler queues purge my-queue
✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue
Purged queue 'my-queue'
```

You can also do these operations using the [Queues REST API](https://developers.cloudflare.com/api/resources/queues/), or the dashboard page for a queue.

![Pause and purge using the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2200,height=574,format=webp/_astro/pause-purge.SQ7B3RCF.png)

This feature is available on all new and existing queues. Head over to the [pause and purge documentation](https://developers.cloudflare.com/queues/configuration/pause-purge) to learn more. And if you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

Mar 27, 2025

[<h2>Register and renew .ai and .shop domains at cost</h2>](https://developers.cloudflare.com/changelog/post/2025-03-27-ai-domains-available/)

[Registrar](https://developers.cloudflare.com/registrar/)

![Example search for .ai domains](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1788,height=818,format=webp/_astro/2025-03-27-ai-domains-available.D96eztke.png)

Cloudflare Registrar now supports `.ai` and `.shop` domains. These are two of our most highly-requested top-level domains (TLDs) and are great additions to the [300+ other TLDs we support ↗︎](https://domains.cloudflare.com/tlds).

Starting today, customers can:

- Register and renew these domains *at cost* without any markups or add-on fees
- Enjoy best-in-class security and performance with native integrations with Cloudflare DNS, CDN, and SSL services like one-click DNSSEC
- Combat domain hijacking with [Custom Domain Protection ↗︎](https://www.cloudflare.com/products/registrar/custom-domain-protection/) (available on enterprise plans)

We can't wait to see what AI and e-commerce projects you deploy on Cloudflare. To get started, transfer your domains to Cloudflare or [search for new ones to register ↗︎](https://domains.cloudflare.com/).

Mar 27, 2025

[<h2>Audit logs (version 2) - Beta Release</h2>](https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.

Availability: Audit logs (version 2) is now in Beta, with support limited to **API access**.

Use the following API endpoint to retrieve audit logs:

```js
GET https://api.cloudflare.com/client/v4/accounts/<account_id>/logs/audit?since=<date>&before=<date>
```

You can access detailed documentation for audit logs (version 2) Beta API release [here ↗︎](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/).

**Key Improvements in the Beta Release:**

- **Automated & standardized logging**: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.
- **Expanded product coverage**: Increased audit log coverage from 75% to 95%. Key API endpoints such as `/accounts`, `/zones`, and `/organizations` are now included.
- **Granular filtering**: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.
- **Enhanced context and traceability**: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.
- **Comprehensive activity capture**: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.

**Known Limitations in Beta**

- Error handling for the API is not implemented.
- There may be gaps or missing entries in the available audit logs.
- UI is unavailable in this Beta release.
- System-level logs and User-Activity logs are not included.

Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: [Introducing Automatic Audit Logs ↗︎](https://blog.cloudflare.com/introducing-automatic-audit-logs/)

Mar 26, 2025

[<h2>Updates to Account Home - Quick actions, traffic insights, Workers projects, and more</h2>](https://developers.cloudflare.com/changelog/post/2025-03-26-account-home-updates/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

![Updated Account Home](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2574,height=982,format=webp/_astro/2025-03-26-account-home-updates.CcOsD1dD.png)

Recently, Account Home has been updated to streamline your workflows:

- **Recent Workers projects**: You'll now find your projects readily accessible from a new `Developer Platform` tab on Account Home. See recently-modified projects and explore what you can work our developer-focused products.
- **Traffic and security insights**: Get a snapshot of domain performance at a glance with key metrics and trends.
- **Quick actions**: You can now perform common actions for your account, domains, and even Workers in just 1-2 clicks from the 3-dot menu.
- **Keep starred domains front and center**: Now, when you filter for starred domains on Account Home, we'll save your preference so you'll continue to only see starred domains by default.

We can't wait for you to take the new Account Home for a spin.

For more info:

- [Try the updated Account Home ↗︎](https://dash.cloudflare.com/)
- [Documentation on starred domains](https://developers.cloudflare.com/fundamentals/manage-domains/star-zones/)

Mar 26, 2025

[<h2>Run Workers for up to 5 minutes of CPU-time</h2>](https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/)

[Workers](https://developers.cloudflare.com/workers/)

You can now run a Worker for up to 5 minutes of CPU time for each request.

Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This meant that some compute-intensive tasks were impossible to do with a Worker. For instance, you might want to take the cryptographic hash of a large file from R2. If this computation ran for over 30 seconds, the Worker request would have timed out.

By default, Workers are still limited to 30 seconds of CPU time. This protects developers from incurring accidental cost due to buggy code.

By changing the `cpu_ms` value in your Wrangler configuration, you can opt in to any value up to 300,000 (5 minutes).

```jsonc
{
	// ...rest of your configuration...
	"limits": {
		"cpu_ms": 300000,
	},
	// ...rest of your configuration...
}
```

```toml
[limits]
cpu_ms = 300_000
```

Note

CPU time is the amount of time the CPU actually spends doing work during a given request. If a Worker's request makes a sub-request and waits for that request to come back before doing additional work, this time spent waiting **is not** counted towards CPU time.

Worker requests could run for more than 30 seconds of total time prior to this change — only CPU time was limited.

For more information on the updates limits, see the documentation on [Wrangler configuration for `cpu_ms`](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and on [Workers CPU time limits](https://developers.cloudflare.com/workers/platform/limits/#cpu-time).

For building long-running tasks on Cloudflare, we also recommend checking out [Workflows](https://developers.cloudflare.com/workflows/) and [Queues](https://developers.cloudflare.com/queues/).

Mar 25, 2025

[<h2>Source Maps are Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/)

[Workers](https://developers.cloudflare.com/workers/)

Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB. Previously, the maximum size limit was 15 MB uncompressed.

Source maps help map between the original source code and the transformed/minified code that gets deployed to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions onto the original source code making it easier to debug.

![Stack Trace without Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1908,height=198,format=webp/_astro/without-source-map.ByYR83oU.png)

With **no source maps uploaded**: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references `js` instead of `ts`.

![Stack Trace with Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=238,format=webp/_astro/with-source-map.PipytmVe.png)

With **source maps uploaded**: all methods reference the correct files and line numbers.

Uploading source maps and stack trace remapping happens out of band from the Worker execution, so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.

To enable source maps, add the following to your [Pages Function's](https://developers.cloudflare.com/pages/functions/source-maps/) or [Worker's](https://developers.cloudflare.com/workers/observability/source-maps/) wrangler configuration:

```jsonc
{
	"upload_source_maps": true
}
```

```toml
upload_source_maps = true
```

Mar 22, 2025

[<h2>WAF Release - 2025-03-22 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-03-22-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...f472013e | 100739 | Next.js - Auth Bypass - CVE:CVE-2025-29927 | N/A | Disabled | This is a New Detection |

Mar 22, 2025

[<h2>New Managed WAF rule for Next.js CVE-2025-29927.</h2>](https://developers.cloudflare.com/changelog/post/2025-03-22-next-js-vulnerability-waf/)

[Workers](https://developers.cloudflare.com/workers/) [Pages](https://developers.cloudflare.com/pages/) [WAF](https://developers.cloudflare.com/waf/)

**Update: Mon Mar 24th, 11PM UTC**: Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions `15.2.4`, `14.2.26`, `13.5.10` or `12.3.6`. **If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation**.

**Update: Mon Mar 24th, 8PM UTC**: Next.js has now [backported the patch for this vulnerability ↗︎](https://github.com/advisories/GHSA-f82v-jwr5-mffw) to cover Next.js v12 and v13. Users on those versions will need to patch to `13.5.9` and `12.3.5` (respectively) to mitigate the vulnerability.

**Update: Sat Mar 22nd, 4PM UTC**: We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.

**We strongly recommend updating your version of Next.js (if eligible)** to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.

#### Enable the Managed Rule (strongly recommended)

This rule is opt-in only for sites on the Pro plan or above in the [WAF managed ruleset](https://developers.cloudflare.com/waf/managed-rules/).

To enable the rule:

1. Head to Security > WAF > Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.
2. Click the three dots next to **Cloudflare Managed Ruleset** and choose **Edit**
3. Scroll down and choose **Browse Rules**
4. Search for **CVE-2025-29927** (ruleId: `34583778093748cc83ff7b38f472013e`)
5. Change the **Status** to **Enabled** and the **Action** to **Block**. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.
6. Click **Next**
7. Scroll down and choose **Save**

This will enable the WAF rule and block requests with the `x-middleware-subrequest` header regardless of Next.js version.

#### Create a WAF rule (manual)

For users on the Free plan, or who want to define a more specific rule, you can create a [Custom WAF rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) to block requests with the `x-middleware-subrequest` header regardless of Next.js version.

To create a custom rule:

1. Head to Security > WAF > Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.
2. Give the rule a name - e.g. `next-js-CVE-2025-29927`
3. Set the matching parameters for the rule match any request where the `x-middleware-subrequest` header `exists` per the rule expression below.

```sh
(len(http.request.headers["x-middleware-subrequest"]) > 0)
```

4. Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).
5. **Deploy** the rule.

![Next.js CVE-2025-29927 WAF rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2116,height=1148,format=webp/_astro/waf-rule-cve-2025-29927.0i0XiweZ.png)

#### Next.js CVE-2025-29927

We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the [Next.js authentication bypass vulnerability ↗︎](https://github.com/advisories/GHSA-f82v-jwr5-mffw) (`CVE-2025-29927`) published on March 21st, 2025.

**Note**: This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.

- This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.
- This rule has been made available (but not enabled by default) to all sites as part of our [WAF Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/) and blocks requests that attempt to bypass authentication in Next.js applications.
- The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js `14.2.26` and `15.2.4`. Earlier, interim releases did not fully patch this vulnerability.
- **Users on older versions of Next.js ( `11.1.4` to `13.5.6`) did not originally have a patch available**, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions `12.3.6` and `13.5.10` as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.

The managed WAF rule mitigates this by blocking *external* user requests with the `x-middleware-subrequest` header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.

Mar 22, 2025

[<h2>Smart Placement is smarter about running Workers and Pages Functions in the best locations</h2>](https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/)

[Workers](https://developers.cloudflare.com/workers/) [Pages](https://developers.cloudflare.com/pages/)

[Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.

Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.

Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.

Mar 21, 2025

[<h2>AI Gateway launches Realtime WebSockets API</h2>](https://developers.cloudflare.com/changelog/post/2025-03-20-websockets/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

We are excited to announce that [AI Gateway](https://developers.cloudflare.com/ai-gateway/) now supports real-time AI interactions with the new [Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/).

This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.

The Realtime WebSockets API works with the [OpenAI Realtime API ↗︎](https://platform.openai.com/docs/guides/realtime#connect-with-websockets), [Google Gemini Live API ↗︎](https://ai.google.dev/gemini-api/docs/multimodal-live), and supports real-time text and speech interactions with models from [Cartesia ↗︎](https://docs.cartesia.ai/api-reference/tts/tts), and [ElevenLabs ↗︎](https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket).

Here's how you can connect AI Gateway to [OpenAI's Realtime API ↗︎](https://platform.openai.com/docs/guides/realtime#connect-with-websockets) using WebSockets:

*OpenAI Realtime API examplejavascript*

```javascript
import WebSocket from "ws";

const url =
	"wss://gateway.ai.cloudflare.com/v1/<account_id>/<gateway>/openai?model=gpt-4o-realtime-preview-2024-12-17";
const ws = new WebSocket(url, {
	headers: {
		"cf-aig-authorization": process.env.CLOUDFLARE_API_KEY,
		Authorization: "Bearer " + process.env.OPENAI_API_KEY,
		"OpenAI-Beta": "realtime=v1",
	},
});

ws.on("open", () => console.log("Connected to server."));
ws.on("message", (message) => console.log(JSON.parse(message.toString())));

ws.send(
	JSON.stringify({
		type: "response.create",
		response: { modalities: ["text"], instructions: "Tell me a joke" },
	}),
);
```

Get started by checking out the [Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/) documentation.

Mar 21, 2025

[<h2>Secure DNS Locations Management User Role</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We're excited to introduce the [**Cloudflare Zero Trust Secure DNS Locations Write role**](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations), designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.

Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.

**Secure DNS Location Requirements:**

- Mandate usage of [Bring your own DNS resolver IP addresses ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip) if available on the account.
- Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.

You can assign the new role via Cloudflare Dashboard (`Manage Accounts > Members`) or via API. For more information, refer to the [Secure DNS Locations documentation ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations).

Mar 21, 2025

[<h2>Dozens of Cloudflare Terraform Provider resources now have proper drift detection</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your `terraform plan` to only show what resources are expected to change.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- API Shield
- Argo Smart Routing
- Argo Tiered Caching
- Bot Management
- BYOIP
- D1
- DNS
- Email Routing
- Hyperdrive
- Observatory
- Pages
- R2
- Rules
- SSL/TLS
- Waiting Room
- Workers
- Zero Trust

Mar 21, 2025

[<h2>Cloudflare Terraform Provider now properly redacts sensitive values</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

In the [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in [Cloudflare's OpenAPI Schema ↗︎](https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml) are now annotated with `x-sensitive: true`. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- Alerts and Audit Logs
- Device API
- DLP
- DNS
- Magic Visibility
- Magic WAN
- TLS Certs and Hostnames
- Tunnels
- Turnstile
- Workers
- Zaraz

Mar 20, 2025

[<h2>Markdown conversion in Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2025-03-20-markdown-conversion/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the `toMarkdown` utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.

You can call this new tool using a binding by calling `env.AI.toMarkdown()` or the using the [REST API](https://developers.cloudflare.com/api/resources/ai/) endpoint.

In this example, we fetch a PDF document and an image from R2 and feed them both to `env.AI.toMarkdown()`. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.

```typescript
import { Env } from "./env";

export default {
	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf
		const pdf = await env.R2.get("somatosensory.pdf");

		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg
		const cat = await env.R2.get("cat.jpeg");

		return Response.json(
			await env.AI.toMarkdown([
				{
					name: "somatosensory.pdf",
					blob: new Blob([await pdf.arrayBuffer()], {
						type: "application/octet-stream",
					}),
				},
				{
					name: "cat.jpeg",
					blob: new Blob([await cat.arrayBuffer()], {
						type: "application/octet-stream",
					}),
				},
			]),
		);
	},
};
```

This is the result:

```json
[
	{
		"name": "somatosensory.pdf",
		"mimeType": "application/pdf",
		"format": "markdown",
		"tokens": 0,
		"data": "# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase..."
	},
	{
		"name": "cat.jpeg",
		"mimeType": "image/jpeg",
		"format": "markdown",
		"tokens": 0,
		"data": "The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat's eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat's facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people."
	}
]
```

See [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) for more information on supported formats, REST API and pricing.

Mar 19, 2025

[<h2>WAF Release - 2025-03-19 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-03-19-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a2cafae7 | 100736 | Generic HTTP Request Smuggling | N/A | Disabled | This is a New Detection |

Mar 18, 2025

[<h2>npm i agents</h2>](https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

![npm i agents](https://developers.cloudflare.com/_astro/npm-i-agents.CXCpJ1-7.apng)

#### `agents-sdk` -> `agents` Updated

📝 **We've renamed the Agents package to `agents`**!

If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to `agents-sdk` with `agents`:

```sh
# Install the new package
npm i agents
```

```sh
# Remove the old (deprecated) package
npm uninstall agents-sdk

# Find instances of the old package name in your codebase
grep -r 'agents-sdk' .
# Replace instances of the old package name with the new one
# (or use find-replace in your editor)
sed -i 's/agents-sdk/agents/g' $(grep -rl 'agents-sdk' .)
```

All future updates will be pushed to the new `agents` package, and the older package has been marked as deprecated.

#### Agents SDK updates New

We've added a number of big new features to the Agents SDK over the past few weeks, including:

- You can now set `cors: true` when using `routeAgentRequest` to return permissive default CORS headers to Agent responses.
- The regular client now syncs state on the agent (just like the React version).
- `useAgentChat` bug fixes for passing headers/credentials, including properly clearing cache on unmount.
- Experimental `/schedule` module with a prompt/schema for adding scheduling to your app (with evals!).
- Changed the internal `zod` schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.

We've also fixed a number of bugs with state synchronization and the React hooks.

```js
// via https://github.com/cloudflare/agents/tree/main/examples/cross-domain
export default {
	async fetch(request, env) {
		return (
			// Set { cors: true } to enable CORS headers.
			(await routeAgentRequest(request, env, { cors: true })) ||
			new Response("Not found", { status: 404 })
		);
	},
};
```

```ts
// via https://github.com/cloudflare/agents/tree/main/examples/cross-domain
export default {
	async fetch(request: Request, env: Env) {
		return (
			// Set { cors: true } to enable CORS headers.
			(await routeAgentRequest(request, env, { cors: true })) ||
			new Response("Not found", { status: 404 })
		);
	},
} satisfies ExportedHandler<Env>;
```

#### Call Agent methods from your client code New

We've added a new [`@unstable_callable()`](https://developers.cloudflare.com/agents/runtime/agents-api/) decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.

```js
// server.ts
import { unstable_callable, Agent } from "agents";

export class Rpc extends Agent {
	// Use the decorator to define a callable method
	@unstable_callable({
		description: "rpc test",
	})
	async getHistory() {
		return this.sql`SELECT * FROM history ORDER BY created_at DESC LIMIT 10`;
	}
}
```

```ts
// server.ts
import { unstable_callable, Agent, type StreamingResponse } from "agents";
import type { Env } from "../server";

export class Rpc extends Agent<Env> {
	// Use the decorator to define a callable method
	@unstable_callable({
		description: "rpc test",
	})
	async getHistory() {
		return this.sql`SELECT * FROM history ORDER BY created_at DESC LIMIT 10`;
	}
}
```

```tsx
// client.tsx
const { call } = useAgent({ agent: "rpc" });

const fetchUserHistory = async () => {
	try {
		setLoading(true);
		// Call methods directly on the Agent!
		const result = await call("getHistory");
		addToast(`RPC result: ${result}`, "success");
	} catch (error) {
		addToast(`Error: ${error}`, "error");
	} finally {
		setLoading(false);
	}
};
```

#### agents-starter Updated

We've fixed a number of small bugs in the [`agents-starter` ↗︎](https://github.com/cloudflare/agents-starter) project — a real-time, chat-based example application with tool-calling & human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest [wrangler v4](https://developers.cloudflare.com/changelog/2025-03-13-wrangler-v4/) release.

If you're new to Agents, you can install and run the `agents-starter` project in two commands:

```sh
# Install it
$ npm create cloudflare@latest agents-starter -- --template="cloudflare/agents-starter"
# Run it
$ npm run start
```

You can use the starter as a template for your own Agents projects: open up `src/server.ts` and `src/client.tsx` to see how the Agents SDK is used.

#### More documentation Updated

We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:

- Expanded [API reference documentation](https://developers.cloudflare.com/agents/runtime/), covering the methods and properties exposed by the Agents SDK, as well as more usage examples.
- More [Client API](https://developers.cloudflare.com/agents/runtime/agents-api/#client-api) documentation that documents `useAgent`, `useAgentChat` and the new `@unstable_callable` RPC decorator exposed by the SDK.
- New documentation on how to [route requests to agents](https://developers.cloudflare.com/agents/runtime/communication/routing/) and (optionally) authenticate clients before they connect to your Agents.

Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the `agents` package.

If you're still wondering what Agents are, [read our blog on building AI Agents on Cloudflare ↗︎](https://blog.cloudflare.com/build-ai-agents-on-cloudflare/) and/or visit the [Agents documentation](https://developers.cloudflare.com/agents/) to learn more.

Mar 18, 2025

[<h2>New API Posture Management for API Shield</h2>](https://developers.cloudflare.com/changelog/post/2025-03-18-api-posture-management/)

[API Shield](https://developers.cloudflare.com/api-shield/)

Now, API Shield **automatically** labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.

View these risks in [Endpoint Management](https://developers.cloudflare.com/api-shield/management-and-monitoring/) by label:

![A list of endpoint management labels](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2172,height=936,format=webp/_astro/endpoint-management-label.BDmf8Ai1.png)

...or in [Security Center Insights](https://developers.cloudflare.com/security/security-insights/):

![An example security center insight](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2250,height=1316,format=webp/_astro/posture-management-insight.7vB7mzGI.png)

API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:

- **cf-risk-sensitive**: applied if the customer is subscribed to the [sensitive data detection ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/) and the WAF detects sensitive data returned on an endpoint in the last seven days.
- **cf-risk-missing-auth**: applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.
- **cf-risk-mixed-auth**: applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.
- **cf-risk-missing-schema**: added when a learned schema is available for an endpoint that has no active schema.
- **cf-risk-error-anomaly**: added when an endpoint experiences a recent increase in response errors over the last 24 hours.
- **cf-risk-latency-anomaly**: added when an endpoint experiences a recent increase in response latency over the last 24 hours.
- **cf-risk-size-anomaly**: added when an endpoint experiences a spike in response body size over the last 24 hours.

In addition, API Shield has two new 'beta' scans for **Broken Object Level Authorization (BOLA) attacks**. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:

- **cf-risk-bola-enumeration**: added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.
- **cf-risk-bola-pollution**: added when an endpoint experiences successful responses where parameters are found in multiple places in the request.

We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.

Refer to the [blog post ↗︎](https://blog.cloudflare.com/cloudflare-security-posture-management/) for more information about Cloudflare's expanded posture management capabilities.

Mar 18, 2025

[<h2>Leaked Credentials Insights in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its security insights, providing visibility into aggregate trends in authentication requests, including the detection of leaked credentials through [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) scans.

We have now introduced the following endpoints:

- [`/leaked_credential_checks/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/): Retrieves summaries of HTTP authentication requests distribution across two different dimensions.
- [`/leaked_credential_checks/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/): Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.

The following dimensions are available, displaying the distribution of HTTP authentication requests based on:

- `compromised`: Credential status (clean vs. compromised).
- `bot_class`: [Bot class](https://developers.cloudflare.com/radar/concepts/bot-classes) (human vs. bot).

Dive deeper into leaked credential detection in this [blog post ↗︎](https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/) and learn more about the expanded Radar security insights in our [blog post ↗︎](https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots).

Mar 17, 2025

[<h2>Cloudflare One Agent for Android (version 2.4)</h2>](https://developers.cloudflare.com/changelog/post/2025-03-17-warp-ga-android/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Android Cloudflare One Agent is now available in the [Google Play Store ↗︎](https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent). This release includes a new feature allowing [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url) during enrollment, as well as fixes and minor improvements.

**Changes and improvements**

- Improved in-app error messages.
- Improved mobile client login with support for [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url).
- Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.

Mar 17, 2025

[<h2>Cloudflare One Agent for iOS (version 1.10)</h2>](https://developers.cloudflare.com/changelog/post/2025-03-17-warp-ga-ios/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release includes a new feature allowing [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url) during enrollment, as well as fixes and minor improvements.

**Changes and improvements**

- Improved in-app error messages.
- Improved mobile client login with support for [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url).
- Bug fixes and performance improvements.

Mar 17, 2025

[<h2>WAF Release - 2025-03-17</h2>](https://developers.cloudflare.com/changelog/post/2025-03-17-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...e59ec18a | 100725 | Fortinet FortiManager - Remote Code Execution - CVE:CVE-2023-42791, CVE:CVE-2024-23666 | Log | Block | |
| Cloudflare Managed Ruleset | ...1dbf58df | 100726 | Ivanti - Remote Code Execution - CVE:CVE-2024-8190 | Log | Block | |
| Cloudflare Managed Ruleset | ...0ad61fa7 | 100727 | Cisco IOS XE - Remote Code Execution - CVE:CVE-2023-20198 | Log | Disabled | Fixed action value in changelog; no rule changes. |
| Cloudflare Managed Ruleset | ...7ee56b66 | 100728 | Sitecore - Remote Code Execution - CVE:CVE-2024-46938 | Log | Block | |
| Cloudflare Managed Ruleset | ...a6752a38 | 100729 | Microsoft SharePoint - Remote Code Execution - CVE:CVE-2023-33160 | Log | Block | |
| Cloudflare Managed Ruleset | ...98d47b69 | 100730 | Pentaho - Template Injection - CVE:CVE-2022-43769, CVE:CVE-2022-43939 | Log | Block | |
| Cloudflare Managed Ruleset | ...69fe1e0d | 100700 | Apache SSRF vulnerability CVE-2021-40438 | N/A | Block | |

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/48/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/48/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
