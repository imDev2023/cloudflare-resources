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

Jul 9, 2026

[<h2>Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</h2>](https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

On **October 5, 2026**, two changes take effect across the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) and [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/): the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the `connections` field. If you manage private network routes or read tunnel connection details through the API, `cloudflared`, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.

#### Route endpoints

The CIDR-encoded route endpoints are deprecated in favor of the standard, `route_id`-based endpoints that already exist today. Both sets of endpoints route a private network through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) or [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) (the API still refers to Mesh nodes as `warp_connector`) — only the request shape changes.

**Deprecated endpoints (removed October 5, 2026):**

- Create a tunnel route (CIDR Endpoint): [`POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/)
- Update a tunnel route (CIDR Endpoint): [`PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/)
- Delete a tunnel route (CIDR Endpoint): [`DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/)

**Replacement endpoints:**

- Create a tunnel route: [`POST /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/)
- Update a tunnel route: [`PATCH /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/)
- Delete a tunnel route: [`DELETE /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/)

#### What is changing

|  | Deprecated (CIDR-encoded path) | Replacement |
| --- | --- | --- |
| Route identifier | URL-encoded CIDR in the path (`/network/{ip_network_encoded}`) | `route_id` in the path (`network` moves to the request body on create) |
| Create | `POST .../teamnet/routes/network/{ip_network_encoded}` | `POST .../teamnet/routes` with `network` and `tunnel_id` in the body |
| Update | `PATCH .../teamnet/routes/network/{ip_network_encoded}` | `PATCH .../teamnet/routes/{route_id}` |
| Delete | `DELETE .../teamnet/routes/network/{ip_network_encoded}` | `DELETE .../teamnet/routes/{route_id}` |

#### Action required

1. Capture each route's `route_id` by calling [List tunnel routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/), or read it from the response the first time you create a route with the replacement endpoint.
2. Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.
3. If you manage routes with the `cloudflared tunnel route ip add | delete` commands, upgrade `cloudflared` to the [latest version ↗︎](https://github.com/cloudflare/cloudflared/releases).
4. If you manage routes with Terraform, make sure you are on a current version of the [`cloudflare_zero_trust_tunnel_cloudflared_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route) resource and the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

```bash
# Before: create a route by URL-encoding the CIDR into the path
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \
     -H 'Content-Type: application/json' \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
     -d '{"tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'

# After: create a route with the network in the request body
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \
     -H 'Content-Type: application/json' \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
     -d '{"network": "172.16.0.0/16", "tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'

# After: update or delete a route using its route_id
curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
     -H 'Content-Type: application/json' \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
     -d '{"comment": "Updated comment for this route."}'

curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

#### Cloudflare Tunnel and Cloudflare Mesh connections

Starting the same day, the `connections` array is removed from list and get responses for [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes (the `cfd_tunnel` and `warp_connector` API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.

This affects:

- [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/) — `connections` removed from each item in `result`
- [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/) — `connections` removed from `result`
- [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/) — `connections` removed from each item in `result`
- [`GET /accounts/{account_id}/warp_connector/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/) — `connections` removed from `result`

#### Action required

Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/). For Cloudflare Mesh, call [`GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/).

```bash
# Before: read connections off the tunnel object
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

# After: query connections directly
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

Update any dashboards, monitoring scripts, or automation that parses `connections` from the tunnel list or get response. `cloudflared` and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.

#### Why we are making these changes

- **Smaller, faster responses.** Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.
- **A single way to identify a route.** Consolidating on `route_id` removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.
- **Consistency across the API.** Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.

To learn more, refer to the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/), the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/), and [Routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/) documentation.

Jul 8, 2026

[<h2>IPsec downgrade protection (beta)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Cloudflare IPsec now supports the [`IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/) IKEv2 extension to protect against downgrade attacks on IPsec tunnels.

IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable [on-path attacker ↗︎](https://www.cloudflare.com/learning/security/threats/on-path-attack/) can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.

Key details:

- Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.
- Cloudflare sends the `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` notification unconditionally as a responder when the feature flag is enabled.
- Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.
- This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.

Refer to [Downgrade protection](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta) for more details.

Jul 8, 2026

[<h2>IP lists, IDS, and SIP rules supported in Unified Routing</h2>](https://developers.cloudflare.com/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) IP lists, IDS, and SIP rules are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. These features require a Cloudflare Advanced Network Firewall subscription.

Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Jul 7, 2026

[<h2>Cloudflare One Client for Windows (version 2026.6.850.0)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.

Jul 7, 2026

[<h2>File transfer controls for browser-based RDP (beta)</h2>](https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.

![File transfer connection settings in the Access policy configuration.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=692,format=webp/_astro/file-transfer-policy-control.CiSEa5rr.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.

#### Configuration options

File transfer controls are configured per policy within your Access application, alongside existing [text clipboard controls](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings). For each policy, you can select one of the following options:

- **Client to remote RDP session allowed** — Users can upload files from their local machine into the browser-based RDP session.
- **Remote RDP session to client allowed** — Users can download files from the browser-based RDP session to their local machine.
- **Both directions allowed** — Users can upload and download files between their local machine and the browser-based RDP session.
- **Disable copying/pasting** — Users are not allowed to transfer files between their local machine and the browser-based RDP session.

By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.

#### How it works

To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.

![The clipboard side panel showing files available for transfer.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=812,height=532,format=webp/_astro/clipboard-side-panel.Us2RfXfs.png) ![A remote document ready for download or local printing.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=770,height=442,format=webp/_astro/remote-doc-ready-for-download-or-print-local.Dcm5hrGD.png)

This feature is in beta and available on all Zero Trust plans. For more information, refer to [File transfer for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files).

Jul 7, 2026

[<h2>Browser Isolation support for authorization proxy endpoints</h2>](https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) now supports Gateway [authorization proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint). You can apply [HTTP Isolate policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.

Previously, only [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.

To get started, [create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [build an Isolate policy](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/).

Jul 6, 2026

[<h2>Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) and generate its license key directly from the dashboard, without contacting your account team.

![Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=988,format=webp/_astro/2026-07-06-virtual-appliance-self-serve-ui.Dn2NC_ql.gif)

- On the **Connectors** page, select **Add an appliance** and choose **Virtual appliance** to register a virtual appliance and generate its authentication key.
- Use **Regenerate authentication key** from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.
- The authentication key is shown only once — copy and store it securely.

This complements the existing [API and Terraform self-serve workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

Jul 2, 2026

[<h2>Hostname routing for Cloudflare Mesh</h2>](https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now add [hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Cloudflare Mesh node, in addition to CIDR routes.

1. [Client device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

   Requests `wiki.internal.local`
2. DNS query↓
3. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

   Returns a token IP, then rewrites the destination to the real private IP. `172.64.128.0/20`
4. [Hostname route](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes)↓
5. [Mesh node](https://developers.cloudflare.com/mesh/)

   Forwards traffic to the host on the local network
6. ↓
7. Private host

   `wiki.internal.local` · `10.0.0.50`

Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:

- **Private hostname** (for example, `wiki.internal.local`) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.
- **Public hostname** (for example, `www.example.com`) — route that hostname's traffic through the node and egress via the node's public IP.

[Go to **Mesh** ↗](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, prerequisites, and DNS options, refer to [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).

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

Jul 1, 2026

[<h2>Fix redirect URL fragment encoding for single-page applications</h2>](https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Access now correctly preserves URL fragment characters (`/`, `?`, `=`, `&`, `;`) when redirecting users back to an application after login. Previously, these characters were encoded with `encodeURIComponent`, which mangled fragment-based routes used by single-page applications (SPAs).

For example, an SPA URL like `https://app.example.com/#/dashboard?tab=settings&view=advanced` would previously redirect to a broken URL after login. This is now handled correctly.

If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.

Jul 1, 2026

[<h2>Independent MFA for infrastructure applications</h2>](https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.

With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, `root`) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.

#### Enrollment

Users enroll their YubiKey PIV key through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). For enrollment instructions and SSH client setup, refer to [Enroll a PIV key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps).

#### Configuration

For setup instructions, refer to [Enforce MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

Jun 30, 2026

[<h2>New permissions and roles for Gateway policies and lists</h2>](https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now assign granular, resource-scoped roles for [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) firewall policies and [Zero Trust lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/). Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the following resource-scoped roles are now available:

| Role | Description |
| --- | --- |
| Zero Trust Gateway Firewall Policies Admin | Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies. |
| Zero Trust Gateway DNS Policies Admin | Can view and edit Gateway DNS policies. |
| Zero Trust Gateway HTTP Policies Admin | Can view and edit Gateway HTTP policies. |
| Zero Trust Gateway Network Policies Admin | Can view and edit Gateway Network policies. |
| Zero Trust Gateway Egress Policies Admin | Can view and edit Gateway Egress policies. |
| Zero Trust Gateway Resolver Policies Admin | Can view and edit Gateway Resolver policies. |
| Zero Trust Gateway Policies Admin | Can view and edit all Gateway policies. |
| Zero Trust Gateway Policies Read | Can view all Gateway policies. |
| Zero Trust Gateway Read Only | Can view all Gateway resources. |
| Zero Trust DNS Locations Admin | Can view and edit DNS locations. |
| Zero Trust Proxy Endpoints Admin | Can view and edit Gateway Proxy Endpoints. |
| Zero Trust Account Lists Admin | Can view and edit all Gateway and Access lists. |
| Zero Trust Account Lists Read | Can view all Gateway and Access lists. |

These roles allow you to:

- Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.
- Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.
- Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.

You can also now assign *Resource-scoped roles*. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. **Existing account-level roles continue to work.** A member with the `Cloudflare Gateway` or `Cloudflare Zero Trust` role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.

#### Get started

- Refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) for setup instructions and supported resources.
- Learn how to [create permission policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/) that use these roles.

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

Jun 26, 2026

[<h2>Service token support for MCP server portals</h2>](https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now connect autonomous agents and bots to an [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) using an [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/). Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.

To set this up:

- Add a [Service Auth policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth) that matches your service token to the portal's Access application.
- Add a Service Auth policy that matches the same token to each linked MCP server's Access application.
- Turn **Require user auth** off ( `on_behalf: false`) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.

The bot connects with `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.

For step-by-step setup, refer to [Connect with a service token](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token).

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

Jun 23, 2026

[<h2>Regionalized IP Bindings for Regional Services</h2>](https://developers.cloudflare.com/changelog/post/2026-06-23-regionalized-ip-bindings/)

[Data Localization Suite](https://developers.cloudflare.com/data-localization/)

Regional Services now supports **Regionalized IP Bindings**, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/).

Where [Regional Hostnames](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/) regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.

Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.

To get started, refer to [Regionalized IP Bindings](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/).

Jun 19, 2026

[<h2>Manage all your routes from one page in the dashboard</h2>](https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

- **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
- **See every route in one table**, with its destination, type, connector, priority, and source, and filter or sort to find what you need.
- **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
- **Manage [virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
- **Test a route** to see which connector and next hop a destination resolves to before you commit a change.

To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[Go to **Routes** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

Jun 18, 2026

[<h2>Cloudflare identity provider is now the default for new accounts</h2>](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

When you create a new Zero Trust organization, Cloudflare now adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method. Previously, new organizations started with [one-time PIN (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/).

With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) whenever you need to.

This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.

Jun 11, 2026

[<h2>Define custom topics for AI prompt protection</h2>](https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/)

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

You can now define custom topics for AI prompt protection. Predefined [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.

You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a [custom wordlist or pattern entry](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets) instead.

Custom topics run through the same [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls) path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.

#### Create a custom AI prompt topic

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Data loss prevention** > **Detection entries**.
2. Select **AI prompt topics**, then select **Custom Prompt Topic**.
3. Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.
4. Add this detection entry to an existing DLP profile, or [create a new DLP profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile).
5. Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.

Note

Write the description as a concept to classify, not a list of keywords. For example, describe "internal financial forecasts and unreleased revenue figures" rather than listing specific document names.

For more information, refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

Jun 5, 2026

[<h2>Filter Workers' public Internet traffic using Gateway policies</h2>](https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Workers using a [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) binding with `network_id: "cf1:network"` now egress to public Internet destinations through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.

1. [Worker](https://developers.cloudflare.com/workers/)

   Calls `env.EGRESS.fetch()`
2. [VPC binding](https://developers.cloudflare.com/workers-vpc/)↓
3. [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

   Bind via [`cf1:network`](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/)
4. ↓
5. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

   Policies applied: [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)
6. ↓
7. ↗Public Internet

   Any public hostname or IP

[Gateway logsDNSHTTPNetwork](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)

What you get by default:

- **Visibility.** Worker egress shows up in Gateway [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) logs alongside your other traffic, so you can audit what your Workers are calling and when.
- **Enforcement.** Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.

```jsonc
{
	"vpc_networks": [
		{
			"binding": "EGRESS",
			"network_id": "cf1:network",
			"remote": true,
		},
	],
}
```

```toml
[[vpc_networks]]
binding = "EGRESS"
network_id = "cf1:network"
remote = true
```

```js
// Egress to a public destination — subject to your Gateway policies and logged
const response = await env.EGRESS.fetch("https://api.example.com/data");
```

```ts
// Egress to a public destination — subject to your Gateway policies and logged
const response = await env.EGRESS.fetch("https://api.example.com/data");
```

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/). For policy authoring, refer to [Cloudflare Gateway traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

Jun 4, 2026

[<h2>Share identity providers across accounts with IdP federation</h2>](https://developers.cloudflare.com/changelog/post/2026-06-04-idp-federation/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access now supports [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/), which allows organizations to share a single identity provider across multiple Cloudflare accounts.

Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.

Key capabilities:

- **One IdP, many accounts** — Configure your IdP once and share it with all accounts in your organization.
- **Lifecycle management** — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.
- **Immutable recipient connections** — IdP connections in recipient accounts cannot be accidentally modified or deleted.

To get started, refer to [IdP federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/).

Jun 3, 2026

[<h2>SAML assertion encryption for identity providers</h2>](https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.

Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.

![SAML encryption toggle in the identity provider configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=344,format=webp/_astro/saml-encryption.J5jmiYv8.png)

SAML encryption includes built-in certificate lifecycle management:

- **Automatic certificate generation**: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.
- **Certificate rotation**: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.
- **PEM export**: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.

To get started, refer to [Encrypt SAML assertions](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions).

Jun 2, 2026

[<h2>Cisco IOS XE</h2>](https://developers.cloudflare.com/changelog/post/2026-06-02-cisco-ios-xe/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:

- Post Quantum Cryptography (PQC)
- Policy-Based Routing (PBR)
- IP Service Level Agreement (IP SLA)

This link will take you directly to the updated [Cisco IOS XE](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/cisco-ios-xe/) guide.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/#page","headline":"Cloudflare One Changelog","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
