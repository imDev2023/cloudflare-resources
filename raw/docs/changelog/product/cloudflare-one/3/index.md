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

Mar 4, 2026

[<h2>User risk score selector in Access policies</h2>](https://developers.cloudflare.com/changelog/post/2026-03-04-user-risk-score-access-policies/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now use [user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) in your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). The new **User Risk Score** selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.

For more information, refer to [Use risk scores in Access policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies).

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

Feb 17, 2026

[<h2>Cloudflare One Product Name Updates</h2>](https://developers.cloudflare.com/changelog/post/2026-02-17-product-name-updates/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Network Flow](https://developers.cloudflare.com/network-flow/)

We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.

We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.

#### What's changing

- **Magic WAN** → **Cloudflare WAN**
- **Magic WAN IPsec** → **Cloudflare IPsec**
- **Magic WAN GRE** → **Cloudflare GRE**
- **Magic WAN Connector** → **Cloudflare One Appliance**
- **Magic Firewall** → **Cloudflare Network Firewall**
- **Magic Network Monitoring** → **Network Flow**
- **Magic Cloud Networking** → **Cloudflare One Multi-cloud Networking**

**No action is required by you** — all functionality, existing configurations, and billing will remain exactly the same.

For more information, visit the [Cloudflare One documentation](https://developers.cloudflare.com/cloudflare-one/).

Feb 11, 2026

[<h2>Post-quantum encryption support for Cloudflare One Appliance</h2>](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance version 2026.2.0 adds [post-quantum encryption](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.

This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.

For more information, refer to [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/).

Jan 30, 2026

[<h2>BGP over GRE and IPsec tunnels</h2>](https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

For configuration details, refer to:

- [Configure BGP routes for Magic WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
- [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)

Jan 27, 2026

[<h2>Configure Cloudflare source IPs (beta)</h2>](https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.

For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:

- Symmetric routing over private network connections
- Proper firewall state preservation
- Private traffic stays on secure paths

Key details:

- **IPv4**: Sourced from `100.64.0.0/12` by default, configurable to any `/12` CIDR
- **IPv6**: Sourced from `2606:4700:cf1:5000::/64` (not configurable)
- **Affected connectors**: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)

Configuring Cloudflare source IPs requires Unified Routing (beta) and the `Cloudflare One Networks Write` permission.

For configuration details, refer to [Configure Cloudflare source IPs](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/).

Jan 22, 2026

[<h2>Require Access protection for zones</h2>](https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.

This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.

![Require Cloudflare Access protection in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2160,height=738,format=webp/_astro/require-cloudflare-access-protection.BAUmTYOs.png)

#### How it works

- **Blocked by default**: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.
- **Explicit access required**: To allow traffic, create an Access application with an Allow or Bypass policy.
- **Hostname exemptions**: You can exempt specific hostnames from this requirement.

To turn on this feature, refer to [Require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/).

Dec 31, 2025

[<h2>Breakout traffic visibility via NetFlow</h2>](https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.

This feature allows you to:

- Monitor breakout traffic statistics in the Cloudflare dashboard.
- View traffic patterns for applications configured to bypass Cloudflare.
- Maintain visibility across all traffic passing through your Magic WAN Connector.

For more information, refer to [NetFlow statistics](https://developers.cloudflare.com/cloudflare-wan/analytics/netflow-analytics/).

Dec 17, 2025

[<h2>Shadow IT - domain level SaaS analytics</h2>](https://developers.cloudflare.com/changelog/post/2025-12-17-shadow-it-domain-analytics/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust has again upgraded its **Shadow IT analytics**, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.

With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.

![New Domain Level Metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=452,format=webp/_astro/shadow-it-domain.DoZnGAtf.png)

These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.

Both the analytics and policies are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

Dec 16, 2025

[<h2>New duplicate action for supported Cloudflare One resources</h2>](https://developers.cloudflare.com/changelog/post/2025-12-16-new-duplicate-action-for-supported-cloudflare-one-resources/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now duplicate specific Cloudflare One resources with a single click from the dashboard.

Initially supported resources:

- Access Applications
- Access Policies
- Gateway Policies

To try this out, simply click on the overflow menu (⋮) from the resource table and click *Duplicate*. We will continue to add the Duplicate action for resources throughout 2026.

Nov 17, 2025

[<h2>New Cloudflare One Navigation and Product Experience</h2>](https://developers.cloudflare.com/changelog/post/new-cloudflare-one-navigation-and-product-experience/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The Zero Trust dashboard and navigation is receiving significant and exciting updates. The dashboard is being restructured to better support common tasks and workflows, and various pages have been moved and consolidated.

There is a new guided experience on login detailing the changes, and you can use the Zero Trust dashboard search to find product pages by both their new and old names, as well as your created resources. To replay the guided experience, you can find it in Overview > Get Started.

![Cloudflare One Dash Changes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1388,height=1546,format=webp/_astro/cf1-dash-changes.Uk_Y-2V-.png)

Notable changes

- Product names have been removed from many top-level navigation items to help bring clarity to what they help you accomplish. For example, you can find Gateway policies under ‘Traffic policies' and CASB findings under ‘Cloud & SaaS findings.'
- You can view all analytics, logs, and real-time monitoring tools from ‘Insights.'
- ‘Networks' better maps the ways that your corporate network interacts with Cloudflare. Some pages like Tunnels, are now a tab rather than a full page as part of these changes. You can find them at Networks > Connectors.
- Settings are now located closer to the tools and resources they impact. For example, this means you'll find your WARP configurations at Team & Resources > Devices.

![New Cloudflare One Navigation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=514,height=1112,format=webp/_astro/new-cf1-navigation.B7-E-9CV.png)

No changes to our API endpoint structure or to any backend services have been made as part of this effort.

Nov 6, 2025

[<h2>Automatic Return Routing (Beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.

Key benefits:

- **Route-less mode**: Static or dynamic routes are optional when using ARR.
- **Overlapping IP space support**: Traffic originating from customer sites can use overlapping private IP ranges.
- **Symmetric routing**: Return traffic is guaranteed to use the same connection as the original on-ramp.

This feature is currently in beta and requires the new Unified Routing mode (beta).

For configuration details, refer to [Configure Automatic Return Routing](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing).

Nov 6, 2025

[<h2>Designate WAN link for breakout traffic</h2>](https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.

With this feature, you can:

- Pin breakout traffic for specific applications to a preferred WAN port.
- Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.
- Benefit from automatic failover to standard WAN port priority if the preferred port goes down.

This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.

For configuration details, refer to [Designate WAN ports for breakout apps](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps).

Sep 16, 2025

[<h2>New AI-Enabled Search for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.

![Example search results in the Zero Trust dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1750,height=1568,format=webp/_astro/searchexample.Di8yS8ju.png)

**Ask Cloudy** — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.

Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.

**Find Recents** — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.

Aug 27, 2025

[<h2>Shadow IT - SaaS analytics dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-08-27-shadow-it-analytics/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust has significantly upgraded its **Shadow IT analytics**, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.

You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including **Unreviewed**, **In Review**, **Approved**, and **Unapproved** designating how they can be used in your organization.

![Cloudflare One Analytics Dashboards](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2814,height=1486,format=webp/_astro/shadow-it-analytics.BLNnG72w.png)

These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.

Both the analytics and policies are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

Jul 21, 2025

[<h2>Virtual Cloudflare One Appliance with KVM support (open beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.

Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.

For setup instructions, refer to [Configure a virtual Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Jul 10, 2025

[<h2>New onboarding guides for Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/2025-07-09-onboarding-resources/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Use our brand new onboarding experience for Cloudflare Zero Trust. New and returning users can now engage with a **Get Started** tab with walkthroughs for setting up common use cases end-to-end.

![Zero Trust onboarding guides](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=966,format=webp/_astro/zt-onboarding-guides._18EfPbe.png)

There are eight brand new onboarding guides in total:

- Securely access a private network (sets up device client and Tunnel)
- Device-to-device / mesh networking (sets up and connects multiple device clients)
- Network to network connectivity (sets up and connects multiple WARP Connectors, makes reference to Magic WAN availability for Enterprise)
- Secure web traffic (sets up device client, Gateway, pre-reqs, and initial policies)
- Secure DNS for networks (sets up a new DNS location and Gateway policies)
- Clientless web access (sets up Access to a web app, Tunnel, and public hostname)
- Clientless SSH access (all the same + the web SSH experience)
- Clientless RDP access (all the same + RDP-in-browser)

Each flow walks the user through the steps to configure the essential elements, and provides a “more details” panel with additional contextual information about what the user will accomplish at the end, along with why the steps they take are important.

Try them out now in the [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/?to=/:account/home)!

Jul 7, 2025

[<h2>Cloudy summaries for Access and Gateway Logs</h2>](https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudy, Cloudflare's AI Agent, will now automatically summarize your [Access](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/) and [Gateway](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/) block logs.

In the log itself, Cloudy will summarize what occurred and why. This will be helpful for quick troubleshooting and issue correlation.

![Cloudy AI summarizes a log](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=472,format=webp/_astro/cloudy-explanation.oFZR6cXa.png)

If you have feedback about the Cloudy summary - good or bad - you can provide that right from the summary itself.

Jul 7, 2025

[<h2>New App Library for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-07-07-dashboard-app-library/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare Zero Trust customers can use the App Library to get full visibility over the SaaS applications that they use in their Gateway policies, CASB integrations, and Access for SaaS applications.

**App Library**, found under **My Team**, makes information available about all Applications that can be used across the Zero Trust product suite.

![Zero Trust App Library](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1089,height=548,format=webp/_astro/app-library.D403GJ9j.png)

You can use the App Library to see:

- How Applications are defined
- Where they are referenced in policies
- Whether they have Access for SaaS configured
- Review their CASB findings and integration status.

Within individual Applications, you can also track their usage across your organization, and better understand user behavior.

Jun 23, 2025

[<h2>Data Security Analytics in the Zero Trust dashboard</h2>](https://developers.cloudflare.com/changelog/post/cf1-data-security-analytics-v1/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust now includes **Data security analytics**, providing you with unprecedented visibility into your organization sensitive data.

The new dashboard includes:

- **Sensitive Data Movement Over Time:**
  - See patterns and trends in how sensitive data moves across your environment. This helps understand where data is flowing and identify common paths.
- **Sensitive Data at Rest in SaaS & Cloud:**
  - View an inventory of sensitive data stored within your corporate SaaS applications (for example, Google Drive, Microsoft 365) and cloud accounts (such as AWS S3).
- **DLP Policy Activity:**
  - Identify which of your Data Loss Prevention (DLP) policies are being triggered most often.
  - See which specific users are responsible for triggering DLP policies.

![Data Security Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3254,height=1580,format=webp/_astro/cf1-data-security-analytics-v1.BGl6fYXl.png)

To access the new dashboard, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Insights** on the sidebar.

Jun 5, 2025

[<h2>Cloudflare One Analytics Dashboards and Exportable Access Report</h2>](https://developers.cloudflare.com/changelog/post/dashboards-access-report/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.

!\[Cloudflare One Analytics Dashboards](\~/assets/images/changelog/cloudflare-one/Analytics Dashboards.png)

Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A **preview** of the report is shown below, with more to be found in the report:

![Cloudflare One Analytics Dashboards](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=950,format=webp/_astro/access-report.C744W7JR.png)

Both features are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

May 29, 2025

[<h2>New Gateway Analytics in the Cloudflare One Dashboard</h2>](https://developers.cloudflare.com/changelog/post/gateway-analytics-v2/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Users can now access significant enhancements to Cloudflare Gateway analytics, providing you with unprecedented visibility into your organization's DNS queries, HTTP requests, and Network sessions. These powerful new dashboards enable you to go beyond raw logs and gain actionable insights into how your users are interacting with the Internet and your protected resources.

You can now visualize and explore:

- Patterns Over Time: Understand trends in traffic volume and blocked requests, helping you identify anomalies and plan for future capacity.
- Top Users & Destinations: Quickly pinpoint the most active users, enabling better policy enforcement and resource allocation.
- Actions Taken: See a clear breakdown of security actions applied by Gateway policies, such as blocks and allows, offering a comprehensive view of your security posture.
- Geographic Regions: Gain insight into the global distribution of your traffic.

![Gateway Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2740,height=1166,format=webp/_astro/gateway-analytics.BdSwbIBb.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and go to Analytics in the side navigation bar.

May 18, 2025

[<h2>New Applications Added to Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/new-applications-71825/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

42 new applications have been added for Zero Trust support within the Application Library and Gateway policy enforcement, giving you the ability to investigate or apply inline policies to these applications.

33 of the 42 applications are Artificial Intelligence applications. The others are Human Resources (2 applications), Development (2 applications), Productivity (2 applications), Sales & Marketing, Public Cloud, and Security.

To view all available applications, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), navigate to the **App Library** under **My Team**.

For more information on creating Gateway policies, see our [Gateway policy documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

May 16, 2025

[<h2>New Access Analytics in the Cloudflare One Dashboard</h2>](https://developers.cloudflare.com/changelog/post/access-analytics-v2/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

A new Access Analytics dashboard is now available to all Cloudflare One customers. Customers can apply and combine multiple filters to dive into specific slices of their Access metrics. These filters include:

- Logins granted and denied
- Access events by type (SSO, Login, Logout)
- Application name (Salesforce, Jira, Slack, etc.)
- Identity provider (Okta, Google, Microsoft, onetimepin, etc.)
- Users ( `chris@cloudflare.com`, `sally@cloudflare.com`, `rachel@cloudflare.com`, etc.)
- Countries (US, CA, UK, FR, BR, CN, etc.)
- Source IP address
- App type (self-hosted, Infrastructure, RDP, etc.)

![Access Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2030,height=1720,format=webp/_astro/accessanalytics.DYXgwZCl.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and find Analytics in the side navigation bar.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-one/3/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product/cloudflare-one/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
