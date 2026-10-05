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

Aug 26, 2025

[<h2>Manage and restrict access to internal MCP servers with Cloudflare Access</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

[Self-hosted applications](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/linked-apps/) in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.

For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the [blog post ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) on the Cloudflare Blog.

Aug 26, 2025

[<h2>MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

![MCP server portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1557,height=420,format=webp/_astro/mcp-server-portal.BOKqTCoI.png)

An [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:

- **Streamlined access to multiple MCP servers**: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.
- **Customized tools per portal**: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.
- **Observability**: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.

This is available in an open beta for all customers across all plans! For more information check out our [blog ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) for this release.

Aug 25, 2025

[<h2>New DLP topic based detection entries for AI prompt protection</h2>](https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.

1. **Prompt Detection for AI Applications**

DLP can now natively detect and inspect user prompts submitted to popular AI applications, including **Google Gemini**, **ChatGPT**, **Claude**, and **Perplexity**.

2. **Prompt Analysis and Topic Classification**

Our DLP engine performs deep analysis on each prompt, applying [topic classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics). These topics are grouped into two evaluation categories:

- **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.
- **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.

To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=439,format=webp/_astro/ai-prompt-detection-entry.4QmdkAuv.png)

3. **Granular Guardrails**

   You can now build guardrails using Gateway HTTP policies with [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls). Apply a DLP profile containing an [AI prompt topic detection](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) to individual AI applications (for example, `ChatGPT`) and specific user actions (for example, `SendPrompt`) to block sensitive prompts.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=731,height=511,format=webp/_astro/ai-prompt-policy.CF3H2rbK.png)
4. **Full Prompt Logging**

   To aid in incident investigation, an optional setting in your Gateway policy allows you to [capture prompt logs](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content) to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by `conversation_id`, allowing you to reconstruct the full context of an interaction that led to a policy violation.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=444,format=webp/_astro/ai-prompt-log.ywQDc5qN.png)

AI prompt protection is now available in open beta. To learn more about it, read the [blog ↗︎](https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging) or refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

Aug 21, 2025

[<h2>Gateway BYOIP Dedicated Egress IPs now available.</h2>](https://developers.cloudflare.com/changelog/post/2025-08-21-byoip-dedicated-egress-ip/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.

Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.

Get started by following the [BYOIP onboarding process](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip). Once your IPs are onboarded, go to **Gateway** > **Egress policies** and select or create an egress policy. In **Select an egress IP**, choose *Use dedicated egress IPs (Cloudflare or BYOIP)*, then select your BYOIP address from the dropdown menu.

![Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=933,height=459,format=webp/_astro/Gateway-byoip-dedicated-egress-ips.D0pzLAbV.png)

For more information, refer to [BYOIP for dedicated egress IPs](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip).

Aug 15, 2025

[<h2>SFTP support for SSH with Cloudflare Access for Infrastructure</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-sftp/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[SSH with Cloudflare Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.

Aug 15, 2025

[<h2>Steer Traffic by AS Number in Load Balancing Custom Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.

This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.

![Create a Load Balancing Custom Rule using AS Num](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2554,height=1472,format=webp/_astro/asnum-custom-rule.CtcHu_zj.png)

To get started, create a [Custom Rule ↗︎](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) in your Load Balancer and select **AS Num** from the **Field** dropdown.

Aug 14, 2025

[<h2>Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access logs now support the [Customer Metadata Boundary (CMB)](https://developers.cloudflare.com/data-localization/metadata-boundary/). If you have configured the CMB for your account, all Access logging will respect that configuration.

Note

For EU CMB customers, the logs will not be stored by Access and will appear as empty in the dashboard. EU CMB customers should utilize [Logpush](https://developers.cloudflare.com/logs/logpush/) to retain their Access logging, if desired.

Aug 7, 2025

[<h2>Expanded Email Link Isolation</h2>](https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.

For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.

![Expanded Email Link Isolation Configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=497,format=webp/_astro/expanded-link-actions.DziIg6E8.jpg)

To isolate all links within a message based on the disposition, select **Settings** > **Link Actions** > **View** and select **Configure**. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on [Configure link actions ↗︎](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/).

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Aug 6, 2025

[<h2>Improvements to Monitoring Using Zone Settings</h2>](https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.

All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.

#### What you can expect:

- More reliable application of zone settings to monitoring requests, including
  - Authenticated Origin Pulls
  - Aegis Egress IP Pools
  - Argo Smart Routing
  - HTTP/2 to Origin
- Improved support and bug fixes for retries, redirects, and proxied origin resolution
- Improved performance and reliability of monitoring requests within the Cloudflare network
- Unrelated CDN or WAF configuration changes should have no risk of impact to pool health

Jul 31, 2025

[<h2>Terraform V5 support for tunnels and routes</h2>](https://developers.cloudflare.com/changelog/post/2025-07-31-terraform-v5-tunnels-routes/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.

For more information, refer to the [Cloudflare Terraform provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

Jul 30, 2025

[<h2>Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</h2>](https://developers.cloudflare.com/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/)

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU ([Customer Metadata Boundary - Europe](https://developers.cloudflare.com/data-localization/metadata-boundary/)) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.

This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.

Specifically, these two GraphQL endpoints are now compatible with CMB EU:

- `magicTransitTunnelHealthChecksAdaptiveGroups`
- `magicTransitTunnelTrafficAdaptiveGroups`

Jul 28, 2025

[<h2>Scam domain category introduced under Security Threats</h2>](https://developers.cloudflare.com/changelog/post/2025-07-28-Spam-domain-category-introduced/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

We have introduced a new Security Threat category called **Scam**. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.

**New category added**

| Parent ID | Parent Name | Category ID | Category Name |
| --- | --- | --- | --- |
| 21 | Security Threats | 191 | Scam |

Refer to [Gateway domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/) to learn more.

Jul 24, 2025

[<h2>Gateway HTTP Filtering on all ports available in open BETA</h2>](https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) can now apply [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) to all proxied HTTP requests, not just traffic on standard HTTP (`80`) and HTTPS (`443`) ports. This means all requests can now be filtered by [A/V scanning](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/), [file sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/), [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/#data-in-transit), and more.

You can turn this [setting](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports) on by going to **Settings** > **Network** > **Firewall** and choosing *Inspect on all ports*.

![HTTP Inspection on all ports setting](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=535,format=webp/_astro/Gateway-Inspection-all-ports.CCmwX6D0.png)

To learn more, refer to [Inspect on all ports (Beta)](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports).

Jul 22, 2025

[<h2>Google Bard Application replaced by Gemini</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The **Google Bard** application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the **Gemini** application (ID: 1340). Any existing Gateway policies that reference the old Google Bard application will no longer function. To ensure your policies continue to work as intended, you should update them to use the new Gemini application. We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies. For more information about application policies, please see the [Cloudflare Gateway documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

Jul 21, 2025

[<h2>Virtual Cloudflare One Appliance with KVM support (open beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.

Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.

For setup instructions, refer to [Configure a virtual Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Jul 17, 2025

[<h2>New detection entry type: Document Matching for DLP</h2>](https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now create [document-based](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries) detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=839,format=webp/_astro/document-match.CcN8pGgR.png)

**Key features and benefits:**

- **Upload documents, forms, or templates:** Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.
- **Granular control with similarity percentage:** Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.
- **Comprehensive coverage:** Apply these document-based detection entries in:
  - **Gateway policies:** To inspect network traffic for sensitive documents as they are uploaded or shared.
  - **CASB (Cloud Access Security Broker):** To scan files stored in cloud applications for sensitive documents at rest.
- **Identify sensitive data:** This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.

Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.

Jul 15, 2025

[<h2>Faster, more reliable UDP traffic for Cloudflare Tunnel</h2>](https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Your real-time applications running over [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) are now faster and more reliable. We've completely re-architected the way `cloudflared` proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.

This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.

**What’s new:**

- **Faster UDP performance**: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.
- **Greater reliability for mixed traffic**: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.

Learn more about running [TCP or UDP applications](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-applications) and [private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/) through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

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

Jul 1, 2025

[<h2>Access RDP securely from your browser — now in open beta</h2>](https://developers.cloudflare.com/changelog/post/2025-07-01-browser-based-rdp-open-beta/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) is now available in open beta for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.

With browser-based RDP, you can:

- **Control how users authenticate to internal RDP resources** with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.
- **Record who is accessing which servers and when** to support regulatory compliance requirements and to gain greater visibility in the event of a security event.
- **Eliminate the need to install and manage software on user devices**. You will only need a web browser.
- **Reduce your attack surface** by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.

![Example of a browsed-based RDP Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2132,height=1814,format=webp/_astro/browser-based-rdp-access-app.BNXce1JL.png)

To get started, see [Connect to RDP in a browser](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/).

Jun 30, 2025

[<h2>Cloudflare One Agent for Android (version 2.4.2)</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Android Cloudflare One Agent is now available in the [Google Play Store ↗︎](https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

- QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
- DNS over HTTPS traffic is now included in the WARP tunnel by default.
- The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).
- Fixed an issue that caused WARP connection failures on ChromeOS devices.

Jun 30, 2025

[<h2>Cloudflare One Agent for iOS (version 1.11)</h2>](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

- QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
- DNS over HTTPS traffic is now included in the WARP tunnel by default.
- The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).

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

Jun 18, 2025

[<h2>Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-new-order-of-enforcement/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) will now evaluate [Network (Layer 4) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) **before** [HTTP (Layer 7) policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.

This change will roll out progressively between **July 14–18, 2025**. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.

#### Updated order of enforcement

**Previous order:**

1. DNS policies
2. HTTP policies
3. Network policies

**New order:**

1. DNS policies
2. **Network policies**
3. **HTTP policies**

#### Action required: Review your Gateway HTTP policies

This change may affect block notifications. For example:

- You have an **HTTP policy** to block `example.com` and display a block page.
- You also have a **Network policy** to block `example.com` silently (no client notification).

With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.

To ensure users still receive a block notification, you can:

- Add a client notification to your Network policy, or
- Use only the HTTP policy for that domain.

---

#### Why we’re making this change

This update is based on user feedback and aims to:

- Create a more intuitive model by evaluating network-level policies before application-level policies.
- Minimize [526 connection errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context) by verifying the network path to an origin before attempting to establish a decrypted TLS connection.

---

To learn more, visit the [Gateway order of enforcement documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
