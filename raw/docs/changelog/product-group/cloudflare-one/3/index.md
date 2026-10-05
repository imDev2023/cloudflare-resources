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

Aug 7, 2026

[<h2>Container image for Cloudflare Mesh</h2>](https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes can now run as Docker containers. The [`cloudflare/mesh` ↗︎](https://hub.docker.com/r/cloudflare/mesh) image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.

The image supports `amd64` and `arm64` architectures and includes built-in [source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat) so return traffic routes correctly without VPC route table changes.

#### Deployment patterns

- **Docker Compose** — add a `cloudflare-mesh` service to your `compose.yaml` and connect your entire stack to a private network.
- **Kubernetes StatefulSet** — deploy a standalone Mesh node with persistent registration state.
- **Kubernetes sidecar** — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.
- **CI/CD** — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.

For [high availability](https://developers.cloudflare.com/mesh/features/high-availability/), run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.

[Go to **Mesh** ↗](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, runtime configuration, and deployment examples, refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/).

Aug 5, 2026

[<h2>Identity-aware controls are now available in AI Gateway</h2>](https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:

- **Protect your gateway endpoint.** Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.
- **Identity-aware controls.** When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.

With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as `cf.user_id`.

For setup instructions, refer to [Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access/).

Aug 3, 2026

[<h2>Control authorization cookies for multi-domain Access applications</h2>](https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.

Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.

The new **Eager redirect cookie** setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a `CF_Authorization` cookie. This supports applications that need to make requests across hostnames before the user visits each one.

For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.

To configure the setting, refer to [Authorization cookie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie).

Aug 3, 2026

[<h2>See fallback pool traffic separately in load balancing analytics</h2>](https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now shows traffic served by your [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) separately from traffic routed to the same pool by normal steering.

Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.

Fallback traffic is now labeled with the pool name followed by `(Fallback)`. A pool named `eu-west`, for example, is shown as `eu-west (Fallback)`. This label appears as its own entry in:

- **Requests over time**, as a separate series in the chart.
- **Pool distribution**, as a separate segment.
- **Top endpoints**, as a separate card for the pool.

The **Latency** view and the health event **Logs** are unchanged.

To see this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same breakdown appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

Refer to [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to learn more.

Jul 31, 2026

[<h2>Cloudflare One Client for Windows (version 2026.7.1210.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-31-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.
- Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.
- A [DNS search domain](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) parsing failure no longer prevents connection.
- Fixed a [MASQUE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) issue where the tunnel could stall while uploading at a high rate.
- Fixed being unable to [switch organizations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/) when the client was stuck in the "Device not in organization" state.
- Fixed the Home Screen dropdown popup not anchoring correctly.
- Fixed a crash during dialog dismissal.
- Increased tolerance for configurations with a large number of [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.
- Fixed a networking issue where IPv6 multicast routes were being assigned to the WARP tunnel interface.
- Fixed fatal errors on UI load on Windows 10.
- Fixed a crash during Windows notification initialization.
- Made the Windows [domain-joined posture check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/) more reliable.
- Fixed orphaned credentials left behind on multi-user uninstall.
- A successful re-authentication will cause the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) to be re-evaluated.
- Improved [dashboard-managed client updates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) by running the updater only when needed.

Jul 31, 2026

[<h2>Cloudflare One Client for macOS (version 2026.7.1210.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.
- Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.
- A [DNS search domain](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) parsing failure no longer prevents connection.
- Fixed a [MASQUE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) issue where the tunnel could stall while uploading at a high rate.
- Fixed being unable to [switch organizations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/) when the client was stuck in the "Device not in organization" state.
- Fixed the Home Screen dropdown popup not anchoring correctly.
- Fixed a crash during dialog dismissal.
- Increased tolerance for configurations with a large number of [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.
- Fixed the WARP client stealing window focus (for example, during reauth).
- Fixed a client crash when connecting to a captive portal over Wi-Fi.
- Fixed the system tray icon showing "disconnected" while the UI showed "connected".
- A successful re-authentication will cause the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) to be re-evaluated.
- Improved [dashboard-managed client updates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) by running the updater only when needed.

Jul 31, 2026

[<h2>Static OAuth client credentials for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.

When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the `client_secret_post` and `client_secret_basic` token endpoint authentication methods.

Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.

For setup instructions, refer to [Configure manual OAuth credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials).

Jul 30, 2026

[<h2>Admins can turn on Code Mode by default for MCP portal users</h2>](https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now support four Code Mode policies: *Off*, *Opt-in*, *On by default*, and *Enforced*. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.

Existing portals retain their current behavior. Portals that previously allowed Code Mode use *Opt-in*, while portals that did not allow Code Mode use *Off*. New portals also use *Opt-in* by default.

Clients turn on Code Mode for an *Opt-in* portal with `?codemode=search_and_execute`. The *On by default* policy lets clients opt out with `?codemode=off`, which avoids nested code execution when a client runs its own Code Mode implementation. The *Off* and *Enforced* policies ignore client overrides.

The Cloudflare API exposes these policies through the `code_mode` field:

```json
{
	"code_mode": "default_on"
}
```

The supported values are `off`, `opt_in`, `default_on`, and `enforced`. The previous `allow_code_mode` boolean is deprecated.

For configuration details and client behavior, refer to [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies).

Jul 28, 2026

[<h2>Control Cloudflare Gateway DNS caching with a maximum TTL setting</h2>](https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.

![The maximum DNS TTL setting in Traffic policies > Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=294,format=webp/_astro/gateway-max-ttl-traffic-settings.BRF3NUMp.png)

The setting is available at two levels:

- **Account level** - In **Traffic Policies** > **Traffic Settings**, under **Proxy and inspection**. This sets the default cap for all DNS locations.
- **Per-location** - Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can inherit the account setting, disable the cap, or override it with a custom value.

Two new fields are also available in DNS logs: `upstream_record_ttls` (the original TTL from the upstream response) and `applied_max_ttl` (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.

For more information, refer to [Maximum DNS TTL](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/).

Jul 21, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.880.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

Jul 21, 2026

[<h2>Cloudflare One Client for macOS (version 2026.6.880.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

Jul 21, 2026

[<h2>Cloudflare One Client for Linux (version 2026.6.880.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

Jul 20, 2026

[<h2>Browser-based login for plaintext HTTP private applications</h2>](https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access now uses the standard browser-based login flow for [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) served over plaintext HTTP on port `80`.

Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an `Authentication required` pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access [application token](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) on success.

This brings the HTTP experience in line with HTTPS apps (with [Gateway TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.

Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.

Jul 17, 2026

[<h2>Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now restart, reboot, or shut down a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard or via API.

![Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-07-17-appliance-restart-reboot-shutdown.DKqTLOh6.gif)

- **Restart** — Restart managed services. Purges temporary and (optionally) persistent state.
- **Reboot** — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.
- **Shutdown** — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.

In the dashboard, go to **Networking** > **Connectors** > **Appliances**, select an appliance, then **Edit** > **Operations** to send an operation. Via API, `POST` to the `/accounts/{account_id}/magic/connectors/{connector_id}/interrupts` endpoint.

For details, refer to [Appliance operations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/).

Jul 17, 2026

[<h2>New header control options for Gateway HTTP policies</h2>](https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports advanced header control on [Allow policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#allow). Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.

#### Header operations

Gateway HTTP policies using the Allow action support three operations in `rule_settings`:

| Operation | API field | Behavior |
| --- | --- | --- |
| Add | `add_headers` | Appends a value to the header. Existing values are preserved. |
| Overwrite | `set_headers` | Replaces the header value. Creates the header if it does not exist. |
| Delete | `delete_headers` | Removes the header from the request. |

Gateway applies operations in order: delete, then overwrite, then add.

#### Dynamic variables

Header values can include dynamic variables using the `@{...}` syntax. Gateway resolves variables at request time from identity, device, and network context.

| Variable | Description |
| --- | --- |
| `@{identity.email}` | User email from the identity provider |
| `@{identity.name}` | User display name from the identity provider |
| `@{identity.id}` | Cloudflare identity UUID |
| `@{identity.groups}` | Identity provider group memberships |
| `@{identity.SAML}` | SAML attributes (if configured) |
| `@{identity.OIDC}` | OIDC claims (if configured) |
| `@{source.ip}` | Source IP of the connection |
| `@{destination.ip}` | Destination IP of the request |
| `@{device.id}` | Cloudflare One Client device UUID |
| `@{device.posture}` | Device posture check results (JSON string) |

You can mix static text and dynamic variables in a single header value. For example, `user-@{identity.email}` resolves to `user-jdoe@example.com`.

For more information, refer to [Custom headers](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tenant-control/).

Jul 16, 2026

[<h2>Bulk print PDFs for browser-based RDP</h2>](https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select **Print all PDFs** in the clipboard panel. The files are combined into one PDF and sent to your local printer.

![The clipboard panel showing the Print all PDFs option for multiple selected PDF files.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=768,height=432,format=webp/_astro/rdp-bulk-print.DT4sCcI-.png)

Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to [Print PDFs for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs).

Jul 15, 2026

[<h2>Internal DNS is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [DNS](https://developers.cloudflare.com/dns/)

[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.

#### Why it matters

- **Consolidate DNS operations.** Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.
- **Simplify split-horizon DNS.** Internal and external resolution are defined as separate [views](https://developers.cloudflare.com/dns/internal-dns/dns-views/) over shared zones, managed from a single control plane — so there is no drift to chase down.
- **Extend Zero Trust to DNS.** Resolver policies decide which users and devices resolve against which view, enforced by the same [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) that already governs the rest of your traffic.

Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.

```json
POST /zones
{
  "account": {
    "id": "<ACCOUNT_ID>"
  },
  "name": "corp.internal",
  "type": "internal"
}
```

Internal DNS is included with [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for Enterprise customers. To get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

Jul 10, 2026

[<h2>Source code detection improvements</h2>](https://developers.cloudflare.com/changelog/post/2026-07-10-source-code-detection-improvements/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.

Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.

Enable and set [confidence levels](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds) to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.

Source code detection applies to standalone source code files in [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). It does not detect source code embedded within other file types or payloads, such as `.docx` files or chat messages.

For more information, refer to [Source Code predefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code).

Jul 9, 2026

[<h2>Wi-Fi signal and network performance analytics for Cloudflare One Client devices</h2>](https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment.

The **Device Monitoring** page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.

![Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1652,height=664,format=webp/_astro/dex-device-monitoring-summary.CBxeSd6b.png)

A summary at the top of the page shows the health of each category at a glance, using **Good**, **Fair**, and **Poor** labels:

- **Connection** — connection status, Cloudflare One Client mode, and tunnel type over time
- **Wi-Fi signal strength** — signal measured in dBm over time, with thresholds that flag a weak signal
- **Traffic performance** — upstream and downstream performance, including network throughput on the active interface
- **Device health** — hardware metrics such as CPU, memory, and disk

![Wi-Fi signal strength and network throughput charts on the Device Monitoring page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1666,height=732,format=webp/_astro/dex-device-monitoring-wifi-network.CoEBznAm.png)

You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.

These analytics are available to all Cloudflare One customers at no additional cost.

To learn more, refer to the [DEX monitoring documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/3/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
