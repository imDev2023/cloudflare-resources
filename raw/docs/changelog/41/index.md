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

Aug 14, 2025

[<h2>Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes</h2>](https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/)

[Workers](https://developers.cloudflare.com/workers/)

The recent [Cloudflare Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) and SDK releases (such as [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript)) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding [Python Workers](https://developers.cloudflare.com/workers/languages/python/) support.

#### Terraform Improvements

#### Fixed Unwarranted Plan Diffs

Resolved several issues with the `cloudflare_workers_script` resource that resulted in unwarranted plan diffs, including:

- Using Durable Objects migrations
- Using some bindings such as `secret_text`
- Using smart placement

A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.

#### Improved File Management

You can now specify `content_file` and `content_sha256` instead of `content`. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id      = "123456789"
  script_name     = "my_worker"
  main_module     = "worker.mjs"
  content_file    = "worker.mjs"
  content_sha256  = filesha256("worker.mjs")
}
```

#### Assets Headers and Redirects Support

Fixed the `cloudflare_workers_script` resource to properly support headers and redirects for Assets:

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id      = "123456789"
  script_name     = "my_worker"
  main_module     = "worker.mjs"
  content_file    = "worker.mjs"
  content_sha256  = filesha256("worker.mjs")
  assets = {
    config = {
      headers = file("_headers")
      redirects = file("_redirects")
    }
    # Completion jwt from:
    # https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/
    jwt = "jwt"
  }
}
```

Available in Cloudflare Terraform Provider 5.8.0.

#### Python Workers Support

Added support for uploading [Python Workers](https://developers.cloudflare.com/workers/languages/python/) (beta) in Terraform. You can now deploy Python Workers with:

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id       = "123456789"
  script_name      = "my_worker"
  content_file     = "worker.py"
  content_sha256   = filesha256("worker.py")
  content_type     = "text/x-python"
}
```

Available in Cloudflare Terraform Provider 5.8.0.

#### SDK Enhancements

#### Improved File Upload API

Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:

```js
const scriptContent = `
  export default {
    async fetch(request, env, ctx) {
      return new Response('Hello World!', { status: 200 });
    }
  };
`;

client.workers.scripts.versions.create('my-worker', {
  account_id: '123456789',
  metadata: {
    main_module: 'my-worker.mjs',
  },
  files: [
    await toFile(
      Buffer.from(scriptContent),
      'my-worker.mjs',
      {
        type: "application/javascript+module",
      }
    )
  ]
});
```

Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.

#### Fixed updating KV values

Previously when creating a KV value like this:

```js
await cf.kv.namespaces.values.update("my-kv-namespace", "key1", {
  account_id: "123456789",
  metadata: "my metadata",
  value: JSON.stringify({
    hello: "world"
  })
});
```

...and recalling it in your Worker like this:

```ts
const value = await c.env.KV.get<{hello: string}>("key1", "json");
```

You'd get back this: `{metadata:'my metadata', value:"{'hello':'world'}"}` instead of the correct value of `{hello: 'world'}`

This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.

Aug 13, 2025

[<h2>IBM Cloud Logs as Logpush destination</h2>](https://developers.cloudflare.com/changelog/post/2025-08-13-ibm-cloud-logs-destination/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports IBM Cloud Logs as a native destination.

Logs from Cloudflare can be sent to [IBM Cloud Logs ↗︎](https://www.ibm.com/products/cloud-logs) via [Logpush](https://developers.cloudflare.com/logs/logpush/). The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/). The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.

For more information, refer to [Destination Configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/) documentation.

Aug 11, 2025

[<h2>MessageChannel and MessagePort</h2>](https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/)

[Workers](https://developers.cloudflare.com/workers/)

A minimal implementation of the [MessageChannel API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) is now available in Workers. This means that you can use `MessageChannel` to send messages between different parts of your Worker, but not across different Workers.

The `MessageChannel` and `MessagePort` APIs will be available by default at the global scope with any worker using a compatibility date of `2025-08-15` or later. It is also available using the `expose_global_message_channel` compatibility flag, or can be explicitly disabled using the `no_expose_global_message_channel` compatibility flag.

```js
const { port1, port2 } = new MessageChannel();

port2.onmessage = (event) => {
	console.log('Received message:', event.data);
};

port2.postMessage('Hello from port2!');
```

Any value that can be used with the `structuredClone(...)` API can be sent over the port.

#### Differences

There are a number of key limitations to the `MessageChannel` API in Workers:

- Transfer lists are currently not supported. This means that you will not be able to transfer ownership of objects like `ArrayBuffer` or `MessagePort` between ports.
- The `MessagePort` is not yet serializable. This means that you cannot send a `MessagePort` object through the `postMessage` method or via JSRPC calls.
- The `'messageerror'` event is only partially supported. If the `'onmessage'` handler throws an error, the `'messageerror'` event will be triggered, however, it will not be triggered when there are errors serializing or deserializing the message data. Instead, the error will be thrown when the `postMessage` method is called on the sending port.
- The `'close'` event will be emitted on both ports when one of the ports is closed, however it will not be emitted when the Worker is terminated or when one of the ports is garbage collected.

Aug 11, 2025

[<h2>WAF Release - 2025-08-11</h2>](https://developers.cloudflare.com/changelog/post/2025-08-11-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's update focuses on a wide range of enterprise software, from network infrastructure and security platforms to content management systems and development frameworks. Flaws include unsafe deserialization, OS command injection, SSRF, authentication bypass, and arbitrary file upload — many of which allow unauthenticated remote code execution. Notable risks include Cisco Identity Services Engine and Ivanti EPMM, where successful exploitation could grant attackers full administrative control of core network infrastructure and popular web services such as WordPress, SharePoint, and Ingress-Nginx, where security bypasses and arbitrary file uploads could lead to complete site or server compromise.

**Key Findings**

- Cisco Identity Services Engine (CVE-2025-20281): Insufficient input validation in a specific API of Cisco Identity Services Engine (ISE) and ISE-PIC allows an unauthenticated, remote attacker to execute arbitrary code with root privileges on an affected device.
- Wazuh Server (CVE-2025-24016): An unsafe deserialization vulnerability in Wazuh Server (versions 4.4.0 to 4.9.0) allows for remote code execution and privilege escalation. By injecting unsanitized data, an attacker can trigger an exception to execute arbitrary code on the server.
- CrushFTP (CVE-2025-54309): A flaw in AS2 validation within CrushFTP allows remote attackers to gain administrative access via HTTPS on systems not using the DMZ proxy feature. This flaw can lead to unauthorized file access and potential system compromise.
- Kentico Xperience CMS (CVE-2025-2747, CVE-2025-2748): Vulnerabilities in Kentico Xperience CMS could enable cross-site scripting (XSS), allowing attackers to inject malicious scripts into web pages. Additionally, a flaw could allow unauthenticated attackers to bypass the Staging Sync Server's authentication, potentially leading to administrative control over the CMS.
- Node.js (CVE-2025-27210): An incomplete fix for a previous vulnerability (CVE-2025-23084) in Node.js affects the `path.join()` API method on Windows systems. The vulnerability can be triggered using reserved Windows device names such as `CON`, `PRN`, or `AUX`.
- WordPress:Plugin:Simple File List (CVE-2025-34085, CVE-2020-36847): This vulnerability in the Simple File List plugin for WordPress allows an unauthenticated remote attacker to upload arbitrary files to a vulnerable site. This can be exploited to achieve remote code execution on the server.  
   (Note: CVE-2025-34085 has been rejected as a duplicate.)
- GeoServer (CVE-2024-29198): A Server-Side Request Forgery (SSRF) vulnerability exists in GeoServer's Demo request endpoint, which can be exploited where the Proxy Base URL has not been configured.
- Ivanti EPMM (CVE-2025-6771): An OS command injection vulnerability in Ivanti Endpoint Manager Mobile (EPMM) before versions 12.5.0.2, 12.4.0.3, and 12.3.0.3 allows a remote, authenticated attacker with high privileges to execute arbitrary code.
- Microsoft SharePoint (CVE-2024-38018): This is a remote code execution vulnerability affecting Microsoft SharePoint Server.
- Manager-IO (CVE-2025-54122): A critical unauthenticated full read Server-Side Request Forgery (SSRF) vulnerability is present in the proxy handler of both Manager Desktop and Server editions up to version 25.7.18.2519. This allows an unauthenticated attacker to bypass network isolation and access internal services.
- Ingress-Nginx (CVE-2025-1974): A vulnerability in the Ingress-Nginx controller for Kubernetes allows an attacker to bypass access control rules. An unauthenticated attacker with access to the pod network can achieve arbitrary code execution in the context of the ingress-nginx controller.
- PaperCut NG/MF (CVE-2023-2533): A Cross-Site Request Forgery (CSRF) vulnerability has been identified in PaperCut NG/MF. Under specific conditions, an attacker could exploit this to alter security settings or execute arbitrary code if they can deceive an administrator with an active login session into clicking a malicious link.
- SonicWall SMA (CVE-2025-40598): This vulnerability could allow an unauthenticated attacker to bypass security controls. This allows a remote, unauthenticated attacker to potentially execute arbitrary JavaScript code.
- WordPress (CVE-2025-5394): The "Alone – Charity Multipurpose Non-profit WordPress Theme" for WordPress is vulnerable to arbitrary file uploads. A missing capability check allows unauthenticated attackers to upload ZIP files containing webshells disguised as plugins, leading to remote code execution.

**Impact**

These vulnerabilities span a broad range of enterprise technologies, including network access control systems, monitoring platforms, web servers, CMS platforms, cloud services, and collaboration tools. Exploitation techniques range from remote code execution and command injection to authentication bypass, SQL injection, path traversal, and configuration weaknesses.

A critical flaw in perimeter devices like Ivanti EPMM or SonicWall SMA could allow an unauthenticated attacker to gain remote code execution, completely breaching the primary network defense. A separate vulnerability within Cisco's Identity Services Engine could then be exploited to bypass network segmentation, granting an attacker widespread internal access. Insecure deserialization issues in platforms like Wazuh Server and CrushFTP could then be used to run malicious payloads or steal sensitive files from administrative consoles. Weaknesses in web delivery controllers like Ingress-Nginx or popular content management systems such as WordPress, SharePoint, and Kentico Xperience create vectors to bypass security controls, exfiltrate confidential data, or fully compromise servers.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...51bc8df1 | 100538 | GeoServer - SSRF - CVE:CVE-2024-29198 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...c9e0b290 | 100548 | Ivanti EPMM - Remote Code Execution - CVE:CVE-2025-6771 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...ad93cda8 | 100550 | Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38018 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...1dca5738 | 100562 | Manager-IO - SSRF - CVE:CVE-2025-54122 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...2e9137e1 | 100565 | Cisco Identity Services Engine - Remote Code Execution - CVE:CVE-2025-20281 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5d8102e1 | 100567 | Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1974 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...99105c43 | 100569 | PaperCut NG/MF - Remote Code Execution - CVE:CVE-2023-2533 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...2c81dc88 | 100571 | SonicWall SMA - XSS - CVE:CVE-2025-40598 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...926c96d4 | 100573 | WordPress - Dangerous File Upload - CVE:CVE-2025-5394 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...40ec2fda

100806  
 | Wazuh Server - Remote Code Execution - CVE:CVE-2025-24016 | Log | Block | This is a New Detection

 |
| Cloudflare Managed Ruleset | ...2401fa3b

100824 | CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 | Log | Block  
 | This is a New Detection

 |
| Cloudflare Managed Ruleset | ...74920ace

100824A | CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 2 | Log | Block  
 | This is a New Detection

 |
| Cloudflare Managed Ruleset | ...c7e63549 | 100825 | AMI MegaRAC - Auth Bypass - CVE:CVE-2024-54085 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...b79037e6 | 100826 | Kentico Xperience CMS - Auth Bypass - CVE:CVE-2025-2747 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...caf261aa | 100827 | Kentico Xperience CMS - XSS - CVE:CVE-2025-2748 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...6f1c2d12 | 100828 | Node.js - Directory Traversal - CVE:CVE-2025-27210 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0341fccc | 100829 | WordPress:Plugin:Simple File List - Remote Code Execution - CVE:CVE-2025-34085 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...4cefeeda | 100829A | WordPress:Plugin:Simple File List - Remote Code Execution - CVE:CVE-2025-34085 - 2 | Log | Disabled | This is a New Detection |

Aug 8, 2025

[<h2>Wrangler and the Cloudflare Vite plugin support \`.env\` files in local development</h2>](https://developers.cloudflare.com/changelog/post/2025-08-08-dot-env-in-local-dev/)

[Workers](https://developers.cloudflare.com/workers/)

Now, you can use `.env` files to provide secrets and override environment variables on the `env` object during local development with Wrangler and the Cloudflare Vite plugin.

Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use `.dev.vars` files. This is still supported, but you can now also use `.env` files, which are more familiar to many developers.

#### Using `.env` files in local development

You can create a `.env` file in your project root to define environment variables that will be used when running `wrangler dev` or `vite dev`. The `.env` file should be formatted like a `dotenv` file, such as `KEY="VALUE"`:

*.envbash*

```bash
TITLE="My Worker"
API_TOKEN="dev-token"
```

When you run `wrangler dev` or `vite dev`, the environment variables defined in the `.env` file will be available in your Worker code via the `env` object:

```javascript
export default {
	async fetch(request, env) {
		const title = env.TITLE; // "My Worker"
		const apiToken = env.API_TOKEN; // "dev-token"
		const response = await fetch(
			`https://api.example.com/data?token=${apiToken}`,
		);
		return new Response(`Title: ${title} - ` + (await response.text()));
	},
};
```

#### Multiple environments with `.env` files

If your Worker defines multiple [environments](https://developers.cloudflare.com/workers/wrangler/environments/), you can set different variables for each environment (ex: production or staging) by creating files named `.env.<environment-name>`.

When you use `wrangler <command> --env <environment-name>` or `CLOUDFLARE_ENV=<environment-name> vite dev`, the corresponding environment-specific file will also be loaded and merged with the `.env` file.

For example, if you want to set different environment variables for the `staging` environment, you can create a file named `.env.staging`:

*.env.stagingbash*

```bash
API_TOKEN="staging-token"
```

When you run `wrangler dev --env staging` or `CLOUDFLARE_ENV=staging vite dev`, the environment variables from `.env.staging` will be merged onto those from `.env`.

```javascript
export default {
	async fetch(request, env) {
		const title = env.TITLE; // "My Worker" (from `.env`)
		const apiToken = env.API_TOKEN; // "staging-token" (from `.env.staging`, overriding the value from `.env`)
		const response = await fetch(
			`https://api.example.com/data?token=${apiToken}`,
		);
		return new Response(`Title: ${title} - ` + (await response.text()));
	},
};
```

#### Find out more

For more information on how to use `.env` files with Wrangler and the Cloudflare Vite plugin, see the following documentation:

- [Environment variables and secrets](https://developers.cloudflare.com/workers/local-development/environment-variables)
- [Wrangler Documentation ↗︎](https://developers.cloudflare.com/workers/wrangler)
- [Cloudflare Vite Plugin Documentation ↗︎](https://developers.cloudflare.com/workers/wrangler/vite)

Aug 8, 2025

[<h2>Introducing observability and metrics for Stream Live Inputs</h2>](https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/)

[Stream](https://developers.cloudflare.com/stream/)

New information about broadcast metrics and events is now available in [Cloudflare Stream](https://developers.cloudflare.com/stream/) in the Live Input details of the Dashboard.

![Live Input details showing metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1382,height=907,format=webp/_astro/2025-08-05-live-input-metrics.B31Z3RGB.png)

You can now easily understand broadcast-side health and performance with new observability, which can help when troubleshooting common issues, particularly for new customers who are just getting started, and platform customers who may have limited visibility into how their end-users configure their encoders.

To get started, start a live stream ([just getting started?](https://developers.cloudflare.com/stream/examples/obs-from-scratch/)), then visit the Live Input details page in Dash.

See our new live [Troubleshooting](https://developers.cloudflare.com/stream/stream-live/troubleshooting/) guide to learn what these metrics mean and how to use them to address common broadcast issues.

Aug 8, 2025

[<h2>Directly import \`waitUntil\` in Workers for easily spawning background tasks</h2>](https://developers.cloudflare.com/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/)

[Workers](https://developers.cloudflare.com/workers/)

You can now import [`waitUntil`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) from `cloudflare:workers` to extend your Worker's execution beyond the request lifecycle from anywhere in your code.

Previously, `waitUntil` could only be accessed through the [execution context](https://developers.cloudflare.com/workers/runtime-apis/context/) (`ctx`) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the `ctx` object through multiple function calls to access `waitUntil`.

Now, you can import `waitUntil` directly and use it anywhere in your Worker without needing to pass `ctx` as a parameter:

```js
import { waitUntil } from "cloudflare:workers";

export function trackAnalytics(eventData) {
	const analyticsPromise = fetch("https://analytics.example.com/track", {
		method: "POST",
		body: JSON.stringify(eventData),
	});

	// Extend execution to ensure analytics tracking completes
	waitUntil(analyticsPromise);
}
```

This is particularly useful when you want to:

- Schedule background tasks from utility functions or modules
- Extend execution for analytics, logging, or cleanup operations
- Avoid passing the execution context through multiple layers of function calls

```js
import { waitUntil } from "cloudflare:workers";

export default {
	async fetch(request, env, ctx) {
		// Background task that should complete even after response is sent
		cleanupTempData(env.KV_NAMESPACE);
		return new Response("Hello, World!");
	}
};

function cleanupTempData(kvNamespace) {
	// This function can now use waitUntil without needing ctx
	const deletePromise = kvNamespace.delete("temp-key");
	waitUntil(deletePromise);
}
```

Note

The imported `waitUntil` function works the same way as [`ctx.waitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil). It extends your Worker's execution to wait for the provided promise to settle, but does not block the response from being sent to the client.

For more information, see the [`waitUntil` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil).

Aug 7, 2025

[<h2>Expanded Email Link Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.

For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.

![Expanded Email Link Isolation Configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=497,format=webp/_astro/expanded-link-actions.DziIg6E8.jpg)

To isolate all links within a message based on the disposition, select **Settings** > **Link Actions** > **View** and select **Configure**. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on [Configure link actions ↗︎](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/).

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Aug 7, 2025

[<h2>WAF Release - 2025-08-07 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-08-07-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s highlight focuses on two critical vulnerabilities affecting key infrastructure and enterprise content management platforms. Both flaws present significant remote code execution risks that can be exploited with minimal or no user interaction.

**Key Findings**

- Squid (≤6.3) — CVE-2025-54574: A heap buffer overflow occurs when processing Uniform Resource Names (URNs). This vulnerability may allow remote attackers to execute arbitrary code on the server. The issue has been resolved in version 6.4.
- Adobe AEM (≤6.5.23) — CVE-2025-54253: Due to a misconfiguration, attackers can achieve remote code execution without requiring any user interaction, posing a severe threat to affected deployments.

**Impact**

Both vulnerabilities expose critical attack vectors that can lead to full server compromise. The Squid heap buffer overflow allows remote code execution by crafting malicious URNs, which can lead to server takeover or denial of service. Given Squid’s widespread use as a caching proxy, this flaw could be exploited to disrupt network traffic or gain footholds inside secure environments.

Adobe AEM’s remote code execution vulnerability enables attackers to run arbitrary code on the content management server without any user involvement. This puts sensitive content, application integrity, and the underlying infrastructure at extreme risk. Exploitation could lead to data theft, defacement, or persistent backdoor installation.

These findings reinforce the urgency of updating to the patched versions — Squid 6.4 and Adobe AEM 6.5.24 or later — and reviewing configurations to prevent exploitation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...ef7e015b | 100844 | Adobe Experience Manager Forms - Remote Code Execution - CVE:CVE-2025-54253 | N/A | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...baec057a | 100840 | Squid - Buffer Overflow - CVE:CVE-2025-54574 | N/A | Block | This is a New Detection |

Aug 7, 2025

[<h2>Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</h2>](https://developers.cloudflare.com/changelog/post/2025-08-07-cache-no-cache/)

[Workers](https://developers.cloudflare.com/workers/)

By setting the value of the `cache` property to `no-cache`, you can force [Cloudflare's cache](https://developers.cloudflare.com/workers/reference/how-the-cache-works/) to revalidate its contents with the origin when making subrequests from [Cloudflare Workers](https://developers.cloudflare.com/workers).

*index.jsjs*

```js
export default {
	async fetch(req, env, ctx) {
		const request = new Request("https://cloudflare.com", {
			cache: "no-cache",
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
		const request = new Request("https://cloudflare.com", { cache: 'no-cache'});
		const response = await fetch(request);
    return response;
  }
} satisfies ExportedHandler<Environment>
```

When `no-cache` is set, the Worker request will first look for a match in Cloudflare's cache, then:

- If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.
- If there is no match, Workers will make a standard request to the origin and cache the response.

This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the [`cache`](https://developers.cloudflare.com/workers/runtime-apis/request/#options) property, which is a cross-platform standard part of the [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) interface. Previously, if you set the `cache` property on `Request` to `'no-cache'`, the Workers runtime threw an exception.

- Learn [how the Cache works with Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
- Enable [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) for your Cloudflare Worker
- Explore [Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) and [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available in Cloudflare Workers

Aug 6, 2025

[<h2>Improvements to Monitoring Using Zone Settings</h2>](https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.

All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.

#### What you can expect:

- More reliable application of zone settings to monitoring requests, including
  - Authenticated Origin Pulls
  - Aegis Egress IP Pools
  - Argo Smart Routing
  - HTTP/2 to Origin
- Improved support and bug fixes for retries, redirects, and proxied origin resolution
- Improved performance and reliability of monitoring requests within the Cloudflare network
- Unrelated CDN or WAF configuration changes should have no risk of impact to pool health

Aug 6, 2025

[<h2>Certificate Transparency Insights in Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-08-04-radar-ct-insights/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Certificate Transparency (CT) insights, providing visibility into certificate issuance trends based on Certificate Transparency logs currently monitored by Cloudflare.

The following API endpoints are now available:

- [`/ct/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries/): Retrieves certificate issuance time series.
- [`/ct/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/summary/): Retrieves certificate distribution by dimension.
- [`/ct/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries_groups/): Retrieves time series of certificate distribution by dimension.
- [`/ct/authorities`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/list/): Lists certification authorities.
- [`/ct/authorities/{ca_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/get/): Retrieves details about a Certification Authority (CA). CA information is derived from the [Common CA Database (CCADB) ↗︎](https://www.ccadb.org/).
- [`/ct/logs`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/list/): Lists CT logs.
- [`/ct/logs/{log_slug}`](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get/): Retrieves details about a CT log. CT log information is derived from the [Google Chrome log list ↗︎](https://googlechrome.github.io/CertificateTransparency/log_lists.html).

For the `summary` and `timeseries_groups` endpoints, the following dimensions are available (and also usable as filters):

- `ca`: Certification Authority (certificate issuer)
- `ca_owner`: Certification Authority Owner
- `duration`: Certificate validity duration (between NotBefore and NotAfter dates)
- `entry_type`: Entry type (certificate vs. pre-certificate)
- `expiration_status`: Expiration status (valid vs. expired)
- `has_ips`: Presence of IP addresses in certificate [Subject Alternative Names (SANs) ↗︎](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/#hostname-and-wildcard-coverage)
- `has_wildcards`: Presence of wildcard DNS names in certificate SANs
- `log`: CT log name
- `log_api`: CT log API ([RFC6962 ↗︎](https://datatracker.ietf.org/doc/html/rfc6962) vs. [Static ↗︎](https://c2sp.org/static-ct-api))
- `log_operator`: CT log operator
- `public_key_algorithm`: Public key algorithm of certificate's key
- `signature_algorithm`: Signature algorithm used by CA to sign certificate
- `tld`: Top-level domain for DNS names found in certificates SANs
- `validation_level`: [Validation level ↗︎](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)

Check out the new Certificate Transparency insights in the [new Radar page ↗︎](https://radar.cloudflare.com/certificate-transparency).

Aug 5, 2025

[<h2>Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</h2>](https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

The latest releases of [@cloudflare/agents ↗︎](https://github.com/cloudflare/agents) brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:

#### MCP elicitation support

MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.

```ts
// Request user confirmation via elicitation
const confirmation = await this.elicitInput({
	message: `Are you sure you want to increment the counter by ${amount}?`,
	requestedSchema: {
		type: "object",
		properties: {
			confirmed: {
				type: "boolean",
				title: "Confirm increment",
				description: "Check to confirm the increment",
			},
		},
		required: ["confirmed"],
	},
});
```

Check out our [demo ↗︎](https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo) to see elicitation in action.

#### HTTP streamable transport for MCP

MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:

- **Better performance**: More efficient data streaming and reduced overhead
- **Improved reliability**: Enhanced connection stability and error recover- **Automatic fallback**: If streamable transport is not available, it gracefully falls back to SSE

```ts
export default MyMCP.serve("/mcp", {
	binding: "MyMCP",
});
```

The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.

#### Enhanced MCP connectivity

Significant improvements to MCP server connections and transport reliability:

- **Auto transport selection**: Automatically determines the best transport method, falling back from streamable-http to SSE as needed
- **Improved error handling**: Better connection state management and error reporting for MCP servers
- **Reliable prop updates**: Centralized agent property updates ensure consistency across different contexts

#### Lightweight .queue for fast task deferral

You can use `.queue()` to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.

```ts
class MyAgent extends Agent {
	doSomethingExpensive(payload) {
		// a long running process that you want to run in the background
	}

	queueSomething() {
		await this.queue("doSomethingExpensive", somePayload); // this will NOT block further execution, and runs in the background
		await this.queue("doSomethingExpensive", someOtherPayload); // the callback will NOT run until the previous callback is complete
		// ... call as many times as you want
	}
}
```

Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.

#### New email adapter

Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.

```ts
export class EmailAgent extends Agent {
	async onEmail(email: AgentEmail) {
		const raw = await email.getRaw();
		const parsed = await PostalMime.parse(raw);

		// create a response based on the email contents
		// and then send a reply

		await this.replyToEmail(email, {
			fromName: "Email Agent",
			body: `Thanks for your email! You've sent us "${parsed.subject}". We'll process it shortly.`,
		});
	}
}
```

You route incoming mail like this:

```ts
export default {
	async email(email, env) {
		await routeAgentEmail(email, env, {
			resolver: createAddressBasedEmailResolver("EmailAgent"),
		});
	},
};
```

You can find a full example [here ↗︎](https://github.com/cloudflare/agents/tree/main/examples/email-agent).

#### Automatic context wrapping for custom methods

Custom methods are now automatically wrapped with the agent's context, so calling `getCurrentAgent()` should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.

```ts
export class MyAgent extends Agent {
	async suggestReply(message) {
		// getCurrentAgent() now correctly works, even when called inside an RPC method
		const { agent } = getCurrentAgent()!;
		return generateText({
			prompt: `Suggest a reply to: "${message}" from "${agent.name}"`,
			tools: [replyWithEmoji],
		});
	}
}
```

Try it out and tell us what you build!

Aug 5, 2025

[<h2>Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</h2>](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

We’ve shipped a major release for the [@cloudflare/sandbox ↗︎](https://github.com/cloudflare/sandbox-sdk) SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.

This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.

This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.

#### Code interpreter (Python, JS, TS)

Create persistent code contexts with support for rich visual + structured outputs.

#### createCodeContext(options)

Creates a new code execution context with persistent state.

```ts
// Create a Python context
const pythonCtx = await sandbox.createCodeContext({ language: "python" });

// Create a JavaScript context
const jsCtx = await sandbox.createCodeContext({ language: "javascript" });
```

Options:

- language: Programming language ('python' | 'javascript' | 'typescript')
- cwd: Working directory (default: /workspace)
- envVars: Environment variables for the context

#### runCode(code, options)

Executes code with optional streaming callbacks.

```ts
// Simple execution
const execution = await sandbox.runCode('print("Hello World")', {
	context: pythonCtx,
});

// With streaming callbacks
await sandbox.runCode(
	`
for i in range(5):
    print(f"Step {i}")
    time.sleep(1)
`,
	{
		context: pythonCtx,
		onStdout: (output) => console.log("Real-time:", output.text),
		onResult: (result) => console.log("Result:", result),
	},
);
```

Options:

- language: Programming language ('python' | 'javascript' | 'typescript')
- cwd: Working directory (default: /workspace)
- envVars: Environment variables for the context

#### Real-time streaming output

Returns a streaming response for real-time processing.

```ts
const stream = await sandbox.runCodeStream(
	"import time; [print(i) for i in range(10)]",
);
// Process the stream as needed
```

#### Rich output handling

Interpreter outputs are auto-formatted and returned in multiple formats:

- text
- html (e.g., Pandas tables)
- png, svg (e.g., Matplotlib charts)
- json (structured data)
- chart (parsed visualizations)

```ts
const result = await sandbox.runCode(
	`
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")
pivot = data.pivot("month", "year", "passengers")
sns.heatmap(pivot, annot=True, fmt="d")
plt.title("Flight Passengers")
plt.show()

pivot.to_dict()
`,
	{ context: pythonCtx },
);

if (result.png) {
	console.log("Chart output:", result.png);
}
```

#### Preview URLs from Exposed Ports

Start background processes and expose them with live URLs.

```ts
await sandbox.startProcess("python -m http.server 8000");
const preview = await sandbox.exposePort(8000);

console.log("Live preview at:", preview.url);
```

#### Full process lifecycle control

Start, inspect, and terminate long-running background processes.

```ts
const process = await sandbox.startProcess("node server.js");
console.log(`Started process ${process.id} with PID ${process.pid}`);

// Monitor the process
const logStream = await sandbox.streamProcessLogs(process.id);
for await (const log of parseSSEStream<LogEvent>(logStream)) {
	console.log(`Server: ${log.data}`);
}
```

- listProcesses() - List all running processes
- getProcess(id) - Get detailed process status
- killProcess(id, signal) - Terminate specific processes
- killAllProcesses() - Kill all processes
- streamProcessLogs(id, options) - Stream logs from running processes
- getProcessLogs(id) - Get accumulated process output

#### Git integration

Clone Git repositories directly into the sandbox.

```ts
await sandbox.gitCheckout("https://github.com/user/repo", {
	branch: "main",
	targetDir: "my-project",
});
```

Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

Aug 5, 2025

[<h2>OpenAI open models now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2025-08-05-openai-open-models/)

[Agents](https://developers.cloudflare.com/agents/) [Workers AI](https://developers.cloudflare.com/workers-ai/)

We're thrilled to be a Day 0 partner with [OpenAI ↗︎](http://openai.com/index/introducing-gpt-oss) to bring their [latest open models ↗︎](https://openai.com/index/gpt-oss-model-card/) to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).

Get started with the new models at `@cf/openai/gpt-oss-120b` and `@cf/openai/gpt-oss-20b`. Check out the [blog ↗︎](https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai) for more details about the new models, and the [`gpt-oss-120b`](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b) and [`gpt-oss-20b`](https://developers.cloudflare.com/workers-ai/models/gpt-oss-20b) model pages for more information about pricing and context windows.

#### Responses API

If you call the model through:

- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`

```plaintext
curl https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLOUDFLARE_API_KEY" \
  -d '{
    "model": "@cf/openai/gpt-oss-120b",
    "reasoning": {"effort": "medium"},
    "input": [
      {
        "role": "user",
        "content": "What are the benefits of open-source models?"
      }
    ]
  }'
```

#### Code Interpreter

The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK ↗︎](https://github.com/cloudflare/sandbox-sdk) and [Containers ↗︎](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.

#### Web Search (coming soon)

We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.

Aug 4, 2025

[<h2>Increased disk space for Workers Builds</h2>](https://developers.cloudflare.com/changelog/post/2025-08-04-builds-increased-disk-size/)

[Workers](https://developers.cloudflare.com/workers/)

As part of the ongoing open beta for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), we’ve increased the available disk space for builds from **8 GB** to **20 GB** for both Free and Paid plans.

This provides more space for larger projects, dependencies, and build artifacts while improving overall build reliability.

| Metric | Free Plan | Paid Plans |
| --- | --- | --- |
| Disk Space | 20 GB | 20 GB |

All other [build limits](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) — including CPU, memory, build minutes, and timeout remain unchanged.

Aug 4, 2025

[<h2>WAF Release - 2025-08-04</h2>](https://developers.cloudflare.com/changelog/post/2025-08-04-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's highlight focuses on a series of significant vulnerabilities identified across widely adopted web platforms, from enterprise-grade CMS to essential backend administration tools. The findings reveal multiple vectors for attack, including critical flaws that allow for full server compromise and others that enable targeted attacks against users.

**Key Findings**

- Sitecore (CVE-2025-34509, CVE-2025-34510, CVE-2025-34511): A hardcoded credential allows remote attackers to access administrative APIs. Once authenticated, they can exploit an additional vulnerability to upload arbitrary files, leading to remote code execution.
- Grafana (CVE-2025-4123): A cross-site scripting (XSS) vulnerability allows an attacker to redirect users to a malicious website, which can then execute arbitrary JavaScript in the victim's browser.
- LaRecipe (CVE-2025-53833): Through Server-Side Template Injection, attackers can execute arbitrary commands on the server, potentially access sensitive environment variables, and escalate access depending on server configuration.
- CentOS WebPanel (CVE-2025-48703): A command injection vulnerability could allow a remote attacker to execute arbitrary commands on the server.
- WordPress (CVE-2023-5561): This vulnerability allows unauthenticated attackers to determine the email addresses of users who have published public posts on an affected website.
- WordPress Plugin - WPBookit (CVE-2025-6058): A missing file type validation allows unauthenticated attackers to upload arbitrary files to the server, creating the potential for remote code execution.
- WordPress Theme - Motors (CVE-2025-4322): Due to improper identity validation, an unauthenticated attacker can change the passwords of arbitrary users, including administrators, to gain access to their accounts.

**Impact**

These vulnerabilities pose a multi-layered threat to widely adopted web technologies, ranging from enterprise-grade platforms like Sitecore to everyday solutions such as WordPress, and backend tools like CentOS WebPanel. The most severe risks originate in remote code execution (RCE) flaws found in Sitecore, CentOS WebPanel, LaRecipe, and the WPBookit plugin. These allow attackers to bypass security controls and gain deep access to the server, enabling them to steal sensitive data, deface websites, install persistent malware, or use the compromised server as a launchpad for further attacks.

The privilege escalation vulnerability is the Motors theme, which allows for a complete administrative account takeover on WordPress sites. This effectively hands control of the application to an attacker, who can then manipulate content, exfiltrate user data, and alter site functionality without needing to breach the server itself.

The Grafana cross-site scripting (XSS) flaw can be used to hijack authenticated user sessions or steal credentials, turning a trusted user's browser into an attack vector.

Meanwhile, the information disclosure flaw in WordPress core provides attackers with valid user emails, fueling targeted phishing campaigns that aim to secure the same account access achievable through the other exploits.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...52f30a13 | 100535A | Sitecore - Dangerous File Upload - CVE:CVE-2025-34510, CVE:CVE-2025-34511 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5045a97f | 100535 | Sitecore - Information Disclosure - CVE:CVE-2025-34509 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...579cd3e0 | 100543 | Grafana - Directory Traversal - CVE:CVE-2025-4123 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0cbd9abc | 100545 | WordPress - Information Disclosure - CVE:CVE-2023-5561 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...8f634977 | 100820 | CentOS WebPanel - Remote Code Execution - CVE:CVE-2025-48703 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...82ae64c1 | 100821 | LaRecipe - SSTI - CVE:CVE-2025-53833 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...194f7b2d | 100822 | WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0bf1b661 | 100823 | WordPress:Theme:Motors - Privilege Escalation - CVE:CVE-2025-4322 | Log | Block | This is a New Detection |

Aug 1, 2025

[<h2>Terraform v5.8.2 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-08-01-terraform-v5.8.2-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.

Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.

#### Changes

- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2) in GitHub.

#### Issues Closed

- [#5666: cloudflare\_ruleset example lists id which is a read-only field ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare\_logpush\_job plan always suggests changes ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare\_list\_item would be recreated "created" state ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare\_zone\_subscription: uses wrong ID field in Read/Update ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare\_api\_token resource always shows changes (drift) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare\_workers\_script with bindings fails to be destroyed ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare\_workers\_script Unable to deploy worker assets ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare\_workers\_script 500 internal server error when uploading python ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare\_workers\_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare\_workers\_script randomly fails to deploy when changing compatibility\_date ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare\_workers\_script (v5.2.0) ignoring content and bindings properties ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare\_workers\_script always detects changes after apply ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare\_zero\_trust\_access\_identity\_provider gives recurring change on OTP pin login ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare\_r2\_custom\_domain doesn't roundtrip jurisdiction properly ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare\_api\_shield\_schema resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Aug 1, 2025

[<h2>Develop locally with Containers and the Cloudflare Vite plugin</h2>](https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/)

[Workers](https://developers.cloudflare.com/workers/)

You can now configure and run [Containers](https://developers.cloudflare.com/containers) alongside your [Worker](https://developers.cloudflare.com/workers) during local development when using the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Previously, you could only develop locally when using [Wrangler](https://developers.cloudflare.com/workers/wrangler/) as your local development server.

#### Configuration

You can simply configure your Worker and your Container(s) in your Wrangler configuration file:

```jsonc
{
  "name": "container-starter",
  "main": "src/index.js",
  "containers": [
    {
      "class_name": "MyContainer",
      "image": "./Dockerfile",
      "instances": 5
    }
  ],
  "durable_objects": {
    "bindings": [
      {
        "class_name": "MyContainer",
        "name": "MY_CONTAINER"
      }
    ]
  },
  "migrations": [
    {
      "new_sqlite_classes": [
        "MyContainer"
      ],
      "tag": "v1"
    }
  ],
}
```

```toml
name = "container-starter"
main = "src/index.js"

[[containers]]
class_name = "MyContainer"
image = "./Dockerfile"
instances = 5

[[durable_objects.bindings]]
class_name = "MyContainer"
name = "MY_CONTAINER"

[[migrations]]
new_sqlite_classes = [ "MyContainer" ]
tag = "v1"
```

#### Worker Code

Once your Worker and Containers are configured, you can access the Container instances from your Worker code:

```ts
import { Container, getContainer } from "@cloudflare/containers";

export class MyContainer extends Container {
  defaultPort = 4000; // Port the container is listening on
  sleepAfter = "10m"; // Stop the instance if requests not sent for 10 minutes
}

async fetch(request, env) {
  const { "session-id": sessionId } = await request.json();
  // Get the container instance for the given session ID
  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)
  // Pass the request to the container instance on its default port
  return containerInstance.fetch(request);
}
```

#### Local development

To develop your Worker locally, start a local dev server by running

```sh
vite dev
```

in your terminal.

#### Resources

Learn more about [Cloudflare Containers ↗︎](https://developers.cloudflare.com/containers/) or the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/) in our developer docs.

Jul 31, 2025

[<h2>Terraform V5 support for tunnels and routes</h2>](https://developers.cloudflare.com/changelog/post/2025-07-31-terraform-v5-tunnels-routes/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.

For more information, refer to the [Cloudflare Terraform provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

Jul 30, 2025

[<h2>Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</h2>](https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/)

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU ([Customer Metadata Boundary - Europe](https://developers.cloudflare.com/data-localization/metadata-boundary/)) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.

This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.

Specifically, these two GraphQL endpoints are now compatible with CMB EU:

- `magicTransitTunnelHealthChecksAdaptiveGroups`
- `magicTransitTunnelTrafficAdaptiveGroups`

Jul 29, 2025

[<h2>Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/)

[Workers](https://developers.cloudflare.com/workers/) [Secrets Store](https://developers.cloudflare.com/secrets-store/)

Any template which uses [Worker environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), or [Secrets Store secrets](https://developers.cloudflare.com/secrets-store/) can now be deployed using a [Deploy to Cloudflare button](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

Define environment variables and secrets store bindings in your Wrangler configuration file as normal:

```jsonc
{
  "name": "my-worker",
  "main": "./src/index.ts",
	// Set this to today's date
	"compatibility_date": "2026-10-05",
  "vars": {
    "API_HOST": "https://example.com",
  },
	"secrets_store_secrets": [
		{
			"binding": "API_KEY",
			"store_id": "demo",
			"secret_name": "api-key"
		}
	]
}
```

```toml
name = "my-worker"
main = "./src/index.ts"
# Set this to today's date
compatibility_date = "2026-10-05"

[vars]
API_HOST = "https://example.com"

[[secrets_store_secrets]]
binding = "API_KEY"
store_id = "demo"
secret_name = "api-key"
```

Add secrets to a `.dev.vars.example` or `.env.example` file:

*.dev.vars.exampleini*

```ini
COOKIE_SIGNING_KEY=my-secret # comment
```

And optionally, you can add a description for these bindings in your template's `package.json` to help users understand how to configure each value:

*package.jsonjson*

```json
{
	"name": "my-worker",
	"private": true,
	"cloudflare": {
		"bindings": {
			"API_KEY": {
				"description": "Select your company's API key for connecting to the example service."
			},
			"COOKIE_SIGNING_KEY": {
				"description": "Generate a random string using `openssl rand -hex 32`."
			}
		}
	}
}
```

These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in [our documentation](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

Jul 29, 2025

[<h2>Audit logs (version 2) - UI Beta Release</h2>](https://developers.cloudflare.com/changelog/post/2025-07-29-audit-logs-v2-ui-beta/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

The Audit Logs v2 UI is now available to all Cloudflare customers in Beta. This release builds on the public [Beta of the Audit Logs v2 API](https://developers.cloudflare.com/changelog/product/audit-logs/) and introduces a redesigned user interface with powerful new capabilities to make it easier to investigate account activity.

**Enabling the new UI**

To try the new user interface, go to **Manage Account > Audit Logs**. The previous version of Audit Logs remains available and can be re-enabled at any time using the **Switch back to old Audit Logs** link in the banner at the top of the page.

**New Features:**

- **Advanced Filtering**: Filter logs by actor, resource, method, and more for faster insights.
- **On-hover filter controls**: Easily include or exclude values in queries by hovering over fields within a log entry.
- **Detailed Log Sidebar**: View rich context for each log entry without leaving the main view.
- **JSON Log View**: Inspect the raw log data in a structured JSON format.
- **Custom Time Ranges**: Define your own time windows to view historical activity.
- **Infinite Scroll**: Seamlessly browse logs without clicking through pages.

![Audit Logs v2 new UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1300,height=686,format=webp/_astro/Audit_logs_v2_filters.Bacd1IHg.png)

For more details on Audit Logs v2, see the [Audit Logs documentation ↗︎](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

**Known issues**

- A small number of audit logs may currently be unavailable in Audit Logs v2. In some cases, certain fields such as actor information may be missing in certain audit logs. We are actively working to improve coverage and completeness for General Availability.
- Export to CSV is not supported in the new UI.

We are actively refining the Audit Logs v2 experience and welcome your feedback. You can share overall feedback by clicking the thumbs up or thumbs down icons at the top of the page, or provide feedback on specific audit log entries using the thumbs icons next to each audit log line or by filling out our [feedback form ↗︎](https://docs.google.com/forms/d/e/1FAIpQLSfXGkJpOG1jUPEh-flJy9B13icmcdBhveFwe-X0EzQjJQnQfQ/viewform?usp=sharing).

Jul 28, 2025

[<h2>Introducing pricing for the Browser Rendering API — $0.09 per browser hour</h2>](https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

We’ve launched pricing for [Browser Rendering](https://developers.cloudflare.com/browser-run/), including a free tier and a pay-as-you-go model that scales with your needs. Starting **August 20, 2025**, Cloudflare will begin billing for Browser Rendering.

There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:

- [**REST API**](https://developers.cloudflare.com/browser-run/quick-actions/): Charged for **Duration** only ($/browser hour)
- [**Browser Sessions**](https://developers.cloudflare.com/browser-run/#integration-methods): Charged for both **Duration** and **Concurrency** ($/browser hour and # of concurrent browsers)

Included usage and pricing by plan

| Plan | Included duration | Included concurrency | Price (beyond included) |
| --- | --- | --- | --- |
| **Workers Free** | 10 minutes per day | 3 concurrent browsers | N/A |
| **Workers Paid** | 10 hours per month | 10 concurrent browsers (averaged monthly) | **1. REST API**: $0.09 per additional browser hour <br>**2. Workers Bindings**: $0.09 per additional browser hour <br> $2.00 per additional concurrent browser |

What you need to know:

- **Workers Free Plan:** 10 minutes of browser usage per day with 3 concurrent browsers at no charge.
- **Workers Paid Plan:** 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.

You can monitor usage via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run). Go to **Compute** > **Browser Run**.

![Browser Rendering dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1880,height=1080,format=webp/_astro/dashboard.BQnX87lT.png)

If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's [included usage](https://developers.cloudflare.com/browser-run/pricing/). To estimate costs, take a look at these [example pricing scenarios](https://developers.cloudflare.com/browser-run/pricing/#examples-of-workers-paid-pricing).

Jul 28, 2025

[<h2>Scam domain category introduced under Security Threats</h2>](https://developers.cloudflare.com/changelog/post/2025-07-28-Spam-domain-category-introduced/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We have introduced a new Security Threat category called **Scam**. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.

**New category added**

| Parent ID | Parent Name | Category ID | Category Name |
| --- | --- | --- | --- |
| 21 | Security Threats | 191 | Scam |

Refer to [Gateway domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/41/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/41/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
