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

Aug 17, 2026

[<h2>Qwen 3.8 27B now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/qwen/qwen3.8-27b`](https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/) is now available on Workers AI.

Qwen 3.8 27B is a 27-billion-parameter instruction-tuned vision language model from Alibaba's Qwen family. It processes images and text together, with reasoning and function calling for agentic workflows.

**Key capabilities:**

- **Vision**: Accept image and text inputs and generate text responses.
- **Reasoning**: Support thinking mode for complex, step-by-step problem-solving.
- **Function calling**: Build agents that invoke tools and APIs across multiple conversation turns.
- **262,144 token context window**: Retain long conversations and multimodal inputs across extended agent sessions.

Use Qwen 3.8 27B through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Qwen 3.8 27B model page](https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 14, 2026

[<h2>WebSocket reporting now includes full connection data transfer and duration</h2>](https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/)

[Analytics](https://developers.cloudflare.com/analytics/)

Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial `101 Switching Protocols` handshake for some WebSocket connections.

Customers with WebSocket traffic will see the correct **Data Transfer** in the dashboard and `EdgeResponseBytes` in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.

The separate [WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/) continues to provide per-connection directional byte counts, timestamps, and close details.

For more information about HTTP Traffic Analytics, refer to [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/#http-traffic).

Aug 14, 2026

[<h2>DeepSeek V4 Flash and Pro now available on Workers AI</h2>](https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/deepseek-ai/deepseek-v4-pro-0813`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/) and [`@cf/deepseek-ai/deepseek-v4-flash-0731`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) are now available on Workers AI.

DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full **one million (1,048,576) token context window**. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.

DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.

**Key capabilities:**

- **Reasoning**: Both models support thinking mode for complex, step-by-step problem-solving.
- **Function calling**: Build agents that invoke tools and APIs across multiple conversation turns.
- **Long context**: Both models support a full 1,048,576 token context window.

Both models require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use these models through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [DeepSeek V4 Pro model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/), the [DeepSeek V4 Flash model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 14, 2026

[<h2>You can now enable Access on a Worker or all Workers at once</h2>](https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/)

[Workers](https://developers.cloudflare.com/workers/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You now have two new ways to protect your [Workers](https://developers.cloudflare.com/workers/) with [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/).

**Protect an application across all its domains at once**

Until now, if a Worker was reachable on a route, a Custom Domain, and a `workers.dev` URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.

Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.

![Access setting for protecting a single Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=689,format=webp/_astro/protect-one-worker.BSpeeOry.png)

**Protect all new and existing Workers by default**

Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.

![Account-wide Access setting that protects all Workers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2436,height=1432,format=webp/_astro/protect-all-workers._AWy-S-E.png)

If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.

![Make a Worker public when all Workers are protected](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1228,height=756,format=webp/_astro/make-worker-public.D3yjPjtf.png)

Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.

For more advanced policy options, edit the policy in [Zero Trust ↗︎](https://dash.cloudflare.com/?to=/:account/one/access/apps).

![Access policy configuration for controlling who can sign in](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1276,height=1220,format=webp/_astro/choose-who-can-sign-in.DKf3kWAK.png)

**View all of your Worker Access policies**

You can view and manage all of your Access policies in the **Access** tab of the Workers & Pages section in the dashboard.

![Access tab showing all configured Access policies](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1646,height=1366,format=webp/_astro/access-policies.DN7yCwHX.png)

**See who is accessing your Worker**

When Access is enabled on your Worker, every authenticated request includes `ctx.access`. Call [`ctx.access.getIdentity()`](https://developers.cloudflare.com/workers/runtime-apis/context/#access) to get the user's email, name, and groups — no manual JWT validation required.

```js
export default {
  async fetch(request, env, ctx) {
    if (!ctx.access) {
      return new Response("Access did not run", { status: 401 });
    }

    const identity = await ctx.access.getIdentity();
    return Response.json({ aud: ctx.access.aud, email: identity?.email });
  },
};
```

**Test Access locally**

You can now test Cloudflare Access locally with `wrangler dev`. Add a `dev` block to your `wrangler.jsonc`:

```json
{
  "access": {
    "dev": {
      "aud": "my-app",
      "identity": { "email": "admin@example.com" }
    }
  }
}
```

Your Worker will receive this identity through `ctx.access` and `ctx.access.getIdentity()`, letting you test authenticated and unauthenticated flows without deploying. Remove the `dev` block to simulate unauthenticated requests.

**API and programmatic access**

You can also set up these policies through the [Workers API](https://developers.cloudflare.com/workers/configuration/cloudflare-access/) instead of the dashboard.

Aug 13, 2026

[<h2>Data localization support for Artifacts</h2>](https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.

Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "namespace": "my-eu-namespace",
    "jurisdiction": "eu"
  }'
```

Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.

For supported jurisdictions and usage details, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).

Aug 13, 2026

[<h2>Detect and control software package downloads with package registry security</h2>](https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) using `pkg.*` selectors to allow or block package downloads.

#### Supported ecosystems

Gateway detects package downloads for the following ecosystems:

| Ecosystem | Namespace |
| --- | --- |
| npm | Scope (for example, `@babel`) |
| PyPI | -- |
| RubyGems | -- |
| Cargo | -- |
| Go | Module path |
| Maven | Group ID |
| NuGet | -- |

#### Selectors

In the dashboard, select **Package Ecosystem** to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five `pkg.*` selectors are available for HTTP policies with the Allow and Block actions:

| Selector | Description |
| --- | --- |
| `pkg.ecosystem` | The package ecosystem detected from the request URL. |
| `pkg.name` | The package name extracted from the download URL. |
| `pkg.version` | The package version, with support for ecosystem-aware comparison operators. |
| `pkg.namespace` | The package namespace, when the ecosystem supports one. |
| `pkg.purl` | The [Package URL (PURL) ↗︎](https://github.com/package-url/purl-spec) derived from the detected coordinates. Available in the API only. |

Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.

Package registry security requires [TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) to be turned on.

For more information, refer to [Package registry security](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/package-registry-security/).

Aug 13, 2026

[<h2>Control Realtime SFU DataChannel delivery</h2>](https://developers.cloudflare.com/changelog/post/2026-08-13-datachannels-reliability-ordering/)

[Realtime](https://developers.cloudflare.com/realtime/)

[Cloudflare Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is a [WebRTC selective forwarding unit](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/) that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.

[DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/) are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.

#### What changed

Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.

With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or the transport's retry window.

#### Choose delivery behavior

Delivery settings answer two questions: whether newer messages can bypass a delayed message, and when the transport should stop retrying delivery.

The publisher chooses one policy for each named channel. Every subscriber mirrors it. Use separate named channels for different policies, such as reliable commands and unreliable pointer updates:

| Goal | Settings | Use when |
| --- | --- | --- |
| Reliable, ordered delivery (default) | Omit `ordered`, `maxRetransmits`, and `maxPacketLifeTime` | Messages remain useful and must arrive in order |
| Reliable, unordered delivery | Set `ordered: false`; omit both retry fields | Messages remain useful, but later messages should not wait for earlier messages |
| No retries or ordering | Set `ordered: false` and `maxRetransmits: 0` | The application tolerates message loss and discards out-of-date updates |
| Limited retries | Set `maxRetransmits: <COUNT>` | Brief recovery is useful, but repeated retries are not |
| Time-limited transport retries | Set `maxPacketLifeTime: <MILLISECONDS>` | Limit how long the transport attempts transmission and retransmission |

Omitted `ordered` means `true`; ordering is independent of retries. Set at most one of `maxRetransmits` and `maxPacketLifeTime`. Omit both for reliable delivery, whether ordered or unordered. Setting `maxRetransmits: 0` explicitly requests no retransmissions.

`maxPacketLifeTime` does not impose an end-to-end message-age deadline. Use application timestamps or sequence numbers to discard stale updates. Reliable delivery does not provide durable storage or confirm command execution.

#### Apply the policy end to end

Your application must supply the publisher's policy in every subscriber request and browser `createDataChannel()` call. Negotiated DataChannels do not communicate these settings to the browser automatically. Each endpoint uses its own allocated channel ID; `waitForAck` and `canReply` remain subscription-specific.

The shared policy applies to one named publication, so other channels in the same session or application can use different policies. Asymmetric reliability is outside the supported contract.

The following example configures unordered delivery with no retransmissions. It begins after you [establish a DataChannel transport on both sessions and complete any required SDP exchange](https://developers.cloudflare.com/realtime/sfu/features/datachannels/#set-up-a-datachannel). Run the API requests from your backend with `APP_ID`, `APP_TOKEN`, `PUBLISHER_SESSION_ID`, and `SUBSCRIBER_SESSION_ID` set in your environment.

1. On the publisher session, create the local DataChannel:

```bash
curl --request POST \
  --url "https://rtc.live.cloudflare.com/v1/apps/$APP_ID/sessions/$PUBLISHER_SESSION_ID/datachannels/new" \
  --header "Authorization: Bearer $APP_TOKEN" \
  --header "Content-Type: application/json" \
  --data @- <<EOF
{
  "dataChannels": [
    {
      "location": "local",
      "dataChannelName": "player-state",
      "ordered": false,
      "maxRetransmits": 0
    }
  ]
}
EOF
```

2. On each subscriber session, pull the remote DataChannel with the same delivery settings:

```bash
curl --request POST \
  --url "https://rtc.live.cloudflare.com/v1/apps/$APP_ID/sessions/$SUBSCRIBER_SESSION_ID/datachannels/new" \
  --header "Authorization: Bearer $APP_TOKEN" \
  --header "Content-Type: application/json" \
  --data @- <<EOF
{
  "dataChannels": [
    {
      "location": "remote",
      "sessionId": "$PUBLISHER_SESSION_ID",
      "dataChannelName": "player-state",
      "ordered": false,
      "maxRetransmits": 0
    }
  ]
}
EOF
```

3. In the publisher and subscriber clients, create the negotiated browser DataChannel with the same settings. In this example, `pc` is the active `RTCPeerConnection`, and `channelId` is the ID returned by the corresponding API request:

```ts
const channel = pc.createDataChannel("player-state", {
  negotiated: true,
  id: channelId,
  ordered: false,
  maxRetransmits: 0,
});
```

#### Related documentation

- [Realtime SFU overview](https://developers.cloudflare.com/realtime/sfu/)
- [DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/)
- [Connection API](https://developers.cloudflare.com/realtime/sfu/api/)

Aug 13, 2026

[<h2>Oracle Cloud Infrastructure Object Storage support in Cloud Connector</h2>](https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/)

[Rules](https://developers.cloudflare.com/rules/)

Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.

OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional `oraclecloud.com` and dedicated `customer-oci.com` path-style endpoints.

Public buckets only

Cloud Connector does not sign requests or provide OCI credentials. Your bucket must allow anonymous object reads. Private buckets and pre-authenticated request URLs are not supported.

#### API example

Set `provider` to `oci_storage` and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:

```json
{
	"expression": "http.request.uri.path wildcard \"/assets/*\"",
	"provider": "oci_storage",
	"description": "Route assets to OCI Object Storage",
	"enabled": true,
	"parameters": {
		"host": "<BUCKET_NAME>.vhcompat.objectstorage.<REGION>.oci.customer-oci.com"
	}
}
```

For endpoint formats and bucket requirements, refer to [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage).

Aug 13, 2026

[<h2>Certificate Transparency Monitoring is now Generally Available</h2>](https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Certificate Transparency Monitoring is now [generally available ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) across all Cloudflare plans.

Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) or the [CT Monitoring docs](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).

Aug 12, 2026

[<h2>Block emails by content with blocked content rules</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security now lets administrators write their own content-based blocking rules. A new **Blocked content** area under **Policies & rules** lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.

- Create rules using either **plaintext** matches or **regular expressions** — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.
- Choose the **search location** for each rule: **subject**, **body**, or **subject and body**.
- Use the built-in **regular expression checker** to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.
- Matching messages are marked with a malicious [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) and prevented from reaching users' inboxes.

Blocked content rules currently only support the block action.

This feature is available for the following Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

To get started, refer to [Blocked content](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/).

Aug 12, 2026

[<h2>Export the code Agent Lee generates</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/)

[Agent Lee](https://developers.cloudflare.com/agent-lee/)

When Agent Lee generates a project for you — a starter static site, a Worker, a scaffold — you can now take the source with you. Agent Lee packages the generated files into a temporary repository and gives you a one-time command to clone it to your own machine.

Previously, generated code lived only in the conversation. You had to copy files out of the chat by hand, which is tedious for anything larger than a single snippet and easy to get wrong.

#### How it works

- Ask Agent Lee to build something, then ask it to export the code.
- An export card appears listing the files and a countdown to expiry.
- Select **Copy clone command**. Agent Lee fetches a fresh command and copies it to your clipboard.
- Run it in your terminal, then point the repository at your own Git host and push:

```sh
git remote set-url origin https://your-git-host.example/you/your-repo.git
git push -u origin main
```

#### Good to know

- **The export is temporary.** The repository expires about 36 hours after it is created and is then deleted automatically. The clone credential expires about an hour after it is issued. Clone promptly, then push to a repository you control.
- **No credential appears in the chat.** The clone command and its read-only credential are delivered only when you select **Copy clone command** — never in the message text or conversation history.
- **Nothing is written to your account.** The temporary repository lives in Cloudflare-managed storage, and connecting a GitHub or GitLab account is not required.
- **Intended for small projects.** An export can include up to 50 files, up to 100 KB per file and 2 MB in total.

Agent Lee remains in beta. Features and behaviors may change as the product evolves.

For details, see [Export generated code](https://developers.cloudflare.com/agent-lee/take-home-code/).

Aug 12, 2026

[<h2>Independent MFA supports FIDO2 for infrastructure applications</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

Aug 12, 2026

[<h2>MCP protocol detection and AI Security dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare Gateway now automatically detects [Model Context Protocol (MCP) ↗︎](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.

#### MCP policy selector

A new **Is MCP** selector (`experimental.is_mcp`) is available in [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#is-mcp). Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.

This selector is currently in beta and may change before general availability.

For example, the following policy blocks MCP traffic that does not arrive through an approved [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/):

| Selector | Operator | Value | Logic | Action |
| --- | --- | --- | --- | --- |
| Is MCP | is | *True* | And | Block |
| Traffic Source | is not | *MCP portal* |  | |

![Example Gateway policy that blocks MCP traffic not arriving through an MCP portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1104,height=664,format=webp/_astro/gateway-block-unknown-mcp.B2Ainj8x.png)

#### AI security report

A new **AI security report** dashboard under **Insights & Logs > Dashboards** provides visibility into MCP usage across your organization. The dashboard includes:

- Total MCP request volume, unique users, and unique MCP servers
- A timeseries chart of unique MCP servers observed over time
- A summary of Gateway policies that target MCP traffic

![AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=928,format=webp/_astro/gateway-mcp-dashboard.C9jPahkp.png)

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).

Aug 12, 2026

[<h2>Traffic Source selector in Gateway policies</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Source** selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.

#### Available traffic source values

| UI name | API value | Description |
| --- | --- | --- |
| Device client | `device_client` | Traffic from the [Cloudflare One Client (WARP)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) |
| Mesh | `mesh` | Traffic from a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) connector |
| Cloudflare WAN | `cloudflare_wan` | Traffic from [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/) (Magic WAN) |
| Clientless RDP | `clientless_rdp` | Traffic from a clientless RDP session |
| Proxy endpoint | `proxy_endpoint` | Traffic from a [proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) (PAC file) |
| Clientless Browser Isolation | `agentless_biso` | Traffic from [clientless Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) |
| MCP portal | `mcp_portal` | Traffic from an [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) |

The selector uses the `net.onramp.type` API field in both HTTP and Network policies.

| UI name | API example |
| --- | --- |
| Traffic Source | `net.onramp.type == "device_client"` |

#### Browser Isolation selector

A **Browser Isolation** selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside [Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/), allowing administrators to apply different policy behavior to isolated traffic.

| UI name | API example |
| --- | --- |
| Browser Isolation | `net.is_isolated == true` |

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

Aug 11, 2026

[<h2>Pages now skips superseded queued builds</h2>](https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/)

[Pages](https://developers.cloudflare.com/pages/)

Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.

Aug 11, 2026

[<h2>New Cloudflare Status page</h2>](https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/)

[Support](https://developers.cloudflare.com/support/)

The Cloudflare Status page at [www.cloudflarestatus.com ↗︎](https://www.cloudflarestatus.com/) has been rebuilt. It is available at the same address, and every previously documented [Status API ↗︎](https://www.cloudflarestatus.com/api) endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.

#### Notifications that fire even when Cloudflare is down

The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.

The **Maintenance Notification** and **Incident Alerts** in [Cloudflare Notifications](https://developers.cloudflare.com/notifications/) remain supported, and deliver to the destinations already configured on your account.

#### Markdown for AI agents

Every page on the status page returns Markdown when requested with an `Accept: text/markdown` header, so agents can read the current status without parsing HTML:

```sh
curl -H "Accept: text/markdown" https://www.cloudflarestatus.com/locations
```

#### Separate feeds for incidents and maintenance

Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:

```txt
https://www.cloudflarestatus.com/api/v3/incidents.rss
https://www.cloudflarestatus.com/api/v3/incidents.atom
https://www.cloudflarestatus.com/api/v3/maintenance.rss
https://www.cloudflarestatus.com/api/v3/maintenance.atom
```

For more information, refer to [Cloudflare Status](https://developers.cloudflare.com/support/cloudflare-status/).

Aug 11, 2026

[<h2>Hostname routing is now generally available, with a new public IP range for initial resolved IPs</h2>](https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Hostname routing ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/) is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:

- **Cloudflare Tunnel**: route a [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) (for example, `wiki.internal.local`) to a private application behind your tunnel, or a [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) (for example, `bank.example.com`) to egress through a specific tunnel and anchor traffic to a dedicated exit node.
- **Cloudflare Mesh**: attract a [private or public hostname's traffic](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Mesh node.

Alongside GA, the default IPv4 range used for initial resolved IPs (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:

- **IPv4**: `172.64.128.0/20`
- **IPv6**: `2606:4700:0cf1:4000::/64`

This is the default range. You can [configure a custom initial resolved IP range](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/) for IPv4 if it conflicts with your existing network.

**Why this is changing:** Starting with [Chrome 142 ↗︎](https://developer.chrome.com/release-notes/142), Local Network Access (LNA) restrictions block background requests to CGNAT addresses (`100.64.0.0/10`), which included the previous initial resolved IP default (`100.80.0.0/16`). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.

**What is affected:** Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:

- [Private](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and [public](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) hostname routing for Cloudflare Tunnel
- [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) for Cloudflare Mesh
- [Access private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) on non-HTTPS ports
- [Egress policy host selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/host-selectors/) (Domain, Host, Application, and Content Categories)

You can check your account's current range, or configure a custom range, at any time from **Networking** > **IP addresses** > **Address space** > **Custom IPs**, or using the [Initial Resolved IP Subnet API](<https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip>).

[Go to **Custom IPs** ↗](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space/custom-ips)

For full instructions, refer to [Configure initial resolved IPs](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/). The IPv6 range (`2606:4700:0cf1:4000::/64`) is unchanged and is not affected by this restriction.

The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to [Automatically managed ranges](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges) for details.

If you were relying on a Chrome Enterprise policy workaround (such as `LocalNetworkAccessRestrictionsTemporaryOptOut`) while your account was still on the legacy CGNAT-based range, refer to [Google Chrome restricts access to private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames) for next steps.

Aug 11, 2026

[<h2>WAF Release - 2026-08-11</h2>](https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.

**Key Findings**

- A new detection provides protection against vBulletin CVE-2026-61511.
- Two existing detections have been improved to strengthen coverage.

**Impact**

Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...94f3006b | N/A | vBulletin - Remote Code Execution - CVE:CVE-2026-61511 | Log | Block | This is a new detection. |
| Cloudflare Managed Ruleset | ...098b749e | N/A | Version Control - Information Disclosure - Beta | Log | Block | This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529) |
| Cloudflare Managed Ruleset | ...d56225d8 | N/A | vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta | Log | Block | This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: ...8fe9f1c7) |

Aug 10, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.905.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-10-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.

Aug 10, 2026

[<h2>Stream live logs from Cloudflare Tunnel in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Real-time Tunnel log streaming is now available in the Cloudflare dashboard under **Networking** > **Tunnels**. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.

![Stream live logs from a tunnel in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-live-logs-core-dashboard.Dtm7Jg51.gif)

In the tunnel detail view, a new **Live logs** tab lets you:

- **Stream logs from single or multiple connectors** — In [highly available](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) deployments with multiple `cloudflared` replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.
- **Filter by log level, event type, and HTTP method** — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or `cloudflared` internal), at any log level.

[Go to **Tunnels** ↗](https://dash.cloudflare.com/?to=/:account/tunnels)

For more information, refer to [Tunnel observability](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) and [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/).

Aug 10, 2026

[<h2>Turnstile Spin is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/)

[Turnstile](https://developers.cloudflare.com/turnstile/)

[Turnstile Spin](https://developers.cloudflare.com/turnstile/spin/) is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.

#### Server-side verification

Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.

- The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.
- The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select **Fix with Spin** to copy a prompt that guides your agent through wiring siteverify into your backend.
- Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.

#### Run Spin

You can run Spin three ways:

- In the **Turnstile dashboard**, select **Set up with Spin**, enter your domains, then select **Set up**. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.
- From the `Wrangler CLI`, run [`wrangler turnstile widget create`](https://developers.cloudflare.com/turnstile/spin/#set-up-from-the-wrangler-cli). Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.
- From your **AI coding agent**, paste the [Spin prompt](https://developers.cloudflare.com/turnstile/spin/#set-up-from-an-ai-coding-agent) into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.

To get started, refer to the [Turnstile Spin documentation](https://developers.cloudflare.com/turnstile/spin/).

Aug 7, 2026

[<h2>Workers AI and AI Gateway unify model access and billing</h2>](https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) [Workers AI](https://developers.cloudflare.com/workers-ai/)

Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.

#### Unified entrypoints and observability

The [AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/) supports both Workers AI and third-party models through `env.AI.run()`. The [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) provides shared `/ai/` endpoints with Cloudflare authentication across providers.

Route a Workers AI request through AI Gateway by specifying a gateway ID. Use `default` to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:

```js
const response = await env.AI.run(
	"@cf/zai-org/glm-5.2",
	{
		messages: [{ role: "user", content: "What is the capital of France?" }],
	},
	{
		gateway: { id: "default" },
	},
);
```

```ts
const response = await env.AI.run(
	"@cf/zai-org/glm-5.2",
	{
		messages: [{ role: "user", content: "What is the capital of France?" }],
	},
	{
		gateway: { id: "default" },
	},
);
```

Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.

#### Unified billing and higher rate limits

You can now use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing**. Workers AI requests routed through that gateway deduct from your credit balance in real time.

Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:

- [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
- [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
- [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)

These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.

For details, refer to [Workers AI limits](https://developers.cloudflare.com/workers-ai/platform/limits/), [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), and the [AI Gateway model catalog](https://developers.cloudflare.com/ai/models/).

Aug 7, 2026

[<h2>MySQL support in Hyperdrive is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same [pricing](https://developers.cloudflare.com/hyperdrive/platform/pricing/) as Postgres.

```js
import { createConnection } from "mysql2/promise";

export default {
	async fetch(request, env, ctx) {
		const connection = await createConnection({
			host: env.HYPERDRIVE.host,
			user: env.HYPERDRIVE.user,
			password: env.HYPERDRIVE.password,
			database: env.HYPERDRIVE.database,
			port: env.HYPERDRIVE.port,
			disableEval: true, // Required for Workers compatibility
		});

		const [results, fields] = await connection.query("SHOW tables;");

		ctx.waitUntil(connection.end());

		return new Response(JSON.stringify({ results, fields }), {
			headers: {
				"Content-Type": "application/json",
				"Access-Control-Allow-Origin": "*",
			},
		});
	},
};
```

```ts
import { createConnection } from "mysql2/promise";

export interface Env {
	HYPERDRIVE: Hyperdrive;
}

export default {
	async fetch(request, env, ctx): Promise<Response> {
		const connection = await createConnection({
			host: env.HYPERDRIVE.host,
			user: env.HYPERDRIVE.user,
			password: env.HYPERDRIVE.password,
			database: env.HYPERDRIVE.database,
			port: env.HYPERDRIVE.port,
			disableEval: true, // Required for Workers compatibility
		});

		const [results, fields] = await connection.query("SHOW tables;");

		ctx.waitUntil(connection.end());

		return new Response(JSON.stringify({ results, fields }), {
			headers: {
				"Content-Type": "application/json",
				"Access-Control-Allow-Origin": "*",
			},
		});
	},
} satisfies ExportedHandler<Env>;
```

Learn more about [how Hyperdrive works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/) and [get started building Workers that connect to MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/get-started/).

Aug 7, 2026

[<h2>Restart a Hyperdrive configuration from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.

Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.

To restart, select your Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to the **Settings** tab, and select **Restart** under **Danger zone**. Restarting requires the [**Hyperdrive Admin** role](https://developers.cloudflare.com/fundamentals/manage-members/roles/). After a restart, the **Settings** tab shows when the configuration was last manually restarted.

![The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=468,format=webp/_astro/dashboard-restart-danger-zone.D1h69zVU.png)

Caution

Restarting drops all active connections in the pool and forces them to be re-established. In-flight queries may see brief errors while the pool rebuilds.

For more information, refer to [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

Aug 7, 2026

[<h2>Load Balancing health notifications now resolve automatically</h2>](https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/) health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.

As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.

This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by [Health Checks](https://developers.cloudflare.com/health-checks/) notifications.

Two things to keep in mind:

- A recovery notification is matched to the earlier unhealthy notification for the **same pool or endpoint**. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.
- If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.

Refer to [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/) to learn more about routing Load Balancing health notifications to an incident management tool.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/8/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
