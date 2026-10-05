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

Jan 12, 2026

[<h2>Enhanced visibility for post-delivery actions</h2>](https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.

Note

Error messages will vary depending on whether you are using Google Workspace or Microsoft 365.

![failure-log-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2348,height=1692,format=webp/_astro/enhanced-visibility-post-delivery-actions.BNiyPtJU.png)

This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.

This applies to all Email Security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Jan 8, 2026

[<h2>Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</h2>](https://developers.cloudflare.com/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare [admin activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/) now capture each time a [DNS over HTTP (DoH) user](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/) is created.

These logs can be viewed from the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com/), pulled via the [Cloudflare API](https://developers.cloudflare.com/api/), and exported through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

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

Dec 9, 2025

[<h2>WARP client for Windows (version 2025.10.118.1)</h2>](https://developers.cloudflare.com/changelog/post/2025-12-09-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes and improvements.

**Changes and improvements**

- The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.
- Fixed an issue where sending large messages to the WARP daemon by Inter-Process Communication (IPC) could cause WARP to crash and result in service interruptions.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

Dec 9, 2025

[<h2>WARP client for macOS (version 2025.10.118.1)</h2>](https://developers.cloudflare.com/changelog/post/2025-12-09-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes and improvements.

**Changes and improvements**

- The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.

Dec 3, 2025

[<h2>Reclassifications to Submissions</h2>](https://developers.cloudflare.com/changelog/post/2025-12-03-submission-terminology-update/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.

Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.

![nav\_example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=756,height=628,format=webp/_astro/reclassification-submission.B6nL5Hw7.png)

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Nov 18, 2025

[<h2>Adjustment to Final Disposition Column</h2>](https://developers.cloudflare.com/changelog/post/2025-11-18-temporary-adjustment-to-final-disposition-column/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

#### Adjustment to Final Disposition column

#### The **Final Disposition** column in **Submissions** > **Team Submissions** tab is changing for non-Phishguard customers.

#### What's Changing

- Column will be called **Status** instead of **Final Disposition**
- Column status values will now be: **Submitted**, **Accepted** or **Rejected**.

#### Next Steps

We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.

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

Nov 14, 2025

[<h2>Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

SSH with [Cloudflare Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.

Previously, users had to generate this certificate by using the [Cloudflare API ↗︎](https://developers.cloudflare.com/api/) directly. With this update, you can now create and manage this certificate in the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com) from the **Access controls** > **Service credentials** page.

![Navigate to Access controls and then Service credentials to see where you can generate an SSH CA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2710,height=1180,format=webp/_astro/SSH-CA-generation.DYa9RnX1.png)

For more details, refer to [Generate a Cloudflare SSH CA](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca).

Nov 14, 2025

[<h2>New SaaS Security weekly digests with API CASB</h2>](https://developers.cloudflare.com/changelog/post/2025-11-14-casb-digest/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

You can now stay on top of your SaaS security posture with the new **CASB Weekly Digest** notification. This opt-in email digest is delivered to your inbox every Monday morning and provides a high-level summary of your organization's Cloudflare API CASB findings from the previous week.

This allows security teams and IT administrators to get proactive, at-a-glance visibility into new risks and integration health without having to log in to the dashboard.

To opt in, navigate to **Manage Account** > **Notifications** in the Cloudflare dashboard to configure the **CASB Weekly Digest** alert type.

#### Key capabilities

- **At-a-glance summary** — Review new high/critical findings, most frequent finding types, and new content exposures from the past 7 days.
- **Integration health** — Instantly see the status of all your connected SaaS integrations (Healthy, Unhealthy, or Paused) to spot API connection issues.
- **Proactive alerting** — The digest is sent automatically to all subscribed users every Monday morning.
- **Easy to configure** — Users can opt in by enabling the notification in the Cloudflare dashboard under **Manage Account** > **Notifications**.

#### Learn more

- Configure [notification preferences](https://developers.cloudflare.com/notifications/) in Cloudflare.

The CASB Weekly Digest notification is available to all Cloudflare users today.

Nov 12, 2025

[<h2>DEX Logpush jobs</h2>](https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.

We've released four new WARP and DEX device data sets that can be exported via [Cloudflare Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.

1. [DEX Application Tests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/)
2. [DEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/)
3. [WARP Config Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_config_changes/)
4. [WARP Toggle Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/)

To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard > Analytics & Logs > Logpush to get started.

![DEX logpush job creation dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2549,height=1283,format=webp/_astro/dex_logpush_datasets.CtCk36pX.png)

Nov 11, 2025

[<h2>WARP client for Windows (version 2025.9.558.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-11-11-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features including [Path Maximum Transmission Unit Discovery (PMTUD)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery). When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.

**Changes and improvements**

- Fixed an inconsistency with [Global WARP override](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices) settings in multi-user environments when switching between users.
- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.
- Fixed an issue where deleting a registration was erroneously reported as having failed.
- Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the [PMTUD documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery).
- Improvements for the [OS version](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/warp-client-checks/os-version/) WARP client check. Windows Updated Build Revision (UBR) numbers can now be checked by the client to ensure devices have required security patches and features installed.
- The WARP client now supports Windows 11 ARM-based machines. For information on known limitations, refer to the [Known limitations page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#cloudflare-one-client-disconnected-on-windows-arm).

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

Nov 11, 2025

[<h2>WARP client for macOS (version 2025.9.558.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-11-11-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features including [Path Maximum Transmission Unit Discovery (PMTUD)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery). When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.

**Changes and improvements**

- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.
- Fixed an issue where deleting a registration was erroneously reported as having failed.
- Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the [PMTUD documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery).

**Known issues**

- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).

Nov 11, 2025

[<h2>WARP client for Linux (version 2025.9.558.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features including [Path Maximum Transmission Unit Discovery (PMTUD)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery). When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.

WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at [pkg.cloudflareclient.com](https://pkg.cloudflareclient.com/).

**Changes and improvements**

- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.
- Fixed an issue where deleting a registration was erroneously reported as having failed.
- Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the [PMTUD documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery).

Nov 11, 2025

[<h2>cloudflared proxy-dns command will be removed starting February 2, 2026</h2>](https://developers.cloudflare.com/changelog/post/2025-11-11-cloudflared-proxy-dns/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting February 2, 2026, the `cloudflared proxy-dns` command will be removed from all new `cloudflared` [releases](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/).

This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the `proxy-dns` command and does not affect any other `cloudflared` features, such as the core [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) service.

The `proxy-dns` command, which runs a client-side [DNS-over-HTTPS (DoH)](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.

Versions of `cloudflared` released before this date will not be affected and will continue to operate. However, note that our [official support policy](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases) for any `cloudflared` release is one year from its release date.

#### Migration paths

We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure [DNS-over-HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/).

#### End-user devices

The preferred method for enabling DNS-over-HTTPS on user devices is the [Cloudflare WARP client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's [Zero Trust policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and [posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/).

#### Servers, routers, and IoT devices

For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the [WARP Connector](https://developers.cloudflare.com/mesh/).

Instead of running `cloudflared proxy-dns` on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your [entire subnet](https://developers.cloudflare.com/mesh/features/routes/) to Cloudflare for [filtering and logging](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

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

Nov 6, 2025

[<h2>Applications to be remapped to the new categories</h2>](https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to [Changelog](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/#2025-10-28). While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories. The remapping of existing applications into these new categories will be completed by January 30, 2026. This timeline allows you a dedicated period to:

- Review the new category structure.
- Identify any policies you have that target the older categories.
- Adjust your rules to reference the new, more precise categories before the old mappings change. Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.

**Applications being remappedd**

| Application Name | Existing Category | New Category |
| --- | --- | --- |
| Google Photos | File Sharing | Photography & Graphic Design |
| Flickr | File Sharing | Photography & Graphic Design |
| ADP | Human Resources | Business |
| Greenhouse | Human Resources | Business |
| myCigna | Human Resources | Health & Fitness |
| UnitedHealthcare | Human Resources | Health & Fitness |
| ZipRecruiter | Human Resources | Business |
| Amazon Business | Human Resources | Business |
| Jobcenter | Human Resources | Business |
| Jobsuche | Human Resources | Business |
| Zenjob | Human Resources | Business |
| DocuSign | Legal | Business |
| Postident | Legal | Business |
| Adobe Creative Cloud | Productivity | Photography & Graphic Design |
| Airtable | Productivity | Development |
| Autodesk Fusion360 | Productivity | IT Management |
| Coursera | Productivity | Education |
| Microsoft Power BI | Productivity | Business |
| Tableau | Productivity | Business |
| Duolingo | Productivity | Education |
| Adobe Reader | Productivity | Business |
| AnpiReport | Productivity | Travel |
| ビズリーチ | Productivity | Business |
| doda (デューダ) | Productivity | Business |
| 求人ボックス | Productivity | Business |
| マイナビ2026 | Productivity | Business |
| Power Apps | Productivity | Business |
| RECRUIT AGENT | Productivity | Business |
| シフトボード | Productivity | Business |
| スタンバイ | Productivity | Business |
| Doctolib | Productivity | Health & Fitness |
| Miro | Productivity | Photography & Graphic Design |
| MyFitnessPal | Productivity | Health & Fitness |
| Sentry Mobile | Productivity | Travel |
| Slido | Productivity | Photography & Graphic Design |
| Arista Networks | Productivity | IT Management |
| Atlassian | Productivity | Business |
| CoderPad | Productivity | Business |
| eAgreements | Productivity | Business |
| Vmware | Productivity | IT Management |
| Vmware Vcenter | Productivity | IT Management |
| AWS Skill Builder | Productivity | Education |
| Microsoft Office 365 (GCC) | Productivity | Business |
| Microsoft Exchange Online (GCC) | Productivity | Business |
| Canva | Sales & Marketing | Photography & Graphic Design |
| Instacart | Shopping | Food & Drink |
| Wawa | Shopping | Food & Drink |
| McDonald's | Shopping | Food & Drink |
| Vrbo | Shopping | Travel |
| American Airlines | Shopping | Travel |
| Booking.com | Shopping | Travel |
| Ticketmaster | Shopping | Entertainment & Events |
| Airbnb | Shopping | Travel |
| DoorDash | Shopping | Food & Drink |
| Expedia | Shopping | Travel |
| EasyPark | Shopping | Travel |
| UEFA Tickets | Shopping | Entertainment & Events |
| DHL Express | Shopping | Business |
| UPS | Shopping | Business |

For more information on creating HTTP policies, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

Oct 28, 2025

[<h2>Access private hostname applications support all ports/protocols</h2>](https://developers.cloudflare.com/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Cloudflare Access for private hostname applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) can now secure traffic on all ports and protocols.

Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port `443` and support Server Name Indicator (SNI).

This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.

![Example private application on non-443 port](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1283,height=496,format=webp/_astro/internal_private_app_any_port.DNXnEy0u.png)

For example, you can now create a self-hosted application in Access for `ssh.testapp.local` running on port `22`. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.

This feature is generally available across all plans.

Oct 28, 2025

[<h2>CASB introduces new granular roles</h2>](https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:

- **Cloudflare CASB Read:** Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.
- **Cloudflare CASB:** Provides full administrative access to configure and manage all aspects of the CASB product.

These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the **Super Administrator** or **Administrator** roles.

To enable [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/), scans in CASB, account members will need the **Cloudflare Zero Trust** role.

You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under **Manage Account** > **Members**.

To learn more about managing roles and permissions, refer to the [Manage account members and roles documentation](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

Oct 28, 2025

[<h2>New Application Categories added for HTTP Traffic Management</h2>](https://developers.cloudflare.com/changelog/post/Gateway-application-categories-added/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

To give you precision and flexibility while creating policies to block unwanted traffic, we are introducing new, more granular application categories in the Gateway product.

We have added the following categories to provide more precise organization and allow for finer-grained policy creation, designed around how users interact with different types of applications:

- Business
- Education
- Entertainment & Events
- Food & Drink
- Health & Fitness
- Lifestyle
- Navigation
- Photography & Graphic Design
- Travel

The new categories are live now, but we are providing a transition period for existing applications to be fully remapped to these new categories.

The full remapping will be completed by January 30, 2026.

We encourage you to use this time to:

- Review the new category structure.
- Identify and adjust any existing HTTP policies that reference older categories to ensure a smooth transition.

For more information on creating HTTP policies, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

Oct 20, 2025

[<h2>Schedule DNS policies from the UI</h2>](https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Admins can now create [scheduled DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/timed-policies/) directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.

- **Preset Schedules**: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.
- **Custom Schedules**: Define your own schedule with specific days and up to three non-overlapping time ranges per day.
- **Timezone Control**: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.
- **Combined with Duration**: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.

You can see the flow in the demo GIF:

![Schedule DNS policies demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1053,height=879,format=webp/_astro/gateway-dns-scheduled-policies-ui.Cf4l1OTE.gif)

This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.

Oct 17, 2025

[<h2>On-Demand Security Report</h2>](https://developers.cloudflare.com/changelog/post/2025-10-16-on-demand-security-report/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now generate on-demand security reports directly from the Cloudflare dashboard. This new feature provides a comprehensive overview of your email security posture, making it easier than ever to demonstrate the value of Cloudflare’s Email security to executives and other decision makers.

These reports offer several key benefits:

- **Executive Summary:** Quickly view the performance of Email security with a high-level executive summary.
- **Actionable Insights:** Dive deep into trend data, breakdowns of threat types, and analysis of top targets to identify and address vulnerabilities.
- **Configuration Transparency:** Gain a clear view of your policy, submission, and domain configurations to ensure optimal setup.
- **Account Takeover Risks:** Get a snapshot of your M365 risky users (requires a Microsoft Entra ID P2 license and [M365 SaaS integration ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/)).

To get started, refer to [Download a security report](https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/#download-a-security-report). ![Report](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1009,height=571,format=webp/_astro/report.CbkPa8Jt.png)

This feature is available across the following Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
