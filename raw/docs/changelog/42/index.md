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

Jul 28, 2025

[<h2>WAF Release - 2025-07-28</h2>](https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s update spotlights several vulnerabilities across Apache Tomcat, MongoDB, and Fortinet FortiWeb. Several flaws related with a memory leak in Apache Tomcat can lead to a denial-of-service attack. Additionally, a code injection flaw in MongoDB's Mongoose library allows attackers to bypass security controls to access restricted data.

**Key Findings**

- Fortinet FortiWeb (CVE-2025-25257): An improper neutralization of special elements used in a SQL command vulnerability in Fortinet FortiWeb versions allows an unauthenticated attacker to execute unauthorized SQL code or commands.
- Apache Tomcat (CVE-2025-31650): A improper Input Validation vulnerability in Apache Tomcat that could create memory leak when incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request.
- MongoDB (CVE-2024-53900, CVE:CVE-2025-23061): Improper use of `$where` in match and a nested `$where` filter with a `populate()` match in Mongoose can lead to search injection.

**Impact**

These vulnerabilities target user-facing components, web application servers, and back-end databases. A SQL injection flaw in Fortinet FortiWeb can lead to data theft or system compromise. A separate issue in Apache Tomcat involves a memory leak from improper input validation, which could be exploited for a denial-of-service (DoS) attack. Finally, a vulnerability in MongoDB's Mongoose library allows attackers to bypass security filters and access unauthorized data through malicious search queries.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...3461ec9e | 100804 | BerriAI - SSRF - CVE:CVE-2024-6587 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...0cb13e1d | 100812 | Fortinet FortiWeb - Remote Code Execution - CVE:CVE-2025-25257 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...67fae7f7 | 100813 | Apache Tomcat - DoS - CVE:CVE-2025-31650 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...4b6a5bb1 | 100815 | MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...688f8e79 | 100816 | MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061 | Log | Block | This is a New Detection |

Jul 24, 2025

[<h2>Gateway HTTP Filtering on all ports available in open BETA</h2>](https://developers.cloudflare.com/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) can now apply [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) to all proxied HTTP requests, not just traffic on standard HTTP (`80`) and HTTPS (`443`) ports. This means all requests can now be filtered by [A/V scanning](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/), [file sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/), [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/#data-in-transit), and more.

You can turn this [setting](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports) on by going to **Settings** > **Network** > **Firewall** and choosing *Inspect on all ports*.

![HTTP Inspection on all ports setting](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=535,format=webp/_astro/Gateway-Inspection-all-ports.CCmwX6D0.png)

To learn more, refer to [Inspect on all ports (Beta)](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports).

Jul 22, 2025

[<h2>Browser Rendering now supports local development</h2>](https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

You can now run your Browser Rendering locally using `npx wrangler dev`, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.

Get started with this [example guide](https://developers.cloudflare.com/browser-run/how-to/deploy-worker/) that shows how to use Cloudflare's [fork of Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/) (you can also use [Playwright](https://developers.cloudflare.com/browser-run/playwright/)) to take screenshots of webpages and store the results in [Workers KV](https://developers.cloudflare.com/kv/).

Jul 22, 2025

[<h2>Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/)

[Workers](https://developers.cloudflare.com/workers/)

Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.

This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch. These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.

![PR comment preview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2900,height=1064,format=webp/_astro/preview-urls-comment.0wQffFIq.png)

#### Preview URL types

Each comment includes **two preview URLs** as shown above:

- **Commit Preview URL**: Unique to the specific version/commit (e.g., `<version-prefix>-<worker-name>.<subdomain>.workers.dev`)
- **Branch Preview URL**: A stable alias based on the branch name (e.g., `<branch-name>-<worker-name>.<subdomain>.workers.dev`)

#### How it works

When you create a pull request:

- **A preview alias is automatically created** based on the Git branch name (e.g., `<branch-name>` becomes `<branch-name>-<worker-name>.<subdomain>.workers.dev`)
- **No configuration is needed**, the alias is generated for you
- **The link stays the same** even as you add commits to the same branch
- **Preview URLs are posted directly to your pull request as comments** (just like they are in Cloudflare Pages)

#### Custom alias name

You can also assign a custom preview alias using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/), by passing the `--preview-alias` flag when [uploading a version](https://developers.cloudflare.com/workers/wrangler/commands/general/#versions-upload) of your Worker:

```bash
wrangler versions upload --preview-alias staging
```

#### Limitations while in beta

- Only available on the **workers.dev** subdomain (custom domains not yet supported)
- Requires **Wrangler v4.21.0+**
- Preview URLs are not generated for Workers that use [Durable Objects](https://developers.cloudflare.com/durable-objects/)
- Not yet supported for [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Jul 22, 2025

[<h2>Google Bard Application replaced by Gemini</h2>](https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

The **Google Bard** application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the **Gemini** application (ID: 1340). Any existing Gateway policies that reference the old Google Bard application will no longer function. To ensure your policies continue to work as intended, you should update them to use the new Gemini application. We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies. For more information about application policies, please see the [Cloudflare Gateway documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

Jul 22, 2025

[<h2>Audio mode for Media Transformations</h2>](https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/)

[Stream](https://developers.cloudflare.com/stream/)

We now support `audio` mode! Use this feature to extract audio from a source video, outputting an M4A file to use in downstream workflows like [AI inference](https://developers.cloudflare.com/workers-ai/), content moderation, or transcription.

For example,

*Example URLtext*

```text
https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>
https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/<input video with diction>
```

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

Jul 21, 2025

[<h2>Virtual Cloudflare One Appliance with KVM support (open beta)</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.

Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.

For setup instructions, refer to [Configure a virtual Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Jul 21, 2025

[<h2>Subaddressing support in Email Routing</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-subaddressing/)

[Email Service](https://developers.cloudflare.com/email-service/)

Subaddressing, as defined in [RFC 5233 ↗︎](https://www.rfc-editor.org/rfc/rfc5233), also known as plus addressing, is now supported in Email Routing. This enables using the "+" separator to augment your custom addresses with arbitrary detail information.

Now you can send an email to `user+detail@example.com` and it will be captured by the `user@example.com` custom address. The `+detail` part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an [Email Worker](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) or an [Agent application ↗︎](https://github.com/cloudflare/agents/tree/main/examples/email-agent).

Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.

![Subaddressing](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1316,height=678,format=webp/_astro/subaddressing.x65bljxx.png)

Check our [Developer Docs](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#subaddressing) to learn how to enable subaddressing in Email Routing.

Jul 21, 2025

[<h2>WAF Release - 2025-07-21 - Emergency</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-emergency/)

[WAF](https://developers.cloudflare.com/waf/)

This week's update highlights several high-impact vulnerabilities affecting Microsoft SharePoint Server. These flaws, involving unsafe deserialization, allow unauthenticated remote code execution over the network, posing a critical threat to enterprise environments relying on SharePoint for collaboration and document management.

**Key Findings**

- Microsoft SharePoint Server (CVE-2025-53770): A critical vulnerability involving unsafe deserialization of untrusted data, enabling unauthenticated remote code execution over the network. This flaw allows attackers to execute arbitrary code on vulnerable SharePoint servers without user interaction.
- Microsoft SharePoint Server (CVE-2025-53771): A closely related deserialization issue that can be exploited by unauthenticated attackers, potentially leading to full system compromise. The vulnerability highlights continued risks around insecure serialization logic in enterprise collaboration platforms.

**Impact**

Together, these vulnerabilities significantly weaken the security posture of on-premise Microsoft SharePoint Server deployments. By enabling remote code execution without authentication, they open the door for attackers to gain persistent access, deploy malware, and move laterally across enterprise environments.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2168f6f0 | 100817 | Microsoft SharePoint - Deserialization - CVE:CVE-2025-53770 | N/A | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...8de656c4 | 100818 | Microsoft SharePoint - Deserialization - CVE:CVE-2025-53771 | N/A | Block | This is a New Detection |

For more details, also refer to [our blog ↗︎](https://blog.cloudflare.com/cloudflare-protects-against-critical-sharepoint-vulnerability-cve-2025-53770/).

Jul 21, 2025

[<h2>WAF Release - 2025-07-21</h2>](https://developers.cloudflare.com/changelog/post/2025-07-21-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.

**Key Findings**

- Wing FTP Server (CVE-2025-47812): A critical Remote Code Execution (RCE) vulnerability that enables unauthenticated attackers to execute arbitrary code with root/SYSTEM-level privileges by exploiting a Lua injection flaw.
- Infoblox NetMRI (CVE-2025-32813): A remote unauthenticated command injection flaw that allows an attacker to execute arbitrary commands, potentially leading to unauthorized access.
- Citrix Netscaler ADC (CVE-2025-5777, CVE-2023-4966): A sensitive information disclosure vulnerability, also known as "Citrix Bleed2", that allows the disclosure of memory and subsequent remote access session hijacking.
- Akamai CloudTest (CVE-2025-49493): An XML External Entity (XXE) injection that could lead to read local files on the system by manipulating XML input.

**Impact**

These vulnerabilities affect critical enterprise infrastructure, from file transfer services and network management appliances to application delivery controllers. The Wing FTP RCE and Infoblox command injection flaws offer direct paths to deep system compromise, while the Citrix "Bleed2" and Akamai XXE vulnerabilities undermine system integrity by enabling session hijacking and sensitive data theft.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...3461ec9e | 100804 | BerriAI - SSRF - CVE:CVE-2024-6587 | Log | Log | This is a New Detection |
| Cloudflare Managed Ruleset | ...5199b58a | 100805 | Wing FTP Server - Remote Code Execution - CVE:CVE-2025-47812 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...919a91a4 | 100807 | Infoblox NetMRI - Command Injection - CVE:CVE-2025-32813 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...7899130f | 100808 | Citrix Netscaler ADC - Buffer Error - CVE:CVE-2025-5777 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...d1cf8e08 | 100809 | Citrix Netscaler ADC - Information Disclosure - CVE:CVE-2023-4966 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...6e70469f | 100810 | Akamai CloudTest - XXE - CVE:CVE-2025-49493 | Log | Block | This is a New Detection |

Jul 18, 2025

[<h2>New APIs for Brand Protection setup</h2>](https://developers.cloudflare.com/changelog/post/2025-07-18-brand-protection-api/)

[Security Center](https://developers.cloudflare.com/security-center/)

The Brand Protection API is now available, allowing users to create new queries and delete existing ones, fetch matches and more!

What you can do:

- **create new string or logo query**
- **delete string or logo queries**
- **download matches for both logo and string queries**
- **read matches for both logo and string queries**

Ready to start? Check out the [Brand Protection API](https://developers.cloudflare.com/api/resources/brand_protection/) in our documentation.

Jul 17, 2025

[<h2>The Cloudflare Vite plugin now supports Vite 7</h2>](https://developers.cloudflare.com/changelog/post/2025-07-17-vite-plugin-vite-7-support/)

[Workers](https://developers.cloudflare.com/workers/)

[Vite 7 ↗︎](https://vite.dev/blog/announcing-vite7) is now supported in the Cloudflare Vite plugin. See the [Vite changelog ↗︎](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24) for a list of changes.

Note that the minimum Node.js versions supported by Vite 7 are 20.19 and 22.12. We continue to support Vite 6 so you do not need to immediately upgrade.

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

Jul 14, 2025

[<h2>Terraform v5.7.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-07-11-terraform-v5.7.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). We are aware of the high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.

Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Addressed permanent diff bug on Cloudflare Tunnel config
- State is now saved correctly for Zero Trust Access applications
- Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
- `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
- Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
- New resource:
  - `cloudflare_zero_trust_tunnel_warp_connector`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0) in GitHub.

#### Issues Closed

- [#5563: cloudflare\_logpull\_retention is missing import ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
- [#5608: cloudflare\_zero\_trust\_access\_policy in 5.5.0 provider gives error upon apply unexpected new value: .app\_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1) ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
- [#5612: data.cloudflare\_zero\_trust\_access\_applications does not exact match ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
- [#5532: cloudflare\_zero\_trust\_access\_identity\_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5662: cloudflare\_zero\_trust\_access\_policy does not support OIDC claims ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
- [#5565: Running Terraform with the cloudflare\_zero\_trust\_access\_policy resource results in updates on every apply, even when no changes are made - breaks idempotency ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
- [#5529: cloudflare\_zero\_trust\_access\_application: self hosted applications with private ips require public domain ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.

If you'd like more information on migrating from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Jul 14, 2025

[<h2>WAF Release - 2025-07-14</h2>](https://developers.cloudflare.com/changelog/post/2025-07-14-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.

**Key Findings**

- XSS – Attribute Overloading: A novel cross-site scripting technique where attackers abuse custom or non-standard HTML attributes to smuggle payloads into the DOM. These payloads evade traditional sanitization logic, especially in frameworks that loosely validate attributes or trust unknown tokens.
- XSS – onToggle Event Abuse: Exploits the lesser-used onToggle event (triggered by elements like `<details>`) to execute arbitrary JavaScript when users interact with UI elements. This vector is often overlooked by static analyzers and can be embedded in seemingly benign components.

**Impact**

These vulnerabilities target both user-facing components and back-end databases, introducing potential vectors for credential theft, session hijacking, or full data exfiltration. The XSS variants bypass conventional filters through overlooked HTML behaviors, while the obfuscated SQLi enables attackers to stealthily probe back-end logic, making them especially difficult to detect and block.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...2aa3d845 | 100798 | XSS - Attribute Overloading | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...37548d06 | 100799 | XSS - OnToggle | Log | Block | This is a New Detection |

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

Jul 9, 2025

[<h2>Usage tracking</h2>](https://developers.cloudflare.com/changelog/post/2025-07-09-usage-tracking/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and [Manage Datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/) screens in Log Explorer.

![Ingested data](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=418,height=157,format=webp/_astro/ingested-data.D2flqRIu.png)

Jul 8, 2025

[<h2>Faster indexing and new Jobs view in AutoRAG</h2>](https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/)

[AI Search](https://developers.cloudflare.com/ai-search/)

You can now expect **3-5× faster indexing** in AutoRAG, and with it, a brand new **Jobs view** to help you monitor indexing progress.

With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the [Sync API](https://developers.cloudflare.com/api/resources/ai-search/subresources/rags/) or by clicking “Sync index” in the dashboard.

With the new jobs observability, you can now:

- View the status, job ID, source, start time, duration and last sync time for each indexing job
- Inspect real-time logs of job events (e.g. `Starting indexing data source...`)
- See a history of past indexing jobs under the Jobs tab of your AutoRAG

This makes it easier to understand what’s happening behind the scenes.

**Coming soon:** We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.

Try it out today on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/autorag).

Jul 8, 2025

[<h2>HEIC support in Cloudflare Images</h2>](https://developers.cloudflare.com/changelog/post/heic-support/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.

When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for [uploading to Images](https://developers.cloudflare.com/images/storage/upload-images/methods/) or [transforming a remote image](https://developers.cloudflare.com/images/optimization/transformations/overview/).

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

Jul 7, 2025

[<h2>Increased IP List Limits for Enterprise Accounts</h2>](https://developers.cloudflare.com/changelog/post/2025-07-07-increased-ip-list-limits/)

[WAF](https://developers.cloudflare.com/waf/)

We have significantly increased the limits for [IP Lists](https://developers.cloudflare.com/waf/tools/lists/) on Enterprise plans to provide greater flexibility and control:

- **Total number of lists**: Increased from 10 to 1,000.
- **Total number of list items**: Increased from 10,000 to 500,000.

Limits for other list types and plans remain unchanged. For more details, refer to the [lists availability](https://developers.cloudflare.com/waf/tools/lists/#availability).

Jul 7, 2025

[<h2>WAF Release - 2025-07-07</h2>](https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.

**Key Findings**

- Next.js - Auth Bypass: A newly detected authentication bypass flaw in the Next.js framework allows attackers to access protected routes or APIs without proper authorization, undermining application access controls.
- Fortinet FortiVoice (CVE-2025-32756): A buffer error vulnerability in FortiVoice systems that could lead to memory corruption and potential code execution or service disruption in enterprise telephony environments.
- Roundcube (CVE-2025-49113): A critical RCE flaw allowing unauthenticated attackers to execute arbitrary PHP code via crafted requests, leading to full compromise of mail servers and user inboxes.

**Impact**

These vulnerabilities affect core business infrastructure, from web interfaces to voice communications and email platforms. The Roundcube RCE and FortiVoice buffer flaw offer potential for deep system access, while the Next.js auth bypass undermines trust boundaries in modern web apps.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...7eb35ee6 | 100795 | Next.js - Auth Bypass | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...c329aeb0 | 100796 | Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756 | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...ab314023 | 100797 | Roundcube - Remote Code Execution - CVE:CVE-2025-49113 | Log | Disabled | This is a New Detection |

Jul 4, 2025

[<h2>Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs</h2>](https://developers.cloudflare.com/changelog/post/2025-07-04-javascript-debug-terminals/)

[Workers](https://developers.cloudflare.com/workers/)

Workers now support breakpoint debugging using VSCode's built-in [JavaScript Debug Terminals ↗︎](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal). All you have to do is open a JS debug terminal (`Cmd + Shift + P` and then type `javascript debug`) and run `wrangler dev` (or `vite dev`) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.

In 2023 we announced [breakpoint debugging support ↗︎](https://blog.cloudflare.com/debugging-cloudflare-workers/) for Workers, which meant that you could easily debug your Worker code in Wrangler's built-in devtools (accessible via the `[d]` hotkey) as well as multiple other devtools clients, [including VSCode ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/). For most developers, breakpoint debugging via VSCode is the most natural flow, but until now it's required [manually configuring a `launch.json` file ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#setup-vs-code-to-use-breakpoints), running `wrangler dev`, and connecting via VSCode's built-in debugger. Now it's much more seamless!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/42/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/42/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
