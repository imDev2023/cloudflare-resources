---
title: Cloudflare One Client Changelog
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

Sep 30, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.2033.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

For Zero Trust documentation, see: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/ For Consumer documentation, see: https://developers.cloudflare.com/warp-client/

Sep 29, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.2028.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 29, 2026

[<h2>Cloudflare One Client for macOS (version 2026.8.2028.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- Fixed Extra Logging failing to capture packets across all interfaces.
- Fixed an issue that could prevent remote diagnostics from completing.
- Fixed DNS connectivity checks failing on IPv6-only networks.
- Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
- Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 21, 2026

[<h2>Cloudflare One Client for macOS (version 2026.8.1755.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- Fixed Extra Logging failing to capture packets across all interfaces.
- Fixed an issue that could prevent remote diagnostics from completing.
- Fixed DNS connectivity checks failing on IPv6-only networks.
- Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
- Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 21, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.1755.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
- Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
- Improved client reaction to the current network lowering its MTU.
- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 9, 2026

[<h2>Cloudflare One Client for macOS (version 2026.8.1290.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- Fixed Extra Logging failing to capture packets across all interfaces.
- Fixed an issue that could prevent remote diagnostics from completing.
- Fixed DNS connectivity checks failing on IPv6-only networks.
- Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
- Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

Sep 9, 2026

[<h2>Cloudflare One Client for Windows (version 2026.8.1290.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

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

Aug 10, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.905.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-08-10-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.

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

Jul 7, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.850.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.

Jul 1, 2026

[<h2>Cloudflare One Client for Linux (version 2026.6.836.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.

If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:

```bash
sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo
sudo dnf clean all
sudo dnf install cloudflare-warp
```

Jun 29, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.822.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-06-29-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
- Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the [announcement blog](https://blog.cloudflare.com/mandatory-authentication-mfa/) and [documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/) for details.
- Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See [Hardware-backed registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/) for details.
- Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
- Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
- The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
- Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.
- Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See [Client version assignments](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) for details.

**Additional Changes and improvements**

- Starting with 2026.6.822.0, the client unifies all API requests under the `api.devices.cloudflare.com` SNI, where previously both `zero-trust-client.cloudflareclient.com` and `notifications.cloudflareclient.com` were used. Review [Cloudflare One Client with firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/) to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.
- Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
- Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in Windows Accessibility settings.
- Path MTU Discovery (PMTUD) is now enabled by default.
- The UseWebView2 registry value (HKLM\\SOFTWARE\\Cloudflare\\CloudflareWARP\\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.
- Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.
- Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai\_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.
- Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
- Fixed a high CPU issue when the device wakes from sleep.
- Users can now register with team names in any case format without errors.
- New UI fixes
  - Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
  - Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
  - Added clear error messaging when the Cloudflare certificate needs to be installed.
  - Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
  - New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
  - Added ability to configure proxy mode for consumer users.
  - Added back the option to quit for consumer users.

**Known issues**

- Single sign-on in the embedded WebView2 authentication browser may fail to use the Windows primary account, prompting for an interactive sign-in.
- An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
- In rare cases, a registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- Windows ARM may prompt the user to close running applications while trying to install this version. Simply click "Ok" with the default highlighted option.

Jun 29, 2026

[<h2>Cloudflare One Client for macOS (version 2026.6.822.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-06-29-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
- Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation. See [Hardware-backed registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/) for details.
- Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
- Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
- The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
- Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.
- Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See [Client version assignments](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) for details.

**Additional Changes and improvements**

- Starting with 2026.6.822.0, the client unifies all API requests under the `api.devices.cloudflare.com` SNI, where previously both `zero-trust-client.cloudflareclient.com` and `notifications.cloudflareclient.com` were used. Review [Cloudflare One Client with firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/) to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.
- Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
- Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.
- Path MTU Discovery (PMTUD) is now enabled by default.
- Fixed the in-client captive-portal browser rendering a blank "Success" page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.
- Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai\_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.
- Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
- Users can now register with team names in any case format without errors.
- New UI fixes
  - Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
  - Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
  - Added clear error messaging when the Cloudflare certificate needs to be installed.
  - Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
  - New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
  - Added ability to configure proxy mode for consumer users.
  - Added back the option to quit for consumer users.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
- When deploying with Microsoft Intune, the client may be repeatedly reinstalled because Intune adds the client's embedded framework bundles to its install-detection list, and those frameworks cannot be detected as installed on their own. See [Repeated reinstalls on macOS with Microsoft Intune](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#repeated-reinstalls-on-macos-with-microsoft-intune) for the workaround.

Jun 29, 2026

[<h2>Cloudflare One Client for Linux (version 2026.6.822.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-06-29-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

- The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
- Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See [Hardware-backed registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/) for details.
- Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
- Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
- The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
- Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.

**Additional changes and improvements**

- Starting with 2026.6.822.0, the client unifies all API requests under the `api.devices.cloudflare.com` SNI, where previously both `zero-trust-client.cloudflareclient.com` and `notifications.cloudflareclient.com` were used. Review [Cloudflare One Client with firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/) to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.
- [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) functionality using the Cloudflare One Client is now supported on RHEL 9 and 10.
- Cloudflare Mesh now supports [hostname-based routing](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).
- Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
- Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the system display settings.
- Path MTU Discovery (PMTUD) is now enabled by default.
- Fixed the in-client captive-portal browser rendering a blank "Success" page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.
- Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai\_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.
- Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
- Fixed an issue where some Debian releases experienced inaccurate version reporting for posture checks.
- Users can now register with team names in any case format without errors.
- New UI fixes
  - Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
  - Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
  - Added clear error messaging when the Cloudflare certificate needs to be installed.
  - Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
  - New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
  - Added ability to configure proxy mode for consumer users.
  - Added back the option to quit for consumer users.

For RHEL deployments, this release introduces a dependency on the [Extra Packages for Enterprise Linux](https://docs.fedoraproject.org/en-US/epel/) repository (EPEL). The EPEL repository provides packages that support the captive portal detection’s in-app browser authentication and system tray icon. See [Getting started with EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) for instructions on enabling EPEL.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.

Jun 24, 2026

[<h2>Cloudflare One Client for macOS (version 2026.6.782.1)</h2>](https://developers.cloudflare.com/changelog/post/2026-06-24-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.

**Additional changes and improvements**

This release also introduces multiple fixes and improvements including:

- Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.
- Path MTU Discovery (PMTUD) is now enabled by default.
- Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
- Users can now register with team names in any case format without errors.
- New UI fixes
  - Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
  - Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
  - Added clear error messaging when the Cloudflare certificate needs to be installed.
  - Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
  - New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
  - Added ability to configure proxy mode for consumer users.
  - Added back the option to quit for consumer users.

**Known issues**

- Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-one-client/#page","headline":"Cloudflare One Client Changelog","url":"https://developers.cloudflare.com/changelog/product/cloudflare-one-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
