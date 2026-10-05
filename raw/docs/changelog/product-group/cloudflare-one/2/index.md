---
title: Cloudflare One Changelog
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

Sep 2, 2026

[<h2>Configure DHCP options from the dashboard on Cloudflare One Appliance</h2>](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now configure [custom DHCP options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/) directly from the dashboard when the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) is acting as the DHCP server for a LAN.

![Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-dhcp-options-ui.B5OEZmib.gif)

- In **LAN configuration**, under **DHCP server options**, select **Add DHCP option** to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select **Add custom option** to enter your own option code, type, and value.
- This complements the existing [API and Terraform workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options) for configuring DHCP options.

For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

Sep 2, 2026

[<h2>Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</h2>](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

- **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
- **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
- **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.

The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

Aug 31, 2026

[<h2>Load Balancing now supports pool sets</h2>](https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.

Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.

For example, this pool set uses Dynamic Latency steering for traffic from Germany:

```json
{
	"pool_sets": [
		{
			"name": "germany-lowest-latency",
			"match": { "topology": { "countries": ["DE"] } },
			"overrides": {
				"pools": [
					"0930eec54a4c7ae6616985b79f678210",
					"c8b4f5a6d7e84910a2b3c4d5e6f70819"
				],
				"steering_policy": "dynamic_latency"
			}
		}
	]
}
```

Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.

For configuration details and more examples, refer to [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/).

Aug 28, 2026

[<h2>Cloudflare One Client for macOS (version 2026.7.1376.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 28, 2026

[<h2>Cloudflare One Client for Windows (version 2026.7.1376.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 28, 2026

[<h2>Cloudflare One Client for Linux (version 2026.7.1377.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 26, 2026

[<h2>Access service token secrets use a scannable format</h2>](https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.

Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same `CF-Access-Client-Id` and `CF-Access-Client-Secret` authentication headers.

For more information, refer to [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Aug 25, 2026

[<h2>Grace periods for service token rotation</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.

The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.

For configuration instructions, refer to [Rotate service token secrets](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets).

Aug 25, 2026

[<h2>Temporarily turn off Access service tokens</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.

Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.

For configuration instructions, refer to [Turn a service token on or off](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off).

Aug 25, 2026

[<h2>MCP server portals support MCP 2026-07-28 specification</h2>](https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support the stateless MCP `2026-07-28` specification for client and upstream server connections.

The portal's `/mcp` endpoint automatically accepts stateless MCP `2026-07-28` requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP `2026-07-28` support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.

SSE connections continue to use the legacy protocol. For details, refer to [MCP server portal transport and protocol compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport).

Aug 24, 2026

[<h2>Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-24-virtual-appliance-self-serve-download/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

When you register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/), you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.

![Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2813,height=1241,format=webp/_astro/2026-08-24-virtual-appliance-self-serve-download.Ca2YGpCA.png)

- On the **Connectors** page, select **Add an appliance**, choose **Virtual appliance**, then select your hypervisor: **VMware ESXi**, **Proxmox**, or **libvirt/KVM**.
- Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.
- Use **View setup guide** to open deployment instructions for your platform.

This complements the existing self-serve [registration and license key generation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) in the dashboard.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine).

Aug 21, 2026

[<h2>Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</h2>](https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use **CASB remediation policies** to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.

#### Remediate Microsoft 365 and Google Workspace findings

A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.

Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to [Run remediations](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations) in the CASB remediation policies documentation.

#### Send webhooks

A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.

A single policy can perform both actions: remediate a finding and send a webhook.

#### Get started

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Policies**.
2. Select **Create a policy**.
3. Under **Basic information**, enter a **Policy name** and, optionally, a **Description**.
4. Under **Choose how you want to trigger the policy**, select a **Vendor**, **Integration**, and **Finding type**.
5. Under **Define what to do with findings that match your trigger**, choose **Run Remediation**, **Send webhooks**, or both.
6. Under **Status**, turn on **Enable policy**.
7. Select **Create policy**.

#### Learn more

- Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.
- Configure [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/) as a policy destination.
- Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.

CASB remediation policies are now available in Cloudflare One.

Aug 21, 2026

[<h2>Test Data Loss Prevention profiles without sending traffic through Gateway</h2>](https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

**Test scan** lets you check how [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.

![Test scan results showing matched profiles, detection entries, and match context](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=587,format=webp/_astro/dlp-test-scan.Dm6EgN6x.gif)

Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.

Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your [Zero Trust plan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

For more details, refer to the [Test scan documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/test-scan/).

Aug 19, 2026

[<h2>Cloudflare One Client for Windows (version 2026.7.1343.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
- When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.

**Additional changes and improvements**

- Fixed a process leak in the Windows GUI that could exhaust system resources during IPC client-creation failures.
- Fixed being unable to switch organizations when the client was stuck in the "Device not in organization" state.
- Fixed an issue where Microsoft Defender would falsely flag the Cloudflare One Client installation as malicious when installing with Intune.
- Made the Windows domain-joined posture check more reliable.
- A DNS search domain parsing failure no longer prevents connection.
- Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
- Fixed missing certificate error display due to a race condition.
- Fixed empty black window after transitioning from docked dual displays to undocked/internal display.

**Known issues**

- If a user upgrades to version 2026.7.1343.0, downgrades to an earlier version, re-registers, and then upgrades back to 2026.7.1343.0, the client might fail to connect or switch organizations. To resolve this issue, run `warp-cli registration delete` or `warp-cli registration delete-all`.

Aug 19, 2026

[<h2>Cloudflare One Client for macOS (version 2026.7.1343.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
- When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.

**Additional changes and improvements**

- Fixed the client not allowing login to another organization when currently showing "Device not in organization."
- A DNS search domain parsing failure no longer prevents connection.
- Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
- Fixed missing certificate error display due to a race condition.
- Fixed crash when trying to connect to captive portal on Wi-Fi.
- Fixed empty black window after transitioning from docked dual displays to undocked/internal display.

**Known issues**

- None

Aug 19, 2026

[<h2>Cloudflare One Client for Linux (version 2026.7.1343.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
- When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.

**Additional changes and improvements**

- Fixed the client not allowing login to another organization when currently showing "Device not in organization."
- A DNS search domain parsing failure no longer prevents connection.
- Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
- Fixed missing certificate error display due to a race condition.
- Fixed empty black window after transitioning from docked dual displays to undocked/internal display.
- Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.

**Known issues**

- When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.

Aug 19, 2026

[<h2>Access resource lists now support resource-scoped roles</h2>](https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.

The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned `403` responses.

For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.

For role definitions and assignment details, refer to [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) and [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/).

Aug 19, 2026

[<h2>Threat Intel Lists supported in Unified Routing</h2>](https://developers.cloudflare.com/changelog/post/2026-08-19-unified-routing-threat-lists/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Threat Intel Lists are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

Support for additional features - Rate Limiting and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Aug 18, 2026

[<h2>Configure origin application settings for Cloudflare Tunnel in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/). These settings control how `cloudflared` connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.

![Configure origin application settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-origin-settings-dashboard.CsC2RwFC.gif)

When editing a published application, expand **Additional application settings** to configure parameters organized into three categories:

- **HTTP** — Set a custom HTTP Host header or disable chunked encoding.
- **TLS** — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.
- **Connection** — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.

[Go to **Tunnels** ↗](https://dash.cloudflare.com/?to=/:account/tunnels)

For the full list of origin parameters, refer to [Origin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/).

Aug 17, 2026

[<h2>Post-quantum key exchange for MX deployments</h2>](https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.

Inbound MX connections and outbound delivery connections now negotiate the [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) hybrid key agreement when the peer supports it, protecting SMTP traffic against [harvest-now, decrypt-later ↗︎](https://blog.cloudflare.com/pq-2024/) attacks.

Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Aug 17, 2026

[<h2>Load balancing analytics now filters by pool name</h2>](https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.

Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.

The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:

- **Requests over time**, filtering the chart series to the selected pool.
- **Pool distribution**, showing only the selected pool segment.
- **Top endpoints**, displaying cards for origins in the selected pool.
- **Latency**, showing latency data for the selected pool.

The **Logs** view and health event filtering are unchanged.

To use this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same pool filter appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

For more information about analytics filters and metrics, refer to [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/).

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

[<h2>Independent MFA supports FIDO2 for infrastructure applications</h2>](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
