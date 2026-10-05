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

Sep 9, 2025

[<h2>Deploy static sites to Workers without a configuration file</h2>](https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/)

[Workers](https://developers.cloudflare.com/workers/)

Deploying static site to Workers is now easier. When you run `wrangler deploy [directory]` or `wrangler deploy --assets [directory]` without an existing [configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) now guides you through the deployment process with interactive prompts.

#### Before and after

**Before:** Required remembering multiple flags and parameters

```bash
wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project
```

**After:** Simple directory deployment with guided setup

```bash
wrangler deploy dist
# Interactive prompts handle the rest as shown in the example flow below
```

#### What's new

**Interactive prompts for missing configuration:**

- Wrangler detects when you're trying to deploy a directory of static assets
- Prompts you to confirm the deployment type
- Asks for a project name (with smart defaults)
- Automatically sets the compatibility date to today

**Automatic configuration generation:**

- Creates a `wrangler.jsonc` file with your deployment settings
- Stores your choices for future deployments
- Eliminates the need to remember complex command-line flags

#### Example workflow

```bash
# Deploy your built static site
wrangler deploy dist

# Wrangler will prompt:
✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes
✔ What do you want to name your project? … my-astro-site

# Automatically generates a wrangler.jsonc file and adds it to your project:
{
  "name": "my-astro-site",
  "compatibility_date": "2025-09-09",
  "assets": {
    "directory": "dist"
  }
}

# Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file
wrangler deploy
```

#### Requirements

- You must use Wrangler version 4.24.4 or later in order to use this feature

Sep 8, 2025

[<h2>Custom IKE ID for IPsec Tunnels</h2>](https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.

This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the [Custom IKE ID feature and the API call to configure it](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/).

Sep 8, 2025

[<h2>Reminders about two-factor authentication backup codes</h2>](https://developers.cloudflare.com/changelog/post/2025-09-08-reminders-about-two-factor-authentication-backup-codes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Two-factor authentication is the best way to help protect your account from account takeovers, but if you lose your second factor, you could be locked out of your account. Lock outs are one of the top reasons customers contact Cloudflare support, and our policies often don't allow us to bypass two-factor authentication for customers that are locked out. Today we are releasing an improvement where Cloudflare will periodically remind you to securely save your backup codes so you don't get locked out in the future.

#### For more information

- [Two-factor authentication](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/)

Sep 8, 2025

[<h2>WAF Release - 2025-09-08</h2>](https://developers.cloudflare.com/changelog/post/2025-09-08-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week’s focus highlights newly disclosed vulnerabilities in web frameworks, enterprise applications, and widely deployed CMS plugins. The vulnerabilities include SSRF, authentication bypass, arbitrary file upload, and remote code execution (RCE), exposing organizations to high-impact risks such as unauthorized access, system compromise, and potential data exposure. In addition, security rule enhancements have been deployed to cover general command injection and server-side injection attacks, further strengthening protections.

**Key Findings**

- Next.js (CVE-2025-57822): Improper handling of redirects in custom middleware can lead to server-side request forgery (SSRF) when user-supplied headers are forwarded. Attackers could exploit this to access internal services or cloud metadata endpoints. The issue has been resolved in versions 14.2.32 and 15.4.7. Developers using custom middleware should upgrade and verify proper redirect handling in `next()` calls.
- ScriptCase (CVE-2025-47227, CVE-2025-47228): In the Production Environment extension in Netmake ScriptCase through 9.12.006 (23), two vulnerabilities allow attackers to reset admin accounts and execute system commands, potentially leading to full compromise of affected deployments.
- Sar2HTML (CVE-2025-34030): In Sar2HTML version 3.2.2 and earlier, insufficient input sanitization of the plot parameter allows remote, unauthenticated attackers to execute arbitrary system commands. Exploitation could compromise the underlying server and its data.
- Zhiyuan OA (CVE-2025-34040): An arbitrary file upload vulnerability exists in the Zhiyuan OA platform. Improper validation in the `wpsAssistServlet` interface allows unauthenticated attackers to upload crafted files via path traversal, which can be executed on the web server, leading to remote code execution.
- WordPress:Plugin:InfiniteWP Client (CVE-2020-8772): A vulnerability in the InfiniteWP Client plugin allows attackers to perform restricted actions and gain administrative control of connected WordPress sites.

**Impact**

These vulnerabilities could allow attackers to gain unauthorized access, execute malicious code, or take full control of affected systems. The Next.js SSRF flaw may expose internal services or cloud metadata endpoints to attackers. Exploitations of ScriptCase and Sar2HTML could result in remote code execution, administrative takeover, and full server compromise. In Zhiyuan OA, the arbitrary file upload vulnerability allows attackers to execute malicious code on the web server, potentially exposing sensitive data and applications. The authentication bypass in WordPress InfiniteWP Client enables attackers to gain administrative access, risking data exposure and unauthorized control of connected sites.

Administrators are strongly advised to apply vendor patches immediately, remove unsupported software, and review authentication and access controls to mitigate these risks.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...963d7afc | 100007D | Command Injection - Common Attack Commands Args | Log | Block | This rule has been merged into the original rule "Command Injection - Common Attack Commands" (ID: ...28345b9b) for New WAF customers only. |
| Cloudflare Managed Ruleset | ...8230a75b | 100617 | Next.js - SSRF - CVE:CVE-2025-57822 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...a22dabf1 | 100659\_BETA | Common Payloads for Server-Side Template Injection - Beta | Log | Block | This rule is merged into the original rule "Common Payloads for Server-Side Template Injection" (ID: ...a28a42c4) |
| Cloudflare Managed Ruleset | ...b416b7ca | 100824B | CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 3 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5db1fa6b | 100848 | ScriptCase - Auth Bypass - CVE:CVE-2025-47227 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2c62d330 | 100849 | ScriptCase - Command Injection - CVE:CVE-2025-47228 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...ef971afd | 100872 | WordPress:Plugin:InfiniteWP Client - Missing Authorization - CVE:CVE-2020-8772 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...bab19b0b | 100873 | Sar2HTML - Command Injection - CVE:CVE-2025-34030 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...f24c0fbe | 100875 | Zhiyuan OA - Remote Code Execution - CVE:CVE-2025-34040 | Log | Block | This is a New Detection |

Sep 5, 2025

[<h2>Bidirectional tunnel health checks are compatible with all Magic on-ramps</h2>](https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.

Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.

There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.

Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.

Sep 5, 2025

[<h2>Introducing EmbeddingGemma from Google on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We're excited to be a launch partner alongside [Google ↗︎](https://developers.googleblog.com/en/introducing-embeddinggemma/) to bring their newest embedding model, **EmbeddingGemma**, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.

[`@cf/google/embeddinggemma-300m`](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/) is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.

**Using EmbeddingGemma in AI Search:** Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.

To use EmbeddingGemma for your AI Search projects:

1. Go to **Create** in the [AI Search dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
2. Follow the setup flow for your new RAG instance
3. In the **Generate Index** step, open up **More embedding models** and select `@cf/google/embeddinggemma-300m` as your embedding model
4. Complete the setup to create an AI Search

Try it out and let us know what you think!

Sep 4, 2025

[<h2>WAF Release - 2025-09-04 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-09-04-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week, new critical vulnerabilities were disclosed in Sitecore’s Sitecore Experience Manager (XM), Sitecore Experience Platform (XP), specifically versions 9.0 through 9.3, and 10.0 through 10.4. These flaws are caused by unsafe data deserialization and code reflection, leaving affected systems at high risk of exploitation.

**Key Findings**

- CVE-2025-53690: Remote Code Execution through Insecure Deserialization
- CVE-2025-53691: Remote Code Execution through Insecure Deserialization
- CVE-2025-53693: HTML Cache Poisoning through Unsafe Reflections

**Impact**

Exploitation could allow attackers to execute arbitrary code remotely on the affected system and conduct cache poisoning attacks, potentially leading to further compromise. Applying the latest vendor-released solution without delay is strongly recommended.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...0ee2c15e | 100878 | Sitecore - Remote Code Execution - CVE:CVE-2025-53691 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...7c5b669c | 100631 | Sitecore - Cache Poisoning - CVE:CVE-2025-53693 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...6c410240 | 100879 | Sitecore - Remote Code Execution - CVE:CVE-2025-53690 | N/A | Block | This is a new detection |

Sep 4, 2025

[<h2>Increased static asset limits for Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/)

[Workers](https://developers.cloudflare.com/workers/) [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

You can now upload up to **100,000 static assets** per Worker version

- Paid and Workers for Platforms users can now upload up to **100,000 static assets** per Worker version, a 5x increase from the previous limit of 20,000.
- Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker
- The individual file size limit of 25 MiB remains unchanged for all customers.

This increase allows you to build larger applications with more static assets without hitting limits.

#### Wrangler

To take advantage of the increased limits, you must use **Wrangler version 4.34.0 or higher**. Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.

#### Learn more

For more information about Workers static assets, see the [Static Assets documentation](https://developers.cloudflare.com/workers/static-assets/) and [Platform Limits](https://developers.cloudflare.com/workers/platform/limits/#static-assets).

Sep 4, 2025

[<h2>A new, simpler REST API for Cloudflare Workers (Beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-09-03-new-workers-api/)

[Workers](https://developers.cloudflare.com/workers/)

You can now manage [**Workers**](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/create/), [**Versions**](<https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)>), and [**Deployments**](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/update/) as separate resources with a new, resource-oriented API (Beta).

This new API is supported in the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) and the [Cloudflare Typescript SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript), allowing platform teams to manage a Worker's infrastructure in Terraform, while development teams handle code deployments from a separate repository or workflow. We also designed this API with AI agents in mind, as a clear, predictable structure is essential for them to reliably build, test, and deploy applications.

#### Try it out

- [**New beta API endpoints**](https://developers.cloudflare.com/api/resources/workers/subresources/beta/)
- [**Cloudflare TypeScript SDK v5.0.0** ↗︎](https://github.com/cloudflare/cloudflare-typescript)
- [**Cloudflare Go SDK v6.0.0** ↗︎](https://github.com/cloudflare/cloudflare-go)
- [**Terraform provider v5.9.0** ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs): [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) , [`cloudflare_worker_version` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version), and [`cloudflare_workers_deployments` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_deployment) resources.
- See full examples in our [Infrastructure as Code (IaC) guide](https://developers.cloudflare.com/workers/platform/infrastructure-as-code)

#### Before: Eight+ endpoints with mixed responsibilities

![Before](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=7360,height=6176,format=webp/_astro/api-before.VkE1i-Rj.png)

The existing API was originally designed for simple, one-shot script uploads:

```sh
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME" \
    -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    -H "X-Auth-Key: $CLOUDFLARE_API_KEY" \
    -H "Content-Type: multipart/form-data" \
    -F 'metadata={
      "main_module": "worker.js",
      "compatibility_date": "$today$"
    }' \
    -F "worker.js=@worker.js;type=application/javascript+module"
```

This API worked for creating a basic Worker, uploading all of its code, and deploying it immediately — but came with challenges:

- **A Worker couldn't exist without code**: To create a Worker, you had to upload its code in the same API request. This meant platform teams couldn't provision Workers with the proper settings, and then hand them off to development teams to deploy the actual code.
- **Several endpoints implicitly created deployments**: Simple updates like adding a secret or changing a script's content would implicitly create a new version and immediately deploy it.
- **Updating a setting was confusing**: Configuration was scattered across eight endpoints with overlapping responsibilities. This ambiguity made it difficult for human developers (and even more so for AI agents) to reliably update a Worker via API.
- **Scripts used names as primary identifiers**: This meant simple renames could turn into a risky migration, requiring you to create a brand new Worker and update every reference. If you were using Terraform, this could inadvertently destroy your Worker altogether.

#### After: Three resources with clear boundaries

![After](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=7360,height=4680,format=webp/_astro/api-after.J8u2vIcT.png) The new API introduces cleaner resource management with three core resources: [**Worker**](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/create/), [**Versions**](<https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)>), and [**Deployment**](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/update/).

All endpoints now use simple JSON payloads, with script content embedded as `base64`-encoded strings -- a more consistent and reliable approach than the previous `multipart/form-data` format.

- **Worker**: The parent resource representing your application. It has a stable UUID and holds persistent settings like `name`, `tags`, and `logpush`. You can now create a Worker to establish its identity and settings **before** any code is uploaded.
- **Version**: An immutable snapshot of your code and its specific configuration, like bindings and `compatibility_date`. Creating a new version is a safe action that doesn't affect live traffic.
- **Deployment**: An explicit action that directs traffic to a specific version.

Note

[Workers](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/) and [Versions](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) use the new `/workers/` beta endpoints, while [Deployments](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/) remain on the existing `/scripts/` endpoint. Pair the new endpoints with the existing Deployment API for a complete workflow.

#### Why this matters

#### You can now create Workers before uploading code

Workers are now standalone resources that can be created and configured without any code. Platform teams can provision Workers with the right settings, then hand them off to development teams for implementation.

#### Example: Typescript SDK

```ts
// Step 1: Platform team creates the Worker resource (no code needed)
const worker = await client.workers.beta.workers.create({
  name: "payment-service",
  account_id: "...",
  observability: {
    enabled: true,
  },
});

// Step 2: Development team adds code and creates a version later
const version = await client.workers.beta.workers.versions.create(worker.id, {
  account_id: "...",
  main_module: "worker.js",
  compatibility_date: "$today",
  bindings: [ /*...*/ ],
  modules: [
    {
      name: "worker.js",
      content_type: "application/javascript+module",
      content_base64: Buffer.from(scriptContent).toString("base64"),
    },
  ],
});

// Step 3: Deploy explicitly when ready
const deployment = await client.workers.scripts.deployments.create(worker.name, {
  account_id: "...",
  strategy: "percentage",
  versions: [
    {
      percentage: 100,
      version_id: version.id,
    },
  ],
});
```

#### Example: Terraform

If you use Terraform, you can now declare the Worker in your Terraform configuration and manage configuration outside of Terraform in your Worker's [`wrangler.jsonc` file](https://developers.cloudflare.com/workers/wrangler/configuration/) and deploy code changes using [Wrangler](https://developers.cloudflare.com/workers/wrangler/).

```tf
resource "cloudflare_worker" "my_worker" {
  account_id = "..."
  name = "my-important-service"
}
# Manage Versions and Deployments here or outside of Terraform
# resource "cloudflare_worker_version" "my_worker_version" {}
# resource "cloudflare_workers_deployment" "my_worker_deployment" {}
```

#### Deployments are always explicit, never implicit

Creating a version and deploying it are now always explicit, separate actions - never implicit side effects. To update version-specific settings (like bindings), you create a new version with those changes. The existing deployed version remains unchanged until you explicitly deploy the new one.

```sh
# Step 1: Create a new version with updated settings (doesn't affect live traffic)
POST /workers/workers/{id}/versions
{
  "compatibility_date": "$today",
  "bindings": [
    {
      "name": "MY_NEW_ENV_VAR",
      "text": "new_value",
      "type": "plain_text"
    }
  ],
  "modules": [...]
}

# Step 2: Explicitly deploy when ready (now affects live traffic)
POST /workers/scripts/{script_name}/deployments
{
  "strategy": "percentage",
  "versions": [
    {
      "percentage": 100,
      "version_id": "new_version_id"
    }
  ]
}
```

#### Settings are clearly organized by scope

Configuration is now logically divided: [**Worker settings**](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/) (like `name` and `tags`) persist across all versions, while [**Version settings**](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) (like `bindings` and `compatibility_date`) are specific to each code snapshot.

```sh
# Worker settings (the parent resource)
PUT /workers/workers/{id}
{
  "name": "payment-service",
  "tags": ["production"],
  "logpush": true,
}
```

```sh
# Version settings (the "code")
POST /workers/workers/{id}/versions
{
  "compatibility_date": "$today",
  "bindings": [...],
  "modules": [...]
}
```

#### `/workers` API endpoints now support UUIDs (in addition to names)

The `/workers/workers/` path now supports addressing a Worker by both its immutable UUID and its mutable name.

```sh
# Both work for the same Worker
GET /workers/workers/29494978e03748669e8effb243cf2515  # UUID (stable for automation)
GET /workers/workers/payment-service                  # Name (convenient for humans)
```

This dual approach means:

- Developers can use readable names for debugging.
- Automation can rely on stable UUIDs to prevent errors when Workers are renamed.
- Terraform can rename Workers without destroying and recreating them.

#### Learn more

- [Infrastructure as Code (IaC) guide](https://developers.cloudflare.com/workers/platform/infrastructure-as-code)
- [API documentation](https://developers.cloudflare.com/api/resources/workers/subresources/beta/)
- [Versions and Deployments overview](https://developers.cloudflare.com/workers/versions-and-deployments/)

#### Technical notes

- The pre-existing Workers REST API remains fully supported. Once the new API exits beta, we'll provide a migration timeline with ample notice and comprehensive migration guides.
- Existing Terraform resources and SDK methods will continue to be fully supported through the current major version.
- While the Deployments API currently remains on the `/scripts/` endpoint, we plan to introduce a new Deployments endpoint under `/workers/` to match the new API structure.

Sep 3, 2025

[<h2>Introducing new headers for rate limiting on Cloudflare's API</h2>](https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare's API now supports rate limiting headers using the pattern developed by the [IETF draft on rate limiting ↗︎](https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html). This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.

Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.

As always, if you need any help with rate limits, please contact Support.

#### Changes

#### New Headers

**Headers that are always returned:**

- `Ratelimit`: List of service limit items, composed of the limit name, the remaining quota ( `r`) and the time next window resets ( `t`). For example: `"default";r=50;t=30`
- `Ratelimit-Policy`: List of quota policy items, composed of the policy name, the total quota ( `q`) and the time window the quota applies to ( `w`). For example: `"burst";q=100;w=60`

**Returned only when a rate limit has been reached (error code: 429):**

- Retry-After: Number of Seconds until more capacity is available, rounded up

#### SDK Back offs

- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached.

#### GraphQL and Edge APIs

These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL.

#### For more information

- [Rate limits at Cloudflare ↗︎](https://developers.cloudflare.com/fundamentals/api/reference/limits/)

Sep 3, 2025

[<h2>Logging headers and cookies using custom fields</h2>](https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) now supports logging and filtering on header or cookie fields in the [`http_requests` dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/).

Create a custom field to log desired header or cookie values into the `http_requests` dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.

![Edit Custom fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1790,height=404,format=webp/_astro/edit-custom-fields.Cy4qXSpL.png)

For more details, refer to [Headers and cookies](https://developers.cloudflare.com/log-explorer/log-search/#headers-and-cookies).

Sep 2, 2025

[<h2>Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</h2>](https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting **December 1, 2025**, list endpoints for the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.

No action is required if you already explicitly set `is_deleted=false` or if you only need to list active resources.

This change affects the following API endpoints:

- List all tunnels: [`GET /accounts/{account_id}/tunnels`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list/)
- List [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/): [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/)
- List [WARP Connector](https://developers.cloudflare.com/mesh/) tunnels: [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/)
- List tunnel routes: [`GET /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/)
- List subnets: [`GET /accounts/{account_id}/zerotrust/subnets`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/)
- List virtual networks: [`GET /accounts/{account_id}/teamnet/virtual_networks`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/)

#### What is changing?

The default behavior of the `is_deleted` query parameter will be updated.

| Scenario | Previous behavior (before December 1, 2025) | New behavior (from December 1, 2025) |
| --- | --- | --- |
| `is_deleted` parameter is omitted | Returns **active & deleted** tunnels, routes, subnets and virtual networks | Returns **only active** tunnels, routes, subnets and virtual networks |

#### Action required

If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the `is_deleted` parameter before **December 1, 2025**.

To get a list of only deleted resources, you must now explicitly add the `is_deleted=true` query parameter to your request:

```bash
# Example: Get ONLY deleted Tunnels
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true" \
     -H "Authorization: Bearer $API_TOKEN"

# Example: Get ONLY deleted Virtual Networks
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true" \
     -H "Authorization: Bearer $API_TOKEN"
```

Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using `is_deleted=false`) and one to get deleted items (`is_deleted=true`).

#### Why we’re making this change

This update is based on user feedback and aims to:

- **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
- **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
- **Improve performance:** For most users, the default query result will now be smaller and more relevant.

To learn more, please visit the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) documentation.

Sep 1, 2025

[<h2>Updated Email security roles</h2>](https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

To provide more granular controls, we refined the [existing roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#email-security-roles) for Email security and launched a new Email security role as well.

All Email security roles no longer have read or write access to any of the other Zero Trust products:

- **Email Configuration Admin**
- **Email Integration Admin**
- **Email security Read Only**
- **Email security Analyst**
- **Email security Policy Admin**
- **Email security Reporting**

To configure [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) or [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation), you now need to be an admin for the Zero Trust dashboard with the **Cloudflare Zero Trust** role.

Also through customer feedback, we have created a new additive role to allow **Email security Analyst** to create, edit, and delete Email security policies, without needing to provide access via the **Email Configuration Admin** role. This role is called **Email security Policy Admin**, which can read all settings, but has write access to [allow policies](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/), and [blocked senders](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Sep 1, 2025

[<h2>WAF Release - 2025-09-01</h2>](https://developers.cloudflare.com/changelog/post/2025-09-01-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week, a critical vulnerability was disclosed in Fortinet FortiWeb (versions 7.6.3 and below, versions 7.4.7 and below, versions 7.2.10 and below, and versions 7.0.10 and below), linked to improper parameter handling that could allow unauthorized access.

**Key Findings**

- Fortinet FortiWeb (CVE-2025-52970): A vulnerability may allow an unauthenticated remote attacker with access to non-public information to log in as any existing user on the device via a specially crafted request.

**Impact**

Exploitation could allow an unauthenticated attacker to impersonate any existing user on the device, potentially enabling them to modify system settings or exfiltrate sensitive information, posing a serious security risk. Upgrading to the latest vendor-released version is strongly recommended.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c49b7cf8 | 100586 | Fortinet FortiWeb - Auth Bypass - CVE:CVE-2025-52970 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...790c9dde | 100136C | XSS - JavaScript - Headers and Body | N/A | N/A | Rule metadata description refined. Detection unchanged. |

Aug 29, 2025

[<h2>Smart Tiered Cache Fallback to Generic</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

[Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#smart-tiered-cache) now falls back to [Generic Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) when the origin location cannot be determined, improving cache precision for your content.

Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.

#### How it works

When Smart Tiered Cache falls back to Generic Tiered Cache:

1. **Multiple upper-tiers**: Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.
2. **Distributed cache requests**: Lower-tier data centers can query any available upper-tier for cached content.
3. **Improved global coverage**: Provides better cache hit ratios across geographically distributed visitors.
4. **Automatic fallback**: Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.

#### Benefits

- **Preserves high performance during fallback**: Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.
- **Minimizes latency impact**: Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.
- **Seamless experience**: No configuration changes or intervention required when fallback occurs.
- **Improved resilience**: Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.

#### Get started

This improvement is automatically applied to all zones using [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/). No action is required on your part.

Aug 29, 2025

[<h2>Cloudflare One WARP Diagnostic AI Analyzer</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-warp-AI-diag-analyzer/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

We're excited to share a new AI feature, the [WARP diagnostic analyzer ↗︎](https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/), to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the [Cloudflare One dashboard ↗︎](https://dash.cloudflare.com/one/) to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing [remote captures](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture) of [WARP diagnostic logs](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs). The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to [WARP diagnostics analyzer (beta)](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta) to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.

Aug 29, 2025

[<h2>DEX MCP Server</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-dex-mcp-server/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device connectivity and performance across your Cloudflare SASE deployment.

We've released an MCP server [(Model Context Protocol) ↗︎](https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) for DEX.

The DEX MCP server is an AI tool that allows customers to ask a question like, "Show me the connectivity and performance metrics for the device used by carly‌@acme.com", and receive an answer that contains data from the DEX API.

Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.

Customers can test the new DEX MCP server in less than one minute. To learn more, read the [DEX MCP server documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/dex-mcp-server/).

Aug 29, 2025

[<h2>Terraform v5.9 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-terrform-v5.9-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

This release includes a new resource, `cloudflare_snippet`, which replaces `cloudflare_snippets`. `cloudflare_snippet` is now considered deprecated but can still be used. Please utilize `cloudflare_snippet` as soon as possible.

#### Changes

- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes

For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0) in GitHub.

#### Issues Closed

- [#5921: In cloudflare\_ruleset removing an existing rule causes recreation of later rules ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare\_zero\_trust\_access\_application is not idempotent ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare\_workers\_script) Durable Object migrations not applied ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare\_workers\_script secret\_text environment variable gets replaced on every deploy ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare\_zone suddenly started showing drift ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare\_zero\_trust\_list always marked for change due to read only attributes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare\_zero\_trust\_gateway\_certificate unable to manage resource (cant mark as active/inactive) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare\_dns\_records is always updated in-place ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare\_zero\_trust\_gateway\_policy after upgrade to V5 provider & also setting expiration fails ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare\_zero\_trust\_access\_application ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare\_zone\_setting inconsistent value of "editable" upon apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare\_zero\_trust\_access\_policies" data source ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare\_zero\_trust\_access\_application type warp diff on every apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare\_zone\_dnssec fails with HTTP/400 "Malformed request body" ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare\_ruleset http\_request\_cache\_settings bypass mismatch between dashboard and terraform ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare\_account\_member invalid type 'string' for field 'roles' ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new issue if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [GitHub Repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare)

Aug 29, 2025

[<h2>WAF Release - 2025-08-29 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.

**Key Findings**

- CVE-2025-55173: Arbitrary file download from the server via image optimization.
- CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.

**Impact**

Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...9ff4bfe3 | 100613 | Next.js - Dangerous File Download - CVE:CVE-2025-55173 | N/A | Block | This is a new detection |
| Cloudflare Managed Ruleset | ...69b9ea7d | 100616 | Next.js - Information Disclosure - CVE:CVE-2025-57752 | N/A | Block | This is a new detection |

Aug 27, 2025

[<h2>Enhanced crawler insights and custom 402 responses</h2>](https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.

**Enhanced Crawlers tab:**

- View total allowed and blocked requests for each AI crawler
- Trend charts show crawler activity over your selected time range per crawler

![Updated AI Crawl Control table showing request counts and trend charts](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1335,height=984,format=webp/_astro/ai-crawl-control-table.BDr0Qd-5.png)

**Custom block responses (paid plans):** You can now return HTTP 402 "Payment Required" responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.

For users on paid plans, when blocking AI crawlers you can configure:

- **Response code:** Choose between 403 Forbidden or 402 Payment Required
- **Response body:** Add a custom message with your licensing contact information

![AI Crawl Control block response configuration interface](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1327,height=419,format=webp/_astro/ai-crawl-control-block-response.L4duQj7-.png)

Example 402 response:

```http
HTTP 402 Payment Required
Date: Mon, 24 Aug 2025 12:56:49 GMT
Content-type: application/json
Server: cloudflare
Cf-Ray: 967e8da599d0c3fa-EWR
Cf-Team: 2902f6db750000c3fa1e2ef400000001

{
  "message": "Please contact the site owner for access."
}
```

Aug 27, 2025

[<h2>Shadow IT - SaaS analytics dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-08-27-shadow-it-analytics/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust has significantly upgraded its **Shadow IT analytics**, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.

You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including **Unreviewed**, **In Review**, **Approved**, and **Unapproved** designating how they can be used in your organization.

![Cloudflare One Analytics Dashboards](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2814,height=1486,format=webp/_astro/shadow-it-analytics.BLNnG72w.png)

These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.

Both the analytics and policies are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

Aug 27, 2025

[<h2>Deepgram and Leonardo partner models now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2025-08-27-partner-models/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

New state-of-the-art models have landed on Workers AI! This time, we're introducing new **partner models** trained by our friends at [Deepgram ↗︎](https://deepgram.com) and [Leonardo ↗︎](https://leonardo.ai), hosted on Workers AI infrastructure.

As well, we're introuding a new turn detection model that enables you to detect when someone is done speaking — useful for building voice agents!

Read the [blog ↗︎](https://blog.cloudflare.com/workers-ai-partner-models) for more details and check out some of the new models on our platform:

- [`@cf/deepgram/aura-1`](https://developers.cloudflare.com/workers-ai/models/aura-1) is a text-to-speech model that allows you to input text and have it come to life in a customizable voice
- [`@cf/deepgram/nova-3`](https://developers.cloudflare.com/workers-ai/models/nova-3) is speech-to-text model that transcribes multilingual audio at a blazingly fast speed
- [`@cf/pipecat-ai/smart-turn-v2`](https://developers.cloudflare.com/workers-ai/models/smart-turn-v2) helps you detect when someone is done speaking
- [`@cf/leonardo/lucid-origin`](https://developers.cloudflare.com/workers-ai/models/lucid-origin) is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction
- [`@cf/leonardo/phoenix-1.0`](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0) is a text-to-image model with exceptional prompt adherence and coherent text

You can filter out new partner models with the `Partner` capability on our [Models](https://developers.cloudflare.com/workers-ai/models) page.

As well, we're introducing WebSocket support for some of our audio models, which you can filter though the `Realtime` capability on our [Models](https://developers.cloudflare.com/workers-ai/models) page. WebSockets allows you to create a bi-directional connection to our inference server with low latency — perfect for those that are building voice agents.

An example python snippet on how to use WebSockets with our new Aura model:

```plaintext
import json
import os
import asyncio
import websockets

uri = f"wss://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/deepgram/aura-1"

input = [
    "Line one, out of three lines that will be provided to the aura model.",
    "Line two, out of three lines that will be provided to the aura model.",
    "Line three, out of three lines that will be provided to the aura model. This is a last line.",
]


async def text_to_speech():
    async with websockets.connect(uri, additional_headers={"Authorization": os.getenv("CF_TOKEN")}) as websocket:
        print("connection established")
        for line in input:
            print(f"sending `{line}`")
            await websocket.send(json.dumps({"type": "Speak", "text": line}))

            print("line was sent, flushing")
            await websocket.send(json.dumps({"type": "Flush"}))
            print("flushed, recving")
            resp = await websocket.recv()
            print(f"response received {resp}")


if __name__ == "__main__":
    asyncio.run(text_to_speech())
```

Aug 26, 2025

[<h2>New CASB integrations for ChatGPT, Claude, and Gemini</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-casb-ai-integrations/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB ↗︎](https://www.cloudflare.com/zero-trust/products/casb/) now supports three of the most widely used GenAI platforms — **OpenAI ChatGPT**, **Anthropic Claude**, and **Google Gemini**. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.

![Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2335,height=1776,format=webp/_astro/casb-ai-integrations-preview.B-zsSA1P.png)

#### Key capabilities

- **Agentless connections** — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required
- **Posture management** — detect insecure settings and misconfigurations that could lead to data exposure
- **DLP detection** — identify sensitive data in uploaded chat attachments or files
- **GenAI-specific insights** — surface risks unique to each provider’s capabilities

#### Learn more

- [ChatGPT integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/)
- [Claude integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/)
- [Gemini integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/)

These integrations are available to all Cloudflare One customers today.

Aug 26, 2025

[<h2>Manage and restrict access to internal MCP servers with Cloudflare Access</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

[Self-hosted applications](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/linked-apps/) in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.

For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the [blog post ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) on the Cloudflare Blog.

Aug 26, 2025

[<h2>MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

![MCP server portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1557,height=420,format=webp/_astro/mcp-server-portal.BOKqTCoI.png)

An [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:

- **Streamlined access to multiple MCP servers**: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.
- **Customized tools per portal**: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.
- **Observability**: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.

This is available in an open beta for all customers across all plans! For more information check out our [blog ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) for this release.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/39/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/39/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
