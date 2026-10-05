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

Jun 17, 2025

[<h2>Terraform v5.6.0 now available</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-terraform-v5.6.0-provider/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Earlier this year, we announced the launch of the new [Terraform v5 Provider](https://developers.cloudflare.com/changelog/2025-02-03-terraform-v5-provider/). Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of [issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.

#### Changes

- Broad fixes across resources with recurring diffs, including, but not limited to:
  - `cloudflare_zero_trust_access_identity_provider`
    - `cloudflare_zone`
- `cloudflare_page_rules` runtime panic when setting `cache_level` to `cache_ttl_by_status`
- Failure to serialize requests in `cloudflare_zero_trust_tunnel_cloudflared_config`
- Undocumented field 'priority' on `zone_lockdown` resource
- Missing importability for `cloudflare_zero_trust_device_default_profile_local_domain_fallback` and `cloudflare_account_subscription`
- New resources:
  - `cloudflare_schema_validation_operation_settings`
  - `cloudflare_schema_validation_schemas`
  - `cloudflare_schema_validation_settings`
  - `cloudflare_zero_trust_device_settings`
- Other bug fixes

For a more detailed look at all of the changes, see the [changelog ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0) in GitHub.

#### Issues Closed

- [#5098: 500 Server Error on updating 'zero\_trust\_tunnel\_cloudflared\_virtual\_network' Terraform resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
- [#5148: cloudflare\_user\_agent\_blocking\_rule doesn’t actually support user agents ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
- [#5472: cloudflare\_zone showing changes in plan after following upgrade steps ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
- [#5508: cloudflare\_zero\_trust\_tunnel\_cloudflared\_config failed to serialize http request ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
- [#5509: cloudflare\_zone: Problematic Terraform behaviour with paused zones ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
- [#5520: Resource 'cloudflare\_magic\_wan\_static\_route' is not working ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
- [#5524: Optional fields cause crash in cloudflare\_zero\_trust\_tunnel\_cloudflared(s) when left null ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
- [#5526: Provider v5 migration issue: no import method for cloudflare\_zero\_trust\_device\_default\_profile\_local\_domain\_fallback ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
- [#5532: cloudflare\_zero\_trust\_access\_identity\_provider detects changes on every plan ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5561: cloudflare\_zero\_trust\_tunnel\_cloudflared: cannot rotate tunnel secret ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
- [#5569: cloudflare\_zero\_trust\_device\_custom\_profile\_local\_domain\_fallback not allowing multiple DNS Server entries ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
- [#5577: Panic modifying page\_rule resource ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
- [#5653: cloudflare\_zone\_setting resource schema confusion in 5.5.0: value vs enabled ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)

If you have an unaddressed issue with the provider, we encourage you to check the [open issues ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues) and open a new one if one does not already exist for what you are experiencing.

#### Upgrading

If you are evaluating a move from v4 to v5, please make use of the [migration guide ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade). We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of `terraform plan` to test your changes before applying, and let us know if you encounter any additional issues by reporting to our [GitHub repository ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare).

#### For more info

- [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)

Jun 17, 2025

[<h2>Control which routes invoke your Worker script for Single Page Applications</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-advanced-routing/)

[Workers](https://developers.cloudflare.com/workers/)

For those building [Single Page Applications (SPAs) on Workers](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/#advanced-routing-control), you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The [`run_worker_first` config option](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first) has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.

**Configuration example:**

```jsonc
{
	"name": "my-spa-worker",
	// Set this to today's date
	"compatibility_date": "2026-10-05",
	"main": "./src/index.ts",
	"assets": {
		"directory": "./dist/",
		"not_found_handling": "single-page-application",
		"binding": "ASSETS",
		"run_worker_first": ["/api/*", "!/api/docs/*"]
	}
}
```

```toml
name = "my-spa-worker"
# Set this to today's date
compatibility_date = "2026-10-05"
main = "./src/index.ts"

[assets]
directory = "./dist/"
not_found_handling = "single-page-application"
binding = "ASSETS"
run_worker_first = [ "/api/*", "!/api/docs/*" ]
```

This new routing control was done in partnership with our community and customers who provided great feedback on [our public proposal ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9143). Thank you to everyone who brought forward use-cases and feedback on the design!

#### Prerequisites

To use advanced routing control with `run_worker_first`, you'll need:

- [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) v4.20.0 and above
- [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/get-started/) v1.7.0 and above

Jun 17, 2025

[<h2>SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers</h2>](https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/)

[Workers](https://developers.cloudflare.com/workers/)

Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the `@opennextjs/cloudflare` package.

The vulnerability stemmed from an unimplemented feature in the Cloudflare adapter for Open Next, which allowed users to proxy arbitrary remote content via the `/_next/image` endpoint.

This issue allowed attackers to load remote resources from arbitrary hosts under the victim site's domain for any site deployed using the Cloudflare adapter for Open Next. For example: `https://victim-site.com/_next/image?url=https://attacker.com`. In this example, attacker-controlled content from `attacker.com` is served through the victim site's domain (`victim-site.com`), violating the same-origin policy and potentially misleading users or other services.

References: [https://www.cve.org/cverecord?id=CVE-2025-6087 ↗︎](https://www.cve.org/cverecord?id=CVE-2025-6087), [https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m)

#### Impact

- SSRF via unrestricted remote URL loading
- Arbitrary remote content loading
- Potential internal service exposure or phishing risks through domain abuse

#### Mitigation

The following mitigations have been put in place:

**Server side updates** to Cloudflare's platform to restrict the content loaded via the `/_next/image` endpoint to images. The update automatically mitigates the issue for all existing and any future sites deployed to Cloudflare using the affected version of the Cloudflare adapter for Open Next

**Root cause fix:** Pull request [#727 ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/pull/727) to the Cloudflare adapter for Open Next. The patched version of the adapter has been released as `@opennextjs/cloudflare@1.3.0`

**Package dependency update:** Pull request [cloudflare/workers-sdk#9608 ↗︎](https://github.com/cloudflare/workers-sdk/pull/9608) to create-cloudflare (c3) to use the fixed version of the Cloudflare adapter for Open Next. The patched version of create-cloudflare has been published as `create-cloudflare@2.49.3`.

In addition to the automatic mitigation deployed on Cloudflare's platform, we encourage affected users to upgrade to `@opennext/cloudflare` v1.3.0 and use the [`remotePatterns` ↗︎](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns) filter in Next config if they need to allow-list external urls with images assets.

Jun 16, 2025

[<h2>Internal DNS (beta) now manageable in the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-06-16-internal-dns-beta-ui/)

[DNS](https://developers.cloudflare.com/dns/)

Participating beta testers can now fully configure [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) directly in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/internal-dns).

#### Internal DNS enables customers to:

- Map internal hostnames to private IPs for services, devices, and applications not exposed to the public Internet
- Resolve internal DNS queries securely through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)
- Use split-horizon DNS to return different responses based on network context
- Consolidate internal and public DNS zones within a single management platform

#### What’s new in this release:

- Beta participants can now create and manage internal zones and views in the Cloudflare dashboard

![Internal DNS UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2364,height=1320,format=webp/_astro/internal-dns-beta-ui.B5uCVZ9o.png)

Note

The Internal DNS beta is currently only available to Enterprise customers.

To learn more and get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

Jun 16, 2025

[<h2>WAF Release - 2025-06-16</h2>](https://developers.cloudflare.com/changelog/post/2025-06-16-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.

**Key Findings**

- Cisco IOS XE (CVE-2025-20188): Critical RCE vulnerability enabling unauthenticated attackers to execute arbitrary commands on network infrastructure devices, risking total router compromise.
- Axios (CVE-2024-39338): SSRF flaw impacting server-side request control, allowing attackers to manipulate internal service requests when misconfigured with unsanitized user input.
- vBulletin (CVE-2025-48827, CVE-2025-48828): Two high-impact RCE flaws enabling attackers to remotely execute PHP code, compromising forum installations and underlying web servers.
- Invision Community (CVE-2025-47916): A critical RCE vulnerability allowing authenticated attackers to run arbitrary code in community platforms, threatening data and lateral movement risk.
- CrushFTP (CVE-2025-32102, CVE-2025-32103): SSRF vulnerabilities in upload endpoint processing permit attackers to pivot internal network scans and abuse internal services.
- Roundcube (CVE-2025-49113): RCE via email processing enables attackers to execute code upon viewing a crafted email — particularly dangerous for webmail deployments.
- WooCommerce WordPress Plugin (CVE-2025-47577): Dangerous file upload vulnerability permits unauthenticated users to upload executable payloads, leading to full WordPress site takeover.
- Cross-Site Scripting (XSS) Detection Improvements: Enhanced detection patterns.

**Impact**

These vulnerabilities span core systems — from routers to e-commerce to email. RCE in Cisco IOS XE, Roundcube, and vBulletin poses full system compromise. SSRF in Axios and CrushFTP supports internal pivoting, while WooCommerce’s file upload bug opens doors to mass WordPress exploitation.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...35fefd53 | 100783 | Cisco IOS XE - Remote Code Execution - CVE:CVE-2025-20188 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...8332af5d | 100784 | Axios - SSRF - CVE:CVE-2024-39338 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...2e1648d2 | 100785 | vBulletin - Remote Code Execution - CVE:CVE-2025-48827, CVE:CVE-2025-48828 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0edcf1ef | 100786 | Invision Community - Remote Code Execution - CVE:CVE-2025-47916 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...d6f5eb48 | 100791 | CrushFTP - SSRF - CVE:CVE-2025-32102, CVE:CVE-2025-32103 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...30baa18a | 100792 | Roundcube - Remote Code Execution - CVE:CVE-2025-49113 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...229ba236 | 100793 | XSS - Ontoggle | Log | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...fa338296 | 100794 | WordPress WooCommerce Plugin - Dangerous File Upload - CVE:CVE-2025-47577 | Log | Block | This is a New Detection |

Jun 16, 2025

[<h2>Grant account members read-only access to the Workers Platform</h2>](https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/)

[Workers](https://developers.cloudflare.com/workers/)

You can now grant members of your Cloudflare account read-only access to the Workers Platform.

The new "Workers Platform (Read-only)" role grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including [Workers](https://developers.cloudflare.com/workers/), [Pages](https://developers.cloudflare.com/pages/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), [KV](https://developers.cloudflare.com/kv/), [R2](https://developers.cloudflare.com/r2/), Zones, [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/) and [Page Rules](https://developers.cloudflare.com/rules/). When Cloudflare introduces new products to the Workers platform, we will add additional read-only permissions to this role.

Additionally, the role previously named "Workers Admin" has been renamed to "Workers Platform Admin". This change ensures that the name more accurately reflects the permissions granted — this role has always granted access to more than just Workers — it grants read and write access to the products mentioned above, and similarly, as new products are added to the Workers platform, we will add additional read and write permissions to this role.

You can review the updated roles in the [developer docs](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

Jun 11, 2025

[<h2>NSEC3 support for DNSSEC</h2>](https://developers.cloudflare.com/changelog/post/2025-06-11-nsec3-support/)

[DNS](https://developers.cloudflare.com/dns/)

Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.

What's new:

- **NSEC3 support for live-signed zones** – For both primary and secondary zones that are configured to be live-signed (also known as "on-the-fly signing"), NSEC3 can now be selected as proof of non-existence.
- **NSEC3 support for pre-signed zones** – Secondary zones that are transferred to Cloudflare in a [pre-signed setup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec) now also support NSEC3 as proof of non-existence.

For more information and how to enable NSEC3, refer to the [NSEC3 documentation](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/).

Jun 10, 2025

[<h2>Increased limits for Media Transformations</h2>](https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/)

[Stream](https://developers.cloudflare.com/stream/)

We have increased the limits for [Media Transformations](https://developers.cloudflare.com/stream/transform-videos/):

- Input file size limit is now 100MB (was 40MB)
- Output video duration limit is now 1 minute (was 30 seconds)

Additionally, we have improved caching of the input asset, resulting in fewer requests to origin storage even when transformation options may differ.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

Jun 10, 2025

[<h2>Access git commit sha and branch name as environment variables in Workers Builds</h2>](https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) connects your Worker to a [Git repository](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/), and automates building and deploying your code on each pushed change.

To make CI/CD pipelines even more flexible, Workers Builds now automatically injects [default environment variables](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables) into your build process (much like the defaults in [Cloudflare Pages projects](https://developers.cloudflare.com/pages/configuration/build-configuration/#environment-variables)). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.

The following environment variables are injected by default:

| Environment Variable | Injected value | Example use-case |
| --- | --- | --- |
| `CI` | `true` | Changing build behavior when run on CI versus locally |
| `WORKERS_CI` | `1` | Changing build behavior when run on Workers Builds versus locally |
| `WORKERS_CI_BUILD_UUID` | `<build-uuid-of-current-build>` | Passing the Build UUID along to custom workflows |
| `WORKERS_CI_COMMIT_SHA` | `<sha1-hash-of-current-commit>` | Passing current commit ID to error reporting, for example, Sentry |
| `WORKERS_CI_BRANCH` | `<branch-name-from-push-event` | Customizing build based on branch, for example, disabling debug logging on `production` |

You can override these default values and add your own custom environment variables by navigating to **your Worker** > **Settings** > **Environment variables**.

Learn more in the [Build configuration documentation](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables).

Jun 9, 2025

[<h2>More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/)

[Rules](https://developers.cloudflare.com/rules/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) can now fetch and store [assets](https://developers.cloudflare.com/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard) and [error pages](https://developers.cloudflare.com/rules/custom-errors/#error-pages) from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.

**What’s new:**

- You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.
- These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.

This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.

Learn more in the [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) documentation.

Jun 9, 2025

[<h2>Match Workers subrequests by upstream zone — cf.worker.upstream\_zone now supported in Transform Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/)

[Rules](https://developers.cloudflare.com/rules/)

You can now use the [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field in [Transform Rules](https://developers.cloudflare.com/rules/transform/) to control rule execution based on whether a request originates from [Workers](https://developers.cloudflare.com/workers/), including subrequests issued by Workers in other zones.

![Match Workers subrequests by upstream zone in Transform Rules](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1446,height=988,format=webp/_astro/transform-rule-subrequest-matching.BeUBEN67.png)

**What's new:**

- `cf.worker.upstream_zone` is now supported in Transform Rules expressions.
- Skip or apply logic conditionally when handling [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

For example, to add a header when the subrequest comes from another zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):

```txt
(cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")
```

Selected operation under **Modify request header**: *Set static*

**Header name**: `X-External-Workers-Subrequest`

**Value**: `1`

This gives you more granular control in how you handle incoming requests for your zone.

Learn more in the [Transform Rules](https://developers.cloudflare.com/rules/transform/) documentation and [Rules language fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) reference.

Jun 9, 2025

[<h2>WAF Release - 2025-06-09</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s update spotlights four critical vulnerabilities across CMS platforms, VoIP systems, and enterprise applications. Several flaws enable remote code execution or privilege escalation, posing significant enterprise risks.

**Key Findings**

- WordPress OttoKit Plugin (CVE-2025-27007): Privilege escalation flaw allows unauthenticated attackers to create or elevate user accounts, compromising WordPress administrative control.
- SAP NetWeaver (CVE-2025-42999): Remote Code Execution vulnerability enables attackers to execute arbitrary code on SAP NetWeaver systems, threatening core ERP and business operations.
- Fortinet FortiVoice (CVE-2025-32756): Buffer error vulnerability may lead to memory corruption and potential code execution, directly impacting enterprise VoIP infrastructure.
- Camaleon CMS (CVE-2024-46986): Remote Code Execution vulnerability allows attackers to gain full control over Camaleon CMS installations, exposing hosted content and underlying servers.

**Impact**

These vulnerabilities target widely deployed CMS, ERP, and VoIP systems. RCE flaws in SAP NetWeaver and Camaleon CMS allow full takeover of business-critical applications. Privilege escalation in OttoKit exposes WordPress environments to full administrative compromise. FortiVoice buffer handling issues risk destabilizing or fully compromising enterprise telephony systems.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...0debd86e | 100769 | WordPress OttoKit Plugin - Privilege Escalation - CVE:CVE-2025-27007 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...5f57b448 | 100770 | SAP NetWeaver - Remote Code Execution - CVE:CVE-2025-42999 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...4df8857a | 100779 | Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...3b840107 | 100780 | Camaleon CMS - Remote Code Execution - CVE:CVE-2024-46986 | Log | Block | This is a New Detection |

Jun 9, 2025

[<h2>Workers native integrations were removed from the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/)

[Workers](https://developers.cloudflare.com/workers/)

Workers native integrations were [originally launched in May 2023 ↗︎](https://blog.cloudflare.com/announcing-database-integrations/) to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The **Integrations** tab in the dashboard has been removed in favor of a more direct, command-line-based approach using [Wrangler secrets](https://developers.cloudflare.com/workers/wrangler/commands/general/#secret).

#### What's changed

- **Integrations tab removed**: The integrations setup flow is no longer available in the Workers dashboard.
- **Manual secret configuration**: New connections should be configured by adding credentials as secrets to your Workers using `npx wrangler secret put` commands.

#### Impact on existing integrations

**Existing integrations will continue to work without any changes required.** If you have integrations that were previously created through the dashboard, they will remain functional.

#### Updating existing integrations

If you'd like to modify your existing integration, you can update the secrets, environment variables, or [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) that were created from the original integration setup.

- **Update secrets**: Use `npx wrangler secret put <SECRET_NAME>` to update credential values.
- **Modify environment variables**: Update variables through the dashboard or Wrangler configuration.
- **Dashboard management**: Access your Worker's settings in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) to modify connections created by our removed native integrations feature.

If you have previously set up an observability integration with [Sentry ↗︎](https://sentry.io), the following environment variables were set and are still modifiable:

- `BLOCKED_HEADERS`: headers to exclude sending to Sentry
- `EXCEPTION_SAMPLING_RATE`: number from 0 - 100, where 0 = no events go through to Sentry, and 100 = all events go through to Sentry
- `STATUS_CODES_TO_SAMPLING_RATES`: a map of status codes -- like 400 or with wildcards like 4xx -- to sampling rates described above

#### Setting up new database and observability connections

For new connections, refer to our step-by-step guides on connecting to popular database and observability providers including: [Sentry](https://developers.cloudflare.com/workers/observability/third-party-integrations/sentry), [Turso](https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/), [Neon](https://developers.cloudflare.com/workers/databases/third-party-integrations/neon/), [Supabase](https://developers.cloudflare.com/workers/databases/third-party-integrations/supabase/), [PlanetScale](https://developers.cloudflare.com/workers/databases/third-party-integrations/planetscale/), [Upstash](https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/), [Xata](https://developers.cloudflare.com/workers/databases/third-party-integrations/xata/).

Jun 5, 2025

[<h2>Performance and size optimization for the Cloudflare adapter for Open Next</h2>](https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/)

[Workers](https://developers.cloudflare.com/workers/)

With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans [to improve performance and size ↗︎](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead).

`@opennextjs/cloudflare` v1.2 released on June 5, 2025 delivers on these enhancements. By removing `babel` from the app code and dropping a dependency on `@ampproject/toolbox-optimizer`, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.

This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.

Users only need to update to the latest version of `@opennextjs/cloudflare` to automatically benefit from these improvements.

Note that we published [CVE-2005-6087 ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m) for a SSRF vulnerability in the `@opennextjs/cloudflare` package. The vulnerability has been fixed from `@opennextjs/cloudflare` v1.3.0 onwards. Please update to any version after this one.

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

Jun 3, 2025

[<h2>AI Gateway adds OpenAI compatible endpoint</h2>](https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Users can now use an [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.

To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the `model` and `apiKey` parameters.

*OpenAI SDK Examplejs*

```js
import OpenAI from "openai";
const client = new OpenAI({
	apiKey: "YOUR_PROVIDER_API_KEY", // Provider API key
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
});

const response = await client.chat.completions.create({
	model: "google-ai-studio/gemini-2.0-flash",
	messages: [{ role: "user", content: "What is Cloudflare?" }],
});

console.log(response.choices[0].message.content);
```

Additionally, the [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) can be combined with our [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!

Learn more in the [OpenAI Compatibility](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) documentation.

Jun 3, 2025

[<h2>Improved onboarding for Shopify merchants</h2>](https://developers.cloudflare.com/changelog/post/2025-06-03-shopify-o2o-improvements/)

[DNS](https://developers.cloudflare.com/dns/)

Shopify merchants can now onboard to **O2O** automatically, without needing to contact support or community members.

What's new:

- **Automatic enablement** – O2O is available for all mutual Cloudflare and Shopify customers.
- **Branded record display** – Merchants see a Shopify logo in DNS records, complete with helpful tooltips.![Shopify O2O logo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=848,height=112,format=webp/_astro/shop-dns-icon-o2o.Ca5DAZHL.png)
- **Checkout protection** – Workers and Snippets are blocked from running on the checkout path to reduce risk and improve security.

For more information, refer to the [provider guide](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/).

Jun 3, 2025

[<h2>View an architecture diagram of your Worker directly in the Cloudflare dashboard</h2>](https://developers.cloudflare.com/changelog/post/2025-06-03-visualize-your-worker-architecture/)

[Workers](https://developers.cloudflare.com/workers/)

You can now visualize, explore and modify your Worker’s architecture directly in the Cloudflare dashboard, making it easier to understand how your application connects to Cloudflare resources like [D1 databases](https://developers.cloudflare.com/d1), [Durable Objects](https://developers.cloudflare.com/durable-objects), [KV namespaces](https://developers.cloudflare.com/kv), and [more](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

![Bindings canvas](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2679,height=2042,format=webp/_astro/bindings-canvas.CszRUVlh.png)

With this new view, you can easily:

- Explore existing bindings in a visual, architecture-style diagram
- Add and manage bindings directly from the same interface
- Discover the full range of compute, storage, AI, and media resources you can attach to your Workers application.

To get started, head to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages) and open the **Bindings** tab of any Workers application.

Jun 2, 2025

[<h2>Cloudflare User Groups & Enhanced Permission Policies are now in Beta</h2>](https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're excited to announce the Public Beta launch of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups**, expanding our RBAC capabilities to simplify user and group management at scale.

We've also visually overhauled the **Permission Policies UI** to make defining permissions more intuitive.

**What's New**

**User Groups \[BETA]**: [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups \[BETA]**: Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are deprecated as of 06/02/25. We recommend migrating SCIM Virtual Groups implementations to use [SCIM User Groups](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/). If you did not use Virtual Groups, no action is needed.

**Revamped Permission Policies UI \[BETA]**: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1884,format=webp/_astro/2025-06-02-permissions-policy-ux.2wLEPgVX.png)

Note

When opting into the Beta for User Groups and Permission Policies, you'll be transitioning to a new experience. Please be aware that opting out isn't currently available.

For more info:

- [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
- [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

Jun 2, 2025

[<h2>WAF Release - 2025-06-02</h2>](https://developers.cloudflare.com/changelog/post/2025-06-02-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.

**Key Findings**

- Versa Concerto SD-WAN (CVE-2025-34026, CVE-2025-34027): Authentication bypass vulnerabilities allow attackers to gain unauthorized access to SD-WAN management interfaces, compromising network segmentation and control.
- Kemp LoadMaster (CVE-2024-7591): Remote Code Execution vulnerability enables attackers to execute arbitrary commands, potentially leading to full device compromise within enterprise load balancing environments.
- AnythingLLM (CVE-2024-0759): Server-Side Request Forgery (SSRF) flaw allows external attackers to force the LLM backend to make unauthorized internal network requests, potentially exposing sensitive internal resources.
- Anyscale Ray (CVE-2023-48022): Remote Code Execution vulnerability affecting distributed AI workloads, allowing attackers to execute arbitrary code on Ray cluster nodes.
- Server-Side Request Forgery (SSRF) - Generic & Obfuscated Payloads: Ongoing advancements in SSRF payload techniques observed, including obfuscation and expanded targeting of cloud metadata services and internal IP ranges.

**Impact**

These vulnerabilities expose critical infrastructure across networking, AI platforms, and SaaS integrations. Unauthenticated RCE and auth bypass flaws in Versa Concerto, Kemp LoadMaster, and Anyscale Ray allow full system compromise. AnythingLLM and SSRF payload variants expand attack surfaces into internal cloud resources, sensitive APIs, and metadata services, increasing risk of privilege escalation, data theft, and persistent access.

| Ruleset | Rule ID | Legacy Rule ID | Description | Previous Action | New Action | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| Cloudflare Managed Ruleset | ...39b52f02 | 100764 | Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34027 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...a34edb97 | 100765 | Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34026 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...0d99b2db | 100766 | Kemp LoadMaster - Remote Code Execution - CVE:CVE-2024-7591 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...95aa3a4f | 100767 | AnythingLLM - SSRF - CVE:CVE-2024-0759 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...840a0966 | 100768 | Anyscale Ray - Remote Code Execution - CVE:CVE-2023-48022 | Log | Block | This is a New Detection |
| Cloudflare Managed Ruleset | ...9d16ee18 | 100781 | SSRF - Generic Payloads | N/A | Disabled | This is a New Detection |
| Cloudflare Managed Ruleset | ...5c963d9d | 100782 | SSRF - Obfuscated Payloads | N/A | Disabled | This is a New Detection |

May 30, 2025

[<h2>Cloudflare Pages builds now provide Node.js v22 by default</h2>](https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/)

[Pages](https://developers.cloudflare.com/pages/)

When you use the built-in build system that is part of [Cloudflare Pages](https://developers.cloudflare.com/pages/), the [Build Image](https://developers.cloudflare.com/pages/configuration/build-image/) now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).

If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings > Build & deployments > Build system version in the Cloudflare dashboard for a specific Pages project.

Note that you can always specify a particular version of Node.js or other built-in dependencies by [setting an environment variable](https://developers.cloudflare.com/pages/configuration/build-image/#override-default-versions).

For more, refer to the [developer docs for Cloudflare Pages builds](https://developers.cloudflare.com/pages/configuration/build-image)

May 30, 2025

[<h2>Fine-tune image optimization — WebP now supported in Configuration Rules</h2>](https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/)

[Rules](https://developers.cloudflare.com/rules/)

You can now enable [Polish](https://developers.cloudflare.com/images/polish/activate-polish/) with the `webp` format directly in [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.

**What’s new:**

- [WebP](https://developers.cloudflare.com/images/polish/compression/#webp) is now a supported [value](https://developers.cloudflare.com/rules/configuration-rules/settings/#polish) in the **Polish** setting for Configuration Rules.

This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.

Learn more in the [Polish](https://developers.cloudflare.com/images/polish/) and [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) documentation.

May 30, 2025

[<h2>Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin</h2>](https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/)

[Workers](https://developers.cloudflare.com/workers/)

You can now [debug, profile, view logs, and analyze memory usage for your Worker ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/) using [Chrome Devtools ↗︎](https://developer.chrome.com/docs/devtools) when your Worker runs locally using the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/).

Previously, this was only possible if your Worker ran locally using the [Wrangler CLI ↗︎](https://developers.cloudflare.com/workers/wrangler/), and now you can do all the same things if your Worker uses [Vite ↗︎](https://vite.dev/).

When you run `vite`, you'll now see a debug URL in your console:

```plaintext
  VITE v6.3.5  ready in 461 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  Debug:   http://localhost:5173/__debug
  ➜  press h + enter to show help
```

Open the URL in Chrome, and an instance of Chrome Devtools will open and connect to your Worker running locally. You can then use Chrome Devtools to debug and introspect performance issues. For example, you can navigate to the Performance tab to understand where CPU time is spent in your Worker:

![CPU Profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2144,height=1134,format=webp/_astro/profile.Dz8PUp_K.png)

For more information on how to get the most out of Chrome Devtools, refer to the following docs:

- [Debug code by setting breakpoints](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/)
- [Profile CPU usage](https://developers.cloudflare.com/workers/observability/dev-tools/cpu-usage/)
- [Observe memory usage and debug memory leaks](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/)

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/44/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/44/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
