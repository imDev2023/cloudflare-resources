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

Mar 17, 2025

[<h2>Cloudflare One Agent for iOS (version 1.10)</h2>](https://developers.cloudflare.com/changelog/post/2025-03-17-warp-ga-ios/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release includes a new feature allowing [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url) during enrollment, as well as fixes and minor improvements.

**Changes and improvements**

- Improved in-app error messages.
- Improved mobile client login with support for [team name insertion by URL](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url).
- Bug fixes and performance improvements.

Mar 13, 2025

[<h2>Cloudflare IP Ranges List</h2>](https://developers.cloudflare.com/changelog/post/2025-03-13-new-managed-iplist/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)

Magic Firewall now supports a new managed list of Cloudflare IP ranges. This list is available as an option when creating a Magic Firewall policy based on IP source/destination addresses. When selecting "is in list" or "is not in list", the option "**Cloudflare IP Ranges**" will appear in the dropdown menu.

This list is based on the IPs listed in the Cloudflare [IP ranges ↗︎](https://www.cloudflare.com/en-gb/ips/). Updates to this managed list are applied automatically.

![Cloudflare IPs Managed List](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1102,height=677,format=webp/_astro/cloudflare-ips.DetyOndL.png)

Note: IP Lists require a Cloudflare Advanced Network Firewall subscription. For more details about Cloudflare Network Firewall plans, refer to [Plans](https://developers.cloudflare.com/cloudflare-network-firewall/plans).

Mar 7, 2025

[<h2>Cloudflare One Agent now supports Endpoint Monitoring</h2>](https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.

Device health metrics are now automatically collected, allowing administrators to:

- View the last network a user was connected to
- Monitor CPU and RAM utilization on devices
- Identify resource-intensive processes running on endpoints

![Device endpoint monitoring dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1226,height=675,format=webp/_astro/cloudflare-one-agent-health-monitoring.XXtiRuOp.gif)

This feature complements existing DEX features like [synthetic application monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) and [network path visualization](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/), creating a comprehensive troubleshooting workflow that connects application performance with device state.

For more details refer to our [DEX](https://developers.cloudflare.com/cloudflare-one/insights/dex/) documentation.

Mar 4, 2025

[<h2>Gain visibility into user actions in Zero Trust Browser Isolation sessions</h2>](https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

We're excited to announce that new logging capabilities for [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) through [Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) are available in Beta starting today!

With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.

```json
{
	"AccountID": "$ACCOUNT_ID",
	"Decision": "block",
	"DomainName": "www.example.com",
	"Timestamp": "2025-02-27T23:15:06Z",
	"Type": "copy",
	"UserID": "$USER_ID"
}
```

User Actions available:

- **Copy & Paste**
- **Downloads & Uploads**
- **Printing**

Learn more about how to get started with Logpush in our [documentation](https://developers.cloudflare.com/logs/logpush/).

Mar 3, 2025

[<h2>New SAML and OIDC Fields and SAML transforms for Access for SaaS</h2>](https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/) now include more configuration options to support a wider array of SaaS applications.

**SAML and OIDC Field Additions**

OIDC apps now include:

- Group Filtering via RegEx
- OIDC Claim mapping from an IdP
- OIDC token lifetime control
- Advanced OIDC auth flows including hybrid and implicit flows

![OIDC field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1021,height=192,format=webp/_astro/oidc-claims.2di8l9Lv.png)

SAML apps now include improved SAML attribute mapping from an IdP.

![SAML field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1051,height=202,format=webp/_astro/saml-attribute-statements.CW45j5Qi.png)

**SAML transformations**

SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.

![Configured SAML statement sent to application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1030,height=254,format=webp/_astro/transformation-box.DyKn-DdN.png)

Mar 1, 2025

[<h2>Use Logpush for Email security detections</h2>](https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select **Email security alerts** as the dataset.

![logpush-detections](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=927,height=688,format=webp/_astro/Logpush-Detections.Dc5tHta3.png)

For more information, refer to [Enable detection logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs).

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Feb 27, 2025

[<h2>Check status of Email security or Area 1</h2>](https://developers.cloudflare.com/changelog/post/2025-02-07-check-status/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Concerns about performance for Email security or Area 1? You can now check the operational status of both on the [Cloudflare Status page ↗︎](https://www.cloudflarestatus.com/).

For Email security, look under **Cloudflare Sites and Services**.

- **Dashboard** is the dashboard for Cloudflare, including Email security
- **Email security (Zero Trust)** is the processing of email
- **API** are the Cloudflare endpoints, including the ones for Email security

For Area 1, under **Cloudflare Sites and Services**:

- **Area 1 - Dash** is the dashboard for Cloudflare, including Email security
- **Email security (Area1)** is the processing of email
- **Area 1 - API** are the Area 1 endpoints

![Status-page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=792,height=348,format=webp/_astro/Status-Page.DcFJ1286.png)

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Feb 25, 2025

[<h2>Use DLP Assist for M365</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-dlp-assist-for-m365/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security customers who have Microsoft 365 environments can quickly deploy an Email DLP (Data Loss Prevention) solution for free.

Simply deploy our add-in, create a DLP policy in Cloudflare, and configure Outlook to trigger behaviors like displaying a banner, alerting end users before sending, or preventing delivery entirely.

Refer to [Outbound Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) to learn more about this feature.

In GUI alert:

![DLP-Alert](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1357,height=212,format=webp/_astro/DLP-Alert.5s-fbKn3.png)

Alert before sending:

![DLP-Pop-up](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1362,height=479,format=webp/_astro/DLP-Pop-up.0gkYy7o5.png)

Prevent delivery:

![DLP-Blocked](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1353,height=329,format=webp/_astro/DLP-Blocked.CmQkGrnM.png)

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Feb 14, 2025

[<h2>Configure your Magic WAN Connector to connect via static IP assignment</h2>](https://developers.cloudflare.com/changelog/post/2025-02-14-local-console-access/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now locally configure your [Magic WAN Connector](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) to work in a static IP configuration.

This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.

For more details, refer to [WAN with a static IP address](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console).

Feb 7, 2025

[<h2>Open email links with Security Center</h2>](https://developers.cloudflare.com/changelog/post/2025-02-07-open-links-security-center/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now investigate links in emails with Cloudflare Security Center to generate a report containing a myriad of technical details: a phishing scan, SSL certificate data, HTTP request and response data, page performance data, DNS records, what technologies and libraries the page uses, and more.

![Open links in Security Center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1118,height=402,format=webp/_astro/Open-Links-Security-Center.b-LJU4YB.png)

From **Investigation**, go to **View details**, and look for the **Links identified** section. Select **Open in Security Center** next to each link. **Open in Security Center** allows your team to quickly generate a detailed report about the link with no risk to the analyst or your environment.

For more details, refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Feb 3, 2025

[<h2>Block files that are password-protected, compressed, or otherwise unscannable.</h2>](https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.

These unscannable files are now matched with the [Download and Upload File Types traffic selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) for HTTP policies:

- Password-protected Microsoft Office document
- Password-protected PDF
- Password-protected ZIP archive
- Unscannable ZIP archive

To get started inspecting and modifying behavior based on these and other rules, refer to [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/).

Jan 20, 2025

[<h2>Detect source code leaks with Data Loss Prevention</h2>](https://developers.cloudflare.com/changelog/post/2025-01-03-source-code-confidence-level/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.

The following programming languages are validated with natural language processing (NLP).

- C
- C++
- C#
- Go
- Haskell
- Java
- JavaScript
- Lua
- Python
- R
- Rust
- Swift

DLP also supports confidence level for [source code profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code).

For more details, refer to [DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/).

Jan 15, 2025

[<h2>Export SSH command logs with Access for Infrastructure using Logpush</h2>](https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Availability

Only available on Enterprise plans.

Cloudflare now allows you to send SSH command logs to storage destinations configured in [Logpush](https://developers.cloudflare.com/logs/logpush/), including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the [SSH logs dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/).

To set up a Logpush job, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

Dec 19, 2024

[<h2>Escalate user submissions</h2>](https://developers.cloudflare.com/changelog/post/2024-12-19-escalate-user-submissions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

After you triage your users' submissions (that are machine reviewed), you can now escalate them to our team for reclassification (which are instead human reviewed). User submissions from the submission alias, PhishNet, and our API can all be escalated.

![Escalate](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=897,height=434,format=webp/_astro/Escalate.CwXPIyM3.png)

From **Reclassifications**, go to **User submissions**. Select the three dots next to any of the user submissions, then select **Escalate** to create a team request for reclassification. The Cloudflare dashboard will then show you the submissions on the **Team Submissions** tab.

Refer to [User submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/) to learn more about this feature.

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

Dec 19, 2024

[<h2>Increased transparency for phishing email submissions</h2>](https://developers.cloudflare.com/changelog/post/2024-12-19-reclassification-tab/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You now have more transparency about team and user submissions for phishing emails through a **Reclassification** tab in the Zero Trust dashboard.

Reclassifications happen when users or admins [submit a phish](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/) to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.

This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.

![Use the Reclassification area to review submitted phishing emails](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1645,height=758,format=webp/_astro/reclassifications-tab.yDgtjG51.png)

Dec 19, 2024

[<h2>Troubleshoot tunnels with diagnostic logs</h2>](https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

The latest `cloudflared` build [2024.12.2 ↗︎](https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2) introduces the ability to collect all the diagnostic logs needed to troubleshoot a `cloudflared` instance.

A diagnostic report collects data from a single instance of `cloudflared` running on the local machine and outputs it to a `cloudflared-diag` file.

For more information, refer to [Diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

Dec 17, 2024

[<h2>Establish BGP peering over Direct CNI circuits</h2>](https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/)

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

Refer to [Magic WAN BGP peering](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) or [Magic Transit BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes) to learn more about this feature and how to set it up.

Dec 5, 2024

[<h2>Generate customized terraform files for building cloud network on-ramps</h2>](https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/)

[Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/)

You can now generate customized terraform files for building cloud network on-ramps to [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/).

[Magic Cloud](https://developers.cloudflare.com/multi-cloud-networking/) can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.

You might want to do this to:

- Review the proposed configuration for an on-ramp before deploying it with Cloudflare.
- Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.

For more details, refer to [Set up with Terraform](https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform).

Nov 22, 2024

[<h2>Find security misconfigurations in your AWS cloud environment</h2>](https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

You can now use CASB to find security misconfigurations in your AWS cloud environment using [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/).

You can also [connect your AWS compute account](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account) to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.

To connect a compute account to your AWS integration:

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Integrations**.
2. Find and select your AWS integration.
3. Select **Open connection instructions**.
4. Follow the instructions provided to connect a new compute account.
5. Select **Refresh**.

Nov 21, 2024

[<h2>Improved non-English keyboard support</h2>](https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.

Nov 7, 2024

[<h2>Use Logpush for Email security user actions</h2>](https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.

When creating a new Logpush job, remember to select **Audit logs** as the dataset and filter by:

- **Field**: `"ResourceType"`
- **Operator**: `"starts with"`
- **Value**: `"email_security"`.

![Logpush-user-actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=829,height=454,format=webp/_astro/Logpush-User-Actions.D14fWgmq.png)

For more information, refer to [Enable user action logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs).

This feature is available across all Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

Oct 2, 2024

[<h2>Search for custom rules using rule name and/or ID</h2>](https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)

The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.

1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select your account.
2. Go to **Analytics & Logs** > **Network Analytics**.
3. Select **Magic Firewall**.
4. Add a filter for **Rule ID**.

![Search for firewall rules with rule IDs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1032,height=801,format=webp/_astro/search-with-rule-id.DJgzqgKk.png)

Additionally, the rule ID URL link has been added to Network Analytics.

Oct 1, 2024

[<h2>Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</h2>](https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.

SSH with [Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: [WARP-to-Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/).

SSH with Access for Infrastructure enables you to:

- **Author fine-grained policy** to control who may access your SSH servers, including specific ports, protocols, and SSH users.
- **Monitor infrastructure access** with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.
- **Preserve your end users' workflows.** SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.

![Example of an infrastructure Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1916,height=1714,format=webp/_astro/infrastructure-app.BhpJOgxs.png)

To get started, refer to [SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/).

Jun 17, 2024

[<h2>Exchange user risk scores with Okta</h2>](https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/)

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Beyond the controls in [Zero Trust](https://developers.cloudflare.com/cloudflare-one/), you can now [exchange user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta) with Okta to inform SSO-level policies.

First, configure Cloudflare One to send user risk scores to Okta.

1. Set up the [Okta SSO integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/).
2. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.
3. In **Your identity providers**, locate your Okta integration and select **Edit**.
4. Turn on **Send risk score to Okta**.
5. Select **Save**.
6. Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.

Next, configure Okta to receive your risk scores.

1. On your Okta admin dashboard, go to **Security** > **Device Integrations**.
2. Go to **Receive shared signals**, then select **Create stream**.
3. Name your integration. In **Set up integration with**, choose *Well-known URL*.
4. In **Well-known URL**, enter the well-known URL value provided by Cloudflare One.
5. Select **Create**.

Jun 16, 2024

[<h2>Explore product updates for Cloudflare One</h2>](https://developers.cloudflare.com/changelog/post/2024-06-16-cloudflare-one/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/) [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [Email security](https://developers.cloudflare.com/cloudflare-one/email-security/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/) [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Network Flow](https://developers.cloudflare.com/network-flow/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Network Interconnect](https://developers.cloudflare.com/network-interconnect/) [Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Welcome to your new home for product updates on [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

Our [new changelog](https://developers.cloudflare.com/changelog/) lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.

If you are looking for older product updates, refer to the following locations.

<details>

<summary>

Older product updates

</summary>

- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/access/">Access</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/browser-isolation/">Browser Isolation</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/casb/">CASB</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/">Cloudflare Tunnel</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/dlp/">Data Loss Prevention</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/dex/">Digital Experience Monitoring</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/email-security/">Email security</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/gateway/">Gateway</a>
- <a href="https://developers.cloudflare.com/multi-cloud-networking/changelog/">Multi-Cloud Networking</a>
- <a href="https://developers.cloudflare.com/cloudflare-network-firewall/changelog/">Cloudflare Network Firewall</a>
- <a href="https://developers.cloudflare.com/network-flow/changelog/">Magic Network Monitoring</a>
- <a href="https://developers.cloudflare.com/magic-transit/changelog/">Magic Transit</a>
- <a href="https://developers.cloudflare.com/cloudflare-wan/changelog/">Magic WAN</a>
- <a href="https://developers.cloudflare.com/network-interconnect/changelog/">Network Interconnect</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/">Risk score</a>
- <a href="https://developers.cloudflare.com/changelog/cloudflare-one-client/">Cloudflare One Client</a>

</details>

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/13/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/13/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
