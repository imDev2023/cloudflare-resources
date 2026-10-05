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

Oct 6, 2025

[<h2>R2 Data Catalog table-level compaction</h2>](https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

You can now enable compaction for individual [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), giving you fine-grained control over different workloads.

```bash
# Enable compaction for a specific table (no token required)
npx wrangler r2 bucket catalog compaction enable <BUCKET> <NAMESPACE> <TABLE> --target-size 256
```

This allows you to:

- Apply different target file sizes per table
- Disable compaction for specific tables
- Optimize based on table-specific access patterns

Learn more at [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

Oct 6, 2025

[<h2>Browser Support Detection for PQ Encryption on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-10-06-radar-pq-encryption-test/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes browser detection for Post-quantum (PQ) encryption. The [Post-quantum encryption card ↗︎](https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption) now checks whether a user’s browser supports post-quantum encryption. If support is detected, information about the key agreement in use is displayed.

![Screenshot of the PQ encryption browser support test on the Adoption \& Usage page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=872,height=109,format=webp/_astro/pq-encryption-test.gx_uoaMX.png)

Oct 6, 2025

[<h2>WAF Release - 2025-10-06</h2>](https://developers.cloudflare.com/changelog/post/2025-10-06-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s highlights prioritise an emergency Oracle E-Business Suite RCE rule deployed to block active, high-impact exploitation. Also addressed are high-severity Chaos Mesh controller command-injection flaws that enable unauthenticated in-cluster RCE and potential cluster compromise, plus a form-data multipart boundary issue that permits HTTP Parameter Pollution (HPP). Two new generic SQLi detections were added to catch inline-comment obfuscation and information disclosure techniques.

**Key Findings**

- New emergency rule released for Oracle E-Business Suite (CVE-2025-61882) addressing an actively exploited remote code execution vulnerability in core business application modules. Immediate mitigation deployed to protect enterprise workloads.
- Chaos Mesh (CVE-2025-59358,CVE-2025-59359,CVE-2025-59360,CVE-2025-59361): A GraphQL debug endpoint on the Chaos Controller Manager is exposed without authentication; several controller mutations ( `cleanTcs`, `killProcesses`, `cleanIptables`) are vulnerable to OS command injection.
- Form-Data (CVE-2025-7783): Attackers who can observe `Math.random()` outputs and control request fields in form-data may exploit this flaw to perform HTTP parameter pollution, leading to request tampering or data manipulation.
- Two new generic SQLi detections added to enhance baseline coverage against inline-comment obfuscation and information disclosure attempts.

**Impact**

- CVE-2025-61882 — Oracle E-Business Suite remote code execution (emergency detection): attacker-controlled input can yield full system compromise, data exfiltration, and operational outage; immediate blocking enforced.
- CVE-2025-59358 / CVE-2025-59359 / CVE-2025-59360 / CVE-2025-59361 — Unauthenticated command-injection in Chaos Mesh controllers allowing remote code execution, cluster compromise, and service disruption (high availability risk).
- CVE-2025-7783 — Predictable multipart boundaries in form-data enabling HTTP Parameter Pollution; results include request tampering, parameter overwrite, and downstream data integrity loss.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...8650f52f | 100882 | Chaos Mesh - Missing Authentication - CVE:CVE-2025-59358 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2b8c3680 | 100883 | Chaos Mesh - Command Injection - CVE:CVE-2025-59359 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...ef859a04 | 100884 | Chaos Mesh - Command Injection - CVE:CVE-2025-59361 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...961f26a7 | 100886 | Form-Data - Parameter Pollution - CVE:CVE-2025-7783 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...26a4074c | 100888 | Chaos Mesh - Command Injection - CVE:CVE-2025-59360 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...31101b2f | 100916 | Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 | N/A | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...29aa43c3 | 100917 | Generic Rules - SQLi - Inline Comment Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...73c10b6f | 100918 | Generic Rules - SQLi - Information Disclosure | N/A | Disabled | This is a New Detection |

Oct 3, 2025

[<h2>WAF Release - 2025-10-03</h2>](https://developers.cloudflare.com/changelog/post/2025-10-03-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**Managed Ruleset Updated**

This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...d61fac74 | 100902 | Generic Rules - Command Execution - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...514aeeb8 | 100908 | Generic Rules - Command Execution - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...8d46a6f4 | 100910 | Generic Rules - Command Execution - 4 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1bd0a329 | 100915 | Generic Rules - Command Execution - 5 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5e51450a | 100899 | Generic Rules - Content-Type Abuse | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7996012f | 100914 | Generic Rules - Content-Type Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...93209312 | 100911 | Generic Rules - Cookie Header Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...0f373b3f | 100905 | Generic Rules - NoSQL Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...78a0ed04 | 100913 | Generic Rules - NoSQL Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5d649624 | 100907 | Generic Rules - Parameter Pollution | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...fd1c674e | 100906 | Generic Rules - PHP Object Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...34c88168 | 100904 | Generic Rules - Prototype Pollution | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3ab43f7e | 100897 | Generic Rules - Prototype Pollution 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...0d94ee22 | 100903 | Generic Rules - Reverse Shell | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d5add8e3 | 100909 | Generic Rules - Reverse Shell - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...565c78b0 | 100898 | Generic Rules - SSJI NoSQL | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...12b837a0 | 100896 | Generic Rules - SSRF | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...11c4fb00 | 100895 | Generic Rules - Template Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d3ed0123 | 100895A | Generic Rules - Template Injection - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7501a1d9 | 100912 | Generic Rules - XXE | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...dc55cdb6 | 100900 | Relative Paths - Anomaly Headers | N/A | Disabled | This is a New Detection |

Oct 3, 2025

[<h2>One-click Cloudflare Access for Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-10-03-one-click-access-for-workers/)

[Workers](https://developers.cloudflare.com/workers/)

You can now enable [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for your [`workers.dev`](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) and [Preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) in a single click.

![Screenshot of the Enable/Disable Cloudflare Access button on the workers.dev route settings page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1016,format=webp/_astro/workers-access.DGGYThLx.png)

Access allows you to limit access to your Workers to specific users or groups. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

To enable Cloudflare Access:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page. [Go to **Workers & Pages** ↗](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
2. In **Overview**, select your Worker.
3. Go to **Settings** > **Domains & Routes**.
4. For `workers.dev` or Preview URLs, click **Enable Cloudflare Access**.
5. Optionally, to configure the Access application, click **Manage Cloudflare Access**. There, you can change the email addresses you want to authorize. View [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors) to learn about configuring alternate rules.

To fully secure your application, it is important that you validate the JWT that Cloudflare Access adds to the `Cf-Access-Jwt-Assertion` header on the incoming request.

The following code will validate the JWT using the [jose NPM package ↗︎](https://www.npmjs.com/package/jose):

```javascript
import { jwtVerify, createRemoteJWKSet } from "jose";

export default {
	async fetch(request, env, ctx) {
		// Verify the POLICY_AUD environment variable is set
		if (!env.POLICY_AUD) {
			return new Response("Missing required audience", {
				status: 403,
				headers: { "Content-Type": "text/plain" },
			});
		}

		// Get the JWT from the request headers
		const token = request.headers.get("cf-access-jwt-assertion");

		// Check if token exists
		if (!token) {
			return new Response("Missing required CF Access JWT", {
				status: 403,
				headers: { "Content-Type": "text/plain" },
			});
		}

		try {
			// Create JWKS from your team domain
			const JWKS = createRemoteJWKSet(
				new URL(`${env.TEAM_DOMAIN}/cdn-cgi/access/certs`),
			);

			// Verify the JWT
			const { payload } = await jwtVerify(token, JWKS, {
				issuer: env.TEAM_DOMAIN,
				audience: env.POLICY_AUD,
			});

			// Token is valid, proceed with your application logic
			return new Response(`Hello ${payload.email || "authenticated user"}!`, {
				headers: { "Content-Type": "text/plain" },
			});
		} catch (error) {
			// Token verification failed
			return new Response(`Invalid token: ${error.message}`, {
				status: 403,
				headers: { "Content-Type": "text/plain" },
			});
		}
	},
};
```

#### Required environment variables

Add these [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) to your Worker:

- `POLICY_AUD`: Your application's AUD tag
- `TEAM_DOMAIN`: `https://<your-team-name>.cloudflareaccess.com`

Both of these appear in the modal that appears when you enable Cloudflare Access.

You can set these variables by adding them to your Worker's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), or via the Cloudflare dashboard under **Workers & Pages** > **your-worker** > **Settings** > **Environment Variables**.

Oct 2, 2025

[<h2>Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Fine-grained permissions for **Access Applications, Identity Providers (IdPs), and Targets** is now available in Public Beta. This expands our RBAC model beyond account & zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.

#### What's New

- **[Access Applications ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3004,height=1410,format=webp/_astro/2025-10-01-fine-grained-permissioning-ux.BWVmQsVF.png)

Note

During the public beta, members must also be assigned an account-scoped, read only role to view resources in the dashboard. This restriction will be lifted in a future release.

- **Account Read Only** plus a fine-grained permission for a specific App, IdP, or Target
- **Cloudflare Zero Trust Read Only** plus fine-grained permission for a specific App, IdP, or Target

For more info:

- [Get started with Cloudflare Permissioning](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
- [Manage Member Permissioning via the UI & API](https://developers.cloudflare.com/fundamentals/manage-members/manage)

Oct 2, 2025

[<h2>New Deepgram Flux model available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Deepgram's newest Flux model [`@cf/deepgram/flux`](https://developers.cloudflare.com/workers-ai/models/flux/) is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out [Deepgram's blog ↗︎](https://deepgram.com/flux) for more details on the release.

The Flux model can be used in conjunction with Deepgram's speech-to-text model [`@cf/deepgram/nova-3`](https://developers.cloudflare.com/workers-ai/models/nova-3/) and text-to-speech model [`@cf/deepgram/aura-1`](https://developers.cloudflare.com/workers-ai/models/aura-1/) to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.

#### Promotional Pricing

For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](https://developers.cloudflare.com/workers-ai/models/flux/) for pricing details in the future.

#### Example Usage

The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.

1. Create a worker that establishes a websocket connection with `@cf/deepgram/flux`

```js
export default {
  async fetch(request, env, ctx): Promise<Response> {
    const resp = await env.AI.run("@cf/deepgram/flux", {
      encoding: "linear16",
      sample_rate: "16000"
    }, {
      websocket: true
    });
    return resp;
  },
} satisfies ExportedHandler<Env>;
```

2. Deploy your worker

```bash
npx wrangler deploy
```

3. Write a client script to connect to your worker and start sending random audio bytes to it

```js
const ws = new WebSocket('wss://<your-worker-url.com>');

ws.onopen = () => {
  console.log('Connected to WebSocket');

  // Generate and send random audio bytes
  // You can replace this part with a function
  // that reads from your mic or other audio source
  const audioData = generateRandomAudio();
  ws.send(audioData);
  console.log('Audio data sent');
};

ws.onmessage = (event) => {
  // Transcription will be received here
  // Add your custom logic to parse the data
  console.log('Received:', event.data);
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

ws.onclose = () => {
  console.log('WebSocket closed');
};

// Generate random audio data (1 second of noise at 44.1kHz, mono)
function generateRandomAudio() {
  const sampleRate = 44100;
  const duration = 1;
  const numSamples = sampleRate * duration;
  const buffer = new ArrayBuffer(numSamples * 2);
  const view = new Int16Array(buffer);

  for (let i = 0; i < numSamples; i++) {
    view[i] = Math.floor(Math.random() * 65536 - 32768);
  }

  return buffer;
}
```

Oct 2, 2025

[<h2>Workers Analytics Engine adds supports for new SQL functions</h2>](https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/)

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) [Workers](https://developers.cloudflare.com/workers/)

You can now perform more powerful queries directly in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/) with a major expansion of our SQL function library.

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.

Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:

[**New aggregate functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/)

- `argMin()` - Returns the value associated with the minimum in a group
- `argMax()` - Returns the value associated with the maximum in a group
- `topK()` - Returns an array of the most frequent values in a group
- `topKWeighted()` - Returns an array of the most frequent values in a group using weights
- `first_value()` - Returns the first value in an ordered set of values within a partition
- `last_value()` - Returns the last value in an ordered set of values within a partition

[**New bit functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/)

- `bitAnd()` - Returns the bitwise AND of two expressions
- `bitCount()` - Returns the number of bits set to one in the binary representation of a number
- `bitHammingDistance()` - Returns the number of bits that differ between two numbers
- `bitNot()` - Returns a number with all bits flipped
- `bitOr()` - Returns the inclusive bitwise OR of two expressions
- `bitRotateLeft()` - Rotates all bits in a number left by specified positions
- `bitRotateRight()` - Rotates all bits in a number right by specified positions
- `bitShiftLeft()` - Shifts all bits in a number left by specified positions
- `bitShiftRight()` - Shifts all bits in a number right by specified positions
- `bitTest()` - Returns the value of a specific bit in a number
- `bitXor()` - Returns the bitwise exclusive-or of two expressions

[**New mathematical functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/)

- `abs()` - Returns the absolute value of a number
- `log()` - Computes the natural logarithm of a number
- `round()` - Rounds a number to a specified number of decimal places
- `ceil()` - Rounds a number up to the nearest integer
- `floor()` - Rounds a number down to the nearest integer
- `pow()` - Returns a number raised to the power of another number

[**New string functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/)

- `lowerUTF8()` - Converts a string to lowercase using UTF-8 encoding
- `upperUTF8()` - Converts a string to uppercase using UTF-8 encoding

[**New encoding functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/)

- `hex()` - Converts a number to its hexadecimal representation
- `bin()` - Converts a string to its binary representation

[**New type conversion functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/)

- `toUInt8()` - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer

#### Ready to get started?

Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started](https://developers.cloudflare.com/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/).

Oct 1, 2025

[<h2>New Confidence Intervals in GraphQL Analytics API</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/)

[Analytics](https://developers.cloudflare.com/analytics/)

The GraphQL Analytics API now supports confidence intervals for `sum` and `count` fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.

- **Supported datasets**: Adaptive (sampled) datasets only.
- **Supported fields**: All `sum` and `count` fields.
- **Usage**: The confidence `level` must be provided as a decimal between 0 and 1 (e.g. `0.90`, `0.95`, `0.99`).
- **Default**: If no confidence level is specified, no intervals are returned.

For examples and more details, see the [GraphQL Analytics API documentation](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/).

Oct 1, 2025

[<h2>Larger Container instance types</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/)

[Containers](https://developers.cloudflare.com/containers/)

New instance types provide up to 4 vCPU, 12 GiB of memory, and 20 GB of disk per container instance.

| Instance Type | vCPU | Memory | Disk |
| --- | --- | --- | --- |
| lite | 1/16 | 256 MiB | 2 GB |
| basic | 1/4 | 1 GiB | 4 GB |
| standard-1 | 1/2 | 4 GiB | 8 GB |
| standard-2 | 1 | 6 GiB | 12 GB |
| standard-3 | 2 | 8 GiB | 16 GB |
| standard-4 | 4 | 12 GiB | 20 GB |

The `dev` and `standard` instance types are preserved for backward compatibility and are aliases for `lite` and `standard-1`, respectively. The `standard-1` instance type now provides up to 8 GB of disk instead of only 4 GB.

See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container, and the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

Oct 1, 2025

[<h2>Expanded File Type Controls for Executables and Disk Images</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.

We have expanded Gateway's file type controls to include:

- Apple Disk Image (dmg)
- Microsoft Software Installer (msix, appx)
- Apple Software Package (pkg)

You can find these new options within the [*Upload File Types* and *Download File Types* selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) when creating or editing an HTTP policy. The file types are categorized as follows:

- **System**: *Apple Disk Image (dmg)*
- **Executable**: *Microsoft Software Installer (msix)*, *Microsoft Software Installer (appx)*, *Apple Software Package (pkg)*

To ensure these file types are blocked effectively, please note the following behaviors:

- DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.
- MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type *Unscannable*. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.

To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to [supported file types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#supported-file-types).

Oct 1, 2025

[<h2>Return markdown</h2>](https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.

```sh
curl https://developers.cloudflare.com/workers/ -H 'Accept: text/markdown'  -v
```

If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example [here ↗︎](https://github.com/cloudflare/cloudflare-docs/pull/25493).

Sep 30, 2025

[<h2>Application granular controls for operations in SaaS applications</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway users can now apply granular controls to their file sharing and AI chat applications through [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies).

The new feature offers two methods of controlling SaaS applications:

- **Application Controls** are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include *Upload*, *Download*, *Prompt*, *Voice*, and *Share* depending on the application.
- **Operations** are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.

Get started using [Application Granular Controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls) and refer to the list of [supported applications](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications).

Sep 29, 2025

[<h2>Regional Data in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-09-29-radar-regional-data/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.

The following API endpoints are now available:

- [`Get Geolocation`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/get/) - Retrieves geolocation by `geoId`.
- [`List Geolocations`](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/list/) - Lists geolocations.
- [`NetFlows Summary By Dimension`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary_v2/) - Retrieves NetFlows summary by dimension.

All `summary` and `timeseries_groups` endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/) now include an `adm1` dimension for grouping data by first level administrative division (for example, state, province, etc.)

A new filter `geoId` was also added to all endpoints in [`HTTP`](https://developers.cloudflare.com/api/resources/radar/subresources/http/) and [`NetFlows`](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/), allowing filtering by a specific administrative division.

Check out the new Regional traffic insights on a country specific traffic page [new Radar page ↗︎](https://radar.cloudflare.com/traffic/pt).

Sep 29, 2025

[<h2>WAF Release - 2025-09-29</h2>](https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week highlights four important vendor- and component-specific issues: an authentication bypass in SimpleHelp (CVE-2024-57727), an information-disclosure flaw in Flowise Cloud (CVE-2025-58434), an SSRF in the WordPress plugin Ditty (CVE-2025-8085), and a directory-traversal bug in Vite (CVE-2025-30208). These are paired with improvements to our generic detection coverage (SQLi, SSRF) to raise the baseline and reduce noisy gaps.

**Key Findings**

- SimpleHelp (CVE-2024-57727): Authentication bypass in SimpleHelp that can allow unauthorized access to management interfaces or sessions.
- Flowise Cloud (CVE-2025-58434): Information-disclosure vulnerability in Flowise Cloud that may expose sensitive configuration or user data to unauthenticated or low-privileged actors.
- WordPress:Plugin: Ditty (CVE-2025-8085): SSRF in the Ditty WordPress plugin enabling server-side requests that could reach internal services or cloud metadata endpoints.
- Vite (CVE-2025-30208): Directory-traversal vulnerability in Vite allowing access to filesystem paths outside the intended web root.

**Impact**

These vulnerabilities allow attackers to gain access, escalate privileges, or execute actions that were previously unavailable:

- SimpleHelp (CVE-2024-57727): An authentication bypass that can let unauthenticated attackers access management interfaces or hijack sessions — enabling lateral movement, credential theft, or privilege escalation within affected environments.
- Flowise Cloud (CVE-2025-58434): Information-disclosure flaw that can expose sensitive configuration, tokens, or user data; leaked secrets may be chained into account takeover or privileged access to backend services.
- WordPress:Plugin: Ditty (CVE-2025-8085): SSRF that enables server-side requests to internal services or cloud metadata endpoints, potentially allowing attackers to retrieve credentials or reach otherwise inaccessible infrastructure, leading to privilege escalation or cloud resource compromise.
- Vite (CVE-2025-30208): Directory-traversal vulnerability that can expose filesystem contents outside the web root (configuration files, keys, source code), which attackers can use to escalate privileges or further compromise systems.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...8c2e30fb | 100717 | SimpleHelp - Auth Bypass - CVE:CVE-2024-57727 | Log | Block | This rule is merged to 100717 in legacy WAF and ...958094d3 in new WAF |
| Cloudflare Managed Ruleset | ...d58b886b | 100775 | Flowise Cloud - Information Disclosure - CVE:CVE-2025-58434 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...9bce1ff4 | 100881 | WordPress:Plugin:Ditty - SSRF - CVE:CVE-2025-8085 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...ddc329dd | 100887 | Vite - Directory Traversal - CVE:CVE-2025-30208 | Log | Block | This is a New Detection |

Sep 28, 2025

[<h2>WAF Release - 2025-09-28 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-09-28-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.

**Key Findings**

- Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.

**Impact**

Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...9ee0ab84 | 100788 | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d30f768e | 100788A | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Disabled | This is a New Detection |

Sep 26, 2025

[<h2>WAF Release - 2025-09-26</h2>](https://developers.cloudflare.com/changelog/post/2025-09-26-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

**Managed Ruleset Updated**

This update introduces 11 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...a67d8561 | 100859A | SQLi - UNION - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...4de80468 | 100889 | Command Injection - Generic 9 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...f2be3ddf | 100890 | Information Disclosure - Common Files - 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...80a252a8 | 100891 | Anomaly:URL - Relative Paths | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...7e7d3865 | 100894 | XSS - Inline Function | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3792565c | 100895 | XSS - DOM | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...42978e38 | 100896 | SQLi - MSSQL Length Enumeration | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...3ab43f7e | 100897 | Generic Rules - Code Injection - 3 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c1686741 | 100898 | SQLi - Evasion | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...20999be0 | 100899 | SQLi - Probing 2 | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...b4026c88 | 100900 | SQLi - Probing | N/A | Disabled | This is a New Detection |

Sep 26, 2025

[<h2>Automatic loopback bindings via ctx.exports</h2>](https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/)

[Workers](https://developers.cloudflare.com/workers/)

The [`ctx.exports` API](https://developers.cloudflare.com/workers/runtime-apis/context/#exports) contains automatically-configured bindings corresponding to your Worker's top-level exports. For each top-level export extending `WorkerEntrypoint`, `ctx.exports` will contain a [Service Binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings) by the same name, and for each export extending `DurableObject` (and for which storage has been configured via a [migration](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/)), `ctx.exports` will contain a [Durable Object namespace binding](https://developers.cloudflare.com/durable-objects/api/namespace/). This means you no longer have to configure these bindings explicitly in `wrangler.jsonc`/`wrangler.toml`.

Example:

```js
import { WorkerEntrypoint } from "cloudflare:workers";

export class Greeter extends WorkerEntrypoint {
  greet(name) {
    return `Hello, ${name}!`;
  }
}

export default {
  async fetch(request, env, ctx) {
    let greeting = await ctx.exports.Greeter.greet("World")
    return new Response(greeting);
  }
}
```

At present, you must use [the `enable_ctx_exports` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags#enable-ctxexports) to enable this API, though it will be on by default in the future.

[See the API reference for more information.](https://developers.cloudflare.com/workers/runtime-apis/context/#exports)

Sep 25, 2025

[<h2>Pipelines now supports SQL transformations and Apache Iceberg</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-pipelines-sql/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/)

Today, we are launching the new [Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/): a streaming data platform that ingests events, transforms them with [SQL](https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/), and writes to [R2](https://developers.cloudflare.com/r2/) as [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables or Parquet files.

Pipelines can receive events via [HTTP endpoints](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#send-via-http) or [Worker bindings](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#send-via-workers), transform them with SQL, and deliver to R2 with exactly-once guarantees. This makes it easy to build analytics-ready warehouses for server logs, mobile application events, IoT telemetry, or clickstream data without managing streaming infrastructure.

For example, here is a pipeline that ingests clickstream events and filters out bot traffic while extracting domain information:

```sql
INSERT into events_table
SELECT
  user_id,
  lower(event) AS event_type,
  to_timestamp_micros(ts_us) AS event_time,
  regexp_match(url, '^https?://([^/]+)')[1]  AS domain,
  url,
  referrer,
  user_agent
FROM events_json
WHERE event = 'page_view'
  AND NOT regexp_like(user_agent, '(?i)bot|spider');
```

Get started by creating a pipeline in the dashboard or running a single command in [Wrangler](https://developers.cloudflare.com/workers/wrangler/):

```bash
npx wrangler pipelines setup
```

Check out our [getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/) to learn how to create a pipeline that delivers events to an [Iceberg table](https://developers.cloudflare.com/basin-catalog/) you can query with R2 SQL. Read more about today's announcement in our [blog post ↗︎](https://blog.cloudflare.com/cloudflare-data-platform).

Sep 25, 2025

[<h2>Announcing R2 SQL</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/)

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Today, we are launching the **open beta** for [R2 SQL](https://developers.cloudflare.com/basin-sql/): A serverless, distributed query engine that can efficiently analyze petabytes of data in [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from [Pipelines](https://developers.cloudflare.com/basin-pipelines/), or clickstream and user behavior data.

If you already have a table in R2 Data Catalog, running queries is as simple as:

```bash
npx wrangler r2 sql query YOUR_WAREHOUSE "
SELECT
    user_id,
    event_type,
    value
FROM events.user_events
WHERE event_type = 'CHANGELOG' or event_type = 'BLOG'
  AND __ingest_ts > '2025-09-24T00:00:00Z'
ORDER BY __ingest_ts DESC
LIMIT 100"
```

To get started with R2 SQL, check out our [getting started guide](https://developers.cloudflare.com/basin-sql/get-started/) or learn more about supported features in the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For a technical deep dive into how we built R2 SQL, read our [blog post ↗︎](https://blog.cloudflare.com/r2-sql-deep-dive/).

Sep 25, 2025

[<h2>Browser Rendering Playwright GA, Stagehand support (Beta), and higher limits</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-br-playwright-ga-stagehand-limits/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

We’re shipping three updates to Browser Rendering:

- Playwright support is now Generally Available and synced with [Playwright v1.55 ↗︎](https://playwright.dev/docs/release-notes#version-155), giving you a stable foundation for critical automation and AI-agent workflows.
- We’re also adding [Stagehand support (Beta)](https://developers.cloudflare.com/browser-run/stagehand/) so you can combine code with natural language instructions to build more resilient automations.
- Finally, we’ve tripled [limits](https://developers.cloudflare.com/browser-run/limits/#workers-paid) for paid plans across both the [REST API](https://developers.cloudflare.com/browser-run/quick-actions/) and [Browser Sessions](https://developers.cloudflare.com/browser-run/#integration-methods) to help you scale.

To get started with Stagehand, refer to the [Stagehand](https://developers.cloudflare.com/browser-run/stagehand/) example that uses Stagehand and [Workers AI](https://developers.cloudflare.com/workers-ai/) to search for a movie on this [example movie directory ↗︎](https://demo.playwright.dev/movies), extract its details using natural language (title, year, rating, duration, and genre), and return the information along with a screenshot of the webpage.

*Stagehand examplets*

```ts
const stagehand = new Stagehand({
	env: "LOCAL",
	localBrowserLaunchOptions: { cdpUrl: endpointURLString(env.BROWSER) },
	llmClient: new WorkersAIClient(env.AI),
	verbose: 1,
});

await stagehand.init();
const page = stagehand.page;

await page.goto("https://demo.playwright.dev/movies");

// if search is a multi-step action, stagehand will return an array of actions it needs to act on
const actions = await page.observe('Search for "Furiosa"');
for (const action of actions) await page.act(action);

await page.act("Click the search result");

// normal playwright functions work as expected
await page.waitForSelector(".info-wrapper .cast");

let movieInfo = await page.extract({
	instruction: "Extract movie information",
	schema: z.object({
		title: z.string(),
		year: z.number(),
		rating: z.number(),
		genres: z.array(z.string()),
		duration: z.number().describe("Duration in minutes"),
	}),
});

await stagehand.close();
```

![Stagehand video](https://developers.cloudflare.com/images/browser-run/speedystagehand.gif)

Sep 25, 2025

[<h2>AI Search (formerly AutoRAG) now with More Models To Choose From</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.

With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.

To use AI Search with other [model providers](https://developers.cloudflare.com/ai-search/configuration/models/):

1. **Add provider keys to AI Gateway**
   1. Go to AI > AI Gateway in the dashboard.
   2. Select or create an AI gateway.
   3. In Provider Keys, choose your provider, click Add, and enter the key.
2. **Connect a gateway to AI Search**: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.
3. **Select models**: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.

Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a `/ai-search` request:

```javascript
export default {
  async fetch(request, env) {
    
    // Query your AI Search instance with a natural language question to an OpenAI model
    const result = await env.AI.autorag("my-ai-search").aiSearch({
      query: "What's new for Cloudflare Birthday Week?",
      model: "openai/gpt-5"
    });

    // Return only the generated answer as plain text
    return new Response(result.response, {
      headers: { "Content-Type": "text/plain" },
    });
  },
};
```

In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the [AI Search Changelog](https://developers.cloudflare.com/changelog/product/ai-search/) and [Discord ↗︎](https://discord.cloudflare.com/) for more updates!

Sep 25, 2025

[<h2>R2 Data Catalog now supports compaction</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/)

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

You can now enable automatic compaction for [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) to improve query performance.

Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.

To enable automatic compaction in R2 Data Catalog, find it under **R2 Data Catalog** in your R2 bucket settings in the dashboard.

![compaction-dash](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=799,height=400,format=webp/_astro/compaction.MLojYuHL.png)

Or with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:

```bash
npx wrangler r2 bucket catalog compaction enable <BUCKET_NAME>  --target-size 128 --token <API_TOKEN>
```

To get started with compaction, check out [manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/). For best practices and limitations, refer to [about compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Sep 25, 2025

[<h2>Run more Containers with higher resource limits</h2>](https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/)

[Containers](https://developers.cloudflare.com/containers/)

You can now run more Containers concurrently with higher limits on CPU, memory, and disk.

| Limit | New Limit | Previous Limit |
| --- | --- | --- |
| Memory for concurrent live Container instances | 400GiB | 40GiB |
| vCPU for concurrent live Container instances | 100 | 20 |
| Disk for concurrent live Container instances | 2TB | 100GB |

You can now run 1000 instances of the `dev` instance type, 400 instances of `basic`, or 100 instances of `standard` concurrently.

This opens up new possibilities for running larger-scale workloads on Containers.

See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container, and the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

Sep 25, 2025

[<h2>Refine DLP Scans with New Body Phase Selector</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.

In the Gateway HTTP policy builder, you will find a new selector called *Body Phase*. This allows you to define the direction of traffic the DLP engine will inspect:

- *Request Body*: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.
- *Response Body*: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.

For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the **Body Phase** to *Request Body*, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.

All policies without this selector will continue to scan both request and response bodies to ensure continued protection.

For more information, refer to [Gateway HTTP policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#body-phase).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/37/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/37/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
