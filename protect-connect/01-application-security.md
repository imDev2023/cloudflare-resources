# Application Security (Protect & Connect)

Snapshot of the Cloudflare developer docs as mirrored on 2026-10-05; everything that moves (plans, limits, beta or GA status) is dated "as of 2026-10-05".
The Protect & Connect > Application Security dropdown on developers.cloudflare.com lists eight products: WAF, DDoS Protection, SSL/TLS, Bots, API Shield, Page Shield (now named Client-side security), Turnstile and Security Center (source: `raw/nav/home-sidebar.md`).
The top-level `llms.txt` "Application security" section adds Challenges, DMARC Management, Firewall Rules (deprecated), Key Transparency Auditor and Secrets Store, and the "Other" section adds the Security dashboard.
This file covers all of them except DMARC Management (see `protect-connect/03-domains-dns.md`) and Secrets Store (covered elsewhere).
Most of these products are one request pipeline: DDoS mitigation runs first, then WAF custom rules, rate limiting rules, WAF Managed Rules and Super Bot Fight Mode, all built on the Ruleset Engine and its Rules language, while detections (attack score, bot score, leaked credentials, malicious uploads, AI Security for Apps, JWT and schema checks) only populate fields that rules then act on.
The free tier is real but narrow (5 custom rules, 1 rate limiting rule, the Free Managed Ruleset, Bot Fight Mode, Universal SSL, unmetered DDoS, Turnstile with 20 widgets, script monitoring), while the strongest controls (bot score, JA3/JA4, attack score fields, Advanced Rate Limiting, API Shield, Client-Side Security Advanced, malicious uploads, AI Security for Apps) are Enterprise or Enterprise add-ons.

## Table of contents

1. [Sidebar map and request pipeline](#1-sidebar-map-and-request-pipeline)
2. [WAF](#2-waf)
3. [DDoS Protection](#3-ddos-protection)
4. [SSL/TLS](#4-ssltls)
5. [Bots](#5-bots)
6. [API Shield](#6-api-shield)
7. [Client-side security (formerly Page Shield)](#7-client-side-security-formerly-page-shield)
8. [Turnstile](#8-turnstile)
9. [Challenges](#9-challenges)
10. [Security Center](#10-security-center)
11. [Security dashboard (new application security dashboard)](#11-security-dashboard-new-application-security-dashboard)
12. [Key Transparency Auditor](#12-key-transparency-auditor)
13. [Firewall Rules (deprecated)](#13-firewall-rules-deprecated)
14. [Plan availability cheat sheet](#14-plan-availability-cheat-sheet)
15. [Build hooks for Web3 projects](#15-build-hooks-for-web3-projects)
16. [Gaps and contradictions](#16-gaps-and-contradictions)

---

## 1. Sidebar map and request pipeline

| Sidebar entry | Docs root | Source folder | Status as of 2026-10-05 |
| --- | --- | --- | --- |
| WAF | https://developers.cloudflare.com/waf/ | `raw/docs/waf/` (170 pages) | GA, "Available on all plans" |
| DDoS Protection | https://developers.cloudflare.com/ddos-protection/ | `raw/docs/ddos-protection/` (152 pages, most are changelog entries) | GA, "Available on all plans" |
| SSL/TLS | https://developers.cloudflare.com/ssl/ | `raw/docs/ssl/` (137 pages) | GA, "Available on all plans" |
| Bots | https://developers.cloudflare.com/bots/ | `raw/docs/bots/` (50 pages) | GA, "Available on all plans" |
| API Shield | https://developers.cloudflare.com/api-shield/ | `raw/docs/api-shield/` (37 pages) | "Enterprise-only paid add-on" |
| Page Shield | https://developers.cloudflare.com/page-shield/ (redirects) | `raw/docs/client-side-security/` (28 pages) | Renamed Client-side security, "Available on all plans" |
| Turnstile | https://developers.cloudflare.com/turnstile/ | `raw/docs/turnstile/` (45 pages) | GA, Free and Enterprise plans |
| Security Center | https://developers.cloudflare.com/security-center/ | `raw/docs/security-center/` (16 pages) | GA, all plans; Brand Protection and Security Reports in beta |

Products in `llms.txt` but not in the sidebar, covered here: Challenges (https://developers.cloudflare.com/cloudflare-challenges/), Key Transparency Auditor (https://developers.cloudflare.com/key-transparency/), Security dashboard (https://developers.cloudflare.com/security/) and Firewall Rules (deprecated, https://developers.cloudflare.com/firewall/).

### Execution order of the security phases

Source: https://developers.cloudflare.com/waf/feature-interoperability/ and https://developers.cloudflare.com/waf/concepts/.

| Order | Phase | Product |
| --- | --- | --- |
| 1 | `ddos_l7` | HTTP DDoS Attack Protection |
| 2 | `http_request_firewall_custom` | WAF custom rules (account-level custom rulesets run before zone-level rules) |
| 3 | `http_ratelimit` | Rate limiting rules |
| 4 | `http_request_firewall_managed` | WAF Managed Rules (and WAF exceptions, which are `skip` rules in this phase) |
| 5 | `http_request_sbfm` | Super Bot Fight Mode |

Within each phase, account-level rulesets run before zone-level rulesets.
The first rule with a terminating action (Block, Managed Challenge, Redirect and so on) stops evaluation of every later phase.
A custom rule with the Skip action can bypass rate limiting rules, Super Bot Fight Mode and Managed Rules.
Bot Fight Mode is not part of the Ruleset Engine, so it cannot be skipped by any rule.
IP Access rules, Zone Lockdown, User Agent Blocking, Browser Integrity Check, Hotlink Protection and Security Level are evaluated outside the Ruleset Engine and do not follow the phase order.
The WAF concepts page gives a simpler order: IP Access rules, Firewall rules (deprecated), custom rules, rate limiting rules, Managed Rules, then the previous Rate Limiting (no longer available).

---

## 2. WAF

Docs: https://developers.cloudflare.com/waf/

### What it is

The Cloudflare WAF checks incoming web and API requests and filters traffic using rulesets written in the Rules language (https://developers.cloudflare.com/ruleset-engine/rules-language/).
It has three building blocks: Managed Rules (signature rules written by Cloudflare), traffic detections that enrich requests with scores and flags, and user-defined custom rules and rate limiting rules (https://developers.cloudflare.com/waf/concepts/).
The docs separate detection from mitigation: "Detections only score traffic. They do not block or challenge requests on their own."

### Plan availability (WAF overview page, as of 2026-10-05)

Source: https://developers.cloudflare.com/waf/

| Feature | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Attack score | No | No | Yes (one field) | Yes |
| Leaked credentials detection | Yes (one field) | Yes | Yes | Yes |
| Malicious uploads detection | No | No | No | Paid add-on |
| AI Security for Apps | No | No | No | Paid add-on |
| Custom rules | Yes | Yes | Yes | Yes |
| Rate limiting rules | Yes (one rule) | Yes | Yes | Yes |
| Advanced Rate Limiting | No | No | No | Paid add-on |
| WAF Managed Rules | Free Managed Ruleset only | Yes | Yes | Yes |
| Sensitive Data Detection | No | No | No | Yes |
| Account-level WAF configuration | No | No | No | Yes |
| Custom lists | Yes | Yes | Yes | Yes |
| Managed IP Lists | No | No | No | Yes |
| Email Address Obfuscation, Hotlink Protection, Replace insecure JS libraries, IP Access rules, User Agent Blocking, Zone Lockdown | Yes | Yes | Yes | Yes |
| Security Analytics (zone) | Yes | Yes | Yes | Yes |
| Security Analytics (account) | No | No | Yes | Yes |
| Security Events | Yes (sampled logs only) | Yes | Yes | Yes |
| Security Events alerts | No | No | Yes | Yes |
| Advanced Security Events alerts | No | No | No | Yes |

The docs give no dollar prices for the Pro, Business or Enterprise plans or for the paid add-ons; they point to https://www.cloudflare.com/plans/.
Enterprise customers can preview rate limiting as a non-contract service with "full access, free of metered usage fees" (https://developers.cloudflare.com/waf/rate-limiting-rules/).

### Custom rules

Docs: https://developers.cloudflare.com/waf/custom-rules/

Custom rules are expression plus action rules in the `http_request_firewall_custom` phase; actions include Block, Managed Challenge, Skip and (Enterprise only) Log.
In the new security dashboard they are one type of "security rule".

| Custom rules | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Number of rules | 5 | 20 | 100 | 1,000 |
| Supported actions | All except Log | All except Log | All except Log | All |
| Regex support | No | No | Yes | Yes |
| Custom rulesets (zone) | 1 | 2 | 5 | 10 |
| Account-level custom rulesets | No | No | No | Yes |

The rule quota counts all rules in the `http_request_firewall_custom` phase, including rules inside zone-level custom rulesets.
The dashboard cannot work with zone-level custom rulesets; they need the API.
Use cases documented include allowlisting IPs, geo blocking, challenging bad bots, blocking by attack score, JWT-claim checks for admin users, token authentication, requiring headers or cookies, stopping R.U.D.Y. slow-POST attacks and sequence rules (https://developers.cloudflare.com/waf/custom-rules/use-cases/).

Configuration:

- Dashboard: **Security rules** page, **Create rule** > **Custom rules** (https://developers.cloudflare.com/waf/custom-rules/create-dashboard/).
- API: Rulesets API, `POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules` on the zone entry point ruleset of phase `http_request_firewall_custom` (https://developers.cloudflare.com/waf/custom-rules/create-api/).
- Terraform: `resource "cloudflare_ruleset"` with `kind = "zone"` and `phase = "http_request_firewall_custom"`; account-level custom rulesets use `kind = "custom"` plus a `root` ruleset that executes them (https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).

### Rate limiting rules

Docs: https://developers.cloudflare.com/waf/rate-limiting-rules/

A rate limiting rule has an expression, an action, counting characteristics, a period, requests per period, a mitigation timeout (duration), and an action behavior.
By default the action applies for the whole mitigation timeout; some Enterprise customers can instead throttle requests above the rate.
Counters are per Cloudflare data center: "Cloudflare does not support global rate limiting counters across the entire network", except that data centers in the same geographic location share counters (https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/).
Every rule silently includes `cf.colo.id` as a mandatory characteristic; when created via API you must include it yourself.
There can be "a delay of up to a few seconds" between a request and the counter update, so excess requests can reach the origin.
Workers subrequests to the same zone can be counted as separate requests.
Applying rate limits to verified bots can affect SEO.

| Rate limiting | Free | Pro | Business | Enterprise with app security | Enterprise with Advanced Rate Limiting |
| --- | --- | --- | --- | --- | --- |
| Fields in rule expression | Path, Verified Bot | Host, URI, Path, Full URI, Query, Verified Bot | adds Method, Source IP, User Agent | General request and header fields, Verified Bot, Bot Management fields (needs Bot Management) | adds request body fields |
| Counting characteristics | IP | IP | IP, IP with NAT support | IP, IP with NAT support | adds Query, Host, Headers, Cookie, ASN, Country, Path, JA3/JA4, JSON field value, Body, Form input value, Custom |
| Custom counting expression (incl. response code and headers) | No | No | Yes | Yes | Yes |
| Counting model | Requests | Requests | Requests | Requests | Requests or complexity score |
| Throttle behavior | No | No | No | Yes | Yes |
| Counting periods | 10 s | up to 1 min | up to 10 min | up to 65,535 s | up to 65,535 s |
| Mitigation timeout | 10 s | up to 1 h | up to 1 day | up to 1 day (custom via API) | up to 1 day (custom via API) |
| Number of rules | 1 | 2 | 5 | 100 (contract-dependent) | 100 |

Supported period values in seconds are 10, 15, 20, 30, 40, 45, 60, 90, 120, 180, 240, 300, 480, 600, 900, 1200, 1800, 2400, 3600, 65535 and 86400, and not all are on every plan.
Complexity-based rate limiting (Advanced Rate Limiting) counts a numeric cost score from a response header your origin returns, with values from 1 to 1,000,000, instead of a request count (https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting).
Best practices include counting only failed attempts (response code 401 or 403) on OTP endpoints (Business or higher), limiting reuse of a single `cf_clearance` cookie (example: 100 requests per 10 minutes on `/checkout`), GraphQL complexity limits and credential-stuffing patterns (https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/).
Account-level rate limiting rulesets deploy to multiple Enterprise zones (https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/).
The previous Rate Limiting product (billed by usage) is "no longer available" (https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/).

Terraform example from https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/ (provider v5 syntax; the page also shows the older block syntax):

```tf
resource "cloudflare_ruleset" "zone_rl" {
  zone_id     = var.cloudflare_zone_id
  name        = "Rate limiting for my zone"
  kind        = "zone"
  phase       = "http_ratelimit"
  rules = [{
    ref         = "rate_limit_api_requests_ip"
    expression  = "(http.request.uri.path matches \"^/api/\")"
    action      = "block"
    ratelimit = {
      characteristics     = ["cf.colo.id", "ip.src"]
      period              = 60
      requests_per_period = 100
      mitigation_timeout  = 600
    }
  }]
}
```

### Managed Rules

Docs: https://developers.cloudflare.com/waf/managed-rules/

| Managed ruleset | Ruleset ID suffix | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- | --- |
| Cloudflare Free Managed Ruleset | `...dfb893ba` | Yes | Yes | Yes | Yes |
| Cloudflare Managed Ruleset | `...376e9aee` | No | Yes | Yes | Yes |
| Cloudflare OWASP Core Ruleset (score-based, paranoia level and threshold) | `...c25d2f1f` | No | Yes | Yes | Yes |
| Cloudflare Exposed Credentials Check (deprecated) | `...14069605` | No | Yes | Yes | Yes |
| Cloudflare Sensitive Data Detection (response phase) | `...499d988e` | No | No | No | Yes |

Customize behavior with exceptions (skip rules, which take priority) or overrides (ruleset, tag or rule level); ruleset and tag overrides also apply to future rules.
At zone level each managed ruleset deploys once; at account level (Enterprise) the same ruleset can be deployed several times with different configurations.
Payload logging encrypts the matched payload with your own public key (https://developers.cloudflare.com/waf/managed-rules/payload-logging/).
Maximum inspected body size: Enterprise 128 KB, other paid plans "lower by default", Free 1 MB (as written; see Gaps), and `http.request.body.truncated` flags truncated bodies.
Configuration: dashboard **Security** > **Settings** to deploy; API `PUT .../zones/$ZONE_ID/rulesets/phases/http_request_firewall_managed/entrypoint`; Terraform `cloudflare_ruleset` with `phase = "http_request_firewall_managed"` (https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/).
The changelog lists scheduled and past managed rule changes (https://developers.cloudflare.com/waf/change-log/).

### Traffic detections

Docs: https://developers.cloudflare.com/waf/detections/

| Detection | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Leaked credentials fields | Password Leaked | Password Leaked, User and Password Leaked | Password Leaked, User and Password Leaked | All fields |
| Custom detection locations | 0 | 0 | 0 | 10 |
| Attack score | No | No | One field only | Yes |
| Malicious uploads | No | No | No | Paid add-on |
| AI Security for Apps | No | No | No | Yes (overview says paid add-on) |

Detections are enabled under **Security** > **Settings**, filtered by **Detection tools**; bot score and attack score cannot be managed there.

**WAF attack score** (https://developers.cloudflare.com/waf/detections/attack-score/): an ML score from 1 (almost certainly malicious) to 99 (likely clean) that catches variations of attacks that do not exactly match Managed Rules signatures.
Fields: `cf.waf.score`, `cf.waf.score.sqli`, `cf.waf.score.xss`, `cf.waf.score.rce` (Enterprise) and `cf.waf.score.class` with values `attack` (1-20), `likely_attack` (21-50), `likely_clean` (51-80) and `clean` (81-99) (Business and above).
A score of 100 means not scored; 0 in Logpush means the request never reached the attack score stage.
It decodes Base64, JavaScript Unicode escapes and URL encoding anywhere in the request.
Recommended starting rule: `cf.waf.score le 20` with Block (Enterprise) or `cf.waf.score.class eq "attack"` (Business); blocking everything under 50 is "not recommended".

**Leaked credentials detection** (https://developers.cloudflare.com/waf/detections/leaked-credentials/): compares usernames and passwords found in requests against the Have I Been Pwned password dataset, Cloudflare-collected usernames and leaked pairs.
Fields: `cf.waf.credential_check.password_leaked` (all plans), `cf.waf.credential_check.username_and_password_leaked` (Pro+), `cf.waf.credential_check.username_leaked`, `cf.waf.credential_check.username_password_similar` and `cf.waf.auth_detected` (Enterprise).
It is on by default for Free plans and scans default locations for Drupal, Joomla, Ghost, Magento, Plone, WordPress, Microsoft Exchange OWA plus generic patterns.
Enterprise can add custom detection locations such as `lookup_json_string(http.request.body.raw, "user")`.
A managed transform can add an `Exposed-Credential-Check` header to the origin request (1 = pair leaked, 2 = username leaked, 4 = password leaked).
Passwords are hashed and never stored in plaintext.
API: `https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks` and `.../leaked-credential-checks/detections`; Terraform `cloudflare_leaked_credential_check` and `cloudflare_leaked_credential_check_rule` (https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/).
It replaces the deprecated Exposed Credentials Check managed ruleset.

**Malicious uploads detection** (also called content scanning, https://developers.cloudflare.com/waf/detections/malicious-uploads/): Enterprise paid add-on that sends detected content objects to the same antivirus scanner used by Cloudflare Zero Trust.
It ignores `Content-Type` and finds objects heuristically, excluding `text/html`, `text/x-shellscript`, `application/json`, `text/csv` and `text/xml`.
It scans only the first 50 MB of a request body; objects beyond that are silently not reported, so rules should check `cf.waf.content_scan.truncated`.
It will not scan password-protected archives, archives over three recursion levels or over 300 files, or PGP-encrypted files.
Custom scan expressions locate Base64 payloads inside JSON, and Base64 is decoded automatically.
Fields include `cf.waf.content_scan.has_malicious_obj`, `num_malicious_obj`, `has_failed`, `truncated`, `obj_sizes`, `obj_types` and `obj_results` (`clean`, `suspicious`, `infected`, `not scanned`).
Terraform: `cloudflare_content_scanning` and `cloudflare_content_scanning_expression`.
Scanning "can introduce latency".

**AI Security for Apps** (formerly Firewall for AI, https://developers.cloudflare.com/waf/detections/ai-security-for-apps/): model-agnostic detections for PII in prompts, unsafe and custom topics, and prompt injection, applied to endpoints labeled `cf-llm` with `application/json` bodies only.
LLM endpoint discovery is on all plans; the AI Security Log Mode Ruleset and AI detection fields are an Enterprise paid add-on requested through the account team.
Token counting supports rate limiting by LLM tokens (https://developers.cloudflare.com/waf/detections/ai-security-for-apps/token-counting/).

**Threat intelligence** (https://developers.cloudflare.com/waf/detections/threat-intelligence/): matches the client IP against Cloudforce One indicators from a rolling seven-day window, exposing `cf.intel.ip.attacker_names`, `cf.intel.ip.target_industries`, `cf.intel.ip.attacker_countries`, `cf.intel.ip.target_countries` and `cf.intel.ip.datasets` (`ddos`, `waf`).
It requires a Cloudforce One subscription.

**Application Profiles** (https://developers.cloudflare.com/waf/detections/application-profiles/): a positive-security model; Schema Profile is the only profile type, learned from traffic or uploaded as OpenAPI.
It is always-on detection after a profile exists, with mitigation via custom rules.
API Security customers have it; a closed beta is open to invited Enterprise customers without API Security, as of 2026-10-05.

**Attack Signature Detection** (https://developers.cloudflare.com/waf/detections/attack-signature-detection/): Early Access, as of 2026-10-05.
It uses the same signature catalog as Managed Rules (signature Ref equals Managed Rule public ID) but records confidence, category and Ref metadata without acting, and adds no latency unless a rule references its fields.

**Bot score** is a Bots product field; see section 5.

### Lists, IP Access rules and other tools

Lists (https://developers.cloudflare.com/waf/tools/lists/) are account-level groups of IPs, hostnames or ASNs referenced as `$list_name` in expressions.

| Lists | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Custom lists (any type) | 1 | 10 | 10 | 1,000 |
| Max items across custom lists | 10,000 | 10,000 | 10,000 | 500,000 |
| IP lists | Yes | Yes | Yes | Yes |
| Hostname and ASN lists | No | No | No | Yes (up to 40 each; 10,000 hostname items and 30,000 ASN items) |
| Managed IP Lists | No | No | No | Yes |

The list quota follows the highest plan in the account.
List names must match `^[a-z0-9_]+$`, max 50 characters.
A list cannot be deleted while any rule references it.

IP Access rules (https://developers.cloudflare.com/waf/tools/ip-access-rules/) allow, block or challenge by IP, ASN or country, with up to 50,000 rules per account on every plan; block by country is Enterprise only.
Allowing an IP or ASN bypasses custom rules, rate limiting rules, Managed Rules and firewall rules, and Cloudflare recommends custom rules with IP lists instead.
Other tools: Browser Integrity Check, Security Level, User Agent Blocking, Zone Lockdown, Privacy Pass, Replace insecure JS libraries, Email Address Obfuscation and Hotlink Protection (https://developers.cloudflare.com/waf/tools/).

### Analytics

Security Analytics shows all incoming requests including unmitigated ones (https://developers.cloudflare.com/waf/analytics/security-analytics/).
Security Events shows mitigated requests; on Free it is sampled logs only (https://developers.cloudflare.com/waf/analytics/security-events/).

### Most useful WAF pages

- Overview and plan table: https://developers.cloudflare.com/waf/
- Concepts and execution order: https://developers.cloudflare.com/waf/concepts/
- Feature interoperability: https://developers.cloudflare.com/waf/feature-interoperability/
- Phases: https://developers.cloudflare.com/waf/reference/phases/
- Custom rules: https://developers.cloudflare.com/waf/custom-rules/
- Rate limiting rules: https://developers.cloudflare.com/waf/rate-limiting-rules/
- Rate limiting parameters: https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/
- Rate limiting best practices: https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/
- Managed Rules: https://developers.cloudflare.com/waf/managed-rules/
- Attack score: https://developers.cloudflare.com/waf/detections/attack-score/
- Leaked credentials: https://developers.cloudflare.com/waf/detections/leaked-credentials/
- Malicious uploads: https://developers.cloudflare.com/waf/detections/malicious-uploads/
- AI Security for Apps: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/
- Lists: https://developers.cloudflare.com/waf/tools/lists/

---

## 3. DDoS Protection

Docs: https://developers.cloudflare.com/ddos-protection/

### What it is

Cloudflare provides "unmetered and unlimited" DDoS protection at layers 3, 4 and 7 to all customers on all plans, enabled by the Autonomous DDoS Protection Edge (https://developers.cloudflare.com/ddos-protection/about/).
Mitigation logic is exposed as two managed rulesets: HTTP DDoS Attack Protection (L7, phase `ddos_l7`) and Network-layer DDoS Attack Protection (L3/4; UDP floods, SYN-ACK reflection, SYN floods, DNS floods) (https://developers.cloudflare.com/ddos-protection/managed-rulesets/).
The HTTP ruleset is always on and you can only change its action and sensitivity level.

### Key concepts

- Origin Protect rule `dd42da7baabe4e518eaf11c393596a9d` mitigates floods causing origin errors; default High sensitivity is 1,000 errors per second, and on Pro, Business and Enterprise the error rate must also be at least five times normal origin traffic (https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/).
- Errors counted are the 52x range and 53x range excluding 530.
- Adaptive DDoS Protection builds seven-day traffic profiles (95th percentile daily maxima) per origin errors, user agent (network-wide), client country and IP protocol, with default action Log (https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/).
- HTTP adaptive rules profile at zone level, so they may be ineffective for a Cloudflare for SaaS zone shared by many custom hostnames.
- Advanced TCP Protection (out-of-state TCP floods) and Advanced DNS Protection (random prefix attacks) are for Magic Transit customers.
- Programmable Flow Protection runs customer eBPF programs against UDP-based L7 protocols; it is a closed beta add-on for Magic Transit only, as of 2026-10-05 (https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/).
- Botnet Threat Feed gives service providers (verified via PeeringDB ASN affiliation) a free list of their own IPs that took part in HTTP DDoS attacks, via `GET /accounts/{account_id}/botnet_feed/asn/{asn}/full_report` and `.../day_report?date=YYYY-MM-DD`, with two weeks of data; the path is planned to change to `.../ddos_botnet_feed/...` (https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/).
- You may simulate DDoS attacks against your own properties without asking Cloudflare, as long as they are not shared with others (https://developers.cloudflare.com/ddos-protection/reference/simulate-ddos-attack/).

### Plan availability (as of 2026-10-05)

Source: https://developers.cloudflare.com/ddos-protection/

| Feature | Free | Pro | Business | Enterprise | Enterprise + Advanced DDoS Protection |
| --- | --- | --- | --- | --- | --- |
| Unmetered L3-7 DDoS, HTTP and network rulesets | Yes | Yes | Yes | Yes | Yes |
| Managed rules customization | Yes | Yes | Yes | Yes, with Log action | Expression fields and multi-rule support |
| Proactive false positive detection for new rules | No | No | No | Yes | Yes |
| Adaptive DDoS protection | Error adaptive rules only | Error adaptive rules only | Error adaptive rules only | Error adaptive rules only | All adaptive rules |
| Profiling signals | Error rates | Error rates | Error rates and historical trends | Error rates and historical trends | adds client country, user agent, query string, ML scores |
| Ruleset overrides | 1 | 1 | 1 | 1 | 10 (custom expressions) |
| Alerts | Yes | Yes | Yes | Yes | Advanced alerts with filtering |

Non-Advanced customers get one override that cannot have a custom expression and applies to all traffic.

### Configuration

- Dashboard: **Security** > **DDoS** (old) or the **DDoS protection** tab under Security rules (new); network-layer overrides are account level (https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/).
- API: `PUT https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/ddos_l7/entrypoint` (or the account equivalent); account-level HTTP DDoS overrides are API only (https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-api/).
- Terraform: `cloudflare_ruleset` resources `zone_level_http_ddos_config` and `account_level_network_ddos_config` (https://developers.cloudflare.com/terraform/additional-configurations/ddos-managed-rulesets/).

### Most useful pages

- https://developers.cloudflare.com/ddos-protection/about/attack-coverage/
- https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/
- https://developers.cloudflare.com/ddos-protection/best-practices/proactive-defense/
- https://developers.cloudflare.com/ddos-protection/best-practices/third-party/
- https://developers.cloudflare.com/ddos-protection/change-log/

---

## 4. SSL/TLS

Docs: https://developers.cloudflare.com/ssl/

### What it is

SSL/TLS covers two connections: the edge certificate (visitor to Cloudflare) and the origin certificate or encryption mode (Cloudflare to origin) (https://developers.cloudflare.com/ssl/concepts/).
It is "Available on all plans", and Universal SSL issues free certificates automatically.

### Edge certificates

| Option | What it covers | Plans (as of 2026-10-05) |
| --- | --- | --- |
| Universal SSL | Apex and first-level subdomains in full setup; every proxied subdomain in CNAME setup; 90-day validity, renewal starts 30 days before expiry; Cloudflare picks the CA and may change it without notice | All plans |
| Advanced certificates (Advanced Certificate Manager) | Choose CA, hostnames, validity (2 weeks, 1 month, 3 months, or 1 year with SSL.com for Enterprise); delegated DCV | Paid add-on on all plans |
| Total TLS | Auto certificates for proxied hostnames at any depth | Requires ACM and full DNS setup |
| Custom certificates | Upload your own (any CA and validation level) | Business (5 Modern and 1 Legacy pack), Enterprise (more purchasable); not Free or Pro |
| Keyless SSL | Private key stays on your key server or HSM | Enterprise paid add-on, your own CA certificate required |
| Geo Key Manager | Restrict where private keys are stored | Custom certificates only, API only; v2 in closed beta |
| Backup certificates | Automatic | All plans; only Enterprise can opt out |

Sources: https://developers.cloudflare.com/ssl/edge-certificates/, https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/, https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/, https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/, https://developers.cloudflare.com/ssl/keyless-ssl/, https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/.
CAs used: Let's Encrypt, Google Trust Services, SSL.com and Sectigo (https://developers.cloudflare.com/ssl/reference/certificate-authorities/).
Universal SSL only serves certificates for proxied records, does not cover load balancing hostnames by default, is not compatible with Spectrum, can be refused for domains containing trademark-like words, and HPKP pinning is not supported.
Cipher suite customization and per-hostname minimum TLS need ACM; zone-level minimum TLS is on all plans and cannot be set for Pages hostnames (https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/).
Other edge options: Always Use HTTPS, Automatic HTTPS Rewrites, HSTS, TLS 1.3, Opportunistic Encryption, CAA records, and Certificate Transparency Monitoring (opt-in alerts when a CA logs a certificate for your domain; it does not catch lookalike domains) (https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).
ECH (Encrypted Client Hello) is on by default for Free zones and toggleable elsewhere; all ECH traffic shows the outer SNI `cloudflare-ech.com` (https://developers.cloudflare.com/ssl/edge-certificates/ech/).

### Origin side

Encryption modes (https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/): Automatic SSL/TLS (default, being rolled out gradually, uses SSL/TLS Recommender scans roughly monthly and upgrades in 1% then 10% traffic steps, never downgrades) or Custom: Off, Flexible, Full, Full (strict), Strict (SSL-Only Origin Pull).
API: `PATCH /zones/$ZONE_ID/settings/ssl` with `off`, `flexible`, `full`, `strict` or `origin_pull`; opt out of automatic mode with `PATCH /zones/$ZONE_ID/settings/ssl_automatic_mode` value `custom`.
Cloudflare "strongly recommends" Full or Full (strict).
Cloudflare Origin CA issues free origin certificates trusted only by Cloudflare (https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/).
Authenticated Origin Pulls (AOP) proves to the origin that requests come from Cloudflare via a client certificate, at global (shared Cloudflare certificate), zone-level or per-hostname scope; it is on all plans, needs Full or Full (strict), and is not compatible with Cloudflare Tunnel (https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/).
Custom Origin Trust Store requires ACM.

### Client certificates (mTLS)

Docs: https://developers.cloudflare.com/ssl/client-certificates/

Cloudflare validates client certificates against account-level CAs and sets `cf.tls_client_auth.cert_verified`, which WAF custom rules then enforce.
The Cloudflare-managed CA is on all plans with 100 active client certificates per zone by default, raised to 100,000 per zone with Enterprise API Shield.
BYOCA is Enterprise only, with up to five CA certificates per account shared across API Shield, Workers mTLS and Cloudflare Gateway.
The mTLS Workers binding is for a Worker presenting a client certificate to an external service.

### Post-quantum cryptography

Cloudflare deploys the hybrid key agreement X25519MLKEM768 (TLS id `0x11ec`, recommended; X25519Kyber768Draft00 `0x6399` is obsolete), only on TLS 1.3 and HTTP/3, and supports ML-DSA signatures on the Cloudflare-to-origin connection; it targets 2029 to be fully post-quantum secure (https://developers.cloudflare.com/ssl/post-quantum-cryptography/).

### Terraform and API

Terraform resources mentioned in the mirror include `cloudflare_certificate_pack` (advanced certificates) and `cloudflare_zone_setting` (for settings like `ssl`, `min_tls_version`, `always_use_https`).
API references: https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/create/ and https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/api-commands/.

### Most useful pages

- https://developers.cloudflare.com/ssl/get-started/
- https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/
- https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/
- https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/
- https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/
- https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/

---

## 5. Bots

Docs: https://developers.cloudflare.com/bots/

### What it is

Three bot products: Bot Fight Mode (Free), Super Bot Fight Mode (Pro, Business, Enterprise without the add-on) and Bot Management for Enterprise (add-on).
Bot Fight Mode and Super Bot Fight Mode apply to the whole domain and "Cannot be customized, adjusted, or reconfigured via WAF custom rules", although Super Bot Fight Mode can be skipped with a Skip custom rule (https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/).
Both "may challenge API or mobile app traffic".

### Plans (as of 2026-10-05)

| | Free | Pro | Business (and Enterprise without BM) | Enterprise Bot Management |
| --- | --- | --- | --- | --- |
| Product | Bot Fight Mode | Super Bot Fight Mode | Super Bot Fight Mode | Bot Management |
| Bots detected | Simple bots from cloud providers, headless browsers | Simple bots, headless browsers | adds many sophisticated bots | adds domain-specific anomalies |
| Actions | Computationally expensive challenge only | Allow, block or challenge | Allow, block or challenge | Block and various challenges, by rule |
| Likely automated category | No | No | Yes | Yes (via score) |
| Analytics | None listed | Limited Bot Report | Bot Analytics in Security Analytics | Bot Analytics |
| Control | Whole domain | Whole domain | Whole domain | Per path, IP and more; bot score, JA3/JA4, bot tags, detection IDs |
| Block AI bots, AI Labyrinth, managed robots.txt | Yes | Yes | Yes | Yes |
| Static resource protection | No | Yes | Yes | Yes |

Sources: https://developers.cloudflare.com/bots/plans/free/, https://developers.cloudflare.com/bots/plans/pro/, https://developers.cloudflare.com/bots/plans/biz-and-ent/, https://developers.cloudflare.com/bots/plans/bm-subscription/.
Enterprise customers can preview Bots as a non-contract service.
Zones with Bot Management do not see Bot Fight Mode or Super Bot Fight Mode.

### Key concepts

- Bot score 1-99 (1 = automated, 99 = human); granular scores only with Bot Management, others see groupings: Not computed (0), Automated (1), Likely automated (2-29), Likely human (30-99), Verified bot (https://developers.cloudflare.com/bots/concepts/bot-score/).
- Engines (Enterprise BM): Heuristics (score 1, sometimes 29), Machine learning (most scores 2-99), Anomaly detection (deprecated, no new customers), JavaScript detections, and Cloudflare Service.
- Requests with a missing or empty `User-Agent` get score 1.
- The `__cf_bm` cookie smooths scores per user session.
- Fields: `cf.bot_management.score`, `cf.bot_management.verified_bot`, `cf.bot_management.ja3_hash`, `cf.bot_management.ja4`, `cf.bot_management.detection_ids`, `cf.bot_management.js_detection.passed`, `cf.bot_management.corporate_proxy` (https://developers.cloudflare.com/bots/reference/bot-management-variables/).
- JA3/JA4 fingerprints and JA4 Signals (ratios, ranks and quantiles over one hour) are BM only; they are absent for plain HTTP, after TLS session resumption, or when BM is skipped, and are preserved through Orange-to-Orange chains (https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/).
- Detection IDs for account takeover: `201326592` (suspicious login failures), `201326593` (suspicious login attempts), `201326598` (dynamic threshold) (https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/).
- Account Abuse Protection (bulk account creation and account takeover signals) is Early Access for BM customers at no extra cost "for a limited period", as of 2026-10-05 (https://developers.cloudflare.com/bots/account-abuse-protection/).
- Sequence rules track request order and timing in cookies and need the Fraud Detection subscription (https://developers.cloudflare.com/bots/additional-configurations/sequence-rules/).
- Web Bot Auth verifies bots by Ed25519 HTTP Message Signatures (IETF drafts) and feeds the Verified Bots program (https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/; blog https://blog.cloudflare.com/verified-bots-with-cryptography/).
- BotBase (BM only) is a directory of known bots and agents; Business Insights (BM only) is an observability view (https://developers.cloudflare.com/bots/botbase/).
- AI Labyrinth injects hidden nofollow links that trap non-compliant AI crawlers (https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/).

### Configuration

Dashboard: **Security** > **Settings**, filter **Bot traffic**.
Bot Management rules are WAF custom rules using bot fields; the documented example blocks a bot score below 30 on website paths while allowing API paths used by authenticated partners (https://developers.cloudflare.com/waf/feature-interoperability/).
If you use Cloudflare Tunnel, keep Super Bot Fight Mode's Definitely Automated on Allow to avoid `websocket: bad handshake`.

### Most useful pages

- https://developers.cloudflare.com/bots/get-started/bot-management/
- https://developers.cloudflare.com/bots/concepts/bot/verified-bots/
- https://developers.cloudflare.com/bots/troubleshooting/false-positives/
- https://developers.cloudflare.com/bots/workers-templates/delay-action/

---

## 6. API Shield

Docs: https://developers.cloudflare.com/api-shield/

### What it is

API Shield discovers API endpoints, validates requests against schemas and tokens, and detects API abuse.
The overview says "Enterprise-only paid add-on" and "Anyone can set up Mutual TLS with a Cloudflare-managed certificate authority".
API Shield "currently does not work for JDCloud customers".

### Features and availability (as of 2026-10-05)

| Feature | Availability per docs |
| --- | --- |
| Endpoint Management, saved operations | Limits by plan (table below) |
| Schema validation (uploaded OpenAPI, `cf.schema_validation.uploaded.violated`) | Limits by plan (table below); 10,000 operations cap for API Shield subscribers |
| Schema learning, Application Profiles | API Shield subscribers; closed beta for invited Enterprise without API Shield |
| API Discovery | Paid API Shield add-on (Enterprise) |
| Session identifiers (up to 10; header, cookie or JWT claim) | API Shield subscription or eligible trial; auto-configured from `Authorization` if it appears on over 1% of sampled 2xx requests |
| JWT validation (`http.request.jwt.claims`, `is_jwt_valid()`, headers or cookies only) | All API Shield customers |
| GraphQL malicious query protection (depth and size; POST bodies up to 20 KiB) | All API Shield customers |
| Volumetric Abuse Detection (per-session rate limit recommendations, seven-day window) | API Shield |
| Sequence Analytics and Sequence mitigation | API Shield |
| BOLA vulnerability detection | Enterprise |
| Vulnerability Scanner | Enterprise API Shield, open beta |
| mTLS | All plans with Cloudflare-managed CA |
| Developer portals (hosted on Pages) | All API Shield subscribers |
| Sensitive Data Detection with API Shield | Separate subscription |

| Plan | Saved endpoints | Enabled uploaded schemas | Combined schema size | Rule action | Schema body size limit |
| --- | --- | --- | --- | --- | --- |
| Free | 100 | 5 | 200 KiB | Block only | 1 KiB |
| Pro | 250 | 5 | 500 KiB | Block only | 8 KiB |
| Business | 500 | 10 | 2 MiB | Block only | 8 KiB |
| Enterprise without API Shield | 3,000 | 10 | 5 MiB | Log or Block | 128 KiB |
| Enterprise with API Shield | 10,000 | 10 | 10+ MiB | Log or Block | 128 KiB |

Sources: https://developers.cloudflare.com/api-shield/plans/, https://developers.cloudflare.com/api-shield/security/schema-validation/, https://developers.cloudflare.com/api-shield/security/jwt-validation/, https://developers.cloudflare.com/api-shield/security/graphql-protection/, https://developers.cloudflare.com/api-shield/security/api-discovery/, https://developers.cloudflare.com/api-shield/security/vulnerability-scanner/, https://developers.cloudflare.com/api-shield/security/bola-vulnerability-detection/.
Classic Schema validation is deprecated (https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/).
Rate limiting rules can count by a JWT string claim such as `sub` (https://developers.cloudflare.com/api-shield/security/jwt-validation/).

### Configuration

- Dashboard: **Security** > **Settings** filtered by **API abuse**, and **Web Assets** > **Operations** (https://developers.cloudflare.com/api-shield/get-started/).
- API: API Gateway resources at https://developers.cloudflare.com/api/resources/api_gateway/.
- Terraform: `cloudflare_api_shield` (session identifiers), `cloudflare_api_shield_operation`, `cloudflare_schema_validation_schemas`, `cloudflare_token_validation_config` and `cloudflare_token_validation_rules` (https://developers.cloudflare.com/api-shield/reference/terraform/).
- Learned schemas export as OpenAPI v3.0.0.

---

## 7. Client-side security (formerly Page Shield)

Docs: https://developers.cloudflare.com/client-side-security/ (the sidebar link https://developers.cloudflare.com/page-shield/ redirects here; no `raw/docs/page-shield/` folder exists).

### What it is

Client-side security monitors scripts, connections and cookies loaded in visitors' browsers to catch client-side supply-chain attacks such as Magecart skimmers.
It works by adding a `content-security-policy-report-only` header to a sample of HTML responses; browsers then report every script and connection to Cloudflare (https://developers.cloudflare.com/client-side-security/how-it-works/).
Content security rules add real CSP headers to 100% of matching responses: Log rules use the report-only header and Allow rules use `content-security-policy` to block anything not allowlisted (https://developers.cloudflare.com/client-side-security/rules/).
"The Page Shield add-on is now Client-Side Security Advanced. The features and entitlements are unchanged."

### Plan availability (as of 2026-10-05)

| Feature | Free | Pro | Business | Enterprise | Advanced (add-on) |
| --- | --- | --- | --- | --- | --- |
| Script monitoring | Yes | Yes | Yes | Yes | Yes |
| Connection monitoring, cookie monitoring, page attribution | No | No | Yes | Yes | Yes |
| New Resources and New Domain alerts | No | No | Yes | Yes | Yes |
| Malicious script, code change and malicious connection detection and alerting | No | No | No | No | Yes |
| Cookie monitoring advanced fields | No | No | No | No | Yes |
| Content security rules (positive blocking) | 0 | 0 | 0 | 0 | 5 |
| Logpush jobs | 0 | 0 | 0 | 0 | 4 |

Source: https://developers.cloudflare.com/client-side-security/

### Detection

Malicious script detection analyzes JavaScript with machine learning including an LLM on Workers AI, assigns a JS integrity score 1-99, and classifies a script as malicious below the threshold 10, with sub-scores for Magecart, crypto mining and malware (https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).
The classifier only runs on scripts up to 300 KB.
Malicious URL and domain checks use threat feeds; categories include C2 and botnet, crypto mining, spyware, phishing, malware, DGA domains and typosquatting.

### Configuration

- Dashboard: **Security** > **Settings**, filter **Client-side abuse**, turn on **Continuous script monitoring**; review under **Web assets** > **Client-side resources**; alerts under **Notifications** (https://developers.cloudflare.com/client-side-security/get-started/).
- API (still under the old name): `https://api.cloudflare.com/client/v4/zones/$ZONE_ID/page_shield`, `/page_shield/scripts`, `/page_shield/connections`, `/page_shield/cookies`, `/page_shield/policies` (https://developers.cloudflare.com/client-side-security/reference/api/).
- PCI DSS 4.0 mapping: https://developers.cloudflare.com/client-side-security/reference/pci-dss/.

### Related reading

The blog post "Improving the trustworthiness of Javascript on the Web" previews WAICT (Web Application Integrity, Consistency, and Transparency), a W3C-backed spec Cloudflare coauthored that builds on Subresource Integrity to make site JavaScript auditable (https://blog.cloudflare.com/improving-the-trustworthiness-of-javascript-on-the-web/).

---

## 8. Turnstile

Docs: https://developers.cloudflare.com/turnstile/

### What it is

Turnstile is Cloudflare's CAPTCHA alternative that runs on any website "without sending traffic through Cloudflare".
It runs non-interactive JavaScript challenges (proof-of-work, proof-of-space, web API probing, browser-quirk detection) on the same Challenge Platform as Challenge Pages.
Widget modes: Managed (recommended), Non-interactive and Invisible (https://developers.cloudflare.com/turnstile/concepts/widget/).

### Plans (as of 2026-10-05)

| | Free | Enterprise |
| --- | --- | --- |
| Pricing | Free | Contact Sales |
| Widgets | Up to 20 per account | Unlimited |
| Challenges | Unlimited | Unlimited |
| Hostnames per widget | 10 | 200 |
| Any-hostname widget | No | Yes |
| Analytics lookback | 7 days | 30 days |
| Pre-clearance | Yes | Yes |
| Ephemeral IDs | No | Yes |
| Offlabel (no Cloudflare branding) | No | Yes |

Source: https://developers.cloudflare.com/turnstile/plans/

### Key concepts

- Server-side validation is mandatory: `POST https://challenges.cloudflare.com/turnstile/v0/siteverify` with `secret`, `response`, optional `remoteip` and `idempotency_key` (https://developers.cloudflare.com/turnstile/get-started/server-side-validation/).
- Tokens are at most 2048 characters, valid for 300 seconds, and single use; a replay returns `timeout-or-duplicate`.
- Check `success`, `action` and `hostname` in the response.
- Pre-clearance lets a Turnstile solve also issue a `cf_clearance` cookie at level `interactive`, `managed`, `jschallenge` or `no_clearance` (default) so the visitor skips WAF challenges on the same zone, including API calls from single-page apps (https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/).
- Ephemeral IDs are short-lived per-device identifiers that link activity across rotating IPs without cookies; Enterprise entitlement, then enabled per widget via API (https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/).
- Turnstile Spin is a setup flow from the dashboard, `wrangler turnstile widget create`, or an AI coding agent skill at https://developers.cloudflare.com/turnstile/spin/prompt.md (https://developers.cloudflare.com/turnstile/spin/).
- Test sitekeys: `1x00000000000000000000AA` (always passes), `2x00000000000000000000AB` (always fails), `3x00000000000000000000FF` (forces interactive); test secrets `1x0000000000000000000000000000000AA` (pass), `2x0000000000000000000000000000000AA` (fail), `3x0000000000000000000000000000000AA` (token already spent) (https://developers.cloudflare.com/turnstile/troubleshooting/testing/).

### Configuration

- Dashboard: **Turnstile** > **Add widget** (https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/).
- API: `https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets`, plus `/$SITEKEY` and `/$SITEKEY/rotate_secret` (https://developers.cloudflare.com/turnstile/get-started/widget-management/api/).
- Terraform: `cloudflare_turnstile_widget` with `account_id`, `name`, `domains`, `mode` and `region` (https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/).
- Wrangler: `wrangler turnstile widget create|list|get|update|delete`.

### Most useful pages

- https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/
- https://developers.cloudflare.com/turnstile/tutorials/integrating-turnstile-waf-and-bot-management/
- https://developers.cloudflare.com/turnstile/tutorials/fraud-detection-with-ephemeral-ids/
- https://developers.cloudflare.com/turnstile/get-started/mobile-implementation/
- https://developers.cloudflare.com/turnstile/migration/recaptcha/

---

## 9. Challenges

Docs: https://developers.cloudflare.com/cloudflare-challenges/ (not in the sidebar)

Challenges are how Cloudflare checks that a visitor is human; Cloudflare "does not use CAPTCHA puzzles or visual tests".
Interstitial Challenge Pages are triggered by WAF rules, Bot Management or rate limiting, with actions Non-Interactive Challenge (JavaScript only, usually under five seconds), Managed Challenge (recommended for most rules) and Interactive Challenge (https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/).
Passing sets a `cf_clearance` cookie (max 4096 bytes) bound to the visitor and device; clearance levels are hierarchical (Interactive covers Managed and Non-Interactive) (https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/).
Challenge Passage sets clearance lifetime: default 30 minutes, recommended 15 to 45 minutes, plus an extra hour for XmlHTTP requests; it does not apply to rate limiting rules (https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/).
Precursor is a client-side, session-based script that continuously re-evaluates behavior and can reduce or invalidate clearance mid-session; it is enabled under **Security** > **Settings** (https://developers.cloudflare.com/cloudflare-challenges/precursor/).
JavaScript Detections inject an invisible script into HTML page responses only (not AJAX, API or mobile app traffic), with a 15-minute lifespan, and populate `cf.bot_management.js_detection.passed`; they do not enforce anything without a WAF rule (https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/).
Private Access Tokens reduce challenge steps on supporting devices; a 401 on `/cdn-cgi/challenge-platform/.../pat/...` is expected (https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/).
Cloudflare recommends a rate limiting rule keyed on the `cf_clearance` value so one valid cookie cannot be replayed at volume.

---

## 10. Security Center

Docs: https://developers.cloudflare.com/security-center/

### What it is

Security Center combines attack-surface mapping, asset inventory, configuration scanning and threat intelligence.
Main features: Security Insights (scans DNS, SSL/TLS, WAF and Access settings and reports findings by severity), Infrastructure (domains, IPs and assets), Investigate (IP, domain, hostname lookups with category and passive DNS, plus URL Scanner), Security Reports (beta) and Brand Protection (beta).
It is available on all plans as of 2026-10-05; Administrator Read Only users cannot access it.

### Limits (as of 2026-10-05)

| Threat Intelligence API calls per month | Free | Pro | Business | Enterprise | Cloudforce One Core | Cloudforce One Premier |
| --- | --- | --- | --- | --- | --- | --- |
| Calls | 100 | 100 | 100 | 2,500 | 10,000 | 50,000 |

Investigate, Brand Protection and client-side security also consume this quota; the DDoS Botnet Threat Feed does not (https://developers.cloudflare.com/security-center/intel-apis/limits/).

| URL Scanner | Search history | Public scans per month | Unlisted scans per month | Rate limit |
| --- | --- | --- | --- | --- |
| Free / Radar | last 50 scans | 5,000 | none | 1 per 10 s |
| Self serve | 30 days | 5,000 | 500 | 1 per 10 s |
| Enterprise | 12 months | 10,000 | 5,000 | 12 per s |
| Cloudforce One | Unlimited | 75,000 | 20,000 | 12 per s |

Source: https://developers.cloudflare.com/security-center/investigate/scan-limits/

### Brand Protection (beta)

Brand Protection watches newly registered domains for typosquatting, homoglyphs and service concatenation using string queries (character distance 0-3, max 0 for terms under five characters) and AI logo search (minimum 75% threshold, PNG or JPEG) (https://developers.cloudflare.com/security-center/brand-protection/).
You can report abuse directly only if the lookalike uses Cloudflare Registrar or Cloudflare-hosted IPs; otherwise the dashboard generates Cease and Desist letters from WHOIS data.
Brand Protection alerts and digest need "Professional plans or higher"; Logo Match Alerts need Enterprise.
There is a Brand Protection API (https://developers.cloudflare.com/api/resources/brand_protection/).

### Cloudforce One and indicator feeds

Cloudforce One is Cloudflare's threat intelligence platform (subscription), with threat events datasets (APTs, DDoS, cybercrime, compromised devices, residential proxies, WAF attacks), indicator search including JA3, automated WAF rules, STIX2 export, RFIs and the Cloudy AI agent (https://developers.cloudflare.com/security-center/cloudforce-one/).
Custom Indicator Feeds include public feeds such as the Treasury Early Indicator Feed (feed ID 14) and UK NCSC Public Threat Indicators (feed ID 24) for Gateway users (https://developers.cloudflare.com/security-center/indicator-feeds/).
A managed `security.txt` file can be set up from Security Center (https://developers.cloudflare.com/security-center/infrastructure/security-file/).

---

## 11. Security dashboard (new application security dashboard)

Docs: https://developers.cloudflare.com/security/ (in `llms.txt` under "Other", not in the sidebar)

The new **Security** dashboard is being made default gradually; users can opt in with **Try new dashboard** and opt out "for a limited time", as of 2026-10-05.
It has four areas: Security overview, Security Analytics, Web Assets and Security rules, plus Security settings.
Security overview lists action items by criticality (Critical, Moderate, Low) across categories (web application exploits, AI exploits, DDoS, bot traffic, API abuse, client-side abuse, fraud), with archive reasons False Positive, Accept Risk or Other, and audit-log endpoints such as `GET /api/accounts/{accountID}/insights/audit-log` (https://developers.cloudflare.com/security/overview/).
Security rules unify custom rules, rate limiting rules, API sequence rules, API JWT validation rules, managed rules exceptions and content security rules, with templates (https://developers.cloudflare.com/security/rules/).
Security settings group toggles by threat category: Web application exploits, DDoS attacks, Bot traffic, API abuse and Client-side abuse (https://developers.cloudflare.com/security/settings/).
Web Assets discovers "operations" (HTTP method plus hostname pattern plus path pattern), and labels such as `cf-llm` drive AI Security for Apps (https://developers.cloudflare.com/security/web-assets/).
Security Insights scans run automatically: every 7 days on Free, every 3 days on Pro and Business, daily on Enterprise, and Free scans may pause for inactive accounts (https://developers.cloudflare.com/security/security-insights/how-it-works/).

---

## 12. Key Transparency Auditor

Docs: https://developers.cloudflare.com/key-transparency/ (not in the sidebar)

Cloudflare audits Key Transparency Logs for end-to-end encrypted messaging, starting with WhatsApp, so public keys are distributed through a verifiable append-only log similar to Certificate Transparency.
The Auditor signs epoch information (receive time, epoch number, digest) and verifies facebook/akd proofs asynchronously (https://developers.cloudflare.com/key-transparency/api/auditor-information/).
Public API base: `https://plexi.key-transparency.cloudflare.com` with `/info`, `/namespaces` and `/namespaces/{namespace}/audits/{epoch}`.
Publishing epochs and creating or disabling namespaces is authenticated by mTLS, and new namespaces are registered by contacting Cloudflare (https://developers.cloudflare.com/key-transparency/api/namespaces/).
Epochs must increase by one, have unique 32-byte hex digests, and cannot be republished (https://developers.cloudflare.com/key-transparency/api/epochs/).
Anyone can verify locally with the Rust CLI Plexi (`cargo install plexi`, Rust 1.81+); `plexi ls` lists `whatsapp.key-transparency.v1` (https://developers.cloudflare.com/key-transparency/monitor-the-auditor/).
No pricing or plan gating is stated.

---

## 13. Firewall Rules (deprecated)

Docs: https://developers.cloudflare.com/firewall/ and upgrade guide https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/.
Firewall Rules were expression plus action rules (block, challenge, log, allow, bypass) built on the Filters API, and Cloudflare has moved all existing firewall rules to WAF custom rules, which have the same plan quotas (5, 20, 100 and 1,000 rules; Log action Enterprise only) and replace Allow and Bypass with a single Skip action, evaluate strictly in order, and return a different block response and error page.
The Firewall Rules API, the Filters API and the Terraform resources `cloudflare_firewall_rule` and `cloudflare_filter` have been unsupported since 2025-06-15, so any automation still using them must move to the Rulesets API and `cloudflare_ruleset`; accounts with invalid configurations that blocked the automatic upgrade must contact their account team.

---

## 14. Plan availability cheat sheet

All as of 2026-10-05, from the pages cited above.

| Capability | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Unmetered DDoS (L3-7) | Yes | Yes | Yes | Yes (Advanced DDoS add-on for adaptive rules and 10 overrides) |
| WAF custom rules | 5 | 20 | 100 | 1,000 |
| Rate limiting rules | 1 (IP, 10 s) | 2 | 5 | 100 (Advanced Rate Limiting add-on) |
| Managed rulesets | Free Managed Ruleset | + Managed, OWASP | + Managed, OWASP | + Sensitive Data Detection, account-level |
| Attack score | No | No | Class field | Full |
| Leaked credentials | Password field | + pair field | + pair field | All fields, custom locations |
| Malicious uploads, AI Security for Apps | No | No | No | Paid add-ons |
| Custom lists | 1 | 10 | 10 | 1,000 |
| Bots | Bot Fight Mode | Super Bot Fight Mode | Super Bot Fight Mode + likely automated | Bot Management add-on (score, JA3/JA4) |
| Universal SSL, AOP, Origin CA, managed-CA mTLS | Yes | Yes | Yes | Yes |
| Custom certificates | No | No | Yes | Yes |
| ACM, Total TLS | Paid add-on | Paid add-on | Paid add-on | Paid add-on |
| Keyless SSL, BYOCA mTLS | No | No | No | Yes (Keyless is paid add-on) |
| API Shield schema validation | 100 endpoints, 5 schemas | 250, 5 | 500, 10 | 3,000 or 10,000 with API Shield |
| API Shield discovery, JWT, sequences, GraphQL | No | No | No | API Shield add-on |
| Client-side script monitoring | Yes | Yes | Yes | Yes |
| Client-side connection/cookie monitoring | No | No | Yes | Yes |
| Client-side malicious detection and CSP rules | No | No | No | Client-Side Security Advanced |
| Turnstile | 20 widgets, free | (Free tier) | (Free tier) | Enterprise Turnstile |
| Security Center scans | Every 7 days | Every 3 days | Every 3 days | Daily |
| Threat Intelligence API calls per month | 100 | 100 | 100 | 2,500 |

---

## 15. Build hooks for Web3 projects

Concrete uses for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
Each item names the documented Cloudflare feature it relies on; the Web3 framing is ours, not Cloudflare's.

### Sniper bots, airdrop farming and faucet abuse

- Put a Managed-mode Turnstile widget on faucet claims, allowlist or whitelist signups, airdrop claims and launch "commit" forms, and verify every token server side with `siteverify`, checking `action` and `hostname`, because tokens are single use for 300 seconds and replays fail with `timeout-or-duplicate`.
- Bind the Turnstile `action` to the operation (for example `faucet-claim-base`) and reject tokens minted for another action, so a token farmed on one page cannot be spent on another.
- Do the wallet-address rate limit in your own backend (Durable Object or KV keyed by address), because Free to Business rate limiting rules count only by IP (and IP with NAT support), and JSON body characteristics such as a wallet address in a request body need Enterprise Advanced Rate Limiting.
- On Free, the single rate limiting rule (10-second period, 10-second timeout, path field only) is best spent on the faucet or claim path.
- On Business, count only failed attempts with a counting expression on response codes, the same pattern as the documented OTP example, so legitimate claimers are never limited.
- Rate limiting counters are per data center, so a distributed sniper botnet can exceed a global allowance; treat WAF rate limits as abuse brakes and enforce exact per-wallet or per-launch caps in your own state (Durable Objects) or on-chain.
- With Enterprise Turnstile, use Ephemeral IDs to link claims from one device across rotating IPs, which is the documented defense against fake account creation with IP rotation.
- Use Turnstile pre-clearance (`managed` level) on the launchpad landing page so that a human who solved Turnstile once is not re-challenged by WAF Managed Challenge rules on the zone's API calls for the Challenge Passage window (default 30 minutes).
- Add a rate limiting rule keyed on the `cf_clearance` cookie (documented best practice) so one solved challenge cannot drive thousands of buy calls.

### Bot trading and RPC proxies

- Front your RPC proxy (for example the Helius one-click Cloudflare Worker proxy, `raw/external/github.com_helius-labs_helius-rpc-proxy.md`, whose README itself suggests locking `CORS_ALLOW_ORIGIN`, using the Cloudflare WAF, and allowlisting Cloudflare IP ranges at Helius) with WAF custom rules that only allow `POST` with `content-type: application/json` on the RPC path and block everything else.
- With Enterprise Advanced Rate Limiting, count by JSON field value (the JSON-RPC `method`) or use complexity-based rate limiting where the proxy returns a cost header (1 to 1,000,000) so expensive calls such as `getProgramAccounts` or `eth_getLogs` drain the budget faster than `getBalance`.
- On Business, use a custom counting expression on response headers or codes so only upstream 429s or errors count.
- The same Worker-proxy-plus-WAF pattern applies to Ethereum, Base and Robinhood Chain (4663) JSON-RPC endpoints; keep provider keys in Worker secrets, never in the frontend.
- Bot Management (Enterprise) exposes `cf.bot_management.score`, JA3/JA4 fingerprints and JA4 Signals, which let a trading UI challenge headless scripted clients hitting quote or order endpoints while allowing your own mobile app by its stable JA3/JA4 fingerprint (documented "Allow mobile traffic" use case).
- Do not put Bot Fight Mode on a zone that serves a public trading API or bot-friendly endpoints, because it cannot be skipped and "may challenge API or mobile app traffic"; use Super Bot Fight Mode with Skip rules, or put the API on a separate hostname or zone.
- Challenge pages break non-browser clients (the CLI tools and contract verifiers that get a challenge page instead of JSON), so scope Managed Challenge rules to HTML paths and exempt API paths with Skip rules.
- If you want allowed third-party bots (aggregators, indexers, AI agents) to reach the API, Web Bot Auth lets them sign requests with Ed25519 keys and be treated as verified bots.

### Trading and launchpad APIs

- Upload an OpenAPI schema for your order, quote and launch endpoints to API Shield schema validation: even Free zones get 100 saved endpoints and 5 schemas with Block, which rejects malformed or oversized order payloads before they reach the matcher.
- Free schema validation inspects bodies only up to 1 KiB, Pro and Business up to 8 KiB, Enterprise 128 KiB, so large batch-order bodies will hit body-size violations on lower plans.
- If you issue JWTs after Sign-In with Ethereum or Sign-In with Solana, API Shield JWT validation can verify them at the edge and rate limiting rules can count by the `sub` claim (wallet address) instead of IP (API Shield customers).
- GraphQL malicious query protection limits depth and size for GraphQL indexer endpoints (API Shield, 20 KiB parse limit).
- Use mTLS (managed CA on all plans, 100 client certificates per zone) for server-to-server channels such as keeper bots, market-maker gateways or your own sequencer callbacks, enforced by a custom rule on `cf.tls_client_auth.cert_verified`.
- Use Authenticated Origin Pulls with Full (strict) so the origin running the indexer or relayer accepts only Cloudflare-proxied requests; note AOP does not work with Cloudflare Tunnel.

### Wallet drainers and frontend integrity

- Turn on client-side script monitoring (all plans) on any page that calls `eth_sendTransaction`, `signTypedData` or Solana `signTransaction`, so a newly injected script (the classic wallet-drainer injection after a CDN or npm compromise) shows up in the inventory.
- Business adds connection monitoring, which reveals scripts beaconing to unknown domains (drainers exfiltrate to attacker endpoints), and New Domain alerts.
- Client-Side Security Advanced (add-on) adds the ML malicious script classifier (Magecart, crypto mining, malware scores), code change alerts and up to 5 Allow content security rules that enforce a strict CSP allowlist of script sources, which is the strongest documented control against drainer injection.
- Start content security rules in Log mode, then switch to Allow once the wallet adapters, RPC hosts and analytics domains are allowlisted.
- Pair this with Subresource Integrity on pinned third-party scripts; Cloudflare's WAICT blog post describes where browser-level code transparency is heading.
- Keep SSL/TLS on Full (strict), enable HSTS and Always Use HTTPS, and enable Certificate Transparency Monitoring so you are alerted when any CA issues a certificate for your dapp domain, an early sign of a DNS or registrar hijack.
- CT Monitoring does not catch lookalike domains; use Security Center Brand Protection string queries (character distance up to 3) and logo search to find phishing clones of your launchpad.
- DNSSEC and registrar lock are covered in `protect-connect/03-domains-dns.md`; they complement the controls here against frontend hijacks.

### Application-layer hardening

- Turn on leaked credentials detection (on by default for Free) if the app has any email and password login, and forward the `Exposed-Credential-Check` header to force resets.
- Use the Free Managed Ruleset on every plan and the Cloudflare Managed Ruleset plus OWASP from Pro up in front of admin panels and launchpad back offices; restrict admin paths to an IP list with a custom rule.
- Use malicious uploads detection (Enterprise add-on) on NFT or token-logo upload endpoints to stop malware uploads.
- Use AI Security for Apps (Enterprise add-on) on `cf-llm` labeled endpoints if your trading UI has an LLM assistant, to block prompt injection that tries to make the agent sign or recommend malicious transactions.
- Use Turnstile test keys (`1x00000000000000000000AA`, `2x0000000000000000000000000000000AA`) in CI and Playwright tests of wallet flows instead of disabling verification.

---

## 16. Gaps and contradictions

Flagged, not resolved; each lists the conflicting pages.

1. AI Security for Apps on Enterprise: the WAF overview availability table says "Paid add-on" (https://developers.cloudflare.com/waf/) while the traffic detections table says "Yes" (https://developers.cloudflare.com/waf/detections/); the AI Security for Apps page itself says paid add-on for the log ruleset and detection fields.
2. Managed Rules body inspection size: https://developers.cloudflare.com/waf/managed-rules/ says Enterprise is 128 KB, other paid plans are "lower by default", and Free is 1 MB, which makes the Free limit larger than the Enterprise limit; recorded as written.
3. Custom rules Log action: the custom rules availability table says Log is Enterprise only (https://developers.cloudflare.com/waf/custom-rules/), while the interoperability page lists Log among custom rule actions without that caveat (https://developers.cloudflare.com/waf/feature-interoperability/).
4. The interoperability page's "E-commerce site (Pro or Business plan)" scenario says those plans "add" custom rules and Managed Rules, but custom rules and the Free Managed Ruleset are already on Free.
5. DDoS proactive false positive detection: the DDoS overview table says No for Business (https://developers.cloudflare.com/ddos-protection/), while the managed rulesets page says "Only available on Business and Enterprise plans" (https://developers.cloudflare.com/ddos-protection/managed-rulesets/).
6. Adaptive DDoS Protection: the overview table gives error adaptive rules to every plan including Free, while the adaptive protection page says it "is available to Enterprise customers" (https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/).
7. DDoS overrides: the DDoS overview and HTTP ruleset pages say all plans can create one override, while the Security rules and Security settings pages say "DDoS attack protection overrides are only available to Enterprise customers with the Advanced DDoS Protection subscription" (https://developers.cloudflare.com/security/rules/, https://developers.cloudflare.com/security/settings/).
8. Certificate validity: the validity periods page says "Cloudflare only issues certificates with validity periods of three months or less" while the same page lists a 1-year validity for Enterprise advanced certificates from SSL.com (https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/).
9. Certificate Transparency Monitoring status: the Key Transparency overview calls it "an opt-in feature in public beta" (https://developers.cloudflare.com/key-transparency/), while the CT Monitoring page itself does not mention beta (https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).
10. Turnstile accessibility: the overview says "WCAG 2.2 AA compliant" (https://developers.cloudflare.com/turnstile/) and the plans table says "WCAG 2.2 AAA compliance" (https://developers.cloudflare.com/turnstile/plans/).
11. API Shield availability: the overview says "Cloudflare API Security products are available to Enterprise customers only" (https://developers.cloudflare.com/api-shield/), while the plans page gives Free, Pro and Business zones saved endpoints and uploaded schemas with a Block action (https://developers.cloudflare.com/api-shield/plans/).
12. Security Center scan frequency: the Security Center overview says every 7 days on Free, Pro and Business and every 3 days on Enterprise (https://developers.cloudflare.com/security-center/), while Get started and Security Insights How it works say Free 7 days, Pro and Business 3 days, Enterprise daily (https://developers.cloudflare.com/security-center/get-started/, https://developers.cloudflare.com/security/security-insights/how-it-works/).
13. Security Center manual scans: the overview and Get started say only accounts with a Business or Enterprise zone (or Teams Standard or Enterprise) can start a manual scan, while the scan frequency tables on the same Get started page and on How it works say on-demand scans are available on all plans.
14. Super Bot Fight Mode customization: its page says it "Cannot be customized, adjusted, or reconfigured via WAF custom rules" and, a few lines later, explains configuring exceptions with a Skip custom rule (https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/).
15. Client-side malicious detection: the malicious detection page says "Domain-based threat intelligence is available to all customers", while the availability table lists malicious connection detection and alerting only for Advanced (https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/, https://developers.cloudflare.com/client-side-security/).
16. Execution order pages differ in scope: the WAF concepts page lists IP Access rules first in the order, while the interoperability page says IP Access rules are outside the Ruleset Engine and "do not follow the phase order".
17. Security settings page lists Block AI Bots, Bot Management, Challenge Passage, schema learning and similar bot or API settings under the "DDoS attacks" category, which looks like a copy error (https://developers.cloudflare.com/security/settings/).
18. Gaps: no dollar pricing exists in the docs for Pro, Business, Enterprise, Advanced Certificate Manager, Advanced Rate Limiting, Bot Management, API Shield, Client-Side Security Advanced, malicious uploads or AI Security for Apps; Key Transparency states no plan or pricing; Precursor's plan availability is not stated on its page; Programmable Flow Protection, Attack Signature Detection, Application Profiles (without API Shield), Account Abuse Protection, Brand Protection, Security Reports and the Vulnerability Scanner are beta or Early Access as of 2026-10-05 with no GA dates.
19. Naming drift: the sidebar still says "Page Shield" and the API paths still use `/page_shield/`, while the docs product is "Client-side security" and the add-on is "Client-Side Security Advanced"; "malicious uploads detection" and "content scanning" name the same feature (fields `cf.waf.content_scan.*`, Terraform `cloudflare_content_scanning`); "AI Security for Apps" was "Firewall for AI".
