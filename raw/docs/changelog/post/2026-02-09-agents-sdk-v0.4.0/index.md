---
description: The latest release of the Agents SDK brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.
title: "Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers"
image: https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/og.png?v=dbca6f0117e01f3d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 9, 2026

## Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.

#### Readonly connections

Agents can now restrict WebSocket clients to read-only access, preventing them from modifying agent state. This is useful for dashboards, spectator views, or any scenario where clients should observe but not mutate.

New hooks: `shouldConnectionBeReadonly`, `setConnectionReadonly`, `isConnectionReadonly`. Readonly connections block both client-side `setState()` and mutating `@callable()` methods, and the readonly flag survives hibernation.

```js
class MyAgent extends Agent {
	shouldConnectionBeReadonly(connection) {
		// Make spectators readonly
		return connection.url.includes("spectator");
	}
}
```

```ts
class MyAgent extends Agent {
	shouldConnectionBeReadonly(connection) {
		// Make spectators readonly
		return connection.url.includes("spectator");
	}
}
```

#### Custom MCP OAuth providers

The new `createMcpOAuthProvider` method on the `Agent` class allows subclasses to override the default OAuth provider used when connecting to MCP servers. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.

```js
class MyAgent extends Agent {
	createMcpOAuthProvider(callbackUrl) {
		return new MyCustomOAuthProvider(this.ctx.storage, this.name, callbackUrl);
	}
}
```

```ts
class MyAgent extends Agent {
	createMcpOAuthProvider(callbackUrl: string): AgentMcpOAuthProvider {
		return new MyCustomOAuthProvider(this.ctx.storage, this.name, callbackUrl);
	}
}
```

#### MCP SDK upgrade to 1.26.0

Upgraded the MCP SDK to 1.26.0 to prevent cross-client response leakage. Stateless MCP Servers should now create a new `McpServer` instance per request instead of sharing a single instance. A guard is added in this version of the MCP SDK which will prevent connection to a Server instance that has already been connected to a transport. Developers will need to modify their code if they declare their `McpServer` instance as a global variable.

#### MCP OAuth callback URL security fix

Added `callbackPath` option to `addMcpServer` to prevent instance name leakage in MCP OAuth callback URLs. When `sendIdentityOnConnect` is `false`, `callbackPath` is now required — the default callback URL would expose the instance name, undermining the security intent. Also fixes callback request detection to match via the `state` parameter instead of a loose `/callback` URL substring check, enabling custom callback paths.

#### Deprecate `onStateUpdate` in favor of `onStateChanged`

`onStateChanged` is a drop-in rename of `onStateUpdate` (same signature, same behavior). `onStateUpdate` still works but emits a one-time console warning per class. `validateStateChange` rejections now propagate a `CF_AGENT_STATE_ERROR` message back to the client.

#### x402 v2 migration

Migrated the x402 MCP payment integration from the legacy `x402` package to `@x402/core` and `@x402/evm` v2.

**Breaking changes for x402 users:**

- Peer dependencies changed: replace `x402` with `@x402/core` and `@x402/evm`
- `PaymentRequirements` type now uses v2 fields (e.g. `amount` instead of `maxAmountRequired`)
- `X402ClientConfig.account` type changed from `viem.Account` to `ClientEvmSigner` (structurally compatible with `privateKeyToAccount()`)

```bash
npm uninstall x402
npm install @x402/core @x402/evm
```

Network identifiers now accept both legacy names and CAIP-2 format:

```ts
// Legacy name (auto-converted)
{
	network: "base-sepolia",
}

// CAIP-2 format (preferred)
{
	network: "eip155:84532",
}
```

**Other x402 changes:**

- `X402ClientConfig.network` is now optional — the client auto-selects from available payment requirements
- Server-side lazy initialization: facilitator connection is deferred until the first paid tool invocation
- Payment tokens support both v2 ( `PAYMENT-SIGNATURE`) and v1 ( `X-PAYMENT`) HTTP headers
- Added `normalizeNetwork` export for converting legacy network names to CAIP-2 format
- Re-exports `PaymentRequirements`, `PaymentRequired`, `Network`, `FacilitatorConfig`, and `ClientEvmSigner` from `agents/x402`

#### Other improvements

- Fix `useAgent` and `AgentClient` crashing when using `basePath` routing
- CORS handling delegated to partyserver's native support (simpler, more reliable)
- Client-side `onStateUpdateError` callback for handling rejected state updates

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/#page","headline":"Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers","description":"The latest release of the Agents SDK brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-09-agents-sdk-v0.4.0/og.png?v=dbca6f0117e01f3d","dateModified":"2026-02-09","datePublished":"2026-02-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
