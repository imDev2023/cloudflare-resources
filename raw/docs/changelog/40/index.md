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

Aug 26, 2025

[<h2>List all vectors in a Vectorize index with the new list-vectors operation</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now list all vector identifiers in a Vectorize index using the new `list-vectors` operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.

The operation is available via Wrangler CLI and REST API. Refer to the [list-vectors best practices guide](https://developers.cloudflare.com/vectorize/best-practices/list-vectors/) for detailed usage guidance.

Aug 25, 2025

[<h2>Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</h2>](https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/)

[Secrets Store](https://developers.cloudflare.com/secrets-store/) [AI Gateway](https://developers.cloudflare.com/ai-gateway/) [SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through [Bring Your Own Key ↗︎](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.

You can now create a secret directly from your AI Gateway [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/ai-gateway) by navigating into your gateway -> **Provider Keys** -> **Add**.

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1842,format=webp/_astro/add-secret-ai-gateway.B-SIPr6s.png)

You can also create your secret with the newly available **ai\_gateway** scope via [wrangler ↗︎](https://developers.cloudflare.com/workers/wrangler/commands/), the [Secrets Store dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), or the [API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/).

Then, pass the key in the request header using its Secrets Store reference:

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic/v1/messages \
 --header 'cf-aig-authorization: ANTHROPIC_KEY_1 \
 --header 'anthropic-version: 2023-06-01' \
 --header 'Content-Type: application/json' \
 --data  '{"model": "claude-3-opus-20240229", "messages": [{"role": "user", "content": "What is Cloudflare?"}]}'
```

Or, using Javascript:

```plaintext
import Anthropic from '@anthropic-ai/sdk';


const anthropic = new Anthropic({
 apiKey: "ANTHROPIC_KEY_1",
 baseURL: "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic",
});


const message = await anthropic.messages.create({
 model: 'claude-3-opus-20240229',
 messages: [{role: "user", content: "What is Cloudflare?"}],
 max_tokens: 1024
});
```

For more information, check out the [blog ↗︎](https://blog.cloudflare.com/ai-gateway-aug-2025-refresh)!

Aug 25, 2025

[<h2>New DLP topic based detection entries for AI prompt protection</h2>](https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.

1. **Prompt Detection for AI Applications**

DLP can now natively detect and inspect user prompts submitted to popular AI applications, including **Google Gemini**, **ChatGPT**, **Claude**, and **Perplexity**.

2. **Prompt Analysis and Topic Classification**

Our DLP engine performs deep analysis on each prompt, applying [topic classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics). These topics are grouped into two evaluation categories:

- **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.
- **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.

To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=439,format=webp/_astro/ai-prompt-detection-entry.4QmdkAuv.png)

3. **Granular Guardrails**

   You can now build guardrails using Gateway HTTP policies with [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls). Apply a DLP profile containing an [AI prompt topic detection](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) to individual AI applications (for example, `ChatGPT`) and specific user actions (for example, `SendPrompt`) to block sensitive prompts.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=731,height=511,format=webp/_astro/ai-prompt-policy.CF3H2rbK.png)
4. **Full Prompt Logging**

   To aid in incident investigation, an optional setting in your Gateway policy allows you to [capture prompt logs](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content) to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by `conversation_id`, allowing you to reconstruct the full context of an interaction that led to a policy violation.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=444,format=webp/_astro/ai-prompt-log.ywQDc5qN.png)

AI prompt protection is now available in open beta. To learn more about it, read the [blog ↗︎](https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging) or refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

Aug 25, 2025

[<h2>WAF Release - 2025-08-25</h2>](https://developers.cloudflare.com/changelog/post/2025-08-25-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week, critical vulnerabilities were disclosed that impact widely used open-source infrastructure, creating high-risk scenarios for code execution and operational disruption.

**Key Findings**

- Apache HTTP Server – Code Execution (CVE-2024-38474): A flaw in Apache HTTP Server allows attackers to achieve remote code execution, enabling full compromise of affected servers. This vulnerability threatens the confidentiality, integrity, and availability of critical web services.
- Laravel (CVE-2024-55661): A security flaw in Laravel introduces the potential for remote code execution under specific conditions. Exploitation could provide attackers with unauthorized access to application logic and sensitive backend data.

**Impact**

These vulnerabilities pose severe risks to enterprise environments and open-source ecosystems. Remote code execution enables attackers to gain deep system access, steal data, disrupt services, and establish persistent footholds for broader intrusions. Given the widespread deployment of Apache HTTP Server and Laravel in production systems, timely patching and mitigation are critical.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...28050359 | 100822\_BETA | WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058 | N/A | Disabled | This was merged in to the original rule "WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058" (ID: ...194f7b2d) |
| Cloudflare Managed Ruleset | ...3bdcdbad | 100831 | Apache HTTP Server - Code Execution - CVE:CVE-2024-38474 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...02eaac5b | 100846 | Laravel - Remote Code Execution - CVE:CVE-2024-55661 | Log | Disabled | This is a New Detection |

Aug 25, 2025

[<h2>Content type returned in Workers Assets for Javascript files is now \`text/javascript\`</h2>](https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/)

[Workers](https://developers.cloudflare.com/workers/)

JavaScript asset responses have been updated to use the `text/javascript` Content-Type header instead of `application/javascript`. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends `text/javascript` as the preferred type going forward.

This change improves:

- Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.
- Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.
- Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.
- Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.

Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.

Users will see this change on the next deployment of their assets.

Aug 22, 2025

[<h2>Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance</h2>](https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/)

[KV](https://developers.cloudflare.com/kv/)

Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.

![Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1486,height=796,format=webp/_astro/kv-hybrid-providers-performance-improvements.D6MBO22S.png)

#### Performance improvements

The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:

- **p95 latency**: Reduced from \~150ms to \~50ms (67% decrease)
- **p99 latency**: Reduced from \~350ms to \~250ms (29% decrease)

Aug 22, 2025

[<h2>Audit logs (version 2) - Logpush Beta Release</h2>](https://developers.cloudflare.com/changelog/post/2025-08-22-audit-logs-v2-logpush/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

[Audit Logs v2 dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/) is now available via Logpush.

This expands on earlier releases of Audit Logs v2 in the [API](https://developers.cloudflare.com/changelog/2025-03-27-automatic-audit-logs-beta-release/) and [Dashboard UI](https://developers.cloudflare.com/changelog/2025-07-29-audit-logs-v2-ui-beta/).

We recommend creating a new Logpush job for the Audit Logs v2 dataset.

Timelines for General Availability (GA) of Audit Logs v2 and the retirement of Audit Logs v1 will be shared in upcoming updates.

For more details on Audit Logs v2, refer to the [Audit Logs documentation ↗︎](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

Aug 22, 2025

[<h2>Dedicated Egress IP for Logpush</h2>](https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with [Aegis IP](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/), your log destination only needs to allow Aegis IPs making setup more secure.

Highlights:

- Fixed egress IPs ensure your destination only accepts traffic from known addresses.
- Works with any supported Logpush destination.
- Recommended to use a dedicated zone as a proxy for easier management.

To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the [Logpush documentation](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/).

Aug 22, 2025

[<h2>WAF Release - 2025-08-22</h2>](https://developers.cloudflare.com/changelog/post/2025-08-22-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...5fcca5c8 | 100850 | Command Injection - Generic 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...744305c4 | 100851 | Remote Code Execution - Java Deserialization | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2b083459 | 100852 | Command Injection - Generic 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...efb7e5b9 | 100853 | Remote Code Execution - Common Bash Bypass Beta | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...78513ad7 | 100854 | XSS - Generic JavaScript | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...e9a5daac | 100855 | Command Injection - Generic 4 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...480f6093 | 100856 | PHP Object Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d4ae0a33 | 100857 | Generic - Parameter Fuzzing | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1121ee45 | 100858 | Code Injection - Generic 4 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...20de01e3 | 100859 | SQLi - UNION - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c0177e21 | 100860 | Command Injection - Generic 5 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...85f4d7b3 | 100861 | Command Execution - Generic | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3fa8ee7f | 100862 | GraphQL Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c7a41d4b | 100863 | Command Injection - Generic 6 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...65e3c165 | 100864 | Code Injection - Generic 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...161aafdc | 100865 | PHP Object Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1cc3c3f8 | 100866 | SQLi - LIKE 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...48ac2221 | 100867 | SQLi - DROP - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1f4eec13 | 100868 | Code Injection - Generic 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2755f99e | 100869 | Command Injection - Generic 7 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...413592e2 | 100870 | Command Injection - Generic 8 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d2dd41b5 | 100871 | SQLi - LIKE 3 | N/A | Disabled | This is a New Detection |

Aug 22, 2025

[<h2>Build durable multi-step applications in Python with Workflows (now in beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

You can now build [Workflows](https://developers.cloudflare.com/workflows/) using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the [Python Workers](https://developers.cloudflare.com/workers/languages/python/) runtime.

Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable [DAG (Directed Acyclic Graph) workflows](https://developers.cloudflare.com/workflows/python/dag/), where you can define complex dependencies between steps using the depends parameter.

Here’s a simple example:

```python
from workers import Response, WorkflowEntrypoint

class PythonWorkflowStarter(WorkflowEntrypoint):
    async def run(self, event, step):
        @step.do("my first step")
        async def my_first_step():
            # do some work
            return "Hello Python!"

        await my_first_step()

        await step.sleep("my-sleep-step", "10 seconds")

        @step.do("my second step")
        async def my_second_step():
            # do some more work
            return "Hello again!"

        await my_second_step()

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        await self.env.MY_WORKFLOW.create()
        return Response("Hello Workflow creation!")
```

Note

Python Workflows requires a `compatibility_date = "2025-08-01"`, or lower, in your wrangler toml file.

Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.

To learn more and get started, refer to [Python Workflows documentation](https://developers.cloudflare.com/workflows/python/).

Aug 21, 2025

[<h2>New getByName() API to access Durable Objects</h2>](https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

You can now create a client (a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/)) to a Durable Object with the new `getByName` method, removing the need to convert Durable Object names to IDs and then create a stub.

```js
// Before: (1) translate name to ID then (2) get a client 
const objectId = env.MY_DURABLE_OBJECT.idFromName("foo"); // or .newUniqueId()
const stub = env.MY_DURABLE_OBJECT.get(objectId); 

// Now: retrieve client to Durable Object directly via its name 
const stub = env.MY_DURABLE_OBJECT.getByName("foo");

// Use client to send request to the remote Durable Object
const rpcResponse = await stub.sayHello();
```

Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.

To learn more, visit the Durable Objects [API Documentation](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname) or the [getting started guide](https://developers.cloudflare.com/durable-objects/get-started/).

Aug 21, 2025

[<h2>Gateway BYOIP Dedicated Egress IPs now available.</h2>](https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.

Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.

Get started by following the [BYOIP onboarding process](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip). Once your IPs are onboarded, go to **Gateway** > **Egress policies** and select or create an egress policy. In **Select an egress IP**, choose *Use dedicated egress IPs (Cloudflare or BYOIP)*, then select your BYOIP address from the dropdown menu.

![Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=933,height=459,format=webp/_astro/Gateway-byoip-dedicated-egress-ips.D0pzLAbV.png)

For more information, refer to [BYOIP for dedicated egress IPs](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip).

Aug 19, 2025

[<h2>Subscribe to events from Cloudflare services with Queues</h2>](https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/)

[Queues](https://developers.cloudflare.com/queues/)

You can now subscribe to events from other Cloudflare services (for example, [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai), [Workers](https://developers.cloudflare.com/workers)) and consume those events via [Queues](https://developers.cloudflare.com/queues/), allowing you to build custom workflows, integrations, and logic in response to account activity.

![Event subscriptions architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=924,height=403,format=webp/_astro/queues-event-subscriptions.3aVidnXJ.png)

Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with [Workers](https://developers.cloudflare.com/workers/) or [pull via HTTP from anywhere](https://developers.cloudflare.com/queues/configuration/pull-consumers/).

To create a subscription, use the dashboard or [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/queues/#queues-subscription-create):

```bash
npx wrangler queues subscription create my-queue --source r2 --events bucket.created
```

An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:

*Example R2 bucket created eventjson*

```json
{
  "type": "cf.r2.bucket.created",
  "source": {
    "type": "r2"
  },
  "payload": {
    "name": "my-bucket",
    "location": "WNAM"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventTimestamp": "2025-07-28T10:30:00Z"
  }
}
```

Current [event sources](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/) include [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/), and [Workflows](https://developers.cloudflare.com/workflows/). More sources and events are on the way.

For more information on event subscriptions, available events, and how to get started, refer to our [documentation](https://developers.cloudflare.com/queues/event-subscriptions/).

Aug 19, 2025

[<h2>Easier debugging in Workers with improved Wrangler error screen</h2>](https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/)

[Workers](https://developers.cloudflare.com/workers/)

Wrangler's error screen has received several improvements to enhance your debugging experience!

The error screen now features a refreshed design thanks to [youch ↗︎](https://www.npmjs.com/package/youch), with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.

| Before | After (Light) | After (Dark) |
| --- | --- | --- |
| ![Old error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/old-error-screen.yurLWiKb.png) | ![New light theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-light.CcroERTP.png) | ![New dark theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-dark.BIDA2RGg.png) |

Try it out now with `npx wrangler@latest dev` in your Workers project.

Aug 18, 2025

[<h2>WAF Release - 2025-08-18</h2>](https://developers.cloudflare.com/changelog/post/2025-08-18-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**This week's update**

This week, a series of critical vulnerabilities were discovered impacting core enterprise and open-source infrastructure. These flaws present a range of risks, providing attackers with distinct pathways for remote code execution, methods to breach internal network boundaries, and opportunities for critical data exposure and operational disruption.

**Key Findings**

- SonicWall SMA (CVE-2025-32819, CVE-2025-32820, CVE-2025-32821): A remote authenticated attacker with SSLVPN user privileges can bypass path traversal protections. These vulnerabilities enable a attacker to bypass security checks to read, modify, or delete arbitrary files. An attacker with administrative privileges can escalate this further, using a command injection flaw to upload malicious files, which could ultimately force the appliance to reboot to its factory default settings.
- Ms-Swift Project (CVE-2025-50460): An unsafe deserialization vulnerability exists in the Ms-Swift project's handling of YAML configuration files. If an attacker can control the content of a configuration file passed to the application, they can embed a malicious payload that will execute arbitrary code and it can be executed during deserialization.
- Apache Druid (CVE-2023-25194): This vulnerability in Apache Druid allows an attacker to cause the server to connect to a malicious LDAP server. By sending a specially crafted LDAP response, the attacker can trigger an unrestricted deserialization of untrusted data. If specific "gadgets" (classes that can be abused) are present in the server's classpath, this can be escalated to achieve Remote Code Execution (RCE).
- Tenda AC8v4 (CVE-2025-51087, CVE-2025-51088): Vulnerabilities allow an authenticated attacker to trigger a stack-based buffer overflow. By sending malformed arguments in a request to specific endpoints, an attacker can crash the device or potentially achieve arbitrary code execution.
- Open WebUI (CVE-2024-7959): This vulnerability allows a user to change the OpenAI URL endpoint to an arbitrary internal network address without proper validation. This flaw can be exploited to access internal services or cloud metadata endpoints, potentially leading to remote command execution if the attacker can retrieve instance secrets or access sensitive internal APIs.
- BentoML (CVE-2025-54381): The vulnerability exists in the serialization/deserialization handlers for multipart form data and JSON requests, which automatically download files from user-provided URLs without proper validation of internal network addresses. This allows attackers to fetch from unintended internal services, including cloud metadata and localhost.
- Adobe Experience Manager Forms (CVE-2025-54254): An Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could lead to arbitrary file system read in Adobe AEM (≤6.5.23).

**Impact**

These vulnerabilities affect core infrastructure, from network security appliances like SonicWall to data platforms such as Apache Druid and ML frameworks like BentoML. The code execution and deserialization flaws are particularly severe, offering deep system access that allows attackers to steal data, disrupt services, and establish a foothold for broader intrusions. Simultaneously, SSRF and XXE vulnerabilities undermine network boundaries, exposing sensitive internal data and creating pathways for lateral movement. Beyond data-centric threats, flaws in edge devices like the Tenda router introduce the tangible risk of operational disruption, highlighting a multi-faceted threat to the security and stability of key enterprise systems.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...418d9a3b | 100574 | SonicWall SMA - Remote Code Execution - CVE:CVE-2025-32819, CVE:CVE-2025-32820, CVE:CVE-2025-32821 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1e6fefdb | 100576 | Ms-Swift Project - Remote Code Execution - CVE:CVE-2025-50460 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...08ac45b3 | 100585 | Apache Druid - Remote Code Execution - CVE:CVE-2023-25194 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...e4855472 | 100834 | Tenda AC8v4 - Auth Bypass - CVE:CVE-2025-51087, CVE:CVE-2025-51088 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...022ab542 | 100835 | Open WebUI - SSRF - CVE:CVE-2024-7959 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...6339f132 | 100837 | SQLi - OOB | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...b83d2625 | 100841 | BentoML - SSRF - CVE:CVE-2025-54381 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...739180d2 | 100841A | BentoML - SSRF - CVE:CVE-2025-54381 - 2 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...6ab910c2 | 100841B | BentoML - SSRF - CVE:CVE-2025-54381 - 3 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2197ec51 | 100845 | Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...96f34ce3 | 100845A | Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254 - 2 | Log | Block | This is a New Detection |

Aug 15, 2025

[<h2>SFTP support for SSH with Cloudflare Access for Infrastructure</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-sftp/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[SSH with Cloudflare Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.

Aug 15, 2025

[<h2>Steer Traffic by AS Number in Load Balancing Custom Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.

This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.

![Create a Load Balancing Custom Rule using AS Num](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2554,height=1472,format=webp/_astro/asnum-custom-rule.CtcHu_zj.png)

To get started, create a [Custom Rule ↗︎](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) in your Load Balancer and select **AS Num** from the **Field** dropdown.

Aug 15, 2025

[<h2>Extended retention</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-extended-retention/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Customers can now rely on Log Explorer to meet their log retention compliance requirements.

Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.

Aug 15, 2025

[<h2>Save time with bulk query creation in Brand Protection</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-brand-protection-bulk-endpoint/)

[Security Center](https://developers.cloudflare.com/security-center/)

[Brand Protection](https://developers.cloudflare.com/security-center/brand-protection/) detects domains that may be impersonating your brand — from common misspellings (`cloudfalre.com`) to malicious concatenations (`cloudflare-okta.com`). Saved search queries run continuously and alert you when suspicious domains appear.

You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the [Brand Protection bulk query creation API](https://developers.cloudflare.com/api/resources/brand_protection/subresources/queries/methods/bulk/).

Aug 15, 2025

[<h2>Terraform v5.8.4 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-terraform-v5.8.4-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.

One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes

For a more detailed look at all of the changes, refer to the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4) in GitHub.

#### Issues Closed

- [#5017: 'Uncaught Error: No such module' using cloudflare\_snippets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare\_workers\_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare\_argo\_smart\_routing importing doesn't read the actual value ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Aug 15, 2025

[<h2>The Node.js and Web File System APIs in Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-nodejs-fs/)

[Workers](https://developers.cloudflare.com/workers/)

Implementations of the [`node:fs` module ↗︎](https://nodejs.org/docs/latest/api/fs.html) and the [Web File System API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API) are now available in Workers.

#### Using the `node:fs` module

The `node:fs` module provides access to a virtual file system in Workers. You can use it to read and write files, create directories, and perform other file system operations.

The virtual file system is ephemeral with each individual request havig its own isolated temporary file space. Files written to the file system will not persist across requests and will not be shared across requests or across different Workers.

Workers running with the `nodejs_compat` compatibility flag will have access to the `node:fs` module by default when the compatibility date is set to `2025-09-01` or later. Support for the API can also be enabled using the `enable_nodejs_fs_module` compatibility flag together with the `nodejs_compat` flag. The `node:fs` module can be disabled using the `disable_nodejs_fs_module` compatibility flag.

```js
import fs from "node:fs";

const config = JSON.parse(fs.readFileSync("/bundle/config.json", "utf-8"));

export default {
	async fetch(request) {
		return new Response(`Config value: ${config.value}`);
	},
};
```

There are a number of initial limitations to the `node:fs` implementation:

- The glob APIs (e.g. `fs.globSync(...)`) are not implemented.
- The file watching APIs (e.g. `fs.watch(...)`) are not implemented.
- The file timestamps (modified time, access time, etc) are only partially supported. For now, these will always return the Unix epoch.

Refer to the [Node.js documentation ↗︎](https://nodejs.org/docs/latest/api/fs.html) for more information on the `node:fs` module and its APIs.

#### The Web File System API

The Web File System API provides access to the same virtual file system as the `node:fs` module, but with a different API surface. The Web File System API is only available in Workers running with the `enable_web_file_system` compatibility flag. The `nodejs_compat` compatibility flag is not required to use the Web File System API.

```js
const root = navigator.storage.getDirectory();

export default {
	async fetch(request) {
		const tmp = await root.getDirectoryHandle("/tmp");
		const file = await tmp.getFileHandle("data.txt", { create: true });
		const writable = await file.createWritable();
		const writer = writable.getWriter();
		await writer.write("Hello, World!");
		await writer.close();

		return new Response("File written successfully!");
	},
};
```

As there are still some parts of the Web File System API that are not fully standardized, there may be some differences between the Workers implementation and the implementations in browsers.

Aug 15, 2025

[<h2>Workers Static Assets: Corrected handling of double slashes in redirect rule paths</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/)

[Workers](https://developers.cloudflare.com/workers/)

[Static Assets](https://developers.cloudflare.com/workers/static-assets/): Fixed a bug in how [redirect rules ↗︎](https://developers.cloudflare.com/workers/static-assets/redirects/) defined in your Worker's `_redirects` file are processed.

If you're serving Static Assets with a `_redirects` file containing a rule like `/ja/* /:splat`, paths with double slashes were previously misinterpreted as external URLs. For example, visiting `/ja//example.com` would incorrectly redirect to `https://example.com` instead of `/example.com` on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: [Cloudflare Pages](https://developers.cloudflare.com/pages/) was not affected by this issue.

Aug 14, 2025

[<h2>Workers per-branch preview URLs now support long branch names</h2>](https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/)

[Workers](https://developers.cloudflare.com/workers/)

We've updated [preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) for Cloudflare Workers to support long branch names.

Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.

Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.

#### How it works

- **63 characters or less**: `<branch-name>-<worker-name>` → Uses actual branch name as is
- **64 characters or more**: `<truncated-branch-name>--<hash>-<worker-name>` → Uses truncated name with 4-character hash
- **Hash generation**: The hash is derived from the full branch name to ensure uniqueness
- **Stable URLs**: The same branch always generates the same hash across all commits

#### Requirements and compatibility

- **Wrangler 4.30.0 or later**: This feature requires updating to wrangler@4.30.0+
- **No configuration needed**: Works automatically with existing preview URL setups

Aug 14, 2025

[<h2>Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access logs now support the [Customer Metadata Boundary (CMB)](https://developers.cloudflare.com/data-localization/metadata-boundary/). If you have configured the CMB for your account, all Access logging will respect that configuration.

Note

For EU CMB customers, the logs will not be stored by Access and will appear as empty in the dashboard. EU CMB customers should utilize [Logpush](https://developers.cloudflare.com/logs/logpush/) to retain their Access logging, if desired.

Aug 14, 2025

[<h2>Python Workers handlers now live in an entrypoint class</h2>](https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/)

[Workers](https://developers.cloudflare.com/workers/)

We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as `on_fetch`, `on_scheduled`, etc. methods, but now they live in an entrypoint class.

Here's an example of how to now define a Worker with a fetch handler:

```python
from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response("Hello World!")
```

To keep using the old-style handlers, you can specify the `disable_python_no_global_handlers` compatibility flag in your wrangler file:

```jsonc
{
	"compatibility_flags": [
		"disable_python_no_global_handlers"
	]
}
```

```toml
compatibility_flags = [ "disable_python_no_global_handlers" ]
```

Consult the [Python Workers documentation](https://developers.cloudflare.com/workers/languages/python/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/40/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/40/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
