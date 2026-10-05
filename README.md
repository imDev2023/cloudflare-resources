# Cloudflare knowledge base

Everything on Cloudflare's developer platform and network products, scraped and distilled on 2026-10-05.
Read the synthesized files first; drop into `raw/` only when you need the exact source wording.

This repository is the one canonical copy.
Locally it lives at `/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/cloudflare`; elsewhere use https://github.com/imDev2023/cloudflare-resources (public).
Projects point at it and never copy it.
The `cloudflare-kb` skill (`~/.claude/skills/cloudflare-kb/SKILL.md`) is the pointer other sessions use.

## What was scraped

| Source | Where | Size |
| --- | --- | --- |
| Every page of developers.cloudflare.com, as its official Markdown (`<url>/index.md`), discovered from all 134 nested `llms.txt` indexes plus the sitemap | `raw/docs/<url path>/index.md` | 8,957 URLs fetched, 0 failures, 77 redirects (`raw/docs/_manifest.json`) |
| The changelog (part of the docs mirror) | `raw/docs/changelog/` | 1,579 pages, 1,307 posts |
| The docs sidebar with every dropdown expanded, captured in a browser | `raw/nav/home-sidebar.{json,md}` | 13 groups, 93 links |
| API reference (developers.cloudflare.com/api/) | `raw/api/resources/**/index.md`, `raw/api/llms.txt` | 1,111 resource pages |
| Official OpenAPI spec (github.com/cloudflare/api-schemas) | `raw/api/openapi.json` (gitignored), `raw/api/endpoints.tsv` | 3,647 operations on 2,287 paths |
| Cloudflare blog posts tagged web3, ethereum, ipfs, x402, payments, cryptography, randomness | `raw/blog/` (local only; `index.tsv` committed) | 38 posts |
| Press releases and third-party pages (NET Dollar, Wallets, x402 Foundation, Helius RPC proxy) | `raw/external/` (local only; `urls.txt` committed) | 7 pages |
| Every public repo of the cloudflare GitHub org | `raw/github/repos.tsv`, `raw/github/readmes/` | 580 repos, 80 READMEs |
| Alternative platforms research (Tavily and Jina), plus 129 llms.txt probes | `raw/alternatives/` (`llms-probe.tsv`; third-party `llms-full` dumps gitignored) | 47 searches, 148 pages |

Scraping used the official Markdown endpoints with plain HTTP (no scraping service), `agent-browser` for the sidebar, `gh` for GitHub, and Tavily and Jina for third-party pages.

## Sources and license

The mirrored Cloudflare documentation in `raw/docs/` and `raw/api/` is by Cloudflare, Inc. and contributors, used under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (code samples under MIT), as stated in https://github.com/cloudflare/cloudflare-docs.
Cloudflare names and logos are trademarks of Cloudflare; this repository is not affiliated with or endorsed by Cloudflare.
The synthesized files are original notes that cite their sources.
Third-party material (Cloudflare blog posts, press releases, news articles and other platforms' docs) is not redistributed here: only its URL lists are committed (`raw/blog/index.tsv`, `raw/external/urls.txt`, `raw/alternatives/llms-probe.tsv`), and `scripts/fetch-blog.py` and `scripts/jina-fetch.sh` re-fetch it locally.

## Keeping it current

Anything that moves (prices, limits, beta or GA status, model lists) is a snapshot dated 2026-10-05; re-check the live docs before relying on it in production.
Any docs page is available live as Markdown by appending `index.md` to its URL.
When a project learns something new about Cloudflare, write it back here, not only into the project.

| Step | Command |
| --- | --- |
| Refresh everything below in one go | `scripts/refresh-all.sh` |
| Re-mirror every docs page | `python3 scripts/fetch-docs.py` |
| Re-mirror the API reference, OpenAPI spec and `endpoints.tsv` | `python3 scripts/fetch-api.py` |
| Re-mirror the Web3 and payments blog posts (extra URLs in `raw/blog/extra-urls.txt`) | `python3 scripts/fetch-blog.py` |
| Refresh the GitHub org catalog and READMEs | `scripts/fetch-repos.sh` |
| Re-capture the sidebar (agent-browser, own named session) | `scripts/capture-nav.sh` |
| Rebuild `navigation.md` | `python3 scripts/build-nav.py` |
| Scrape a list of third-party pages | `JINA_API_KEY=... xargs -P 6 -I{} scripts/jina-fetch.sh {} < raw/external/urls.txt` |

After a refresh, `git diff --stat raw/` shows which pages changed, and the synthesized files covering those pages need updating.

## Where to start

| Question | Read |
| --- | --- |
| Which page or file covers what; the sidebar with page counts; products missing from the sidebar | [navigation.md](navigation.md) |
| Agent Setup, MCP servers, skills, the `cf` CLI, Wrangler, Terraform, Pulumi, SDKs, Support, Fundamentals | [platform-and-tooling.md](platform-and-tooling.md) |
| The REST API: auth, token types, scoping, rate limits, all 128 resources, local endpoint lookup | [api-reference.md](api-reference.md) |
| Build > Compute: Workers, Containers, Durable Objects, Queues, Workflows, Flagship, Browser Run, Workers VPC, Cloudflare for Platforms, Email Service, Pages, Dynamic Workers | [build/01-compute.md](build/01-compute.md) |
| Build > AI: Models, Workers AI, AI Gateway, Agents SDK, x402 and MPP payments, Agent Memory, Wallets, Sandboxes, Vectorize, AI Search, Web Search API, AI Crawl Control, Agent Lee | [build/02-ai.md](build/02-ai.md) |
| Build > Storage & Database: R2, Basin (Pipelines, Catalog, SQL), K2, D1, KV, Hyperdrive, Artifacts, Secrets Store | [build/03-storage-database.md](build/03-storage-database.md) |
| Build > Media: Images, Stream, Realtime, MoQ | [build/04-media.md](build/04-media.md) |
| Application Security: WAF, DDoS, SSL/TLS, Bots, API Shield, Page Shield (client-side security), Turnstile, Security Center | [protect-connect/01-application-security.md](protect-connect/01-application-security.md) |
| Cloudflare One (Zero Trust): Access, Gateway, Tunnel connectors, CASB, DLP, RBI | [protect-connect/02-cloudflare-one.md](protect-connect/02-cloudflare-one.md) |
| Domains & DNS: DNS, 1.1.1.1, Registrar, Email Routing, DMARC, Web3 (Ethereum and IPFS) gateways | [protect-connect/03-domains-dns.md](protect-connect/03-domains-dns.md) |
| Networking: Tunnel, Mesh, Magic Transit, Cloudflare WAN, Interconnect, Spectrum, BYOIP | [protect-connect/04-networking.md](protect-connect/04-networking.md) |
| Monetize: Monetization Gateway, x402, NET Dollar, paying Cloudflare in USDC | [protect-connect/05-monetize.md](protect-connect/05-monetize.md) |
| Delivery & Performance: Cache, Speed, Load Balancing, Waiting Room, Argo, Zaraz | [protect-connect/06-delivery-performance.md](protect-connect/06-delivery-performance.md) |
| Manage & Observe: Observability, Analytics, Web Analytics, Logs, Log Explorer, Health Checks, Notifications | [manage-observe.md](manage-observe.md) |
| Everything not in the sidebar: Rules, Ruleset Engine, Billing, Randomness Beacon (drand), Radar, Tenant and more | [other-products.md](other-products.md) |
| What changed in the last 12 months, the 2026 timeline, deprecations and upcoming cutoffs | [changelog.md](changelog.md) |
| How to launch a dapp, launchpad or trading UI on Solana, Ethereum, Base or Robinhood Chain with Cloudflare | [web3-launch-playbook.md](web3-launch-playbook.md) |
| Platforms similar to Cloudflare, and which to use or scrape next | [alternatives.md](alternatives.md) |
| What each cloudflare GitHub repo does | [github-repos.md](github-repos.md) |

Every product file ends with a "Build hooks for Web3 projects" section and a "Gaps and contradictions" section where the official sources disagree.

## Headline facts (as of 2026-10-05)

- Cloudflare's only on-chain access is the Web3 gateways: an Ethereum JSON-RPC gateway (Mainnet and Sepolia only, HTTP only, `eth_getLogs` capped at 800 blocks) and a read-only IPFS gateway, both a paid add-on with 500k requests or 50 GB included.
- There is no Cloudflare gateway or RPC for Solana, Base or Robinhood Chain; for those, Cloudflare is the hosting, API, security and real-time layer in front of a third-party RPC (see [web3-launch-playbook.md](web3-launch-playbook.md)).
- Robinhood Chain (4663) appears in no Cloudflare source.
- The crypto features are about payments: x402 tools in the Agents SDK (docs list EVM, Solana and others, but every Cloudflare sample is Base or Base Sepolia), Monetization Gateway (closed beta since 2026-09-30, US only, settles USDC on Base), AI Gateway Machine Payments (beta), paying Cloudflare invoices in USDC on Base or Polygon, Cloudflare Wallets (handle reservation only), and NET Dollar (announced, no docs).
- Workers Paid is $5 a month with 10M requests and 30M CPU-ms included; Free is 100k requests a day, 10 ms CPU and 50 subrequests; Node.js compatibility is on by default from compatibility date 2026-08-04.
- New projects should use Workers static assets; the Pages docs say "Start new projects with Workers", with no Pages deprecation date.
- `cf` is the new all-API CLI (beta since 2026-09-28, 2,900+ commands, JSON output); Wrangler remains the Workers dev and deploy tool.
- The Code Mode API MCP server at `https://mcp.cloudflare.com/mcp` reaches the whole API through two tools; agent guides also install 16 skills from `cloudflare/skills`.
- Basin (formerly Pipelines, R2 Data Catalog and R2 SQL) and AI Search went GA on 2026-10-01.
- Waiting Room needs Business or higher (advanced queueing needs Enterprise); rate limiting by a JSON body field such as a wallet address needs Enterprise, so exact per-wallet limits need your own state, for example a Durable Object.
- Turnstile is free with unlimited challenges and up to 20 widgets.
- Best companions to Cloudflare for the owner's chains (recommendation in [alternatives.md](alternatives.md)): Helius then Triton for Solana RPC; Alchemy, with dRPC as fallback and Chainstack for debug and trace, for EVM including Robinhood Chain; Privy or Turnkey for embedded wallets; the Coinbase CDP x402 facilitator on Base and Solana.
- Avoid Fleek (hosting shut down 2026-01-31), Google Blockchain Node Engine (shuts 2026-12-15) and Amazon Managed Blockchain (no new customers from 2026-10-29).
- The OpenAPI spec has 3,647 operations, but the published reference lists only 2,824; 736 operations (Agent Memory, Artifacts, K2, Monetization and others) have no reference page.

## Known stale or broken things

- `cloudflare-eth.com` still answers but refuses requests: `eth_blockNumber` returned JSON-RPC error `-32046 Cannot fulfill request` (live check, 2026-10-05).
- `cloudflare-ipfs.com` no longer resolves in DNS (live check, 2026-10-05); the public IPFS gateways moved to Interplanetary Shipyard on 2024-08-14, yet many docs pages still use them in examples.
- The sidebar's "Page Shield" entry points to `/page-shield/`, which redirects; the content is at `/client-side-security/`.
- Cloudflare's "Choose a storage product" page omits K2, Artifacts, Basin Catalog and Basin SQL.
- The legacy KV REST routes (`/workers/namespaces/*`) stop working on 2026-10-15, and Stream WebRTC live streaming starts billing the same day.
- Service Key auth reached end of life on 2026-09-30, yet the OpenAPI spec still lists it on 83 operations.
- `McpAgent` is deprecated (Agents SDK v0.20.0), but it is still the base class of the x402 `paidTool` and MPP samples.
- The Workers AI pricing page still prices models deprecated on 2026-05-30.
- Several Logpush pages still say Enterprise only, but Logpush is on every plan since 2026-09-30.
- The changelog's RSS page lists group feeds for only 7 of 13 product groups.
