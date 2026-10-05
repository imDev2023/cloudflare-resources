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

Jun 5, 2025

[<h2>Cloudflare One Analytics Dashboards and Exportable Access Report</h2>](https://developers.cloudflare.com/changelog/post/dashboards-access-report/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.

!\[Cloudflare One Analytics Dashboards](\~/assets/images/changelog/cloudflare-one/Analytics Dashboards.png)

Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A **preview** of the report is shown below, with more to be found in the report:

![Cloudflare One Analytics Dashboards](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=950,format=webp/_astro/access-report.C744W7JR.png)

Both features are accessible in the Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/), empowering organizations with better visibility and control.

Jun 4, 2025

[<h2>New Account-Level Load Balancing UI and Private Load Balancers</h2>](https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

We've made two large changes to load balancing:

- Redesigned the user interface, now centralized at the **account level**.
- Introduced [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.

This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.

![Load Balancing UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=822,format=webp/_astro/account-load-balancing-ui.CoCi7gPb.png)

**Key Enhancements:**

- **Account-Level UI Consolidation:**
  - **Unified Management:** Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.
  - **Improved Efficiency:** This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.
- **Private Network Load Balancing:**
  - **Secure Internal Application Access:** Create [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.
  - **WARP & Magic WAN Integration:** Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.
  - **Enhanced Security for Internal Resources:** Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.

![Private Load Balancers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=744,format=webp/_astro/private-load-balancer.yti20m_p.png)

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

May 27, 2025

[<h2>Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</h2>](https://developers.cloudflare.com/changelog/post/2025-05-27-Protocol-Detection-availability/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.

With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.

This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).

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

May 15, 2025

[<h2>Open email attachments with Browser Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open email attachments to view and investigate them.

What this means is that messages now have a **Attachments** section. Here, you can view processed attachments and their classifications (for example, *Malicious*, *Suspicious*, *Encrypted*). Next to each attachment, a **Browser Isolation** icon allows your team to safely open the file in a **clientless, isolated browser** with no risk to the analyst or your environment.

![Attachment-RBI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=517,height=155,format=webp/_astro/Attachment-RBI.U9Dp8dJO.png)

To use this feature, you must:

- Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
- Have **Browser Isolation (BISO)** seats assigned.

For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

May 14, 2025

[<h2>Domain Categories improvements</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-domain-category-improvements/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

**New categories added**

| Parent ID | Parent Name | Category ID | Category Name |
| --- | --- | --- | --- |
| 1 | Ads | 66 | Advertisements |
| 3 | Business & Economy | 185 | Personal Finance |
| 3 | Business & Economy | 186 | Brokerage & Investing |
| 21 | Security Threats | 187 | Compromised Domain |
| 21 | Security Threats | 188 | Potentially Unwanted Software |
| 6 | Education | 189 | Reference |
| 9 | Government & Politics | 190 | Charity and Non-profit |

**Changes to existing categories**

| Original Name | New Name |
| --- | --- |
| Religion | Religion & Spirituality |
| Government | Government/Legal |
| Redirect | URL Alias/Redirect |

Refer to [Gateway domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/) to learn more.

May 13, 2025

[<h2>SAML HTTP-POST bindings support for RBI</h2>](https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused `405` errors during login and improves compatibility with multi-factor authentication (MFA) flows.

With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to [set up Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/).

May 13, 2025

[<h2>New Applications Added for DNS Filtering</h2>](https://developers.cloudflare.com/changelog/post/2025-05-13-new-applications-added/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now create DNS policies to manage outbound traffic for an expanded list of applications. This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.

With this update, you can:

- Create DNS policies for a wider range of applications
- Manage outbound traffic more effectively
- Improve your organization's security and compliance posture

For more information on creating DNS policies, see our [DNS policy documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/).

May 12, 2025

[<h2>Case Sensitive Custom Word Lists</h2>](https://developers.cloudflare.com/changelog/post/2025-05-12-case-sensitive-cwl/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now configure [custom word lists](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets) to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.

![dlp](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1289,height=910,format=webp/_astro/case-sesitive-cwl.MPuOc_3r.png)

May 8, 2025

[<h2>Open email links with Browser Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open links in emails to view and investigate them.

![Open links with Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=558,height=204,format=webp/_astro/investigate-links.pYbpGkt5.jpg)

From **Investigation**, go to **View details**, and look for the **Links identified** section. Next to each link, the Cloudflare dashboard will display an **Open in Browser Isolation** icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links) to learn more about this feature.

To use this feature, you must:

- Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
- Have **Browser Isolation (RBI)** seats assigned.

For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

May 7, 2025

[<h2>Send forensic copies to storage without DLP profiles</h2>](https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now [send DLP forensic copies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination) to third-party storage for any HTTP policy with an `Allow` or `Block` action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.

By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1324,height=636,format=webp/_astro/forensic-copies-for-all.fxeFrCY4.png)

May 6, 2025

[<h2>UDP and ICMP Monitor Support for Private Load Balancing Endpoints</h2>](https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports **UDP (Layer 4)** and **ICMP (Layer 3)** health monitors for **private endpoints**. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.

#### What you can do:

- Set up **ICMP ping monitors** to check if your private endpoints are reachable.
- Use **UDP monitors** for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.
- Gain better visibility and uptime guarantees for services running behind **Private Network Load Balancing**, without requiring public IP addresses.

This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with [**Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [**WARP**](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), and [**Magic WAN**](https://developers.cloudflare.com/cloudflare-wan/) to create a secure and observable private network.

Learn more about [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) or view the full list of [supported health monitor protocols](https://developers.cloudflare.com/load-balancing/monitors/#supported-protocols).

May 1, 2025

[<h2>Browser Isolation Overview page for Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/2025-05-01-browser-isolation-overview-page/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

A new **Browser Isolation Overview** page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) deployments, providing:

- **Streamlined Onboarding:** Easily set up and manage isolation policies from one location.
- **Quick Testing:** Validate [clientless web application isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) with ease.
- **Simplified Configuration:** Configure [isolated access applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/) and policies efficiently.
- **Centralized Monitoring:** Track aggregate usage and blocked actions.

This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.

![Browser Isolation Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1717,height=1286,format=webp/_astro/browser-isolation-overview.Ljd5ax_O.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and find Browser Isolation in the side navigation bar.

Apr 30, 2025

[<h2>Dark Mode for Zero Trust Dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-04-30-zero-trust-dashboard-dark-mode/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The [Cloudflare Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) now supports Cloudflare's native dark mode for all accounts and plan types.

Zero Trust Dashboard will automatically accept your user-level preferences for system settings, so if your Dashboard appearance is set to 'system' or 'dark', the Zero Trust dashboard will enter dark mode whenever the rest of your Cloudflare account does.

![Zero Trust dashboard supports dark mode](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3456,height=1596,format=webp/_astro/dark-mode.DfLeS20d.png)

To update your view preference in the Zero Trust dashboard:

1. Log into the [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/).
2. Select your user icon.
3. Select **Dark Mode**.

To update your view preference in the Core dashboard:

1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
2. Go to **My Profile**
3. For **Appearance**, choose **Dark**.

Apr 30, 2025

[<h2>Cloudflare One Appliance supports multiple DNS server IPs</h2>](https://developers.cloudflare.com/changelog/post/2025-04-30-appliance-multiple-dns-servers/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.

Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.

For configuration details, refer to [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/).

Apr 28, 2025

[<h2>FQDN Filtering For Gateway Egress Policies</h2>](https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.

- Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.
- During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
  - For WARP client support, additional configuration is required. For more information, refer to the [WARP client configuration documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#limitations).

![Egress by FQDN and Hostname](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=841,height=1045,format=webp/_astro/Gateway-Egress-FQDN-Policy-preview.Civon5p8.png)

This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.

Apr 21, 2025

[<h2>Access bulk policy tester</h2>](https://developers.cloudflare.com/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

The [Access bulk policy tester](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application) is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).

![Example policy tester](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1531,height=693,format=webp/_astro/example-policy-tester.DCY8hQvx.png)

Apr 14, 2025

[<h2>New predefined detection entry for ICD-11</h2>](https://developers.cloudflare.com/changelog/post/2025-04-14-icd11-support/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You now have access to the World Health Organization (WHO) 2025 edition of the [International Classification of Diseases 11th Revision (ICD-11) ↗︎](https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29) as a predefined detection entry. The new dataset can be found in the [Health Information](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information) predefined profile.

ICD-10 dataset remains available for use.

Apr 11, 2025

[<h2>HTTP redirect and custom block page redirect</h2>](https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now use more flexible redirect capabilities in Cloudflare One with Gateway.

- A new **Redirect** action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.
- For **Block** actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.

Learn more in our documentation for [HTTP Redirect](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#redirect) and [Block page redirect](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page).

Apr 9, 2025

[<h2>Cloudflare Zero Trust SCIM User and Group Provisioning Logs</h2>](https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Cloudflare Zero Trust SCIM provisioning](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim) now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The [SCIM logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/) support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.

SCIM logs can be found on the Zero Trust Dashboard under **Logs** -> **SCIM provisioning**.

![Example SCIM Logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2318,height=1060,format=webp/_astro/example-scim-log.Bv5Zqckh.png)

Apr 1, 2025

[<h2>CASB and Email security</h2>](https://developers.cloudflare.com/changelog/post/2025-04-01-casb-email-security/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

With Email security, you get two free CASB integrations.

Use one SaaS integration for Email security to sync with your directory of users, take actions on delivered emails, automatically provide EMLs for reclassification requests for clean emails, discover CASB findings and more.

With the other integration, you can have a separate SaaS integration for CASB findings for another SaaS provider.

Refer to [Add an integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) to learn more about this feature.

![CASB-EmailSecurity](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=727,height=502,format=webp/_astro/CASB-EmailSecurity.B1wd9be2.png)

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Mar 21, 2025

[<h2>Secure DNS Locations Management User Role</h2>](https://developers.cloudflare.com/changelog/post/2025-03-21-pdns-user-locations-role/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We're excited to introduce the [**Cloudflare Zero Trust Secure DNS Locations Write role**](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations), designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.

Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.

**Secure DNS Location Requirements:**

- Mandate usage of [Bring your own DNS resolver IP addresses ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip) if available on the account.
- Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.

You can assign the new role via Cloudflare Dashboard (`Manage Accounts > Members`) or via API. For more information, refer to the [Secure DNS Locations documentation ↗︎](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations).

Mar 17, 2025

[<h2>Cloudflare One Agent for Android (version 2.4)</h2>](https://developers.cloudflare.com/changelog/post/2025-03-17-warp-ga-android/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Android Cloudflare One Agent is now available in the [Google Play Store ↗︎](https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent). This release includes a new feature allowing [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url) during enrollment, as well as fixes and minor improvements.

**Changes and improvements**

- Improved in-app error messages.
- Improved mobile client login with support for [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url).
- Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
