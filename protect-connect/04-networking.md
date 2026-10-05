# Networking (Protect & Connect)

Snapshot of the Cloudflare developer docs as mirrored on 2026-10-05; everything that moves (plans, limits, versions, beta or GA status) is dated "as of 2026-10-05".
The Protect & Connect > Networking dropdown on developers.cloudflare.com lists seven products: Tunnel, Mesh, Magic Transit, Magic WAN (now titled Cloudflare WAN), Network Interconnect, Spectrum and BYOIP (source: `raw/nav/home-sidebar.md`), and the top-level `llms.txt` "Network security" group adds Network Error Logging and Network Flow, both covered here.
The split is simple: Tunnel (all plans, free) and Mesh (beta, includes the Zero Trust Free plan) are software connectors any team can use today, Spectrum is the paid L4 reverse proxy for TCP and UDP (only SSH, Minecraft and RDP single apps below Enterprise, arbitrary TCP/UDP is an Enterprise add-on), Network Error Logging and the free tier of Network Flow are visibility tools on all plans, and Magic Transit, Cloudflare WAN, Network Interconnect and BYOIP are Enterprise-only network products that assume your own routers and, for Magic Transit and BYOIP, your own `/24` IPv4 (or `/48` IPv6) prefix.
For Web3 teams the practical toolkit is Tunnel (expose RPC, indexer and metrics endpoints with no inbound ports), Mesh (private bidirectional links between nodes and laptops) and, at larger scale, Spectrum or Magic Transit for public TCP/UDP node ports, each with caveats on source-IP visibility and plan cost that are spelled out below.
Identity and policy layers that sit on top of these connectors (Access, Gateway, the Cloudflare One Client) are in `protect-connect/02-cloudflare-one.md`.

## Table of contents

1. [Sidebar map and how the products fit](#1-sidebar-map-and-how-the-products-fit)
2. [Cloudflare Tunnel](#2-cloudflare-tunnel)
3. [Cloudflare Mesh](#3-cloudflare-mesh)
4. [Magic Transit](#4-magic-transit)
5. [Cloudflare WAN (formerly Magic WAN)](#5-cloudflare-wan-formerly-magic-wan)
6. [Network Interconnect (CNI)](#6-network-interconnect-cni)
7. [Spectrum](#7-spectrum)
8. [BYOIP](#8-byoip)
9. [Network Error Logging](#9-network-error-logging)
10. [Network Flow](#10-network-flow)
11. [Plan availability cheat sheet](#11-plan-availability-cheat-sheet)
12. [Build hooks for Web3 projects](#12-build-hooks-for-web3-projects)
13. [Gaps and contradictions](#13-gaps-and-contradictions)

---

## 1. Sidebar map and how the products fit

| Sidebar entry | Docs root | Source folder | Status as of 2026-10-05 |
| --- | --- | --- | --- |
| Tunnel | https://developers.cloudflare.com/tunnel/ | `raw/docs/tunnel/` (40 pages) | "Available on all plans" |
| Mesh | https://developers.cloudflare.com/mesh/ | `raw/docs/mesh/` (11 pages) | Beta, Cloudflare One accounts including Free |
| Magic Transit | https://developers.cloudflare.com/magic-transit/ | `raw/docs/magic-transit/` (43 pages) | "Enterprise-only", not self-serve |
| Magic WAN | https://developers.cloudflare.com/cloudflare-wan/ | `raw/docs/cloudflare-wan/` (110 pages, about 6 MB, 5 MB of it a third-party license page) | "Enterprise-only", renamed Cloudflare WAN |
| Network Interconnect | https://developers.cloudflare.com/network-interconnect/ | `raw/docs/network-interconnect/` (7 pages) | "Enterprise-only" |
| Spectrum | https://developers.cloudflare.com/spectrum/ | `raw/docs/spectrum/` (22 pages) | "Available on Paid plans" |
| BYOIP | https://developers.cloudflare.com/byoip/ | `raw/docs/byoip/` (21 pages) | "Enterprise-only" |
| Network Error Logging (llms.txt only) | https://developers.cloudflare.com/network-error-logging/ | `raw/docs/network-error-logging/` (4 pages) | All plan types |
| Network Flow (llms.txt only) | https://developers.cloudflare.com/network-flow/ | `raw/docs/network-flow/` (23 pages) | "Available on all plans", free version with limits |

Direction and source-IP behavior decide which product fits ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)):

| Product | Direction | Source IP at the origin | Typical use |
| --- | --- | --- | --- |
| Tunnel | Inbound to origin only (client-initiated) | `cloudflared` IP; `CF-Connecting-IP` header for HTTP only | Publish apps, private network access, Workers VPC |
| Mesh | Bidirectional, any participant | Preserved end to end | Device-to-device, site-to-site, replication |
| Spectrum | Inbound L4 reverse proxy | Cloudflare edge IP unless Proxy Protocol (Enterprise) | Public TCP/UDP apps with DDoS protection |
| Magic Transit | Inbound (optionally egress) at L3 for whole prefixes | Original packets delivered over GRE/IPsec/CNI | DDoS protection for networks you own |
| Cloudflare WAN | Bidirectional site-to-site | Preserved within GRE/IPsec | Replace MPLS and SD-WAN |
| CNI | Bidirectional private circuit | n/a (physical or virtual link) | Bypass the public Internet |

## 2. Cloudflare Tunnel

### What it is

Cloudflare Tunnel connects origins to Cloudflare through outbound-only, post-quantum encrypted connections from the `cloudflared` daemon, so the origin needs no public IP and no open inbound ports ([Tunnel](https://developers.cloudflare.com/tunnel/)).
Each tunnel keeps four long-lived connections to at least two Cloudflare data centers ([Tunnel](https://developers.cloudflare.com/tunnel/), [configuration](https://developers.cloudflare.com/tunnel/configuration/)).
Use cases are secure origin connectivity with CDN, WAF and DDoS applied, public ingress routing, Workers VPC (Workers reaching private services) and Load Balancing endpoints ([Tunnel](https://developers.cloudflare.com/tunnel/)).
The standalone `tunnel/` docs cover public applications; private networking, VPN replacement and Gateway filtering are documented under https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/ ([Tunnel](https://developers.cloudflare.com/tunnel/)).
The product was called Warp in beta, then Argo Tunnel, and became Cloudflare Tunnel once Argo was no longer required ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).

### Key concepts

- Tunnel: a persistent object with a UUID in your account; routes reference this ID ([fundamentals](https://developers.cloudflare.com/tunnel/concepts/)).
- Connector: one running `cloudflared` instance; extra connectors for the same tunnel are replicas ([fundamentals](https://developers.cloudflare.com/tunnel/concepts/)).
- Remotely managed tunnel: configured in the dashboard or API and run with a token; locally managed tunnel: configured with a YAML file and a credentials JSON ([tunnel tokens](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/), [configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/)).
- Quick Tunnel: `cloudflared tunnel --url http://localhost:8080` gives a random `trycloudflare.com` URL with no account ([Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)).
- Routes: published applications (public hostname to service), private network routes (CIDR or hostname, for Cloudflare One clients) and Workers VPC ([fundamentals](https://developers.cloudflare.com/tunnel/concepts/)).
- "The tunnel provides connectivity. Access to each resource is controlled separately." ([fundamentals](https://developers.cloudflare.com/tunnel/concepts/)).

### Configuration

Dashboard: Networking > Tunnels > Create Tunnel, choose OS, run the shown install command, then Routes > Add route > Published application with a hostname and a Service URL such as `http://localhost:80` ([get started](https://developers.cloudflare.com/tunnel/get-started/)).
API: `POST /accounts/$ACCOUNT_ID/cfd_tunnel` with `{"name":"api-tunnel","config_src":"cloudflare"}` returns `id` and `token`, and `PUT /accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/configurations` sets ingress rules ending in a catch-all `http_status:404` ([get started](https://developers.cloudflare.com/tunnel/get-started/)).
API token permissions are Account Cloudflare Tunnel Edit and Zone DNS Edit, and endpoints accept `Cloudflare One Connectors Write`, `Cloudflare One Connector: cloudflared Write` or `Cloudflare Tunnel Write` ([get started](https://developers.cloudflare.com/tunnel/get-started/)).
Locally managed `config.yml` example from the docs:

```yaml
tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef
credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json
ingress:
  - hostname: gitlab.widgetcorp.tech
    service: http://localhost:80
  - hostname: gitlab-ssh.widgetcorp.tech
    service: ssh://localhost:22
  - service: http_status:404
```

Source: [configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/), which also shows path regex matching and wildcard hostnames (`"*.example.com"`).
Useful commands: `cloudflared tunnel login`, `create`, `list`, `info`, `run`, `cleanup` (including `--connector-id`), `delete`, `route dns <tunnel> <hostname>`, `route lb`, `tail <UUID>` and `update` ([useful commands](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/)).
Supported service types: `http`, `https` (with `noTLSVerify` for self-signed), `unix`, `unix+tls`, `tcp`, `ssh`, `rdp`, `smb` (non-HTTP ones streamed over WebSocket and needing `cloudflared access` on the client), `http_status`, `bastion` and `hello_world`; IPv6 literals need brackets like `http://[2001:db8::1]:8000` ([routing](https://developers.cloudflare.com/tunnel/concepts/routing/)).
Dashboard routes create a CNAME to `<UUID>.cfargotunnel.com`, which only proxies for DNS records in the same account; a stopped tunnel leaves the record in place and visitors see error `1016` ([routing](https://developers.cloudflare.com/tunnel/concepts/routing/)).
Replicas give basic redundancy, but a load balancer treats all replicas of one UUID as one endpoint, so use separate tunnels per host for steering and session affinity ([routing](https://developers.cloudflare.com/tunnel/concepts/routing/)).
Terraform (provider `>= 5.8.2`, with a v4 variant `>= 4.40.0, < 5.0.0` also shown) uses `cloudflare_zero_trust_tunnel_cloudflared`, `cloudflare_zero_trust_tunnel_cloudflared_token` (data source), `cloudflare_zero_trust_tunnel_cloudflared_config`, `cloudflare_zero_trust_tunnel_cloudflared_route`, `cloudflare_dns_record`, `cloudflare_zero_trust_access_application` and `cloudflare_zero_trust_access_policy` ([Terraform guide](https://developers.cloudflare.com/tunnel/guides/terraform/)).
Other deployment guides: Ansible, AWS, Azure, GCP, Kubernetes, granular permissions per tunnel, and running as a service on Linux, macOS and Windows ([Tunnel llms.txt](https://developers.cloudflare.com/tunnel/llms.txt)).
Tokens: anyone with a remotely managed tunnel token can run the tunnel; rotate with "Rotate token" and reinstall with `cloudflared service install <NEW_TOKEN>`, and force-disconnect connectors if compromised ([tunnel tokens](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/)).

### Networking requirements

`cloudflared` connects outbound on port 7844 (TCP for `http2`, UDP for `quic`) to `region1.v2.argotunnel.com` and `region2.v2.argotunnel.com` (198.41.192.x and 198.41.200.x), with US-only (`--region us`) and FedRAMP High endpoint sets ([configuration](https://developers.cloudflare.com/tunnel/configuration/)).
SNI-enforcing firewalls must allow `cftunnel.com`, `h2.cftunnel.com`, `quic.cftunnel.com` and `_v2-origintunneld._tcp.argotunnel.com` on 7844; port 443 to `api.cloudflare.com`, `update.argotunnel.com`, `github.com` and `<team>.cloudflareaccess.com` is optional (updates, Access JWT validation) ([configuration](https://developers.cloudflare.com/tunnel/configuration/)).
Common run parameters: `--loglevel`, `--logfile`, `--metrics` (default `127.0.0.1:20241` to `20245`), `--protocol auto|quic|http2`, `--region us` and `--token` ([configuration](https://developers.cloudflare.com/tunnel/configuration/)).
Common origin parameters: `originServerName`, `noTLSVerify`, `httpHostHeader`, `connectTimeout` (default 30s), plus `access` ("Protect with Access") for JWT validation in `cloudflared` ([configuration](https://developers.cloudflare.com/tunnel/configuration/), [origin parameters](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/)).
System requirements: two dedicated hosts per location with at least 4 GB RAM and 4 cores, 50,000 local ports per host (`net.ipv4.ip_local_port_range = 11000 60999`) and `ulimit -n` of at least 70,000 ([system requirements](https://developers.cloudflare.com/tunnel/platform/system-requirements/)).

### Observability

Statuses are Healthy, Inactive (never run), Down and Degraded, and they only reflect the `cloudflared` to Cloudflare link, not origin reachability ([observability](https://developers.cloudflare.com/tunnel/observability/)).
Tunnel Creation or Deletion and Tunnel Health notifications are included with all Zero Trust plans ([observability](https://developers.cloudflare.com/tunnel/observability/)).
`cloudflared` exposes a Prometheus endpoint at `127.0.0.1:<20241-20245>/metrics`, and there is a Grafana tutorial ([observability](https://developers.cloudflare.com/tunnel/observability/), [Grafana tutorial](https://developers.cloudflare.com/tunnel/tutorials/grafana/)).

### Limits, plans and status (as of 2026-10-05)

- All plans; no paid Access plan is needed to publish an app, only to protect it with Access policies ([Tunnel](https://developers.cloudflare.com/tunnel/), [published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)).
- 1,000 tunnels per account, 1,000 routes per account shared with Mesh, 25 active replicas (100 connections) per tunnel, 1,000 virtual networks ([account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/), [configuration](https://developers.cloudflare.com/tunnel/configuration/)).
- Quick Tunnels: no uptime guarantee, 200 in-flight requests (then `429`), no Server-Sent Events, new hostname each run ([Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)).
- Quick Tunnels can now require email one-time PIN with `--allowed-mail alice@example.com`, repeated, comma-separated or `'*@example.com'` (added 2026-10-02) ([Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/), [Tunnel changelog](https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/)).
- Public hostname routes on Free, Pro and Business are bound by the CDN video-serving terms; private network routes are not ([routing](https://developers.cloudflare.com/tunnel/concepts/routing/), [Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
- WebSockets are fully supported; gRPC only via private subnet routing, not public hostnames ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
- Origins never see visitor IPs directly ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
- Cloudflare supports `cloudflared` versions within one year of the latest release ([downloads](https://developers.cloudflare.com/tunnel/downloads/)).
- 32-bit Windows and Intel macOS `cloudflared` builds stop receiving releases in 2027 (announced 2026-09-18) ([Tunnel changelog](https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/)).
- Spectrum can sit in front of Tunnel only for HTTP/HTTPS applications per the Tunnel integrations page; see section 7 for the conflicting virtual-network origin feature ([integrations](https://developers.cloudflare.com/tunnel/integrations/)).

### Most useful pages

- Overview https://developers.cloudflare.com/tunnel/
- Get started https://developers.cloudflare.com/tunnel/get-started/
- Quick Tunnels https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/
- Routing and protocols https://developers.cloudflare.com/tunnel/concepts/routing/
- Configuration (replicas, firewall, parameters) https://developers.cloudflare.com/tunnel/configuration/
- Terraform https://developers.cloudflare.com/tunnel/guides/terraform/
- Private networks (Cloudflare One) https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/

## 3. Cloudflare Mesh

### What it is

Mesh gives every enrolled server, laptop and phone a private Mesh IP and lets participants talk over TCP, UDP or ICMP through Cloudflare, including device-to-device without customer infrastructure ([Mesh](https://developers.cloudflare.com/mesh/)).
It was previously WARP Connector plus peer-to-peer connectivity; WARP Connectors are now Mesh nodes with no migration needed ([Mesh](https://developers.cloudflare.com/mesh/)).

### Key concepts

- Mesh nodes are Linux servers, VMs or containers running the Cloudflare One Client (`warp-cli`) headless and can advertise routes and run active-passive replicas; client devices are laptops and phones running the same client with a UI ([concepts](https://developers.cloudflare.com/mesh/concepts/)).
- Mesh IPs come from `100.96.0.0/12` (CGNAT space), configurable if it conflicts ([concepts](https://developers.cloudflare.com/mesh/concepts/)).
- Nodes must use MASQUE; on WireGuard, hostname routes, IPv6 CIDR routes and high availability do not work ([concepts](https://developers.cloudflare.com/mesh/concepts/)).
- Routes: CIDR routes (private or public ranges, IPv4 or IPv6) and hostname routes for private or public hostnames; a node with a public CIDR acts like an exit node ([routes](https://developers.cloudflare.com/mesh/features/routes/), [concepts](https://developers.cloudflare.com/mesh/concepts/)).
- Policy comes from Gateway network policies and device posture, which the concepts page maps to "ACLs" in other mesh products ([concepts](https://developers.cloudflare.com/mesh/concepts/)).

| | Mesh | Tunnel |
| --- | --- | --- |
| Direction | Bidirectional | Inbound to origin |
| Addressing | Mesh IP per participant | Server side only |
| Connector | `warp-cli` | `cloudflared` |
| Protocols | TCP, UDP, ICMP | HTTP/S, TCP, SSH, RDP, SMB over WebSocket |

Source: [concepts](https://developers.cloudflare.com/mesh/concepts/).
Mesh is recommended for long-lived TCP such as database replication, ERP and RDP, and Tunnel for publishing specific apps ([concepts](https://developers.cloudflare.com/mesh/concepts/)).

### Configuration

Dashboard: Networking > Mesh > Add participant > Add node, then pick Linux, Kubernetes, Docker Compose or Docker CLI; client devices enroll interactively with the IdP, and headless Windows, macOS or Linux devices enroll with a service token ([get started](https://developers.cloudflare.com/mesh/get-started/)).
API: `POST /accounts/{account_id}/warp_connector` (with `"ha": true` for replicas) and `GET .../warp_connector/{id}/token`, using `Cloudflare One Connectors Write` or `Cloudflare One Connector: WARP Write` ([high availability](https://developers.cloudflare.com/mesh/features/high-availability/), [containers](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/)).
The first API token must be created in the dashboard, and account bootstrap settings must be configured before API or Terraform automation ([get started](https://developers.cloudflare.com/mesh/get-started/)).
Route management needs `Cloudflare One Networks Write` or `Cloudflare Tunnel Write` ([routes](https://developers.cloudflare.com/mesh/features/routes/)).
The `cloudflare/mesh` image (tags `latest`, `latest-amd64`, `latest-arm64`, Wolfi base) runs a node in Docker or Kubernetes ([containers](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/)).
Best practices: update with `apt-get install --only-upgrade cloudflare-warp`, persist IP forwarding in `/etc/sysctl.d/99-zzz-cloudflare-warp-connector.conf`, and apply cloud-provider forwarding settings (GCP and others) ([best practices](https://developers.cloudflare.com/mesh/best-practices/)).

### Limits, plans and status (as of 2026-10-05)

- Beta, available to Cloudflare One accounts including Free ([platform](https://developers.cloudflare.com/mesh/platform/)).
- 50 Mesh nodes per account and 1,000 CIDR routes shared with Tunnel ([account limits](https://developers.cloudflare.com/cloudflare-one/account-limits/)).
- High availability is active-passive for nodes with routes, enabled by default for dashboard-created nodes ([high availability](https://developers.cloudflare.com/mesh/features/high-availability/)).
- With Cloudflare WAN, Mesh requires Unified Routing ([platform](https://developers.cloudflare.com/mesh/platform/)).
- Mesh to Cloudflare One Client traffic is encapsulated twice, giving an effective MTU of about 1,280 ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
- Bulk creation of Tunnel and Mesh routes arrived 2026-09-02 ([Tunnel changelog](https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/)).

### Most useful pages

- https://developers.cloudflare.com/mesh/concepts/
- https://developers.cloudflare.com/mesh/get-started/
- https://developers.cloudflare.com/mesh/features/routes/
- https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/

## 4. Magic Transit

### What it is

An "Enterprise-only" L3 service that announces your IP space via BGP from all Cloudflare locations, scrubs DDoS traffic near its source, and delivers clean traffic to your origin over anycast GRE, IPsec or CNI, optionally also carrying egress ([Magic Transit](https://developers.cloudflare.com/magic-transit/), [about](https://developers.cloudflare.com/magic-transit/about/)).
It is "not a self-serve product"; onboarding starts with Cloudflare's team ([get started](https://developers.cloudflare.com/magic-transit/get-started/)).
China Network does not support Magic Transit ([about](https://developers.cloudflare.com/magic-transit/about/)).

### Key concepts

- Prefixes: you need a publicly routable block of at least `/24`, or you can lease Cloudflare-owned IPs, which need no LOA and turn on Magic Transit Egress automatically ([get started](https://developers.cloudflare.com/magic-transit/get-started/), [Cloudflare IPs](https://developers.cloudflare.com/magic-transit/cloudflare-ips/)).
- Letter of Agency: a PDF authorizing Cloudflare to announce your prefixes ([get started](https://developers.cloudflare.com/magic-transit/get-started/)).
- Router requirements: GRE (or IPsec), at least one tunnel per ISP, MSS clamping, and asymmetric flow support for ingress-only ([get started](https://developers.cloudflare.com/magic-transit/get-started/)).
- On-demand: advertise prefixes only during an attack via the dashboard or API, not available with leased IPs ([on-demand](https://developers.cloudflare.com/magic-transit/on-demand/)).
- Egress: source IPs must come from your Magic Transit prefix, with policy-based routing and tunnel failure detection recommended ([egress](https://developers.cloudflare.com/magic-transit/reference/egress/)).
- Traffic steering uses static routes with priorities and weights, or BGP peering (beta) influenced by communities and AS-path prepends, plus ECMP and regional route scoping ([traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/)).
- DDoS layers: always-on network-layer managed ruleset, Advanced TCP Protection and Advanced DNS Protection (auto-enabled in Monitor mode for new customers), Programmable Flow Protection (eBPF over UDP payloads, closed beta add-on), and Cloudflare Network Firewall, which is included ([DDoS protection](https://developers.cloudflare.com/magic-transit/ddos/), [Programmable Flow Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/)).

### Routing modes

Unified Routing became GA for Cloudflare WAN and Magic Transit on 2026-09-18 and is recommended for all new accounts ([Magic Transit changelog](https://developers.cloudflare.com/magic-transit/changelog/)).
It uses one routing fabric for the Cloudflare One Client, Tunnel, IPsec, GRE and CNI, private Cloudflare source IPs, and enables Mesh plus WAN together; BGP over CNI stays closed beta in both modes and IPv6 is beta ([WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/)).

### Configuration and operations

Dashboard pages cover tunnel endpoints, routes, advertising prefixes, Magic user roles, IPv6 (beta) and safely withdrawing a BYOIP prefix ([Magic Transit llms.txt](https://developers.cloudflare.com/magic-transit/llms.txt)).
Health is monitored with tunnel health checks (configurable frequency), endpoint health checks (beta), tunnel health alerts, Network Analytics, GraphQL bandwidth and health queries, traceroutes and packet captures ([Magic Transit llms.txt](https://developers.cloudflare.com/magic-transit/llms.txt)).
Kentik is documented as a partner for attack detection ([Kentik](https://developers.cloudflare.com/magic-transit/partners/kentik/)).
Network Flow can detect attacks and trigger Magic Transit on-demand ([Network Flow integration](https://developers.cloudflare.com/magic-transit/network-flow/)).

### Most useful pages

- https://developers.cloudflare.com/magic-transit/about/
- https://developers.cloudflare.com/magic-transit/get-started/
- https://developers.cloudflare.com/magic-transit/ddos/
- https://developers.cloudflare.com/magic-transit/reference/traffic-steering/
- https://developers.cloudflare.com/reference-architecture/architectures/magic-transit/

## 5. Cloudflare WAN (formerly Magic WAN)

### What it is

An "Enterprise-only" WAN-as-a-Service that connects data centers, offices and clouds over Cloudflare using anycast GRE or IPsec, replacing MPLS and hub-and-spoke backhaul, with Cloudflare Network Firewall integrated ([Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)).
It is standalone; adding Cloudflare One (client, Tunnel, Gateway, Access) needs no migration because both share the same network ([Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)).
The sidebar still says "Magic WAN" while every page says Cloudflare WAN ([home sidebar](https://developers.cloudflare.com/), [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)).

### Structure of the 110 pages

| llms.txt section | What it covers |
| --- | --- |
| Overview, WAN transformation | Product scope; migration from MPLS and SD-WAN with open standards (IPsec, GRE, BGP) ([WAN transformation](https://developers.cloudflare.com/cloudflare-wan/wan-transformation/)) |
| Get started | Enterprise purchase; automatic setup via Cloudflare One Appliance (preferred) or manual setup with third-party routers; MSS clamping 1,436 for GRE and 1,360 for IPsec on the edge router ([get started](https://developers.cloudflare.com/cloudflare-wan/get-started/)) |
| On-ramps | Appliance, GRE/IPsec devices, CNI, Cloudflare Tunnel, the Cloudflare One Client, Multi-Cloud Networking, on-ramp partners ([on-ramps](https://developers.cloudflare.com/cloudflare-wan/on-ramps/)) |
| Security filters | Network Firewall at L3/L4 and Gateway for DNS, network and HTTP ([security filters](https://developers.cloudflare.com/cloudflare-wan/security/)) |
| Cloudflare One integration | Gateway, WARP (Cloudflare One Client) as on-ramp, Tunnel, connectivity options, which security service applies where ([Zero Trust integration](https://developers.cloudflare.com/cloudflare-wan/zero-trust/)) |
| CNI, Load Balancing | Private interconnect on-ramp and load balancing across tunnel endpoints |
| Analytics | Network overview, Network Analytics, NetFlow statistics, traceroutes, packet captures, GraphQL bandwidth and tunnel-health queries |
| Public to private | Proxy public hostnames to private origins over WAN ([private origins](https://developers.cloudflare.com/dns/private-origins/)) |
| configuration (largest) | Appliance (hardware Dell VEP1460 and Virtual Appliance on ESXi 7.0U1+ or Proxmox beta with 8 GB RAM; DHCP server/relay/reservations, link aggregation, NAT for subnets, network segmentation, routed subnets, application-aware breakout and prioritized traffic, maintenance, heartbeat, interrupt window, device metrics); common settings (sites, tunnel health checks and alerts, Magic user roles, custom IKE ID); how-to (tunnel endpoints, routes, Cloudflare source IPs, traceroute); 21 third-party device guides; cloud on-ramps |
| reference | Anti-replay, bandwidth measurement, device compatibility, GRE and IPsec parameters, MTU/MSS, traffic steering, tunnel health checks and alert math, virtual networks |
| troubleshooting | Connectivity, IPsec, routing and BGP, tunnel health |
| legal | Third-party licenses (about 5 MB of the 6 MB) |

Third-party guides as of 2026-10-05: Alibaba Cloud, Aruba EdgeConnect, AWS Transit Gateway, Azure Virtual WAN and VPN Gateway, Cisco IOS XE, Cisco Meraki MX, Cisco SD-WAN (Viptela), Fortinet, Furukawa FITELnet, Google Cloud VPN, Juniper SRX, Oracle Cloud, Palo Alto NGFW, pfSense, SonicWall, Sophos, strongSwan, Ubiquiti, Velocloud, VyOS and Yamaha RTX (`raw/docs/cloudflare-wan/configuration/third-party/`).

### Key technical facts

- IPsec IKE SA supports AES-GCM-16 (128 or 256) or AES-CBC-256, SHA2-256, and key exchange ML-KEM-768 plus DH group 20 (recommended post-quantum hybrid), ML-KEM-1024 plus group 20, or classical groups 20, 14 and 5 ([GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/)).
- Unified Routing (GA 2026-09-18) adds Automatic Return Routing for Internet return traffic, BGP over IPsec and GRE (beta), configurable Cloudflare source IPs, custom client device subnets and Mesh interoperability ([traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/)).
- On Unified Routing, full packet captures are not available, while Network Firewall GeoIP country, ASN lists, account IP lists, threat intel lists and SIP rules are beta ([traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/)).
- Virtual Appliance high availability cannot be added to an existing on-ramp ([Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/)).
- The Appliance cannot share its host with other software and is aimed at 1 Gbps or more ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).

### Most useful pages

- https://developers.cloudflare.com/cloudflare-wan/get-started/
- https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/
- https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/
- https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/

## 6. Network Interconnect (CNI)

### What it is

An "Enterprise-only" private connection from your network to Cloudflare instead of the public Internet, for lower latency, steadier throughput and a smaller attack surface ([CNI](https://developers.cloudflare.com/network-interconnect/)).

### Key concepts

| | Direct | Partner | Cloud |
| --- | --- | --- | --- |
| Port | Physical fiber cross-connect in a shared facility | Virtual connection via partners (Megaport, Equinix Fabric, PacketFabric) | Private link from AWS, GCP or Azure |
| Operations | You order the cross-connect | Partner portal | Cloudflare connects to the cloud provider |

Sources: [CNI](https://developers.cloudflare.com/network-interconnect/), [connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/).
Dataplane v1 is a peering connection to an edge data center using GRE tunnels (GRE-less option for Magic Transit Direct Server Return), and Dataplane v2 uses the Customer Connectivity Router with no GRE and a 1,500-byte MTU both ways ([CNI](https://developers.cloudflare.com/network-interconnect/)).
Use cases: Magic Transit DSR, Magic Transit with egress, Cloudflare WAN and Zero Trust backbone, public peering with AS13335, and Argo Smart Routing via peering ([get started](https://developers.cloudflare.com/network-interconnect/get-started/)).

### Requirements, plans and status (as of 2026-10-05)

- CNI ports are offered at no charge to Enterprise customers; others can peer at Internet exchanges under the open peering policy ([get started](https://developers.cloudflare.com/network-interconnect/get-started/)).
- Prefixes must be `/24` or shorter for IPv4 and `/48` or shorter for IPv6 ([get started](https://developers.cloudflare.com/network-interconnect/get-started/)).
- Optics: v1 10GBASE-LR or 100GBASE-LR, v2 10GBASE-LR or 100GBASE-LR4, single-mode fiber ([get started](https://developers.cloudflare.com/network-interconnect/get-started/)).
- BGP over CNI is closed beta and not available to new customers ([get started](https://developers.cloudflare.com/network-interconnect/get-started/)).
- Direct CNI locations are listed per facility with v1 and v2 device counts (for example Equinix DC2 Ashburn has two of each) ([locations](https://developers.cloudflare.com/network-interconnect/locations/)).
- Planned maintenance on Dataplane v2 in multi-homed PoPs gets at least one week notice, and maintenance alerts exist for v1 ([maintenance](https://developers.cloudflare.com/network-interconnect/maintenance/), [monitoring](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/)).
- Interconnects moved in the dashboard to Connectors > Interconnects on 2026-03-24 ([CNI changelog](https://developers.cloudflare.com/network-interconnect/changelog/)).
- Combining CNI with Tunnel can reduce Tunnel redundancy when CNI advertises only one region ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).

## 7. Spectrum

### What it is

Spectrum is a Layer 4 reverse proxy that puts any TCP or UDP application (MQTT, email, file transfer, version control, games and more) behind Cloudflare to hide the origin and absorb DDoS ([Spectrum](https://developers.cloudflare.com/spectrum/)).
It is "Available on Paid plans", and custom TCP/UDP apps need Enterprise with Spectrum as a paid add-on ([Spectrum](https://developers.cloudflare.com/spectrum/)).

### Protocols per plan (as of 2026-10-05)

| | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Availability | No | Paid add-on | Paid add-on | Yes |
| TCP, UDP, HTTP, HTTPS | No | No | No | Paid add-on |
| Minecraft (one app) | No | Yes | Yes | Yes |
| SSH (one app) | No | Yes | Yes | Yes |
| RDP (one app) | No | No | Yes | Yes |

Source: [protocols per plan](https://developers.cloudflare.com/spectrum/protocols-per-plan/).
Enterprise-only API fields: `origin_dns`, `origin_port`, `proxy_protocol`, `ip_firewall`, `tls` and `argo_smart_routing` ([settings by plan](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/)).

### Key concepts and configuration

- Application types: TCP/UDP proxy straight to the origin, or HTTP/HTTPS to run CDN, Workers and Bot Management on the traffic ([configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
- Each app gets an anycast IPv4 and IPv6 (or IPv6 only); the IPs are not static and should be resolved via DNS, and are not announced from China data centers ([configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
- Static IPs are an Enterprise feature by request (API only), tied to the DNS name ([static IP](https://developers.cloudflare.com/spectrum/about/static-ip/)).
- All TCP ports are supported, and port ranges map edge ranges to equally sized origin ranges, for example `"protocol": "tcp/1000-2000"` to `tcp://192.0.2.1:3000-4000` ([configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
- Origins can be an IP, a CNAME, a load balancer (adding TCP health checks and failover) or a virtual network origin through Tunnel or Cloudflare WAN ([get started](https://developers.cloudflare.com/spectrum/get-started/), [load balancer](https://developers.cloudflare.com/spectrum/about/load-balancer/)).
- Virtual network origins (`virtual_network_id`) work only for TCP and UDP apps, with exactly one `origin_direct` private IP and a single port ([configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
- Client IP: Spectrum origins see Cloudflare IPs unless you enable PROXY protocol v1, v2 or Simple Proxy Protocol for UDP, which is Enterprise-only ([enable Proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/), [Simple Proxy Protocol header](https://developers.cloudflare.com/spectrum/reference/simple-proxy-protocol-header/)).
- Access control: WAF custom rules do not apply; use IP Access rules (`ip_firewall`) ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- DDoS: TCP connections must complete before proxying (moving SYN floods to Cloudflare), floods of the wrong protocol or to unconfigured ports are dropped, and the network-layer DDoS managed ruleset is on by default ([DDoS for Spectrum](https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/)).
- Edge TLS termination modes are off (passthrough), flexible, full and strict, and Universal SSL is not compatible, so advanced or custom certificates are needed ([settings by plan](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/), [limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- Logs: the `spectrum_events` Logpush dataset records connect, disconnect and error events with Spectrum-specific status codes (for example `403` firewall deny) ([event logs](https://developers.cloudflare.com/spectrum/reference/logs/)).
- SMTP: Spectrum acts as a TCP load balancer, not a mail relay, and has no reverse DNS ([configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).

### Limits (as of 2026-10-05)

- 10 unique Spectrum hostnames on Cloudflare-managed IPv4 per account (IPv6-only apps exempt), with BYOIP, IPv6, CNAME sharing or Cloudflare for SaaS as workarounds ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- HTTPS apps do not support HTTP/3 ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- Fragmented UDP packets are dropped at the edge ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- UDP apps work with BYOIP and CDN/Spectrum service bindings but not with Magic Transit service bindings ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- Minecraft Java only, not Bedrock ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- A Spectrum IP completes TCP handshakes on every port but only proxies ports with a configured app ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).
- Proxy protocol is not supported when Spectrum is the on-ramp to Private Network Load Balancing ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/)).

### Most useful pages

- https://developers.cloudflare.com/spectrum/protocols-per-plan/
- https://developers.cloudflare.com/spectrum/get-started/
- https://developers.cloudflare.com/spectrum/reference/configuration-options/
- https://developers.cloudflare.com/spectrum/reference/limitations/

## 8. BYOIP

### What it is

"Enterprise-only": Cloudflare announces your own IP prefixes from all locations and uses them for Magic Transit, Spectrum, CDN services and more, instead of Cloudflare-owned anycast IPs ([BYOIP](https://developers.cloudflare.com/byoip/)).
The contract must cover it, and the BYOIP service-specific terms apply ([get started](https://developers.cloudflare.com/byoip/get-started/)).

### Key concepts

- Requirements: prefix registered with AFRINIC, APNIC, ARIN, LACNIC or RIPE, IRR `route`/`route6` objects with the right `origin`, and valid RPKI ROAs ([get started](https://developers.cloudflare.com/byoip/get-started/)).
- The self-serve flow announces only under Cloudflare's ASN (AS13335); your own ASN needs the account team ([get started](https://developers.cloudflare.com/byoip/get-started/)).
- Minimum sizes are `/24` IPv4 and `/48` IPv6 ([Spectrum BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/)).
- Onboarding for Magic Transit follows the Magic Transit process, not the BYOIP get-started page ([get started](https://developers.cloudflare.com/byoip/get-started/)).
- Service bindings (API only) map IPs to Magic Transit, CDN or Spectrum; Magic Transit must be the default for the whole prefix, individual IPs can be upgraded to CDN or Spectrum, and changes take four to six hours to propagate with likely disruption ([service bindings](https://developers.cloudflare.com/byoip/service-bindings/)).
- Address maps tie IPs to zones and accounts, prefix delegations let other accounts use a prefix, and dynamic advertisement announces or withdraws prefixes on demand ([address maps](https://developers.cloudflare.com/byoip/address-maps/), [prefix delegations](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/), [dynamic advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/)).
- Route Leak Detection alerts on unexpected announcements of your prefixes and is included with BYOIP ([Route Leak Detection](https://developers.cloudflare.com/byoip/route-leak-detection/)).
- Static IPs (Cloudflare-leased, not BYOIP) are an Enterprise add-on, managed with the same address maps ([static IPs](https://developers.cloudflare.com/byoip/concepts/static-ips/)).
- Switching an existing Spectrum app to BYOIP requires deleting and recreating it ([Spectrum BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/)).

API entry point: `POST /accounts/$ACCOUNT_ID/addressing/prefixes` ([get started](https://developers.cloudflare.com/byoip/get-started/)).

## 9. Network Error Logging

NEL is a browser-based reporting system: Cloudflare adds a `report-to` header (group `cf-nel`, `max_age` 31536000) so browsers report failed connections to a Cloudflare endpoint, giving visibility into last-mile failures ([NEL](https://developers.cloudflare.com/network-error-logging/)).
It is available on all plan types; Free and Pro enable it under Account home > Network > Network Error Logging Monitoring, while Business and Enterprise must contact support or the account team ([get started](https://developers.cloudflare.com/network-error-logging/get-started/)).
Reports appear under Analytics & Logs > Edge Reachability and in the `nel_reports` Logpush dataset, showing failure reason, country, last-mile network and the intended data center ([how to](https://developers.cloudflare.com/network-error-logging/how-to/)).
The reference explains signatures: ISP outages show `tcp.timed_out`, `tcp.failed`, `h2.protocol_error` and `h3.protocol_error` from one ASN, transit flaps show short bursts across many ASNs (usually under two minutes), and infrastructure or Cloudflare outages raise `tcp.timed_out`, `tcp.failed` and `tcp.aborted` across networks ([reference](https://developers.cloudflare.com/network-error-logging/reference/)).

## 10. Network Flow

Network Flow (formerly Magic Network Monitoring) analyzes NetFlow v5, v9, IPFIX and sFlow from your routers, plus AWS VPC flow logs via Firehose (beta, API only), to show traffic and detect volumetric DDoS ([Network Flow](https://developers.cloudflare.com/network-flow/), [get started](https://developers.cloudflare.com/network-flow/get-started/), [cloud flow logs](https://developers.cloudflare.com/network-flow/cloud-flow-logs/)).
It is "Available on all plans", and the free version has every enterprise feature but caps registered routers at 10, rules at 25 and flows at 250 per second per account ([free version](https://developers.cloudflare.com/network-flow/network-flow-free/)).
Rules are static threshold, dynamic threshold and sFlow DDoS attack rules, with email, webhook or PagerDuty notifications ([Network Flow llms.txt](https://developers.cloudflare.com/network-flow/llms.txt)).
Enterprise customers can pair it with Magic Transit on-demand to start mitigation automatically when an attack is detected ([Network Flow](https://developers.cloudflare.com/network-flow/)).
Setup registers the router's public IP and sampling rate in the dashboard (Network flow page) before configuring the export ([get started](https://developers.cloudflare.com/network-flow/get-started/)).
Router guides cover NetFlow/IPFIX and sFlow configuration, recommended sampling rates and supported routers, plus tutorials for DDoS testing, encrypting flow data and GraphQL ([Network Flow llms.txt](https://developers.cloudflare.com/network-flow/llms.txt)).
The community channel is `magic-network-monitoring` in Cloudflare's Discord ([free version](https://developers.cloudflare.com/network-flow/network-flow-free/)).

## 11. Plan availability cheat sheet

| Product | Free | Pro / Business | Enterprise | Status (as of 2026-10-05) |
| --- | --- | --- | --- | --- |
| Tunnel | Yes | Yes | Yes | GA |
| Mesh | Yes (Zero Trust Free) | Yes | Yes | Beta |
| Spectrum | No | Paid add-on, one SSH/Minecraft (Pro) or plus RDP (Business) app | TCP/UDP/HTTP/HTTPS as paid add-on | GA |
| Magic Transit | No | No | Yes | GA; Unified Routing GA 2026-09-18; BGP peering beta |
| Cloudflare WAN | No | No | Yes | GA; BGP over IPsec/GRE beta |
| Network Interconnect | Peering via IX only | Peering via IX only | Yes, ports at no charge | GA; BGP over CNI closed beta |
| BYOIP | No | No | Yes | GA |
| Network Error Logging | Yes (self-enable) | Pro self-enable, Business via support | Via account team | GA |
| Network Flow | Free version with limits | Free version | Full, with Magic Transit integration | GA; cloud flow logs beta |
| Programmable Flow Protection | No | No | Magic Transit add-on | Closed beta |

## 12. Build hooks for Web3 projects

These uses apply to teams launching on Solana, Ethereum, Base and Robinhood Chain (an EVM L2 with chain id 4663); node ports and client behavior are the team's own assumptions, and only the Cloudflare behavior is sourced.

1. Expose a self-hosted RPC node (EVM JSON-RPC or a Solana RPC node) through a Tunnel published application, with no inbound ports open on the node host, then protect it with an Access Service Auth policy so only your backend or bots holding a service token can call it ([get started](https://developers.cloudflare.com/tunnel/get-started/), [service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)).
2. WebSocket subscriptions (for example `eth_subscribe` or Solana account subscriptions) pass through Tunnel because Tunnel fully supports WebSockets, but Server-Sent Events do not work on Quick Tunnels ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/), [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)).
3. Keep gRPC streams (for example Geyser-style plugins on a Solana node) on Tunnel private network routes, because gRPC is not supported on public hostnames ([Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)).
4. Run two `cloudflared` replicas per node location for redundancy, and separate tunnels behind a load balancer when you need health-checked failover between several RPC nodes ([configuration](https://developers.cloudflare.com/tunnel/configuration/), [routing](https://developers.cloudflare.com/tunnel/concepts/routing/)).
5. Publish validator or node metrics (Prometheus exporters, Grafana) and indexer dashboards on hostnames behind Access, and scrape `cloudflared`'s own `/metrics` for tunnel health ([observability](https://developers.cloudflare.com/tunnel/observability/), [Grafana tutorial](https://developers.cloudflare.com/tunnel/tutorials/grafana/)).
6. Share a local devnet, fork (Anvil, Hardhat, `solana-test-validator`) or webhook receiver with a teammate using a Quick Tunnel restricted by `--allowed-mail`, keeping in mind the 200 in-flight request cap and no uptime guarantee ([Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)).
7. Let Workers (for example a relayer, keeper or x402 payment Worker) call a private RPC node or database through Workers VPC over Tunnel instead of a public endpoint ([integrations](https://developers.cloudflare.com/tunnel/integrations/)).
8. Use Mesh to link archive nodes, indexers and operator laptops by private Mesh IP for long-lived bidirectional connections such as database replication, with Gateway network policies as the ACL, on the free beta ([Mesh concepts](https://developers.cloudflare.com/mesh/concepts/)).
9. For public p2p or gossip ports that peers must reach over raw TCP or UDP, Tunnel is the wrong tool because it is client-initiated and hides source IPs; Spectrum can proxy arbitrary TCP and UDP only on Enterprise as a paid add-on, and Pro or Business only get one SSH, Minecraft or RDP app ([connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/), [protocols per plan](https://developers.cloudflare.com/spectrum/protocols-per-plan/)).
10. If Spectrum fronts node ports, plan for these documented behaviors: the node sees Cloudflare IPs unless Proxy Protocol (Enterprise) is enabled and the node software parses it, fragmented UDP is dropped, port ranges are supported, IPs are dynamic unless you buy static IPs or BYOIP, and IP Access rules (not WAF rules) are the allowlist tool ([enable Proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/), [limitations](https://developers.cloudflare.com/spectrum/reference/limitations/), [configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
11. A validator or RPC provider that owns a `/24` and an ASN can use Magic Transit (Enterprise) to keep real source IPs while scrubbing L3/L4 DDoS, and Programmable Flow Protection (closed beta add-on) lets it write eBPF filters for a custom UDP protocol ([get started](https://developers.cloudflare.com/magic-transit/get-started/), [Programmable Flow Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/)).
12. Run Network Flow free (10 routers, 250 flows per second) on a node operator's edge router to see volumetric attacks against validator IPs before paying for mitigation ([free version](https://developers.cloudflare.com/network-flow/network-flow-free/)).
13. Turn on Network Error Logging for the dapp and RPC zones to see when users in a given ASN or country cannot reach the frontend during a launch ([NEL](https://developers.cloudflare.com/network-error-logging/)).
14. BYOIP Route Leak Detection alerts if someone announces your prefixes, a guard against BGP hijacks of RPC or frontend IPs ([Route Leak Detection](https://developers.cloudflare.com/byoip/route-leak-detection/)).

## 13. Gaps and contradictions

- Spectrum plus Tunnel: the Spectrum limitations page and the Tunnel integrations page say Spectrum with Tunnel is supported only for HTTP/HTTPS apps and recommend Private Network Load Balancing for L4, while the Spectrum get-started and configuration options pages document TCP/UDP virtual-network origins through Tunnel, and the Cloudflare One published-applications page says TCP or UDP apps can use that path ([limitations](https://developers.cloudflare.com/spectrum/reference/limitations/), [integrations](https://developers.cloudflare.com/tunnel/integrations/), [get started](https://developers.cloudflare.com/spectrum/get-started/), [published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)).
- Spectrum Argo Smart Routing is "only available for TCP applications with traffic_type set to direct" on the settings-by-plan page but "available for TCP and UDP (beta) applications" on the configuration options page ([settings by plan](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/), [configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)).
- Spectrum availability reads "Available on Paid plans" on the overview while the plan table makes Pro and Business a "Paid add-on" and arbitrary TCP/UDP Enterprise-only ([Spectrum](https://developers.cloudflare.com/spectrum/), [protocols per plan](https://developers.cloudflare.com/spectrum/protocols-per-plan/)).
- BGP over Direct CNI was announced as usable from the dashboard in the 2024-12-17 changelog, while the get-started page and the WAN routing table say BGP over CNI is closed beta and not available to new customers ([CNI changelog](https://developers.cloudflare.com/network-interconnect/changelog/), [get started](https://developers.cloudflare.com/network-interconnect/get-started/)).
- The CNI monitoring page still says "go to Interconnects" although the 2026-03-24 changelog moved Interconnects under Connectors ([monitoring](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/), [CNI changelog](https://developers.cloudflare.com/network-interconnect/changelog/)).
- Naming drift: the sidebar says "Magic WAN" while the docs say Cloudflare WAN, Magic Transit and WAN pages still offer "Enable Magic user roles", the CNI changelog still says "Magic routing table", and Cloudflare One Appliance was "Magic WAN Connector" ([home sidebar](https://developers.cloudflare.com/), [Magic roles](https://developers.cloudflare.com/magic-transit/how-to/enable-magic-roles/), [CNI changelog](https://developers.cloudflare.com/network-interconnect/changelog/), [connectivity options](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/)).
- The WAN `llms.txt` describes "WAN transformation" as "Transform WAN traffic with header and protocol modifications", but the page is a migration guide from MPLS and SD-WAN ([WAN transformation](https://developers.cloudflare.com/cloudflare-wan/wan-transformation/)).
- Tunnel, Mesh and Cloudflare WAN are each documented twice, once as standalone products and once under `cloudflare-one/networks/connectors/`, and dashboard paths differ between copies ("Networking > Tunnels" versus Zero Trust > Networks) ([Tunnel](https://developers.cloudflare.com/tunnel/), [C1 Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)).
- The Tunnel overview advertises "Supports HTTP, HTTPS, TCP, SSH, RDP" on public hostnames, while the Tunnels FAQ says gRPC is not supported on public hostnames, and non-HTTP public routes need `cloudflared` on the client ([Tunnel](https://developers.cloudflare.com/tunnel/), [Tunnels FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/), [routing](https://developers.cloudflare.com/tunnel/concepts/routing/)).
- The Network Error Logging get-started page says it is "available to users on all plan types" but only Free and Pro can enable it themselves ([get started](https://developers.cloudflare.com/network-error-logging/get-started/)).
- IDS is listed as a Network Firewall feature for Magic Transit, but on Unified Routing it is "not available for Magic Transit accounts", and Unified Routing is now recommended for all new accounts ([IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/), [Magic Transit changelog](https://developers.cloudflare.com/magic-transit/changelog/)).
- No page gives prices for Spectrum, Magic Transit, Cloudflare WAN, CNI or BYOIP; all are "contact your account team".
- The docs do not discuss blockchain p2p or validator traffic, so whether a given node client accepts PROXY protocol or tolerates Cloudflare-terminated TCP is untested in these sources.
