# Domains & DNS (Protect & Connect)

This file covers the Protect & Connect > Domains & DNS dropdown of the Cloudflare developer docs as mirrored on 2026-10-05: authoritative DNS, the 1.1.1.1 public resolver, Registrar, Email Routing (the inbound half of Email Service) and DMARC Management, plus the Web3 gateways (Ethereum and IPFS), which are not in this dropdown but attach to DNS hostnames in a zone.
Authoritative DNS is free on every plan, while partial (CNAME) setups need Business, and zone transfers, subdomain zones, Foundation DNS, NSEC3, zone holds, Internal DNS and DNS Firewall are Enterprise features.
Registrar sells domains at registry cost, forces Cloudflare nameservers (full setup), offers one-click DNSSEC through CDS/CDNSKEY scanning, and gained a beta registration API on 2026-04-15.
Email Routing forwards inbound mail to verified addresses or Workers for free, with unlimited inbound volume and hard caps of 200 rules per domain and 200 destination addresses per account.
The Web3 gateways are a usage-billed add-on on every plan that proxies a hostname to Cloudflare-run Ethereum nodes (Mainnet and Sepolia only) or IPFS nodes (DNSLink on all plans, Universal Path on Enterprise), while Cloudflare's free public IPFS gateway hostnames were moved to Interplanetary Shipyard and stopped serving IPFS on 2024-08-14.
Everything that moves (plans, limits, prices, beta or GA status) is stated as of 2026-10-05.

## Table of contents

1. [Where this sits in the sidebar](#1-where-this-sits-in-the-sidebar)
2. [DNS (authoritative)](#2-dns-authoritative)
3. [1.1.1.1 (public resolver)](#3-1111-public-resolver)
4. [Registrar](#4-registrar)
5. [Email Routing](#5-email-routing)
6. [DMARC Management](#6-dmarc-management)
7. [Web3 gateways (Ethereum and IPFS)](#7-web3-gateways-ethereum-and-ipfs)
8. [Build hooks for Web3 projects](#8-build-hooks-for-web3-projects)
9. [Gaps and contradictions](#9-gaps-and-contradictions)

---

## 1. Where this sits in the sidebar

The home sidebar (`raw/nav/home-sidebar.md`) lists the Domains & DNS dropdown as: DNS (https://developers.cloudflare.com/dns/), 1.1.1.1 (https://developers.cloudflare.com/1.1.1.1/), Registrar (https://developers.cloudflare.com/registrar/), Email Routing (which links to https://developers.cloudflare.com/email-service/) and DMARC Management (https://developers.cloudflare.com/dmarc-management/).
Web3 is not in this dropdown or anywhere else in the home sidebar; the docs-wide index (https://developers.cloudflare.com/llms.txt) files it under "Application performance".
The Email Routing sidebar entry now lands on the combined Email Service product, whose dashboard home is **Compute > Email Service**, so sending is covered in `build/01-compute.md` and this file only covers inbound routing.

| Product | Plans (as of 2026-10-05) | Status (as of 2026-10-05) | Docs |
| --- | --- | --- | --- |
| DNS | All plans, features vary by plan | GA; Internal DNS GA 2026-07-15; Private origins closed beta | https://developers.cloudflare.com/dns/ |
| 1.1.1.1 | Free public service, "Available on all plans" | GA, no SLA | https://developers.cloudflare.com/1.1.1.1/ |
| Registrar | All plans, at-cost pricing | GA; Registrar API beta since 2026-04-15 | https://developers.cloudflare.com/registrar/ |
| Email Routing | Workers Free and Workers Paid | GA (Email Sending is the beta half) | https://developers.cloudflare.com/email-service/ |
| DMARC Management | All plans with Cloudflare DNS | Labelled beta on its enable and statistics pages | https://developers.cloudflare.com/dmarc-management/ |
| Web3 gateways | Add-on, usage-based billing on all plans | GA since 2022-05-16 per blog | https://developers.cloudflare.com/web3/ |

---

## 2. DNS (authoritative)

### 2.1 What it is

Cloudflare DNS is an authoritative DNS service on Cloudflare's anycast network, marked "Available on all plans", that also protects against DDoS and route leaks or hijacking (https://developers.cloudflare.com/dns/).
Its three headline features are DNS records, DNSSEC (including multi-signer DNSSEC) and CNAME flattening.
Enterprise customers can also run private DNS with Internal DNS and proxy public hostnames to private origins (beta).
The FAQ says DNS is free on all plans, that Cloudflare "never limits or caps DNS queries", that Free, Pro and Business are not charged for queries, and that for Enterprise the monthly query count is a pricing input for a custom quote (https://developers.cloudflare.com/dns/faq/).

### 2.2 Key concepts

- **Zone**: the administrative boundary for a domain and its subdomains; each domain added to an account is a zone (https://developers.cloudflare.com/dns/concepts/).
- **Zone apex**: the top of a zone, written `@` in the record name field; with subdomain setup (Enterprise) a subdomain such as `sub.example.com` can itself be a zone apex.
- **Authoritative nameservers**: the servers that give the final answer; Cloudflare offers standard, advanced (Foundation DNS) and custom nameservers (https://developers.cloudflare.com/dns/nameservers/).
- **Proxy status**: A, AAAA and CNAME records can be Proxied (orange cloud, answered with Cloudflare anycast IPs so HTTP/HTTPS goes through Cloudflare) or DNS-only (grey cloud, answered with the origin IP) (https://developers.cloudflare.com/dns/proxy-status/).
- **Zone statuses**: Initializing, Pending, Active, Moved, Deleted, Purged (https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/).
- The setups page warns paid-plan users not to put production traffic on pending zones, especially without zone holds (https://developers.cloudflare.com/dns/zone-setups/).

### 2.3 Zone setups and plan availability

| Setup | Free | Pro | Business | Enterprise | Source |
| --- | --- | --- | --- | --- | --- |
| Primary (full): Cloudflare is the authoritative provider | Yes | Yes | Yes | Yes | https://developers.cloudflare.com/dns/zone-setups/full-setup/ |
| CNAME (partial): keep your DNS provider, proxy individual hostnames via `{hostname}.cdn.cloudflare.net` | No | No | Yes | Yes | https://developers.cloudflare.com/dns/zone-setups/partial-setup/ |
| Zone transfers: Cloudflare as primary (outgoing) or secondary (incoming), AXFR and IXFR | No | No | No | Yes | https://developers.cloudflare.com/dns/zone-setups/zone-transfers/ |
| Subdomain setup: a delegated subdomain as its own zone, possibly in another account | No | No | No | Yes | https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/ |

- Partial setups are not supported on Cloudflare Registrar domains, and DDoS protection for attacks on DNS infrastructure only applies to full setups because partial zones do not use Cloudflare nameservers.
- On partial setups, if the same zone is added to different accounts, the last account to complete setup gains ownership.
- The maximum number of linked peers per zone is 30, each peer carries one TSIG, and Cloudflare always supports IXFR for outgoing transfers.
- Secondary DNS overrides let you proxy records on a secondary zone, but choosing pre-signed DNSSEC makes Cloudflare treat those records as DNS-only (https://developers.cloudflare.com/dns/proxy-status/limitations/).
- Subdomain setup combinations: a Full or Secondary parent can have a Full or Secondary child but not a Partial child; a Partial parent can have Full, Secondary or Partial children.
- DNS-only zone mode can be set per zone (`PATCH /zones/{zone_id}/dns_settings` with `{"zone_mode":"dns_only"}`) or as an account default for new zones (`PATCH /accounts/{account_id}/dns_settings` with `zone_defaults.zone_mode`).
- Conversions exist between all three of full, partial and secondary (six conversion pages under https://developers.cloudflare.com/dns/zone-setups/conversions/).

### 2.4 DNS records

Supported types are grouped as IP resolution (A, AAAA, CNAME), email authentication (MX, DKIM, SPF, DMARC), and specialized (TXT, CAA, SRV, SVCB and HTTPS, PTR, SOA, NS, DS and DNSKEY), plus URI, NAPTR, SSHFP, TLSA, SMIMEA and CERT (https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/).
CAA records specify which certificate authorities may issue certificates for the domain (details at https://developers.cloudflare.com/ssl/edge-certificates/caa-records/).
Cloudflare supports up to 10 NS records per delegation name and recommends seven or fewer, citing RFC 1912.
For proxied names with HTTP/2 or HTTP/3 and Universal SSL, Cloudflare synthesizes HTTPS records automatically and ignores manually added HTTPS records; a manual HTTPS record is only served if every record with that name is DNS-only.

**Record quotas** (https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota, as of 2026-10-05):

| Plan | Quota |
| --- | --- |
| Free zones created before 2024-09-01 00:00 UTC | 1,000 records per zone |
| Free zones created on or after 2024-09-01 00:00 UTC | 200 records per zone |
| Pro | 3,500 records per zone |
| Business | 3,500 records per zone |
| Enterprise | Per-account quota instead, default 1,000,000 public records and a separate 1,000,000 internal records; higher on request |

- Records that other Cloudflare services create on your behalf (for example Email Routing's TXT and MX records) count toward the quota, with a small buffer so those services are not disrupted.
- The account-level Enterprise quota was introduced on 2026-06-10 (https://developers.cloudflare.com/dns/changelog/).
- Quota and usage are readable through the DNS usage API (zone and account variants linked from the quota section).

**Record attributes** (comments and tags, full and partial zones only; https://developers.cloudflare.com/dns/manage-dns-records/reference/record-attributes/):

|  | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Comment characters | 100 | 500 | 500 | 500 |
| Comments per record | 1 | 1 | 1 | 1 |
| Tags | No | Yes | Yes | Yes |
| Tags per record | N/A | 20 | 20 | 20 |
| Tag name / value characters | N/A | 32 / 100 | 32 / 100 | 32 / 100 |

- Reserved `cf-` tags on export or import carry Cloudflare settings, for example `cf-flatten-cname`.
- **Batch changes**: one `/batch` API call can contain deletes, patches, puts and posts, executed in that order, all-or-nothing; the maximum records per action is 200 on Free and 3,500 on Pro, Business and Enterprise (https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/).
- **Import and export**: BIND zone files up to 256 KiB, API rate limit three requests per minute per user (https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/).
- **TTL**: proxied records are fixed at Auto (300 seconds); DNS-only records accept 30 seconds (Enterprise) or 60 seconds (other plans) up to one day (https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/).
- The FAQ says changes take effect globally within five minutes, usually less.
- **Shadowed records**: since 2026-09-14 all zones show warnings for records sitting at or below a subdomain delegation, and the records API returns shadow metadata with `include_shadow_metadata=true`.
- The DNS records page got a new dashboard UX rolled out from 2026-05-20 (Free first, Enterprise 2026-06-08 to 2026-07-03).

### 2.5 Proxy status

- Only A, AAAA and CNAME records that serve HTTP or HTTPS can be proxied; MX, TXT and others are always DNS-only (https://developers.cloudflare.com/dns/proxy-status/).
- If one A or AAAA record on a name is proxied, all A and AAAA records on that name are treated as proxied, and a hostname is proxied if any CNAME in its chain is proxied.
- A CNAME to a zone in a different Cloudflare account returns Error 1014 (CNAME Cross-User Banned).
- Some CNAME targets cannot be proxied, mainly DKIM and verification targets such as `dkim.amazonses.com`, `onmicrosoft.com` subdomains and `acm-validations.aws` subdomains (https://developers.cloudflare.com/dns/proxy-status/limitations/).
- While a zone is pending (up to 24 hours), proxied records answer with origin IPs, so Cloudflare recommends rotating origin IPs after activation.
- Non-HTTP or non-standard-port traffic needs Spectrum.
- **Enforce DNS-only** (`enforce_dns_only`, added 2026-04-28) is an API-only account-level break-glass that makes every proxied record in the account answer with origin IPs, removing DDoS, WAF and caching for all zones; it excludes Spectrum, Tunnel CNAMEs, R2 custom domains, Web3 gateways and Workers custom domains (https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/).

### 2.6 DNSSEC

- Enabling DNSSEC signs the zone, publishes keys and generates the DS record you add at your registrar; dashboard path **DNS > Settings > Enable DNSSEC** (https://developers.cloudflare.com/dns/dnssec/).
- Cloudflare's preferred algorithm is 13 (ECDSA Curve P-256 with SHA-256); if your registrar or TLD lacks it, the docs suggest asking the registrar, switching registrar, filing an ICANN complaint, or contacting the TLD.
- Cloudflare automatically adds DS records for Cloudflare Registrar domains and for `.ch` and `.cz` domains.
- Cloudflare publishes CDS and CDNSKEY records so RFC 8078 registrars can update the DS automatically (https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/).
- When onboarding a domain that already has DNSSEC, you must either disable it at the registrar and wait for the DS TTL (commonly 24 to 48 hours) to expire, or use the zero-downtime active migration with multi-signer DNSSEC if the old provider accepts external DNSKEYs (https://developers.cloudflare.com/dns/dnssec/dnssec-active-migration/).
- Changing nameservers before the old DS TTL expires makes validating resolvers return SERVFAIL.
- **Multi-signer DNSSEC** follows RFC 8901 model 1 (one shared KSK) or model 2 (each provider's own KSK, two DS records); Cloudflare recommends model 2 and, when enabled, lets you add external DNSKEYs and signs them with Cloudflare's KSK (https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/).
- Multi-provider DNS on a primary zone requires multi-signer DNSSEC if DNSSEC is on (https://developers.cloudflare.com/dns/nameservers/nameserver-options/).
- **NSEC3**: Cloudflare's default negative answers use compact denial of existence (RFC 9824) which prevents zone walking; NSEC3 is available only on Enterprise, via `PATCH /zones/{zone_id}/dnssec` with `dnssec_use_nsec3: true` (https://developers.cloudflare.com/dns/dnssec/enable-nsec3/).
- **Secondary zones** have three DNSSEC options: multi-signer, live signing and pre-signed (https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/).
- **Foundation DNS** lets Enterprise accounts request a ZSK/KSK pair unique to the account (https://developers.cloudflare.com/dns/foundation-dns/dnssec-keys/).
- **Post-quantum**: the 2026-09-10 blog says 1.1.1.1 now validates ML-DSA-44 (DNSSEC algorithm 18) and that ML-DSA-44 signing in Cloudflare Authoritative DNS and DS support in Cloudflare Registrar are the "next step" and "will be available to all customers for free" (https://blog.cloudflare.com/post-quantum-dnssec-1111/); the authoritative DNS docs do not yet mention it.

### 2.7 CNAME flattening

- Cloudflare resolves the CNAME chain and returns the final IPs, which allows a CNAME at the apex (https://developers.cloudflare.com/dns/cname-flattening/).
- Apex CNAMEs are flattened by default on all plans; proxied CNAMEs are always flattened; same-zone targets are flattened regardless of the setting (https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/).
- Paid zones can flatten all CNAMEs (`flatten_all_cnames: true` on the zone DNS settings) or individual records (`settings.flatten_cname: true` per record, tagged `cf-flatten-cname` on export).
- Flattening can break third-party domain verification that expects the CNAME itself, and a dangling CNAME returns NODATA.

### 2.8 Nameservers

- **Standard**: two `<name>.ns.cloudflare.com` nameservers auto-assigned per zone; IPs are static (https://developers.cloudflare.com/dns/nameservers/).
- **Advanced** (Foundation DNS, Enterprise): three per zone, `<color>.foundationdns.com`, `.net` and `.org`.
- **Custom (vanity)**: zone custom nameservers on Business and Enterprise; account custom nameservers on Enterprise or on Business after contacting Support; tenant custom nameservers API-only for tenant owners; each set has two to five names (https://developers.cloudflare.com/dns/nameservers/custom-nameservers/).
- Custom nameservers do not get the advantages of Foundation DNS advanced nameservers, so the docs say use one or the other.
- **Assignment**: "To prevent domain hijacking, you can no longer preset Cloudflare nameservers at your registrar before creating the respective zone in Cloudflare"; a preset domain gets a new nameserver set (https://developers.cloudflare.com/dns/nameservers/nameserver-options/).
- Once a zone is created its nameservers cannot be changed, "not even by Cloudflare Support".
- **DNS zone defaults** (Enterprise) can choose randomized standard, advanced, or account custom nameservers for new zones.
- **Multi-provider DNS** (optional on full, forced on secondary) stops Cloudflare ignoring apex NS records and lets a zone activate with other providers' nameservers at the registrar.
- **Nameserver TTL** defaults to 86,400 seconds and accepts 30 to 86,400 seconds; it is part of Foundation DNS.

### 2.9 Foundation DNS (Enterprise only)

Foundation DNS bundles advanced nameservers (strategically distributed IPs, reduced exposure to incidents and software regressions, more consistent assignment), account-unique DNSSEC keys, zone defaults, account custom nameservers, custom SOA and nameserver TTL; advanced nameservers and unique keys are opt-in (https://developers.cloudflare.com/dns/foundation-dns/).

### 2.10 Internal DNS (Enterprise, GA since 2026-07-15)

- Authoritative DNS for private zones that get no Cloudflare nameservers and can only be queried through the Cloudflare Gateway resolver; zones are grouped into views, which Gateway resolver policies select by query context such as source IP (https://developers.cloudflare.com/dns/internal-dns/).
- Included with Cloudflare Gateway for Enterprise customers, no extra SKU; open beta from 2026-03-31, GA 2026-07-15 (https://developers.cloudflare.com/dns/changelog/).
- Reference zones let a zone fall through to another internal zone; a resolver policy can fall back to public DNS (`public_dns`) on REFUSED, NXDOMAIN or CNAME responses.
- Create with `POST /zones` and `"type": "internal"`; in Terraform, the same `cloudflare_zone` resource with `type = "internal"` (https://developers.cloudflare.com/dns/internal-dns/get-started/).

### 2.11 DNS Firewall (Enterprise-only paid add-on)

DNS Firewall proxies all queries for your own authoritative nameservers through Cloudflare, caching answers and absorbing DDoS, with per-data-center rate limiting, min and max cache TTL, ANY blocking and random prefix attack mitigation (https://developers.cloudflare.com/dns/dns-firewall/).
A refreshed dashboard (2026-07-09) exposes settings that were API-only, such as attack mitigation, rate limiting, negative TTL and resolver subnet.

### 2.12 Private origins (Enterprise, closed beta)

Proxies public hostnames to origins in a private network through Cloudflare WAN IPsec tunnels so CDN, WAF and cache apply; access is by request to the account team (https://developers.cloudflare.com/dns/private-origins/).

### 2.13 Analytics, logs and audit

DNS analytics (dashboard and GraphQL `dnsAnalyticsAdaptive` / `dnsAnalyticsAdaptiveGroups`) by plan (https://developers.cloudflare.com/dns/additional-options/analytics/):

|  | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Max interval (zone) | 30 days | 31 days | 31 days | 62 days |
| Max interval (account) | 7 days | 7 days | 7 days | 62 days |
| History (zone) | 31 days | 31 days | 31 days | 62 days |
| History (account) | 8 days | 8 days | 8 days | 62 days |

- Per-query DNS logs through Logpush are Enterprise only.
- Account Audit Logs v2 record user and system actions across about 95% of products, are kept 18 months (90 days in the UI), and can be exported by Logpush (https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).
- **Zone holds** (Enterprise only, on by default for Enterprise zones) block anyone else from adding your zone to another Cloudflare account, optionally including subdomains and custom hostnames (https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/).

### 2.14 Configuration surfaces

- **Dashboard**: zone **DNS > Records**, **DNS > Settings** (DNSSEC, CNAME flattening, multi-provider), **DNS > Analytics**; account **Configurations > DNS Settings > DNS Zone Transfers**; account **DNS Firewall**.
- **API**: zone records (`/zones/{zone_id}/dns_records`, including `/batch`), DNSSEC (`/zones/{zone_id}/dnssec`), zone and account DNS settings, usage, zone transfer peers, ACLs and TSIGs (https://developers.cloudflare.com/api/resources/dns/).
- **Terraform**: the tutorial creates records with `resource "cloudflare_dns_record"` (fields `zone_id`, `name`, `content`, `type`, `ttl = 1` for Auto, `proxied`, `comment`) (https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/), and subdomain zones with `resource "cloudflare_zone"` and `type = "full"` (https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/).
- **Domain Connect** templates are supported with Cloudflare as DNS provider (https://developers.cloudflare.com/dns/reference/domain-connect/).

### 2.15 Most useful DNS pages

- Overview: https://developers.cloudflare.com/dns/
- Setups and plan matrix: https://developers.cloudflare.com/dns/zone-setups/
- Record quotas: https://developers.cloudflare.com/dns/manage-dns-records/
- Record types: https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/
- Proxy status and limitations: https://developers.cloudflare.com/dns/proxy-status/ and https://developers.cloudflare.com/dns/proxy-status/limitations/
- DNSSEC: https://developers.cloudflare.com/dns/dnssec/ and https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/
- Nameserver options: https://developers.cloudflare.com/dns/nameservers/nameserver-options/
- Analytics: https://developers.cloudflare.com/dns/additional-options/analytics/
- Changelog: https://developers.cloudflare.com/dns/changelog/
- FAQ: https://developers.cloudflare.com/dns/faq/

---

## 3. 1.1.1.1 (public resolver)

### 3.1 What it is

1.1.1.1 is Cloudflare's free public recursive resolver, operated in partnership with APNIC, which provided the address (https://developers.cloudflare.com/1.1.1.1/ and https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/).
It is DNSSEC-validating, sends the DO flag on every query, does not send EDNS Client Subnet (except to Akamai's debug domain `whoami.ds.akahelp.net`), and answers ANY with NOTIMPL (https://developers.cloudflare.com/1.1.1.1/faq/).

### 3.2 Addresses and families (https://developers.cloudflare.com/1.1.1.1/ip-addresses/)

| Resolver | IPv4 | IPv6 | DoH | DoT hostname |
| --- | --- | --- | --- | --- |
| 1.1.1.1 (no filtering) | `1.1.1.1`, `1.0.0.1` | `2606:4700:4700::1111`, `2606:4700:4700::1001` | `https://cloudflare-dns.com/dns-query` (also `https://one.one.one.one/dns-query`) | `one.one.one.one` |
| Families, block malware | `1.1.1.2`, `1.0.0.2` | `2606:4700:4700::1112`, `2606:4700:4700::1002` | `https://security.cloudflare-dns.com/dns-query` | `security.cloudflare-dns.com` |
| Families, block malware and adult content | `1.1.1.3`, `1.0.0.3` | `2606:4700:4700::1113`, `2606:4700:4700::1003` | `https://family.cloudflare-dns.com/dns-query` | `family.cloudflare-dns.com` |

Families blocks malware and phishing (and optionally adult content) under the same privacy commitments; miscategorizations are reported through Radar (https://developers.cloudflare.com/1.1.1.1/setup/).

### 3.3 Encryption

- **DoT** on port 853 per RFC 7858, TLS 1.2 and 1.3 (https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/).
- **DoH** on port 443 over HTTP/1, HTTP/2 and HTTP/3, with a JSON API (`accept: application/dns-json`) and the RFC 8484 wireformat (https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/).
- The DoH JSON `data` formatting changed in a breaking way from 2026-07-28 (presentation format for CAA, SVCB, HTTPS, TLSA and others; numeric DNSSEC algorithm ids); the changelog says the JSON format has no RFC and is not stable, so use wireformat for stability (https://developers.cloudflare.com/1.1.1.1/changelog/).
- **ODoH** (RFC 9230, flagged as experimental and not IETF-endorsed): 1.1.1.1 acts as a target at `odoh.cloudflare-dns.com`, usable with clients such as dnscrypt-proxy (https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/).
- **Tor**: 1.1.1.1 is reachable as an onion service (https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/).
- **WARP**: the iOS and Android 1.1.1.1 apps default to WARP mode, which encrypts all HTTP traffic including DNS; the overview points to the WARP client for whole-device encryption (https://developers.cloudflare.com/1.1.1.1/setup/ios/ and https://developers.cloudflare.com/warp-client/).

### 3.4 DNSSEC validation

- The DNSKEY page (last updated 2026-05-05) lists RSA/SHA-1, RSA/SHA-256, RSA/SHA-512, RSASHA1-NSEC3-SHA1, ECDSAP256SHA256, ECDSAP384SHA384 and ED25519 (https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/).
- The 2026-09-10 blog adds ML-DSA-44 (algorithm 18) validation and a stricter local policy: if a zone's authenticated DS set includes a supported post-quantum algorithm, at least one ML-DSA-44 path must validate, which blocks downgrade to classical signatures; test with `dig @1.1.1.1 valid.mldsa44.dnstest.dev +dnssec` (https://blog.cloudflare.com/post-quantum-dnssec-1111/).
- The same post says about 85% of 1.1.1.1 queries arrive over UDP and that the Big Pineapple platform behind it also serves Gateway DNS.
- RFC 8509 root key trust anchor sentinels were added 2026-09-24, testable with `root-key-sentinel-is-ta-38696.dnstest.dev` for KSK-2024.

### 3.5 Privacy commitments (policy dated 2024-03-27)

- No selling or sharing personal data and no ad targeting.
- Source IPs are not written to non-volatile storage, except randomly sampled packets from at most 0.05% of traffic for troubleshooting and DoS mitigation.
- IPs are truncated (last octet for IPv4, last 80 bits for IPv6) and truncated IPs are deleted within 25 hours.
- Resolver logs (fields listed on the page) are deleted within 25 hours, except aggregates that may be kept indefinitely for Radar.
- Only APNIC gets access to anonymized logs, never client IPs.
- A top-four accounting firm audits the practices.
- Government blocking requests would be legally challenged and reported in the transparency report (https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/).
- The Firefox resolver and the consumer apps have separate privacy terms (https://developers.cloudflare.com/1.1.1.1/privacy/).

### 3.6 Limits, support and tools

- No SLA and limited support; Cloudflare points anyone needing an SLA to Cloudflare Gateway (https://developers.cloudflare.com/1.1.1.1/infrastructure/sla-and-support/).
- A public Purge Cache tool refreshes 1.1.1.1's cache for a name (https://one.one.one.one/purge-cache/).
- Extended DNS error codes, IPv6-only network guidance and network operator notes are under https://developers.cloudflare.com/1.1.1.1/infrastructure/.

---

## 4. Registrar

### 4.1 What it is

Cloudflare Registrar ("Available on all plans") sells and renews domains at the registry and ICANN price with no markup, redacts WHOIS by default, and offers free one-click DNSSEC (https://developers.cloudflare.com/registrar/).
Every Registrar domain must use Cloudflare nameservers on a full setup; you cannot point it at third-party nameservers, only delegate subdomains or use custom (vanity) nameservers on Business or Enterprise (https://developers.cloudflare.com/registrar/faq/).
Partial (CNAME) setups are not supported for Registrar domains (https://developers.cloudflare.com/dns/zone-setups/partial-setup/).

### 4.2 TLDs and registration

- "Over 400" TLDs per the TLD page (last updated 2026-05-15), with the full list at https://www.cloudflare.com/tld-policies/ (https://developers.cloudflare.com/registrar/top-level-domains/).
- `.ai` and `.shop` were added 2025-03-27 (https://developers.cloudflare.com/changelog/post/2025-03-27-ai-domains-available/).
- Internationalized domain names (IDNs, Punycode `xn--`) are not supported.
- `.us` and `.uk` have extra pages.
- Most TLDs allow up to ten years per term; `.co` caps at five per the FAQ.
- A verified account email is required; ICANN registrant email verification is required, and an unverified or expired verification puts the domain on hold with parking nameservers until verified (https://developers.cloudflare.com/registrar/get-started/register-domain/).
- Contact data must be ASCII.
- Auto-renew is on by default in the dashboard, first attempt about 30 days before expiry, last the day before; renewals are at registry list price, final and non-refundable (https://developers.cloudflare.com/registrar/account-options/renew-domains/).

### 4.3 Pricing

- At cost: "You only pay what is charged by registries and ICANN" (https://developers.cloudflare.com/registrar/about/).
- The FAQ's pricing answer just links to https://www.cloudflare.com/learning/dns/what-is-cloudflare-registrar/, so the docs contain no price list.
- The Registrar API guide shows example responses of USD 8.57 for a `.com`, 10.11 for a `.dev` and 11.00 for a `.app`, but these are illustrative examples, not a price table (https://developers.cloudflare.com/registrar/registrar-api/).
- Transfers in cost one year of registration at cost for most gTLDs (an ICANN requirement), while `.uk` and `.nz` transfers are free and add no year.
- Registrations, renewals and transfers are non-refundable.

### 4.4 Transfers

- **In**: the domain must already be an Active full-setup zone, at least 60 days old, not transferred in the last 60 days, with no registrant name, organization or email change in the last 60 days; disable DNSSEC first, unlock at the old registrar (`clientTransferProhibited` must clear), get the auth/EPP code, pay, then approve at the old registrar (up to five days) (https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/).
- Wait 45 days after a renewal at the old registrar, or the registry may not add the paid year.
- Shopify, Block and Wix domains must go to another registrar first and wait 60 days.
- **Out**: **Configuration > Unlock** gives an auth code; rejecting the outbound request makes Cloudflare reapply the registrar lock (https://developers.cloudflare.com/registrar/account-options/transfer-out-from-cloudflare/).
- The docs warn that anyone with Super Administrator or Administrator rights on a zone can unlock domains and get auth codes, so be careful who holds those roles.
- **Between Cloudflare accounts**: domain older than 10 days, verified registrant email, DNSSEC off, not locked or in redemption; target account approves within five days; the domain is then transfer-locked for 30 days and all source configuration is lost (https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/).
- Approving a Change of Registrant applies a 60-day transfer lock unless you opt out.

### 4.5 Security features

- **DNSSEC**: one click under **Manage Domains > Configuration > Enable DNSSEC**; Cloudflare publishes CDS and CDNSKEY and Registrar scans them and sends the DS to the registry, taking one to two days; WHOIS then shows `signedDelegation` (https://developers.cloudflare.com/registrar/get-started/enable-dnssec/).
- **Registrar lock**: domains are locked and must be explicitly unlocked to transfer out; API registrations return `"locked": true`.
- **WHOIS redaction** is free where the registry allows; state or province and country stay public; WHOIS and RDAP lookups at https://rdap.cloudflare.com/; third parties contact registrants through an abuse form (https://developers.cloudflare.com/registrar/account-options/whois-redaction/).
- **Deletion** needs a token emailed to all Super Administrators (https://developers.cloudflare.com/registrar/account-options/domain-management/).
- **Custom Domain Protection** (Enterprise, high-profile domains): Registry Lock where available, out-of-band manual authentication for ownership and nameserver changes, and no dashboard interface, so a compromised account cannot hijack the domain; contact the account team (https://developers.cloudflare.com/registrar/custom-domain-protection/).
- Domain ownership certificates (WHOIS ownership letters) can be generated from the dashboard (https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/).

### 4.6 Registrar API (beta since 2026-04-15)

- Flow: `GET /accounts/{account_id}/registrar/domain-search?q=...` (cached, discovery only), then `POST /accounts/{account_id}/registrar/domain-check` (live registry check, up to 20 domains, returns `reason` such as `domain_unavailable`, `extension_not_supported_via_api`, `extension_not_supported`, `extension_disallows_registration`), then `POST /accounts/{account_id}/registrar/registrations` with `domain_name` (https://developers.cloudflare.com/registrar/registrar-api/).
- Registration waits up to 10 seconds and returns `201` or `202`; `Prefer: respond-async` forces async; poll `.../registrations/{domain}/registration-status` for `in_progress`, `succeeded`, `failed`, `action_required` or `blocked`.
- API defaults: `auto_renew` false, `privacy_mode` `redaction` where supported, default payment method charged automatically.
- Prerequisites: an API token with Registrar write, a billing profile with a default payment method, a default registrant contact, and acceptance of the Domain Registration Agreement.
- Beta limits: a subset of extensions only; no renewals, transfers or contact updates through the API; premium domains will need explicit fee acknowledgement.
- The endpoints are exposed through Cloudflare MCP for agent use.
- The OpenAPI dump (`raw/api/endpoints.tsv`) also lists `registrar/extensions`, `registrar/domain-transfer-check`, a parallel `registrar-sandbox/...` set, and marks the older `registrar/domains` endpoints as deprecated.

### 4.7 Expiry timeline (FAQ)

Day 0 expiry; days 1 to 30 grace (resolves normally); days 31 to 40 suspension page; days 41 to 70 redemption (restore fee may apply); days 71 to 75 pending delete, then release (https://developers.cloudflare.com/registrar/faq/).

### 4.8 Most useful Registrar pages

- https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/
- https://developers.cloudflare.com/registrar/get-started/enable-dnssec/
- https://developers.cloudflare.com/registrar/registrar-api/
- https://developers.cloudflare.com/registrar/custom-domain-protection/
- https://developers.cloudflare.com/registrar/faq/
- https://developers.cloudflare.com/registrar/troubleshooting/

---

## 5. Email Routing

Sending (Email Sending, beta, Workers Paid: 3,000 emails per month included then USD 0.35 per 1,000, as of 2026-10-05) is covered in `build/01-compute.md`.
This section covers inbound routing only.

### 5.1 What it is

- Email Routing receives mail for your domain on Cloudflare MX servers and forwards it to verified addresses, hands it to a Worker's `email()` handler, or drops it (https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/).
- It requires Cloudflare DNS (https://developers.cloudflare.com/email-service/get-started/route-emails/).
- It is available on Workers Free and Workers Paid with unlimited inbound email; routing Workers are billed at normal Workers pricing (https://developers.cloudflare.com/email-service/platform/pricing/).
- Sending to your own verified destination addresses is free on every plan, even with only Email Routing configured, and does not count toward sending quotas.

### 5.2 Setup and DNS records

Dashboard: **Compute > Email Service > Email Routing > Onboard Domain** adds, on the apex (https://developers.cloudflare.com/email-service/configuration/domains/):

- MX `route1.mx.cloudflare.net`, `route2.mx.cloudflare.net`, `route3.mx.cloudflare.net` (priorities set by Cloudflare).
- SPF TXT `v=spf1 include:_spf.mx.cloudflare.net ~all` (merge with existing SPF and stay within 10 lookups).
- DKIM TXT at `cf2024-1._domainkey` (separate from the sending selector `cf-bounce._domainkey`).

Notes:

- These records are **locked** after onboarding and cannot be edited from **DNS > Records** until unlocked in Email Routing settings; only routing records can be unlocked.
- Disabling Email Routing removes them; to migrate providers, unlock, add the new provider's records, then disable.
- You cannot use Email Routing alongside external MX servers.
- These records count toward the DNS record quota (https://developers.cloudflare.com/dns/manage-dns-records/).
- If an MX target is a proxied hostname, Cloudflare inserts a `_dc-mx.<hash>` record pointing at the origin so SMTP bypasses the proxy.

### 5.3 Rules, addresses, catch-all

- A routing rule pairs an email pattern (local part plus domain) with one action: *Send to an email*, *Send to a Worker*, or *Drop*.
- Rules stay disabled until their destination is verified, deleting a destination disables its rules, and duplicate patterns mean only the first listed rule runs.
- Destination addresses are account-level and shared across domains.
- The **catch-all rule** handles every unmatched local part (apex only).
- **Subaddressing** (RFC 5233 plus addressing, added 2025-07-21) is enabled in Settings: `user+detail@` matches the `user@` rule unless a more specific rule exists, and `+detail` is kept in `message.to`.
- **Subdomains** can be added in Email Routing settings, with literal rules only (no catch-all) (https://developers.cloudflare.com/email-service/configuration/subdomains/).
- **Wrangler-managed rules** (Wrangler 4.113.0 or later, changelog 2026-09-04): a top-level `addresses` array in the Worker config (literal addresses or `*@example.com` catch-all) is reconciled on `wrangler deploy`, always with the Send to a Worker action; an empty array removes all rules the Worker manages; destructive changes need interactive confirmation.

### 5.4 Workers `email()` handler

- `message` is a `ForwardableEmailMessage` with `from`, `to`, `headers`, `raw` (ReadableStream), `rawSize`, `canBeForwarded`, and actions `setReject(reason)`, `forward(rcptTo, headers?)` and `reply(EmailMessage)` (https://developers.cloudflare.com/email-service/api/route-emails/email-handler/).
- `forward()` only reaches verified destinations and only accepts added headers prefixed `X-`.
- Fan-out to several destinations is done by calling `forward()` once per destination.
- `reply()` requires the inbound message to have a valid DMARC result (among other checks listed on the page) and throws if the message has more than 100 `References` entries.
- Parsing is shown with `postal-mime`, and replies with `mimetext` plus the `nodejs_compat` flag.
- Local testing works with `wrangler dev` (https://developers.cloudflare.com/email-service/local-development/routing/).
- Since 2025-07-03 Email Routing only forwards mail authenticated by SPF or DKIM, so Workers must handle forward failures for unauthenticated mail (https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/).

### 5.5 Limits (as of 2026-10-05, https://developers.cloudflare.com/email-service/platform/limits/)

| Limit | Value |
| --- | --- |
| Routing rules per domain | 200 |
| Destination addresses per account | 200 |
| Inbound message size | 25 MiB (larger rejected) |
| Domains (Routing plus Sending) per zone, including apex | 30 |
| Reply `References` entries | 100 |

On the Workers Free plan, complex handlers can hit CPU and memory limits (`EXCEEDED_CPU`), and mail sent from a Worker via `send_email` shows as "dropped" in the Email Routing summary even when delivered.

### 5.6 API

- Zone settings: `GET`, `PATCH` and `PUT /zones/{zone_id}/email/routing`, with `DELETE /zones/{zone_id}/email/routing/dns` to disable (the older `POST .../disable` is deprecated).
- Account destination addresses: `/accounts/{account_id}/email/routing/addresses`.
- Account rules: `/accounts/{account_id}/email/routing/rules`, plus `/rules/plan`.
- The `email/routing/suppression` endpoints are deprecated (from `raw/api/endpoints.tsv`; reference at https://developers.cloudflare.com/api/resources/email_routing/).
- Audit logs cover rule edits and address additions (https://developers.cloudflare.com/email-service/observability/audit-logs/).

---

## 6. DMARC Management

- DMARC Management ("Available on all plans" with Cloudflare DNS, labelled beta on its enable and statistics pages) collects DMARC aggregate reports for your domain so you can see every source sending as you and whether it passes SPF, DKIM and DMARC (https://developers.cloudflare.com/dmarc-management/).
- Enable it at **Email > DMARC Management > Enable DMARC Management** (https://developers.cloudflare.com/dmarc-management/enable/):
  - it works only on apex domains and not on subdomain-setup zones;
  - if no DMARC record exists it offers to add one;
  - if one exists it appends a Cloudflare `rua` reporting address;
  - the first report can take up to 24 hours.
- It cannot safely modify SPF when a CNAME in the zone points to an external domain.
- **Statistics**: volume graph over up to 30 days, per-day report lists, top 10 sources, and drill-down per third-party sender (https://developers.cloudflare.com/dmarc-management/statistics/).
- **Security records**: create SPF, DKIM and DMARC records from **Email record overview > View records** (https://developers.cloudflare.com/dmarc-management/security-records/).
- **SPF lookup check**: the record editor warns when SPF exceeds the RFC 7208 limit of 10 DNS lookups (https://developers.cloudflare.com/dmarc-management/dns-lookup-limits/).
- Related: Email Sending onboarding writes `_dmarc` as `v=DMARC1; p=reject;` and documents `p=none` (monitor), `p=quarantine` and `p=reject` (https://developers.cloudflare.com/email-service/configuration/domains/).
- Inbox-side protection is the separate Cloudflare One Email security product (https://developers.cloudflare.com/cloudflare-one/email-security/).

---

## 7. Web3 gateways (Ethereum and IPFS)

### 7.1 History and status

| Date | Event | Source |
| --- | --- | --- |
| 2018-09-17 | Crypto Week day 1: public IPFS gateway at `cloudflare-ipfs.com` launched as the first "Distributed Web Gateway" product, with free SSL for custom hostnames via CNAME | https://blog.cloudflare.com/distributed-web-gateway/ and https://blog.cloudflare.com/crypto-week-2018/ |
| 2018-09-17 | End-to-end integrity work: an `ipfs-sec` mode that requires DNSSEC because the site's root hash lives in DNS, a verifying gateway and a browser extension | https://blog.cloudflare.com/e2e-integrity/ |
| 2019-06-19 | Ethereum gateway at `cloudflare-eth.com` (Crypto Week 2019), built on Workers caching, Load Balancing and Argo Tunnel, usable as a custom-hostname backend via SSL for SaaS | https://blog.cloudflare.com/cloudflare-ethereum-gateway/ |
| 2019-06-19 | IPFS gateway improvements: automatic cache purge by checking DNSLink through DoH to 1.1.1.1, Orange-to-Orange beta for Enterprise, subdomain gateway `cf-ipfs.com` (Base32 CIDv1 as subdomain), session affinity, persistent peering with Pinata | https://blog.cloudflare.com/continuing-to-improve-our-ipfs-gateway/ |
| 2021-01-13 | Distributed Web Resolver: ENS names resolved to IPFS content at the edge in a Worker; `eth.link` (run by True Name LTD) to switch to it on 2021-01-18 | https://blog.cloudflare.com/cloudflare-distributed-web-resolver/ |
| 2021-09-29 | IPFS Safemode, an open-source go-ipfs fork (`v0.9.1-safemode`) letting node operators block CIDs at both the HTTP and P2P layers | https://blog.cloudflare.com/cloudflare-ipfs-safe-mode/ |
| 2021-10-01 | Private beta of Ethereum and IPFS gateways; blog cites over 2,000 IPFS customers (275 TB per month) and over 200 Ethereum customers (13 TB, 1.6 billion requests per month) | https://blog.cloudflare.com/announcing-web3-gateways/ |
| 2022-05-16 | Public availability to all customers, new API and zone dashboard, legacy endpoints to be migrated; same day: Pages-on-IPFS preview, IPFS gateway monitor, plan to run staked Ethereum validators | https://blog.cloudflare.com/ea-web3-gateways/, https://blog.cloudflare.com/cloudflare-pages-on-ipfs/, https://blog.cloudflare.com/ipfs-measurements/, https://blog.cloudflare.com/next-gen-web3-network/ |
| 2022-09-13 | Görli and Sepolia testnet support and readiness for the Merge; Rinkeby signer retirement announced | https://blog.cloudflare.com/ethereum-merge-and-testnet-gateways/ |
| 2023-01 | Rinkeby support ends (docs: 2023-01-30; blog: 2023-01-15) | https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/ |
| 2024-05-14 | Cloudflare starts redirecting its public IPFS gateway traffic to the IPFS Foundation gateways `ipfs.io` and `dweb.link`, maintained by Interplanetary Shipyard | https://blog.cloudflare.com/cloudflares-public-ipfs-gateways-and-supporting-interplanetary-shipyard/ |
| 2024-08-14 | `cloudflare-ipfs.com` and `cf-ipfs.com` "will no longer connect to IPFS"; users must switch to `ipfs.io` or `dweb.link` | same post |

The Shipyard post says Cloudflare will keep sponsoring Shipyard as gateway stewards and that no more end-user data is visible to any party after the transition.
The custom (customer-hostname) gateways documented under https://developers.cloudflare.com/web3/ are a separate, paid product and are still documented as of 2026-10-05, with the overview and limits pages last updated 2026-08-14.

### 7.2 How it works

- You create a gateway on a hostname that must be a subdomain of the current zone; Cloudflare then creates proxied DNS records, proxies the hostname and issues a TLS certificate (https://developers.cloudflare.com/web3/get-started/).
- The records route requests to a Cloudflare Workers script that talks to Cloudflare-run IPFS or Ethereum nodes, caching reads at the edge (https://developers.cloudflare.com/web3/about/).
- Writes are only possible on EVM gateways and go to a Cloudflare node's mempool.
- The 2022 Merge blog describes the Ethereum path as Worker, then Load Balancer per network, then Ethereum node proxies in Kubernetes, then nodes running an execution client plus a consensus client.

**DNS records created** (https://developers.cloudflare.com/web3/reference/gateway-dns-records/):

- Ethereum gateways: a proxied CNAME to `ethereum.cloudflare.com`.
- IPFS gateways: a proxied CNAME to `ipfs.cloudflare.com` plus a TXT record holding the DNSLink value (for `www.example.com`: `_dnslink.www.example.com` TXT `dnslink=/ipns/onboarding.ipfs.cloudflare.com` by default).
- These records cannot be edited in DNS, only through the gateway, and creating a gateway overwrites any existing records on that hostname.
- Account-level enforce DNS-only does not affect Web3 gateways (https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/).

**Statuses**: Active, Pending, Deleting, Error; Refresh (an empty-body `PATCH`) re-creates the DNS records (https://developers.cloudflare.com/web3/reference/gateway-status/).

### 7.3 Configuration

- **Subscribe**: **Web3 > Subscribe to Web3 Gateways**, choose gateways, pay; manage under **Manage Subscriptions** (https://developers.cloudflare.com/web3/how-to/enable-gateways/).
- Enterprise customers can preview the product as a non-contract service, free of metered usage fees and limits.
- **Create in the dashboard**: **Web3 > Create Gateway** with Hostname, Description, Gateway Type (IPFS DNSLink, IPFS Universal Path, Ethereum) and, for IPFS, DNSLink (https://developers.cloudflare.com/web3/how-to/manage-gateways/).
- **Create with the API**: `POST /zones/{zone_id}/web3/hostnames` with `name`, `target` (`ethereum`, `ipfs`, `ipfs_universal_path`), optional `description` and `dnslink`.
- **Edit**: only description and DNSLink can be changed (`PATCH .../web3/hostnames/{id}`); anything else means delete and recreate.
- **Delete**: `DELETE` removes the DNS records and cannot be undone.
- **Universal Path blocklist**: block CIDs (v0 or v1), `/ipfs/...` paths or `/ipns/...` paths, through the dashboard or `.../ipfs_universal_path/content_list/entries`.
- **Customize**: once Active, the hostname takes normal zone security and performance settings (https://developers.cloudflare.com/web3/how-to/customize-cloudflare-settings/); the 2022 GA blog lists rate limits, WAF rules, custom security filters, Workers logic and redirects.
- **Restrict access**: for backend-only use, block normal traffic with Cloudflare Access policies and allow your service with Access service tokens (https://developers.cloudflare.com/web3/how-to/restrict-gateway-access/).
- **Billing alerts**: the get-started page recommends a Usage Based Billing notification.
- **Terraform**: no Terraform example appears in the Web3 docs.

### 7.4 Ethereum gateway

- **Networks** (https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/): Ethereum Mainnet (`/v1/mainnet`, on your gateway or the public `cloudflare-eth.com`) and Sepolia (`/v1/sepolia`, on your gateway).
  No other chain is listed.
- **Interface**: JSON-RPC over HTTP POST with the JSON-RPC body; docs examples use `https://web3-trial.cloudflare-eth.com/v1/mainnet` (https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/).
- **Writes**: only signed transactions via `eth_sendRawTransaction`.
- **Supported methods** (https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-api-methods/): `web3_clientVersion`, `web3_sha3`, `net_version`, `net_listening`, `eth_syncing`, `eth_mining`, `eth_gasPrice`, `eth_feeHistory` (max block count 10), `eth_blockNumber`, `eth_chainId`, `eth_getBalance`, `eth_getStorageAt`, `eth_getTransactionCount`, block and uncle count methods, `eth_getCode`, `eth_sendRawTransaction`, `eth_call`, `eth_estimateGas`, block, transaction and receipt getters, uncle getters, `eth_getLogs` (max 800-block range), `eth_getWork`, `eth_getProof`, and `trace_filter` (max 800 blocks, `count` max 200).
- **Unsupported, returning 403**: `net_peerCount`, `eth_protocolVersion`, `eth_coinbase`, `eth_hashrate`, `eth_accounts`, `eth_sign`, `eth_sendTransaction`, compilers, all filter methods (`eth_newFilter`, `eth_newBlockFilter`, `eth_newPendingTransactionFilter`, `eth_uninstallFilter`, `eth_getFilterChanges`, `eth_getFilterLogs`), `eth_submitWork`, `eth_submitHashrate`.
- No WebSocket or `eth_subscribe` support is documented.
- **Nodes**: full and archive nodes; archive nodes answer `eth_getBalance`, `eth_getCode`, `eth_getTransactionCount`, `eth_getStorageAt` and `eth_call` for blocks older than the latest 128 or `earliest` (https://developers.cloudflare.com/web3/ethereum-gateway/concepts/node-types/).
- The kill-switch reference page is general smart-contract advice (the DAO and Parity incidents), not a gateway feature (https://developers.cloudflare.com/web3/ethereum-gateway/reference/kill-switches/).

### 7.5 IPFS gateway

- Read-only HTTP access to IPFS; writes are not supported (https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/).
- Paths are `/ipfs/<CID>` (immutable) or `/ipns/<domain>` (follows DNSLink, so mutable).
- **DNSLink (restricted) gateway**: bound to one CID or IPNS name through the TXT record; updating the DNSLink to a new CID publishes a new version without a new URL (https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/).
- **Universal Path gateway**: serves any CID or IPNS path, open by default, so use the blocklist; Enterprise only per limits (https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/).
- **Websites**: use relative links so the site works on its domain, a gateway path, and an immutable hash; tips for Angular, React, Vue, Gatsby (gatsby-plugin-ipfs) and Jekyll, plus the `make-relative` script (https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/).
- **CI/CD**: `ipfs-deploy` (pins to third-party pinning services and updates Cloudflare DNS), `dnslink-cloudflare` (updates DNSLink records), and Fission (https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/).
- **Peering**: the docs list 12 Cloudflare IPFS peer IDs at `/dnsaddr/node-{1..12}.ingress.cloudflare-ipfs.com` for your node's `Peering.Peers` config (https://developers.cloudflare.com/web3/ipfs-gateway/reference/peering-with-content-providers/).
- **Troubleshooting**: `no link named "ipfs"` means a gateway without DNSLink; content fails when only free or anonymous pinning was used, no node is online, nodes are behind NAT (forward port 4001), content was not pinned or announced (`ipfs pin -r`, `ipfs dht provide -rv`), or nodes run outdated versions (https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/).
- **Measured performance** (2022 blog, consumer hardware, Cloudflare gateway): cached IPFS content averaged 0.116 s; newly published content averaged 44.4 s (max 343 s); unavailable CIDs time out after about five minutes; DNSLink-as-path to `/ipfs/` averaged 0.346 s versus about 19 to 21 s for IPNS-backed DNSLink (https://blog.cloudflare.com/ipfs-measurements/).

### 7.6 Limits and pricing (as of 2026-10-05, https://developers.cloudflare.com/web3/reference/limits/)

|  | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Availability | Usage-based billing | Usage-based billing | Usage-based billing | Usage-based billing |
| IPFS gateways per account | 15 | 15 | 15 | Unlimited |
| IPFS gateway types | DNSLink | DNSLink | DNSLink | DNSLink, Universal Path |
| IPFS included transfer | 50 GB | 50 GB | 50 GB | 100 GB |
| IPFS file size limit | None | None | None | None |
| Ethereum gateways | 15 | 15 | 15 | Unlimited |
| Ethereum included requests | 500,000 HTTP requests | 500,000 | 500,000 | 1,000,000 |

Overage prices are not in the docs; the limits page points to https://www.cloudflare.com/application-services/products/web3/ and the overview to the dashboard Web3 page for pricing.

### 7.7 Legacy migration

- Cloudflare is deprecating legacy customer hostnames that point at the public endpoints `cloudflare-eth.com` and `cloudflare-ipfs.com` (set up during the private beta).
- To migrate, create a Cloudflare account, then create a Web3 custom gateway on the same hostname, or on a new hostname and repoint the application (https://developers.cloudflare.com/web3/reference/migration-guide/).

### 7.8 Most useful Web3 pages

- Get started: https://developers.cloudflare.com/web3/get-started/
- Manage gateways: https://developers.cloudflare.com/web3/how-to/manage-gateways/
- Supported methods: https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-api-methods/
- Supported networks: https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/
- DNSLink: https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/
- Limits: https://developers.cloudflare.com/web3/reference/limits/
- API: https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/list/

---

## 8. Build hooks for Web3 projects

These are concrete uses for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (EVM L2, chain id 4663), built only from the documented features above.

**Domain hijack and frontend-drainer defence**

- Register the project domain on Cloudflare Registrar and turn on DNSSEC in one click; the DS reaches the registry through CDS/CDNSKEY within one to two days.
  A hijacked resolver path or forged answer cannot then send wallets to a cloned drainer frontend through validating resolvers such as 1.1.1.1.
- Keep the registrar lock on, and treat the Super Administrator and Administrator roles as able to unlock and pull auth codes, because the docs say they can.
- For a high-value launchpad or exchange domain on Enterprise, buy Custom Domain Protection: registry lock, out-of-band verification of nameserver and ownership changes, and no dashboard surface to phish.
- On Enterprise, turn on zone holds (with "Also prevent subdomains") so nobody can stand up the same zone or a subdomain zone in another Cloudflare account.
- Watch Audit Logs v2 (18 months of retention, Logpush export) for DNS record, DNSSEC and Registrar changes; a changed A, CNAME or DNSLink TXT on the dapp hostname is the signature of a frontend takeover.
- Nameservers cannot be preset before zone creation and cannot be changed after creation, which closes the "pre-claimed nameserver" hijack trick.
- Publish CAA records that limit issuance to the CAs you actually use, so a DNS-level attacker cannot quietly obtain a certificate for the dapp domain from another CA.
- Keep ICANN registrant email verification current; an expired verification makes the registry swap in parking nameservers, which takes the dapp offline.

**Ethereum RPC through Cloudflare**

- An Ethereum gateway on `rpc.yourproject.xyz` gives a branded Mainnet and Sepolia JSON-RPC endpoint.
- Because the hostname is a normal proxied zone hostname, WAF custom rules, rate limiting and Turnstile-gated routes apply to it, which helps against scraping and spam submission of signed transactions.
- For a server-only RPC, lock it down with Access service tokens.
- Budget against the documented limits: 500,000 included requests on Free, Pro and Business, an 800-block cap on `eth_getLogs` and `trace_filter`, no filter methods, and no `eth_sendTransaction` (sign client-side and use `eth_sendRawTransaction`).
- The supported-networks page lists only Ethereum Mainnet and Sepolia.
  Base, Robinhood Chain (4663) and Solana are not supported, so those chains need a third-party or self-run RPC, which can still sit behind a proxied Cloudflare hostname to get WAF and rate limiting.

**Immutable frontends on IPFS**

- Build a static dapp or launchpad UI with relative links, pin it to IPFS (your node or a pinning service), and serve it through an IPFS DNSLink gateway on `app.yourproject.xyz`.
- Release by updating the DNSLink TXT to the new CID; users and auditors can pin and verify the exact CID.
- DNSSEC is mandatory in this design, because the 2018 end-to-end integrity post notes that the site's root hash lives in DNS, so DNS spoofing swaps the whole frontend.
- Do not hardcode `cloudflare-ipfs.com` or `cf-ipfs.com` links (NFT metadata, token logos) anywhere; those hostnames stopped serving IPFS on 2024-08-14, so use `ipfs.io` or `dweb.link` or your own DNSLink or Universal Path gateway.
- A Universal Path gateway (Enterprise) can serve token-list or NFT images by CID, with the blocklist used to cut off reported phishing or drainer content.

**ENS**

- The 2021 Distributed Web Resolver resolved ENS names to IPFS content in a Worker and powered `eth.link`.
- The current Web3 docs do not cover ENS resolution, so treat ENS as something to resolve yourself, for example with `eth_call` against the ENS contracts through an Ethereum gateway.

**Email and anti-impersonation**

- Use Email Routing to give the project `security@`, `support@` and `listings@` addresses forwarding to the team, plus a catch-all.
- A Worker `email()` handler can file bug-bounty or listing requests into KV or Queues and auto-reply.
- Only SPF- or DKIM-authenticated mail is forwarded.
- Turn on DMARC Management to see who sends as your domain, then move `_dmarc` towards `p=reject` so "official airdrop" phishing mail spoofing the launchpad domain fails at receivers.

**Resolver-side checks and ops**

- Use the 1.1.1.1 DoH wireformat endpoint (`https://cloudflare-dns.com/dns-query`) from a monitoring Worker or CI job to confirm that DNSLink TXT, A or CNAME and DS records still match expected values.
- Use wireformat rather than JSON, which changed in a breaking way on 2026-07-28.
- After a DNSLink update, use the 1.1.1.1 Purge Cache tool to refresh resolver caches.
- Keep the account-level `enforce_dns_only` break-glass in mind only for origin-level emergencies: it removes WAF and DDoS from every proxied hostname at once, though Web3 gateways themselves are excluded.

---

## 9. Gaps and contradictions

**Web3**

- **Free tier**: the 2022 GA blog says free users "will continue to use the gateways at no cost with our free tier option" with "no cap in the amount of traffic", but the current docs call Web3 "a paid add-on" requiring a subscription and payment details, with usage-based billing on every plan and included allowances (https://blog.cloudflare.com/ea-web3-gateways/ against https://developers.cloudflare.com/web3/get-started/ and https://developers.cloudflare.com/web3/reference/limits/).
- **Overage pricing** for Web3 gateways is not in the docs; it is only referenced on the marketing page and the dashboard.
- **Universal gateway**: the IPFS troubleshooting page says "Cloudflare currently only supports restricted gateways - and not universal gateways", while the limits, concepts and manage-gateways pages and the API document Universal Path gateways on Enterprise (https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/ against https://developers.cloudflare.com/web3/reference/limits/).
- **Rinkeby end date**: docs say 2023-01-30, the 2022 Merge blog says 2023-01-15.
- **Görli**: the 2022 blog announced Görli testnet support, but the supported-networks page lists only Mainnet and Sepolia, and Görli is not mentioned elsewhere in the docs.
- **Public endpoints**: several Web3 docs pages still use `cloudflare-ipfs.com` and `cf-ipfs.com` in examples (IPFS concepts, DNSLink, use-IPFS, website pages), and the peering page lists `node-N.ingress.cloudflare-ipfs.com` peers, although the 2024 blog says those hostnames stopped connecting to IPFS on 2024-08-14.
  Whether the peering addresses still work is not stated.
- **`cloudflare-eth.com`**: the supported-networks page still offers `/v1/mainnet` on the public `cloudflare-eth.com` gateway, while the migration guide says legacy hostnames pointing at `cloudflare-eth.com` are deprecated.
  The current status of the public Ethereum endpoint is not stated.
- **Restrict access mechanism**: the Web3 `llms.txt` describes "Restrict gateway access" as "with WAF custom rules", but the page itself describes Cloudflare Access policies and service tokens; the get-started page calls it Zero Trust.
- **Pages on IPFS**: the 2022 blog promised to make serving Cloudflare Pages sites on IPFS available "later this year", but no Pages or Web3 docs page in the mirror documents it, so its fate is unknown.
- **ENS and eth.link**: the ENS resolver and eth.link integration (2021) and the Ethereum validator experiment (2022) have no current docs; their status is unknown.

**DNS**

- **Account custom nameservers**: the custom nameservers page offers them to Business (via Support) and Enterprise, while the Foundation DNS page lists them as a Foundation DNS (Enterprise-only) feature.
- **Zone transfer peers**: the zone transfers page says "The maximum number of linked peers per zone is 30", which reads as 30 peers per zone; whether it also limits zones per peer is unclear.
- **Post-quantum DNSSEC**: the 2026-09-10 blog says 1.1.1.1 validates ML-DSA-44, but the 1.1.1.1 DNSKEY page (last updated 2026-05-05) does not list ML-DSA-44, and the 1.1.1.1 changelog does not mention it.
- **Post-quantum signing**: authoritative ML-DSA-44 signing and Registrar DS support are announced as future work without dates.
- **Changelog date**: the 1.1.1.1 changelog page shows "Last updated Jul 20, 2026" but contains a 2026-09-24 entry.

**Registrar**

- **Auto-renew default**: the dashboard enrolls domains in auto-renew by default, but the Registrar API defaults `auto_renew` to false (https://developers.cloudflare.com/registrar/account-options/renew-domains/ against https://developers.cloudflare.com/registrar/registrar-api/).
- **Post-expiry timeline**: renew-domains says an unrenewed domain enters a 30-day Redemption Grace Period after expiry, while the FAQ gives a 40-day grace period (30 days resolving, 10 days suspended) before a 30-day redemption period and 5 days of pending delete.
- **TLD count**: the TLD page says "over 400", while the 2025-03-27 changelog says "300+ other TLDs".
  The count moves, so treat both as dated snapshots.
- **API extension list**: the Registrar API guide still contains the editorial placeholder "Add a link here to the supported extensions list once it exists", although the OpenAPI spec has `GET /accounts/{account_id}/registrar/extensions`.
- **Sandbox**: the `registrar-sandbox` endpoints in the spec are not described in the guide.
- **Wrong description**: the Registrar `llms.txt` describes the About page as "Learn how Cloudflare Firewall Rules work", which is a copy error.
- **Pricing**: no per-TLD price table exists in the docs; the FAQ links out to a Learning Center page.

**Email Routing and DMARC Management**

- **REST API link**: the routing rules page links "Email Routing REST API" to `/email-service/platform/email-routing-rest-api/`, but the Email Service `llms.txt` points to `/api/resources/email_routing/`, and the mirror has no page at the former path.
- **Dashboard location**: the sidebar puts Email Routing under Domains & DNS, while its dashboard home is **Compute > Email Service**; DMARC Management is reached at zone **Email > DMARC Management**.
- **DMARC beta label**: the DMARC Management overview says "Available on all plans" with no beta label, but the enable and statistics pages call it "DMARC Management (beta)".
