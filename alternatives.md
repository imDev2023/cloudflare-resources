# Alternatives to Cloudflare for Web3 builders

Snapshot as of 2026-10-05.
Every price, free tier, chain listing and beta status below is dated to that day unless a source states another date.

## Summary

No single platform replaces Cloudflare for a Web3 builder; the realistic picture is Cloudflare as the edge, storage and agent layer, combined with chain-specific providers that Cloudflare does not offer.
On the hosting side, Vercel, Netlify, Deno Deploy, Bunny.net, Fastly and the hyperscalers each cover parts of Workers, Pages, R2, KV and the CDN, but none of their docs mention Solana, Ethereum or x402 except Supabase (wallet sign-in for Ethereum and Solana) and Vercel (an x402 Foundation member with an x402 starter template).
On the Web3 side, the important 2026 changes are that Fleek shut its hosting down on 2026-01-31, Storacha's domains now redirect to Fil One, Google Cloud retires Blockchain Node Engine and Blockchain RPC on 2026-12-15, and Amazon Managed Blockchain stops taking new customers on 2026-10-29.
For Robinhood Chain (4663), RPC is documented by Alchemy (the chain's recommended provider), QuickNode, dRPC, Ankr and Chainstack, and wallet infrastructure by Privy, Turnkey and Dynamic, with Crossmint listing it only as "not self-serve"; the Coinbase CDP x402 facilitator does not list it, and no hosted x402 facilitator in the x402 docs names it.
Almost every platform surveyed publishes an `llms.txt`, and most also publish an `llms-full.txt`, so their docs can be mirrored the way Cloudflare's were; the exceptions are Google Cloud (Firebase only), Azure, Fleek, and the Linode and Amplify sites.
The recommendation section names Helius, Alchemy, Coinbase CDP plus x402, Privy and Turnkey as the next knowledge bases to build, in that order.

## Table of contents

1. [Method and conventions](#1-method-and-conventions)
2. [At a glance](#2-at-a-glance)
3. [Edge, serverless and hosting platforms](#3-edge-serverless-and-hosting-platforms)
4. [Web3-native infrastructure](#4-web3-native-infrastructure)
5. [Robinhood Chain (4663) support matrix](#5-robinhood-chain-4663-support-matrix)
6. [Docs mirrorability: llms.txt per platform](#6-docs-mirrorability-llmstxt-per-platform)
7. [Cloudflare product -> best alternative(s)](#7-cloudflare-product---best-alternatives)
8. [Recommendations for the owner's use cases](#8-recommendations-for-the-owners-use-cases)
9. [Gaps and contradictions](#9-gaps-and-contradictions)

## 1. Method and conventions

Searches were run through the Tavily API and every result set is saved as JSON in `raw/alternatives/search/`.
Pages were fetched through the Jina reader or plain curl and saved in `raw/alternatives/pages/`.
Every `llms.txt` and `llms-full.txt` probe (URL, HTTP status, content type, size, final URL after redirects) is recorded in `raw/alternatives/llms-probe.tsv`, run 2026-10-05.
Firecrawl was not used.
Where a primary source (the vendor's own pricing page or docs) exists, it is cited; third-party sources are cited only when no primary source could be read, and are marked "third-party".
Statements that compare a platform to Cloudflare are drawn from the cited numbers on both sides; any judgment beyond that is marked "Assessment" or "Recommendation".
What is already known about Robinhood Chain comes from the canonical knowledge base at `/Volumes/Farhan/Work Folder/Dev/AI/Research-Projects/resources/` (`ROBINHOOD-CHAIN.md` section 2, `robinhood-chain/19-account-abstraction.md`, `robinhood-chain/32-explorer-and-data-apis.md` sections 8 and 11, `robinhood-chain/52-swap-throughput-and-head-following.md`).

Cloudflare baseline used for comparisons, from the mirrored docs:

- Workers Free allows 100,000 requests per day with 10 ms of CPU time per invocation, and Workers Paid costs a $5 monthly minimum with 10 million requests included and $0.30 per additional million ([Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)).
- Requests to static assets are free and unlimited on Workers ([Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)).
- R2 charges nothing for egress in any storage class ([R2 pricing](https://developers.cloudflare.com/r2/pricing/)).
- Cloudflare's Web3 product covers IPFS and Ethereum gateways ([Web3 docs](https://developers.cloudflare.com/web3/)).
- Cloudflare Wallets, last updated 2026-08-19, today only reserves a `cloudflare.pay` handle and "does not yet let you send, receive, or hold funds" ([Wallets docs](https://developers.cloudflare.com/wallets/)).
- Agent payments over x402 and MPP are documented under [Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/).

## 2. At a glance

### 2.1 Edge, serverless and hosting

| Platform | Maps to Cloudflare | Free tier (as of 2026-10-05) | Paid entry | Web3 in docs | llms.txt |
| --- | --- | --- | --- | --- | --- |
| Vercel | Workers, Pages, Firewall, Sandbox, Workflows, Queues, AI Gateway | Hobby $0, non-commercial only | Pro $20/month with $20 usage credit | x402 starter template, x402 Foundation member | Yes, plus llms-full |
| Netlify | Pages, Workers (functions and edge functions), AI Gateway | 300 credits/month, hard limit | Personal $9, Pro $20 | None found | Yes, no llms-full |
| Fastly Compute | Workers (Wasm), KV, R2-like Object Storage, CDN, WAF | Monthly free tier per docs (contradicted by third parties) | Usage-based | None found | Yes, no llms-full |
| Akamai | Workers (EdgeWorkers JS, Functions Wasm), CDN; Linode for VMs | 30-day EdgeWorkers trial; US$100 Akamai Cloud credit | Unpublished (EdgeWorkers) | None found | Yes, nested per section |
| Deno Deploy | Workers, KV, Workers for Platforms (Subhosting), Sandbox | 1M requests, 20 GiB egress, 10 h CPU | Pro $20, Builder $200 | None found | Yes, plus llms-full |
| Fly.io | Containers | No free tier; trial of 2 h runtime or 7 days | Pay as you go | None found | Yes, plus llms-full |
| Railway | Containers, R2-like Object Storage | 30-day trial with $5 credit, then $1/month | Hobby $5 min, Pro $20 min | None found | Yes, plus llms-full |
| Render | Containers, Pages | Hobby $0 plus free instances that spin down | Pro $25/month + compute | None found | Yes, plus llms-full |
| AWS | Workers (Lambda), CDN and WAF (CloudFront), Pages (Amplify) | Up to $200 credit over 6 months; CloudFront Free plan $0 | Pay as you go; CloudFront from $15 | AMB being retired | Yes, plus per-guide files |
| Google Cloud | Containers (Cloud Run), Pages and Workers (Firebase) | Cloud Run 2M requests/month; Firebase Spark | Pay as you go | Blockchain RPC being retired | Firebase only |
| Azure | Workers (Functions), Pages (Static Web Apps), CDN (Front Door) | 250,000 executions/month; SWA Free | SWA Standard $9/app/month | None checked | None found |
| Bunny.net | CDN, Workers (Edge Scripting), Containers, Images, Stream, DNS | 14-day trial | $1 monthly minimum | Accepts crypto payment | Yes, plus llms-full |
| Supabase | D1 (Postgres), R2-like storage, Workers (Edge Functions), auth | 500 MB DB, 50,000 MAU, pauses after 1 idle week | Pro $25/month | Sign in with Ethereum and Solana | Yes, plus llms-full |
| Convex | Durable Objects-style reactive backend, D1 | 1M function calls/month | Professional $25/developer/month | None found | Yes, plus llms-full |
| Puter (newer entrant) | Workers, KV, storage, AI Gateway | Free to developer; end user pays | User-pays | None found | Yes |

### 2.2 Web3-native

| Platform | Role | Solana | Ethereum | Base | Robinhood Chain | Free tier (as of 2026-10-05) | llms.txt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fleek | Former IPFS hosting | - | - | - | - | Hosting discontinued 2026-01-31 | None |
| Pinata | IPFS pinning, gateways, agents | n/a | n/a | x402 payments in USDC on Base | n/a | 1 GB, 1 gateway | Yes, plus llms-full |
| Fil One (ex-Storacha domains) | S3-compatible storage on Filecoin | n/a | n/a | n/a | n/a | 30-day trial | Yes, plus llms-full |
| AR.IO / Arweave | Permanent storage, gateways, naming | Protocol runs on Solana | Ethereum wallets can hold Turbo Credits | Base-ETH accepted for uploads | n/a | Uploads under 100 KiB free | Yes, plus llms-full |
| Akash | Container and GPU compute marketplace | n/a | n/a | n/a | n/a | $100 AkashML inference credit | Yes, plus llms-full |
| Spheron | GPU rental (no longer Web3 hosting) | n/a | n/a | n/a | n/a | Not found | Yes |
| 4EVERLAND | IPFS/Arweave hosting, RPC | SNS domains only | RPC | Not listed | Not listed | 7-day trial; monthly free package after on-chain registration | Yes, plus llms-full |
| Helius | Solana RPC, streaming, wallets | Yes | No | No | No | 1M credits, 10 rps | Yes, plus llms-full |
| Triton One | Solana, Sui, Monad RPC | Yes | No | No | No | None; $125 prepaid minimum | Yes, plus llms-full |
| Alchemy | Multi-chain RPC, data, wallets | Yes | Yes | Yes | Yes (recommended provider) | 30M CU/month | Yes, plus llms-full |
| QuickNode | Multi-chain RPC, streams, x402 RPC | Yes | Yes | Yes | Yes | 1-month trial, 10M credits | Yes, plus llms-full |
| Infura | Multi-chain RPC | Yes | Yes | Yes | Not listed | 3M credits/day | Yes (per-network files) |
| Ankr | Multi-chain RPC | Yes | Yes | Yes | Yes | 200M API credits/month | Yes, plus llms-full |
| dRPC | Multi-chain RPC | Yes | Yes | Yes | Yes | 210M CU/month | Yes, plus llms-full |
| Chainstack | Multi-chain RPC and dedicated nodes | Yes | Yes | Yes | Yes, both networks, with debug and trace | 3M request units/month | Yes, plus llms-full |
| Coinbase CDP | Wallets, x402 facilitator, node, paymaster | Yes | Yes | Yes | Not listed | 5,000 wallet ops; 1,000 facilitator tx; 10M node BU | Yes, plus llms-full |
| Privy | Embedded wallets, auth | Yes | Yes | Yes | Yes | Up to 500 MAU, 50K signatures | Yes, plus llms-full |
| Dynamic | Embedded wallets, auth | Yes | Yes | Yes | Yes (all EVM networks) | Up to 1,000 MAU | Yes (sectioned) |
| Crossmint | Smart wallets, checkout, onramp | Yes | Not self-serve | Yes | Not self-serve | 1,000 monthly active wallets | Yes, plus llms-full |
| Turnkey | Key management and signing | Yes | Yes | Yes | Yes | 25 signatures/month, up to 1k wallets | Yes, plus llms-full |

Each cell is sourced in sections 3 to 6.

## 3. Edge, serverless and hosting platforms

### 3.1 Vercel

**Maps to Cloudflare:** Workers (Vercel Functions on Fluid compute), Pages, the CDN, Firewall and Bot Management (WAF, BotID), Sandbox, Workflows, Queues, Blob storage (R2-like), and AI Gateway, all listed on the [pricing page](https://vercel.com/pricing).

**Pricing and free tier (as of 2026-10-05):**
- Hobby is $0/month and is "for personal, non-commercial use" ([pricing FAQ](https://vercel.com/pricing)).
- Hobby includes 1M CDN requests and 100 GB Fast Data Transfer per month, 4 hours of Fluid Active CPU, 360 GB-hours of provisioned memory, 1 GB of Blob storage and 5 hours of Sandbox Active CPU ([pricing](https://vercel.com/pricing)).
- Pro is $20/month per developer seat with $20 of included usage credit and a "Flat Rate CDN" ([pricing](https://vercel.com/pricing)).
- Pro overage starts at $0.128 per Active CPU hour, $0.0106 per provisioned GB-hour and $0.60 per 1M function invocations ([pricing](https://vercel.com/pricing)).
- Workflows include 50K events per month, then $20 per 1M events ([pricing](https://vercel.com/pricing)).
- A third-party summary says a Hobby project is paused rather than billed when it hits a limit ([temps.sh, third-party](https://temps.sh/blog/vercel-pricing-complete-guide-2026)).

**Web3 relevance:** the x402 docs link a "Vercel Starter" x402 AI template ([docs.x402.org llms.txt](https://docs.x402.org/llms.txt), [template](https://vercel.com/templates/ai/x402-ai-starter)), and Vercel is listed as an x402 Foundation member ([x402.org llms.txt](https://x402.org/llms.txt)).
Vercel's own `llms-full.txt` (10.3 MB) has no occurrence of "x402", "Solana", "Ethereum" or "web3" (grep, 2026-10-05).

**Chain support:** none native; RPC and wallets come from the providers in section 4.

**Versus Cloudflare:**
- Cloudflare Workers Free has no commercial-use restriction in its pricing doc, while Vercel Hobby forbids commercial use ([Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/), [Vercel pricing](https://vercel.com/pricing)).
- Vercel meters data transfer (100 GB on Hobby); Cloudflare does not charge for static-asset requests ([Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)).
- Assessment: Vercel's strength is framework-first deploys for Next.js; its weakness for this owner is the non-commercial Hobby plan and per-seat Pro pricing.

**Docs for LLMs:** [vercel.com/docs/llms.txt](https://vercel.com/docs/llms.txt) (redirects to `vercel.com/llms.txt`, 4.9 KB) and [vercel.com/docs/llms-full.txt](https://vercel.com/docs/llms-full.txt) (10.3 MB).

### 3.2 Netlify

**Maps to Cloudflare:** Pages, Workers (Functions and Edge Functions), Blob storage, Firewall Traffic Rules and rate limiting, AI Gateway, and a Netlify Database ([pricing](https://www.netlify.com/pricing/)).

**Pricing and free tier (as of 2026-10-05):**
- Free is $0 forever with a 300-credit monthly limit and no auto recharge ([pricing](https://www.netlify.com/pricing/), [credit-based plans docs](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans)).
- Personal is $9/month with 1,000 credits; Pro is $20/month "with unlimited members" starting at 3,000 credits and selectable up to 20,000 credits ([pricing](https://www.netlify.com/pricing/)).
- Credits are consumed at 15 per production deploy, 10 per GB-hour of compute, 20 per GB of bandwidth and 2 per 10k web requests ([pricing](https://www.netlify.com/pricing/)).
- A 2026-04-14 changelog announced free unlimited seats on Pro and updated credit rates ([changelog](https://www.netlify.com/changelog/2026-04-14-pricing-updates-april-2026)).

**Web3 relevance:** no Web3, x402 or chain content in the docs index ([docs.netlify.com/llms.txt](https://docs.netlify.com/llms.txt), grep 2026-10-05).

**Versus Cloudflare:** 300 credits buys about 15 GB of bandwidth at 20 credits per GB, against unmetered static-asset requests on Workers ([Netlify pricing](https://www.netlify.com/pricing/), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)).
Assessment: Netlify is a Pages substitute, not a Workers or Durable Objects substitute.

**Docs for LLMs:** [docs.netlify.com/llms.txt](https://docs.netlify.com/llms.txt) (25 KB) and [www.netlify.com/llms.txt](https://www.netlify.com/llms.txt); `docs.netlify.com/llms-full.txt` returns 404.

### 3.3 Fastly (Compute)

**Maps to Cloudflare:** Workers (WebAssembly-based Edge Compute supporting Rust, JavaScript and Go), Workers KV (Key Value Store), R2 (Object Storage with "zero egress fees"), CDN, Next-Gen WAF and DDoS ([fastly.com/llms.txt](https://www.fastly.com/llms.txt)).

**Pricing and free tier (as of 2026-10-05):**
- Fastly's docs say "We provide a monthly free tier of services for many Network Services and Compute products, subject to certain limitations" ([account types](https://www.fastly.com/documentation/guides/organizations-and-accounts/billing/account-types)).
- A "Legacy Compute services development trial" of up to $50 of Compute charges applies only to trial accounts created before 2026-03-31 ([account types](https://www.fastly.com/documentation/guides/organizations-and-accounts/billing/account-types)).
- Third-party rate cards give Compute at $0.50 per million requests plus duration and vCPU charges ([srvrlss.io, third-party](https://www.srvrlss.io/provider/fastly)).
- The official pricing page rendered only an image through the reader, so list prices were not read from Fastly directly.
- Fastly runs a free program for open-source and nonprofit projects called Fast Forward ([account types](https://www.fastly.com/documentation/guides/organizations-and-accounts/billing/account-types)).

**Web3 relevance:** none found in the docs index.

**Versus Cloudflare:** Assessment: Fastly is the closest architectural peer for programmable edge plus KV plus object storage, but with Wasm instead of V8 isolates and without Durable Objects, D1, Queues or a Web3 gateway equivalent.

**Docs for LLMs:** [www.fastly.com/documentation/llms.txt](https://www.fastly.com/documentation/llms.txt) (14 KB), also at `docs.fastly.com/llms.txt`; no `llms-full.txt` (404).

### 3.4 Akamai (EdgeWorkers, Akamai Functions, Akamai Cloud / Linode)

**Maps to Cloudflare:** Workers (EdgeWorkers runs JavaScript on V8; Akamai Functions runs WebAssembly through Spin on Akamai Cloud), CDN and security, and with Akamai Cloud (formerly Linode) VMs, object storage and Kubernetes ([EdgeWorkers](https://www.akamai.com/products/serverless-computing-edgeworkers), [Akamai Functions](https://www.akamai.com/products/akamai-functions), [Akamai Functions llms.txt](https://techdocs.akamai.com/akamai-functions/llms.txt)).

**Pricing and free tier (as of 2026-10-05):**
- EdgeWorkers offers a 30-day free trial requested through a sales form ([EdgeWorkers](https://www.akamai.com/products/serverless-computing-edgeworkers)).
- EdgeWorkers list pricing is not published; a third party reports three tiers (Basic, Dynamic and Enterprise Compute) billed by events per month ([srvrlss.io, third-party](https://www.srvrlss.io/provider/akamai-edge)).
- Akamai Cloud advertises "US$100 in credits" for new accounts ([Linode pricing page](https://www.linode.com/pricing/)).
- The Nanode 1 GB shared-CPU VM is $5/month according to a third party; the official plan table did not render through the reader ([costbench, third-party](https://costbench.com/software/cloud-infrastructure/linode/free-plan)).

**Web3 relevance:** none found.

**Versus Cloudflare:** EdgeWorkers allows a 64 to 128 MB memory range and up to 1 minute timeout according to a third party ([srvrlss.io, third-party](https://www.srvrlss.io/compare/akamai-edge-vs-fermyon-wasm-functions)).
Assessment: enterprise-sales pricing makes EdgeWorkers a poor fit for a solo Web3 builder; Akamai Cloud VMs are a plain VPS alternative for indexers.

**Docs for LLMs:** [techdocs.akamai.com/llms.txt](https://techdocs.akamai.com/llms.txt) (122 KB) links a separate `llms.txt` per product and section; Akamai Cloud has [techdocs.akamai.com/cloud-computing/llms.txt](https://techdocs.akamai.com/cloud-computing/llms.txt); `www.linode.com/llms.txt` and `www.akamai.com/llms.txt` return 403.

### 3.5 Deno Deploy

**Maps to Cloudflare:** Workers, Workers KV (Deno KV), Workers for Platforms (Deno Subhosting) and Sandbox (Deno Sandbox) ([pricing](https://deno.com/deploy/pricing)).

**Pricing and free tier (as of 2026-10-05), all from the [pricing page](https://deno.com/deploy/pricing):**
- Free: 1M requests/month, 20 GiB egress, 5 custom domains, 10 hours of active CPU, 150 GiB-hours of memory time, 10 apps, 1 GiB KV storage.
- Pro: $20/month, 5M requests then $2/M, 200 GiB egress then $0.20/GiB, 50 hours of active CPU then $0.10/hour.
- Builder: $200/month, 25M requests, 2,000 GiB egress, aimed at Subhosting users.
- Active CPU is billed only while code runs, not while waiting on network I/O.

**Web3 relevance:** none found.

**Versus Cloudflare:** Deno Free allows 1M requests per month; Workers Free allows 100,000 per day, about 3M per month ([Deno pricing](https://deno.com/deploy/pricing), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)).
Assessment: the closest like-for-like Workers substitute for JavaScript and TypeScript, without Durable Objects, R2, D1 or Queues equivalents.

**Docs for LLMs:** [docs.deno.com/llms.txt](https://docs.deno.com/llms.txt) and [docs.deno.com/llms-full.txt](https://docs.deno.com/llms-full.txt) (2.5 MB).

### 3.6 Fly.io

**Maps to Cloudflare:** Containers (Fly Machines are full VMs), plus Sprites, Managed Postgres and volumes ([pricing](https://fly.io/pricing/)).

**Pricing and free tier (as of 2026-10-05):**
- "There is no 'free account/free tier' on Fly.io" ([cost management](https://docs.fly.io/about/cost-management)).
- New accounts get a trial of 2 hours of Machine runtime or 7 days, whichever comes first, with no credit card ([free trial](https://docs.fly.io/about/free-trial)).
- The cheapest always-on app, a `shared-cpu-1x` Machine with 256 MB in `iad` or `ewr`, costs $2.19 per 30 days plus egress at $0.02/GB in North America and Europe ([pricing docs](https://docs.fly.io/about/pricing)).
- Some items stay free after the trial: the first 10 GB of volume snapshots, 10 single-hostname certificates, inbound transfer, shared IPv4 and IPv6 ([pricing docs](https://docs.fly.io/about/pricing)).

**Web3 relevance:** none found; one generic "crypto" mention in 2.9 MB of docs.

**Versus Cloudflare:** Assessment: Fly suits long-running processes Workers cannot host, such as a Solana gRPC stream consumer or an indexer holding WebSocket subscriptions, at the cost of managing VM sizing.

**Docs for LLMs:** [fly.io/llms.txt](https://fly.io/llms.txt), [docs.fly.io/llms.txt](https://docs.fly.io/llms.txt) (83 KB) and [docs.fly.io/llms-full.txt](https://docs.fly.io/llms-full.txt) (2.9 MB).

### 3.7 Railway

**Maps to Cloudflare:** Containers, R2 (Object Storage with free egress), plus sandboxes and VMs ([pricing](https://railway.com/pricing)).

**Pricing and free tier (as of 2026-10-05), all from the [pricing page](https://railway.com/pricing):**
- Free: a 30-day free trial with $5 of credits, then $1 per month, up to 1 vCPU and 0.5 GB RAM per service, 0.5 GB of volume storage, no credit card required.
- Hobby: $5 minimum usage including $5 of credits; Pro: $20 minimum usage including $20 of credits.
- Rates: memory $0.00000386 per GB-second, CPU $0.00000772 per vCPU-second, egress $0.05/GB, Object Storage $0.015 per GB-month with free egress.

**Web3 relevance:** none found.

**Versus Cloudflare:** Assessment: a simpler always-on container host than Cloudflare Containers for bots and indexers, with per-second billing.

**Docs for LLMs:** [docs.railway.com/llms.txt](https://docs.railway.com/llms.txt) (77 KB), [docs.railway.com/llms-full.txt](https://docs.railway.com/llms-full.txt) (2.6 MB) and [railway.com/llms.txt](https://railway.com/llms.txt).

### 3.8 Render

**Maps to Cloudflare:** Containers, Pages (static sites), plus managed Postgres and Key Value ([pricing](https://render.com/pricing)).

**Pricing and free tier (as of 2026-10-05):**
- Hobby is $0/month plus compute, with up to 25 services and 5 GB of bandwidth; Pro is $25/month plus compute with 25 GB of bandwidth; Scale is $499/month plus compute ([pricing](https://render.com/pricing)).
- Free web services spin down after 15 minutes without inbound traffic and take about a minute to spin back up ([free docs](https://render.com/docs/free)).
- Each workspace gets 750 free instance hours per month ([free docs](https://render.com/docs/free)).
- Free Render Postgres databases expire 30 days after creation, with a 14-day grace period before deletion ([free docs](https://render.com/docs/free)).

**Web3 relevance:** none found.

**Versus Cloudflare:** Assessment: free instances that sleep are unsuitable for bots or listeners that must stay connected.

**Docs for LLMs:** [render.com/docs/llms.txt](https://render.com/docs/llms.txt) (46 KB) and [render.com/docs/llms-full.txt](https://render.com/docs/llms-full.txt) (1.1 MB, stamped "Generated on: 2026-10-05").

### 3.9 AWS (Lambda, CloudFront, Amplify)

**Maps to Cloudflare:** Workers (Lambda), CDN, DNS, DDoS, WAF and edge compute (CloudFront), Pages (Amplify Hosting), R2 (S3).

**Pricing and free tier (as of 2026-10-05):**
- New accounts get $100 of credits at sign-up and can earn up to $100 more, for up to $200 over 6 months on the Free plan, after which the account closes unless converted to a Paid plan ([AWS Free Tier](https://aws.amazon.com/free/)).
- Lambda's free tier includes 1 million requests and 400,000 GB-seconds per month; requests cost $0.20 per 1M after that ([Lambda pricing](https://aws.amazon.com/lambda/pricing/)).
- CloudFront now sells flat-rate plans per distribution with no overage charges: Free $0 (1M requests, 100 GB), Pro $15 (10M requests, 50 TB), Business $200 (125M requests, 50 TB) and Premium $1,000 (500M requests, 50 TB) ([CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/)).
- The CloudFront Free plan includes DNS, always-on DDoS protection, CDN, a WAF with 5 rules, serverless edge compute and 5 GB of S3 storage, and "Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage allowance" ([CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/)).
- Amplify Hosting charges $0.01 per build minute, $0.15 per GB served and $0.30 per 1M SSR requests, with free allowances of 1,000 build minutes, 15 GB transfer and 500,000 SSR requests per month ([Amplify pricing](https://aws.amazon.com/amplify/pricing/)).

**Web3 relevance:** Amazon Managed Blockchain (AMB) "will stop accepting new customers on October 29, 2026" and can be used by existing customers "until September 29, 2027" ([AMB end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html)).
AMB supported Ethereum, Polygon, Bitcoin and Hyperledger Fabric, not Solana or Base ([AMB](https://aws.amazon.com/managed-blockchain)).

**Versus Cloudflare:** CloudFront's Free plan is the first AWS offer shaped like Cloudflare's free CDN plan, with 1M requests and 100 GB per month ([CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/)).
Assessment: AWS is worth using for S3-adjacent workloads, not as a Web3 node provider, given AMB's retirement.

**Docs for LLMs:** [docs.aws.amazon.com/llms.txt](https://docs.aws.amazon.com/llms.txt) (418 KB) plus per-guide files such as [Lambda's](https://docs.aws.amazon.com/lambda/latest/dg/llms.txt) (93 KB); `aws.amazon.com/llms.txt` and `docs.amplify.aws/llms.txt` return 404.

### 3.10 Google Cloud (Cloud Run, Firebase)

**Maps to Cloudflare:** Containers (Cloud Run), Pages and Workers (Firebase Hosting, App Hosting and Cloud Functions), D1 or KV (Firestore), and authentication.

**Pricing and free tier (as of 2026-10-05):**
- Cloud Run's free tier gives 180,000 vCPU-seconds, 360,000 GiB-seconds and 2 million requests per month, aggregated per billing account, plus 1 GiB of free North America egress ([Cloud Run pricing](https://cloud.google.com/run/pricing)).
- Firebase's no-cost Spark plan needs no payment method; the Blaze plan is pay as you go ([Firebase pricing](https://firebase.google.com/pricing)).
- On Blaze, Cloud Functions include 2M invocations per month then $0.40 per million, and App Hosting includes 10 GiB of egress per month then $0.20/GiB uncached or $0.15/GiB cached ([Firebase pricing](https://firebase.google.com/pricing)).
- Firebase Hosting includes 10 GB storage and 360 MB/day of transfer; Authentication includes 50K MAU; Firestore includes 1 GiB stored, 50K reads and 20K writes per day ([Firebase pricing](https://firebase.google.com/pricing)).

**Web3 relevance:** "Blockchain Node Engine and Blockchain RPC will be shut down on December 15, 2026" and existing nodes and endpoints will be deleted that day ([release notes](https://docs.cloud.google.com/blockchain-node-engine/docs/release-notes)).
Google's migration guide points to QuickNode ([release notes](https://docs.cloud.google.com/blockchain-node-engine/docs/release-notes), [QuickNode migration page](https://www.quicknode.com/gcp-node-migration)).

**Versus Cloudflare:** Assessment: Cloud Run is a credible container host with a meaningful free tier; Google's own Web3 node product should not be adopted now.

**Docs for LLMs:** [firebase.google.com/docs/llms.txt](https://firebase.google.com/docs/llms.txt) (1.8 MB); `cloud.google.com/llms.txt` answers with an HTML page and `docs.cloud.google.com/llms.txt` returns 404, so Google Cloud itself has no `llms.txt` (probe 2026-10-05).

### 3.11 Azure (Functions, Static Web Apps, Front Door)

**Maps to Cloudflare:** Workers (Azure Functions), Pages (Static Web Apps) and CDN and WAF (Azure Front Door).

**Pricing and free tier (as of 2026-10-05):**
- The Flex Consumption plan includes "a monthly free grant of 250,000 executions and 100,000 GB-s of resource consumption per month per subscription" ([Functions pricing](https://azure.microsoft.com/en-us/pricing/details/functions/)).
- Per-unit prices on that page are rendered by script and came through the reader as "$-", so they were not captured.
- Static Web Apps Free is for hobby projects; Standard is $9/app/month; both include 100 GB of bandwidth per subscription ([SWA pricing](https://azure.microsoft.com/en-us/pricing/details/app-service/static/)).

**Web3 relevance:** none checked beyond the pricing pages.

**Versus Cloudflare:** Assessment: no reason to choose Azure for this owner's stack unless an enterprise customer requires it.

**Docs for LLMs:** none found; `learn.microsoft.com/llms.txt`, `learn.microsoft.com/en-us/azure/llms.txt`, `azure.microsoft.com/llms.txt` and `learn.microsoft.com/en-us/azure/azure-functions/llms.txt` all return 404.

### 3.12 Bunny.net

**Maps to Cloudflare:** CDN, Workers (Edge Scripting), Containers (Magic Containers), R2-like Bunny Storage, Images (Optimizer), Stream, DNS, and a Bunny Database ([pricing](https://bunny.net/pricing/), [docs llms.txt](https://bunny.net/docs/llms.txt)).

**Pricing and free tier (as of 2026-10-05):**
- $1 monthly minimum, no request fees, and a 14-day free trial with no credit card ([pricing](https://bunny.net/pricing/)).
- Standard CDN network (119 PoPs): $0.01/GB in Europe and North America, $0.03 in Asia and Oceania, $0.045 in South America, $0.06 in the Middle East and Africa; Volume network (10 PoPs) from $0.005/GB ([pricing](https://bunny.net/pricing/)).
- Edge Scripting costs $0.02 per 1,000 seconds of CPU time plus $0.20 per million requests, with a $0.22 minimum monthly charge ([Edge Scripting pricing](https://bunny.net/docs/scripting/pricing)).
- Magic Containers bills CPU at $0.02 per CPU-hour and RAM in 64 MB increments per hour ([Magic Containers pricing](https://bunny.net/docs/magic-containers/pricing)).
- Bunny accepts payment by PayPal, cards "and crypto" ([pricing](https://bunny.net/pricing/)).

**Web3 relevance:** only crypto payment for invoices.

**Versus Cloudflare:** Assessment: the cheapest predictable CDN bandwidth in this survey and a Workers-like scripting layer, but no free plan after the trial and no stateful edge primitive like Durable Objects.

**Docs for LLMs:** [bunny.net/docs/llms.txt](https://bunny.net/docs/llms.txt) (73 KB, `docs.bunny.net` redirects there), [bunny.net/docs/llms-full.txt](https://bunny.net/docs/llms-full.txt) (1.7 MB) and [bunny.net/llms.txt](https://bunny.net/llms.txt).

### 3.13 Supabase

**Maps to Cloudflare:** D1 (managed Postgres), R2-like file storage, Workers (Edge Functions), Realtime, and authentication that Cloudflare does not offer as a product.

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://supabase.com/pricing):**
- Free: 50,000 MAU, 500 MB database, 5 GB egress, 5 GB cached egress, 1 GB file storage, 500,000 Edge Function invocations.
- "Free projects are paused after 1 week of inactivity. Limit of 2 active projects."
- Pro: $25/month with 100,000 MAU and 250 GB egress; Team: $599/month.

**Web3 relevance:** `signInWithWeb3` signs users in by verifying a wallet signature, supporting Ethereum (Sign-In-With-Ethereum, EIP-4361) and Solana (Sign-In-With-Solana) ([auth-web3 guide](https://supabase.com/docs/guides/auth/auth-web3), [JS reference](https://supabase.com/docs/reference/javascript/auth-signinwithweb3)).

**Chain support:** Ethereum and Solana wallet sign-in; Base and Robinhood Chain are EVM and the SIWE flow is chain-agnostic per EIP-4361, but neither is named in the docs.

**Versus Cloudflare:** Assessment: complements rather than replaces Cloudflare; Hyperdrive exists to front a Postgres such as Supabase from Workers.

**Docs for LLMs:** [supabase.com/llms.txt](https://supabase.com/llms.txt) (3 KB index) and [supabase.com/llms-full.txt](https://supabase.com/llms-full.txt) (7.2 MB).

### 3.14 Convex

**Maps to Cloudflare:** a reactive TypeScript database and function runtime that overlaps Durable Objects plus D1, with file storage, text and vector search, crons and auth ([pricing](https://www.convex.dev/pricing)).

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://www.convex.dev/pricing):**
- Free and Starter: $0/month and pay as you go for 1 to 6 developers; 1M function calls included then $2.20 per additional 1M; 20 GB-hours of action compute then $0.33 per GB-hour.
- Professional: $25 per developer per month, 25M function calls then $2 per 1M, 250 GB-hours of action compute.
- Enterprise: $2,500 monthly minimum.

**Web3 relevance:** none found.

**Versus Cloudflare:** Assessment: a faster path to real-time app state (live order books, chat) than hand-rolled Durable Objects, at the cost of a second vendor.

**Docs for LLMs:** [docs.convex.dev/llms.txt](https://docs.convex.dev/llms.txt) (46 KB), [docs.convex.dev/llms-full.txt](https://docs.convex.dev/llms-full.txt) (2.6 MB) and [www.convex.dev/llms.txt](https://www.convex.dev/llms.txt).

### 3.15 Newer entrants surfaced by the 2026 searches

**Puter.**
A May 2026 Puter blog lists "Puter (Serverless Workers)" first among Cloudflare Workers alternatives and describes a "User-Pays Model" in which a worker's AI, storage or compute cost is "charged to the end user's" Puter account ([Puter blog](https://developer.puter.com/blog/cloudflare-workers-alternatives)).
Puter.js offers auth, storage, a key-value database and one API for 400+ to 500+ AI models ([developer llms.txt](https://developer.puter.com/llms.txt)).
The ranking comes from Puter's own blog, so it is a vendor claim.
Docs: [developer.puter.com/llms.txt](https://developer.puter.com/llms.txt) and [docs.puter.com/llms.txt](https://docs.puter.com/llms.txt).

**Northflank.**
Northflank appears in several 2026 "alternatives" lists and prices compute at $0.01667 per vCPU-hour and $0.00833 per GB-hour, with egress at $0.06/GB ([pricing](https://northflank.com/pricing), [Northflank blog](https://northflank.com/blog/best-cloudflare-workers-alternatives)).
It is not new in 2026; it is listed because the searches surfaced it.
Docs: [northflank.com/docs/llms.txt](https://northflank.com/docs/llms.txt).

No search surfaced a 2026 launch that changes the comparison; the 2026 news in this space was retirements (Fleek hosting, Google Blockchain RPC, AWS AMB) rather than entrants.

## 4. Web3-native infrastructure

### 4.1 Decentralized hosting, storage and compute

#### Fleek

**Status:** Fleek's IPFS hosting "was discontinued on January 31st, 2026" ([IPFS docs case study](https://docs.ipfs.tech/case-studies/fleek)).
Shipyard, which maintains IPFS, wrote that "Fleek is pivoting to AI and discontinuing its hosting services on January 31, 2026" and moved ipfs.tech and its docs to GitHub Pages plus self-hosted IPFS Cluster plus DNSLink ([Shipyard blog, 2026-01-06](https://ipshipyard.com/blog/2026-ipfs-self-hosting-migration)).
The same post notes that nft.storage transitioned operations and Infura deprecated its public IPFS API and gateway ([Shipyard blog](https://ipshipyard.com/blog/2026-ipfs-self-hosting-migration)).
On 2026-10-05, `fleek.xyz` redirected to `fleek.sh`, which shows only "What if you could start over? We've been building something new" ([fleek.sh](https://fleek.sh/)), and `docs.fleek.xyz` did not resolve in DNS.

**Maps to Cloudflare:** previously Pages plus the IPFS gateway; now nothing.

**Docs for LLMs:** none.

**Shipyard's lesson, which they state directly:** build the CAR file in your own CI so content is portable across pinning providers, and keep HTTP hosting, IPFS pinning and DNSLink independent; Cloudflare Pages is one of the HTTP options they name ([Shipyard blog](https://ipshipyard.com/blog/2026-ipfs-self-hosting-migration)).

#### Pinata

**Maps to Cloudflare:** R2 plus the IPFS gateway (dedicated gateways with CDN), and now hosted AI agents ([pricing](https://pinata.cloud/pricing), [docs llms.txt](https://docs.pinata.cloud/llms.txt)).

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://pinata.cloud/pricing):**
- Free: $0, 1 GB storage, 1 gateway, 0 agents.
- Picnic: $20/month, 1 TB storage, 1 gateway plus CDN, 1 agent.
- Fiesta: $100/month, 5 TB storage, 3 gateways plus CDN, 3 agents.

**Web3 relevance:** x402 monetization attaches payment requirements to private files "using USDC on Base" and "is available on paid Pinata accounts" ([x402 intro](https://docs.pinata.cloud/files/x402/intro)).
Pinata also runs an MPP server for "account-free IPFS uploads and downloads using crypto payments" ([docs llms.txt](https://docs.pinata.cloud/llms.txt)).

**Chain support:** payments on Base; storage is chain-neutral.

**Versus Cloudflare:** Cloudflare's IPFS gateway reads content; Pinata pins and serves it, so the two are complementary.

**Docs for LLMs:** [docs.pinata.cloud/llms.txt](https://docs.pinata.cloud/llms.txt) (23 KB) and [docs.pinata.cloud/llms-full.txt](https://docs.pinata.cloud/llms-full.txt) (717 KB).

#### Storacha, now Fil One

**Status:** on 2026-10-05, `docs.storacha.network` and `storacha.network` both redirected to `www.fil.one` (see `raw/alternatives/llms-probe.tsv`).
A Filecoin post describes "Storacha Forge, built on Filecoin. IPFS-compatible, high-throughput storage with programmable access at $5.99 per TB" ([Filecoin on X](https://x.com/Filecoin/status/2034578162206535839)).

**Maps to Cloudflare:** R2 (S3-compatible object storage).

**Pricing and free tier (as of 2026-10-05):** "flat pricing at $5.99/TB/month", "no egress penalties, no per-request charges", and a "Free 30-day trial, no credit card required"; regions are `eu-west-1` (France, default) and `us-east-1` (Michigan), each run by an independent storage operator ([Fil One llms-full.txt](https://www.fil.one/llms-full.txt)).

**Web3 relevance:** Filecoin-backed durability; no chain payment flow is described in the llms files.
A third-party on-chain census reports Filecoin storage providers down 87% and deals down 97% from peak ([Bitquery, third-party](https://bitquery.io/investigations/filecoin-storage-in-numbers)).

**Versus Cloudflare:** both charge no egress; R2 adds a free tier and Workers bindings ([R2 pricing](https://developers.cloudflare.com/r2/pricing/)).

**Docs for LLMs:** [www.fil.one/llms.txt](https://www.fil.one/llms.txt) (5.5 KB) and [www.fil.one/llms-full.txt](https://www.fil.one/llms-full.txt) (10 KB).

#### AR.IO and Arweave

**Maps to Cloudflare:** Pages for permanent sites, R2 for permanent data, the IPFS gateway role (gateways that "cache, index, verify, and serve permanent data"), and a naming layer (ArNS) that loosely parallels DNS ([ar.io llms.txt](https://ar.io/llms.txt)).

**Pricing and free tier (as of 2026-10-05):**
- "Files under 100 KiB upload free via Turbo" ([docs llms.txt](https://docs.ar.io/llms.txt)).
- Larger uploads use Turbo Credits; the `ario-deploy` tool can pay on demand with ARIO or Base-ETH, converting them to Turbo Credits ([docs llms-full.txt](https://docs.ar.io/llms-full.txt)).
- A free Solana devnet testnet sandbox is available at `https://ar-io.dev` ([docs llms.txt](https://docs.ar.io/llms.txt)).

**Web3 relevance:** "ar.io is the access and naming layer for Arweave (permanent storage), with protocol execution on Solana"; ARIO is an SPL token and ArNS name tokens are Metaplex Core NFTs ([docs llms.txt](https://docs.ar.io/llms.txt)).
ArNS names resolve as subdomains on every gateway, for example `yourname.ar.io` ([docs llms.txt](https://docs.ar.io/llms.txt)).

**Chain support:** Solana for the protocol; Base-ETH for upload payment.

**Versus Cloudflare:** Assessment: the only option here whose frontends outlive the vendor; pair it with a Cloudflare-hosted domain for a normal URL.

**Docs for LLMs:** [docs.ar.io/llms.txt](https://docs.ar.io/llms.txt), [docs.ar.io/llms-full.txt](https://docs.ar.io/llms-full.txt) (1.3 MB), [ar.io/llms.txt](https://ar.io/llms.txt), plus a `SKILL.md` for agents.

#### Akash Network

**Maps to Cloudflare:** Containers and Workers AI (AkashML hosted inference).

**Pricing and free tier (as of 2026-10-05):**
- Akash is "an open marketplace for cloud compute" where providers bid on deployments; the managed Console funds deployments from USD account credits, and ACT is a USD-pegged compute credit ([llms.txt](https://akash.network/llms.txt), [llms-full.txt](https://akash.network/llms-full.txt)).
- Listed GPU rates include H100 80 GB SXM5 at $2.72/hour, A100 80 GB PCIe at $1.33/hour and B200 at $5.00/hour ([GPU pricing](https://akash.network/pricing/gpus/)).
- New AkashML accounts receive "$100 in AI token credits" ([AkashML blog](https://akash.network/blog/akashml-managed-ai-inference-on-the-decentralized-supercloud)).
- Burn-Mint Equilibrium went live on mainnet on 2026-03-23 ([Q1 2026 report](https://akash.network/blog/akash-network-q1-2026-report)).

**Web3 relevance:** token-coordinated compute; no chain RPC product.

**Versus Cloudflare:** Assessment: cheaper GPU access than Workers AI for self-hosted models, but persistent storage "is provider-local and needs backups" ([llms.txt](https://akash.network/llms.txt)).

**Docs for LLMs:** [akash.network/llms.txt](https://akash.network/llms.txt) (18 KB) and [akash.network/llms-full.txt](https://akash.network/llms-full.txt) (50 KB).

#### Spheron

**Status:** Spheron's docs now describe "Enterprise GPU Rental" with GPUs "from $0.72/hr" ([docs llms.txt](https://docs.spheron.ai/llms.txt)), and `docs.spheron.network` redirects to `docs.spheron.ai`.
Neither llms file mentions IPFS, Web3 or static-site hosting (grep 2026-10-05), so Spheron no longer overlaps Cloudflare Pages.

**Maps to Cloudflare:** Workers AI only, as raw GPU capacity.

**Docs for LLMs:** [docs.spheron.ai/llms.txt](https://docs.spheron.ai/llms.txt) (19 KB) and [www.spheron.network/llms.txt](https://www.spheron.network/llms.txt) (194 KB); no `llms-full.txt`.

#### 4EVERLAND

**Maps to Cloudflare:** Pages (IPFS and Arweave hosting), R2-like storage, the IPFS gateway, and RPC ([docs llms.txt](https://docs.4everland.org/llms.txt)).

**Pricing and free tier (as of 2026-10-05), from the [pricing model](https://docs.4everland.org/get-started/billing-and-pricing/pricing-model):**
- Trial: free for 7 days, 1 GB IPFS, 10 MB Arweave, 50 build minutes, 1 GB bandwidth, no RPC.
- Standard: free monthly after "on-chain identity registration": 6 GB/month IPFS, 100 MB Arweave total, 250 build minutes/month, 10 GB/month bandwidth, 100,000,000 RPC CUs/month at 300 CUPS.
- Pay as you go is priced in LAND at 1 USD = 1,000,000 LAND: bandwidth $0.1/GB, build time $3 per 100 minutes, RPC $1 per 5,000,000 CUs, IPFS storage $0.08/GB/month, Arweave dynamic.

**Chain support:** RPC pages exist for BSC/opBNB, Ethereum, Optimism, Polygon and Taiko; there are domain guides for ENS and Solana Name Service (SNS); no Solana RPC, Base or Robinhood Chain page is listed ([docs llms.txt](https://docs.4everland.org/llms.txt)).

**Versus Cloudflare:** Assessment: the remaining all-in-one IPFS host after Fleek's exit, which is exactly the coupling Shipyard warns against.

**Docs for LLMs:** [docs.4everland.org/llms.txt](https://docs.4everland.org/llms.txt) (13 KB) and [docs.4everland.org/llms-full.txt](https://docs.4everland.org/llms-full.txt) (374 KB, "part 1 of 2", paginated).

### 4.2 RPC and node providers

Cloudflare's Ethereum gateway is the only overlap here; Cloudflare offers no Solana, Base or Robinhood Chain RPC ([Web3 docs](https://developers.cloudflare.com/web3/)).
Every provider in this section is therefore an addition to Cloudflare, not a replacement.
The knowledge base already holds an example of combining the two: a Workers proxy that hides a Helius key (`raw/external/github.com_helius-labs_helius-rpc-proxy.md`, [Helius key-protection guide](https://www.helius.dev/docs/rpc/protect-your-keys)).

#### Helius (Solana)

**Pricing and free tier (as of 2026-10-05), from the [plans page](https://www.helius.dev/docs/billing/plans):**

| Plan | Price | Monthly credits | RPC rate limit |
| --- | --- | --- | --- |
| Free | $0 | 1M | 10 req/s |
| Developer | $49 | 10M | 50 req/s |
| Business | $499 | 100M | 200 req/s |
| Professional | $999 | 200M | 500 req/s |

- LaserStream gRPC is devnet-only on Developer and devnet plus mainnet from Business up; Shred Delivery is $1,000 per month per IP ($800 on Professional) ([plans](https://www.helius.dev/docs/billing/plans)).
- Wallet-as-a-Service costs 200 credits ($0.001) per signature with no per-MAU fee, on paid plans only, in beta ([plans](https://www.helius.dev/docs/billing/plans)).
- The docs also list Helius Sender, Preconfirmations, a Priority Fee API and "Gatekeeper (Beta)" for lower latency ([plans](https://www.helius.dev/docs/billing/plans)).

**Chain support:** Solana only ("Solana's leading infrastructure provider", [helius.dev/llms.txt](https://www.helius.dev/llms.txt)).

**Versus Cloudflare:** no overlap; Cloudflare can front it as a key-hiding proxy.

**Docs for LLMs:** [www.helius.dev/docs/llms.txt](https://www.helius.dev/docs/llms.txt) (34 KB, stamped "last_updated: 2026-10-02"), [www.helius.dev/docs/llms-full.txt](https://www.helius.dev/docs/llms-full.txt) (2.7 MB) and [helius.dev/llms.txt](https://www.helius.dev/llms.txt).

#### Triton One (Solana, Sui, Monad)

**Pricing and free tier (as of 2026-10-05):** sign-up requires a $125 minimum deposit, "prepaid, non-refundable, and valid for 12 months", usable across Solana, Monad and Sui; listed rates include $0.08/GB bandwidth plus $10 per million calls, and dedicated nodes from $450/month ([pricing](https://triton.one/pricing)).
The page's "Is there a free trial?" answer is collapsed and did not render.

**Chain support:** Solana, Sui and Monad; no EVM chains in this owner's set.

**Docs for LLMs:** [docs.triton.one/llms.txt](https://docs.triton.one/llms.txt) (10 KB) and [docs.triton.one/llms-full.txt](https://docs.triton.one/llms-full.txt) (495 KB).

#### Alchemy

**Pricing and free tier (as of 2026-10-05):** Free gives 30M compute units per month with 5 apps and 5 webhooks; Pay As You Go costs $0.525 per 1M CUs with 30 apps and 100 webhooks; Enterprise is custom ([pricing](https://www.alchemy.com/pricing)).

**Chain support:** Solana, Ethereum, Base and Robinhood Chain, with `https://robinhood-mainnet.g.alchemy.com/v2/API_KEY` in Alchemy's own endpoint table ([docs llms-full.txt](https://www.alchemy.com/docs/llms-full.txt)).
Robinhood's docs call Alchemy "the recommended infrastructure provider" for the chain, supplying RPC, Data API and gasless transactions, and the chain's account abstraction "is powered by Alchemy" (resources KB `robinhood-chain/02-connecting.md` and `19-account-abstraction.md`, from [docs.robinhood.com/chain/connecting](https://docs.robinhood.com/chain/connecting)).
Measured in the resources KB: the free tier caps `eth_getLogs` at a 10-block range, serves `eth_subscribe`, and is the only measured provider that served historical state on 4663 (`robinhood-chain/32-explorer-and-data-apis.md` sections 8 and 11).

**Web3 relevance beyond RPC:** Alchemy docs describe agents authenticating "with a crypto wallet instead of an API key, purchasing Alchemy credits in USDC via the x402 payment protocol", and an `alchemy x402 request` CLI command ([docs llms-full.txt](https://www.alchemy.com/docs/llms-full.txt), "Build with AI" and "x402 payments" pages).

**Docs for LLMs:** [www.alchemy.com/docs/llms.txt](https://www.alchemy.com/docs/llms.txt) is a 472-byte stub, [www.alchemy.com/docs/llms-full.txt](https://www.alchemy.com/docs/llms-full.txt) is 11.5 MB, and [www.alchemy.com/llms.txt](https://www.alchemy.com/llms.txt) indexes the marketing site.

#### QuickNode

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://www.quicknode.com/pricing):** a 1-month free trial with 10M API credits and 15 requests per second; $49/month for 80M credits at 50 rps; $249 for 450M credits at 125 rps; $499 for 950M credits at 250 rps.

**x402 RPC:** QuickNode sells RPC paid per request over x402 at $0.001 in USDC or USDG per request, a $0.0001 nanopayment option through Circle Gateway, or credit drawdown at $10 per 1,000,000 credits on mainnet, paid on Base, Polygon, XLayer or Solana ([x402.quicknode.com/llms.txt](https://x402.quicknode.com/llms.txt)).
QuickNode is an x402 Foundation member ([x402.org llms.txt](https://x402.org/llms.txt)) and Google's named migration target for Blockchain Node Engine ([release notes](https://docs.cloud.google.com/blockchain-node-engine/docs/release-notes)).

**Chain support:** Solana, Ethereum, Base and Robinhood Chain ([chains page](https://www.quicknode.com/chains), [Robinhood docs llms.txt](https://www.quicknode.com/docs/robinhood/llms.txt): "Robinhood Chain, an Arbitrum Orbit L2. JSON-RPC and Debug").
The resources KB notes QuickNode is named in Robinhood's docs but has not been measured on 4663 (`robinhood-chain/32-explorer-and-data-apis.md` section 11).

**Docs for LLMs:** [www.quicknode.com/docs/llms.txt](https://www.quicknode.com/docs/llms.txt) (17.5 KB) with a per-chain `llms.txt` for each network, [www.quicknode.com/docs/llms-full.txt](https://www.quicknode.com/docs/llms-full.txt) (494 KB, "key documentation pages", not the whole site) and [www.quicknode.com/llms.txt](https://www.quicknode.com/llms.txt).

#### Infura (MetaMask)

**Pricing and free tier (as of 2026-10-05):** Core Free shows 3 million credits per day at 500 credits per second; Developer is US$50/month for 15 million per day; Team is US$225/month for 75 million per day ([pricing](https://www.infura.io/pricing)).
The same page's FAQ says the Free plan includes 6 million credits per day at 2,000 credits per second (see section 9).

**Chain support:** per-network reference files exist for Ethereum, Base, Arbitrum, Optimism, Polygon PoS, Linea and IPFS ([docs llms.txt](https://docs.infura.io/llms.txt)), and for Solana ([Solana reference](https://docs.infura.io/llms-reference-solana.txt)).
`https://docs.infura.io/llms-reference-robinhood.txt` returns 404 and the networks page does not list Robinhood Chain ([networks](https://www.infura.io/networks)), so Infura does not document 4663.
Infura deprecated its public IPFS API and gateway ([Shipyard blog](https://ipshipyard.com/blog/2026-ipfs-self-hosting-migration)).

**Docs for LLMs:** [docs.infura.io/llms.txt](https://docs.infura.io/llms.txt) (3.6 KB) linking per-topic and per-network files, and [docs.metamask.io/llms.txt](https://docs.metamask.io/llms.txt).

#### Ankr

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://www.ankr.com/rpc/pricing/):** Freemium gives 200M API credits per month; Premium pay as you go starts at $10 per 100M credits (about 500K requests); Deal plans run $500 to $3,000 per month with 20% extra credits; RPC costs $0.02 per 1,000 EVM requests and $0.05 per 1,000 Solana requests.

**Chain support:** Solana, Ethereum, Base and Robinhood Chain, with Robinhood API pages for `eth`, `debug`, `web3` and `net` methods ([docs llms.txt](https://www.ankr.com/docs/llms.txt), [Robinhood page](https://www.ankr.com/docs/rpc-service/chains/chains-api/robinhood/index.md)).

**Docs for LLMs:** [www.ankr.com/docs/llms.txt](https://www.ankr.com/docs/llms.txt) (73 KB), [www.ankr.com/docs/llms-full.txt](https://www.ankr.com/docs/llms-full.txt) (9.6 MB, 645 pages) and [www.ankr.com/llms.txt](https://www.ankr.com/llms.txt).

#### dRPC

**Pricing and free tier (as of 2026-10-05):** Free gives 210M CU per month at 100 requests per second; Growth is pay as you go at $6 per 1M requests and 5K rps, with "no monthly limits, overage fees or expiration on requests" ([pricing](https://drpc.org/pricing)).

**Chain support:** Solana, Ethereum, Base and Robinhood Chain appear in the [chainlist](https://drpc.org/chainlist).
Measured in the resources KB on 4663: the free plan caps `eth_getLogs` at 101 blocks per request, refuses JSON-RPC batches of more than 3, serves `eth_subscribe` for `newHeads` and `logs`, does not serve historical state 3.5 million blocks back, and pulled 724,750 blocks of logs in 3.53 minutes for free (`robinhood-chain/32-explorer-and-data-apis.md` sections 8 and 11, `52-swap-throughput-and-head-following.md`).

**Docs for LLMs:** [drpc.org/llms.txt](https://drpc.org/llms.txt) (3.6 KB) and [drpc.org/llms-full.txt](https://drpc.org/llms-full.txt) (8 KB, a guide rather than full docs); `drpc.org/docs/llms.txt` returns 404.

#### Chainstack

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://chainstack.com/pricing/):**

| Plan | Price | Request units/month | RPS | Extra per 1M RUs |
| --- | --- | --- | --- | --- |
| Developer | Free | 3M | 25 | $20 |
| Growth | $49/month | 20M | 250 | $15 |
| Pro | $199/month | 80M | 400 | $12.5 |
| Business | not captured | 200M | 600 | $10 |
| Enterprise | custom | 400M | unlimited | $5 |

- The Developer plan lists "Pay in Crypto" ([pricing](https://chainstack.com/pricing/)).

**Chain support:** Solana, Ethereum, Base and Robinhood Chain on both networks; Chainstack's Robinhood nodes "serve the Geth-style `debug_*` namespace" including `debug_traceTransaction` and `debug_traceBlockByNumber`, and Chainstack Self-Hosted supports Robinhood Chain ([docs llms-full.txt](https://docs.chainstack.com/llms-full.txt), [announcement](https://chainstack.com/chainstack-introduces-robinhood-chain-support/)).
This matters because the resources KB found that the Robinhood public endpoint has no debug or trace and Alchemy's free tier refuses `debug_traceBlockByNumber` (`robinhood-chain/32-explorer-and-data-apis.md`, `53-launch-sources-measured.md`).

**Docs for LLMs:** [docs.chainstack.com/llms.txt](https://docs.chainstack.com/llms.txt) (1.6 KB), [docs.chainstack.com/llms-full.txt](https://docs.chainstack.com/llms-full.txt) (9.7 MB) and [chainstack.com/llms.txt](https://chainstack.com/llms.txt) (122 KB, blog and marketing).

### 4.3 Wallet and payments infrastructure

Cloudflare's overlap here is Cloudflare Wallets (handle reservation only so far) and x402 and MPP support in the Agents SDK ([Wallets](https://developers.cloudflare.com/wallets/), [Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)).
The x402 protocol itself supports "any EVM chain" as `eip155:<chainId>`, with ERC-20 transfers through EIP-3009 or Permit2 ([network and token support](https://docs.x402.org/core-concepts/network-and-token-support)).

#### Coinbase Developer Platform (CDP) and its x402 facilitator

**Pricing and free tier (as of 2026-10-05):**
- Wallets: each wallet operation costs $0.005, the first 5,000 per month are free, and read operations are not billed; sending a transaction counts as 2 operations ([wallet pricing](https://docs.cdp.coinbase.com/wallets/pricing)).
- x402 facilitator: up to 1,000 onchain transactions per month free, then $0.001 each; "payment verification is always free" ([CDP facilitator](https://docs.cdp.coinbase.com/x402/network-support)).
- The facilitator billing started "as of January 1st" and enforces a $0.001 minimum payment ([CDP changelog](https://docs.cdp.coinbase.com/get-started/changelog)).
- CDP Node: 10 million billing units free per month, then $0.50 per million, at about 50 requests per second ([node overview](https://docs.cdp.coinbase.com/data/node/overview)).

**Chain support:** the CDP facilitator supports Base, Base Sepolia, Polygon, Arbitrum, World, World Sepolia, Solana and Solana Devnet ([CDP facilitator](https://docs.cdp.coinbase.com/x402/network-support)).
CDP says its facilitator "has processed more than 100 million transactions and $28 million in payment volume across Base and Solana alone" ([CDP facilitator](https://docs.cdp.coinbase.com/x402/network-support)).
Robinhood Chain does not appear in CDP's 11.5 MB `llms-full.txt` except as the exchange counterparty "Robinhood Crypto, LLC" (grep 2026-10-05).
CDP non-custodial accounts "are network-agnostic. The same address works on any EVM network", with the network chosen when sending ([CDP MCP page](https://docs.cdp.coinbase.com/ai-agents/cdp-for-agents/cdp-mcp)).

**Docs for LLMs:** [docs.cdp.coinbase.com/llms.txt](https://docs.cdp.coinbase.com/llms.txt) (59 KB) and [docs.cdp.coinbase.com/llms-full.txt](https://docs.cdp.coinbase.com/llms-full.txt) (11.5 MB, including exchange and Deribit API references).

#### Other x402 facilitators

The x402 docs list production facilitators including Dexter ("free public x402 facilitator across Solana and EVM chains with no fees and no account required"), PayAI ("multi-network ... No API keys required"), Corbits (EVM and Solana), Fireblocks, Solvador, Mogami (Base), Polygon, Celo, Stellar, NEAR, XRPL and Canton facilitators ([facilitators](https://docs.x402.org/dev-tools/facilitators)).
None of the listed facilitators names Robinhood Chain in its description ([facilitators](https://docs.x402.org/dev-tools/facilitators)).
The default-asset table for dollar-string pricing covers Base, Ethereum, Avalanche, Polygon, Arbitrum, Monad and others but not 4663 ([network and token support](https://docs.x402.org/core-concepts/network-and-token-support)).
Permit2 is deployed on Robinhood Chain at the canonical `0x000000000022D473030F116dDEE9F6B43aC78BA3` (resources KB `uniswap/DEPLOYMENTS.md`), so the protocol's Permit2 path is available there in principle.
Third-party trackers put Daydreams and Coinbase's facilitators at the top by cumulative transactions ([web3trackers, third-party](https://www.web3trackers.com/x402-dashboard)).

**Docs for LLMs:** [docs.x402.org/llms.txt](https://docs.x402.org/llms.txt) (6.3 KB, per-page `.md` links), [x402.org/llms.txt](https://x402.org/llms.txt), and an older [x402.gitbook.io/x402/llms.txt](https://x402.gitbook.io/x402/llms.txt).

#### Privy

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://www.privy.io/pricing):**
- Developer: free up to 500 MAU, with "50K signatures and $1M transaction volume for free every month".
- Core: $299/month up to 2,500 MAU; Scale: $499/month for 2,500 to 9,999 MAU; Enterprise is custom, with signature pricing "as low as $0.001/signature".
- If a subscription is cancelled, access is limited to 500 MAU and new sign-ups stop once an app is past that.
- A third party reports Privy was acquired by Stripe in June 2025 ([Openfort, third-party](https://www.openfort.io/blog/privy-vs-turnkey)); Stripe is also listed as an x402 Foundation member ([x402.org llms.txt](https://x402.org/llms.txt)).

**Chain support:** Privy's docs list Robinhood Chain as chain 4663 (`eip155:4663`) and Robinhood Testnet as 46630, and include `robinhood`, `solana` and `base` among supported mainnets ([fetch balance](https://docs.privy.io/wallets/gas-and-asset-management/assets/fetch-balance), [swap](https://docs.privy.io/financial-flows/swap)).
Privy also publishes a recipe for a robo-advisor agent trading on Robinhood Chain ([docs llms.txt](https://docs.privy.io/llms.txt)).
Robinhood's own docs list Privy as an account abstraction provider (resources KB `robinhood-chain/19-account-abstraction.md`).

**Docs for LLMs:** [docs.privy.io/llms.txt](https://docs.privy.io/llms.txt) (58 KB) and [docs.privy.io/llms-full.txt](https://docs.privy.io/llms-full.txt) (4.5 MB).

#### Dynamic

**Pricing and free tier (as of 2026-10-05):** free up to 1,000 MAU; a $249/month plan with "additional $0.05 per MAU"; "Dynamic was acquired by Fireblocks in October 2025" ([pricing](https://www.dynamic.xyz/pricing)).

**Chain support:** Tier 1 chains, with send, sign, gasless, on-chain events and delegated access, are "EVM (all EVM networks)" and Solana, plus Bitcoin, Sui, Tempo, Arc, TON, Stellar, Tron, Aleo and Midnight with narrower feature sets ([chain support](https://www.dynamic.xyz/docs/embedded-wallets/chains/overview.md)).
The on-chain events page lists Base, Robinhood Chain (mainnet and testnet) and Solana by name ([on-chain events](https://www.dynamic.xyz/docs/embedded-wallets/on-chain-events.md)).
Robinhood's docs list Dynamic as an account abstraction provider (resources KB `robinhood-chain/19-account-abstraction.md`).

**Docs for LLMs:** [www.dynamic.xyz/docs/llms.txt](https://www.dynamic.xyz/docs/llms.txt) (4.6 KB) routes to a separate `llms.txt` per section and SDK; its `llms-full.txt` is also only an index (4.5 KB), so mirroring needs one fetch per section file.

#### Crossmint

**Pricing and free tier (as of 2026-10-05):** "Free 1,000 Monthly Active Wallets. Overages start at $0.025 per MAU", while the same page lists smart wallets as "Starts at $0.02 per MAW", treasury and pre-generation actions from $0.01 per action, and tokenization uploads at $0.002 each ([pricing](https://www.crossmint.com/pricing)).
Crossmint Europe is authorised by Spain's CNMV as a crypto-asset service provider under MiCA ([pricing](https://www.crossmint.com/pricing)).

**Chain support:** Base and Solana are self-serve for Wallets, Checkout, Onramp and Tokenization; Ethereum wallets and all four Robinhood Chain products are marked "Available, but not self-serve. Contact us", with labels `robinhood-chain` and `robinhood-chain-testnet` ([supported chains](https://docs.crossmint.com/introduction/supported-chains)).

**Docs for LLMs:** [docs.crossmint.com/llms.txt](https://docs.crossmint.com/llms.txt) (70 KB) and [docs.crossmint.com/llms-full.txt](https://docs.crossmint.com/llms-full.txt) (4.2 MB).

#### Turnkey

**Pricing and free tier (as of 2026-10-05), from the [pricing page](https://www.turnkey.com/pricing):** free to start with up to 1k wallets and 25 free signatures per month, then $0.10 per signature; a $99/month plan at $0.05 per signature with up to 2k free wallets; enterprise "as low as $0.0015 / signature".

**Chain support:** Turnkey's balances webhooks list Ethereum, Base, Solana and Robinhood Chain (`eip155:4663`, 10 confirmations) plus Robinhood Chain Testnet (`eip155:46630`) ([balances](https://docs.turnkey.com/features/transaction-management/balances)), and Turnkey announced Robinhood Chain support on its blog ([Turnkey blog](https://www.turnkey.com/blog/robinhood-chain-support)).

**Docs for LLMs:** [docs.turnkey.com/llms.txt](https://docs.turnkey.com/llms.txt) (3.9 KB, with agent instructions) and [docs.turnkey.com/llms-full.txt](https://docs.turnkey.com/llms-full.txt) (4.6 MB).

## 5. Robinhood Chain (4663) support matrix

Robinhood's own docs name Alchemy as the recommended provider, give a QuickNode endpoint pattern, and also list Blockdaemon, dRPC and Validation Cloud; account abstraction lists Alchemy, ZeroDev, Privy and Dynamic (resources KB `ROBINHOOD-CHAIN.md` section 2 and `robinhood-chain/19-account-abstraction.md`).
"Documented" below means the provider's own docs or pages name the chain; "Measured" means the resources KB tested it.

| Provider | Category | 4663 status | Evidence |
| --- | --- | --- | --- |
| Alchemy | RPC, AA, data | Documented and measured | Alchemy endpoint table; Robinhood docs; resources KB file 32 |
| dRPC | RPC | Documented and measured | [chainlist](https://drpc.org/chainlist); resources KB files 32 and 52 |
| QuickNode | RPC | Documented, not measured | [Robinhood llms.txt](https://www.quicknode.com/docs/robinhood/llms.txt); Robinhood docs |
| Ankr | RPC | Documented, not measured | [Robinhood API page](https://www.ankr.com/docs/rpc-service/chains/chains-api/robinhood/index.md) |
| Chainstack | RPC, debug and trace, dedicated, self-hosted | Documented, not measured | [announcement](https://chainstack.com/chainstack-introduces-robinhood-chain-support/), docs llms-full |
| Infura | RPC | Not documented | 404 on `llms-reference-robinhood.txt`; absent from [networks](https://www.infura.io/networks) |
| Helius, Triton | RPC | Not applicable (non-EVM focus) | [Helius](https://www.helius.dev/llms.txt), [Triton](https://triton.one/pricing) |
| 4EVERLAND | RPC | Not documented | [docs llms.txt](https://docs.4everland.org/llms.txt) |
| Privy | Embedded wallets | Documented | [fetch balance](https://docs.privy.io/wallets/gas-and-asset-management/assets/fetch-balance) |
| Turnkey | Signing, wallets | Documented | [balances](https://docs.turnkey.com/features/transaction-management/balances) |
| Dynamic | Embedded wallets | Documented ("all EVM networks"; named in on-chain events) | [chain support](https://www.dynamic.xyz/docs/embedded-wallets/chains/overview.md) |
| Crossmint | Wallets, checkout | Not self-serve | [supported chains](https://docs.crossmint.com/introduction/supported-chains) |
| Coinbase CDP | Wallets, facilitator | Not documented (EVM accounts are network-agnostic) | [CDP facilitator](https://docs.cdp.coinbase.com/x402/network-support) |
| x402 facilitators | Payments | None names 4663 | [facilitators](https://docs.x402.org/dev-tools/facilitators) |

Third-party roundups also name Dwellir, Blockdaemon, Validation Cloud, GetBlock, Goldsky, Tenderly, thirdweb and RouteMesh as Robinhood Chain RPC sources ([Chainstack roundup](https://chainstack.com/learn/compare/top-6-robinhood-chain-rpc-providers-in-2026), [Dwellir](https://www.dwellir.com/blog/best-robinhood-chain-rpc-providers), [QuickNode guide](https://www.quicknode.com/builders-guide/best/top-10-robinhood-chain-rpc-providers)); none of these were checked against the providers' own docs here.

## 6. Docs mirrorability: llms.txt per platform

All rows were probed on 2026-10-05; the raw results are in `raw/alternatives/llms-probe.tsv`.
"Full" means a single-file `llms-full.txt` exists; sizes are bytes as downloaded.

| Platform | llms.txt | Full file | Notes |
| --- | --- | --- | --- |
| Vercel | [vercel.com/docs/llms.txt](https://vercel.com/docs/llms.txt) | Yes, 10.3 MB | `vercel.com/llms-full.txt` is an HTML page; use the `/docs/` path |
| Netlify | [docs.netlify.com/llms.txt](https://docs.netlify.com/llms.txt) | No (404) | 25 KB index |
| Fastly | [fastly.com/documentation/llms.txt](https://www.fastly.com/documentation/llms.txt) | No (404) | Also at `docs.fastly.com` |
| Akamai | [techdocs.akamai.com/llms.txt](https://techdocs.akamai.com/llms.txt) | No | Nested `llms.txt` per product and section |
| Akamai Cloud (Linode) | [techdocs.akamai.com/cloud-computing/llms.txt](https://techdocs.akamai.com/cloud-computing/llms.txt) | No | `linode.com/llms.txt` returns 403 |
| Deno | [docs.deno.com/llms.txt](https://docs.deno.com/llms.txt) | Yes, 2.5 MB | |
| Fly.io | [docs.fly.io/llms.txt](https://docs.fly.io/llms.txt) | Yes, 2.9 MB | |
| Railway | [docs.railway.com/llms.txt](https://docs.railway.com/llms.txt) | Yes, 2.6 MB | |
| Render | [render.com/docs/llms.txt](https://render.com/docs/llms.txt) | Yes, 1.1 MB | Regenerated daily |
| AWS | [docs.aws.amazon.com/llms.txt](https://docs.aws.amazon.com/llms.txt) | No single file | 418 KB root plus per-guide files |
| Google Cloud | None | No | Only [Firebase](https://firebase.google.com/docs/llms.txt), 1.8 MB index |
| Azure | None | No | Four candidate URLs returned 404 |
| Bunny.net | [bunny.net/docs/llms.txt](https://bunny.net/docs/llms.txt) | Yes, 1.7 MB | |
| Supabase | [supabase.com/llms.txt](https://supabase.com/llms.txt) | Yes, 7.2 MB | |
| Convex | [docs.convex.dev/llms.txt](https://docs.convex.dev/llms.txt) | Yes, 2.6 MB | |
| Puter | [docs.puter.com/llms.txt](https://docs.puter.com/llms.txt) | Not probed | |
| Northflank | [northflank.com/docs/llms.txt](https://northflank.com/docs/llms.txt) | Not probed | |
| Fleek | None | No | Product gone |
| Pinata | [docs.pinata.cloud/llms.txt](https://docs.pinata.cloud/llms.txt) | Yes, 717 KB | |
| Fil One (Storacha) | [fil.one/llms.txt](https://www.fil.one/llms.txt) | Yes, 10 KB | Storacha URLs redirect here |
| AR.IO | [docs.ar.io/llms.txt](https://docs.ar.io/llms.txt) | Yes, 1.3 MB | Plus `SKILL.md` and per-SDK `llm.txt` |
| Akash | [akash.network/llms.txt](https://akash.network/llms.txt) | Yes, 50 KB | A curated reference, not every page |
| Spheron | [docs.spheron.ai/llms.txt](https://docs.spheron.ai/llms.txt) | No (404) | |
| 4EVERLAND | [docs.4everland.org/llms.txt](https://docs.4everland.org/llms.txt) | Yes, 374 KB | Paginated, part 1 of 2 |
| Helius | [helius.dev/docs/llms.txt](https://www.helius.dev/docs/llms.txt) | Yes, 2.7 MB | |
| Triton One | [docs.triton.one/llms.txt](https://docs.triton.one/llms.txt) | Yes, 495 KB | |
| Alchemy | [alchemy.com/docs/llms.txt](https://www.alchemy.com/docs/llms.txt) | Yes, 11.5 MB | The `llms.txt` is a 472-byte stub |
| QuickNode | [quicknode.com/docs/llms.txt](https://www.quicknode.com/docs/llms.txt) | Partial, 494 KB | Per-chain `llms.txt` files |
| Infura | [docs.infura.io/llms.txt](https://docs.infura.io/llms.txt) | Per topic | Per-network and per-topic full files |
| Ankr | [ankr.com/docs/llms.txt](https://www.ankr.com/docs/llms.txt) | Yes, 9.6 MB | |
| dRPC | [drpc.org/llms.txt](https://drpc.org/llms.txt) | 8 KB guide | No full docs file |
| Chainstack | [docs.chainstack.com/llms.txt](https://docs.chainstack.com/llms.txt) | Yes, 9.7 MB | |
| Coinbase CDP | [docs.cdp.coinbase.com/llms.txt](https://docs.cdp.coinbase.com/llms.txt) | Yes, 11.5 MB | Includes exchange APIs; filter on mirror |
| x402 | [docs.x402.org/llms.txt](https://docs.x402.org/llms.txt) | No; per-page `.md` | Small enough to mirror page by page |
| Privy | [docs.privy.io/llms.txt](https://docs.privy.io/llms.txt) | Yes, 4.5 MB | |
| Dynamic | [dynamic.xyz/docs/llms.txt](https://www.dynamic.xyz/docs/llms.txt) | Index only | One `llms.txt` per section |
| Crossmint | [docs.crossmint.com/llms.txt](https://docs.crossmint.com/llms.txt) | Yes, 4.2 MB | |
| Turnkey | [docs.turnkey.com/llms.txt](https://docs.turnkey.com/llms.txt) | Yes, 4.6 MB | |

The `llms.txt` indexes of Pinata, Privy, Crossmint, Turnkey, CDP, x402 and Dynamic link each page as Markdown at `<page-url>.md`, the same method the resources KB used for the Uniswap archive.

## 7. Cloudflare product -> best alternative(s)

This mapping is this document's synthesis of sections 3 and 4; each named product is sourced there.

| Cloudflare product | Best alternative(s) | Why, in one line |
| --- | --- | --- |
| Workers | Deno Deploy; Fastly Compute; Vercel Functions | Closest isolate or Wasm edge runtimes with published free tiers (Fastly's disputed) |
| Pages / Workers static assets | Vercel; Netlify; Render static sites; AR.IO for permanent frontends | Git-push hosting; AR.IO for sites that outlive the host |
| Durable Objects | Convex; a Fly.io or Railway container | No direct isolate-with-storage equivalent; Convex covers real-time state |
| Workers KV | Deno KV; Fastly KV Store | Edge key-value stores on the matching runtimes |
| D1 | Supabase Postgres; Convex | Managed databases with free tiers |
| R2 | Fil One; Railway Object Storage; Bunny Storage; Fastly Object Storage | All advertise free or no egress |
| Queues / Workflows | Vercel Queues and Workflows | Same product shape in one platform |
| Containers / Sandbox | Fly.io; Railway; Render; Cloud Run; Akash | Long-running processes for bots, indexers and stream consumers |
| Workers AI | Akash (AkashML or GPUs); Spheron GPUs | Cheaper raw GPU capacity |
| AI Gateway | Vercel AI Gateway; Netlify AI Gateway; Puter | Model routing on other edges |
| CDN and cache | Bunny.net; CloudFront flat-rate plans; Fastly | Bunny for price, CloudFront for a free plan with WAF |
| DNS | CloudFront plans (include DNS); Bunny DNS | Bundled with the CDN plans |
| WAF, DDoS, bot management | CloudFront plans; Vercel Firewall and BotID; Fastly Next-Gen WAF | Bundled security on other edges |
| Turnstile | None found in this survey | No surveyed platform documents a CAPTCHA alternative |
| Web3 IPFS gateway | Pinata dedicated gateways; AR.IO gateways for Arweave | Pin and serve, not only read |
| Web3 Ethereum gateway | Alchemy; QuickNode; dRPC; Chainstack; Ankr | Full RPC across Ethereum, Base and 4663 |
| (no Cloudflare product) Solana RPC | Helius; Triton; Alchemy; QuickNode | Cloudflare has none |
| Wallets / agent payments (x402) | Coinbase CDP wallets and facilitator; Privy; Turnkey; QuickNode x402 RPC | Cloudflare Wallets cannot hold funds yet |
| Hyperdrive | No alternative needed; pair with Supabase | Hyperdrive fronts an external Postgres |

## 8. Recommendations for the owner's use cases

Everything in this section is a recommendation, not a sourced fact; the facts it rests on are cited in the sections above.

### 8.1 What to combine with Cloudflare

1. **Keep Cloudflare as the edge, API and agent layer** (Workers, Durable Objects, R2, Queues, the Agents SDK) and add chain providers behind it, because no surveyed platform covers both, and Cloudflare's free static-asset requests and zero-egress R2 suit dapp frontends and indexer output.
2. **Solana RPC: Helius first, Triton second.**
   Helius has a free tier, LaserStream and Sender for trading UIs and bots, and a documented Workers key-hiding proxy; Triton needs a $125 prepaid deposit but is a reasonable failover for the same use.
3. **EVM RPC including Robinhood Chain: Alchemy as primary, dRPC as the free bulk-log and subscription fallback, Chainstack when you need `debug_*` or `trace` on 4663.**
   Alchemy is Robinhood's recommended provider and the only one measured serving historical state; dRPC's free plan already proved itself for wide log scans; Chainstack documents debug and trace on 4663, which neither the public endpoint nor Alchemy's free tier serves.
4. **Agent-paid RPC: QuickNode's x402 endpoint** for AI agents that should pay per call in USDC or USDG instead of holding an API key.
5. **Embedded wallets: Privy or Turnkey for apps that span Solana, Base and Robinhood Chain.**
   Both document 4663 by chain id; choose Privy for bundled auth plus wallets with a 500-MAU free tier, Turnkey for raw signing with per-signature pricing.
   Dynamic is a third option, whose free tier is larger (1,000 MAU).
   Avoid Crossmint for 4663 unless sales enables it.
6. **x402 selling: CDP facilitator on Base and Solana.**
   For Robinhood Chain, plan on running your own facilitator over the Permit2 path (Permit2 is deployed on 4663) until a hosted facilitator names the chain; verify first whether USDG implements EIP-3009.
7. **Permanent or censorship-resistant launchpad frontends: build the CAR in CI, pin on Pinata, publish to Arweave through AR.IO Turbo, and keep the domain and HTTP copy on Cloudflare.**
   This follows Shipyard's post-Fleek advice and avoids depending on a single all-in-one host such as 4EVERLAND.
8. **Long-running bots and stream consumers: Fly.io or Railway containers** if Cloudflare Containers or Durable Objects do not fit; avoid Render's free instances, which sleep after 15 minutes.
9. **Do not adopt** Fleek (gone), Google Cloud Blockchain RPC or Node Engine (shuts down 2026-12-15), or Amazon Managed Blockchain (no new customers from 2026-10-29).
10. **Supabase** is worth adding only if you want Postgres plus wallet sign-in for Ethereum and Solana without writing SIWE yourself; reach it from Workers through Hyperdrive.

### 8.2 Which to scrape next into a knowledge base, in priority order

1. **Helius** ([llms-full.txt](https://www.helius.dev/docs/llms-full.txt), 2.7 MB).
   It is the Solana backbone for trading UIs, bots and indexers, and it is one clean file.
   Check first whether the jupiter-meteora knowledge base already holds it; if not, Helius belongs there, since it is Solana-specific.
2. **Alchemy** ([llms-full.txt](https://www.alchemy.com/docs/llms-full.txt), 11.5 MB).
   It is the recommended Robinhood Chain provider and covers Ethereum, Base and Solana, plus smart wallets and gas sponsorship.
   Filter to the chains in use; the Robinhood-specific findings belong in the resources knowledge base.
3. **Coinbase CDP and the x402 docs** ([CDP llms-full.txt](https://docs.cdp.coinbase.com/llms-full.txt), 11.5 MB; [docs.x402.org](https://docs.x402.org/llms.txt) page by page).
   They define how payments, the facilitator and server wallets work, which directly complements the Cloudflare x402 and Wallets material already here.
   Drop the exchange, Prime and Deribit sections when mirroring.
4. **Privy** ([llms-full.txt](https://docs.privy.io/llms-full.txt), 4.5 MB).
   It is the embedded-wallet provider with explicit Solana, Base and 4663 coverage and an agent recipe on Robinhood Chain.
5. **Turnkey** ([llms-full.txt](https://docs.turnkey.com/llms-full.txt), 4.6 MB).
   It is the signing layer for server-side bots and agents across the same chains.
6. **QuickNode** ([docs llms.txt](https://www.quicknode.com/docs/llms.txt) plus the Solana, Base, Ethereum and Robinhood per-chain files, and [x402 llms.txt](https://x402.quicknode.com/llms.txt)).
   Its llms-full is only a subset, so mirror per chain.
7. **Chainstack** ([llms-full.txt](https://docs.chainstack.com/llms-full.txt), 9.7 MB), filtered to Robinhood Chain and Solana, for the debug and trace methods.
8. **AR.IO** ([llms-full.txt](https://docs.ar.io/llms-full.txt), 1.3 MB) and **Pinata** ([llms-full.txt](https://docs.pinata.cloud/llms-full.txt), 717 KB), together, for permanent and IPFS frontends.
9. **Supabase** or **Vercel** only if one becomes part of the stack; both are large (7.2 MB and 10.3 MB) and mostly non-Web3.

## 9. Gaps and contradictions

### 9.1 Contradictions between sources

- **Fastly free tier.**
  Fastly's docs say it provides "a monthly free tier of services for many Network Services and Compute products" ([account types](https://www.fastly.com/documentation/guides/organizations-and-accounts/billing/account-types)), while third parties say there is "No permanent free tier" and only a $50 trial credit ([BlazingCDN](https://blog.blazingcdn.com/en-us/fastly-cdn-pricing-tiers-explained), [Vendr](https://www.vendr.com/marketplace/fastly), [costbench](https://costbench.com/software/cdn-edge/fastly/free-plan)).
  The docs also say the $50 Compute trial applies only to accounts created before 2026-03-31, which may explain the difference.
- **Infura free plan.**
  The [pricing page](https://www.infura.io/pricing) shows 3 million credits per day at 500 credits per second in the plan card, and 6 million credits per day at 2,000 credits per second in its own FAQ.
- **Crossmint overage.**
  The [pricing page](https://www.crossmint.com/pricing) says overages "start at $0.025 per MAU" and also that smart wallets start "at $0.02 per MAW".
- **Netlify Pro credits.**
  The earlier credit-plan changelog lists Pro at 5,000 credits for $20 per member per month ([changelog](https://www.netlify.com/changelog/netlify-pricing-update-introducing-credit-based-plans)); the current [pricing page](https://www.netlify.com/pricing/) shows Pro at $20/month with unlimited members starting at 3,000 credits.
  The 2026-04-14 changelog changed seats and credit rates in between.
- **Deno Deploy free tier.**
  A third party says the free plan includes 100 GB bandwidth and 50 ms CPU per request ([srvrlss.io](https://www.srvrlss.io/provider/deno-deploy)); the official [pricing page](https://deno.com/deploy/pricing) says 20 GiB egress and 10 hours of active CPU.
  Another third party gives Builder 20M requests where the official page says 25M ([rfp.wiki](https://www.rfp.wiki/cloud-computing/serverless-computing-function-as-a-service/deno-deploy/vercel)).
- **AWS Amplify free period.**
  The [Amplify pricing page](https://aws.amazon.com/amplify/pricing/) says "Free for 12 months", while the [AWS Free Tier page](https://aws.amazon.com/free/) describes a Free plan of up to $200 credit that closes after 6 months, and the Amplify page itself says new customers since 2025-07-15 get the credit model.
- **Storacha.**
  A May 2026 third-party write-up lists Storacha tiers of Free 5 GB, Starter $10 and Pro $100 ([Blockcritics](https://blockcritics.com/blog/2026/05/07/storacha-network-protocol-labs-play-for-hot-decentralized-storage-at-scale)); on 2026-10-05 Storacha's domains redirect to Fil One at a flat $5.99/TB/month with a 30-day trial ([Fil One](https://www.fil.one/llms-full.txt)).
  The relationship between Storacha, Storacha Forge and Fil One is not stated on any page read.
- **4EVERLAND bandwidth.**
  A search snippet of [4everland.org/price](https://www.4everland.org/price) lists 0 to 100 GB of bandwidth free per month, while the [docs pricing model](https://docs.4everland.org/get-started/billing-and-pricing/pricing-model) gives 10 GB/month on the free Standard package.
  The URL `www.4everland.org/pricing/` returned 404 on 2026-10-05.
- **Spheron entry price.**
  The docs say GPUs "from $0.72/hr" ([docs llms.txt](https://docs.spheron.ai/llms.txt)), a third party quotes "from $0.58 per GPU-hour" ([gpufind](https://www.gpufind.cloud/providers/spheron/review)), and a pricing-page snippet gives H100 from $2.65/hr ([pricing](https://www.spheron.network/pricing)).
- **Privy billing unit.**
  Privy's [pricing page](https://www.privy.io/pricing) tiers by MAU plus signatures, while a third-party plan catalog says Privy "is sold by monthly active wallets (MAW)" ([apis.io](https://apis.io/plans/privy/privy-plans-pricing)).
- **dRPC getLogs error text.**
  The resources KB records that dRPC's free plan serves at most 101 blocks per `eth_getLogs` while the error message itself says "ranges over 10000 blocks are not supported on free plan" (`robinhood-chain/32-explorer-and-data-apis.md` section 8); the measured limit, not the message, is what applies.

### 9.2 Gaps

- **Pages that did not render through the reader:** Fastly's pricing page (image only), the Coinbase CDP pricing page (navigation only; CDP prices here come from its docs), Azure per-unit prices (script-rendered "$-"), the Linode plan table, Chainstack's Business plan price, and Triton's free-trial answer.
- **Unpublished pricing:** Akamai EdgeWorkers and Akamai Functions list prices; Bunny Database pricing was not found in the docs.
- **Robinhood Chain support is docs-only** for QuickNode, Ankr, Chainstack, Privy, Turnkey and Dynamic; none was tested live on 4663 for this document.
  Only Alchemy and dRPC have measurements, in the resources KB.
- **No hosted x402 facilitator for 4663** was found, and whether Robinhood Chain's USDG implements EIP-3009 `transferWithAuthorization` was not checked; QuickNode accepting USDG for x402 RPC does not say on which chain.
- **Fleek's new product** is unannounced; `fleek.sh` only says "We've been building something new".
- **Google Cloud and Azure** publish no `llms.txt`; whether Microsoft Learn's MCP server or Google's developer knowledge API could substitute was not checked.
- **Free tiers were read, not exercised**: no account was created on any platform, so limits such as Vercel's Hobby pause behaviour come from pages, not tests.
- **Helius and Triton** were not checked for any EVM product; both describe themselves as Solana-first.
- **Newer entrants:** only Puter and Northflank surfaced; the searches may have missed 2026 launches that did not rank for "Cloudflare alternatives".
- **Raw captures:** `raw/alternatives/pages/` holds about 91 MB, mostly `llms-full.txt` files kept as evidence for the citations above; they are not a maintained mirror and should be refreshed before reuse.
