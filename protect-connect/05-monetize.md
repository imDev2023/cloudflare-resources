# Monetize: Monetization Gateway, x402 and Cloudflare's payment rails

Snapshot as of 2026-10-05.
The Protect & Connect > Monetize dropdown holds one product, the Monetization Gateway, which lets a seller put an HTTP 402 paywall in front of any proxied hostname (APIs, MCP tools, web pages, datasets) and get paid per request through the x402 protocol, with Cloudflare doing verification and settlement at the edge.
As of 2026-10-05 it is in closed beta (opened 2026-09-30), restricted to United States sellers and buyers, and per the beta blog it settles in USDC on the Base blockchain through Coinbase's x402 Facilitator; the developer docs themselves never name a chain or token, they only say "CAIP-2 network" and "atomic units" where one unit equals $0.000001.
Prices run from $0.001 to $100 per request, with a fixed (`exact`) scheme and a variable (`upto`) scheme where the origin reports the actual charge, and the beta API adds a third `origin_controlled` scheme the docs do not mention.
This file also covers the pieces around it that the sources tie together: the x402 protocol and x402 Foundation, the do-it-yourself x402 tooling in the Agents SDK (Worker proxy, `paidTool`, `withX402Client`), the Machine Payments Protocol, AI Gateway Machine Payments (the first Cloudflare product sold through the gateway), Pay Per Crawl, Cloudflare Wallets, the NET Dollar stablecoin announcement, and paying Cloudflare's own bills in USDC.

## Table of contents

1. [Where Monetize sits in the docs](#1-where-monetize-sits-in-the-docs)
2. [Timeline and status](#2-timeline-and-status)
3. [Monetization Gateway](#3-monetization-gateway)
   - 3.1 What it is
   - 3.2 Eligibility
   - 3.3 Supported chains, tokens and facilitators
   - 3.4 The HTTP 402 / x402 v2 request flow
   - 3.5 Origin payment validation (`PAYMENT-CONTEXT`, `PAYMENT-SETTLEMENT`)
   - 3.6 Monetization rules (schemes, prices, audiences, conditions)
   - 3.7 Dashboard setup
   - 3.8 API (beta) and Terraform
   - 3.9 Limits and pricing
   - 3.10 Customers in production
   - 3.11 Most useful pages
4. [The x402 protocol as Cloudflare documents it](#4-the-x402-protocol-as-cloudflare-documents-it)
5. [Do-it-yourself x402 on Workers and the Agents SDK](#5-do-it-yourself-x402-on-workers-and-the-agents-sdk)
6. [Machine Payments Protocol (MPP)](#6-machine-payments-protocol-mpp)
7. [AI Gateway Machine Payments](#7-ai-gateway-machine-payments)
8. [Adjacent products: Pay Per Crawl, Wallets, NET Dollar, stablecoin billing](#8-adjacent-products-pay-per-crawl-wallets-net-dollar-stablecoin-billing)
9. [Comparison: which payment path to use](#9-comparison-which-payment-path-to-use)
10. [Build hooks for Web3 projects](#10-build-hooks-for-web3-projects)
11. [Gaps and contradictions](#11-gaps-and-contradictions)
12. [Sources](#12-sources)

---

## 1. Where Monetize sits in the docs

The home sidebar (`raw/nav/home-sidebar.md`) has a top-level "Monetize" group with a single entry, Monetization Gateway, at https://developers.cloudflare.com/monetization-gateway/.
The root `llms.txt` describes it as "Define monetization policies to charge any visitor accessing APIs, MCP tools, web pages, or datasets" (https://developers.cloudflare.com/monetization-gateway/llms.txt).
The product has only seven doc pages, all "Last updated Sep 30, 2026": overview, Eligibility, Get started, x402 protocol, Configuration, Monetization rules and Payment validation.
Related payment features live elsewhere in the sidebar:
- Wallets is under AI (https://developers.cloudflare.com/wallets/).
- Agentic payments (x402 and MPP for the Agents SDK) are under Agents > Tools > Payments (https://developers.cloudflare.com/agents/tools/payments/).
- Pay Per Crawl is under AI Crawl Control (https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/).
- Machine Payments is under AI Gateway (https://developers.cloudflare.com/ai-gateway/features/machine-payments/).
- Stablecoin payments for Cloudflare invoices are under Billing (https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/).

## 2. Timeline and status

All dates come from the sources listed; status is as of 2026-10-05.

| Date | Event | Source |
| --- | --- | --- |
| 2025-09-23 | Coinbase announces its intent to launch the x402 Foundation with Cloudflare; Cloudflare ships x402 in the Agents SDK and MCP, proposes a `deferred` x402 scheme, launches the x402 playground on Base testnet USDC | https://blog.cloudflare.com/x402/, https://www.coinbase.com/blog/coinbase-and-cloudflare-will-launch-x402-foundation |
| 2025-09-25 | Cloudflare announces plans for NET Dollar, a U.S. dollar-backed stablecoin | https://www.cloudflare.com/press/press-releases/2025/cloudflare-introduces-net-dollar-to-support-a-new-business-model-for-the-ai-driven-internet/ |
| 2026-02-09 | Agents SDK v0.4.0 migrates its x402 integration to x402 v2 (`@x402/core`, `@x402/evm`) | https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/ |
| 2026-06-12 | Last update of the Billing "Stablecoin payments" page (USDC on Base and Polygon for paying Cloudflare) | https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/ |
| 2026-07-01 | Monetization Gateway announced, waitlist opened | https://blog.cloudflare.com/monetization-gateway/ |
| 2026-08-04 | Cloudflare Wallets and cloudflare.pay announced; handle reservations open | https://blog.cloudflare.com/wallets/, https://www.cloudflare.com/press/press-releases/2026/cloudflare-gives-ai-agents-an-identity-and-a-wallet/ |
| 2026-09-30 | Monetization Gateway closed beta; AI Gateway Machine Payments beta | https://blog.cloudflare.com/monetization-gateway-beta/, https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/, https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/ |

Status summary as of 2026-10-05:
- Monetization Gateway: closed beta; access is requested through the dashboard at `https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway`.
- Monetization API endpoints: marked `x-stability: beta` in the OpenAPI spec (`raw/api/openapi.json`).
- AI Gateway Machine Payments: beta.
- Pay Per Crawl: closed beta (docs say "closed beta"; the 2025-12-10 changelog title says "Private beta").
- Cloudflare Wallets: only handle reservation is live; reserved handles cannot send, receive or hold funds yet.
- NET Dollar: announced plans only; no developer docs page mentions it.
- Stablecoin billing (paying Cloudflare in USDC): documented as available, with no beta label.

---

## 3. Monetization Gateway

### 3.1 What it is

Monetization Gateway "applies x402 payment requirements to matching traffic" (https://developers.cloudflare.com/monetization-gateway/).
The seller defines the shape of the request to match, how much to charge, and the receiving wallet.
It is meant to protect APIs, Model Context Protocol (MCP) tools, sites and datasets.
Payment happens inside the HTTP request flow: the buyer signs a cryptographic payment authorization, with no checkout redirect and no separate payment API call.
The announcement blog frames it as a "single control plane to manage payment policies and access controls across your applications" that also protects the origin "from high payment volumes by handling payment verification and enforcement at the edge" (https://blog.cloudflare.com/monetization-gateway/).
The beta blog calls it, in its simplest form, a "paywall for agents" and says Cloudflare handles payment verification and settlement, failures and retries, analytics, and keeping up with x402 protocol changes (https://blog.cloudflare.com/monetization-gateway-beta/).
The beta blog positions it for resources "where every request is the use, like APIs, tools, and data", and points high-value content (crawled once, used many times) to a separate product called Pay Per Use (linked as http://blog.cloudflare.com/pay-per-use, which is not in the mirror).
The July blog says settlement is peer-to-peer, so buyer funds are deposited directly into the seller's wallet, and that Cloudflare aims for sub-second settlement.
The July blog says sellers "will be able to use the stablecoins they accumulate for their own transactions or redeem the stablecoins for equivalent fiat currency in their bank account"; no docs page describes an off-ramp.

### 3.2 Eligibility

From https://developers.cloudflare.com/monetization-gateway/eligibility/ (as of 2026-10-05):

Buyers and sellers must be based in the United States.

Seller (account) requirements:
- Accept the Service-Specific Terms (https://www.cloudflare.com/service-specific-terms-application-services/).
- Be based in the United States.
- Keep a credit card on file.
- Verify the account email address.
- Use an account older than 60 days.
- Pass Cloudflare account-level security checks.

Zone requirements:
- The zone is proxied through Cloudflare.
- The zone is older than 30 days.
- The zone passes Cloudflare zone-level security checks.

Get started adds one more prerequisite: "You have a receiving wallet" (https://developers.cloudflare.com/monetization-gateway/get-started/).
The API exposes eligibility as a decision with status `pending`, `approved` or `rejected`, plus optional human-readable `reasons` for a rejection (section 3.8).
The beta blog says support for "new geographies" is "on the way", with no date.
No page lists a required Cloudflare plan (Free, Pro, Business or Enterprise) for Monetization Gateway itself; the only plan-gated items are the Enterprise-only Body and Body size conditions (section 3.6).

### 3.3 Supported chains, tokens and facilitators

This is the most important table in the file, so each row names its source.

| Item | What the sources say | Source |
| --- | --- | --- |
| Settlement chain | "Payments settle on the Base blockchain" | Beta blog, https://blog.cloudflare.com/monetization-gateway-beta/ |
| Token | "using USDC, a stablecoin pegged to the U.S. dollar" | Beta blog |
| Facilitator | "payment verification and settlement through Coinbase's x402 Facilitator" (links https://docs.cdp.coinbase.com/x402/seller/facilitator) | Beta blog; docs overview step 6 says "settles the payment through the Coinbase x402 Facilitator" |
| Protocol version | x402 version 2 | https://developers.cloudflare.com/monetization-gateway/x402/ |
| Network field | "Blockchain network identifier in CAIP-2 format"; the docs example uses the placeholder `<CAIP_2_NETWORK>` | x402 protocol page |
| Asset field | "Asset identifier used for payment"; placeholder `<ASSET_IDENTIFIER>` | x402 protocol page |
| Receiving wallet format | "0x-prefixed 20-byte hexadecimal Ethereum address", pattern `^0x[0-9a-fA-F]{40}$`; mixed-case addresses must carry a valid EIP-55 checksum; all-lowercase or all-uppercase accepted | OpenAPI schema `monetization_monetization-rule-input-fixed-price` |
| Unit | One atomic unit equals $0.000001 | https://developers.cloudflare.com/monetization-gateway/configuration/rules/ |
| Unit (API wording) | "smallest indivisible unit of the configured payment token", with "$0.001 for a 6-decimal token such as USDC" | OpenAPI schema `monetization_monetization-price` |
| Wallet screening | Every address "must pass wallet screening" whenever a rule is deployed or patched | OpenAPI ruleset and patch schemas |
| Payment rails beyond stablecoins | Planned: "support additional payment rails" | Beta blog |
| Other stablecoins | The July blog names "Open USD and USDC" as examples of stablecoins in general; only USDC is stated for the beta | https://blog.cloudflare.com/monetization-gateway/ |

What this means in plain terms, as of 2026-10-05:
- The only chain any source names for Monetization Gateway is Base, and the only token is USDC.
- Solana, Ethereum mainnet, Polygon and other x402 networks are not stated as supported by Monetization Gateway, even though Cloudflare's generic x402 docs list them for x402 in general (section 4).
- Robinhood Chain (chain id 4663) is not mentioned anywhere in the Monetize, x402, Wallets or billing sources.
- The receiving address must be an EVM (`0x`) address, so a Solana base58 address cannot be configured as a `payTo` through the API.
- NET Dollar is not mentioned in any Monetization Gateway source.

### 3.4 The HTTP 402 / x402 v2 request flow

The overview lists seven steps (https://developers.cloudflare.com/monetization-gateway/):
1. A buyer requests a protected resource.
2. Monetization Gateway returns payment requirements.
3. The buyer signs an authorization and retries the request.
4. Monetization Gateway verifies the authorized payment is valid.
5. The origin receives the verified payment and produces a response.
6. The gateway settles the payment through the Coinbase x402 Facilitator.
7. The buyer receives the requested resource.

For fixed pricing the gateway settles the signed amount; for variable pricing the origin reports the actual amount.

Header map (https://developers.cloudflare.com/monetization-gateway/x402/ and https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/):

| Header | Between | Direction | Encoding | Purpose |
| --- | --- | --- | --- | --- |
| `PAYMENT-REQUIRED` | Gateway and client | Gateway to client, on a `402 Payment Required` | Base64-encoded JSON | Describes the resource and accepted payment options |
| `PAYMENT-SIGNATURE` | Client and gateway | Client to gateway, on the retry | Base64-encoded JSON | Signed payment authorization bound to the chosen requirements |
| `PAYMENT-CONTEXT` | Gateway and origin | Gateway to origin | Signed JWT (Ed25519) | Cloudflare-specific proof that payment was authorized |
| `PAYMENT-SETTLEMENT` | Origin and gateway | Origin to gateway, on a successful `upto` response only | JSON, for example `{ "amount": "1000000" }` | Reports the actual variable charge; stripped before the response reaches the buyer |

The docs call `PAYMENT-CONTEXT` and `PAYMENT-SETTLEMENT` "between Monetization Gateway and your origin" and "not x402 client headers".

Step 1, unpaid request and 402:

```http
GET /premium-data HTTP/1.1
Host: api.example.com

HTTP/1.1 402 Payment Required
PAYMENT-REQUIRED: <BASE64_ENCODED_PAYMENT_REQUIRED>
```

Decoded fixed-price `PAYMENT-REQUIRED` body, as shown in the docs:

```json
{
	"x402Version": 2,
	"resource": {
		"url": "https://api.example.com/premium-data",
		"description": "Premium data",
		"mimeType": "application/json"
	},
	"accepts": [
		{
			"scheme": "exact",
			"network": "<CAIP_2_NETWORK>",
			"asset": "<ASSET_IDENTIFIER>",
			"amount": "25000",
			"payTo": "<RECEIVING_WALLET>",
			"maxTimeoutSeconds": 3600,
			"extra": {}
		}
	]
}
```

`accepts` fields: `scheme` (`exact` for fixed, `upto` for variable), `network` (CAIP-2), `asset`, `amount` (fixed charge or maximum, in atomic units), `payTo` (seller's receiving wallet), `maxTimeoutSeconds` (maximum time allowed for the authorization).

Step 2, paid retry:

```http
GET /premium-data HTTP/1.1
Host: api.example.com
PAYMENT-SIGNATURE: <BASE64_ENCODED_PAYMENT_PAYLOAD>
```

The docs tell buyers to use an x402 client library rather than build the payload by hand, and point to https://developers.cloudflare.com/agents/tools/payments/x402/ and https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/.
After settlement the gateway returns the origin response.
If verification or settlement fails, the gateway does not serve the protected resource, and clients "should inspect the HTTP status and x402 response before retrying".

### 3.5 Origin payment validation (`PAYMENT-CONTEXT`, `PAYMENT-SETTLEMENT`)

From https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/:
- The origin receives the payment authorization in the `PAYMENT-CONTEXT` header as a JWT and must validate it before serving paid content.
- Use only the pinned JWKS at https://payments.cloudflare.com/certs.
- Require Ed25519 signatures.
- Cache keys according to the JWKS endpoint's `Cache-Control` header.
- Never parse the token without verifying its signature; reject requests when validation fails.
- If `PAYMENT-CONTEXT` is absent, treat the request as unpaid and unverified, do not serve paid content and do not set `PAYMENT-SETTLEMENT`.
- Get started says Cloudflare "strongly recommends" this verification, which is how a seller stops buyers from bypassing the gateway.

Recommended JWT libraries: JavaScript, TypeScript and Workers `jose`; Python `PyJWT` with `cryptography`; Java Nimbus JOSE + JWT; Go `github.com/golang-jwt/jwt/v5`; Rust `jsonwebtoken`.

Fixed (`exact`) claims example:

```json
{ "iat": 1770000000, "nbf": 1770000000, "exp": 1770000120,
  "aud": "https://api.example.com/premium-data", "scheme": "exact", "amount": "25000" }
```

For fixed pricing the origin must not set `PAYMENT-SETTLEMENT`; the gateway settles the signed amount.

Variable (`upto`) claims example, where `amount` is the authorized maximum:

```json
{ "iat": 1770000000, "nbf": 1770000000, "exp": 1770000120,
  "aud": "https://api.example.com/generate", "scheme": "upto", "amount": "100000" }
```

Variable settlement rules:
- The origin computes an actual amount with `0 <= actual <= authorized maximum`, in atomic units.
- If the reported amount exceeds the maximum, the gateway settles the maximum instead.
- If the reported amount is zero, nothing is settled.
- Set `PAYMENT-SETTLEMENT` only on a successful `upto` response, and before sending response headers.
- Do not set it when the response status is `400` or greater.
- Do not create a `PAYMENT-RESPONSE` header at the origin.
- The gateway creates the payment receipt after settlement and removes `PAYMENT-SETTLEMENT` from the response the buyer sees.

The example JWTs expire 120 seconds after issue (`exp - iat = 120`), so the origin is expected to check `nbf`, `exp` and `aud` within a short window; the docs do not state a required clock skew.

### 3.6 Monetization rules (schemes, prices, audiences, conditions)

From https://developers.cloudflare.com/monetization-gateway/configuration/rules/:
"Each rule defines a domain, URL, price, and audience."

Pricing schemes:

| Dashboard name | x402 scheme | Behavior |
| --- | --- | --- |
| Fixed | `exact` | Same price for each request with fixed inputs; the gateway settles the signed amount |
| Variable | `upto` | Authorizes a maximum price; the origin discloses and settles the actual amount |
| (API only) | `origin_controlled` | "lets the origin server set pricing dynamically"; the rule carries no price and any `price` value, including "0", is rejected (OpenAPI only; not in the docs pages) |

The beta blog describes origin-controlled pricing as co-designed with AI Gateway: the gateway "requests pricing information directly from the seller", and other sellers who want it are told to email x402@cloudflare.com.

Prices (as of 2026-10-05):
- One atomic unit = $0.000001; $0.001 = 1,000 units; $0.01 = 10,000 units.
- Minimum settlement $0.001 (1,000 units).
- Maximum price $100 (100,000,000 units).
- API pattern `^([1-9]\d{3,7}|10{8})$`: a canonical decimal string, no leading zeros, a bare JSON number is rejected.
- The API says 1,000 is "the smallest amount the payment facilitator can settle".

Audiences:

| Audience | Behavior |
| --- | --- |
| Everyone | Charges all traffic matching the URL and advanced conditions |
| Verified Bots | Charges matching bots identified through BotBase (https://developers.cloudflare.com/bots/botbase/) |

HTTP methods: a rule charges `GET` by default; several methods can be selected per rule.

Advanced conditions: Header, URI Query String, User Agent, X-Forwarded-For, IP Source Address, Continent, Country, European Union, Cookie Value, Body (Enterprise only), Body size (Enterprise only).

In the API a rule is a wirefilter `expression` (for example `(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})`), "forwarded verbatim to the Rulesets API, which validates its syntax"; rules are evaluated in array order.

Planned capabilities from the July announcement that the docs do not (yet) describe, as of 2026-10-05:
- Intercept origin HTTP 401 responses and return 402 with payment instructions, so only unauthenticated callers pay.
- Require agents to authenticate with Web Bot Auth and apply usage-based pricing against accounts they already hold.
- Make sellers' services discoverable to agents, expose logs for all transactions, and add identity primitives (beta blog "over time" list).

### 3.7 Dashboard setup

From https://developers.cloudflare.com/monetization-gateway/get-started/:
1. In Monetization Gateway, select the domain to monetize.
2. Select the receiving wallet.
3. Enter the URL to be monetized.
4. Select an audience: Everyone or Verified Bots.
5. Select a pricing scheme: Fixed, or Variable (which requires the origin to report the actual amount).
6. Enter the price (minimum $0.001).
7. Use the advanced settings described in Monetization rules.
8. Verify payment at the origin (section 3.5).

Dashboard deep link: `https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway`.

### 3.8 API (beta) and Terraform

The docs pages do not mention an API, but the OpenAPI spec mirrored in `raw/api/openapi.json` (tag `Monetization`, all endpoints `x-stability: beta`, auth by API token or API email plus key) defines these endpoints:

| Method and path | Operation id | What it does |
| --- | --- | --- |
| `GET /accounts/{account_id}/monetization` | `monetization-get-account-eligibility` | Latest stored account eligibility result; 404 if none |
| `POST /accounts/{account_id}/monetization` | `monetization-check-account-eligibility` | Runs the account check; body `{"acceptedTermsOfService": true}` (required, must be `true`) |
| `GET /zones/{zone_id}/monetization` | `monetization-get-zone-eligibility` | Latest stored zone eligibility result; 404 if none |
| `POST /zones/{zone_id}/monetization` | `monetization-check-zone-eligibility` | Runs the zone check and "enables its entitlement when the decision is approved"; returns `enabled` |
| `GET /zones/{zone_id}/monetization/rules` | `monetization-list-rules` | Deployed Payment Required rules; 404 if the zone has no Payment Required ruleset |
| `PUT /zones/{zone_id}/monetization/rules` | `monetization-deploy-ruleset` | Replaces the whole ruleset with the submitted desired state; empty array clears it; 403 "policy restrictions" possible |
| `DELETE /zones/{zone_id}/monetization/rules` | `monetization-delete-ruleset` | Removes every Payment Required rule; rules the service does not own are preserved; no-op if none |
| `GET /zones/{zone_id}/monetization/rules/{rule_id}` | `monetization-get-rule` | One rule |
| `PATCH /zones/{zone_id}/monetization/rules/{rule_id}` | `monetization-patch-rule` | Partial update; returns the full collection |
| `DELETE /zones/{zone_id}/monetization/rules/{rule_id}` | `monetization-delete-rule` | Deletes one rule; returns the remaining collection |

Rule object fields:
- `id`: server-assigned, max 32 chars, stable across full-ruleset replacements; include it on PUT to update in place, omit to create, and rules omitted from a PUT are deleted.
- `expression`: wirefilter expression (required).
- `address`: receiving EVM address (required).
- `scheme`: `exact`, `upto` or `origin_controlled` (required).
- `price`: atomic-unit decimal string, required for `exact` and `upto`, forbidden for `origin_controlled`.
- `description`: max 512 characters.
- `enabled`: boolean, default `true`.

Ruleset limits: at most 40 unique wallet addresses per ruleset (case-insensitive comparison), and every address must pass wallet screening before deployment.
The 5XX responses are described as "Payments-edge dependency failure", "Entitlements API dependency failure" or "Rulesets dependency failure", which indicates the rules are stored as a Rulesets API ruleset.
The OpenAPI does not show an audience field; how the Verified Bots audience maps into the expression is not documented.

Example deploy body built only from the schema:

```json
{
	"rules": [
		{
			"description": "Premium API endpoint",
			"expression": "(http.request.uri.path eq \"/premium\" and http.request.method in {\"GET\" \"POST\"})",
			"address": "0x1234567890abcdef1234567890abcdef12345678",
			"scheme": "exact",
			"price": "10000"
		}
	]
}
```

Terraform: the July blog says rules can be managed "as code through the Cloudflare API and Terraform", but no Terraform resource for Monetization Gateway appears anywhere in the mirrored docs, API reference or GitHub catalog as of 2026-10-05.

### 3.9 Limits and pricing

| Limit | Value (as of 2026-10-05) | Source |
| --- | --- | --- |
| Minimum price / settlement | $0.001 (1,000 atomic units) | Rules page, Get started, OpenAPI |
| Maximum price | $100 (100,000,000 atomic units) | Rules page, OpenAPI |
| Unique wallet addresses per zone ruleset | 40 | OpenAPI |
| Rule description length | 512 characters | OpenAPI |
| Example `maxTimeoutSeconds` | 3600 (example value, not stated as a limit) | x402 protocol page |
| Geography | U.S. buyers and sellers only | Eligibility, beta blog |
| Account age | Older than 60 days | Eligibility |
| Zone age | Older than 30 days | Eligibility |
| Enterprise-only conditions | Body, Body size | Rules page |

Cloudflare's own fee for Monetization Gateway is not stated in any mirrored source as of 2026-10-05.
The docs have no pricing page for the product.
The July blog says Cloudflare is "designing the Monetization Gateway to keep payment overhead low".
Network gas fees for Base settlement are not discussed in any Monetization Gateway source.

### 3.10 Customers in production

From the 2026-09-30 beta blog (https://blog.cloudflare.com/monetization-gateway-beta/):

| Seller | What is sold | Scheme |
| --- | --- | --- |
| Cloudflare AI Gateway | Inference on select models, triggered by `Payment-Method: x402` | Origin-controlled pricing (AI Gateway's own pricing module) |
| Ceramic.ai | Web search API (index of 40 billion+ pages, results in as little as 50 ms) without an API key | Fixed |
| Stocktwits | Ticker sentiment, message volume, followers and trending signals on a separate agent-facing path | Per request (scheme not named) |
| API2PDF | HTML and Office to PDF; returns 402 when no API key is sent | Variable |

The API2PDF example shows the raw exchange: `POST https://v2.api2pdf.com/chrome/pdf/html` without a key returns `HTTP/2 402` with a `payment-required` header.
API2PDF reported a more than 50% conversion drop when it required a credit card after the first month, which motivated the switch.

### 3.11 Most useful pages

- Overview: https://developers.cloudflare.com/monetization-gateway/
- Eligibility: https://developers.cloudflare.com/monetization-gateway/eligibility/
- Get started: https://developers.cloudflare.com/monetization-gateway/get-started/
- x402 protocol: https://developers.cloudflare.com/monetization-gateway/x402/
- Configuration: https://developers.cloudflare.com/monetization-gateway/configuration/
- Monetization rules: https://developers.cloudflare.com/monetization-gateway/configuration/rules/
- Payment validation: https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/
- Closed beta changelog: https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/
- JWKS: https://payments.cloudflare.com/certs
- Announcement: https://blog.cloudflare.com/monetization-gateway/
- Beta: https://blog.cloudflare.com/monetization-gateway-beta/
- Contact: x402@cloudflare.com

---

## 4. The x402 protocol as Cloudflare documents it

Sources: https://blog.cloudflare.com/x402/ (2025-09-23), https://developers.cloudflare.com/agents/tools/payments/x402/ (updated 2026-06-03), https://developers.cloudflare.com/agents/tools/payments/ (updated 2026-08-05), Coinbase's post https://www.coinbase.com/blog/coinbase-and-cloudflare-will-launch-x402-foundation.

Origin and governance:
- x402 is "a payment standard created by Coinbase" and is named for the HTTP 402 status code.
- Coinbase's 2025-09-23 post announced the "intent to launch the x402 Foundation, in collaboration with Cloudflare", co-founded by Coinbase and Cloudflare "with additional members to be announced", covering governance, ecosystem grants and interoperability.
- The July 2026 Monetization Gateway blog says x402 is being built "with a coalition of more than 25 industry leaders via the x402 Foundation" and links a Linux Foundation release titled "Linux Foundation is launching the x402 Foundation and welcoming the contribution of the x402 protocol".
- The Agents docs say x402 "is governed by Coinbase and Cloudflare, two of the founding members of the x402 Foundation".
- The spec repo is referenced both as https://github.com/coinbase/x402 (2025 blog) and https://github.com/x402-foundation/x402 (2026 docs).
- Cloudflare said in 2025 that sites on Cloudflare already send "over a billion HTTP 402 response codes" a day to bots and crawlers.

Generic flow (Agents docs):
1. Client requests `GET /resource`.
2. Server returns `402` with a Base64 `PAYMENT-REQUIRED` header holding price, accepted token, network and merchant address.
3. Client retries with a signed payload in `PAYMENT-SIGNATURE`.
4. Server verifies, directly or through a facilitator, and settles on-chain.
5. Server returns the resource with a `PAYMENT-RESPONSE` header carrying settlement confirmation.

Facilitator:
- An optional but recommended third party that exposes `POST /verify` and `POST /settle`.
- It "does not hold funds"; it verifies and broadcasts the client's pre-signed transaction.
- `https://x402.org/facilitator` is "the public facilitator operated by Coinbase and is used in all Cloudflare examples".
- More facilitators per network are listed at https://www.x402.org/ecosystem?filter=facilitators.

Schemes and networks (Agents docs, as of 2026-10-05):

| Scheme | Networks | Meaning |
| --- | --- | --- |
| `exact` | EVM, Solana, Aptos, Stellar, Hedera, Sui | Transfers a fixed token amount, "typically ERC-20 USDC on EVM" |
| `upto` | EVM only | Authorizes a maximum; actual charge set at settlement |

Named supported networks: Base, Ethereum, Polygon, Optimism, Arbitrum, Avalanche, Solana, Aptos, Stellar and Sui (Hedera appears only in the scheme table).
Test network: `base-sepolia`, with free test USDC from https://faucet.circle.com/.
The Agents payments overview summarises x402 as "on-chain stablecoin payments (USDC on Base, Ethereum, Solana, and other networks)".

Proposed `deferred` scheme (2025 blog, a proposal, not a shipped feature in any docs page):
- Designed for payments that need delayed settlement or aggregation (disputes, daily batch billing), settled by card, bank or stablecoin.
- The client signs with HTTP Message Signatures using a JWK in a hosted directory (the Web Bot Auth pattern, `tag="web-bot-auth"`), sends a `Payment:` header with `scheme="deferred"`, and receives `Payment-Response` on success.
- "In this scenario, there is no blockchain associated with the payments."
- Cloudflare said it would bring the scheme to Pay Per Crawl; Coinbase's post repeats this.

x402 playground: https://playground.x402.cloudflare.com/ creates a wallet funded with testnet USDC on a Base testnet and lets an Agents SDK agent call free and paid MCP tools (2025 blog).

---

## 5. Do-it-yourself x402 on Workers and the Agents SDK

These paths do not require Monetization Gateway, and no source applies the U.S.-only restriction to them.
They are documented with Base (`base`) and Base Sepolia (`base-sepolia`) and Coinbase's public facilitator.

Charge for HTTP content with the x402-proxy Worker template (https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/):
- Deploy from https://github.com/cloudflare/templates/tree/main/x402-proxy-template.
- Configure `PAY_TO`, `NETWORK` (`base-sepolia` for testing, `base` for production) and `PROTECTED_PATTERNS` (pattern, price such as `"$0.10"`, description) in `wrangler.jsonc`.
- With Bot Management, add `bot_score_threshold` (requests at or below the score hit the paywall) and `except_detection_ids` to allowlist crawlers, so humans stay free.
- The same template is listed under AI Crawl Control Worker templates as the "x402 Payment-Gated Proxy" (https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/).

Custom Worker endpoints with Hono:

```ts
import { Hono } from "hono";
import { paymentMiddleware } from "x402-hono";

const app = new Hono<{ Bindings: Env }>();
app.use(
	paymentMiddleware(
		"0xYourWalletAddress" as `0x${string}`,
		{ "/premium": { price: "$0.10", network: "base-sepolia", config: { description: "Premium content" } } },
		{ url: "https://x402.org/facilitator" },
	),
);
app.get("/premium", (c) => c.json({ message: "Thanks for paying!" }));
export default app;
```

Charge for MCP tools (https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/):
- Wrap `McpServer` with `withX402(server, X402_CONFIG)` and register tools with `this.server.paidTool(name, description, priceUsd, inputSchema, annotations, handler)`.
- `X402Config` fields: `network` (`base` or `base-sepolia`), `recipient` (wallet), `facilitator` (`{ url: "https://x402.org/facilitator" }`).
- Free and paid tools can be mixed; example at https://github.com/cloudflare/agents/tree/main/examples/x402-mcp.

Pay from an agent (https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/):
- `withX402Client(mcpClient, { network: "base-sepolia", account })` with a viem `privateKeyToAccount` signer.
- `x402Client.callTool(onPaymentRequired, { name, arguments })`; pass `null` instead of the callback to pay automatically, or implement human-in-the-loop approval.
- Store the key with `npx wrangler secret put MY_PRIVATE_KEY`.

Pay from coding tools (https://developers.cloudflare.com/agents/tools/payments/x402/pay-with-tool-plugins/): an OpenCode plugin and a Claude Code `PostToolUse` hook on `WebFetch` that retry 402 responses with `@x402/fetch` (`wrapFetchWithPayment`) and `@x402/evm` (`registerExactEvmScheme`), using an `X402_PRIVATE_KEY` environment variable.

SDK packages: `x402-hono`, `@x402/fetch`, `@x402/evm`, and `agents/x402` (inside `agents`).
Agents SDK v0.4.0 (2026-02-09) moved to x402 v2: replace `x402` with `@x402/core` and `@x402/evm`, `PaymentRequirements` uses `amount` instead of `maxAmountRequired`, and `X402ClientConfig.account` became `ClientEvmSigner`.
The v0.20.0 changelog (2026-07-27) marks the old `withX402Client` `callTool(params, resultSchema, options)` overload as a compatibility overload with no announced removal version.
All Cloudflare code samples use EVM packages only; no Cloudflare page shows a Solana x402 signer, even though Solana is listed for the `exact` scheme.

---

## 6. Machine Payments Protocol (MPP)

Source: https://developers.cloudflare.com/agents/tools/payments/mpp/ and sub-pages.

- MPP (https://mpp.dev) is an open protocol that standardizes HTTP 402 with a formal authentication scheme proposed to the IETF (https://paymentauth.org).
- It uses `WWW-Authenticate: Payment` and `Authorization: Payment` headers, and MCP tools use the same flow through JSON-RPC.
- It is payment-method agnostic: stablecoins, cards through Stripe, and custom methods.
- It defines three intents: `charge` (one-time), `session` (measured usage) and `subscription` (recurring).
- It is "backwards-compatible with x402": MPP clients can consume existing x402 services unchanged.
- SDKs exist for TypeScript (`mppx`), Python, Rust, Go and Ruby.
- The mpp-proxy Worker (https://github.com/cloudflare/mpp-proxy) gates routes, issues a 1-hour session cookie after payment, needs `JWT_SECRET` and `MPP_SECRET_KEY` secrets, and uses the Tempo network: production `PAYMENT_CURRENCY` `0x20c000000000000000000000b9537d11c60e8b50`, testnet `TEMPO_TESTNET: true` with `0x20c0000000000000000000000000000000000000`.
- Worker routes use `Mppx.create({ methods: [tempo.charge({ testnet: true })], secretKey })` and `mppx.charge({ amount, currency, description, recipient })` in Hono.

Monetization Gateway is documented as x402 only; no source says it accepts MPP.

---

## 7. AI Gateway Machine Payments

Source: https://developers.cloudflare.com/ai-gateway/features/machine-payments/ (updated 2026-09-30) and changelog https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/.

- Status: beta as of 2026-10-05.
- Lets clients pay for inference from a stablecoin wallet instead of holding prepaid Unified Billing credits.
- Requirements: based in the United States, a credit card on file, an authenticated AI Gateway, and a Cloudflare API token.
- Trigger: the Cloudflare-specific request header `Payment-Method: x402`; without it, normal credential precedence applies and Unified Billing credits may be charged.
- Endpoint: only `POST /accounts/{account_id}/ai/run`.
- Eligible models: `z-ai/glm-4.7-flash`, `google/gemma-4-26b-a4b-it`, `openai/gpt-oss-20b`, `alibaba/qwen3.8-27b`.
- Flow: AI Gateway returns `402` with `PAYMENT-REQUIRED`; "most AI Gateway models use the `upto` payment scheme"; the client signs up to the maximum and retries with `PAYMENT-SIGNATURE`; Cloudflare runs inference and settles the actual cost, never above the maximum.
- The beta blog says this is sold through Monetization Gateway with origin-controlled pricing.
- The page does not name the chain or token.

---

## 8. Adjacent products: Pay Per Crawl, Wallets, NET Dollar, stablecoin billing

### 8.1 Pay Per Crawl (AI Crawl Control)

Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/ and sub-pages.
- Status: closed beta as of 2026-10-05; sign-up at https://www.cloudflare.com/paypercrawl-signup/ or through an Enterprise account executive.
- Charges AI crawlers a per-zone price; Cloudflare is the Merchant of Record.
- It is fiat and Stripe based, not x402: publishers connect a dedicated Cloudflare Stripe Connect account (pre-existing Stripe accounts are not compatible), Cloudflare aggregates charges and pays out monthly.
- Crawlers must use Web Bot Auth; the 402 carries `crawler-price: USD 0.01`, the crawler retries with `crawler-exact-price` or `crawler-max-price` (which must be inside the signed `signature-input` components since 2025-12-10), and a 200 carries `crawler-charged`.
- Errors return a `crawler-error` header with 11 codes.
- Minimum price $0.001 per crawl; one price for all crawlers set to "Charge"; only successful responses are charged.
- Always-free paths: `/robots.txt`, `/sitemap.xml`, `/security.txt`, `/.well-known/security.txt`, `/crawlers.json`.
- Dynamic pricing (2026-06-16): the origin returns a `crawler-price` response header, or a Worker sets it; Cloudflare adds a `cf-pay-per-crawl` request header to origin requests.
- WAF or Bot Management blocks override the "charge" action.
- Discovery API for crawlers: `GET https://crawlers-api.ai-audit.cfdata.org/charged_zones` with Web Bot Auth.
- The API reference also lists `pay-per-crawl` and `pay-per-use` endpoint families (for example `POST /accounts/{account_id}/pay-per-use/usage-reports`), but no docs page for Pay Per Use exists in the mirror.

### 8.2 Cloudflare Wallets and cloudflare.pay

Sources: https://developers.cloudflare.com/wallets/, https://developers.cloudflare.com/wallets/faq/, https://blog.cloudflare.com/wallets/, the 2026-08-04 press release.
- Announced 2026-08-04 as the buyer side of the market that Monetization Gateway sells into.
- Account Wallets (for humans) will add funds, delegate to Virtual Wallets and remove funds; Virtual Wallets (for agents, operated by API key) will have a spending cap, an approved-merchant allow list and a maximum transaction size.
- "At first, Cloudflare Wallets will be able to send, receive, and hold stablecoins"; no chain or token is named.
- Identity: a handle at `HANDLE.cloudflare.pay`, with agent sub-identities such as `research.example.cloudflare.pay`, built on Web Bot Auth keypairs.
- Available today: one free handle per account at https://cloudflare.pay/; handles cannot be changed, released or moved, and a reservation "does not guarantee access to a Cloudflare Wallet on release".
- The press release says full wallet access, including on-ramp, off-ramp and Virtual Wallets, "will be available in the coming months".
- Wallets sits under the AI section of the sidebar.

### 8.3 NET Dollar

Sources: the 2025-09-25 press release and the Ledger Insights write-up (https://www.ledgerinsights.com/cloudflare-to-launch-net-stablecoin-for-ai-agentic-payments).
- Cloudflare "announced plans to introduce NET Dollar, a new U.S. dollar-backed stablecoin that will enable instant, secure transactions for the agentic web".
- Stated goals: payments anywhere, instant automated transactions, and a new business model where creators, API developers and AI companies are paid fairly.
- The release says Cloudflare also contributes to the Agent Payments Protocol (AP2) and x402.
- More information is pointed to at https://netdollar.cloudflare.com/.
- Neither source names an issuer, a chain, a launch date or a token contract.
- No developer docs page, changelog entry or API endpoint in the 2026-10-05 mirror mentions NET Dollar, and Monetization Gateway settles in USDC, not NET Dollar.

### 8.4 Paying Cloudflare with stablecoins (Billing)

Source: https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/ (updated 2026-06-12).
- Select **Crypto** at checkout; the wallet is connected on a Stripe-hosted page at `crypto.stripe.com`.
- Supported: USDC on Base and Polygon; wallets MetaMask, Phantom, Coinbase Wallet and 400+ via WalletConnect; invoices are in USD.
- A one-time smart contract permit authorizes the first charge and future recurring charges: plan renewals, usage-based charges billed at threshold for Workers, R2 and Stream, and prorated upgrades.
- No chargebacks or disputes; payments are final on-chain.
- Failures: insufficient funds (subscription enters dunning), approval revoked, or wallet screening flagged; if a card is on file, Cloudflare falls back to it.
- Refunds come back as USDC to the paying wallet, "typically within minutes".
- Gas is paid by the wallet; Cloudflare adds no markup or transaction fee.
- Payments appear with method `crypto` under **Manage Account** > **Billing** > **Invoices**.
- This is a buyer-of-Cloudflare feature and is unrelated to receiving money through Monetization Gateway.

---

## 9. Comparison: which payment path to use

| Need | Monetization Gateway | DIY x402 Worker or `paidTool` | Pay Per Crawl | mpp-proxy |
| --- | --- | --- | --- | --- |
| Status (as of 2026-10-05) | Closed beta | Documented, no beta label | Closed beta | Documented, no beta label |
| Who can sell | U.S. sellers, account over 60 days, zone over 30 days | Any Cloudflare account (no restriction stated) | Approved beta publishers | Any Cloudflare account (no restriction stated) |
| Who can buy | U.S. buyers | Anyone with a supported wallet (no restriction stated) | Verified AI crawlers with a Cloudflare account and Stripe | MPP clients |
| Chain and token | USDC on Base (beta blog) | Whatever the facilitator supports; docs examples use `base` and `base-sepolia` | Fiat via Stripe | Tempo (stablecoin contract addresses given) |
| Facilitator | Coinbase x402 Facilitator, run by Cloudflare | You choose; examples use `https://x402.org/facilitator` | None (Cloudflare is Merchant of Record) | MPP SDK |
| Variable pricing | `upto` plus `PAYMENT-SETTLEMENT`; `origin_controlled` in API | `upto` on EVM per x402 spec | Dynamic `crawler-price` header | `session` intent |
| Code at origin | Validate `PAYMENT-CONTEXT` JWT | Your Worker does everything | Optional dynamic pricing | None for proxy mode |
| Bot targeting | Verified Bots audience via BotBase | `bot_score_threshold` with Bot Management | Per-crawler charge, allow or block | `bot_score_threshold` with Bot Management |
| Cloudflare fee | Not stated | Not applicable in docs | Not stated in the pages read | Not stated |

---

## 10. Build hooks for Web3 projects

These are concrete uses for dapps, launchpads and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
The Cloudflare facts they rely on are cited above; anything about other platforms is marked as an assumption to verify.

Selling data and tools to agents and bots:
- Put a token-analytics or launchpad-data API (new pools, holder counts, bonding-curve progress, trending tokens) behind Monetization Gateway with a Fixed price of $0.001 to $0.01 per call, copying the Stocktwits pattern of a separate agent-facing path next to the existing keyed API.
- Use the Verified Bots audience to charge crawlers and agents that scrape launchpad pages while human users stay free, then add Turnstile and rate limiting for the unverified bot traffic that the audience does not cover (see `protect-connect/01-application-security.md`).
- Use Variable (`upto`) pricing for compute-heavy endpoints such as backtests, route simulations, MEV or slippage simulations, or wallet risk scoring, reporting the actual charge in `PAYMENT-SETTLEMENT` and settling zero for failed work.
- Wrap a paid RPC or indexer proxy (for example a Helius-style RPC proxy Worker, see `raw/external/github.com_helius-labs_helius-rpc-proxy.md`) so agents pay per call instead of holding an API key; at the $0.001 minimum this is $1 per 1,000 calls, so it suits premium methods (archive queries, trace calls, simulation) more than bulk `getBalance` traffic.
- Expose trading tools (quote, simulate, build transaction) from an MCP server with `paidTool` at a few cents per call, and let agent clients pay with `withX402Client`.

Chain fit, stated carefully:
- Monetization Gateway receives on Base in USDC only (beta blog) to a `0x` address, so a Solana-native team needs an EVM receiving wallet to use it; no source says Solana settlement is supported by the gateway.
- Ethereum mainnet and Robinhood Chain (4663) are not named as Monetization Gateway networks in any source as of 2026-10-05.
- For Solana-paid or non-Base EVM endpoints, the DIY route is the option the docs leave open: the x402 `exact` scheme lists Solana and EVM networks and a facilitator is pluggable, but every Cloudflare code sample is EVM and Base only; whether any facilitator supports Robinhood Chain 4663 is not stated in these sources and must be verified on https://www.x402.org/ecosystem?filter=facilitators.
- The U.S.-only rule applies to Monetization Gateway and AI Gateway Machine Payments; the DIY x402 docs state no geography restriction, which matters for global launchpad users.

Security patterns specific to paid endpoints:
- Always validate `PAYMENT-CONTEXT` at the origin with `jose` against https://payments.cloudflare.com/certs, Ed25519 only, and check `aud` equals the exact resource URL, so a token bought for a cheap endpoint cannot unlock an expensive one.
- Lock the origin so it only accepts traffic through Cloudflare (Tunnel or authenticated origin pulls, covered in other files); otherwise a buyer could skip the gateway entirely.
- Because the origin produces the response before settlement (overview steps 5 and 6), keep expensive side effects (on-chain writes, airdrop claims, mint reservations) idempotent and tied to the JWT, so a failed settlement does not leave free work behind.
- Use per-product receiving addresses within the 40-address cap to separate revenue streams (API, MCP tools, data exports) for accounting, and expect wallet screening to reject flagged addresses.
- Treat a micro-fee as an anti-abuse control: putting a $0.001 to $0.01 x402 charge on faucet claims, token-creation endpoints or vanity-address generation raises the cost of Sybil and sniper-bot spam, combined with Turnstile and rate limiting for human paths.

Paying side for Web3 teams:
- Pay Cloudflare invoices (Workers, R2, Stream usage) in USDC on Base or Polygon from MetaMask, Phantom or Coinbase Wallet, keeping a card on file as fallback.
- Give trading or research agents a Virtual Wallet with a spending cap and merchant allow list once Cloudflare Wallets ships; until then only the handle (`HANDLE.cloudflare.pay`) can be reserved, so reserve the project's brand handle early because handles cannot be changed or moved.
- Pay for AI inference per request from a wallet with `Payment-Method: x402` on AI Gateway (U.S. only, four eligible models as of 2026-10-05), for example for a launchpad's token-description or moderation model.

---

## 11. Gaps and contradictions

1. Chain and token are only in a blog post.
   The Monetization Gateway docs never name Base or USDC; they use placeholders (`<CAIP_2_NETWORK>`, `<ASSET_IDENTIFIER>`) and define one atomic unit as $0.000001.
   The beta blog states Base and USDC.
   The API ties the unit to "the configured payment token" and cites USDC as a 6-decimal example.
   If a non-6-decimal token were ever configured, the docs' "1 unit = $0.000001" would not hold.
2. Facilitator identity.
   The docs and beta blog say "Coinbase x402 Facilitator" and link Coinbase CDP docs; the Agents docs say `https://x402.org/facilitator` is "the public facilitator operated by Coinbase".
   The sources do not say whether these are the same service.
3. Third pricing scheme.
   The API (and the beta blog's AI Gateway story) have `origin_controlled`; the Monetization rules page lists only Fixed and Variable.
4. Audience in the API.
   The docs say every rule defines an audience (Everyone or Verified Bots), but the API rule schema has no audience field; how Verified Bots is expressed in the wirefilter expression is undocumented.
5. Verified Bots needs BotBase, and the BotBase page says "BotBase is available to Enterprise Bot Management customers".
   The Monetization Gateway pages do not say whether the Verified Bots audience therefore needs Enterprise Bot Management.
6. Receipts to the buyer.
   The Monetization Gateway x402 page lists two client-facing headers (`PAYMENT-REQUIRED`, `PAYMENT-SIGNATURE`); the generic Agents x402 page lists three, adding `PAYMENT-RESPONSE`.
   The payment validation page says the gateway "creates the payment receipt after settlement" but does not say how the buyer receives it.
7. Order of work and settlement.
   The overview has the origin produce its response (step 5) before settlement (step 6); the generic x402 flow settles before returning the resource.
   The docs say a failed settlement means the resource is not served, but do not say what happens to origin work already done.
8. Sub-minimum variable settlements.
   The minimum settlement is $0.001 (1,000 units) and a zero report settles nothing, but the docs do not say what happens if the origin reports between 1 and 999 units.
9. Terraform.
   The July blog promised Terraform management; no Terraform resource exists in the mirrored docs, API reference or GitHub catalog as of 2026-10-05.
   The API itself is marked beta.
10. Cloudflare's fee is undocumented: no pricing page, no fee in the blogs, no gas-fee discussion for sellers.
11. Off-ramp.
    The July blog says sellers will be able to redeem stablecoins for fiat; no docs page describes this, and Wallets on-ramp and off-ramp are "coming months".
12. How U.S. residency of buyers is verified is not described anywhere.
13. Planned features missing from docs: 401-to-402 interception, Web Bot Auth-linked account pricing, discoverability, transaction logs and analytics (the beta blog says "we handle... analytics" but no analytics page exists).
14. Date mismatch.
    The Wallets blog (2026-08-04) says "Earlier this month, we announced the Monetization Gateway", but the Monetization Gateway announcement is dated 2026-07-01.
15. x402 Foundation governance.
    Coinbase's 2025 post says the foundation "will be co-founded by Coinbase and Cloudflare"; the July 2026 blog links a Linux Foundation release about launching it with 25+ members; the Agents docs say x402 "is governed by Coinbase and Cloudflare".
    The spec repo moved from `coinbase/x402` to `x402-foundation/x402`.
    The sources do not reconcile who governs it now.
16. The `deferred` x402 scheme was proposed in 2025 for Pay Per Crawl; the 2026 Pay Per Crawl docs still use Cloudflare's own `crawler-*` headers and Stripe, and no page says the deferred scheme shipped.
17. Pay Per Use is named in the beta blog and has API endpoints (`/accounts/{account_id}/pay-per-use/...`) but has no docs pages and its blog post is not in the mirror.
18. Pay Per Crawl status wording differs: "closed beta" on the docs page versus "Private beta" in the 2025-12-10 changelog title.
19. NET Dollar has no chain, issuer, contract or date in any source, and nothing in the docs mirror references it; the July blog's stablecoin examples are "Open USD and USDC", not NET Dollar.
20. Example values that conflict with their own schema: the OpenAPI example address `0x1234567890abcdef1234567890abcdef12345678===` fails its own pattern `^0x[0-9a-fA-F]{40}$`.
    The 2025 x402 blog's `paidTool` sample destructures `{ number }` but uses `a`; the 2026 docs sample is corrected.
21. Example timing values: the `PAYMENT-REQUIRED` example has `maxTimeoutSeconds: 3600`, while the example `PAYMENT-CONTEXT` JWT lives 120 seconds; neither is stated as a fixed limit.
22. AI Gateway Machine Payments is described as paying "directly from a stablecoin wallet" but still requires a Cloudflare account, API token and card on file, unlike the accountless buyer model in the Monetization Gateway blogs.

---

## 12. Sources

Docs (all under https://developers.cloudflare.com/):
- monetization-gateway/ and its six sub-pages listed in 3.11
- agents/tools/payments/, agents/tools/payments/x402/, agents/tools/payments/x402/charge-for-http-content/, agents/tools/payments/x402/charge-for-mcp-tools/, agents/tools/payments/x402/pay-from-agents-sdk/, agents/tools/payments/x402/pay-with-tool-plugins/
- agents/tools/payments/mpp/, agents/tools/payments/mpp-charge-for-http-content/, agents/tools/payments/mpp/accept-payments/
- ai-gateway/features/machine-payments/, ai-gateway/features/unified-billing/
- ai-crawl-control/features/pay-per-crawl/ (what-is-pay-per-crawl, faq, crawl-pages, set-a-pay-per-crawl-price, manage-payouts), ai-crawl-control/reference/worker-templates/
- wallets/, wallets/faq/
- billing/payment-methods/stablecoin-payments/
- bots/botbase/
- changelog/post/2026-09-30-closed-beta/, changelog/post/2026-09-30-machine-payments/, changelog/post/2026-02-09-agents-sdk-v0.4.0/, changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/, changelog/post/2025-12-10-pay-per-crawl-enhancements/, changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/

API reference: `raw/api/openapi.json` and `raw/api/endpoints.tsv`, tag `Monetization` (10 endpoints, beta).

Blog:
- https://blog.cloudflare.com/x402/ (2025-09-23)
- https://blog.cloudflare.com/monetization-gateway/ (2026-07-01)
- https://blog.cloudflare.com/wallets/ (2026-08-04)
- https://blog.cloudflare.com/monetization-gateway-beta/ (2026-09-30)

External:
- https://www.coinbase.com/blog/coinbase-and-cloudflare-will-launch-x402-foundation (2025-09-23)
- https://www.cloudflare.com/press/press-releases/2025/cloudflare-introduces-net-dollar-to-support-a-new-business-model-for-the-ai-driven-internet/ (2025-09-25)
- https://www.ledgerinsights.com/cloudflare-to-launch-net-stablecoin-for-ai-agentic-payments (2025-09-26)
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-gives-ai-agents-an-identity-and-a-wallet/ (2026-08-04)
- https://ffnews.com/news/cloudflare-launches-wallets-and-cloudflarepay-to-enable-secure-ai-agent-commerce
