# Cloudflare One (Protect & Connect)

Snapshot of the Cloudflare developer docs as mirrored on 2026-10-05; everything that moves (plans, limits, versions, beta or GA status) is dated "as of 2026-10-05".
The Protect & Connect > Cloudflare One dropdown on developers.cloudflare.com has twelve entries: Overview, Insights & Logs, Team & Resources, Networks, Access controls, Traffic policies, Cloud & SaaS findings, Email security, Data loss prevention, Browser isolation, Reusable components and Integrations (source: `raw/nav/home-sidebar.md`), all served from `raw/docs/cloudflare-one/` (740 pages, about 13 MB, with eight section-level `llms.txt` files).
Cloudflare One is Cloudflare's SASE platform: identity-aware access to private apps (Access), outbound filtering (Gateway, the Secure Web Gateway), connectors that bring networks and devices onto Cloudflare (Tunnel, Mesh, the Cloudflare One Client formerly WARP, Cloudflare WAN), and data controls (CASB, DLP, Browser Isolation, Email security), all under one dashboard and one seat-based subscription.
The top-level `llms.txt` "Cloudflare One" group also lists Cloudflare Network Firewall, Data Localization Suite and Multi-Cloud Networking, and the "Consumer services" group lists the WARP Client; those are covered in section 18, while Cloudflare Tunnel as a standalone product, Mesh and Cloudflare WAN get their own deep dive in `protect-connect/04-networking.md`.
The Cloudflare One overview page says the platform is "Available on all plans" and that "Cloudflare Zero Trust offers both Free and Paid plans", but the cloudflare-one docs never state the free seat count; the "up to 50 users" free figure appears only in the SASE reference architecture and a blog post (section 2).
For a small team the free plan already covers the core recipe of Cloudflare Tunnel plus Access in front of admin panels, deployer UIs, SSH and internal dashboards, with service tokens for CI (section 19), while Logpush, risk scoring, resolver and egress policies, DLP beyond two profiles, file sandboxing and most network products are Enterprise or paid add-ons.

## Table of contents

1. [Platform map](#1-platform-map)
2. [Plans, pricing and the free tier](#2-plans-pricing-and-the-free-tier)
3. [Account limits](#3-account-limits)
4. [Get started, team name and dashboard](#4-get-started-team-name-and-dashboard)
5. [Insights and Logs](#5-insights-and-logs)
6. [Team and Resources](#6-team-and-resources)
7. [Networks](#7-networks)
8. [Access controls](#8-access-controls)
9. [Traffic policies (Gateway)](#9-traffic-policies-gateway)
10. [Cloud and SaaS findings (CASB)](#10-cloud-and-saas-findings-casb)
11. [Email security](#11-email-security)
12. [Data loss prevention](#12-data-loss-prevention)
13. [Browser isolation](#13-browser-isolation)
14. [Reusable components](#14-reusable-components)
15. [Integrations](#15-integrations)
16. [Roles, API and Terraform](#16-roles-api-and-terraform)
17. [Tutorials, implementation guides and recent changelog](#17-tutorials-implementation-guides-and-recent-changelog)
18. [Related Cloudflare One products](#18-related-cloudflare-one-products)
19. [Small-team recipe: Access and Tunnel for admin panels, deploy keys and dashboards](#19-small-team-recipe-access-and-tunnel-for-admin-panels-deploy-keys-and-dashboards)
20. [Build hooks for Web3 projects](#20-build-hooks-for-web3-projects)
21. [Gaps and contradictions](#21-gaps-and-contradictions)

---

## 1. Platform map

The overview page (last updated Sep 16, 2026) defines Cloudflare One as Cloudflare's Secure Access Service Edge (SASE) platform built on the Zero Trust principle that every request is authenticated and authorized on identity and context ([overview](https://developers.cloudflare.com/cloudflare-one/)).
It lists these products: Access, Cloudflare Tunnel, Cloudflare Mesh, Secure Web Gateway, Cloudflare One Client, Browser Isolation, CASB, DLP, Email security, Digital Experience Monitoring (DEX), Cloudflare WAN, Cloudflare One Appliance, Cloudflare Network Firewall, Multi-Cloud Networking and Data Localization Suite ([overview](https://developers.cloudflare.com/cloudflare-one/)).
The overview also says Enterprise customers can preview the product as a non-contract service with full access free of metered usage fees ([overview](https://developers.cloudflare.com/cloudflare-one/)).

| Sidebar entry | Docs root | What lives there | Status as of 2026-10-05 |
| --- | --- | --- | --- |
| Overview | https://developers.cloudflare.com/cloudflare-one/ | Product map, setup, limits, FAQ, roles, API/Terraform, troubleshooting, tutorials, changelog | "Available on all plans" |
| Insights & Logs | https://developers.cloudflare.com/cloudflare-one/insights/ | Analytics overview, dashboards, DEX, network visibility (packet captures), logs, Logpush | Logpush "Enterprise-only" |
| Team & Resources | https://developers.cloudflare.com/cloudflare-one/team-and-resources/ | Users, seats, SCIM, risk score, devices, Cloudflare One Client, user-side certificates, App Library | Risk score Enterprise-only |
| Networks | https://developers.cloudflare.com/cloudflare-one/networks/ | Connectivity options, Tunnel (SASE use), Mesh, Cloudflare WAN connector, routes, resolvers and proxies, virtual networks | Mesh in beta |
| Access controls | https://developers.cloudflare.com/cloudflare-one/access-controls/ | Applications, policies, AI controls (MCP portals), service credentials, settings, coding agents | MCP portals GA on 2026-09-24 |
| Traffic policies | https://developers.cloudflare.com/cloudflare-one/traffic-policies/ | Gateway DNS, network, HTTP, egress, resolver policies, packet filtering, IDS | Egress and resolver policies Enterprise-only |
| Cloud & SaaS findings | https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/ | CASB findings, remediation policies, DLP scans of SaaS | Free: two integrations |
| Email security | https://developers.cloudflare.com/cloudflare-one/email-security/ | Inbound and outbound email protection (formerly Area 1) | Sales-led purchase, free Retro Scan |
| Data loss prevention | https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/ | Profiles, detection entries, data classification, HTTP and SaaS scanning | "Add-on to Zero Trust Enterprise plans" |
| Browser isolation | https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/ | Remote browser, clientless isolation, isolation policies | "Add-on to Zero Trust Pay-as-you-go and Enterprise" |
| Reusable components | https://developers.cloudflare.com/cloudflare-one/reusable-components/ | Lists, tags, custom pages, posture checks, packet filtering fields | Some custom pages paid only |
| Integrations | https://developers.cloudflare.com/cloudflare-one/integrations/ | Identity providers, CASB integrations, endpoint (service) providers | n/a |

Two naming notes matter when reading older material.
The Cloudflare One Client is "formerly WARP" and still installs `warp-cli`, `warp-diag` and a `warp-svc` daemon ([client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)).
Cloudflare Mesh was "previously known as WARP Connector and peer-to-peer connectivity" ([Mesh](https://developers.cloudflare.com/mesh/)), Cloudflare WAN was "formerly Magic WAN" and Cloudflare Network Firewall was "formerly Magic Firewall" ([Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/), [Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)).

## 2. Plans, pricing and the free tier

As of 2026-10-05 the docs describe three Zero Trust plan tiers by name in different places: "Zero Trust Free", "Pay-as-you-go" (also called "Standard" in limit tables) and "Enterprise" ([account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/), [DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)).
Prices are not in the developer docs; the overview links out to https://www.cloudflare.com/plans/zero-trust-services/ ([overview](https://developers.cloudflare.com/cloudflare-one/)).
Onboarding requires choosing a plan and entering payment details even on the Zero Trust Free plan, where "you will not be charged" ([get started](https://developers.cloudflare.com/cloudflare-one/setup/)).

### The 50-user free plan

No page under `raw/docs/cloudflare-one/` states a free seat count.
The SASE reference architecture says "many of the capabilities described in this document can be used for free, without any time constraints, for up to 50 users" ([SASE reference architecture](https://developers.cloudflare.com/reference-architecture/architectures/sase/)).
A Cloudflare blog post on post-quantum WARP links to the "free zero-trust offering for teams of under 50 users" (`raw/blog/post-quantum-warp.md`).
The "Zero Trust for startups" design guide calls Cloudflare Zero Trust "a simple, (sometimes free!) way for startups" without a number ([startups guide](https://developers.cloudflare.com/reference-architecture/design-guides/zero-trust-for-startups/)).
Treat 50 as the documented free ceiling, with the caveat that the product docs themselves do not repeat it and "up to 50" and "under 50" differ by one (section 21).

### How seats work

A seat is consumed when a user performs an authentication event: any Access login (App Launcher or an application) or any Cloudflare One Client device connecting within the seat-expiration window ([seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/)).
A user holds one seat regardless of how many apps or devices they use, and once all seats are consumed additional users who log in are blocked ([seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/)).
Service tokens do not consume seats, and the docs suggest service tokens or Bypass policies when seat counts exceed real users ([device registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/), [seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/)).
Inactive users are not removed automatically unless you enable seat expiration (one month to one year) under Settings > Admin controls, or deprovision via SCIM ([seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/)).
"Revoke" ends sessions but keeps the seat, "Remove" frees the seat, and user records can never be deleted ([seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/), [getting started FAQ](https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/)).
Publishing an app through Tunnel does not need a paid Access plan; seats are only needed when Access policies protect it ([published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)).
Downgrades apply next billing cycle and upgrades bill immediately ([getting started FAQ](https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/)).

### Plan availability cheat sheet (as of 2026-10-05)

| Feature | Free | Pay-as-you-go / Standard | Enterprise | Source |
| --- | --- | --- | --- | --- |
| Access, Gateway DNS/network/HTTP, Tunnel, Cloudflare One Client | Yes | Yes | Yes | [overview](https://developers.cloudflare.com/cloudflare-one/) |
| Cloudflare Mesh | Yes (beta) | Yes (beta) | Yes (beta) | [Mesh platform](https://developers.cloudflare.com/mesh/platform/) |
| Access for Infrastructure (SSH) | Yes | Yes | Yes | [infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) |
| Access mTLS | No | Yes | Yes | [mTLS](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/) |
| Custom Access block page template, App Launcher customization | No | Yes | Yes | [Access block page](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/) |
| Gateway protocol detection | Yes | Yes | Yes | [Gateway changelog](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/) |
| AV scanning max file size | 15 MB | 25 MB | 100 MB | [AV scanning](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/) |
| CASB | 2 integrations, no finding details | Yes | Yes, finding details | [CASB](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/) |
| DLP | Financial Information and SSN/ID predefined profiles only | Same as Free | Add-on | [DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) |
| Browser Isolation | No | Add-on | Add-on | [RBI](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) |
| DEX tests per account | 10 | 30 | 50 | [account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/) |
| DEX MCP server | Yes | Yes | Yes | [DEX MCP](https://developers.cloudflare.com/cloudflare-one/insights/dex/dex-mcp-server/) |
| Log retention (Access/DNS/HTTP) | 24 hours | 30 days | 180 days Access and DNS, 30 days HTTP and network | [logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/) |
| Logpush | No | No | Yes ("Enterprise-only") | [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) |
| Risk score, User Risk Score selector | No | No | Yes | [risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) |
| Resolver policies, egress policies | No | No | Yes | [resolver](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/), [egress](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/) |
| Dedicated egress IPs, file sandboxing | No | No | Add-on | [dedicated egress](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/), [sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/) |
| Source IP proxy endpoints | No | No | Yes | [connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/) |
| Custom root certificate for TLS inspection | No | No | Yes | [user-side certificates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) |
| Tiered policies (Organizations), Tenant API | No | No | Enterprise (Tenant API for partners) | [tiered policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/) |
| Network Firewall, Cloudflare WAN, CNI, Multi-Cloud Networking, DLS | No | No | Enterprise-only | sections 7 and 18 |

## 3. Account limits

Default limits as of 2026-10-05 (page last updated Sep 4, 2026); "these limits may be increased on Enterprise accounts" by contacting the account team ([account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).

| Area | Limit |
| --- | --- |
| Access applications | 500 |
| Access audit Logpush jobs | 5 |
| Emails per rule / IPs per rule | 1,000 / 1,000 |
| Rule groups / rules per group | 300 / 1,000 |
| mTLS root certificates | 50 |
| Service tokens | 50 |
| Identity providers | 50 |
| Reusable policies | 500 |
| Rules per application / domains per application | 1,000 / 50 |
| Infrastructure targets | 5,000 |
| MCP portals / servers per portal / custom domains per portal | 20 / 80 / 5 |
| MCP portal session inactivity timeout | 24 hours |
| Gateway DNS, network, HTTP, egress, resolver policies | 500 each per account |
| DNS locations / source CIDRs per location | 250 / 1,500 |
| HTTP/2 concurrent streams | 256 |
| PAC files | 50 Standard, 1,000 Enterprise |
| Proxy endpoints | 50 Standard, 500 Enterprise |
| Source IP CIDRs per proxy endpoint | 2,000 |
| Lists / entries per list | 100 / 1,000 Standard, 5,000 Enterprise |
| List API requests | 600 per minute |
| DNS and HTTP Logpush jobs | 5 each |
| DLP custom entries | 25 |
| EDM cells per spreadsheet / dataset cells per account | 100,000 / 1,000,000 |
| Custom Wordlist keywords | 200 per spreadsheet, 1,000 per account |
| `cloudflared` tunnels per account | 1,000 |
| Routes (CIDR + hostname) per account | 1,000, shared between Tunnel and Mesh |
| Active `cloudflared` replicas per tunnel | 25 |
| Virtual networks per account | 1,000 |
| Mesh nodes per account | 50 |
| DEX tests | Free 10, Standard 30, Enterprise 50 |
| DEX remote captures per day | Free 100, Standard 200, Enterprise 800 |
| Active / generated-per-day / custom certificates | 10 / 3 / 5 |
| Gateway API policy expression length | 140,000 characters |
| Team domain and application URL | 63 characters |
| Device profile expression | 10,000 characters |
| Split Tunnel + Local Domain Fallback entries per profile | 1,000 combined |
| Device IP profiles per account | 30 |

Other limits stated outside the limits page: list CSV uploads must be under 2 MB and the list API blocks callers for 120 seconds after exceeding 600 requests per minute ([lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)); Cloudflare Network Firewall allows 200 custom policies by default ([add policies](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/)).

## 4. Get started, team name and dashboard

Prerequisites are a Cloudflare account with two-factor authentication and a Zero Trust organization created under Zero Trust in the dashboard ([get started](https://developers.cloudflare.com/cloudflare-one/setup/)).
The team name becomes `<team-name>.cloudflareaccess.com`, the App Launcher host and the name users type when enrolling devices ([getting started FAQ](https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/)).
A team name can be changed (unless dashboard SSO is on), but deleting the whole Zero Trust organization permanently reserves its team name so no account can reuse it ([getting started FAQ](https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/)).
New organizations get the Cloudflare identity provider as the default login method, and one-time PIN is no longer added automatically ([get started](https://developers.cloudflare.com/cloudflare-one/setup/), [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)).
The guided onboarding at https://one.dash.cloudflare.com offers four use cases: replace your VPN (device to network, device to device, network to network), secure private apps from any browser (private web app, clientless SSH, in-browser RDP), filter DNS, and secure web traffic ([get started](https://developers.cloudflare.com/cloudflare-one/setup/)).
https://help.one.cloudflare.com/ shows whether a device is protected ([getting started FAQ](https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/)).
Implementation guides point to learning paths: secure Internet traffic and SaaS apps, replace your VPN, deploy clientless access, secure your email, and holistic AI security ([implementation guides](https://developers.cloudflare.com/cloudflare-one/implementation-guides/)).

## 5. Insights and Logs

Insights groups the Analytics overview, Analytics dashboards (Access events, Gateway DNS/HTTP/network sessions, Shadow IT SaaS analytics, network sessions, AI security report, Application Access Report, data security), Logs and DEX ([insights](https://developers.cloudflare.com/cloudflare-one/insights/)).
The recommended workflow is dashboards for trends, logs for event-level checks, and DEX for device or network causes ([insights](https://developers.cloudflare.com/cloudflare-one/insights/)).
The AI security report needs Gateway inspecting traffic to AI apps and MCP servers behind Access ([AI security](https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/)).
Shadow IT analytics needs HTTP filtering and syncs review status with the App Library ([Shadow IT](https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/)).

### Dashboard logs and retention

Dashboard logs cover admin activity, Access authentication, Gateway activity (with a PII management page), SSH command logs, SCIM provisioning, posture and tunnel audit logs ([dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)).
SSH command logs are encrypted with a public key you upload and must be downloaded and decrypted locally with the ssh-log-cli tool ([SSH command logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/)).

| Log type | Free | Standard | Access plan | Gateway plan | Enterprise |
| --- | --- | --- | --- | --- | --- |
| Admin | 18 months | 18 months | 18 months | 18 months | 18 months |
| Access | 24 hours | 30 days | 30 days | 24 hours | 180 days |
| DNS | 24 hours | 30 days | 24 hours | 30 days | 180 days (not for per-query Enterprise plans) |
| Network | 24 hours | 30 days | 24 hours | 30 days | 30 days |
| HTTP | 24 hours | 30 days | 24 hours | 30 days | 30 days |
| DEX | 7 days | 7 days | 7 days | 7 days | 7 days |
| Device posture | 30 days | 30 days | 30 days | 30 days | 30 days |

Source: [logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/), as of 2026-10-05.
Log Explorer (beta) can store Zero Trust datasets (`access_requests`, `casb_findings`, `device_posture_results`, `gateway_dns`, `gateway_http`, `gateway_network`, `zero_trust_network_sessions`) in R2 and query them ([logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)).
Logpush to SIEMs or storage is marked "Enterprise-only" and is set up under Insights > Logs > Manage Logpush ([Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)); the R2 tutorial shows R2 as a destination ([R2 logs tutorial](https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/)).
Customer Metadata Boundary from the Data Localization Suite can keep Zero Trust logs in the EU or US ([logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)).

### Digital Experience Monitoring (DEX) and network visibility

DEX uses telemetry from enrolled devices plus optional synthetic HTTP and traceroute tests, device monitoring, remote packet captures, speed tests, notifications and IP visibility ([DEX](https://developers.cloudflare.com/cloudflare-one/insights/dex/)).
The DEX MCP server at `https://dex.mcp.cloudflare.com/mcp` is available on Free, Pay-as-you-go and Enterprise accounts ([DEX MCP](https://developers.cloudflare.com/cloudflare-one/insights/dex/dex-mcp-server/)).
Network visibility adds packet captures to customer cloud storage buckets ([packet captures](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/)).

## 6. Team and Resources

### Users, seats, SCIM

Seat rules are in section 2.
SCIM works with any SAML or OIDC IdP that uses SCIM 2.0; it deprovisions users and supplies group names, but Access still evaluates group membership from the SAML assertion or OIDC token at login, whereas Gateway evaluates identity against the User Registry that SCIM updates continuously ([SCIM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/)).
Zero Trust SCIM does not give dashboard access; that needs a separate dashboard SSO SCIM integration ([SCIM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/)).

### Risk score (Enterprise only)

Risk scoring adds user and entity behavior analytics: each user is Low, Medium or High, equal to the highest-level behavior triggered ([risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)).
Predefined behaviors (all disabled by default) are impossible travel, high number of DLP matches, SentinelOne threat, CrowdStrike low (0 to 50) or medium (50 to 79) ZTA score, interaction with a malicious file, suspicious security domain visited, and high risk domain visited ([risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)).
Scores feed the Access "User Risk Score" selector (example: Allow `@example.com` but Exclude High) and can be sent to Okta as shared signals ([risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)).

### Devices and device registration

A device registration is one Cloudflare One Client session on a physical device with its own public key, device profile and virtual IPs; it never expires until deleted, unlike Access sessions ([device registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/)).
Device enrollment permissions are Access-style policies under Team & Resources > Devices > Device profiles > Management, with login methods and optional instant authentication; device posture checks are not supported in enrollment policies ([device enrollment](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/)).

### Cloudflare One Client (formerly WARP)

The client sends device traffic to Cloudflare over a proxy tunnel using WireGuard or MASQUE, proxies DNS over DoH, and reports device health for posture checks ([client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)).
It ships a GUI, the WARP daemon (`warp-svc`), `warp-cli` and `warp-diag`; Linux logs live in `/var/log/cloudflare-warp/` ([client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)).
It is required for Access for Infrastructure and for reaching private network routes ([client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)).

| Mode | DNS filtering | Network filtering | HTTP filtering | `warp-cli settings` service mode |
| --- | --- | --- | --- | --- |
| Traffic and DNS (default) | Yes | Yes | Yes | `WarpWithDnsOverHttps` |
| DNS only | Yes | No | No | `DnsOverHttps` |
| Traffic only | No | Yes | Yes | `TunnelOnly` |
| Local proxy (MASQUE only, SOCKS5/HTTP on `127.0.0.1:40000`, 10 s request timeout) | No | No | Yes | `WarpProxy on port 40000` |
| Posture only | No | No | No | `PostureOnly` |

Source: [client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/).
Traffic only and Local proxy modes are desktop only (Windows, Linux, macOS) ([client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/)).
MDM configuration files override dashboard device profiles, including the mode ([client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/)).
Configuration areas: client sessions, device IPs, device profiles, managed networks, route traffic (client architecture, Local Domain Fallback, Split Tunnels), device settings, captive portal detection and Emergency Disconnect ([client llms.txt](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/llms.txt)).
Deployment covers manual, MDM (Intune, Jamf, JumpCloud, Kandji, Hexnode, Fleet), hardware-backed registration, client version assignments, PMTUD, protocol-handler registration, switching organizations, multi-user Windows, pre-login and no-internet-until-auth on Windows, and coexistence with legacy VPNs ([client llms.txt](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/llms.txt)).
Headless Linux machines enroll with a service token in a root-only `/var/lib/cloudflare-warp/mdm.xml` containing `auth_client_id`, `auth_client_secret` and `organization` ([headless Linux tutorial](https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/)).
Release channels: beta (no security fix guarantee), stable, and LTS releases that get security fixes for at least 12 months plus 90 days of overlap after the next LTS; mobile platforms ship stable only through app stores ([support lifecycle](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/)).
Latest client releases in the changelog are Windows 2026.8.2033.1 (2026-09-30) and macOS 2026.8.2028.1 (2026-09-29) ([client changelog](https://developers.cloudflare.com/cloudflare-one/changelog/cloudflare-one-client/)).

### User-side certificates

TLS inspection, DLP, AV scanning and Browser Isolation need a root CA on devices; Zero Trust generates one per account, Enterprise can upload a custom one, and the client can install it automatically on desktops ([user-side certificates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/)).
The old default Cloudflare certificate expired on 2025-02-02 at 16:05 UTC ([user-side certificates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/)).

### Application Library

The App Library consolidates SaaS apps across Gateway, Access and CASB, groups "Do Not Inspect" variants, shows review status and exposes application IDs for API and Terraform ([App Library](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/)).

## 7. Networks

### Connectivity options

The connectivity options page is the best single map of on-ramps (into Cloudflare) and off-ramps (to your infrastructure) ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).

| Option | Protocol | Direction | Use when | Plan note |
| --- | --- | --- | --- | --- |
| Cloudflare Tunnel (`cloudflared`) | HTTP/2, QUIC, outbound on port 7844 | Off-ramp only, no server-initiated traffic | Exposing private apps without a public IP | All plans |
| Cloudflare One Client | MASQUE (default), WireGuard | Bidirectional | Remote devices | All plans |
| Cloudflare Mesh | MASQUE | Bidirectional, preserves source IP | Device-to-device, site-to-site, VoIP, long-lived TCP | Beta, includes Free |
| DNS locations | DNS, DoH, DoT | On-ramp | DNS filtering without agents | All plans |
| Proxy endpoints | HTTP/HTTPS via PAC | On-ramp | Web filtering without agents (no UDP, HTTP/3, RBI) | Source IP endpoints Enterprise |
| Clientless Web Isolation | HTTP/HTTPS | On-ramp | Unmanaged devices | Browser Isolation add-on |
| GRE and IPsec tunnels | GRE, IPsec IKEv2 | Bidirectional | Sites with routers and firewalls | Cloudflare WAN subscription |
| Cloudflare One Appliance (formerly Magic WAN Connector) | IPsec | Bidirectional | Zero-touch branches, Dell VEP1460 or ESXi/Proxmox VM | Cloudflare WAN subscription |
| Network Interconnect (CNI) | Direct, Partner, Cloud | Bidirectional | Bypass the public Internet | Enterprise |
| Multi-Cloud Networking | Automated IPsec | Bidirectional | AWS, Azure, GCP VPCs | Cloudflare WAN plus MCN |

Source: [connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/), as of 2026-10-05.
Tunnel hides the client IP from non-HTTP origins (use `CF-Connecting-IP` for HTTP), while Mesh, GRE/IPsec and the Appliance preserve source IPs ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
If CIDRs overlap, Cloudflare Tunnel routes take priority over Cloudflare WAN routes, and there is no automatic failover between different connectivity types ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
Effective MTUs: GRE 1,476 (MSS 1,436 or lower), IPsec 1,400 to 1,436, client behind WAN about 1,300, Mesh to client about 1,280 ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
Mesh and Cloudflare WAN only coexist on Unified Routing, not Legacy routing ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).

### Cloudflare Tunnel inside Cloudflare One

The Cloudflare One copy of the Tunnel docs covers private networking and Zero Trust use, while the standalone https://developers.cloudflare.com/tunnel/ docs cover publishing public applications ([C1 Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)); the core daemon, config file, replicas and limits are in `protect-connect/04-networking.md`.
A tunnel is a persistent UUID object, each `cloudflared` process is a connector, and multiple connectors can serve one tunnel ([C1 Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)).
Because there is no inbound listener, Authenticated Origin Pulls has no effect on tunnel hostnames ([C1 Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)).
`cloudflared` only proxies user-to-server traffic; server-initiated traffic uses the host's routing table ([connect with cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/)).
Private network routes can be IP/CIDR or private hostname routes; hostname routes return an initial resolved IP from `172.64.128.0/20` (a Cloudflare-owned public range, chosen to avoid Chrome's Local Network Access restrictions) and rewrite to the real IP ([private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/)).
Private hostname routing needs client 2025.4.929.0 or later on desktop ([private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/)).
Private network routes are exempt from the CDN video-delivery restriction, so large transfers and backups are allowed there ([private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)).
Virtual networks let overlapping RFC 1918 ranges coexist (1,000 per account) ([virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/), [account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).
Use-case guides cover gRPC, RDP (browser, client-side `cloudflared`, device client), SMB, SSH and VNC in the browser, plus deployment guides for Ansible, AWS, Azure, GCP, Kubernetes and Terraform ([C1 Tunnel llms.txt](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/llms.txt)).
The Tunnels FAQ says WebSockets are fully supported, gRPC works over private subnet routing but not public hostnames, origins never see visitor IPs, and deleted tunnels cannot be restored ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).

#### SSH options compared

| Method | Setup time | Needs | Differentiator |
| --- | --- | --- | --- |
| Client-side `cloudflared` | 15-30 min | `cloudflared` on server and client, Access | No Cloudflare One Client; `ProxyCommand /usr/local/bin/cloudflared access ssh --hostname %h` |
| Access for Infrastructure | 45-60 min | `cloudflared` on server, Cloudflare One Client (or WAN) | Short-lived SSH certificates, per-user UNIX usernames, command logging |
| Self-managed SSH keys | 30-45 min | `cloudflared` on server, Cloudflare One Client | Keep existing keys, network-level policies |
| Browser-rendered terminal | 20-30 min | `cloudflared` on server, Access | No SSH client or device client |

Source: [SSH](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/), [client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/).
Access for Infrastructure needs a Cloudflare SSH CA (`POST /accounts/$ACCOUNT_ID/access/gateway_ca`) trusted via `TrustedUserCAKeys /etc/ssh/ca.pub` in `sshd_config`; it supports `scp`, `sftp` and `rsync` but not port forwarding, `ProxyJump`, agent forwarding or X11, and sessions have a maximum expected duration of 10 hours ([SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/)).
Older short-lived CAs from the legacy short-lived certificates feature are incompatible with the Gateway SSH proxy ([SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/)).

### Cloudflare Mesh (beta)

Mesh gives every enrolled server, laptop and phone a Mesh IP from `100.96.0.0/12` and lets any participant reach any other over TCP, UDP or ICMP through Cloudflare, with Mesh nodes running the Cloudflare One Client headless on Linux and optionally advertising CIDR or hostname routes ([Mesh concepts](https://developers.cloudflare.com/mesh/concepts/)).
It is in beta for Cloudflare One accounts including Free, nodes must use MASQUE, and accounts are limited to 50 Mesh nodes ([Mesh platform](https://developers.cloudflare.com/mesh/platform/), [account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).
Full coverage is in `protect-connect/04-networking.md`.

### Cloudflare WAN connector pages

`raw/docs/cloudflare-one/networks/connectors/cloudflare-wan/` mirrors the Cloudflare WAN product docs (Appliance, third-party IPsec/GRE device guides, security filters, Cloudflare One integration, CNI, load balancing, analytics, troubleshooting, reference) ([Networks llms.txt](https://developers.cloudflare.com/cloudflare-one/networks/llms.txt)); see `protect-connect/04-networking.md`.
Granular permissions can scope members to individual tunnels and Mesh nodes ([granular permissions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/)).

### Routes, resolvers and proxies

Routes pages cover adding routes, reserved IP addresses and the configurable initial resolved IP range ([add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/), [reserved IPs](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/)).
DNS locations accept plain IPv4/IPv6, DoH and DoT; identity-based DNS without the client uses DoH with user tokens, and resolving internal names needs resolver policies (Enterprise) ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/), [DoH](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/)).
Proxy endpoints come as authorization endpoints (Access identity) or source IP endpoints (Enterprise), configured with PAC files ([proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/)).

## 8. Access controls

### Application types

| Type | Protects | Needs client | Notes |
| --- | --- | --- | --- |
| Self-hosted | Public hostnames on Cloudflare DNS (full or partial CNAME), private IPs/hostnames/CIDRs with ports, Workers by name including preview deployments | Only for private destinations | Full policy engine, app tokens, `cloudflared access` CLI login |
| SaaS | Third-party apps via SAML or OIDC, with Access as SSO | No | Enforced at sign-on and session reissue only |
| Infrastructure | SSH targets by hostname or tag | Yes | Protocol-aware authz (ports, usernames), command logs, short-lived certificates, all plans |
| Bookmark | Links in the App Launcher | No | Not protected by Access |
| Private network app (legacy) | Private IPs via generated Gateway rules | Yes | Deprecated for new customers |

Source: [choose an application type](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/choose-application-type/).
The SaaS catalogue has 35 app guides (generic OIDC and SAML, AWS, GitHub Enterprise Cloud, Google Workspace and Cloud, Grafana and Grafana Cloud, Slack, Salesforce, Zoom and more) ([Access llms.txt](https://developers.cloudflare.com/cloudflare-one/access-controls/llms.txt)).
Creating a public self-hosted app: Access controls > Applications > Create new application > Self-hosted and private > Add public hostname, attach policies, pick IdPs (optionally instant authentication and "Authenticate with Cloudflare One Client"), optional independent MFA, session duration, and optional 401 for Service Auth ([self-hosted public app](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)).
Create the Access application before the tunnel route, otherwise the published app is open to the Internet ([self-hosted public app](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)).
Automatic Platform Optimization, Zaraz and Google tag gateway are not supported on Access self-hosted apps ([self-hosted public app](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)).

### Policies

Each policy has one action (Allow, Block, Bypass, Service Auth), rule types (Include = OR, Require = AND, Exclude = NOT, at least one Include), selectors and values ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
Access is deny by default; Bypass disables enforcement and logging and cannot use identity selectors, and Cloudflare recommends Service Auth instead when you need logging ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
Evaluation order: Service Auth and Bypass first (top to bottom), then Allow and Block in order, stopping at the first Allow or Block match ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
Selectors include Emails, Emails ending in, External Evaluation, IP ranges, Country, Everyone, Common Name, Valid Certificate, Service Token, Any Access Service Token, User Risk Score (Enterprise), Linked App Token, Login Methods, Authentication Method, IdP group, SAML Group, OIDC Claim, Device posture, Warp, Gateway and Cloudflare Account Member; non-identity selectors are re-checked on every request ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
The two documented misconfigurations that open an app to anyone are "Include Everyone" and "Include Login Methods: One-time PIN" in an Allow policy ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
Extra policy features: rule groups, purpose justification, temporary authentication with approver emails (grants up to 24 hours), External Evaluation, isolate application, application paths, MFA requirements ([temporary auth](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/), [Access policies llms.txt](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/llms.txt)).

### Sessions and tokens

Login creates a global session token on the team domain and an application token per app; global duration is 15 minutes to one month (default 24 hours), app and policy durations range from immediate to one month (default 24 hours) ([session management](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/)).
Precedence is client session, then policy, then application, then global ([session management](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/)).
Logout is `<app-domain>/cdn-cgi/access/logout` or `<team>.cloudflareaccess.com/cdn-cgi/access/logout`, revoked users cannot log in again for up to 1 minute, and AJAX calls with `X-Requested-With: XMLHttpRequest` get a 401 on expiry ([session management](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/)).
Origins should validate the `Cf-Access-Jwt-Assertion` header (not the `CF_Authorization` cookie) against keys at `https://<team>.cloudflareaccess.com/cdn-cgi/access/certs`, matching `kid` in `public_certs` and checking the application AUD tag; keys rotate every 6 weeks and old keys stay valid 7 days ([validate JWTs](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/)).
`cloudflared` can validate the JWT for you with the origin parameter `access: {required: true, teamName, audTag}` ("Protect with Access") ([origin parameters](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/)).

### Service credentials

Service tokens are a Client ID and Client Secret sent as `CF-Access-Client-Id` and `CF-Access-Client-Secret`, matched by a Service Auth policy; the secret is shown once ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
Create them in the dashboard, with `POST /accounts/$ACCOUNT_ID/access/service_tokens` (`{"name","duration":"8760h"}`), or Terraform `cloudflare_zero_trust_access_service_token` with `create_before_destroy` ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
Since August 26, 2026 new secrets use the `cfast_` prefix plus a checksum so secret scanners can find them, and old 64-hex secrets keep working ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
A self-hosted app can read the token from one header (`read_service_tokens_from_header`, for example `Authorization`) ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
Strict service token authentication returns 401 or 403 instead of a 302, ignores Allow policies and cookies for token requests and issues no cookie; organizations created on or after October 5, 2026 have it on and cannot turn it off ([Access changelog 2026-10-02](https://developers.cloudflare.com/cloudflare-one/changelog/access/)).
Inactive service tokens can now be managed automatically (2026-09-22) ([Access changelog](https://developers.cloudflare.com/cloudflare-one/changelog/access/)).
Mutual TLS needs Pay-as-you-go or Enterprise ([mTLS](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/)).

### Settings, MFA, agents, MCP

"Require Access protection" blocks every hostname in the account that lacks an Access application, returning `Error 1050`, with optional exempt hostnames ([require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/)).
Independent MFA supports TOTP (one per user), WebAuthn security keys, biometrics, and for infrastructure apps only YubiKey PIV (firmware 4.3+) and FIDO2 keys, with optional AAGUID restrictions via lists ([independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/), [lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)).
Managed OAuth turns Access into an OAuth 2.0 authorization server for non-browser clients (RFC 8707 clients) ([managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/)).
Coding agents authenticate with `cloudflared access curl <url>`, `cloudflared access login <url>` tokens, or service tokens for headless runs ([authenticate coding agents](https://developers.cloudflare.com/cloudflare-one/access-controls/authenticate-agents/)).
MCP server portals put many MCP servers behind one Access-protected endpoint with tool curation, aliases, Code Mode in Dynamic Workers, optional Gateway routing for DLP, and support stateless MCP `2026-07-28` and 2025 Streamable HTTP; they became GA on 2026-09-24 ([MCP portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), [Access changelog](https://developers.cloudflare.com/cloudflare-one/changelog/access/)).
Access emits Queues event subscriptions such as `cf.access.application.created` ([event subscriptions](https://developers.cloudflare.com/cloudflare-one/access-controls/event-subscriptions/)).

## 9. Traffic policies (Gateway)

Gateway is the Secure Web Gateway, filtering at DNS, network (L4 FWaaS) and HTTP (L7 forward proxy with TLS decryption) layers, plus egress and packet filtering ([traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)).
The recommended rollout is DNS filtering, then network policies, then HTTP inspection, then egress and full integration ([get started](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/)).

### Order of enforcement

Gateway applies DNS policies evaluated before resolution, resolver policies, DNS policies evaluated after resolution, egress policies, network policies, then HTTP policies ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).
DNS blocks are standalone, so a user who knows the IP can still reach a DNS-blocked site unless an HTTP or network policy also blocks it ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).
Since 2025-07-14 network-level policies run before application-level ones, and a network Block no longer shows the HTTP block page ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).
Unmatched traffic is allowed by default in all three builders, so a default-deny posture needs a catch-all Block at the lowest precedence; Do Not Inspect policies run before all other HTTP policies ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).
Gateway sends a TCP SYN to the origin before evaluating policies; only Cloudflare Network Firewall (Enterprise) can stop that SYN ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).

### DNS policies

Actions are Allow (optionally disabling DNSSEC validation), Block (custom block page, client notifications), Override, Safe Search and YouTube Restricted Mode ([DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)).
Selectors include Application, Authoritative Nameserver IP, Content and Security Categories, CNAME/MX/PTR/TXT record, DoH subdomain, Domain (matches subdomains, `any(dns.domains[*] == "example.com")`), Host (exact, `dns.fqdn == "example.com"`), Indicator Feeds (`dns.indicator_feed`), Location, query type, resolved IP/country/continent, source IP/country, and Users ([DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)).
Rules are created with `POST /accounts/$ACCOUNT_ID/gateway/rules` using wirefilter traffic expressions such as `any(dns.domains[*] in $<LIST_UUID>)` ([DNS common policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/common-policies/)).
Timed DNS policies and a maximum DNS TTL setting also exist ([Gateway llms.txt](https://developers.cloudflare.com/cloudflare-one/traffic-policies/llms.txt)).

### Domain categories

Security categories: Anonymizer, Brand Embedding, Command and Control & Botnet, Compromised Domain, Cryptomining, DGA Domains, DNS Tunneling, Malware, Phishing, Potentially Unwanted Software, Private IP Address, Scam, Spam, Spyware ([domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/)).
Security risk subcategories: New Domains (registered in the past 30 days), Newly Seen Domains (first resolved in the past 30 days), Parked & For Sale Domains ([domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/)).
"Cryptocurrency" is a content subcategory (ID 183 under Business & Economy), separate from the "Cryptomining" security category (ID 83) ([domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/)).
Categorization combines Cloudflare network data, 30+ open-source and commercial feeds (Avira, Zvelo), ML models and community feedback; Terraform can look categories up with the `cloudflare_zero_trust_gateway_categories_list` data source ([domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/)).
Publicly available indicator feeds for all Gateway users are the UK NCSC Public Threat Indicators (feed 24) and the Cloudforce One Public Feed (feed 34), plus the Treasury feed for eligible institutions ([indicator feeds](https://developers.cloudflare.com/security-center/indicator-feeds/)).

### Network, HTTP and egress policies

Network policies match IPs, ports, protocol, detected protocol, SNI and SNI domain, device posture, users and virtual network, with Allow, Block and Network Override actions ([network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)).
HTTP actions are Allow, Block, Redirect, Isolate, Do Not Inspect, Do Not Isolate, Do Not Scan and Quarantine; selectors include Access Infrastructure Target, Access Private App, application and granular controls, DLP Profile, Is MCP (beta), file types and sizes, package ecosystem/name/namespace/PURL/version, security risks, URL and virtual network ([HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)).
TLS decryption is enabled under Traffic policies > Traffic settings or `tls_decrypt` in `cloudflare_zero_trust_gateway_settings`, needs a user-side certificate, and decrypts in memory only ([TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/)).
Package registry security (added 2026-08-13) detects npm, PyPI, RubyGems, Cargo, Go, Maven and NuGet downloads by URL structure, works for mirrors and proxies, needs TLS decryption, and fails open ([package registry security](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/package-registry-security/)).
AV scanning limits are 15 MB Free, 25 MB Pay-as-you-go and 100 MB Enterprise, and file sandboxing is an Enterprise add-on ([AV scanning](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/), [file sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/)).
Egress policies (Enterprise) choose egress IPs, dedicated egress IPs are an Enterprise add-on, and "egress through Cloudflare Tunnel" lets client traffic exit via a `cloudflared` host whose IP is already allowlisted by a third party ([egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/), [egress through Tunnel](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/)).
Resolver policies (Enterprise) send matching queries to custom or private resolvers ([resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/)).
Packet filtering in the Gateway section is Cloudflare Network Firewall ("Enterprise-only") including rate limiting policies (beta), managed rulesets, protocol validation and IDS ([packet filtering overview](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/network-firewall-overview/)).
Recent Gateway changes: Traffic Destination selector (2026-09-23), replica identification for Mesh, Workers VPC and Tunnel in network logs (2026-09-29), RBAC for Browser Isolation policies (2026-09-30) ([Gateway changelog](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/)).

## 10. Cloud and SaaS findings (CASB)

CASB connects read-only to SaaS and cloud APIs to find misconfigurations, overshared data and risky users after login; it is "available for all Zero Trust users", Free accounts get up to two integrations, and finding instance details need Enterprise ([CASB](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/)).
Scans run roughly every 1 to 24 hours, findings can trigger remediation policies or webhooks, and DLP can scan stored files ([CASB](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/), [remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/)).
Integrations documented as of 2026-10-05: Anthropic, Atlassian Confluence and Jira, AWS S3, Bitbucket Cloud, Box, Dropbox, GCP Cloud Storage, GitHub, Google Workspace (Gmail, Drive, Calendar, Admin, Gemini, with FedRAMP variants), Microsoft 365 (Admin Center, Copilot, OneDrive, Outlook, SharePoint, with FedRAMP variants), OpenAI, Salesforce, ServiceNow and Slack ([CASB llms.txt](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/llms.txt)).
The GitHub integration flags missing default-branch protection, no required PR review, force pushes allowed, stale approvals, no admin restrictions or status checks, default WRITE permission, repos idle 12+ months, and organization or member 2FA disabled ([GitHub CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/github/)).

## 11. Email security

Email security (formerly Area 1) analyzes inbound mail for phishing, malware and Business Email Compromise and can be deployed post-delivery (Microsoft Graph API, BCC or journaling) or pre-delivery (MX/Inline) ([Email security](https://developers.cloudflare.com/cloudflare-one/email-security/), [before you begin](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)).
Microsoft 365 supports API and MX, Google Workspace supports BCC and MX, other providers MX only; post-delivery remediation uses auto-moves while MX/Inline can block, quarantine or modify messages ([before you begin](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)).
Dispositions are Malicious, Spam (header `UCE`), Bulk, Suspicious and Spoof, written to `X-CFEmailSecurity-Disposition` ([dispositions](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/)).
Retro Scan is a free, Microsoft 365 only scan of up to 14 days of mail listing up to 1,000 flagged emails ([Retro Scan](https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/)).
PhishGuard adds a human analyst team, works post-delivery only and requires auto-moves ([PhishGuard](https://developers.cloudflare.com/cloudflare-one/email-security/phishguard/)).
Blocked content rules are Enterprise and Enterprise plus PhishGuard only, and the purchase path is "Contact Sales" ([blocked content](https://developers.cloudflare.com/cloudflare-one/email-security/policies/inbound/blocked-content/)).
Other features: impersonation registry, link actions, text add-ons (MX/Inline only), trusted domains, outbound DLP (Microsoft 365), PhishNet for Microsoft 365 and Google Workspace, regional processing (MX/Inline or BCC/Journaling), and an Email security API ([Email security llms.txt](https://developers.cloudflare.com/cloudflare-one/email-security/llms.txt)).
Post-quantum key exchange for MX deployments arrived on 2026-08-17 ([Email security changelog](https://developers.cloudflare.com/cloudflare-one/changelog/email-security/)).

## 12. Data loss prevention

DLP is "available as an add-on to Zero Trust Enterprise plans", while Free and Pay-as-you-go can use the Financial Information and Social Security, Insurance, Tax and Identifier Numbers predefined profiles ([DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)).
It scans HTTP bodies (not headers) through Gateway with TLS decryption, SaaS files at rest through CASB, AI Gateway prompts and responses, and outbound Microsoft 365 email; scanned content is held in memory only, with optional payload logging encrypted to your own public key ([DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/), [DLP settings](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/)).
Building blocks are profiles (predefined, custom, integration), detection entries, and data classification classes with labels and templates ([DLP llms.txt](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/llms.txt)).
Predefined profiles are AI Prompt, Credentials and Secrets, Financial Information, Health Information, HAR files, PII Record, SSN/ID numbers and Source Code ([predefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/)).
Predefined detection entries include Bitcoin Wallet and Ethereum Wallet addresses, SSH Private Key, AWS/Azure/GCP keys, GitHub PAT (`ghp_`), npm (`npm_`) and PyPI (`pypi-`) tokens, OpenAI keys (`sk-proj-`), Slack and Stripe keys, Cloudflare tokens (`cfk_`, `cfut_`, `cfat_`) and unsanitized HAR files ([predefined detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/)).
No seed phrase (BIP-39 mnemonic), raw hex private key or Solana address entry appears in the docs as of 2026-10-05, so those would need custom entries (25 per account) or wordlists ([predefined detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/), [account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).
Recent additions: test scans without sending traffic (2026-08-21) and Passive Detection on sampled traffic before writing policies (2026-09-14) ([DLP changelog](https://developers.cloudflare.com/cloudflare-one/changelog/dlp/)).

## 13. Browser isolation

Remote Browser Isolation runs page code in a remote browser and streams draw commands, is an add-on to Pay-as-you-go and Enterprise, and is configured with Gateway HTTP Isolate and Do Not Isolate actions ([RBI](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)).
Isolation policy settings can disable copy, paste, file downloads, file uploads, keyboard input and printing, with common policies for security threats, high-risk content, news, uncategorized content and ChatGPT ([isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)).
Clientless Web Isolation serves `https://<team-name>.cloudflareaccess.com/browser/<URL>` after Access login, for unmanaged devices ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
Canvas Remoting is on by default for all isolation customers ([Canvas Remoting](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/canvas-remoting/)).

## 14. Reusable components

Lists hold URLs, hostnames, serial numbers, user emails, IPs, device IDs or AAGUIDs, can be uploaded as CSV, are limited to 1,000 entries (Standard) or 5,000 (Enterprise), and hostname lists do not accept wildcards like `*.example.com` ([lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)).
Zero Trust lists are distinct from WAF account-level custom lists ([lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)).
Custom pages cover the Gateway block page, App Launcher customization, Access login page and Access block pages, the latter two customizations being Pay-as-you-go and Enterprise only ([App Launcher customization](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/app-launcher-customization/)).
Client posture checks: antivirus, application, Carbon Black, client certificate, serial numbers, device UUID, disk encryption, domain joined, file, firewall, OS version, Require Gateway, Require WARP, SentinelOne and Tanium (legacy), plus Access integrations ([posture checks llms.txt](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/llms.txt)).
Tags and a packet-filtering fields reference also live here ([tags](https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/), [packet filtering fields](https://developers.cloudflare.com/cloudflare-one/reusable-components/packet-filtering-fields/)).

## 15. Integrations

Identity providers: Cloudflare (default), one-time PIN, generic OIDC, generic SAML 2.0, IdP federation across accounts, Active Directory (SAML), Amazon Cognito, AWS IAM (SAML), Centrify, Citrix ADC, Facebook, GitHub, Google, Google Workspace, JumpCloud, Keycloak, LinkedIn, Microsoft Entra ID, Okta, OneLogin, PingFederate, PingOne, signed AuthN requests and Yandex ([integrations llms.txt](https://developers.cloudflare.com/cloudflare-one/integrations/llms.txt)).
GitHub login needs only a GitHub OAuth app whose homepage is the team domain, and does not need a GitHub organization ([GitHub IdP](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/)).
OTP lets outside collaborators in without an IdP ([one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)).
Endpoint (service provider) posture integrations: custom, CrowdStrike, Kolide, Microsoft Endpoint Manager, SentinelOne, Tanium, Uptycs and Workspace ONE ([integrations llms.txt](https://developers.cloudflare.com/cloudflare-one/integrations/llms.txt)).

## 16. Roles, API and Terraform

Roles: Super Administrator, Cloudflare Zero Trust (all products except billing edit), Access, Gateway, Zero Trust Read Only, Reporting, DNS Locations Write, DEX, CASB Read and CASB, plus the add-on Zero Trust PII role; PII in Access logs is always visible ([roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/)).
Super Administrators can set the dashboard read-only so that all changes go through the API or Terraform ([API and Terraform](https://developers.cloudflare.com/cloudflare-one/api-terraform/)).
Terraform resources seen in these docs include `cloudflare_zero_trust_access_application`, `cloudflare_zero_trust_access_policy`, `cloudflare_zero_trust_access_service_token`, `cloudflare_zero_trust_gateway_settings`, `cloudflare_zero_trust_tunnel_cloudflared`, `cloudflare_zero_trust_tunnel_cloudflared_config`, `cloudflare_zero_trust_tunnel_cloudflared_route` and the categories data source ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/), [Tunnel Terraform guide](https://developers.cloudflare.com/tunnel/guides/terraform/)).

## 17. Tutorials, implementation guides and recent changelog

Tutorials as of 2026-10-05: GraphQL analytics for Network Firewall, detect MCP traffic in Gateway logs, clientless access via private DNS, MySQL behind Tunnel with network policies, `cloudflared` CLI access, kubectl, AI agent wrapper with AI Gateway, custom headers with Workers, headless Linux client, regional private DNS, Microsoft MCAS, risky Entra ID users, MongoDB SSH, Grafana for Tunnel, S3 buckets, M365 dedicated egress, Okta U2F, SSO attributes via Workers, R2 as log destination, Tunnel with client-go credential plugins, Entra Conditional Access, user-selectable egress IPs, FastAPI JWT validation, and GitLab ([C1 llms.txt](https://developers.cloudflare.com/cloudflare-one/llms.txt)).
The `cloudflared access token -app=<url>` command plus header `cf-access-token` lets scripts call Access-protected APIs ([CLI tutorial](https://developers.cloudflare.com/cloudflare-one/tutorials/cli/)).

| Product changelog | Latest entries (as of 2026-10-05) |
| --- | --- |
| Access | 2026-10-02 strict service token authentication; 2026-10-01 simpler target tagging; 2026-09-24 MCP portals GA; 2026-09-22 inactive service token management |
| Gateway | 2026-09-30 RBAC for isolation policies; 2026-09-29 replica identification in network logs; 2026-09-23 Traffic Destination selector; 2026-08-13 package registry security |
| Tunnel | 2026-10-02 Quick Tunnels with email auth; 2026-09-18 32-bit Windows and Intel macOS builds deprecated in 2027; 2026-09-02 bulk route creation |
| Cloudflare One Client | 2026-09-30 Windows 2026.8.2033.1; 2026-09-29 Windows and macOS 2026.8.2028.1 |
| CASB | 2026-09-09 Zoom integration; 2026-08-21 API remediation for M365 and Google Workspace; 2026-05-19 Claude Compliance API |
| DLP | 2026-09-14 Passive Detection; 2026-08-21 test scan |
| Browser Isolation | 2026-09-30 RBAC; 2026-09-09 iOS tap-to-type |
| Email security | 2026-08-17 post-quantum MX; 2026-08-12 blocked content rules |
| Network Firewall | 2026-09-25 managed rulesets in Unified Routing; 2026-08-19 threat intel lists in Unified Routing |
| DEX | latest 2026-07-09 |
| Risk score | latest 2026-04-08 |

Source: [changelog](https://developers.cloudflare.com/cloudflare-one/changelog/) and per-product pages.

## 18. Related Cloudflare One products

### Cloudflare Network Firewall (formerly Magic Firewall)

Enterprise-only firewall-as-a-service that filters packets at Cloudflare's edge with the Wireshark-inspired Rules language, available with Magic Transit or Cloudflare WAN ([Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)).
Standard features: protocol, port, IP, packet length and bit-field rules, sub-minute propagation, API and Terraform, per-rule analytics ([plans](https://developers.cloudflare.com/cloudflare-network-firewall/plans/)).
Advanced features: custom and managed threat-intel IP lists, country and ASN rules, on-demand packet captures, protocol validation, Gateway SWG for outbound traffic, and IDS ([plans](https://developers.cloudflare.com/cloudflare-network-firewall/plans/)).
Rules are managed under Cloudflare One > Firewall policies > Custom policies, 200 by default ([add policies](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/)).
With proxied services like CDN and Spectrum, source-IP rules may not behave as expected because rules run after Cloudflare terminates TCP, and fragments are reassembled before inspection ([about](https://developers.cloudflare.com/cloudflare-network-firewall/about/)).
Unified Routing drops `ip.geoip.country` (use `ip.src.country`/`ip.dst.country`) and changes IPv6 and L4 rule matching ([Unified Routing changes](https://developers.cloudflare.com/cloudflare-network-firewall/about/unified-routing-changes/)).
IDS is beta on WAN with Unified Routing and unavailable for Magic Transit on Unified Routing ([IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/)).

### Data Localization Suite

An "Enterprise-only paid add-on" with three parts: Geo Key Manager (where TLS private keys live), Customer Metadata Boundary (logs and analytics stay in the EU or US), and Regional Services (which data centers decrypt and process HTTPS) ([DLS](https://developers.cloudflare.com/data-localization/), [region support](https://developers.cloudflare.com/data-localization/region-support/)).
Regional Services still accepts traffic anywhere and applies L3/L4 DDoS mitigation globally, but terminates TLS only in-region ([Regional Services](https://developers.cloudflare.com/data-localization/regional-services/)).
For Zero Trust: Gateway regionalization only applies in Traffic and DNS mode, DNS filtering cannot be regionalized, custom certificates cannot be region-restricted yet, `cloudflared --region` is independent of Regional Services, and DEX supports the EU metadata boundary ([DLS Zero Trust](https://developers.cloudflare.com/data-localization/how-to/zero-trust/), [DEX](https://developers.cloudflare.com/cloudflare-one/insights/dex/)).

### Multi-Cloud Networking (formerly Magic Cloud Networking)

"Enterprise-only" and in closed beta (sign-up form), it discovers VPCs, subnets, VMs and routes in AWS, Azure and GCP and builds VPN on-ramps to Cloudflare WAN, with AWS hub (Transit Gateway) support and downloadable Terraform (`main.tf` plus `instructions.txt`) ([MCN](https://developers.cloudflare.com/multi-cloud-networking/), [cloud on-ramps](https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/)).
It needs a Cloudflare WAN account, uses the cloud provider's own VPN gateways (billed by the provider), takes 15 to 45 minutes to provision, and rejects personal Microsoft accounts ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/), [get started](https://developers.cloudflare.com/multi-cloud-networking/get-started/)).

### WARP Client (consumer 1.1.1.1 with WARP)

The consumer WARP client is "Available on all plans" and separate from the Cloudflare One Client used for Zero Trust ([WARP Client](https://developers.cloudflare.com/warp-client/)).
Modes: DNS only (formerly 1.1.1.1, DoH or DoT), Traffic and DNS (formerly 1.1.1.1 with WARP, over MASQUE with UDP, DoT or DoH DNS), Traffic only, and Local proxy (desktop, HTTPS or SOCKS5) ([WARP modes](https://developers.cloudflare.com/warp-client/warp-modes/)).
WARP "does not provide anonymity" and cannot spoof country; WebRTC (camera, microphone) bypasses it ([WARP modes](https://developers.cloudflare.com/warp-client/warp-modes/), [FAQ](https://developers.cloudflare.com/warp-client/known-issues-and-faq/)).
WARP+ Unlimited is a monthly App Store or Play Store subscription usable on up to five devices; Linux registers it with `warp-cli registration license <KEY>` ([WARP modes](https://developers.cloudflare.com/warp-client/warp-modes/), [Linux](https://developers.cloudflare.com/warp-client/get-started/linux/)).
Linux basics: `warp-cli registration new`, `warp-cli connect`, verify `warp=on` at `https://www.cloudflare.com/cdn-cgi/trace`, `warp-cli mode doh` or `warp+doh`, `warp-cli tunnel protocol set MASQUE|WireGuard`, and 1.1.1.1 for Families via `warp-cli dns families off|malware|full` ([Linux](https://developers.cloudflare.com/warp-client/get-started/linux/)).
Post-quantum needs Android 2.4.3, iOS 1.11.1 or desktop 2025.6.1335.0 or later ([WARP modes](https://developers.cloudflare.com/warp-client/warp-modes/)).
System requirements as of 2026-10-05: Android 5.0+, iOS 15+, macOS Sequoia 15.1+ (8 GB RAM), Windows 10 LTSC or 11 with .NET 4.7.2, and Linux RHEL 9/10, Debian 12/13, Fedora 43/44, Ubuntu 22.04/24.04/26.04 on x86-64 or ARM64 ([get started](https://developers.cloudflare.com/warp-client/get-started/)).

## 19. Small-team recipe: Access and Tunnel for admin panels, deploy keys and dashboards

Every step below is on the free plan unless marked, and each cites the page that documents it.

1. Create the Zero Trust organization and pick a team name, choosing the Free plan ([get started](https://developers.cloudflare.com/cloudflare-one/setup/)).
2. Add a login method: GitHub (only an OAuth app is needed) or Google, plus one-time PIN for contractors ([GitHub IdP](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/), [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)).
3. Turn on "Require Access protection" so any new hostname without an Access app is blocked with `Error 1050`, exempting only the public marketing site ([require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/)).
4. Create an Access self-hosted application for each internal hostname (for example `admin.example.com`, `deployer.example.com`, `grafana.example.com`) before adding any tunnel route ([self-hosted public app](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)).
5. Attach a reusable Allow policy such as Include "Emails" (named teammates) with Require "Login Methods" GitHub, and add independent MFA with security keys for the deployer app ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/), [independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/)).
6. Avoid "Include Everyone" and "Include Login Methods: One-time PIN" in Allow policies, which open the app to anyone ([policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)).
7. For a production deploy panel, add temporary authentication with purpose justification so each session needs an approver, up to 24 hours ([temporary authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/)).
8. Install `cloudflared` on the host as a remotely managed tunnel and add published application routes from those hostnames to `http://localhost:<port>`, keeping all inbound ports closed and only outbound 7844 open ([Tunnel get started](https://developers.cloudflare.com/tunnel/get-started/), [Tunnel configuration](https://developers.cloudflare.com/tunnel/configuration/)).
9. Enable "Protect with Access" on each route (`access.required: true`, `teamName`, `audTag`) or validate `Cf-Access-Jwt-Assertion` in the app, so traffic that somehow bypasses Access is rejected ([origin parameters](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/), [validate JWTs](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/)).
10. For CI and bots that must call these apps or a deploy webhook, create a service token per pipeline and a Service Auth policy, send `CF-Access-Client-Id` and `CF-Access-Client-Secret`, and store the `cfast_` secret in the CI secret store; service tokens consume no seats ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
11. For SSH to deploy hosts, use Access for Infrastructure with short-lived certificates and SSH command logging so no long-lived deploy SSH keys sit on laptops, or browser-rendered SSH for quick fixes ([SSH](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/), [SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/)).
12. For databases or internal APIs that are not HTTP, publish them as private network routes and reach them with the Cloudflare One Client, controlled by Gateway network policies ([MySQL tutorial](https://developers.cloudflare.com/cloudflare-one/tutorials/mysql-network-policy/), [connect an IP/CIDR](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/)).
13. Give coding agents access via `cloudflared access curl` under the developer's own identity, or a dedicated service token for headless agents ([authenticate coding agents](https://developers.cloudflare.com/cloudflare-one/access-controls/authenticate-agents/)).
14. Keep the free tier's 24-hour log retention in mind; Logpush to keep audit trails longer is Enterprise-only ([logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/), [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)).
15. Manage it all in Terraform and optionally lock the dashboard read-only ([API and Terraform](https://developers.cloudflare.com/cloudflare-one/api-terraform/), [Tunnel Terraform guide](https://developers.cloudflare.com/tunnel/guides/terraform/)).

Here "deploy keys" means the credentials that let people or CI push a deployment: the docs cover protecting the deployer UI and webhook with Access plus service tokens, replacing static SSH keys with Access short-lived certificates, and detecting leaked tokens with DLP entries; they say nothing about storing on-chain deployer private keys, which Cloudflare One does not manage.

## 20. Build hooks for Web3 projects

These uses apply to teams launching on Solana, Ethereum, Base and Robinhood Chain (an EVM L2 with chain id 4663); chain-side details are the team's own, and only the Cloudflare behavior is sourced.

1. Put every admin surface behind Access: token launch dashboards, presale or allowlist admin, treasury and multisig coordination tools, indexer and subgraph admin UIs, Grafana for nodes, all as self-hosted apps on a deny-by-default account ([self-hosted public app](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/), [require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/)).
2. Put the contract deployer UI (for example a Foundry or Anchor deploy dashboard) behind Access with security-key MFA and temporary authentication, so a stolen password alone cannot trigger a mainnet deploy ([independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/), [temporary authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/temporary-auth/)).
3. Expose a self-hosted RPC endpoint, indexer API or validator metrics through Tunnel without opening ports, gate it with a Service Auth policy, and hand the bot or frontend backend a service token (`CF-Access-Client-Id`/`CF-Access-Client-Secret`) instead of an IP allowlist ([service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/), [published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)); JSON-RPC over HTTP and WebSocket subscriptions both pass through Tunnel ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
4. Keep gRPC services (for example a Solana Geyser-style stream) on private network routes, because the Tunnels FAQ says gRPC is not supported on public hostnames ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
5. Replace SSH keys on validator, sequencer-adjacent or keeper hosts with Access for Infrastructure short-lived certificates and encrypted SSH command logs, which also gives an audit trail of who touched a signing host ([SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/), [SSH command logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/)).
6. Block known drainer and fake-airdrop domains for the whole team with a Gateway DNS policy on a hostname list (`any(dns.domains[*] in $<LIST_UUID>)`), plus the Phishing, Scam, Brand Embedding and New Domains / Newly Seen Domains categories; lists hold 1,000 entries on Standard and do not take wildcards, so use the Domain selector, which already matches subdomains ([DNS common policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/common-policies/), [domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/), [lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)).
7. Do not block the "Cryptocurrency" content category (ID 183) on a Web3 team, since it is a content category distinct from the "Cryptomining" security category ([domain categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/)).
8. Pair the DNS block with an HTTP or network block, because a DNS block alone does not stop direct-IP access ([order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/)).
9. If Browser Isolation is purchased, isolate New Domains and uncategorized sites with keyboard input and paste disabled, so users cannot type or paste into a fresh lookalike dapp ([isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)).
10. Use package registry security to block or log suspicious npm and Cargo downloads on developer machines and CI runners that pass through Gateway ([package registry security](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/package-registry-security/)).
11. Use DLP (Enterprise add-on) Credentials and Secrets plus custom entries to catch private keys and seed phrases leaving via web uploads or AI prompts; Bitcoin and Ethereum address entries exist but a seed phrase or Solana key entry does not ([predefined detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/)).
12. Connect the GitHub organization to CASB (free for two integrations) to catch unprotected default branches and disabled 2FA on contract repos ([GitHub CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/github/)).
13. Use Mesh (free beta) to link a home-lab archive node, a cloud indexer and laptops by private Mesh IP for bidirectional replication without a VPN concentrator ([Mesh concepts](https://developers.cloudflare.com/mesh/concepts/)).
14. Front team MCP tooling (chain data, explorer, deploy helpers) with an MCP server portal so agents get curated tools behind Access ([MCP portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)).
15. For public TCP/UDP node ports (p2p, validator gossip), Cloudflare One is the wrong tool; see Spectrum and Magic Transit in `protect-connect/04-networking.md`.

## 21. Gaps and contradictions

- The free seat count is not in the Cloudflare One docs; only the SASE reference architecture ("up to 50 users") and a blog post ("teams of under 50 users") state it, and the two phrasings differ by one ([SASE reference architecture](https://developers.cloudflare.com/reference-architecture/architectures/sase/), `raw/blog/post-quantum-warp.md`).
- Plan names vary: "Standard" in limit tables, "Pay-as-you-go" elsewhere, and a separate "Access" and "Gateway" plan column in the log retention table that no other page explains ([account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/), [logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)).
- Dashboard paths disagree: "Team & Resources" versus "Teams & Resources", "Zero Trust > ..." versus Cloudflare One at one.dash.cloudflare.com, and the standalone Tunnel docs use "Networking > Tunnels" ([seat management](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/), [client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/), [Tunnel get started](https://developers.cloudflare.com/tunnel/get-started/)).
- Tunnel is documented twice (standalone `tunnel/` for public apps and `cloudflare-one/networks/connectors/cloudflare-tunnel/` for private networking) and Mesh and Cloudflare WAN are mirrored under `cloudflare-one/networks/connectors/`, so the same fact can drift between copies.
- `routing-to-tunnel` says TCP or UDP apps can be routed through a Spectrum application on a virtual network, while the Spectrum limitations page and Tunnel integrations page say Spectrum plus Tunnel is only supported for HTTP/HTTPS; Spectrum's own get-started does document TCP/UDP virtual-network origins ([published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), [Spectrum limitations](https://developers.cloudflare.com/spectrum/reference/limitations/), [Spectrum get started](https://developers.cloudflare.com/spectrum/get-started/)).
- The connectivity options page links Cloudflare One Appliance docs at `.../configuration/appliances/` while the actual path is `.../configuration/appliance/` ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
- The Logpush page is "Enterprise-only" while the account limits page lists Logpush job counts without a plan qualifier ([Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), [account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).
- CASB added a Zoom integration on 2026-09-09 but no Zoom page exists under `integrations/cloud-and-saas/` in the mirror ([CASB changelog](https://developers.cloudflare.com/cloudflare-one/changelog/casb/)).
- DLP lists Bitcoin and Ethereum wallet address entries, but they appear in no predefined profile and there is no seed phrase, raw private key or Solana entry ([predefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/)).
- The Gateway overview page contains a typo ("network.fprotecting") in the DLP bullet ([traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)).
- Multi-Cloud Networking is "closed beta" on its own page, while the connectivity options page presents it as a regular option enabled by the account team ([MCN](https://developers.cloudflare.com/multi-cloud-networking/), [connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
- Data Localization Suite is an "Enterprise-only paid add-on", while region support says managed regions are "available to all accounts, though some may require specific entitlements", and Regional Services calls itself an Enterprise add-on ([DLS](https://developers.cloudflare.com/data-localization/), [region support](https://developers.cloudflare.com/data-localization/region-support/), [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/)).
- Email security publishes no plan or price, only "Contact Sales" and a free Retro Scan ([Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)).
- The consumer WARP privacy page still refers to "Cloudflare for Teams", an old name ([WARP privacy](https://developers.cloudflare.com/warp-client/privacy/)).
- No page states Zero Trust per-seat prices; they live only on cloudflare.com, which is not mirrored here.
