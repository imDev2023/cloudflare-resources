# Docs navigation map

The sidebar of https://developers.cloudflare.com/ with every dropdown expanded, as captured on the date in `raw/docs/_manifest.json`.
Page counts are the mirrored pages under each URL in `raw/docs/`; the last column is the synthesized file that covers the entry.
Regenerate with `python3 scripts/build-nav.py`.

## Get started

- [Overview](https://developers.cloudflare.com/) - 1 pages - `platform-and-tooling.md`
- [API](https://developers.cloudflare.com/api/) - 30 pages - `platform-and-tooling.md`
- [Agent Setup](https://developers.cloudflare.com/agent-setup/) - 12 pages - `platform-and-tooling.md`
- [Directory](https://developers.cloudflare.com/directory/) - 1 pages - `platform-and-tooling.md`
- [Changelog](https://developers.cloudflare.com/changelog/) - 1579 pages - `platform-and-tooling.md`
- **Resources** - `platform-and-tooling.md`
  - [Learning paths](https://developers.cloudflare.com/resources/?filter-pcx_content_type=learning-path) - 1 pages - `platform-and-tooling.md`
  - [Use cases](https://developers.cloudflare.com/use-cases/) - 59 pages - `platform-and-tooling.md`
  - [Reference architecture](https://developers.cloudflare.com/reference-architecture/) - 80 pages - `platform-and-tooling.md`
- **API & IaC** - `platform-and-tooling.md`
  - [API reference](https://developers.cloudflare.com/api/) - 30 pages - `platform-and-tooling.md`
  - [Terraform](https://developers.cloudflare.com/terraform/) - 26 pages - `platform-and-tooling.md`
  - [Pulumi](https://developers.cloudflare.com/pulumi/) - 7 pages - `platform-and-tooling.md`
  - [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) - 1 pages - `platform-and-tooling.md`
- [Support](https://developers.cloudflare.com/support/) - 121 pages - `platform-and-tooling.md`

## Developer Tools

- [Cloudflare CLI](https://developers.cloudflare.com/cf/) - 13 pages - `platform-and-tooling.md`

## Build

- **Compute** - `build/01-compute.md`
  - [Workers](https://developers.cloudflare.com/workers/) - 439 pages - `build/01-compute.md`
  - [Containers](https://developers.cloudflare.com/containers/) - 39 pages - `build/01-compute.md`
  - [Durable Objects](https://developers.cloudflare.com/durable-objects/) - 54 pages - `build/01-compute.md`
  - [Queues](https://developers.cloudflare.com/queues/) - 37 pages - `build/01-compute.md`
  - [Workflows](https://developers.cloudflare.com/workflows/) - 34 pages - `build/01-compute.md`
  - [Flagship](https://developers.cloudflare.com/flagship/) - 21 pages - `build/01-compute.md`
  - [Browser Run](https://developers.cloudflare.com/browser-run/) - 53 pages - `build/01-compute.md`
  - [Workers VPC](https://developers.cloudflare.com/workers-vpc/) - 21 pages - `build/01-compute.md`
  - [Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/) - 88 pages - `build/01-compute.md`
  - [Email Service](https://developers.cloudflare.com/email-service/) - 51 pages - `build/01-compute.md`
- **AI** - `build/02-ai.md`
  - [Models](https://developers.cloudflare.com/ai/models/) - 234 pages - `build/02-ai.md`
  - [Workers AI](https://developers.cloudflare.com/workers-ai/) - 131 pages - `build/02-ai.md`
  - [AI Gateway](https://developers.cloudflare.com/ai-gateway/) - 98 pages - `build/02-ai.md`
  - [Agents](https://developers.cloudflare.com/agents/) - 130 pages - `build/02-ai.md`
  - [Agent Memory](https://developers.cloudflare.com/agent-memory/) - 11 pages - `build/02-ai.md`
  - [Wallets](https://developers.cloudflare.com/wallets/) - 2 pages - `build/02-ai.md`
  - [Sandboxes](https://developers.cloudflare.com/sandbox/) - 120 pages - `build/02-ai.md`
  - [Vectorize](https://developers.cloudflare.com/vectorize/) - 23 pages - `build/02-ai.md`
  - [AI Search](https://developers.cloudflare.com/ai-search/) - 84 pages - `build/02-ai.md`
  - [Web Search API](https://developers.cloudflare.com/web-search/) - 4 pages - `build/02-ai.md`
  - [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) - 34 pages - `build/02-ai.md`
- **Storage & Database** - `build/03-storage-database.md`
  - [R2](https://developers.cloudflare.com/r2/) - 84 pages - `build/03-storage-database.md`
  - **Basin** - `build/03-storage-database.md`
    - [Overview](https://developers.cloudflare.com/basin/) - 7 pages - `build/03-storage-database.md`
    - [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) - 39 pages - `build/03-storage-database.md`
    - [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) - 17 pages - `build/03-storage-database.md`
    - [Basin SQL](https://developers.cloudflare.com/basin-sql/) - 15 pages - `build/03-storage-database.md`
  - [K2](https://developers.cloudflare.com/k2/) - 9 pages - `build/03-storage-database.md`
  - [D1](https://developers.cloudflare.com/d1/) - 54 pages - `build/03-storage-database.md`
  - [KV](https://developers.cloudflare.com/kv/) - 32 pages - `build/03-storage-database.md`
  - [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) - 64 pages - `build/03-storage-database.md`
  - [Artifacts](https://developers.cloudflare.com/artifacts/) - 32 pages - `build/03-storage-database.md`
- **Media** - `build/04-media.md`
  - [Images](https://developers.cloudflare.com/images/) - 64 pages - `build/04-media.md`
  - [Stream](https://developers.cloudflare.com/stream/) - 65 pages - `build/04-media.md`
  - [Realtime](https://developers.cloudflare.com/realtime/) - 715 pages - `build/04-media.md`

## Protect & Connect

- **Application Security** - `protect-connect/01-application-security.md`
  - [WAF](https://developers.cloudflare.com/waf/) - 170 pages - `protect-connect/01-application-security.md`
  - [DDoS Protection](https://developers.cloudflare.com/ddos-protection/) - 152 pages - `protect-connect/01-application-security.md`
  - [SSL/TLS](https://developers.cloudflare.com/ssl/) - 137 pages - `protect-connect/01-application-security.md`
  - [Bots](https://developers.cloudflare.com/bots/) - 50 pages - `protect-connect/01-application-security.md`
  - [API Shield](https://developers.cloudflare.com/api-shield/) - 37 pages - `protect-connect/01-application-security.md`
  - [Page Shield](https://developers.cloudflare.com/page-shield/) - 0 pages - `protect-connect/01-application-security.md`
  - [Turnstile](https://developers.cloudflare.com/turnstile/) - 45 pages - `protect-connect/01-application-security.md`
  - [Security Center](https://developers.cloudflare.com/security-center/) - 16 pages - `protect-connect/01-application-security.md`
- **Cloudflare One** - `protect-connect/02-cloudflare-one.md`
  - [Overview](https://developers.cloudflare.com/cloudflare-one/) - 740 pages - `protect-connect/02-cloudflare-one.md`
  - [Insights & Logs](https://developers.cloudflare.com/cloudflare-one/insights/) - 42 pages - `protect-connect/02-cloudflare-one.md`
  - [Team & Resources](https://developers.cloudflare.com/cloudflare-one/team-and-resources/) - 66 pages - `protect-connect/02-cloudflare-one.md`
  - [Networks](https://developers.cloudflare.com/cloudflare-one/networks/) - 200 pages - `protect-connect/02-cloudflare-one.md`
  - [Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/) - 82 pages - `protect-connect/02-cloudflare-one.md`
  - [Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) - 54 pages - `protect-connect/02-cloudflare-one.md`
  - [Cloud & SaaS findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/) - 5 pages - `protect-connect/02-cloudflare-one.md`
  - [Email security](https://developers.cloudflare.com/cloudflare-one/email-security/) - 77 pages - `protect-connect/02-cloudflare-one.md`
  - [Data loss prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) - 18 pages - `protect-connect/02-cloudflare-one.md`
  - [Browser isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) - 11 pages - `protect-connect/02-cloudflare-one.md`
  - [Reusable components](https://developers.cloudflare.com/cloudflare-one/reusable-components/) - 28 pages - `protect-connect/02-cloudflare-one.md`
  - [Integrations](https://developers.cloudflare.com/cloudflare-one/integrations/) - 81 pages - `protect-connect/02-cloudflare-one.md`
- **Domains & DNS** - `protect-connect/03-domains-dns.md`
  - [DNS](https://developers.cloudflare.com/dns/) - 137 pages - `protect-connect/03-domains-dns.md`
  - [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) - 40 pages - `protect-connect/03-domains-dns.md`
  - [Registrar](https://developers.cloudflare.com/registrar/) - 23 pages - `protect-connect/03-domains-dns.md`
  - [Email Routing](https://developers.cloudflare.com/email-service/) - 51 pages - `protect-connect/03-domains-dns.md`
  - [DMARC Management](https://developers.cloudflare.com/dmarc-management/) - 5 pages - `protect-connect/03-domains-dns.md`
- **Networking** - `protect-connect/04-networking.md`
  - [Tunnel](https://developers.cloudflare.com/tunnel/) - 40 pages - `protect-connect/04-networking.md`
  - [Mesh](https://developers.cloudflare.com/mesh/) - 11 pages - `protect-connect/04-networking.md`
  - [Magic Transit](https://developers.cloudflare.com/magic-transit/) - 43 pages - `protect-connect/04-networking.md`
  - [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/) - 110 pages - `protect-connect/04-networking.md`
  - [Network Interconnect](https://developers.cloudflare.com/network-interconnect/) - 7 pages - `protect-connect/04-networking.md`
  - [Spectrum](https://developers.cloudflare.com/spectrum/) - 22 pages - `protect-connect/04-networking.md`
  - [BYOIP](https://developers.cloudflare.com/byoip/) - 21 pages - `protect-connect/04-networking.md`
- **Monetize** - `protect-connect/05-monetize.md`
  - [Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/) - 7 pages - `protect-connect/05-monetize.md`
- **Delivery & Performance** - `protect-connect/06-delivery-performance.md`
  - [Cache](https://developers.cloudflare.com/cache/) - 91 pages - `protect-connect/06-delivery-performance.md`
  - [Speed](https://developers.cloudflare.com/speed/) - 43 pages - `protect-connect/06-delivery-performance.md`
  - [Load Balancing](https://developers.cloudflare.com/load-balancing/) - 63 pages - `protect-connect/06-delivery-performance.md`
  - [Waiting Room](https://developers.cloudflare.com/waiting-room/) - 30 pages - `protect-connect/06-delivery-performance.md`
  - [Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/) - 4 pages - `protect-connect/06-delivery-performance.md`
  - [Zaraz](https://developers.cloudflare.com/zaraz/) - 50 pages - `protect-connect/06-delivery-performance.md`

## Manage & Observe

- **Observe** - `manage-observe.md`
  - [Observability](https://developers.cloudflare.com/observability/) - 14 pages - `manage-observe.md`
  - [Analytics](https://developers.cloudflare.com/analytics/) - 117 pages - `manage-observe.md`
  - [Web Analytics](https://developers.cloudflare.com/web-analytics/) - 17 pages - `manage-observe.md`
  - [Logs](https://developers.cloudflare.com/logs/) - 110 pages - `manage-observe.md`
  - [Log Explorer](https://developers.cloudflare.com/log-explorer/) - 9 pages - `manage-observe.md`
  - [Health Checks](https://developers.cloudflare.com/health-checks/) - 8 pages - `manage-observe.md`

## Products not in the sidebar

These are listed in https://developers.cloudflare.com/llms.txt but have no sidebar entry; see `other-products.md` unless another file is named in the README.

- [Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/) (Application performance) - 16 pages - Improve WordPress site performance by serving it from Cloudflare's global network
- [China Network](https://developers.cloudflare.com/china-network/) (Application performance) - 11 pages - Fast, global network serving visitors inside and outside of China
- [Google tag gateway for advertisers](https://developers.cloudflare.com/google-tag-gateway/) (Application performance) - 1 pages - Add a layer of data security and privacy controls when using Google Tag Manager
- [Smart Shield](https://developers.cloudflare.com/smart-shield/) (Application performance) - 23 pages - Safeguard your origin with just a few clicks.
- [Web3](https://developers.cloudflare.com/web3/) (Application performance) - 34 pages - Gateways to networks to help you develop applications without worrying about running infrastructure
- [Challenges](https://developers.cloudflare.com/cloudflare-challenges/) (Application security) - 21 pages - Verify visitors are not bots with lightweight challenges
- [Client-side security](https://developers.cloudflare.com/client-side-security/) (Application security) - 28 pages - Provide client-side protection for your website visitors
- [Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/) (Application security) - 28 pages - Create rules that examine incoming HTTP traffic against a set of powerful filters to block, challenge, log, or allow matching requests. Firewall Rules have been replaced with WAF custom rules.
- [Key Transparency Auditor](https://developers.cloudflare.com/key-transparency/) (Application security) - 6 pages - Secure the distribution of public keys in E2EE messaging systems
- [Secrets Store](https://developers.cloudflare.com/secrets-store/) (Application security) - 7 pages - Encrypt and store sensitive information as secrets that are securely reusable across an account
- [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) (Cloudflare One) - 34 pages - Protect your enterprise network with advanced firewall-as-a-service protection
- [Data Localization Suite](https://developers.cloudflare.com/data-localization/) (Cloudflare One) - 27 pages - Control where Cloudflare stores and inspects data
- [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/) (Cloudflare One) - 6 pages - Automate resource discovery and simplify managing your public cloud infrastructure
- [Radar](https://developers.cloudflare.com/radar/) (Consumer services) - 26 pages - Investigate Internet usage around the world using Cloudflare's data
- [WARP Client](https://developers.cloudflare.com/warp-client/) (Consumer services) - 12 pages - Allows individuals or organizations to have a faster, more secure connection to the Internet
- [Billing](https://developers.cloudflare.com/billing/) (Core platform) - 33 pages - Manage billing, plans, and subscriptions for your account
- [Network](https://developers.cloudflare.com/network/) (Core platform) - 8 pages - Manage Cloudflare network settings for your website
- [Notifications](https://developers.cloudflare.com/notifications/) (Core platform) - 10 pages - Define what you want to be notified about and how
- [Randomness Beacon](https://developers.cloudflare.com/randomness-beacon/) (Core platform) - 9 pages - Explore drand, a distributed service providing randomness to applications
- [Resource Tagging](https://developers.cloudflare.com/resource-tagging/) (Core platform) - 9 pages - Attach key-value metadata to Cloudflare resources for organization, access control, and billing attribution
- [Rules](https://developers.cloudflare.com/rules/) (Core platform) - 188 pages - Modify incoming requests, change Cloudflare settings, or trigger actions
- [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/) (Core platform) - 235 pages - Create rulesets and rules for different Cloudflare products
- [Tenant](https://developers.cloudflare.com/tenant/) (Core platform) - 11 pages - Provision and manage Cloudflare accounts and services for your team or customers
- [Time Services](https://developers.cloudflare.com/time-services/) (Core platform) - 9 pages - Cloudflare's suite of time services: NTP, NTS, and Roughtime
- [Version Management](https://developers.cloudflare.com/version-management/) (Core platform) - 14 pages - Safely manage configurations on Cloudflare's global network with versioning, staging, and rollbacks
- [Agent Lee](https://developers.cloudflare.com/agent-lee/) (Developer platform) - 3 pages - An AI co-pilot built into the Cloudflare dashboard that helps you navigate, configure, and take actions on Cloudflare services
- [Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/) (Developer platform) - 7 pages - Implement the Oblivious HTTP IETF standard to improve client privacy
- [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) (Developer platform) - 19 pages - Spin up isolated Workers on demand to execute code
- [MoQ](https://developers.cloudflare.com/moq/) (Developer platform) - 4 pages - Protocol for live media
- [Pages](https://developers.cloudflare.com/pages/) (Developer platform) - 123 pages - Build full-stack, serverless applications globally with minimal configuration
- [Privacy Pass](https://developers.cloudflare.com/privacy-pass/) (Developer platform) - 7 pages - Privacy Pass tokens let users prove a claim without revealing their identity or being tracked across requests.
- [Privacy Proxy](https://developers.cloudflare.com/privacy-proxy/) (Developer platform) - 14 pages - A MASQUE-based forward proxy that protects user privacy while preserving geolocation accuracy
- [Learning Paths](https://developers.cloudflare.com/learning-paths/) (Docs collections) - 322 pages - Guided modules and projects to help you get started with Cloudflare
- [Network Error Logging](https://developers.cloudflare.com/network-error-logging/) (Network security) - 4 pages - Review connectivity issues to learn when and where an incident is happening and its impact
- [Network Flow](https://developers.cloudflare.com/network-flow/) (Network security) - 23 pages - Visibility into your network and cloud traffic by analyzing network flow data
- [Docs for agents](https://developers.cloudflare.com/docs-for-agents/) (Other) - 1 pages - Learn how AI agents and LLMs consume Cloudflare documentation
- [Migration Guides](https://developers.cloudflare.com/migration-guides/) (Other) - 1 pages - Content designed to help you migrate from another provider to Cloudflare.
- [Security dashboard](https://developers.cloudflare.com/security/) (Other) - 14 pages - Documentation for the Security dashboard with an updated user interface.
- [Style Guide](https://developers.cloudflare.com/style-guide/) (Other) - 156 pages - Style guide to follow for contributing to Cloudflare docs.

Total mirrored docs pages: 8878.
