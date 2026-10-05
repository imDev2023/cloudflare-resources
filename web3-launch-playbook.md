# Web3 launch playbook: using Cloudflare for Solana, Ethereum, Base and Robinhood Chain projects

Snapshot as of 2026-10-05, built from the developer docs mirrored that day under `raw/docs/`, the Cloudflare blog posts under `raw/blog/`, the press and third-party pages under `raw/external/`, the search captures under `raw/search/`, and the GitHub catalog under `raw/github/`.
Chain facts come from the owner's sibling knowledge bases and are linked, not copied.

## Summary

Cloudflare's only native blockchain access products are two Web3 gateways: an Ethereum Gateway (JSON-RPC over HTTP to Ethereum Mainnet and Sepolia, a fixed method allowlist, no subscriptions or filters) and a read-only IPFS Gateway, both a paid, usage-based add-on as of 2026-10-05.
There is no Cloudflare gateway, RPC or node service for Solana, Base or Robinhood Chain in any mirrored source, and Robinhood Chain is not mentioned anywhere in Cloudflare's material.
Cloudflare's newer Web3-adjacent products are about payments rather than chain access: the x402 tooling in the Agents SDK, the Monetization Gateway (closed beta, US sellers and buyers only, settling USDC on Base through Coinbase's facilitator), AI Gateway Machine Payments (beta), paying Cloudflare's own invoices in USDC on Base or Polygon, Cloudflare Wallets (handle reservation only, no funds yet), the announced but undocumented NET Dollar stablecoin, and the drand randomness beacon.
For a launch, Cloudflare's value is therefore the general developer platform and edge security wrapped around a third-party RPC provider: a static frontend on Workers, a key-hiding RPC proxy Worker, an API Worker with D1, KV, R2 and Hyperdrive, Durable Objects for live price fan-out, Queues and Workflows for launch pipelines, Cron Triggers for keepers, and Turnstile, rate limiting, bot controls, client-side security, DNSSEC and registrar lock against snipers, faucet abuse and wallet-drainer frontend attacks.
A small launch fits in the $5 Workers Paid plan plus tens of dollars of usage; the binding constraints are the Free plan's 100,000 requests a day and 10 ms CPU, the 6 simultaneous connections per invocation, outbound WebSockets that never hibernate, and the fact that Waiting Room and real Bot Management are Business and Enterprise features.
Keys that move user or treasury funds should never live in a Worker; the docs' only signing pattern is a hot-wallet private key stored as a Worker secret for x402 payments.

## Contents

1. [How the owner has used Cloudflare so far](#1-how-the-owner-has-used-cloudflare-so-far)
2. [What Cloudflare offers natively for Web3](#2-what-cloudflare-offers-natively-for-web3)
3. [What Cloudflare does not offer, chain by chain](#3-what-cloudflare-does-not-offer-chain-by-chain)
4. [Reference architecture for a launch](#4-reference-architecture-for-a-launch)
5. [Runtime compatibility for chain libraries and cryptography](#5-runtime-compatibility-for-chain-libraries-and-cryptography)
6. [Per-chain sections](#6-per-chain-sections)
7. [Costs for a small launch](#7-costs-for-a-small-launch)
8. [Risks and limits](#8-risks-and-limits)
9. [Next steps checklist](#9-next-steps-checklist)
10. [Gaps and contradictions](#10-gaps-and-contradictions)

Related files in this knowledge base: `build/03-storage-database.md`, `protect-connect/01-application-security.md`, `protect-connect/03-domains-dns.md`, `protect-connect/05-monetize.md`.

---

## 1. How the owner has used Cloudflare so far

This section is context from the owner's own projects, not from Cloudflare's docs.

- **Octopus (bonding-curve launchpad and DEX on Robinhood Chain testnet 46630).**
  Hosting was decided as Cloudflare Pages on 2026-08-10, chosen over Netlify, Vercel and GitHub Pages "on proxy request economics" (`/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/Uniswap-V3/.session-prompts/010-2026-08-10-cloudflare-pages-hosting.md`).
  It shipped on 2026-08-11 at `https://octopus-68a.pages.dev` by direct upload, with a Pages Function `frontend/functions/rpc.ts` serving `/rpc`, the upstream URL held as the runtime secret `RPC_UPSTREAM_URL`, and a generated `_headers` file carrying HSTS, CSP and six other security headers (`Uniswap-V3/docs/security-checklist.md`).
  The project measured that `_headers` does not reach Function responses, that the edge adds `Access-Control-Allow-Origin: *` to static assets but not to the Function, and that a real `eth_chainId` through `/rpc` returned `0xb626` in 300 ms.
  It refuses cross-site browser callers on `Sec-Fetch-Site` and records that "a proxy protects the key from theft, not the quota from use", leaving a Cloudflare rate-limiting rule on the path as the open lever.
  Its budget note: about 27 requests a minute per open token page against the Free plan's 100,000 a day, so about 60 tab-hours a day (`Uniswap-V3/.session-prompts/011-2026-08-11-commit-43-and-deploy.md`).
- **Robinhood Chain measurements from Workers egress.**
  The Robinhood Chain knowledge base records that the chain's public RPC returned HTTP 429 to 70 of 72 `eth_getLogs` requests from a deployed Worker on 2026-09-20, that a full-chain log scan "never completes inside 180 s from a deployed Worker", and that a Worker plus one Durable Object holding provider WebSockets is the owner's head-following probe (`/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/resources/robinhood-chain/32-explorer-and-data-apis.md`, `robinhood-chain/52-swap-throughput-and-head-following.md`).
- **Meteora tooling already leans on Cloudflare.**
  Meteora's `fun-launch` scaffold stores token images in Cloudflare R2 through `@aws-sdk/client-s3`, and Meteora publishes `MeteoraAg/cloudflare-kv-merkle-proof`, a Worker plus KV that serves Alpha Vault merkle proofs (`/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/jupiter-meteora/meteora/03-dev-dbc-vaults-launch.md`, `jupiter-meteora/github-repos.md`).
- **Current Solana project.**
  `jug-meteora` has not chosen a concept yet; the working recommendation is a Meteora DBC launch paired with either a launchpad on `fun-launch` or an AI trading agent, with a token page built from a TradingView chart, the Jupiter Plugin and a small cached candles backend (`/Volumes/Farhan/Work Folder/Dev/AI/jug-meteora/findings/README.md`, `findings/project-ideas.md`, `findings/trading-ui-integration.md`).

---

## 2. What Cloudflare offers natively for Web3

### 2.1 Status at a glance (as of 2026-10-05)

| Offering | What it is | Status | Who can use it | Chains named by the sources |
| --- | --- | --- | --- | --- |
| Ethereum Gateway | JSON-RPC over HTTP to Cloudflare-run Ethereum full and archive nodes, read and write | Paid add-on, usage-based billing | All plans | Ethereum Mainnet, Sepolia |
| IPFS Gateway | Read-only HTTP access to IPFS content (DNSLink or Universal Path) | Paid add-on, usage-based billing | All plans; Universal Path Enterprise only per the limits table | IPFS |
| x402 in the Agents SDK | `withX402`, `paidTool`, `withX402Client`, `x402-hono` middleware, an `x402-proxy` Worker template | Shipping in the `agents` package | Anyone | x402 networks listed: Base, Ethereum, Polygon, Optimism, Arbitrum, Avalanche, Solana, Aptos, Stellar, Sui |
| Machine Payments Protocol (MPP) | Alternative 402 protocol, backwards compatible with x402 | Documented guides with the `mppx` SDK | Anyone | Examples use Tempo testnet |
| Monetization Gateway | Edge rule engine that charges matching requests via x402 | Closed beta since 2026-09-30 | US-based sellers and buyers, eligibility checks | Settles USDC on Base (blog) |
| AI Gateway Machine Payments | Pay for `/ai/run` inference from a stablecoin wallet with `Payment-Method: x402` | Beta since 2026-09-30 | US-based customers with a card on file | Not named in docs |
| Stablecoin billing | Pay Cloudflare invoices in USDC through Stripe's `crypto.stripe.com` | Documented | Checkout payment method | USDC on Base and Polygon |
| Cloudflare Wallets and `cloudflare.pay` | Account Wallets and agent Virtual Wallets holding stablecoins | Handle reservation only; wallets "in the coming months" | One handle per account | Not named |
| NET Dollar | US dollar-backed stablecoin | Announced 2025-09-25 as "plans to introduce"; no developer docs | Not stated | Not named |
| drand randomness beacon | League of Entropy public randomness, served at `drand.cloudflare.com` | Production since 2020 per docs | Anyone | Not chain-specific |

### 2.2 Web3 gateways: how they work, plans, limits and pricing

- The gateways are "an add-on feature" that give HTTP access to IPFS and Ethereum "without having to worry about running infrastructure" (https://developers.cloudflare.com/web3/).
- Creating a gateway adds a proxied `CNAME` on a subdomain of your zone (`ethereum.cloudflare.com` for Ethereum, `ipfs.cloudflare.com` plus a DNSLink `TXT` record for IPFS), issues a certificate, and routes requests "to a Cloudflare Workers script that communicates with the underlying network" (https://developers.cloudflare.com/web3/about/, https://developers.cloudflare.com/web3/reference/gateway-dns-records/).
- These DNS records cannot be edited in Cloudflare DNS, and creating a gateway on a hostname with existing records overwrites them (https://developers.cloudflare.com/web3/reference/gateway-dns-records/).
- The API target values are exactly `ethereum`, `ipfs` and `ipfs_universal_path`; the OpenAPI schema `web3_target` enum contains nothing else (https://developers.cloudflare.com/web3/how-to/manage-gateways/, `raw/api/openapi.json`).
- Statuses are Active, Pending, Deleting and Error, and a stuck gateway is fixed with a Refresh (`PATCH` with an empty body) (https://developers.cloudflare.com/web3/reference/gateway-status/).
- Getting access requires subscribing in the dashboard and entering payment details: "Web3 gateways are a paid add-on" (https://developers.cloudflare.com/web3/get-started/, https://developers.cloudflare.com/web3/how-to/enable-gateways/).
- Cloudflare recommends a usage-based billing notification because the product bills by usage (https://developers.cloudflare.com/web3/get-started/).
- Enterprise customers can preview it as a non-contract service "free of metered usage fees, limits, and certain other restrictions" (https://developers.cloudflare.com/web3/).
- Because the hostname is proxied through your zone, WAF, rate limiting and other zone settings apply to gateway traffic (https://developers.cloudflare.com/web3/how-to/customize-cloudflare-settings/, https://blog.cloudflare.com/ea-web3-gateways/).
- For backend-only use, restrict the hostname with an Access policy and a service token (https://developers.cloudflare.com/web3/how-to/restrict-gateway-access/).

Limits and included usage, as of 2026-10-05 (https://developers.cloudflare.com/web3/reference/limits/):

| | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| Availability | Usage-based billing | Usage-based billing | Usage-based billing | Usage-based billing |
| Total gateways (each product) | 15 | 15 | 15 | Unlimited |
| Ethereum included usage | 500,000 HTTP requests | 500,000 HTTP requests | 500,000 HTTP requests | 1,000,000 HTTP requests |
| IPFS included usage | 50 GB data transfer | 50 GB | 50 GB | 100 GB |
| IPFS gateway types | DNSLink | DNSLink | DNSLink | DNSLink, Universal Gateway |
| IPFS file size limit | None | None | None | None |

The overage price is not in the mirrored docs; they point to the Web3 product page and the dashboard for pricing (https://developers.cloudflare.com/web3/reference/limits/).

### 2.3 Ethereum Gateway in detail

- **Networks.** Ethereum Mainnet (`/v1/mainnet`) and Sepolia (`/v1/sepolia`), nothing else (https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/).
  Rinkeby was deprecated, and Görli, which a 2022 blog announced, is no longer listed (https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/, https://blog.cloudflare.com/ethereum-merge-and-testnet-gateways/).
- **Transport.** Plain HTTP `POST` with a JSON-RPC body (https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/).
  No WebSocket endpoint, `eth_subscribe` or batch request support is documented.
- **Supported methods** (32): `web3_clientVersion`, `web3_sha3`, `net_version`, `net_listening`, `eth_syncing`, `eth_mining`, `eth_gasPrice`, `eth_feeHistory`, `eth_blockNumber`, `eth_chainId`, `eth_getBalance`, `eth_getStorageAt`, `eth_getTransactionCount`, `eth_getBlockTransactionCountByHash`, `eth_getBlockTransactionCountByNumber`, `eth_getUncleCountByBlockHash`, `eth_getUncleCountByBlockNumber`, `eth_getCode`, `eth_sendRawTransaction`, `eth_call`, `eth_estimateGas`, `eth_getBlockByHash`, `eth_getBlockByNumber`, `eth_getTransactionByHash`, `eth_getTransactionByBlockHashAndIndex`, `eth_getTransactionByBlockNumberAndIndex`, `eth_getTransactionReceipt`, `eth_getUncleByBlockHashAndIndex`, `eth_getUncleByBlockNumberAndIndex`, `eth_getLogs`, `eth_getWork`, `eth_getProof`, plus the trace method `trace_filter` (https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-api-methods/).
- **Unsupported methods** return `403`: `net_peerCount`, `eth_protocolVersion`, `eth_coinbase`, `eth_hashrate`, `eth_accounts`, `eth_sign`, `eth_sendTransaction`, the `eth_compile*` family, every filter method (`eth_newFilter`, `eth_newBlockFilter`, `eth_newPendingTransactionFilter`, `eth_uninstallFilter`, `eth_getFilterChanges`, `eth_getFilterLogs`), `eth_submitWork` and `eth_submitHashrate` (same page).
- **Per-method caps.** `eth_getLogs` max block range 800, `eth_feeHistory` max block count 10, `trace_filter` max 800 blocks and `count` max 200 (same page).
- **Archive behaviour.** Cloudflare runs full and archive nodes; archive nodes serve `eth_getBalance`, `eth_getCode`, `eth_getTransactionCount`, `eth_getStorageAt` and `eth_call` when the block is older than the latest 128 or is `earliest` (https://developers.cloudflare.com/web3/ethereum-gateway/concepts/node-types/).
- **Writes.** Only `eth_sendRawTransaction`; you sign elsewhere and the gateway places the transaction in a Cloudflare node's mempool (https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/, https://developers.cloudflare.com/web3/about/).
  The About page says writes are "only available for gateways to EVM-based chains, such as Ethereum", but Ethereum is the only EVM chain offered.

### 2.4 IPFS Gateway in detail

- Read-only: "Cloudflare's IPFS Gateway is currently limited to read-only access", so pinning and uploads happen elsewhere (https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/).
- A DNSLink gateway is restricted to one CID or IPNS name, defaulting to `/ipns/onboarding.ipfs.cloudflare.com` until you set your own; a Universal Path gateway serves any CID and has a CID and path blocklist (https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/, https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/).
- Cloudflare's public IPFS hostnames `cloudflare-ipfs.com` and `cf-ipfs.com` were redirected to `ipfs.io` and `dweb.link` from 2024-05-14 and stopped connecting to IPFS on 2024-08-14 (https://blog.cloudflare.com/cloudflares-public-ipfs-gateways-and-supporting-interplanetary-shipyard/).
- Launch relevance (recommendation, not documented): a DNSLink gateway pointed at a CID gives a content-addressed, immutable mirror of a frontend release that users can cross-check against the hosted site; it does not replace a normal frontend because it is read-only and every release needs a new CID and DNSLink update.
  The docs recommend relative links for IPFS-hosted sites and list `ipfs-deploy` and `dnslink-cloudflare` for automating DNSLink updates (https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/, https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/).

### 2.5 x402 and the Agents SDK payments tools

- x402 "is a payment standard created by Coinbase" that "uses on-chain stablecoin payments (USDC on Base, Ethereum, Solana, and other networks)", "governed by Coinbase and Cloudflare, two of the founding members of the x402 Foundation" (https://developers.cloudflare.com/agents/tools/payments/).
- Flow: `402` with a Base64 `PAYMENT-REQUIRED` header, client retries with `PAYMENT-SIGNATURE`, server verifies and settles, optionally through a facilitator, and returns `PAYMENT-RESPONSE` (https://developers.cloudflare.com/agents/tools/payments/x402/).
- The facilitator exposes `POST /verify` and `POST /settle`, "does not hold funds", and `https://x402.org/facilitator`, operated by Coinbase, "is used in all Cloudflare examples" (same page).
- Schemes: `exact` on EVM, Solana, Aptos, Stellar, Hedera and Sui; `upto` on EVM only (same page).
- SDK packages listed: `x402-hono`, `@x402/fetch`, `@x402/evm`, and `agents/x402` (same page).
  No Solana scheme package appears in Cloudflare's docs, so Cloudflare's own integrations are EVM-only as documented, even though the protocol lists Solana.
- Agents SDK v0.4.0 (2026-02-09) moved to `@x402/core` and `@x402/evm` v2, accepts CAIP-2 network ids such as `eip155:84532`, and accepts both `PAYMENT-SIGNATURE` and legacy `X-PAYMENT` headers (https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/).
- Ways to charge: the `x402-proxy` Worker template in front of any HTTP origin (routes and prices in `wrangler.jsonc` `vars`), Hono middleware inside a Worker, or `paidTool` on an MCP server (https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/, https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/).
- The proxy template can charge only low bot-score traffic with `bot_score_threshold`, which needs Bot Management (same page).
- Ways to pay: `withX402Client` around an MCP connection inside an Agent, with a `privateKeyToAccount` signer from `viem/accounts` and the key stored with `wrangler secret put` (https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/).
- Test on `base-sepolia` with test USDC from the Circle faucet (same pages).
- MPP is the second protocol the SDK supports; it adds `WWW-Authenticate: Payment` and `Authorization: Payment`, supports cards via Stripe and stablecoins, and "MPP clients can consume existing x402 services without modification" (https://developers.cloudflare.com/agents/tools/payments/mpp/).

The docs' own x402 Worker pattern, verbatim except for the price and network values (https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/):

```ts
import { Hono } from "hono";
import { paymentMiddleware } from "x402-hono";

const app = new Hono<{ Bindings: Env }>();

app.use(
	paymentMiddleware(
		"0xYourWalletAddress" as `0x${string}`,
		{
			"/premium": {
				price: "$0.10",
				network: "base-sepolia",
				config: { description: "Premium content" },
			},
		},
		{ url: "https://x402.org/facilitator" },
	),
);

app.get("/premium", (c) => c.json({ message: "Thanks for paying!" }));

export default app;
```

### 2.6 Monetization Gateway

- Closed beta since 2026-09-30; request access in the dashboard (https://developers.cloudflare.com/monetization-gateway/, https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/).
- It applies x402 version 2 requirements to matching traffic on a proxied zone; rules match URL, headers, query, cookie, IP, country and more, with body matching Enterprise only (https://developers.cloudflare.com/monetization-gateway/configuration/rules/).
- Prices are in atomic units of $0.000001; minimum $0.001, maximum $100; schemes `exact` (fixed) and `upto` (variable, origin reports `PAYMENT-SETTLEMENT`) (same page, https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/).
- The origin receives a `PAYMENT-CONTEXT` JWT signed with Ed25519, to be verified against the pinned JWKS at `https://payments.cloudflare.com/certs`, with `jose` recommended for Workers (https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/).
- Audience can be Everyone or Verified Bots identified by BotBase (https://developers.cloudflare.com/monetization-gateway/get-started/).
- Eligibility: "Buyers and sellers must be based in the United States"; seller account older than 60 days with a card on file and a verified email; zone proxied and older than 30 days; Service-Specific Terms accepted (https://developers.cloudflare.com/monetization-gateway/eligibility/).
- Settlement "through Coinbase's x402 Facilitator", and "Payments settle on the Base blockchain using USDC" (https://blog.cloudflare.com/monetization-gateway-beta/).
- Production users named in the beta post: Cloudflare AI Gateway, Ceramic.ai, Stocktwits and API2PDF (same post).
- Fees for sellers are not documented.

### 2.7 AI Gateway Machine Payments

- Beta since 2026-09-30: pay for `POST /ai/run` inference on four open models (`z-ai/glm-4.7-flash`, `google/gemma-4-26b-a4b-it`, `openai/gpt-oss-20b`, `alibaba/qwen3.8-27b`) from a stablecoin wallet by sending the Cloudflare-specific header `Payment-Method: x402` (https://developers.cloudflare.com/ai-gateway/features/machine-payments/).
- Most models use the `upto` scheme; requires a Cloudflare API token, a US base and a card on file (same page, https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/).

### 2.8 Paying Cloudflare in stablecoins

- Checkout offers **Crypto** next to card, Apple Pay and Google Pay; you connect a wallet on Stripe's `crypto.stripe.com` and sign a one-time permit that also covers recurring and usage-based charges for Workers, R2 and Stream (https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/).
- Supported: USDC on Base and Polygon; MetaMask, Phantom, Coinbase Wallet and 400+ WalletConnect wallets; invoices in USD; no chargebacks; refunds in USDC "within minutes" (same page).
- Wallets are screened before the transaction, and a flagged wallet fails the payment; a card on file is the automatic fallback (same page).
- Cloudflare adds no markup; the wallet pays gas (same page).

### 2.9 Cloudflare Wallets and cloudflare.pay

- As of 2026-10-05 only handle reservation exists: one free handle per account at `cloudflare.pay`, publishing `HANDLE.cloudflare.pay`, which "does not yet let you send, receive, or hold funds" (https://developers.cloudflare.com/wallets/, https://developers.cloudflare.com/wallets/faq/).
- Planned: Account Wallets for humans and API-key-driven Virtual Wallets for agents with allowances, allow lists and maximum transaction sizes; "at first" they will "send, receive, and hold stablecoins" (https://blog.cloudflare.com/wallets/).
- Full access including on-ramp, off-ramp and Virtual Wallets "will be available in the coming months" from the 2026-08-04 announcement (`raw/external/www.cloudflare.com_press_press-releases_2026_cloudflare-gives-ai-agents-an-identity-and-a-wallet.md`).
- No chain, token or custody model is named in any source, so Wallets cannot yet be planned as a signer or treasury for a launch.

### 2.10 NET Dollar

- On 2025-09-25 Cloudflare "announced plans to introduce NET Dollar, a new U.S. dollar-backed stablecoin" for agentic payments, pointing to `netdollar.cloudflare.com` (`raw/external/www.cloudflare.com_press_press-releases_2025_cloudflare-introduces-net-dollar-to-support-a-new-business-model-for-the-ai-driven-internet.md`).
- It has no page in the developer docs mirror, and no source names its chain, issuer, launch date or availability.
- The Monetization Gateway announcement names USDC and Open USD as example stablecoins, not NET Dollar (https://blog.cloudflare.com/monetization-gateway/).

### 2.11 drand randomness beacon and LavaRand

- drand produces "publicly verifiable, unbiased, unpredictable random values at fixed intervals" with threshold BLS signatures on BLS12-381, and Cloudflare documents it under Randomness Beacon (https://developers.cloudflare.com/randomness-beacon/, https://developers.cloudflare.com/randomness-beacon/cryptographic-background/randomness-generation/).
- The docs defer to `drand.love` for current user and operator documentation (https://developers.cloudflare.com/randomness-beacon/user-guide/).
- Cloudflare serves League of Entropy beacons at `drand.cloudflare.com`; the `quicknet` beacon emits every 3 seconds with unchained randomness, so the message for round `r` is just `r`; `https://drand.cloudflare.com/chains` lists beacons; 18 organisations participated as of the 2024 post (https://blog.cloudflare.com/harnessing-office-chaos/).
- Private randomness for keys and IDs: `crypto.getRandomValues` in a Worker draws on entropy that LavaRand feeds (same post, https://developers.cloudflare.com/workers/runtime-apis/web-crypto/).
- Launch use (recommendation): drand rounds suit off-chain fairness that anyone can re-verify, such as allowlist lotteries or airdrop raffles committed to a future round number.
  On-chain verification of a drand signature needs a BLS12-381 verifier contract or program, which no Cloudflare source discusses, and BLS12-381 is not in the Workers Web Crypto table.

---

## 3. What Cloudflare does not offer, chain by chain

| Chain | Cloudflare gateway or RPC? | Where the chain does appear in Cloudflare sources |
| --- | --- | --- |
| Solana | **No.** The Web3 product covers only IPFS and Ethereum, and the API target enum has no Solana value. | Only as an x402 network ("USDC on Base, Ethereum, Solana"; `exact` scheme on Solana) in https://developers.cloudflare.com/agents/tools/payments/ and https://developers.cloudflare.com/agents/tools/payments/x402/, and as a name in a 2022 blog list of "next generation" chains (https://blog.cloudflare.com/next-gen-web3-network/). The word appears in no other developer doc. |
| Ethereum | **Yes:** the Ethereum Gateway, Mainnet and Sepolia only, HTTP JSON-RPC only. | Web3 docs; x402 network list. |
| Base | **No.** No gateway, RPC or node service. | As a payment network: x402 examples default to `base` and `base-sepolia`; Monetization Gateway settles USDC on Base; stablecoin billing accepts USDC on Base. |
| Robinhood Chain | **No.** | Not mentioned in any mirrored Cloudflare doc, blog, press page or search capture (searched for "robinhood" on 2026-10-05). The only link is the reverse one: Robinhood Chain's Blockscout explorer sits behind Cloudflare's challenge (`resources/robinhood-chain/32-explorer-and-data-apis.md`). |
| Polygon, Optimism, Arbitrum, Avalanche | No gateway. | x402 networks; Polygon is also a stablecoin billing network. |

Other things Cloudflare does not offer, per the sources:

- No WebSocket or subscription RPC for any chain; the Ethereum Gateway rejects every filter method.
- No transaction signing service or KMS for blockchain keys: Secrets Store stores secrets and the Agents examples sign with a key held as a Worker secret (https://developers.cloudflare.com/secrets-store/, https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/).
- No indexer, subgraph or log-archive service for any chain.
- No IPFS pinning or upload; the gateway is read-only.
- No public Cloudflare-run Ethereum or IPFS endpoint you can rely on; see the contradictions section about `cloudflare-eth.com`.

---

## 4. Reference architecture for a launch

Everything in this section is a recommendation assembled from documented building blocks; each building block cites its doc, but the composition is not something Cloudflare documents as a Web3 pattern.

### 4.1 Shape

```
browser (wallet signs locally)
   |
   |  https://app.example.com          (zone on Cloudflare: DNSSEC, WAF, rate limits, Turnstile, client-side security)
   v
+---------------------------- one Worker with static assets ---------------------------+
|  /*            -> static SPA assets (free, unlimited)                                  |
|  /rpc          -> RPC proxy: method allowlist, rate limit, secret upstream URL         |
|  /ws/*         -> Durable Object rooms (hibernatable WebSockets) for prices and trades |
|  /api/*        -> API: D1 (launches, users), KV (cached quotes, config), R2 (images)   |
|                   Hyperdrive (existing Postgres indexer), Turnstile siteverify         |
+----------------------------------------------------------------------------------------+
        |                 |                     |                       |
        v                 v                     v                       v
  Helius / Alchemy /   FeedHub Durable       Queues + Workflows      Cron Triggers
  QuickNode / dRPC /   Object holding the    (tx confirmation,       (keepers, cache
  public RPC           upstream WebSocket    launch steps, retries)  refresh, health)
        |
  self-hosted node or indexer  <- Cloudflare Tunnel + Workers VPC, admin UI behind Access
```

### 4.2 Frontend on Workers static assets (or Pages)

- Pages docs now say: "Workers supports most Pages use cases and offers a broader feature set ... It is Cloudflare's primary platform for building applications. Start new projects with Workers." (https://developers.cloudflare.com/pages/).
  Octopus is on Pages; a new project should start on Workers static assets, and a move can follow the Pages migration guide (https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/).
- Requests to static assets are free and unlimited; requests that run the Worker are billed as Workers (https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/).
- `assets.run_worker_first` takes up to 100 patterns such as `["/api/*", "!/api/docs/*"]`, and with `not_found_handling: "single-page-application"` the rest is served as the SPA (https://developers.cloudflare.com/workers/static-assets/routing/).
  On the Free plan, every request matching `run_worker_first` invokes the Worker and counts against the 100,000 a day (https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/).
- Limits: 20,000 asset files per version on Free and 100,000 on Paid, 25 MiB per file (https://developers.cloudflare.com/workers/platform/limits/).
- `_headers` sets security headers on asset responses only: "Custom headers defined in the `_headers` file are not applied to responses generated by your Worker code" (https://developers.cloudflare.com/workers/static-assets/headers/), matching what Octopus measured on Pages.
  Set headers in code on `/rpc` and `/api/*` replies.
- Next.js (the `fun-launch` scaffold is Next.js 15): Cloudflare recommends `vinext` for new Next.js apps, described as for "an existing Next.js 16 app" and in beta, and keeps OpenNext for existing apps, where Node.js middleware from Next.js 15.2 "is not yet supported" (https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/, https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/).

### 4.3 RPC key-hiding proxy Worker

Documented facts the design rests on:

- Helius publishes a one-click Cloudflare Worker that proxies JSON-RPC and WebSockets to Helius so the API key stays server-side, stored as an encrypted variable `HELIUS_API_KEY` (`raw/external/github.com_helius-labs_helius-rpc-proxy.md`).
  Its README suggests narrowing `CORS_ALLOW_ORIGIN` and allowlisting Cloudflare's IP ranges in Helius (same file).
  Its latest commit fixed WebSocket subscriptions being dropped by a pre-connect buffer cap of 10 messages while the upstream socket opens (same file).
- Helius lists the proxy as its first key-protection method; its alternative "Secure URL" is paid-only and limited to 5 requests per second per IP (`raw/external/www.helius.dev_docs_rpc_protect-your-keys.md`).
- Subrequests are not billed; the Worker is billed per inbound request and CPU (https://developers.cloudflare.com/workers/platform/pricing/).
- The Rate Limiting binding gives per-key limits inside the Worker with a 10 or 60 second period; counters are per Cloudflare location and "intentionally designed to not be used as an accurate accounting system" (https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/).

Recommendations, from those facts and Octopus's lessons:

- Allowlist methods instead of forwarding everything, so the proxy cannot be used for expensive archive or trace calls you never make.
- Refuse cross-site browser callers on `Sec-Fetch-Site` as Octopus does, and still put a rate limit on the path, because a server can call the proxy directly.
- Keep the upstream URL in a secret (`wrangler secret put`) or Secrets Store, never in `vars`, and never under a framework's public prefix such as `VITE_`.
- Give the wallet extension the chain's public RPC, not your proxy, as Octopus's `walletRpcUrlsFor` test enforces.

Sketch in the docs' Worker style:

```ts
// src/rpc.ts - JSON-RPC proxy for /rpc (Solana or EVM upstream)
const ALLOWED = new Set([
	// EVM example; replace with getAccountInfo, getLatestBlockhash, sendTransaction ... for Solana
	"eth_chainId", "eth_blockNumber", "eth_call", "eth_estimateGas", "eth_gasPrice",
	"eth_getBalance", "eth_getTransactionReceipt", "eth_sendRawTransaction", "eth_getLogs",
]);

export async function handleRpc(request: Request, env: Env): Promise<Response> {
	if (request.method !== "POST") return new Response(null, { status: 405, headers: { allow: "POST" } });

	const site = request.headers.get("Sec-Fetch-Site");
	if (site && site !== "same-origin") return new Response("cross-site refused", { status: 403 });

	const ip = request.headers.get("CF-Connecting-IP") ?? "unknown";
	const { success } = await env.RPC_LIMITER.limit({ key: ip });
	if (!success) return new Response("rate limited", { status: 429 });

	const body = await request.text();
	let calls: Array<{ method?: string }>;
	try {
		const parsed = JSON.parse(body);
		calls = Array.isArray(parsed) ? parsed : [parsed];
	} catch {
		return new Response("bad json", { status: 400 });
	}
	if (calls.length > 20 || calls.some((c) => !c.method || !ALLOWED.has(c.method))) {
		return new Response("method not allowed", { status: 403 });
	}

	// RPC_UPSTREAM_URL is a secret: `npx wrangler secret put RPC_UPSTREAM_URL`
	const upstream = await fetch(env.RPC_UPSTREAM_URL, {
		method: "POST",
		headers: { "content-type": "application/json" },
		body,
	});
	return new Response(upstream.body, {
		status: upstream.status,
		headers: { "content-type": "application/json", "cache-control": "no-store" },
	});
}
```

For Solana WebSocket subscriptions through the proxy, the docs' two halves are a `WebSocketPair` returned to the browser and an outbound socket opened with `fetch(url, { headers: { Upgrade: "websocket" } })` then `resp.webSocket.accept()`, optionally with `{ allowHalfOpen: true }` "for WebSocket proxying" (https://developers.cloudflare.com/workers/examples/websockets/).
Outbound WebSockets count toward the 6 connections per invocation that may wait for headers at once (https://developers.cloudflare.com/workers/platform/limits/).
Per-client socket proxying gives each browser its own upstream subscription, which the provider meters; section 4.5 shows the fan-out alternative.

### 4.4 API Worker with D1, KV, R2 and Hyperdrive

| Store | Fits | Documented constraint that matters for a launch |
| --- | --- | --- |
| D1 | Launch records, users, referral codes, allowlists | Free: 5M rows read and 100k rows written per day, 5 GB; Paid includes 25B reads, 50M writes, 5 GB (https://developers.cloudflare.com/workers/platform/pricing/) |
| KV | Cached quotes, token metadata, feature flags, merkle proofs (Meteora's own pattern) | Eventually consistent, "up to 60 seconds or more" to propagate; 1 write per second per key; Free 1,000 writes a day (https://developers.cloudflare.com/kv/concepts/how-kv-works/, https://developers.cloudflare.com/kv/platform/limits/) |
| R2 | Token images, metadata JSON, frontend release archives | No egress charge; free tier 10 GB-month, 1M Class A, 10M Class B per month (https://developers.cloudflare.com/r2/pricing/) |
| Hyperdrive | An existing Postgres or MySQL indexer database, for example a self-hosted graph-node Postgres | Free 100,000 queries a day, Paid unlimited (https://developers.cloudflare.com/hyperdrive/, https://developers.cloudflare.com/workers/platform/pricing/) |
| Analytics Engine | Per-request metrics such as RPC method mix and swap counts | Free 100k data points a day, Paid 10M a month included (https://developers.cloudflare.com/analytics/analytics-engine/pricing/) |

Recommendation: never use KV for anything a user's money depends on in the next minute, such as a bonding-curve price or a "sold out" flag, because of the 60-second propagation; read those from chain or a Durable Object.

### 4.5 Durable Objects for live price feeds and WebSockets

Documented behaviour:

- A Durable Object that accepts client sockets with `this.ctx.acceptWebSocket(server)` can hibernate; clients stay connected and duration charges stop while it sleeps (https://developers.cloudflare.com/durable-objects/best-practices/websockets/).
- "Hibernation is only supported when a Durable Object acts as a WebSocket server. Outgoing WebSockets do not hibernate," and an open outbound socket "prevents eviction for up to 15 minutes" (same page).
- Alarms, incoming requests, `setTimeout` and `setInterval` also prevent hibernation (same page).
- Billing: each WebSocket connect is a request, incoming WebSocket messages are billed at 20:1, outgoing messages are free, and duration is billed on 128 MB while the object is active (https://developers.cloudflare.com/workers/platform/pricing/).
- One object has a soft limit of 1,000 requests per second and 10 GB of storage (https://developers.cloudflare.com/durable-objects/platform/limits/).
- Free plan accounts can use only SQLite-backed Durable Objects (https://developers.cloudflare.com/workers/platform/pricing/).

Recommended pattern:

- One `FeedHub` object per chain holds the single upstream provider WebSocket (Helius `logsSubscribe`, Alchemy or dRPC `eth_subscribe` logs) and stays awake; at 128 MB for 30 days that is 0.125 GB x 2,592,000 s = 324,000 GB-s, inside both the Paid plan's 400,000 GB-s a month and the Free plan's 13,000 GB-s a day (10,800 GB-s per day for one object).
- One `TokenRoom` object per token or pool accepts browser sockets with the Hibernation API and receives updates from `FeedHub` by RPC, so thousands of viewers cost one upstream subscription.
- Batch updates every 50 to 100 ms, as the docs recommend for high-frequency data (https://developers.cloudflare.com/durable-objects/best-practices/websockets/).
- Persist the last seen slot or block in the object's SQLite so a reconnect can backfill the gap with one bounded `getLogs` or `getSignaturesForAddress` call.

Sketch using the docs' hibernation API:

```ts
import { DurableObject } from "cloudflare:workers";

export class TokenRoom extends DurableObject<Env> {
	async fetch(request: Request): Promise<Response> {
		const webSocketPair = new WebSocketPair();
		const [client, server] = Object.values(webSocketPair);
		this.ctx.acceptWebSocket(server); // hibernatable, unlike server.accept()
		return new Response(null, { status: 101, webSocket: client });
	}

	// Called by FeedHub over Durable Object RPC with a batch of trades or a price tick
	async publish(update: string): Promise<void> {
		for (const ws of this.ctx.getWebSockets()) ws.send(update); // outgoing messages are not billed
	}

	async webSocketMessage(ws: WebSocket, message: string | ArrayBuffer) {
		// Read-only feed: ignore client messages, or handle a "resync from block N" request
	}
}
```

### 4.6 Queues and Workflows for transaction pipelines and launch steps

- Queues deliver "at least once", with batching, retries and a dead-letter queue configured on the consumer (https://developers.cloudflare.com/queues/reference/delivery-guarantees/, https://developers.cloudflare.com/queues/configuration/configure-queues/).
  Free: 10,000 operations a day and 24-hour retention; Paid: 1M operations a month included, retention up to 14 days (https://developers.cloudflare.com/workers/platform/pricing/).
- Workflows persist each `step.do` result, retry steps with configured backoff, `step.sleep` up to 365 days, and `step.waitForEvent` until another Worker calls `instance.sendEvent` (https://developers.cloudflare.com/workflows/get-started/guide/, https://developers.cloudflare.com/workflows/build/events-and-parameters/, https://developers.cloudflare.com/workflows/reference/limits/).
  Free: 1,024 steps per Workflow, 3,000 steps a day, 100 concurrent instances; Paid: 10,000 steps per Workflow by default, 500,000 steps a month included, 50,000 concurrent instances (same pages).

Recommended uses:

- **Transaction confirmation.** The API Worker enqueues `{ signature or txHash, chain, launchId }` after the browser submits a signed transaction; a consumer polls the receipt or signature status and writes the outcome to D1.
  Make the consumer idempotent on the transaction id because delivery is at least once.
- **Launch Workflow.** Steps such as: validate parameters and Turnstile result, upload image and metadata to R2, wait for the creator's signed create transaction (`step.waitForEvent`), confirm it, register the pool in D1, warm caches, and announce.
  Workflows never hold the creator's key; the event carries a transaction the browser already signed and sent.

```ts
import { WorkflowEntrypoint, WorkflowEvent, WorkflowStep } from "cloudflare:workers";

type LaunchParams = { launchId: string; mint?: string };

export class LaunchWorkflow extends WorkflowEntrypoint<Env, LaunchParams> {
	async run(event: WorkflowEvent<LaunchParams>, step: WorkflowStep) {
		const meta = await step.do("store metadata", async () => {
			// put image and JSON into R2, return the public URL
			return { uri: `https://assets.example.com/${event.payload.launchId}.json` };
		});

		const signed = await step.waitForEvent<{ txId: string }>("creator signed create tx", {
			type: "create-tx-sent",
			timeout: "1 hour",
		});

		await step.do(
			"confirm on chain",
			{ retries: { limit: 10, delay: "5 seconds", backoff: "exponential" } },
			async () => {
				// call the RPC proxy upstream; throw until finalized so the step retries
			},
		);

		await step.do("register launch", async () => {
			await this.env.DB.prepare("UPDATE launches SET status = 'live', tx = ?1, uri = ?2 WHERE id = ?3")
				.bind(signed.payload.txId, meta.uri, event.payload.launchId)
				.run();
		});
	}
}
```

### 4.7 Cron Triggers for keepers

- Cron Triggers run `scheduled(controller, env, ctx)` on standard cron expressions (https://developers.cloudflare.com/workers/configuration/cron-triggers/).
- Limits: 5 Cron Triggers per account on Free, 250 on Paid; CPU 10 ms on Free, 30 seconds for intervals under an hour and 15 minutes at hourly or longer on Paid (https://developers.cloudflare.com/workers/platform/limits/).
- Fits: refreshing cached quotes and token lists, checking provider health, sweeping stuck launches, publishing stats.
- A keeper that must send transactions needs a signing key; see section 4.13 before putting one in a Worker.
- For sub-minute cadence inside one object, Durable Object alarms are the documented alternative (https://developers.cloudflare.com/durable-objects/api/alarms/).
- The Agents SDK also schedules with `this.schedule("0 9 * * *", "dailyDigest")` (https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/).

### 4.8 Abuse controls: Turnstile, rate limiting and bots (snipers, faucets, spam launches)

| Control | Plan availability (as of 2026-10-05) | Launch use |
| --- | --- | --- |
| Turnstile | Free plan: up to 20 widgets, unlimited challenges, 10 hostnames per widget (https://developers.cloudflare.com/turnstile/plans/) | Gate faucet claims, allowlist sign-ups, "create token" and API key issuance; tokens are single-use and expire after 300 s, and the server must call Siteverify (https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) |
| WAF rate limiting rules | Free: 1 rule, Path field, 10 s period, IP counting; Pro: 2 rules, up to 1 min; Business: 5 rules, up to 10 min, method and user agent fields; Enterprise: 100 rules (https://developers.cloudflare.com/waf/rate-limiting-rules/) | One Free rule on `/rpc` and the faucet path is the cheapest platform-level cap |
| Rate Limiting binding in the Worker | Workers binding, 10 or 60 s periods, per location (https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) | Per wallet, per IP or per API key limits inside the API; not an accounting system |
| Bot Fight Mode | "All Free customers"; challenges simple bots; "cannot bypass or skip Bot Fight Mode using WAF custom rules or Page Rules"; "may challenge API or mobile app traffic" (https://developers.cloudflare.com/bots/plans/free/, https://developers.cloudflare.com/bots/get-started/bot-fight-mode/) | Risky on a zone that serves `/rpc` to wallets and bots you want; test before launch |
| Super Bot Fight Mode | Pro and Business (https://developers.cloudflare.com/bots/plans/pro/, https://developers.cloudflare.com/bots/plans/biz-and-ent/) | Allow, block or challenge by bot class across the zone |
| Bot Management | Enterprise add-on; bot score, JA3/JA4, per-path control (https://developers.cloudflare.com/bots/plans/bm-subscription/) | Needed for score-based rules and the x402 proxy's `bot_score_threshold` |
| DDoS protection and the Free Managed Ruleset | All plans (https://developers.cloudflare.com/ddos-protection/, https://developers.cloudflare.com/waf/managed-rules/) | Baseline |

Recommendations:

- On-chain sniping cannot be stopped at the edge, because snipers call the program or contract directly through any RPC.
  Use the launch platform's own anti-snipe tools for that, such as Meteora's fee schedulers or Jupiter Studio's anti-sniper fee (`jug-meteora/findings/launch-options.md`), and use Cloudflare only to protect your website, API, faucet and allowlist flows.
- Validate Turnstile tokens server-side with the docs' pattern and bind the check to the wallet address you are about to credit.

```ts
// Turnstile Siteverify, from the docs' JSON example
async function validateTurnstile(token: string, remoteip: string, env: Env) {
	const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ secret: env.TURNSTILE_SECRET, response: token, remoteip }),
	});
	return (await response.json()) as { success: boolean; "error-codes"?: string[] };
}
```

### 4.9 Waiting Room for launch-day spikes

- Waiting Room is not available on Free or Pro; Business includes one basic room with FIFO queueing, and Enterprise can buy advanced rooms with Random, Reject and Passthrough methods and a JSON-friendly response (https://developers.cloudflare.com/waiting-room/plans/).
- Recommendation: a Waiting Room only queues browsers on your hostname; it does not slow on-chain buys, so it is useful for an allowlist or mint page with server-side gating, not for a public bonding curve.
  On Free or Pro, a static "launch at block or slot N" page plus Turnstile on the server action is the documented-components alternative.

### 4.10 Frontend integrity against wallet-drainer attacks

A drainer usually arrives by changing what the user's browser loads: a hijacked domain or DNS record, a compromised third-party script, or a tampered deployment.
Documented controls:

- **DNSSEC** is free to all Cloudflare customers and one click on Cloudflare Registrar (https://developers.cloudflare.com/registrar/).
- **Registrar lock and registry lock.** Cloudflare Registrar keeps domains locked and you must explicitly unlock to get a transfer code; anyone with super-admin or admin on the zone can unlock, "Be careful who you give these" roles (https://developers.cloudflare.com/registrar/account-options/transfer-out-from-cloudflare/).
  Custom Domain Protection, for Enterprise and "high-profile domains", applies registry lock and offers "no interface ... to remove the possibility of domain hijack through a compromised account" (https://developers.cloudflare.com/registrar/custom-domain-protection/).
  Registrar sells at cost with no markup (https://developers.cloudflare.com/registrar/faq/).
- **Client-side security** (formerly Page Shield) is on all plans with script monitoring; Business adds connection and cookie monitoring, page attribution and new-resource and new-domain alerts; malicious script, code change and malicious connection detection and content security rules need Client-Side Security Advanced (https://developers.cloudflare.com/client-side-security/).
- **CSP and other headers** via `_headers` on assets and in code on Worker responses (section 4.2); Octopus's eight-header set is a working example.
- **Account security**: two-factor authentication on the Cloudflare account (https://developers.cloudflare.com/fundamentals/user-profiles/2fa/), and scoped API tokens for CI.

Recommendations: keep all JavaScript first-party and content-hashed so a strict `script-src 'self'` holds; alert on any new script or connection domain; never let a CI token have Registrar or DNS edit rights; publish the frontend's expected script hashes or an IPFS CID so users can cross-check.

### 4.11 Access, Tunnel and Workers VPC for admin panels and self-hosted nodes or indexers

- Cloudflare Tunnel connects a server with an outbound-only `cloudflared` connection, "no public IPs required", on all plans (https://developers.cloudflare.com/tunnel/).
- Access policies and service tokens put an admin UI or an internal API behind identity; "Access mTLS ... is not included in the Free plan. Free customers can use service tokens" (https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/, https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).
- Workers VPC lets a Worker call a private host through a Tunnel with a `vpc_services` binding, on Free and Paid plans (https://developers.cloudflare.com/workers-vpc/, https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/).

Recommended uses: a self-hosted Solana or EVM node, a graph-node or custom indexer, and its Postgres stay off the public Internet; the API Worker reaches the node through Workers VPC and the database through Hyperdrive; admin pages for launch parameters sit behind Access.

### 4.12 Observability

- Workers Logs: Free 200,000 events a day with 3 days retention; Paid 20M a month included plus $0.60 per million, 7 days retention; from 2026-12-01 Workers Logs move to Cloudflare Observability pricing (https://developers.cloudflare.com/workers/platform/pricing/).
- Logpush is now self-serve on Free, Pro and Business: 25 GB a month included to internal (R2, Pipelines) and to external destinations, then $0.03 and $0.10 per GB; Workers Trace Events Logpush needs Workers Paid at 10M a month plus $0.05 per million; Logpush cannot backfill (https://developers.cloudflare.com/logs/logpush/, https://developers.cloudflare.com/logs/logpush/pricing/).
- Analytics Engine for custom metrics (section 4.4).

### 4.13 Keys and signing

- Documented: the only signing pattern in Cloudflare's docs is a private key stored as a Worker secret and used with viem's `privateKeyToAccount` inside an Agent, to pay x402 charges (https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/).
- Documented: Cloudflare Wallets will hold stablecoins with spending caps, but cannot yet hold or send funds (section 2.9).
- Recommendation: user transactions are signed in the user's wallet and only relayed by your Worker; deployer, upgrade, treasury and fee-claim keys stay in a hardware wallet or a multisig (Safe is documented on Robinhood Chain in `resources/robinhood-chain/54-safe-wallet-support.md`); a Worker holds a key only for a small hot wallet with a balance you can afford to lose, such as an x402 payer or a gas sponsor with a hard daily cap.

### 4.14 Workers AI and Agents for trading or support agents

- Workers AI: 10,000 Neurons a day free on both plans, then $0.011 per 1,000 Neurons on Workers Paid; some large models need a paid billing method (https://developers.cloudflare.com/workers-ai/platform/pricing/).
- Agents are Durable Object classes with SQLite state, WebSocket connections, scheduling and MCP; the quick start config declares them under `durable_objects` and `new_sqlite_classes` (https://developers.cloudflare.com/agents/getting-started/quick-start/).
- Agents SDK v0.4.0 added read-only WebSocket connections for spectator dashboards (https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/).
- Recommendation for the `jug-meteora` AI trading agent idea: the Agent proposes trades and builds unsigned Jupiter `/swap/v2/order` transactions, and a human signs; if it must trade autonomously, give it a capped hot wallet and log every action to D1 and Analytics Engine.

### 4.15 x402 for paid data APIs

- Charge agents per request for launch analytics, holder snapshots or candle data with the `x402-proxy` template or Hono middleware, settling in USDC on Base (section 2.5).
- If the seller is US-based and eligible, the Monetization Gateway moves verification and settlement to the edge (section 2.6).
- Recommendation: x402 settles on EVM networks in Cloudflare's tooling, so a Solana project charging in USDC needs a Base or other EVM receiving address, or a third-party Solana x402 facilitator outside Cloudflare's docs.

### 4.16 One wrangler.jsonc for the whole stack

Assembled from the docs' per-product snippets (https://developers.cloudflare.com/workers/wrangler/configuration/ and the product pages cited above); IDs are placeholders.

```jsonc
{
	"$schema": "./node_modules/wrangler/config-schema.json",
	"name": "launch-app",
	"main": "src/index.ts",
	// Dates on or after 2026-08-04 enable nodejs_compat and nodejs_compat_v2 by default
	"compatibility_date": "2026-10-05",

	"assets": {
		"directory": "./dist/",
		"binding": "ASSETS",
		"not_found_handling": "single-page-application",
		"run_worker_first": ["/api/*", "/rpc", "/ws/*"]
	},

	"kv_namespaces": [{ "binding": "CACHE", "id": "<KV_ID>" }],
	"d1_databases": [{ "binding": "DB", "database_name": "launch", "database_id": "<D1_ID>" }],
	"r2_buckets": [{ "binding": "MEDIA", "bucket_name": "launch-media" }],
	"hyperdrive": [{ "binding": "INDEXER_DB", "id": "<HYPERDRIVE_ID>" }],
	"analytics_engine_datasets": [{ "binding": "METRICS", "dataset": "launch_metrics" }],
	"ai": { "binding": "AI" },

	"durable_objects": {
		"bindings": [
			{ "name": "FEED_HUB", "class_name": "FeedHub" },
			{ "name": "TOKEN_ROOM", "class_name": "TokenRoom" }
		]
	},
	"migrations": [{ "tag": "v1", "new_sqlite_classes": ["FeedHub", "TokenRoom"] }],

	"queues": {
		"producers": [{ "queue": "tx-confirm", "binding": "TX_QUEUE" }],
		"consumers": [
			{ "queue": "tx-confirm", "max_batch_size": 10, "max_retries": 10, "dead_letter_queue": "tx-confirm-dlq" }
		]
	},
	"workflows": [{ "name": "launch", "binding": "LAUNCH", "class_name": "LaunchWorkflow" }],
	"triggers": { "crons": ["*/5 * * * *"] },

	"ratelimits": [
		{ "name": "RPC_LIMITER", "namespace_id": "1001", "simple": { "limit": 120, "period": 60 } }
	],

	// Self-hosted node or indexer reached through a Tunnel
	"vpc_services": [{ "binding": "NODE", "service_id": "<VPC_SERVICE_ID>" }],

	// Secrets (RPC_UPSTREAM_URL, TURNSTILE_SECRET, provider keys) are set with
	// `npx wrangler secret put <NAME>` or bound from Secrets Store, never in "vars".

	"observability": { "enabled": true, "head_sampling_rate": 0.1 },

	// Optional: run near the RPC provider rather than near the user
	"placement": { "mode": "smart" }
}
```

Placement note: Smart Placement "only considers locations where the Worker has previously run", and combined with `run_worker_first` the whole Worker is placed as one unit, which "may not" optimise correctly (https://developers.cloudflare.com/workers/configuration/placement/, https://developers.cloudflare.com/workers/static-assets/routing/).
Recommendation: put the RPC proxy and API in a separate Worker from the asset-serving one if placement matters.

---

## 5. Runtime compatibility for chain libraries and cryptography

| Question | What the docs say (as of 2026-10-05) |
| --- | --- |
| Node.js APIs | For compatibility dates on or after 2026-08-04, `nodejs_compat` and `nodejs_compat_v2` are on by default; earlier dates from 2024-09-23 need the `nodejs_compat` flag (https://developers.cloudflare.com/workers/runtime-apis/nodejs/). |
| `node:crypto` | "All `node:crypto` APIs are fully supported" except DSA and DH key generation, `argon2`, and the `ed448` and `x448` curves (https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/). |
| Web Crypto Ed25519 | Supported for sign, verify, generate, import and export, plus a legacy `NODE-ED25519` variant; X25519 for key agreement (https://developers.cloudflare.com/workers/runtime-apis/web-crypto/). |
| Web Crypto secp256k1 | **Not mentioned.** ECDSA is listed without naming curves, and "secp256k1" appears nowhere in the mirrored docs. |
| Post-quantum | ML-DSA and ML-KEM behind the `webcrypto_modern_algorithms` flag (same page). |
| viem | Appears only in the Agents x402 examples, imported in Worker and Agent code (`privateKeyToAccount` from `viem/accounts`) (https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/). |
| ethers, `@solana/web3.js`, `@solana/kit` | **Not mentioned anywhere** in the mirrored docs. |
| Bundle and startup | Worker size 64 MiB, global scope must run within 1 second at startup (https://developers.cloudflare.com/workers/platform/limits/). |

What follows from that (recommendation, not documented):

- Solana wallet signatures are Ed25519, so a Worker can verify a Sign-In-With-Solana message with Web Crypto directly.
- Ethereum signatures are secp256k1, which the docs do not cover natively; verify them with a JavaScript implementation such as viem's, whose Worker use the Agents examples show.
- `@solana/web3.js` and `@solana/kit` are untested by Cloudflare's docs; with Node compatibility on by default they are worth a `wrangler dev` smoke test and a `wrangler deploy` that reports `startup_time_ms` before you depend on them.
- Keep heavy decoding out of the Free plan's 10 ms CPU budget; the Robinhood KB measured decode CPU separately for its indexer sizing (`resources/robinhood-chain/52-swap-throughput-and-head-following.md`).

---

## 6. Per-chain sections

### 6.1 Solana

Chain and platform facts live in `/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/jupiter-meteora/README.md` and the `jug-meteora` findings.

| Cloudflare piece | Applies? | Solana-specific note |
| --- | --- | --- |
| Web3 gateways | No | No Solana gateway exists. |
| RPC proxy Worker | Yes | Helius publishes a one-click Cloudflare Worker proxy for JSON-RPC and WebSockets (section 4.3). |
| Durable Object feed | Yes | One `FeedHub` holds a provider `logsSubscribe` or account subscription and fans out; outbound sockets do not hibernate. |
| Static frontend | Yes | `fun-launch` is Next.js 15, which on Workers means OpenNext today or `vinext` once on Next.js 16 (section 4.2). |
| R2 | Yes | `fun-launch` already stores images in R2 with the S3 client. |
| KV | Yes | Meteora's `cloudflare-kv-merkle-proof` serves Alpha Vault proofs from KV; the Meteora studio can upload proofs to Cloudflare KV (`jupiter-meteora/meteora/01-products-and-protocol.md`). |
| Jupiter API key | Yes, behind a Worker | Jupiter uses one host `api.jup.ag` with an `x-api-key` header, keyless at 0.5 RPS, Free plan 1 RPS, and its own firewall rules that can return `Request blocked by firewall` (`jupiter-meteora/jupiter/02-developer-platform-and-apis.md`); a Worker keeps the key server-side, but all users then share one key's rate limit and one egress reputation. |
| Jupiter Plugin | No backend needed | "Needs no API key, no RPC and no backend" (`jug-meteora/findings/trading-ui-integration.md`). |
| Candles backend | Yes | The planned "small cached backend" for candles maps to a Worker with KV or the Cache API in front of `datapi.jup.ag` or another source. |
| Signing | Browser wallet only | Swap flow is `GET /swap/v2/order`, user signs, `POST /swap/v2/execute`; the Worker can relay but should not sign. |
| Web Crypto | Ed25519 native | Wallet-signature login verifiable in the Worker. |
| x402 | Protocol yes, Cloudflare SDK EVM-only | Charging in Solana USDC needs a non-Cloudflare facilitator; Cloudflare's tools settle on Base. |

### 6.2 Ethereum

| Cloudflare piece | Applies? | Note |
| --- | --- | --- |
| Ethereum Gateway | Yes | Mainnet and Sepolia, 32 methods plus `trace_filter`, no filters or subscriptions, `eth_getLogs` 800 blocks, 500,000 requests included then usage-billed (section 2.3). |
| As a fallback transport | Yes (recommendation) | A second transport in a viem `fallback` behind your primary provider, reached through your own Worker so the zone's rate limits apply. |
| Restricting it | Yes | Access policy plus service token for backend-only use (https://developers.cloudflare.com/web3/how-to/restrict-gateway-access/). |
| Live feeds | Provider WebSocket | The gateway has no subscriptions, so a `FeedHub` needs Alchemy, QuickNode or similar. |
| Signing | Wallet or hardware | The gateway accepts only `eth_sendRawTransaction`; it rejects `eth_sign`, `eth_accounts` and `eth_sendTransaction`. |
| x402 | Yes | `ethereum` is a listed x402 network. |

### 6.3 Base

| Cloudflare piece | Applies? | Note |
| --- | --- | --- |
| Gateway | No | No Base RPC from Cloudflare. |
| RPC proxy and feed | Yes | Same as any EVM chain, in front of a third-party provider. |
| x402 | Yes, first-class | Cloudflare examples default to `base` and `base-sepolia` (`eip155:84532`); the Monetization Gateway settles USDC on Base; the playground funds test wallets on a Base testnet (https://blog.cloudflare.com/x402/). |
| Paying Cloudflare | Yes | Stablecoin billing accepts USDC on Base (section 2.8). |
| Data API monetisation | Yes | A Base-native project can sell data to agents through x402 with no new chain integration. |

### 6.4 Robinhood Chain

Chain facts: `/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/resources/ROBINHOOD-CHAIN.md` (chain id 4663, testnet 46630, Arbitrum Nitro L2, ETH gas token, about 0.1 s blocks, public RPC rate-limited and "explicitly not for production", Alchemy the recommended provider, sequencer-level sanctions screening).

| Cloudflare piece | Applies? | Robinhood-specific note |
| --- | --- | --- |
| Gateway | No | Robinhood Chain is absent from every Cloudflare source. |
| RPC proxy | Yes, proven | Octopus runs a Cloudflare `/rpc` proxy for chain 46630 in production on Pages (section 1). |
| Public RPC from Workers | Avoid for scans | From Workers egress the public endpoint returned HTTP 429 to 70 of 72 `eth_getLogs` calls on 2026-09-20 and throttles "far harder than a laptop"; Multicall3 `eth_call` through Alchemy returned in 500 to 600 ms from a Worker (`resources/robinhood-chain/32-explorer-and-data-apis.md`). |
| Log scans | Not in a Worker request | Do the first backfill from a workstation and let Workers scan only incremental ranges; split only on `exceeds limit`, bound retries by wall clock (same file). |
| Live feed | Keyed WebSocket in a Durable Object | The public endpoint's WebSocket gives a socket error; Alchemy and dRPC free plans serve `eth_subscribe`, but Alchemy's free plan closed a Worker-held firehose socket with code 1008 "Monthly capacity limit exceeded" about 39 minutes after subscribing, at about 58 swap logs a second (`resources/robinhood-chain/52-swap-throughput-and-head-following.md`). |
| Polling budget | Plan for it | Octopus measured about 27 requests a minute per open token page; at 0.1 s blocks, polling every block is not viable, so push through a Durable Object. |
| Explorer API | Use the PRO API | `robinhoodchain.blockscout.com` returns Cloudflare's challenge to scripts; `api.blockscout.com/4663` with a key has no challenge (`resources/robinhood-chain/32-explorer-and-data-apis.md`). |
| Signing | Wallet or Safe | Safe is live on 4663 and 46630 (`resources/robinhood-chain/54-safe-wallet-support.md`). |
| x402 | Not as a network | Robinhood Chain is not an x402 network in Cloudflare's docs. |

---

## 7. Costs for a small launch

All prices are the documented list prices as of 2026-10-05, from https://developers.cloudflare.com/workers/platform/pricing/ unless another URL is given.
Zone plan prices (Pro, Business), Bot Management, Waiting Room advanced, Client-Side Security Advanced, Web3 gateway overage, Monetization Gateway fees and domain prices are not in the mirrored docs and are left out.

### 7.1 What the Free plan covers

| Product | Free allowance | What exceeding it does |
| --- | --- | --- |
| Static assets | Free and unlimited | Nothing |
| Workers and Pages Functions requests | 100,000 a day, reset 00:00 UTC, shared with Workflows | Error 1027, or the route fails open if configured (https://developers.cloudflare.com/workers/platform/limits/) |
| CPU | 10 ms per invocation | Error 1102 |
| Subrequests | 50 per invocation | Subrequest limit error |
| KV | 100,000 reads, 1,000 writes, 1 GB | Operations of that type fail |
| D1 | 5M rows read, 100,000 written a day, 5 GB | See D1 limits; not stated on the pricing page |
| Durable Objects (SQLite only) | 100,000 requests, 13,000 GB-s a day, 5 GB | Not stated on the pricing page |
| Queues | 10,000 operations a day, 24 h retention | Not stated on the pricing page |
| Workflows | 3,000 steps a day, 100 concurrent | Not stated on the pricing page |
| R2 | 10 GB-month, 1M Class A, 10M Class B a month (https://developers.cloudflare.com/r2/pricing/) | Billed at R2 rates |
| Workers AI | 10,000 Neurons a day | "further operations will fail with an error"; more needs Workers Paid |
| Workers Logs | 200,000 events a day, 3 days | Not stated on the pricing page |
| Cron Triggers | 5 per account | Cannot add more |
| Turnstile | 20 widgets, unlimited challenges | Not applicable |
| WAF rate limiting | 1 rule | Not applicable |

Rough capacity: at Octopus's measured 27 requests a minute per open page, 100,000 requests a day is about 60 tab-hours of a live token page, so the Free plan suits testnet and private beta, not a public launch.

### 7.2 Illustrative small public launch on Workers Paid

Assumed month (assumptions are this file's, not Cloudflare's): 1M page loads, 30M Worker requests (RPC proxy plus API), 4 ms average CPU, 20M KV reads, 200k KV writes, 2B D1 rows read, 5M written, 2 GB D1, one always-on `FeedHub`, 3M billable Durable Object requests, 3M queue operations, 20,000 launches of 10 Workflow steps, 20 GB in R2 with 1M Class A and 15M Class B operations, 1M Workers AI Neurons, 5M Analytics Engine points, 10 GB Logpush to R2.

| Line | Included in Paid | Usage | Formula | Monthly cost |
| --- | --- | --- | --- | --- |
| Workers Paid subscription | | | | $5.00 |
| Static asset requests | Unlimited | 1M | free | $0.00 |
| Worker requests | 10M | 30M | (30M - 10M) / 1M x $0.30 | $6.00 |
| Worker CPU | 30M ms | 120M ms | (120M - 30M) / 1M x $0.02 | $1.80 |
| KV reads | 10M | 20M | (20M - 10M) / 1M x $0.50 | $5.00 |
| KV writes | 1M | 0.2M | within included | $0.00 |
| D1 reads, writes, storage | 25B, 50M, 5 GB | 2B, 5M, 2 GB | within included | $0.00 |
| Durable Object duration | 400,000 GB-s | 324,000 GB-s | within included | $0.00 |
| Durable Object requests | 1M | 3M | (3M - 1M) / 1M x $0.15 | $0.30 |
| Queues | 1M ops | 3M ops | (3M - 1M) / 1M x $0.40 | $0.80 |
| Workflows steps | 500,000 | 200,000 | within included | $0.00 |
| R2 storage | 10 GB-month | 20 GB | (20 - 10) x $0.015 | $0.15 |
| R2 Class A | 1M | 1M | within free tier | $0.00 |
| R2 Class B | 10M | 15M | (15M - 10M) / 1M x $0.36 | $1.80 |
| Workers AI | 10,000 Neurons a day (about 300,000 a month) | 1,000,000 | (1,000,000 - 300,000) / 1,000 x $0.011 (https://developers.cloudflare.com/workers-ai/platform/pricing/) | $7.70 |
| Analytics Engine | 10M points | 5M | within included | $0.00 |
| Workers Logs | 20M events | under 20M | within included | $0.00 |
| Logpush to R2 | 25 GB | 10 GB | within included (https://developers.cloudflare.com/logs/logpush/pricing/) | $0.00 |
| Turnstile | Free | | | $0.00 |
| **Total** | | | | **$28.55** |

Add-ons that change the picture:

- Ethereum Gateway: 500,000 requests included per month, overage price not documented.
- Waiting Room: needs a Business zone plan.
- Bot score based rules: need Enterprise Bot Management.
- The RPC provider (Helius, Alchemy, QuickNode, dRPC) is usually the biggest bill; subrequests from Cloudflare are free, but every proxied call is still metered by the provider, and the Robinhood KB estimated $500 to $1,400 a month on Alchemy pay-as-you-go if each of 100M monthly subscription notifications were metered (`resources/robinhood-chain/32-explorer-and-data-apis.md`).
- Paying the Cloudflare invoice in USDC on Base or Polygon adds only gas (section 2.8).

---

## 8. Risks and limits

### 8.1 Terms and eligibility

- The mirrored developer docs contain no Acceptable Use Policy or self-serve subscription agreement text about cryptocurrency, tokens or launchpads; the only crypto-related terms in the docs are eligibility rules (searched on 2026-10-05).
- Monetization Gateway and AI Gateway Machine Payments require US-based buyers and sellers or customers, plus account age, card and Service-Specific Terms checks (sections 2.6 and 2.7).
- Stablecoin billing screens wallets and refuses flagged ones (section 2.8); Robinhood Chain's sequencer independently excludes transactions from sanctioned addresses (`resources/ROBINHOOD-CHAIN.md`).
- Wallet handles can be rejected or reclaimed "for any reason" and cannot be changed or moved (https://developers.cloudflare.com/wallets/faq/).
- Client-side security's malicious-code classes include "Crypto mining", so a site that ships an in-browser miner would be flagged (https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

### 8.2 Worker CPU, subrequest and connection limits for RPC fan-out

- Free: 10 ms CPU, 50 subrequests per invocation; Paid: 30 s CPU by default, configurable to 5 minutes, 10,000 subrequests by default, configurable up to 10M (https://developers.cloudflare.com/workers/platform/limits/).
- Only 6 connections may wait for response headers at once per invocation, outbound WebSockets included; extra fetches queue (same page).
- Each hop of a redirect counts as a subrequest (same page).
- `ctx.waitUntil` extends work by at most 30 seconds after the response (same page).
- Cron Triggers, Queue consumers and Durable Object alarms have a 15-minute wall-clock limit (same page).
- Recommendation: fan-out such as "price every token in a list" belongs in one Multicall3 `eth_call` on EVM or one `getMultipleAccounts` on Solana, not N parallel fetches; the Robinhood KB measured a 1,900-call Multicall3 batch at 500 to 600 ms from a Worker.

### 8.3 Cold starts and startup

- Isolates "eliminate the cold starts of the virtual machine model" (https://developers.cloudflare.com/workers/reference/how-workers-works/).
- The global scope must finish within 1 second, which large chain SDK bundles can threaten; Wrangler reports `startup_time_ms` on deploy (https://developers.cloudflare.com/workers/platform/limits/).
- Durable Objects re-run their constructor after hibernation; restore per-socket state with `serializeAttachment` (https://developers.cloudflare.com/durable-objects/best-practices/websockets/).

### 8.4 Upstream and egress risks

- Providers and public RPCs may treat Cloudflare egress worse than a home connection, as measured on Robinhood Chain (section 6.4).
- A proxy concentrates all users on one API key and its rate limit; per-IP limits at the edge are the only way to keep one abuser from exhausting it.
- Outbound WebSockets keep a Durable Object billed for duration and may be closed by a provider's capacity limit; plan reconnect and gap repair.

### 8.5 Data residency

- Durable Objects can be pinned to a jurisdiction such as the EU, but a Worker anywhere can still call them, and object IDs are logged outside the jurisdiction (https://developers.cloudflare.com/durable-objects/reference/data-location/).
- The Data Localization Suite is an "Enterprise-only paid add-on" (https://developers.cloudflare.com/data-localization/).
- KV, D1 and R2 residency controls are not covered here; on-chain data is public in any case, and the residency question is about user records such as emails, IPs and KYC flags.

### 8.6 Product maturity

- Monetization Gateway is a closed beta, Machine Payments a beta, Secrets Store an open beta, `vinext` a beta, and Wallets and NET Dollar are not available, all as of 2026-10-05.
- Free-plan limits reset at 00:00 UTC; a launch timed just before midnight UTC on Free gets two daily budgets, and one timed just after gets one.

---

## 9. Next steps checklist

Account and domain:

- [ ] Put the project domain on Cloudflare Registrar or confirm the current registrar's lock; turn on DNSSEC.
- [ ] Turn on two-factor authentication for every account member and remove unneeded super-admin and admin roles.
- [ ] Create scoped API tokens for CI with no Registrar or DNS edit rights.
- [ ] Decide Free versus Workers Paid before public launch; Paid ($5) is the sensible floor for a public launch.

Build:

- [ ] Start the frontend on Workers static assets with `not_found_handling: "single-page-application"` and `run_worker_first` only for `/api/*`, `/rpc` and `/ws/*`.
- [ ] Write the RPC proxy Worker with a method allowlist, `Sec-Fetch-Site` refusal and the Rate Limiting binding; store the upstream URL as a secret.
- [ ] Add one WAF rate limiting rule on `/rpc` and the faucet or allowlist path.
- [ ] Add Turnstile with server-side Siteverify to faucet, allowlist and create-token actions.
- [ ] Build `FeedHub` and `TokenRoom` Durable Objects; measure duration and request counts in a 24-hour soak before launch.
- [ ] Put launch steps in a Workflow and transaction confirmation behind a Queue with a dead-letter queue and idempotent consumers.
- [ ] Add Cron Triggers for cache refresh and stuck-launch sweeps.
- [ ] Ship `_headers` with a strict CSP for assets and set the same headers in code for Worker responses; load the deployed app and check for zero CSP violations, as Octopus did.
- [ ] Enable client-side security alerts for new scripts and connection domains.
- [ ] Put admin pages behind Access; reach any self-hosted node or indexer through Tunnel and Workers VPC, and its database through Hyperdrive.
- [ ] Turn on Workers Logs and Analytics Engine; add Logpush to R2 if you need history beyond 7 days.

Per chain:

- [ ] Solana: deploy the Helius proxy pattern or your own; smoke-test `@solana/web3.js` or `@solana/kit` under `wrangler dev`; keep Jupiter calls server-side only if you accept one shared key's limits.
- [ ] Ethereum: decide whether the Ethereum Gateway is a primary or a fallback; check the overage price in the dashboard first.
- [ ] Base: if selling data to agents, prototype the `x402-proxy` template on `base-sepolia`.
- [ ] Robinhood Chain: use a keyed provider for WebSockets, never the public endpoint from Workers for log scans, and the Blockscout PRO API for explorer data.

Before launch day:

- [ ] Load test `/rpc` and `/api` from outside Cloudflare and watch for Error 1027 and 1102.
- [ ] Confirm whether the Bot Fight Mode setting challenges wallet or API traffic on the zone.
- [ ] If an allowlist page needs queueing, confirm a Business plan for Waiting Room or design a server-gated alternative.
- [ ] Set usage-based billing notifications for Workers and any Web3 gateway.

Knowledge base:

- [ ] When a launch measures something new about Cloudflare (Durable Object costs for outbound sockets, Solana SDK startup times), write it back here and to the relevant chain knowledge base.

---

## 10. Gaps and contradictions

### 10.1 Contradictions between sources

1. **Web3 gateway pricing.** The 2022 general-availability post says free users "will continue to use the gateways at no cost with our free tier option", with "no cap in the amount of traffic", and that dapps use them "without rate limits or overage caps" (https://blog.cloudflare.com/ea-web3-gateways/).
   The current docs call the gateways "a paid add-on" with usage-based billing on every plan, requiring a subscription and payment details (https://developers.cloudflare.com/web3/get-started/, https://developers.cloudflare.com/web3/reference/limits/).
2. **Universal Path IPFS gateways.** The dashboard and API offer `ipfs_universal_path` without a plan caveat (https://developers.cloudflare.com/web3/how-to/manage-gateways/), the limits table restricts Universal Gateway to Enterprise (https://developers.cloudflare.com/web3/reference/limits/), and the troubleshooting page says "Cloudflare currently only supports restricted gateways - and not universal gateways" (https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/).
3. **Public gateway hostnames.** The supported-networks page still tells you to append `/v1/mainnet` to "the Cloudflare public gateway (`cloudflare-eth.com`)", and examples use `web3-trial.cloudflare-eth.com`, while the migration guide says Cloudflare "is deprecating legacy hostnames that point to our public gateway endpoints at `cloudflare-eth.com` and `cloudflare-ipfs.com`" (https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/, https://developers.cloudflare.com/web3/reference/migration-guide/).
   IPFS docs still show `cloudflare-ipfs.com` and `cf-ipfs.com` URLs although the 2024 post says those hostnames stopped connecting to IPFS on 2024-08-14 (https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/, https://blog.cloudflare.com/cloudflares-public-ipfs-gateways-and-supporting-interplanetary-shipyard/).
   Whether `cloudflare-eth.com` still answers was not checked live for this file.
4. **Rinkeby end date.** Docs say January 30, 2023; the blog says January 15, 2023 (https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/, https://blog.cloudflare.com/ethereum-merge-and-testnet-gateways/).
   The same blog added Görli, which the current supported-networks page does not list.
5. **Write support wording.** The About page limits writes to "gateways to EVM-based chains, such as Ethereum", implying other EVM chains, while only Ethereum Mainnet and Sepolia are offered (https://developers.cloudflare.com/web3/about/).
6. **x402 networks per product.** The Agents x402 page lists Base, Ethereum, Polygon, Optimism, Arbitrum, Avalanche, Solana, Aptos, Stellar and Sui, and its scheme table adds Hedera which the network sentence omits (https://developers.cloudflare.com/agents/tools/payments/x402/).
   The Monetization Gateway docs leave the network as a CAIP-2 placeholder, and its beta post says payments settle on Base in USDC (https://developers.cloudflare.com/monetization-gateway/x402/, https://blog.cloudflare.com/monetization-gateway-beta/).
7. **x402 headers and SDK generation.** The Agents x402 page describes three headers including `PAYMENT-RESPONSE`; the Monetization Gateway describes "two client-facing headers" and tells origins not to create `PAYMENT-RESPONSE` because the gateway makes the receipt (https://developers.cloudflare.com/agents/tools/payments/x402/, https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/).
   The HTTP example still uses `x402-hono` with the legacy name `base-sepolia`, while the SDK migrated to `@x402/core` and `@x402/evm` v2 and prefers CAIP-2 ids (https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/).
8. **Worker size inside Workflows.** The Workflows limits page says 3 MB on Free and 10 MB on Paid; the Workers limits page says 64 MiB on both (https://developers.cloudflare.com/workflows/reference/limits/, https://developers.cloudflare.com/workers/platform/limits/).
9. **`nodejs_compat` in new configs.** The Node.js docs say to omit the flag for compatibility dates on or after 2026-08-04, while the Agents quick start still adds it with a 2026-10-05 date; the docs call the flag redundant but harmless (https://developers.cloudflare.com/workers/runtime-apis/nodejs/, https://developers.cloudflare.com/agents/getting-started/quick-start/).
10. **Static asset requests "free and unlimited".** The pricing page says so, but its footnote 4 says that with Workers Caching enabled, requests served from cache, "including requests to static assets", are billed per request (https://developers.cloudflare.com/workers/platform/pricing/).
11. **NET Dollar status.** Cloudflare's press release says it "announced plans to introduce" NET Dollar; search-captured third-party posts say Cloudflare "has launched" it (`raw/search/q1.json`).
12. **Wallets reservation date.** Cloudflare and FF News date it 2026-08-04; a third-party post in `raw/search/q5.json` says 2026-08-05.

### 10.2 Gaps

- Web3 gateway overage prices are not in the mirrored docs.
- The Ethereum Gateway's support for JSON-RPC batches and any WebSocket endpoint is not documented either way.
- Pro, Business and Enterprise zone plan prices, Waiting Room and Client-Side Security Advanced prices, Bot Management pricing, Rate Limiting binding pricing and Monetization Gateway seller fees are not in the mirror.
- Whether Durable Object billing counts messages received on an outbound WebSocket as requests is not stated; the 20:1 rule is written for incoming client messages.
- `secp256k1`, ethers, `@solana/web3.js` and `@solana/kit` are not mentioned in any Cloudflare doc, so their Workers compatibility is untested by the sources.
- No source names NET Dollar's chain or launch date, or the chains and tokens Cloudflare Wallets will support.
- Cloudflare's AUP and self-serve terms are not in the mirror, so their treatment of tokens, launchpads and crypto is unknown here.
- The Zero Trust Free plan's seat limit is not stated in the mirrored docs.
- The GitHub catalog lists `cloudflare/cfweb3` (318 stars) with no description and no captured README (`raw/github/repos.tsv`).
- The 2022 "Serving Cloudflare Pages sites to the IPFS network" announcement has no counterpart in the current Pages or Web3 docs (https://blog.cloudflare.com/cloudflare-pages-on-ipfs/).
- The Robinhood KB's day-long Workers-egress WebSocket measurement was still marked PENDING on 2026-10-05 (`resources/robinhood-chain/52-swap-throughput-and-head-following.md`).
- No live request was made to any gateway, facilitator or `drand.cloudflare.com` for this file; everything above is from captured sources.
