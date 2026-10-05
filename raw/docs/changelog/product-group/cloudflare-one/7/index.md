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

Apr 7, 2026

[<h2>User Submission Triage Status Tracking</h2>](https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security now supports **Triage Status Tracking for User Submissions**. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.

- The User Submissions table now includes a **Status** column with three states: **Unreviewed** (new submissions awaiting triage), **Reviewed** (submissions assessed by the SOC team), and **Escalated** (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.
- SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.

Triage Status Tracking is **automatically available** for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.

This applies to all Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Apr 7, 2026

[<h2>Link aggregation (LACP) support for Cloudflare One Appliance</h2>](https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.

This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.

To configure a Link Aggregation Group, refer to [Configure link aggregation groups](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/).

Apr 6, 2026

[<h2>DANE Support for MX Deployments</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.

- Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.
- DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Apr 6, 2026

[<h2>Organizations is now in public beta for enterprises</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

We're announcing the public beta of **Organizations** for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.

**What's New**

**Organizations \[BETA]**: [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.

**Self-serve onboarding**: Enterprise customers can [create an Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/) in the dashboard and assign accounts where they are already Super Administrators.

**Centralized Account Management**: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly. **Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) policies across multiple accounts within your Organization to simplify centralized policy management. **Implicit access**: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.

**Unified analytics**: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.

**Terraform provider support**: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization).

**Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policies across multiple accounts within your Organization to simplify centralized policy management.

Note

Organizations is in Public Beta. You must have an Enterprise account to create an organization, but once created, you can add accounts of any plan type where you are a Super Administrator.

For more info:

- [Get started with Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
- [Set up your Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/)
- [Review limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/)

Apr 2, 2026

[<h2>Cloudflare One Client for macOS (version 2026.3.846.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-04-02-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

The next stable release for macOS will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.

**Changes and improvements**

- Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
- Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.
- Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.
- Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
- Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
- Added monitoring for tunnel statistics collection timeouts.
- Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.
- Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.

Apr 2, 2026

[<h2>Cloudflare One Client for Linux (version 2026.3.846.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-04-02-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

The next stable release for Linux will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.

**Changes and improvements**

- Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
- Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.
- Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.
- Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
- Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
- Added monitoring for tunnel statistics collection timeouts.
- Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.
- Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.

Apr 2, 2026

[<h2>Session management for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.

To return to the server selection page, ask your AI agent with a prompt like "take me back to the server selection page." The portal responds with an authorization URL via [MCP elicitation ↗︎](https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation) that you open in your browser:

```txt
https://<subdomain>.<domain>/authorize?elicitationId=<ELICITATION_ID>
```

From the server selection page you can:

- **Enable or disable servers** — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.
- **Log out and reauthenticate** — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.

Users can also enable or disable a server inline by asking their AI agent directly, for example "enable the wiki server" or "disable my Jira server."

The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of [managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal).

For more information, refer to [Manage portal sessions](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions).

Apr 1, 2026

[<h2>Logs UI refresh</h2>](https://developers.cloudflare.com/changelog/post/2026-04-01-logs-ui-refresh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.

![Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2984,height=842,format=webp/_astro/cf1-new-logs-ui.DxF4x0l-.png)

The updated UI includes:

- **Filter by field** - Select any field value to add it as a filter and narrow down your results.
- **Customizable fields** - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.
- **View details** - Select a timestamp to view the full details of a log entry.
- **Switch to classic view** - Return to the previous log viewer interface if needed.

For more information, refer to [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/) and [Gateway activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/).

Mar 26, 2026

[<h2>Code Mode for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support [Code Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/), a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.

To turn it off, edit the portal in **Access controls** > **AI controls** and turn off **Code Mode** under **Basic information**.

When Code Mode is active, the portal exposes a single `code` tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed `codemode.*` methods for each upstream tool. The generated code runs in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment, keeping authentication credentials and environment variables out of the model context.

To use Code Mode, append `?codemode=search_and_execute` to your portal URL when connecting from an MCP client:

```txt
https://<subdomain>.<domain>/mcp?codemode=search_and_execute
```

For more information, refer to [Code Mode](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode).

Mar 26, 2026

[<h2>Context optimization for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the `optimize_context` query parameter to the portal URL.

#### `minimize_tools`

Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special `query` tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=minimize_tools
```

#### `search_and_execute`

Hides all upstream tools and exposes only two tools: `query` and `execute`. The `query` tool searches and retrieves tool definitions. The `execute` tool runs the upstream tools in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=search_and_execute
```

For more information, refer to [Optimize context](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context).

Mar 26, 2026

[<h2>Streaming ZIP file scanning removes per-file size limits</h2>](https://developers.cloudflare.com/changelog/post/2026-03-26-streaming-zip-handler/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.

Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.

This improvement is automatic — no configuration changes are required.

Mar 25, 2026

[<h2>Detect and sanitize HAR files</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.

Gateway now includes a predefined DLP profile called **Unsanitized HAR** that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.

#### How to configure a HAR file policy

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall Policies** > **HTTP** and create a new HTTP policy using the **DLP Profile** selector:

| Selector | Operator | Value | Action |
| --- | --- | --- | --- |
| DLP Profile | in | *Unsanitized HAR* | |

Then choose one of the following actions:

- **Block**: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.
- **Block** with **Gateway Redirect**: Intercepts the upload and redirects the user to `https://har-sanitizer.pages.dev/`, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.

#### Sanitized HAR recognition

HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.

#### Visibility in Gateway logs

Gateway logs will reflect whether a detected HAR file was classified as **Unsanitized** or **Sanitized**, giving your security team full visibility into HAR file activity across your organization.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

Mar 24, 2026

[<h2>OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare Gateway now supports [OIDC Claims](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims) as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.

With this update, you can:

- Filter traffic in [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies based on OIDC claim values.
- Apply custom [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) to route DNS queries to specific resolvers depending on a user's OIDC claims.
- Control [egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/) to assign dedicated egress IPs based on OIDC claim attributes.

For example, you can create a policy that routes traffic differently for users with `department=engineering` in their OIDC claims, or restrict access to certain destinations based on a user's role claim.

To get started, configure [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) on your identity provider and use the **OIDC Claims** selector in the Gateway policy builder.

For more information, refer to [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/).

Mar 20, 2026

[<h2>Managed OAuth for Cloudflare Access</h2>](https://developers.cloudflare.com/changelog/post/2026-03-20-managed-oauth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access supports managed OAuth, which allows non-browser clients — such as CLIs, AI agents, SDKs, and scripts — to authenticate with Access-protected applications using a standard OAuth 2.0 authorization code flow.

Previously, non-browser clients that attempted to access a protected application received a `302` redirect to a login page they could not complete. The established workaround was `cloudflared access curl`, which required installing additional tooling.

With managed OAuth, clients instead receive a `401` response with a `WWW-Authenticate` header that points to Access's OAuth discovery endpoints ([RFC 8414 ↗︎](https://datatracker.ietf.org/doc/html/rfc8414) and [RFC 9728 ↗︎](https://datatracker.ietf.org/doc/html/rfc9728)). The client opens the end user's browser to the Access login page. The end user authenticates with their identity provider, and the client receives an OAuth access token for subsequent requests.

Access enforces the same policies as a browser login; the OAuth layer is a new transport mechanism, not a separate authentication path.

Managed OAuth can be enabled on any self-hosted Access application or [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/). It is opt-in for existing applications to avoid interfering with those that run their own OAuth servers and rely on their own `WWW-Authenticate` headers.

Note

For MCP server portals, managed OAuth is enabled by default on new portals. It remains opt-in for self-hosted applications.

To enable managed OAuth, go to **Zero Trust** > **Access controls** > **Applications**, edit the application, and turn on **Managed OAuth** under **Advanced settings**.

You can also enable it via the API by setting `oauth_configuration.enabled` to `true` on the [Access applications endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/).

![Managed OAuth settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2914,height=1042,format=webp/_astro/managed-oauth.BirLnBpy.png)

For setup instructions, refer to [Enable managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/).

Mar 20, 2026

[<h2>Route MCP server portal traffic through Cloudflare Gateway</h2>](https://developers.cloudflare.com/changelog/post/2026-03-20-mcp-portal-gateway-routing/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now route traffic through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for richer HTTP request logging and data loss prevention (DLP) scanning.

When Gateway routing is turned on, portal traffic appears in your [Gateway HTTP logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/). You can create [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) with [DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/) to detect and block sensitive data sent to upstream MCP servers.

Note

DLP [AI prompt profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#ai-prompt) do not apply to MCP server portal traffic.

To enable Gateway routing, go to **Access controls** > **AI controls**, edit the portal, and turn on **Route traffic through Cloudflare Gateway** under **Basic information**.

![Route MCP server portal traffic through Cloudflare Gateway](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1568,height=158,format=webp/_astro/portal-route-through-gateway.0KMUAXBm.png)

For more details, refer to [Route traffic through Gateway](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway).

Mar 20, 2026

[<h2>Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</h2>](https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) of that tunnel and supports streaming logs from multiple replicas at once.

![View replicas and stream logs from multiple connectors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1040,format=webp/_astro/tunnel-multiconn.DEOEaLlu.gif)

Previously, you could only stream logs from one replica at a time. With this update:

- **Replicas on the tunnel overview** — All active replicas for the selected tunnel now appear on that tunnel's overview page under **Connectors**. Select any replica to stream its logs.
- **Multi-connector log streaming** — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Networks** > **Connectors** > **Cloudflare Tunnels**. Select **View logs** next to the tunnel you want to monitor.

For more information, refer to [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) and [Deploy replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/).

Mar 15, 2026

[<h2>Unlimited result paging in Investigations</h2>](https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.

In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The [Investigations API](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/list) now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.

For high-volume use cases, we recommend:

- **[Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/) to a SIEM** for full-fidelity datasets and long-term retention.
- **SOAR playbooks** against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.
- **The Investigations API** for report exports larger than 1,000 results, which is the dashboard download cap.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Mar 10, 2026

[<h2>WARP client for macOS (version 2026.3.566.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-03-10-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the [Cloudflare Community forum](https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362) and let us know.

**Changes and improvements**

- Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
- Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.
- Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.
- Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
- Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
- Added monitoring for tunnel statistics collection timeouts.
- Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.
- Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.

**Known issues**

- The client may become stuck in a `Connecting` state. To resolve this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface. Alternatively, change the client's operation mode.
- The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.
- Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.

Mar 10, 2026

[<h2>WARP client for Windows (version 2026.3.566.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the [Cloudflare Community forum](https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362) and let us know.

**Changes and improvements**

- Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
- Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
- Added monitoring for tunnel statistics collection timeouts.
- Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.
- Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.
- Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.
- Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.
- Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.
- Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
- Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.
- Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.
- Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.

**Known issues**

- The client may unexpectedly terminate during captive portal login. To work around this issue, use a web browser to authenticate with the captive portal and then re-launch the client.
- An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
- The client may become stuck in a `Connecting` state. To resolve this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface. Alternatively, change the client's operation mode.
- The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.
- Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.
- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 version KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.
- DNS resolution may be broken when the following conditions are all true:
  - The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while the client is connected. To work around this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface.

Mar 4, 2026

[<h2>User risk score selector in Access policies</h2>](https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now use [user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) in your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). The new **User Risk Score** selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.

For more information, refer to [Use risk scores in Access policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies).

Mar 4, 2026

[<h2>Gateway Authorization Proxy and hosted PAC files (open beta)</h2>](https://developers.cloudflare.com/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [PAC file hosting](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now in open beta for all plan types.

Previously, [proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.

This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.

#### Key capabilities

- **Identity-aware proxy traffic** — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write [identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/) like "only the Finance team can access this accounting tool."
- **Multiple identity providers** — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.
- **Cloudflare-hosted PAC files** — Create and host [PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at `https://pac.cloudflare-gateway.com/<account-id>/<slug>` on Cloudflare's global network.
- **Simplified billing** — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.

#### Get started

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Networks** > **Resolvers & Proxies** > **Proxy endpoints**.
2. [Create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and configure Access policies.
3. [Create a hosted PAC file](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) or write your own.
4. [Configure browsers](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file) to use the PAC file URL.
5. [Install the Cloudflare certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) for HTTPS inspection.

For more details, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and the [announcement blog post ↗︎](https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/).

Mar 2, 2026

[<h2>Copy Cloudflare One resources as JSON or POST requests</h2>](https://developers.cloudflare.com/changelog/post/2026-03-copy-resources-as-json-or-post-requests/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now copy Cloudflare One resources as JSON or as a ready-to-use API POST request directly from the dashboard. This makes it simple to transition workflows into API calls, automation scripts, or infrastructure-as-code pipelines.

To use this feature, click the overflow menu (⋮) on any supported resource and select **Copy as JSON** or **Copy as POST request**. The copied output includes only the fields present on your resource, giving you a clean and minimal starting point for your own API calls.

Initially supported resources:

- Access applications
- Access policies
- Gateway policies
- Resolver policies
- Service tokens
- Identity providers

We will continue to add support for more resources throughout 2026.

Mar 1, 2026

[<h2>Clipboard controls for browser-based RDP</h2>](https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.

![Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=546,format=webp/_astro/rdp-clipboard-controls.B0ZmliDb.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.

#### Configuration options

Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:

- **Copy from local client to remote RDP session** — Users can copy/paste text from their local machine into the browser-based RDP session.
- **Copy from remote RDP session to local client** — Users can copy/paste text from the browser-based RDP session to their local machine.

By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.

When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.

For more information, refer to [Clipboard controls for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls).

Feb 27, 2026

[<h2>Export MCP server portal logs with Logpush</h2>](https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Availability

Only available on Enterprise plans.

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now supports [Logpush](https://developers.cloudflare.com/logs/logpush/) integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.

#### Available log fields

The MCP server portal logs dataset includes fields such as:

- `Datetime` — Timestamp of the request
- `PortalID` / `PortalAUD` — Portal identifiers
- `ServerID` / `ServerURL` — Upstream MCP server details
- `Method` — JSON-RPC method (for example, `tools/call`, `prompts/get`, `resources/read`)
- `ToolCallName` / `PromptGetName` / `ResourceReadURI` — Method-specific identifiers
- `UserID` / `UserEmail` — Authenticated user information
- `Success` / `Error` — Request outcome
- `ServerResponseDurationMs` — Response time from upstream server

For the complete field reference, refer to [MCP portal logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/).

#### Set up Logpush

To configure Logpush for MCP server portal logs, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

Note

MCP server portals is currently in beta.

Feb 27, 2026

[<h2>New protocols added for Gateway Protocol Detection (Beta)</h2>](https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway [Protocol Detection](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/) now supports seven additional protocols in beta:

| Protocol | Notes |
| --- | --- |
| IMAP | Internet Message Access Protocol — email retrieval |
| POP3 | Post Office Protocol v3 — email retrieval |
| SMTP | Simple Mail Transfer Protocol — email sending |
| MYSQL | MySQL database wire protocol |
| RSYNC-DAEMON | rsync daemon protocol |
| LDAP | Lightweight Directory Access Protocol |
| NTP | Network Time Protocol |

These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the *Detected Protocol* selector in [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.

If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.

For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
