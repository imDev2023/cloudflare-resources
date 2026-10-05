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

Oct 16, 2025

[<h2>WARP client for Windows (version 2025.9.173.1)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-16-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.

**Changes and improvements**

- Improvements for [Windows multi-user](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/) to maintain the [Global WARP override](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices) state when switching between users.
- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.
- Deleting registrations no longer returns an error when succeeding.
- Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

Oct 16, 2025

[<h2>WARP client for macOS (version 2025.9.173.1)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-16-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.

**Changes and improvements**

- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.
- Deleting registrations no longer returns an error when succeeding.
- Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.

**Known issues**

- macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).

Oct 16, 2025

[<h2>Monitor Groups for Advanced Health Checking With Load Balancing</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-monitor-groups-for-load-balancing/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.

With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.

#### What you can do:

- **Combine Multiple Monitors**: Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific `/login` service.
- **Isolate Monitors for Observation**: Mark a monitor as "monitoring only" to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.
- **Improve Steering Intelligence**: Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.

This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.

For detailed information and API configuration guides, please visit our [developer documentation](https://developers.cloudflare.com/load-balancing/monitors/monitor-groups) for Monitor Groups.

Oct 10, 2025

[<h2>New domain categories added</h2>](https://developers.cloudflare.com/changelog/post/2025-10-10-new-domain-categories/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We have added three new domain categories under the Technology parent category, to better reflect online content and improve DNS filtering.

**New categories added**

| Parent ID | Parent Name | Category ID | Category Name |
| --- | --- | --- | --- |
| 26 | Technology | 194 | Keep Awake Software |
| 26 | Technology | 192 | Remote Access |
| 26 | Technology | 193 | Shareware/Freeware |

Refer to [Gateway domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/) to learn more.

Oct 7, 2025

[<h2>WARP client for Linux (version 2025.8.779.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains significant fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at [pkg.cloudflareclient.com](https://pkg.cloudflareclient.com/).

**Changes and improvements**

- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.
- The MASQUE protocol is now the only protocol that can use [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode). If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.

**Known issues**

- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).

Oct 7, 2025

[<h2>WARP client for Windows (version 2025.8.779.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains significant fixes and improvements.

**Changes and improvements**

- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.
- The MASQUE protocol is now the only protocol that can use [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode). If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.

**Known issues**

- For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).
- Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.
- DNS resolution may be broken when the following conditions are all true:
  - WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
  - A custom DNS server address is configured on the primary network adapter.
  - The custom DNS server address on the primary network adapter is changed while WARP is connected.

  To work around this issue, reconnect the WARP client by toggling off and back on.

Oct 7, 2025

[<h2>WARP client for macOS (version 2025.8.779.0)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains significant fixes and improvements.

**Changes and improvements**

- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.
- The MASQUE protocol is now the only protocol that can use [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode). If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.

**Known issues**

- macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).

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

Sep 30, 2025

[<h2>Application granular controls for operations in SaaS applications</h2>](https://developers.cloudflare.com/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway users can now apply granular controls to their file sharing and AI chat applications through [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies).

The new feature offers two methods of controlling SaaS applications:

- **Application Controls** are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include *Upload*, *Download*, *Prompt*, *Voice*, and *Share* depending on the application.
- **Operations** are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.

Get started using [Application Granular Controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls) and refer to the list of [supported applications](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications).

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

Sep 23, 2025

[<h2>Invalid Submissions Feedback</h2>](https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.

To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user [submission aliases](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/):

- **Email Notifications:** We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to **[Settings ↗︎](https://one.dash.cloudflare.com/?to=/:account/email-security/settings)** > **Invalid submission emails** and turn the feature off.

![EmailSec-Invalid-Submissions-Toggle](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=175,format=webp/_astro/EmailSec-Invalid-Submissions-Toggle.DXjbR6aX.png)

- **Invalid Submission dashboard:** You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.

![EmailSec-Invalid-Submissions-Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=511,format=webp/_astro/EmailSec-Invalid-Submissions-Dashboard.zuf1on2n.png)

Learn more about this feature on [invalid submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/invalid-submissions/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Sep 22, 2025

[<h2>Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</h2>](https://developers.cloudflare.com/changelog/post/2025-09-22-browser-based-rdp-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.

Since we announced our [open beta](https://developers.cloudflare.com/changelog/access/#2025-06-30), we've made a few improvements:

- Support for targets with IPv6.
- Support for [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/) and [WARP Connector](https://developers.cloudflare.com/mesh/) as on-ramps.
- More robust error messaging on the login page to help you if you encounter an issue.
- Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.
- Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.

As a refresher, here are some benefits browser-based RDP provides:

- **Control how users authenticate to internal RDP resources** with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.
- **Record who is accessing which servers and when** to support regulatory compliance requirements and to gain greater visibility in the event of a security event.
- **Eliminate the need to install and manage software on user devices**. You will only need a web browser.
- **Reduce your attack surface** by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.

![Example of a browser-based RDP Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2132,height=1814,format=webp/_astro/browser-based-rdp-access-app.BNXce1JL.png)

To get started, refer to [Connect to RDP in a browser](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/).

Sep 18, 2025

[<h2>Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</h2>](https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

You can now route private traffic to [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is **free for all Cloudflare One customers**.

Previously, Tunnel routes could only be defined by IP address or [CIDR range](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/). This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.

![Hostname-based routing in Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1990,height=530,format=webp/_astro/tunnel-hostname-routing.DSi8MP_7.webp)

**What’s new:**

- **Hostname & Domain Routing**: Create routes for individual hostnames (e.g., `payroll.acme.local`) or entire domains (e.g., `*.acme.local`) and direct their traffic to a specific Tunnel.
- **Simplified Zero Trust Policies**: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.
- **Precise Egress Control**: Route traffic for public hostnames (e.g., `bank.example.com`) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.
- **No More IP Lists**: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.

Get started in the Tunnels section of the Zero Trust dashboard with your first [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) or [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) route.

Learn more in our [blog post ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/).

Sep 16, 2025

[<h2>New AI-Enabled Search for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.

![Example search results in the Zero Trust dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1750,height=1568,format=webp/_astro/searchexample.Di8yS8ju.png)

**Ask Cloudy** — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.

Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.

**Find Recents** — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.

Sep 11, 2025

[<h2>Regional Email Processing for Germany, India, or Australia</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: **MX**, **BCC**, and **Journaling**.

#### What’s new

Customers can now select where their email is processed. The following regions are supported:

- **Germany**
- **India**
- **Australia**

Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.

#### How to use it

When onboarding a domain with MX, BCC, or Journaling:

1. Select the desired processing location (Germany, India, or Australia).
2. The UI will display updated processing addresses specific to that region.
3. For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.

#### Availability

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

#### What’s next

We’re expanding the list of processing locations to match our [Data Localization Suite (DLS)](https://developers.cloudflare.com/data-localization/) footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.

Sep 11, 2025

[<h2>DNS filtering for private network onramps</h2>](https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

[Magic WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering) and [WARP Connector](https://developers.cloudflare.com/mesh/features/routes/#dns-filtering) users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.

Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including [Internal DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#internal-dns) and [hostname-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites).

To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, `172.64.36.1` and `172.64.36.2`. Once you configure DNS resolution and filtering, you can use *Source Internal IP* as a traffic selector in your [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) for routing private DNS traffic to your [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/).

Sep 8, 2025

[<h2>Custom IKE ID for IPsec Tunnels</h2>](https://developers.cloudflare.com/changelog/post/2025-09-08-custom-ike-id-ipsec-tunnels/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.

This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the [Custom IKE ID feature and the API call to configure it](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/).

Sep 5, 2025

[<h2>Bidirectional tunnel health checks are compatible with all Magic on-ramps</h2>](https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.

Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.

There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.

Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.

Sep 2, 2025

[<h2>Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</h2>](https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting **December 1, 2025**, list endpoints for the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.

No action is required if you already explicitly set `is_deleted=false` or if you only need to list active resources.

This change affects the following API endpoints:

- List all tunnels: [`GET /accounts/{account_id}/tunnels`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list/)
- List [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/): [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/)
- List [WARP Connector](https://developers.cloudflare.com/mesh/) tunnels: [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/)
- List tunnel routes: [`GET /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/)
- List subnets: [`GET /accounts/{account_id}/zerotrust/subnets`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/)
- List virtual networks: [`GET /accounts/{account_id}/teamnet/virtual_networks`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/)

#### What is changing?

The default behavior of the `is_deleted` query parameter will be updated.

| Scenario | Previous behavior (before December 1, 2025) | New behavior (from December 1, 2025) |
| --- | --- | --- |
| `is_deleted` parameter is omitted | Returns **active & deleted** tunnels, routes, subnets and virtual networks | Returns **only active** tunnels, routes, subnets and virtual networks |

#### Action required

If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the `is_deleted` parameter before **December 1, 2025**.

To get a list of only deleted resources, you must now explicitly add the `is_deleted=true` query parameter to your request:

```bash
# Example: Get ONLY deleted Tunnels
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true" \
     -H "Authorization: Bearer $API_TOKEN"

# Example: Get ONLY deleted Virtual Networks
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true" \
     -H "Authorization: Bearer $API_TOKEN"
```

Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using `is_deleted=false`) and one to get deleted items (`is_deleted=true`).

#### Why we’re making this change

This update is based on user feedback and aims to:

- **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
- **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
- **Improve performance:** For most users, the default query result will now be smaller and more relevant.

To learn more, please visit the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) documentation.

Sep 1, 2025

[<h2>Updated Email security roles</h2>](https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

To provide more granular controls, we refined the [existing roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#email-security-roles) for Email security and launched a new Email security role as well.

All Email security roles no longer have read or write access to any of the other Zero Trust products:

- **Email Configuration Admin**
- **Email Integration Admin**
- **Email security Read Only**
- **Email security Analyst**
- **Email security Policy Admin**
- **Email security Reporting**

To configure [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) or [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation), you now need to be an admin for the Zero Trust dashboard with the **Cloudflare Zero Trust** role.

Also through customer feedback, we have created a new additive role to allow **Email security Analyst** to create, edit, and delete Email security policies, without needing to provide access via the **Email Configuration Admin** role. This role is called **Email security Policy Admin**, which can read all settings, but has write access to [allow policies](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/), and [blocked senders](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Aug 29, 2025

[<h2>Cloudflare One WARP Diagnostic AI Analyzer</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-warp-AI-diag-analyzer/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

We're excited to share a new AI feature, the [WARP diagnostic analyzer ↗︎](https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/), to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the [Cloudflare One dashboard ↗︎](https://dash.cloudflare.com/one/) to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing [remote captures](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture) of [WARP diagnostic logs](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs). The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to [WARP diagnostics analyzer (beta)](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta) to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.

Aug 29, 2025

[<h2>DEX MCP Server</h2>](https://developers.cloudflare.com/changelog/post/2025-08-29-dex-mcp-server/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device connectivity and performance across your Cloudflare SASE deployment.

We've released an MCP server [(Model Context Protocol) ↗︎](https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) for DEX.

The DEX MCP server is an AI tool that allows customers to ask a question like, "Show me the connectivity and performance metrics for the device used by carly‌@acme.com", and receive an answer that contains data from the DEX API.

Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.

Customers can test the new DEX MCP server in less than one minute. To learn more, read the [DEX MCP server documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/dex-mcp-server/).

Aug 27, 2025

[<h2>Shadow IT - SaaS analytics dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-08-27-shadow-it-analytics/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Zero Trust has significantly upgraded its **Shadow IT analytics**, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.

You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including **Unreviewed**, **In Review**, **Approved**, and **Unapproved** designating how they can be used in your organization.

![Cloudflare One Analytics Dashboards](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2814,height=1486,format=webp/_astro/shadow-it-analytics.BLNnG72w.png)

These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.

Both the analytics and policies are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

Aug 26, 2025

[<h2>New CASB integrations for ChatGPT, Claude, and Gemini</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-casb-ai-integrations/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB ↗︎](https://www.cloudflare.com/zero-trust/products/casb/) now supports three of the most widely used GenAI platforms — **OpenAI ChatGPT**, **Anthropic Claude**, and **Google Gemini**. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.

![Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2335,height=1776,format=webp/_astro/casb-ai-integrations-preview.B-zsSA1P.png)

#### Key capabilities

- **Agentless connections** — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required
- **Posture management** — detect insecure settings and misconfigurations that could lead to data exposure
- **DLP detection** — identify sensitive data in uploaded chat attachments or files
- **GenAI-specific insights** — surface risks unique to each provider’s capabilities

#### Learn more

- [ChatGPT integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/)
- [Claude integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/)
- [Gemini integration docs ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/)

These integrations are available to all Cloudflare One customers today.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/10/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
