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

Apr 30, 2026

[<h2>Post-quantum IPsec interoperability with third-party devices</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. [Cisco ↗︎](https://www.cisco.com/) and [Fortinet ↗︎](https://www.fortinet.com/) are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

Post-quantum IPsec uses [RFC 9370 ↗︎](https://datatracker.ietf.org/doc/rfc9370/) and [draft-ietf-ipsecme-ikev2-mlkem ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) to negotiate hybrid key agreement during the IKEv2 `IKE_INTERMEDIATE` phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against [harvest-now, decrypt-later ↗︎](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) attacks.

Key details:

- Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.
- Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.
- Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.
- No additional licensing required.

Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.

For supported key exchange methods and the list of validated platforms, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability).

Apr 30, 2026

[<h2>Classify sensitive content with Data Classification</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-data-classification/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Cloudflare DLP now includes **Data Classification**, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.

With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.

You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.

For more information, refer to [Data Classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/).

Apr 30, 2026

[<h2>New predefined detection entries are available</h2>](https://developers.cloudflare.com/changelog/post/2026-04-30-standalone-predefined-detection-entries/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Cloudflare DLP now includes new predefined detection entries.

The expanded catalog includes detections for specific credential types, webhooks, addresses, tax identifiers, national IDs, financial data, and crypto wallets.

Examples include `GitHub PAT`, `OpenAI API Key`, `Slack Webhook`, `Discord Webhook`, `US Physical Address`, and `Bitcoin Wallet`.

For the full list, refer to [Predefined detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/).

Apr 29, 2026

[<h2>Digital experience tests to authenticated resources and enhanced configuration</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital experience tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via [Cloudflare Secret Store](https://developers.cloudflare.com/secrets-store/).

Digital experience tests also have enhanced configuration options including:

- New HTTP methods (DELETE, PATCH, POST, PUT)
- Secret Store headers, custom plain text headers, and custom request bodies
- Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates

![Digital experience test configuration for Cloudflare Access applications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1374,format=webp/_astro/dex_test_auth_config.CD3G3zb_.png)![Digital experience enhanced test configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1496,format=webp/_astro/dex_test_enhanced_config.Nsv7Vcob.png)

Apr 29, 2026

[<h2>Gateway Authorization Proxy and hosted PAC files are now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The [Gateway Authorization Proxy](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [hosted PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file) are now generally available for all plan types.

Authorization proxy endpoints add an identity-aware option alongside the existing [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint), using [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) authentication to verify who a user is before applying Gateway filtering — without installing the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.

These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.

To get started, refer to the [proxy endpoints documentation](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/).

Apr 28, 2026

[<h2>Internet outage notifications for devices</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-internet-outage-notification/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/) will display a dashboard notification when an Internet outage or traffic anomaly may impact a [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) device based on its geographic location or network connection.

This Internet outage and traffic anomaly data is pulled from [Cloudflare Radar ↗︎](https://radar.cloudflare.com/). All Internet outage and traffic anomaly observations can be viewed in the [Radar Outage Center ↗︎](https://radar.cloudflare.com/outage-center).

![Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=314,format=webp/_astro/dex_radar_ux_notification.CpdrUVYA.png)![Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2068,height=909,format=webp/_astro/dex_radar_analytics.GaPxWM6C.png)

Apr 28, 2026

[<h2>Cloudflare One Client speed tests</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-speed-test/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

IT teams can now remotely run speed tests from the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) to Cloudflare's network edge.

Each speed test includes the following metrics:

- Internet speed: download and upload throughput
- Latency: download, upload, unloaded latency, and jitter
- Network quality score: video streaming, webchat/real-time communication (RTC)

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Digital experience** > **Diagnostics** and select **Run diagnostics** to use the feature today.

![Cloudflare One client speed test result](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2906,height=1730,format=webp/_astro/dex_speed_test.DukupcRs.png)

Apr 28, 2026

[<h2>Create and manage DLP detection entries outside of profiles</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-detection-entries-outside-profiles/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now create, view, and manage DLP detection entries outside of profiles.

Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the **Detection entries** section and use them in custom DLP profiles.

For more information, refer to [Configure detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/).

Apr 28, 2026

[<h2>Detect PII records with a new predefined DLP profile</h2>](https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: **Personally Identifiable Information (PII) Record**.

Most predefined and custom DLP profiles match when any enabled detection entry matches. The **Personally Identifiable Information (PII) Record** profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.

Detection entries included in the profile:

- AU Passport Number
- American Express Card Number
- Diners Club Card Number
- US Driver's License Number
- Email Address
- Full Name
- US Mailing Address
- Mastercard Card Number
- US Individual Tax Identification Number (ITIN)
- US Passport Number
- US Phone Number
- Union Pay Card Number
- United States SSN Numeric Detection
- Visa Card Number

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

Apr 24, 2026

[<h2>Network Session Logs now available for all on-ramps</h2>](https://developers.cloudflare.com/changelog/post/2026-04-24-nsl-all-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from [proxy endpoints (PAC files)](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) and [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) egress — on-ramps that previously did not generate session logs.

Customers who already consume the `zero_trust_network_sessions` dataset via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) or [Log Explorer](https://developers.cloudflare.com/log-explorer/) may see increased log volume if they use these on-ramps.

For field definitions, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/). For traffic analysis, refer to [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

Apr 23, 2026

[<h2>AAGUID restrictions and AMR matching for Access independent MFA</h2>](https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/) in Cloudflare Access now supports two additional organization-level controls:

- **[Restrict authenticators by AAGUID](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid)** — Limit enrollment to a specific set of WebAuthn authenticators using their [AAGUID ↗︎](https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid). This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new [List](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) type.
- **[AMR matching](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa)** — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the `amr` claim defined in [RFC 8176 ↗︎](https://datatracker.ietf.org/doc/html/rfc8176) and matches supported values such as `hwk`, `otp`, and `fpt` to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.

To get started, refer to [Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/).

Apr 21, 2026

[<h2>Country rules supported in Unified Routing</h2>](https://developers.cloudflare.com/changelog/post/2026-04-21-unified-routing-geoip-country-rules/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Country rules are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.

This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Apr 20, 2026

[<h2>Network session analytics dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The new [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/) dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.

![Cloudflare One Network Session Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2926,height=1574,format=webp/_astro/cf1-network-session-analytics.Gl90hEcp.png)

#### What you can do with Network session analytics

- **Analyze geographic distribution**: View a world map showing where your network traffic originates, with a list of top locations by session count.
- **Monitor key metrics**: Track session count, total bytes transferred, and unique users.
- **Identify connection issues**: Analyze connection close reasons to troubleshoot network problems.
- **Review protocol usage**: See which network protocols (TCP, UDP, ICMP) are most used.

#### Dashboard features

- **Summary metrics**: Session count, bytes total, and unique users
- **Traffic by location**: World map visualization and location list with top traffic sources
- **Top protocols**: Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic
- **Connection close reasons**: Insights into why sessions terminated (client closed, origin closed, timeouts, errors)

#### How to access

1. Log in to [Cloudflare One ↗︎](https://dash.cloudflare.com).
2. Go to **Zero Trust** > **Insights** > **Dashboards**.
3. Select **Network session analytics**.

For more information, refer to the [Network session analytics documentation](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).

Apr 17, 2026

[<h2>Homepage and sign-out for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) display a homepage when users visit the portal domain in a browser.

![MCP server portal homepage showing connection status and setup instructions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1037,height=631,format=webp/_astro/portals-homepage-disconnected.BHbOwayQ.png)

The homepage shows:

- The portal name and organization branding
- The MCP endpoint URL with a copy button
- Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients

Authenticated users see their email address and a **Sign out** button. Selecting **Sign out** revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.

For more information, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage).

Apr 15, 2026

[<h2>Independent MFA for Access applications</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.

This feature also addresses common gaps in IdP-based MFA, such as inconsistent MFA policies across different identity providers or the need for additional security layers beyond what the IdP provides.

Independent MFA supports the following authenticator types:

- **Authenticator application** — Time-based one-time passwords (TOTP) using apps like Google Authenticator, Microsoft Authenticator, or Authy.
- **Security key** — Hardware security keys such as YubiKeys.
- **Biometrics** — Built-in device authenticators including Apple Touch ID, Apple Face ID, and Windows Hello.

Note

Infrastructure applications do not yet support independent MFA.

#### Configuration levels

You can configure MFA requirements at three levels:

| Level | Description |
| --- | --- |
| **Organization** | Enforce MFA by default for all applications in your account. |
| **Application** | Require or turn off MFA for a specific application. |
| **Policy** | Require or turn off MFA for users who match a specific policy. |

Settings at lower levels (policy) override settings at higher levels (organization), giving you granular control over MFA enforcement.

#### User enrollment

Users enroll their authenticators through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). To help with onboarding, administrators can share a direct enrollment link: `<your-team-name>.cloudflareaccess.com/AddMfaDevice`.

To get started with Independent MFA, refer to [Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/).

Apr 15, 2026

[<h2>New, streamlined creation experience for Access Applications and Gateway Policies</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-new-rule-and-application-builders/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The Cloudflare One dashboard now features redesigned builders for two core workflows: creating Gateway policies and configuring self-hosted Access applications.

#### Gateway rule builder

The Gateway rule builder now features a redesigned user experience, bringing it in line with the Access policy builder experience. Improvements include:

- **Streamlined UX** with clearer states and improved user interactions
- **Wirefilter editing** for viewing and editing Gateway rules directly from wirefilter expressions
- **Preview state** to review the impact of your policy in a simple graphic

![New Gateway rule builder](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=1494,format=webp/_astro/gateway-rule-builder.BxvzsN8s.png)

For more information, refer to [Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

#### Access application builder for self-hosted apps

The self-hosted Access application builder now offers a simplified creation workflow with fewer steps from setup to save. Improvements include:

- **New application selection experience** that makes choosing the right application type before you begin easier.
- **Streamlined creation flow** with fewer clicks to build and save an application
- **Inline policy creation** for building Access policies directly within the application creation flow
- **Preview state** to understand how your policies enforce user access before saving

![New Access application builder](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1970,height=1104,format=webp/_astro/access-application-builder.B__yqGin.png)

For more information, refer to [self-hosted applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/).

Apr 15, 2026

[<h2>Last seen timestamp for Cloudflare One Client devices is more consistent</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-dex-consistent-last-seen-timestamps/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

The last seen timestamp for [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.

Apr 14, 2026

[<h2>DLP account-level settings</h2>](https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

**Account-level DLP settings are now available** in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.

Key changes:

- **Consistent enforcement**: Settings configured at the account level apply to all DLP profiles
- **Simplified migration**: Settings enabled on any profile are automatically migrated to account level
- **Deprecation notice**: Profile-level advanced settings will be deprecated in a future release

**Migration details:**

During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.

Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.

For more details, refer to the [DLP settings documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/).

Apr 14, 2026

[<h2>Introducing Cloudflare Mesh</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-mesh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) is now available ([blog post ↗︎](https://blog.cloudflare.com/mesh/)). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.

![Cloudflare Mesh network map showing nodes and devices connected through Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2070,height=875,format=webp/_astro/mesh-network-map.CED6jNHK.gif)

#### What Cloudflare Mesh does

- Assigns a private [Mesh IP](https://developers.cloudflare.com/mesh/concepts/#mesh-ips) to every enrolled device and node.
- Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.
- Supports [CIDR routes](https://developers.cloudflare.com/mesh/features/routes/) for subnet routing through Mesh nodes.
- Supports [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) with active-passive replicas for nodes with routes.
- All traffic flows through Cloudflare, so [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/), [device posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/), and access rules apply to every connection.

#### What changed

- **WARP Connector** is now **Cloudflare Mesh**. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.
- **Peer-to-peer connectivity** is now called **Mesh connectivity** and is part of the Cloudflare Mesh documentation.
- **Mesh node limit** increased from 10 to **50 per account**.
- New [dashboard experience ↗︎](https://dash.cloudflare.com/?to=/:account/mesh) at **Networking** > **Mesh** with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.

#### Get started

Refer to the [Cloudflare Mesh documentation](https://developers.cloudflare.com/mesh/) to set up your first Mesh network.

Apr 14, 2026

[<h2>Detect Cloudflare API tokens with DLP</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

The **Credentials and Secrets** DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:

| Entry name | Token prefix | Detects |
| --- | --- | --- |
| Cloudflare User API Key | `cfk_` | User-scoped API keys |
| Cloudflare User API Token | `cfut_` | User-scoped API tokens |
| Cloudflare Account Owned API Token | `cfat_` | Account-scoped API tokens |

These detections target the new [Cloudflare API credential format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as `Authorization: Bearer` headers is required.

Credentials generated before this format change will not be matched by these entries.

#### How to enable Cloudflare API token detections

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **DLP** > **DLP Profiles**.
2. Select the **Credentials and Secrets** profile.
3. Turn on one or more of the new Cloudflare API token entries.
4. Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.

Example policy:

| Selector | Operator | Value | Action |
| --- | --- | --- | --- |
| DLP Profile | in | *Credentials and Secrets* | Block |

You can also enable individual entries to scope detection to specific credential types — for example, enabling **Account Owned API Token** detection without enabling **User API Key** detection.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

Apr 14, 2026

[<h2>Configure how sensitive data appears in DLP payload logs</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-configurable-payload-log-masking/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select **Zero Trust** > **Data loss prevention** > **DLP settings** and find the **Payload log masking** card.

Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:

- **Full Mask (default):** Masks the match while preserving character count and visual formatting (for example, `***-**-****` for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.
- **Partial Mask:** Reveals 25% of the matched content while masking the remainder (for example, `***-**-6789`).
- **Clear Text:** Stores the full, unmasked violation for deep investigation (for example, `123-45-6789`).

**Important:** The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.

**Applies to all enabled detections:** When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.

For more information, refer to [DLP logging options](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules).

Apr 10, 2026

[<h2>Canvas Remoting optimizes performance for productivity applications</h2>](https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Remote Browser Isolation now supports **Canvas Remoting**, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.

#### Key improvements

- **10x bandwidth reduction:** Microsoft Word and other Office apps use 90% less bandwidth
- **Smooth performance:** Google Sheets maintains consistent 30fps rendering
- **Responsive terminals:** Web-based development environments and AI notebooks work in real-time
- **Zero configuration:** Enabled by default for all Browser Isolation customers

#### How it works

Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:

1. Captures Canvas draw commands at the source
2. Converts them to lightweight vector instructions
3. Renders Canvas content on the client

This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.

#### Managing Canvas Remoting

To temporarily disable for troubleshooting:

- Right-click the isolated webpage background
- Select **Disable Canvas Remoting**
- Re-enable the same way by selecting **Enable Canvas Remoting**

#### Limitations

Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to [Canvas Remoting](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/canvas-remoting/).

Apr 9, 2026

[<h2>Send CASB posture finding instances with webhooks</h2>](https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

You can now use **CASB webhooks** in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.

This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.

To get started, go to **Integrations** > **Webhooks** in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select **Send webhook** to send it.

#### Key capabilities

- **Flexible authentication** — Configure destinations using **None**, **Basic Auth**, **Bearer Auth**, **Static Headers**, or **HMAC-Signing**.
- **Built-in testing** — Use **Test delivery** to send a test request before sending a live finding instance.
- **Posture finding workflows** — Send posture finding instances directly from the finding details workflow in **Cloud & SaaS findings**.
- **HTTPS destinations** — Configure webhook destinations with public `https://` URLs.

#### Learn more

- Configure [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/) in Cloudflare.
- Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare.

CASB webhooks are now available in Cloudflare One.

Apr 8, 2026

[<h2>User risk scoring for high risk browsing activity</h2>](https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/)

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Cloudflare One's **User Risk Scoring** now incorporates direct signals from **Gateway DNS traffic patterns**. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.

#### Why this matters

Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:

- **Security threats**: Domains associated with malware, phishing, or command-and-control (C2) centers.
- **High-risk content**: Categories such as questionable content or violence that may violate corporate compliance.

Even if a Gateway policy is set to **Block** the traffic, the interaction is still captured as a "hit" to ensure the user's risk profile reflects the attempted activity.

#### New risk behaviors

Two new behaviors are now available in the dashboard:

- **Suspicious Security Domain Visited**: Triggers when a user visits a domain in the security threats or security risk categories.
- **High risk domain visited**: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.

To learn more and get started, refer to the [User Risk Scoring documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/).

Apr 7, 2026

[<h2>Cloudflare One Client for Windows (version 2026.3.851.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-04-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

The next stable release for Windows will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.

**Changes and improvements**

- Fixed an issue causing Windows client tunnel interface initialization failure which prevented clients from establishing a tunnel for connection.
- Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
- Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
- Added monitoring for tunnel statistics collection timeouts.
- Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.
- Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.
- Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.
- Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.
- Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.
- Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
- Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.
- Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.
- Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.
- Fixed an issue where degraded Windows Management Instrumentation (WMI) state could put the client in a failed connection state loop during initialization.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 version KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution. This warning will be omitted from future release notes. This Windows update was released in July 2025.
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.
- DNS resolution may be broken when the following conditions are all true:
  - The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while the client is connected.

  To work around this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/6/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
