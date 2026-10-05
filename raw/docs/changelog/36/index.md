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

Oct 21, 2025

[<h2>New Robots.txt tab for tracking crawler compliance</h2>](https://developers.cloudflare.com/changelog/post/2025-10-21-track-robots-txt/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control now includes a **Robots.txt** tab that provides insights into how AI crawlers interact with your `robots.txt` files.

#### What's new

The Robots.txt tab allows you to:

- Monitor the health status of `robots.txt` files across all your hostnames, including HTTP status codes, and identify hostnames that need a `robots.txt` file.
- Track the total number of requests to each `robots.txt` file, with breakdowns of successful versus unsuccessful requests.
- Check whether your `robots.txt` files contain [Content Signals ↗︎](https://contentsignals.org/) directives for AI training, search, and AI input.
- Identify crawlers that request paths explicitly disallowed by your `robots.txt` directives, including the crawler name, operator, violated path, specific directive, and violation count.
- Filter `robots.txt` request data by crawler, operator, category, and custom time ranges.

#### Take action

When you identify non-compliant crawlers, you can:

- Block the crawler in the [Crawlers tab](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- Create custom [WAF rules](https://developers.cloudflare.com/waf/) for path-specific security
- Use [Redirect Rules](https://developers.cloudflare.com/rules/url-forwarding/) to guide crawlers to appropriate areas of your site

To get started, go to **AI Crawl Control** > **Robots.txt** in the Cloudflare dashboard. Learn more in the [Track robots.txt documentation](https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/).

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

Oct 20, 2025

[<h2>WAF Release - 2025-10-20</h2>](https://developers.cloudflare.com/changelog/post/2025-10-20-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.

**Key Findings**

New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.

**Impact**

- Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2b4101ab | 100598A | Remote Code Execution - Common Bash Bypass - Beta | Log | Block | This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: ...50cec478) |
| Cloudflare Managed Ruleset | ...a1118614 | 100916A | Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...c22b51d3 | N/A | HTTP Truncated | N/A | Disabled | This is a New Detection |

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

Oct 17, 2025

[<h2>New Application Security reports (Closed Beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-17-app-sec-reports/)

[Security Center](https://developers.cloudflare.com/security-center/)

Cloudflare's new **Application Security report**, currently in Closed Beta, is now available in the dashboard.

[Go to **Security reports** ↗](https://dash.cloudflare.com/?to=/:account/security-center/reports)

The reports are generated monthly and provide cyber security insights trends for all of the Enterprise zones in your Cloudflare account.

The reports also include an industry benchmark, comparing your cyber security landscape to peers in your industry.

![Application Security report mock data](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2379,height=3367,format=webp/_astro/2025-10-17-application-security-report-mock-data.Cz0-WuoX.png)

Learn more about the reports by referring to the [Security Reports documentation](https://developers.cloudflare.com/analytics/account-and-zone-analytics/app-security-reports/).

Use the feedback survey link at the top of the page to help us improve the reports.

![Application Security report survey](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1126,height=448,format=webp/_astro/2025-10-17-report-feedback-survey.DPmUlWh2.png)

Oct 17, 2025

[<h2>New detections released for WAF managed rulesets</h2>](https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.

**Key Findings**

New detections added for multiple exploit categories:

SSRF (Server-Side Request Forgery) — new rules targeting both local and cloud metadata abuse patterns (Beta).

SQL Injection (SQLi) — rules for common patterns, sleep/time-based injections, and string/wait function exploitation across headers and URIs.

SSTI (Server-Side Template Injection) — arithmetic-based probe detections introduced across URI, header, and body fields.

Reverse Shell and XXE payloads — enhanced heuristics for command execution and XML external entity misuse.

Prototype Pollution — new Beta rule identifying common JSON payload structures used in object prototype poisoning.

PHP Wrapper Injection and HTTP Parameter Pollution detections — to catch path traversal and multi-parameter manipulation attempts.

Anomaly Header Checks — detecting CRLF injection attempts in header names.

**Impact**

These updates help detect multi-vector payloads that blend SSRF + RCE or SQLi + SSTI attacks, especially in cloud-hosted applications with exposed metadata endpoints or unsafe template rendering.

Prototype Pollution and HTTP parameter pollution rules address emerging JavaScript supply-chain exploitation patterns increasingly seen in real-world incidents.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...589f2a1d | N/A | Anomaly:Header - name - CR, LF | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...132fab7e | N/A | Generic Rules - Reverse Shell - Body | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1a027008 | N/A | Generic Rules - Reverse Shell - Header | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...958d0486 | N/A | Generic Rules - Reverse Shell - URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...8e0cf7ad | N/A | Generic Rules - XXE - Body | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...bf8aab5e | N/A | Generic Rules - SQLi - Common Patterns - Header URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2e466337 | N/A | Generic Rules - SQLi - Sleep Function - Header URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...b686ab47 | N/A | Generic Rules - SQLi - String Function - Header URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...b0633709 | N/A | Generic Rules - SQLi - WaitFor Function - Header URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...01a076eb | N/A | SSRF - Local - Beta | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...743a63ec | N/A | SSRF - Local - 2 - Beta | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c2e84e2d | N/A | SSRF - Cloud - Beta | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...ab8af26f | N/A | SSRF - Cloud - 2 - Beta | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...e6e8dc5b | N/A | SSTI - Arithmetic Probe - URI | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...2550d794 | N/A | SSTI - Arithmetic Probe - Header | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...659d12a6 | N/A | SSTI - Arithmetic Probe - Body | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...1a3e521e | N/A | PHP Wrapper Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...8f76bd74 | N/A | PHP Wrapper Injection | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...091e296d | N/A | HTTP parameter pollution | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...e34214ef | N/A | Prototype Pollution - Common Payloads - Beta | N/A | Disabled | This is a New Detection |

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

[<h2>View and edit Durable Object data in UI with Data Studio (Beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-10-16-durable-objects-data-studio/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

![Screenshot of Durable Objects Data Studio](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1699,height=407,format=webp/_astro/do-data-studio.BfCcgtkq.png)

You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using [SQLite storage](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class) can use Data Studio.

[Go to **Durable Objects** ↗](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.

To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the `Workers Platform Admin` role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.

To learn more, visit the Data Studio [documentation](https://developers.cloudflare.com/durable-objects/observability/data-studio/). If you have feedback or suggestions for the new Data Studio, please share your experience on [Discord ↗︎](https://discord.com/channels/595317990191398933/773219443911819284)

Oct 16, 2025

[<h2>Increased HTTP header size limit to 128 KB</h2>](https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

#### CDN now supports 128 KB request and response headers 🚀

We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to **128 KB** for both **request and response headers**.

Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with `HTTP 413` (Request Header Fields Too Large) errors.

---

#### What's new?

- **Support for large headers:** You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.
- **Reduces `413` and `520` HTTP errors:** This change drastically reduces the likelihood of customers encountering `HTTP 413` errors from large request headers or `HTTP 520` errors caused by oversized response headers, improving the overall reliability of your web applications.
- **Enhanced functionality:** This is especially beneficial for applications that rely on:
  - A large number of cookies.
  - Large Content-Security-Policy (CSP) response headers.
  - Advanced use cases with Cloudflare Workers that generate large response headers.

This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.

---

To learn more and get started, refer to the [Cloudflare Fundamentals documentation](https://developers.cloudflare.com/fundamentals/reference/connection-limits/#request-limits).

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

Oct 14, 2025

[<h2>Enhanced AI Crawl Control metrics with new drilldowns and filters</h2>](https://developers.cloudflare.com/changelog/post/2025-10-14-enhanced-metrics-drilldowns/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.

#### What's new

#### Track crawler requests over time

Visualize crawler activity patterns over time, and group data by different dimensions:

- **By Crawler** — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)
- **By Category** — Analyze crawler purpose or type
- **By Operator** — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site
- **By Host** — Break down activity across multiple subdomains
- **By Status Code** — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)

![AI Crawl Control requests over time chart with grouping tabs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1293,height=666,format=webp/_astro/ai-crawl-control-requests-over-time.BtRyz0OT.png "Interactive chart showing crawler requests over time with filterable dimensions")

*Interactive chart showing crawler requests over time with filterable dimensions*

#### Analyze referrer data (Paid plans)

Identify traffic sources with referrer analytics:

- View top referrers driving traffic to your site
- Understand discovery patterns and content popularity from AI operators

![AI Crawl Control top referrers breakdown](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1291,height=656,format=webp/_astro/ai-crawl-control-top-referrers.CEUAwpd8.png "Bar chart showing top referrers and their respective traffic volumes")

*Bar chart showing top referrers and their respective traffic volumes*

#### Export data

Download your filtered view as a CSV:

- Includes all applied filters and groupings
- Useful for custom reporting and deeper analysis

#### Get started

1. Log in to the Cloudflare dashboard, and select your account and domain.
2. Go to **AI Crawl Control** > **Metrics**.
3. Use the grouping tabs to explore different views of your data.
4. Apply filters to focus on specific crawlers, time ranges, or response codes.
5. Select **Download CSV** to export your filtered data for further analysis.

Learn more about [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control).

Oct 14, 2025

[<h2>Single sign-on now manageable in the user experience</h2>](https://developers.cloudflare.com/changelog/post/2025-10-14-sso-self-service-ux/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

![Screenshot of new user experience for managing SSO](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1378,height=877,format=webp/_astro/2025-10-14-sso-configuration-ux.DLkIKSax.png)

During Birthday Week, we announced that [single sign-on (SSO) is available for free ↗︎](https://blog.cloudflare.com/enterprise-grade-features-for-all/) to everyone who signs in with a custom email domain and maintains a compatible [identity provider ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/). SSO minimizes user friction around login and provides the strongest security posture available. At the time, this could only be configured using the API.

Today, we are launching a new user experience which allows users to manage their SSO configuration from within the Cloudflare dashboard. You can access this by going to **Manage account** > **Members** > **Settings**.

#### For more information

- [Cloudflare dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)

Oct 13, 2025

[<h2>WAF Release - 2025-10-13</h2>](https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.

**Key Findings**

New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.

**Impact**

- CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson `ObjectMapper` abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...c04bab5f | 100892 | JinJava - SSTI - CVE:CVE-2025-59340 | Log | Block | This is a New Detection |

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

Oct 10, 2025

[<h2>Worker startup time limit increased to 1 second</h2>](https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/)

[Workers](https://developers.cloudflare.com/workers/)

You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.

This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.

For more information, see the documentation on [Workers startup limits](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).

Oct 9, 2025

[<h2>Expanded CT log activity insights on Cloudflare Radar</h2>](https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:

- **Log growth rate**: The average throughput of the CT log over the past 7 days, measured in certificates per hour.
- **Included certificate count**: The total number of certificates already included in this CT log.
- **Eligible-for-inclusion certificate count**: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.
- **Last update**: The timestamp of the most recent update to the CT log.

These new statistics have been added to the response of the [Get Certificate Log Details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get/) API endpoint, and are displayed on the [CT log information page ↗︎](https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity).

![Screenshot of the CT log activity card on the CT log information page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1598,height=441,format=webp/_astro/ct-log-activity.GHD-K7Mk.png)

Oct 9, 2025

[<h2>You can now deploy full-stack apps on Workers using Terraform</h2>](https://developers.cloudflare.com/changelog/post/2025-10-09-assets-terraform/)

[Workers](https://developers.cloudflare.com/workers/)

You can now upload Workers with [static assets](https://developers.cloudflare.com/workers/static-assets/) (like HTML, CSS, JavaScript, images) with the [Cloudflare Terraform provider v5.11.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs), making it even easier to deploy and manage full-stack apps with IaC.

**Previously**, you couldn't use Terraform to upload static assets without writing custom scripts to handle generating an [asset manifest](https://developers.cloudflare.com/workers/static-assets/direct-upload/#upload-manifest), calling the [Cloudflare API to upload assets in chunks](https://developers.cloudflare.com/workers/static-assets/direct-upload/#upload-static-assets), and handling change detection.

**Now**, you simply define the directory where your assets are built, and we handle the rest. Check out the [examples](https://developers.cloudflare.com/changelog/#examples) for what this looks like in Terraform configuration.

You can get started today with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs), using either the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), or the beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).

#### Examples

#### With `cloudflare_workers_script`

Here's how you can use the existing [`cloudflare_workers_script` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_script) resource to upload your Worker code and assets in one shot.

```hcl
resource "cloudflare_workers_script" "my_app" {
  account_id  = var.account_id
  script_name = "my-app"

  content_file   = "./dist/worker/index.js"
  content_sha256 = filesha256("./dist/worker/index.js")
  main_module    = "index.js"

  # Just point to your assets directory - that's it!
  assets = {
    directory = "./dist/static"
  }
}
```

#### With `cloudflare_worker`, `cloudflare_worker_version`, and `cloudflare_workers_deployment`

And here's an example using the beta [`cloudflare_worker_version` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources:

```hcl
# This tracks the existence of your Worker, so that you
# can upload code and assets separately from tracking Worker state.

resource "cloudflare_worker" "my_app" {
  account_id = var.account_id
  name       = "my-app"
}

resource "cloudflare_worker_version" "my_app_version" {
  account_id = var.account_id
  worker_id  = cloudflare_worker.my_app.id

  # Just point to your assets directory - that's it!
  assets = {
    directory = "./dist/static"
  }

  modules = [{
    name         = "index.js"
    content_file = "./dist/worker/index.js"
    content_type = "application/javascript+module"
  }]
}

resource "cloudflare_workers_deployment" "my_app_deployment" {
  account_id  = var.account_id
  script_name = cloudflare_worker.my_app.name

  strategy = "percentage"
  versions = [{
    version_id = cloudflare_worker_version.my_app_version.id
    percentage = 100
  }]
}
```

#### What's changed

Under the hood, the Cloudflare Terraform provider now handles the same logic that Wrangler uses for static asset uploads. This includes scanning your assets directory, computing hashes for each file, generating a manifest with file metadata, and calling the Cloudflare API to upload any missing files in chunks. We support large directories with parallel uploads and chunking, and when the asset manifest hash changes, we detect what's changed and trigger an upload for *only* those changed files.

#### Try it out

- Get started with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs)
- You can use either the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) to upload your Worker code and assets in one resource.
- Or you can use the new beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version) (along with the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment)) resources to more granularly control the lifecycle of each Worker resource.

Oct 9, 2025

[<h2>You can now deploy and manage Workflows in Terraform</h2>](https://developers.cloudflare.com/changelog/post/2025-10-09-workflows-terraform/)

[Workers](https://developers.cloudflare.com/workers/)

You can now create and manage [Workflows](https://developers.cloudflare.com/workflows/) using Terraform, now supported in the [Cloudflare Terraform provider v5.11.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow). Workflows allow you to build durable, multi-step applications -- without needing to worry about retrying failed tasks or managing infrastructure.

Now, you can deploy and manage Workflows through Terraform using the new [`cloudflare_workflow` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow):

```hcl
resource "cloudflare_workflow" "my_workflow" {
  account_id    = var.account_id
  workflow_name = "my-workflow"
  class_name    = "MyWorkflow"
  script_name   = "my-worker"
}
```

#### Examples

Here are full examples of how to configure `cloudflare_workflow` in Terraform, using the existing [`cloudflare_workers_script` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), and the beta [`cloudflare_worker_version` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).

#### With `cloudflare_workflow` and `cloudflare_workers_script`

```hcl
resource "cloudflare_workers_script" "workflow_worker" {
  account_id  = var.cloudflare_account_id
  script_name = "my-workflow-worker"

  content_file   = "${path.module}/../dist/worker/index.js"
  content_sha256 = filesha256("${path.module}/../dist/worker/index.js")
  main_module    = "index.js"
}

resource "cloudflare_workflow" "workflow" {
  account_id    = var.cloudflare_account_id
  workflow_name = "my-workflow"
  class_name    = "MyWorkflow"
  script_name   = cloudflare_workers_script.workflow_worker.script_name
}
```

#### With `cloudflare_workflow`, and the new beta resources

You can more granularly control the lifecycle of each Worker resource using the beta [`cloudflare_worker_version` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources.

```hcl
resource "cloudflare_worker" "workflow_worker" {
  account_id = var.cloudflare_account_id
  name       = "my-workflow-worker"
}

resource "cloudflare_worker_version" "workflow_worker_version" {
  account_id = var.cloudflare_account_id
  worker_id  = cloudflare_worker.workflow_worker.id

  main_module         = "index.js"

  modules = [{
    name         = "index.js"
    content_file = "${path.module}/../dist/worker/index.js"
    content_type = "application/javascript+module"
  }]
}

resource "cloudflare_workers_deployment" "workflow_deployment" {
  account_id  = var.cloudflare_account_id
  script_name = cloudflare_worker.workflow_worker.name

  strategy = "percentage"
  versions = [{
    version_id = cloudflare_worker_version.workflow_worker_version.id
    percentage = 100
  }]
}

resource "cloudflare_workflow" "my_workflow" {
  account_id    = var.cloudflare_account_id
  workflow_name = "my-workflow"
  class_name    = "MyWorkflow"
  script_name   = cloudflare_worker.workflow_worker.name
}
```

#### Try it out

- Get started with [the Cloudflare Terraform provider (v5.11.0) ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs) and the new [`cloudflare_workflow` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow).

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

Oct 7, 2025

[<h2>Automated reminders for backup codes</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-recovery-codes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to **Profile** > **Security & Authentication** > **Backup codes**.

#### Sign-in security best practices

Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.

- Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.
- Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked
- Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.
- If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.
- If you use a custom email domain to sign in, [configure SSO ↗︎](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/).
- If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.
- If you manage a Cloudflare account for work:
  - Have at least two administrators in case one of them unexpectedly leaves your company
  - Use SCIM to automate permissions management for members in your Cloudflare account

Oct 7, 2025

[<h2>WAF Release - 2025-10-07 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-10-07-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device. The initial two rules were made available on September 28, with a third rule added today, October 7, for more robust protection.

- Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.

**Impact**

Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection. Administrators are strongly advised to apply vendor updates immediately.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...3a4d1bd6 | 100788B | Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363 | N/A | Block | This is a New Detection |

Oct 7, 2025

[<h2>New Overview Page for Cloudflare Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-10-06-new-worker-overview-page/)

[Workers](https://developers.cloudflare.com/workers/)

![Screenshot of the Workers overview page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1016,format=webp/_astro/workers-overview.BM_exs4R.png)

Each of your Workers now has a new overview page in the Cloudflare dashboard.

The goal is to make it easier to understand your Worker without digging through multiple tabs. Think of it as a new home base, a place to get a high-level overview on what's going on.

It's the first place you land when you open a Worker in the dashboard, and it gives you an immediate view of what’s going on. You can see requests, errors, and CPU time at a glance. You can view and add bindings, and see recent versions of your app, including who published them.

Navigation is also simpler, with visually distinct tabs at the top of the page. At the bottom right you'll find guided steps for what to do next that are based on the state of your Worker, such as adding a [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) or connecting a custom domain.

We plan to add more here over time. Better insights, more controls, and ways to manage your Worker from one page.

If you have feedback or suggestions for the new Overview page or your Cloudflare Workers experience in general, we'd love to hear from you. Join the Cloudflare developer community on [Discord ↗︎](https://discord.com/channels/595317990191398933/1064502845061210152).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/36/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/36/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
