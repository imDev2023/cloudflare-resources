---
name: cloudflare-kb
description: "The owner's Cloudflare knowledge base: a full Markdown mirror of developers.cloudflare.com (every product, about 8,900 pages incl. 1,579 changelog entries), the API reference (1,111 resource pages, 3,647 endpoints from the OpenAPI spec), the docs sidebar map, Web3/x402/Wallets/NET Dollar blog and press material, a 580-repo GitHub catalog, distilled guides per sidebar section, a Web3 launch playbook for Solana, Ethereum, Base and Robinhood Chain, and a survey of alternative platforms. Use at the start of ANY work that touches Cloudflare (Workers, Pages, Durable Objects, D1, KV, R2, Queues, Workflows, Containers, Workers AI, Agents SDK, AI Gateway, Turnstile, WAF, DNS, Tunnel, Access, Zero Trust, Web3 gateways, x402, Monetization Gateway, Wallets, wrangler, cf CLI) or hosting/infrastructure choices for a Web3 project, BEFORE searching the web or answering from memory. Trigger: /cloudflare-kb"
trigger: /cloudflare-kb
---

# Cloudflare knowledge base

This skill is a pointer.
The knowledge base is a git repository, and there is exactly one canonical copy of it.

1. **Locally**: `/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/cloudflare`
2. **On GitHub** (public), when the local path is not reachable: https://github.com/imDev2023/cloudflare-resources

Read from the canonical copy only, never copy it into a project.

## How to use it

1. Run `git -C "/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/cloudflare" pull --ff-only` if the session will rely on it for more than a quick lookup.
2. Read `README.md` in the repository root first; it is the index and lists known stale or broken things.
3. Read the specific file for the question, not the whole repository.
4. For exact wording, open the mirrored page: `raw/docs/<url path>/index.md` mirrors `https://developers.cloudflare.com/<url path>/`.
   Find pages with `grep -ril "<term>" raw/docs/<product>/` or the product's `raw/docs/<product>/llms.txt`.
5. For any API endpoint, grep `raw/api/endpoints.tsv`; for full schemas use jq on `raw/api/openapi.json` (gitignored, run `python3 scripts/fetch-api.py` if missing).
6. Everything that moves (prices, limits, beta/GA status, model lists) is a dated snapshot; re-check the live docs (append `index.md` to any docs URL for Markdown) or the Cloudflare docs MCP before relying on it in production.
7. When a session learns something new about Cloudflare, write it back to this repository and commit it.

## Where to look

| Question | File |
| --- | --- |
| Which page covers what; sidebar with page counts | `navigation.md` |
| Agent setup, MCP servers, skills, cf CLI, Wrangler, Terraform, Pulumi, SDKs, fundamentals | `platform-and-tooling.md` |
| Cloudflare REST API: auth, scoping, resources, endpoint lookup | `api-reference.md` |
| Workers, Pages, Containers, Durable Objects, Queues, Workflows, Browser Run, Email | `build/01-compute.md` |
| Workers AI, models, AI Gateway, Agents SDK, x402 tools, Wallets, Sandboxes, Vectorize, AI Search | `build/02-ai.md` |
| R2, Basin, K2, D1, KV, Hyperdrive, Artifacts, Secrets Store | `build/03-storage-database.md` |
| Images, Stream, Realtime, MoQ | `build/04-media.md` |
| WAF, DDoS, SSL, Bots, API Shield, Page Shield, Turnstile | `protect-connect/01-application-security.md` |
| Cloudflare One / Zero Trust (Access, Gateway, Tunnel connectors) | `protect-connect/02-cloudflare-one.md` |
| DNS, Registrar, 1.1.1.1, Email Routing, DMARC, Web3 gateways | `protect-connect/03-domains-dns.md` |
| Tunnel, Mesh, Magic Transit/WAN, Spectrum, BYOIP | `protect-connect/04-networking.md` |
| Monetization Gateway, x402, stablecoin payments | `protect-connect/05-monetize.md` |
| Cache, Speed, Load Balancing, Waiting Room, Argo, Zaraz | `protect-connect/06-delivery-performance.md` |
| Observability, Analytics, Logs, Log Explorer, Health Checks, Notifications | `manage-observe.md` |
| Billing, Rules, Ruleset Engine, Randomness Beacon, Radar and other unlisted products | `other-products.md` |
| What changed recently, deprecations | `changelog.md` |
| Launching a dapp, launchpad or trading UI on Solana, Ethereum, Base or Robinhood Chain with Cloudflare | `web3-launch-playbook.md` |
| Platforms similar to Cloudflare, and what to scrape next | `alternatives.md` |
| What each cloudflare GitHub repo does | `github-repos.md` |
