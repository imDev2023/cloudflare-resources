---
description: Expose Sandbox services on public preview URLs with sandbox.tunnels — zero-config quick tunnels on *.trycloudflare.com, plus named tunnels that bind a persistent custom hostname backed by a Cloudflare Tunnel.
title: Share sandbox previews through Cloudflare Tunnel
image: https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/og.png?v=21fe78533972fca4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 29, 2026

## Share sandbox previews through Cloudflare Tunnel

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) can expose a service running inside the container on a public preview URL through the `sandbox.tunnels` namespace. The SDK uses `cloudflared` inside the sandbox so you can share a running service without configuring `exposePort()` or a custom domain.

By default, `sandbox.tunnels.get(port)` creates a [quick tunnel ↗︎](https://try.cloudflare.com/) on a zero-config `*.trycloudflare.com` URL — no Cloudflare account, DNS record, or custom domain required. This is perfect for quick development and for `.workers.dev` deployments.

```js
import { getSandbox } from "@cloudflare/sandbox";

const sandbox = getSandbox(env.Sandbox, "my-sandbox");
await sandbox.startProcess("python -m http.server 8080");

const tunnel = await sandbox.tunnels.get(8080);
console.log(tunnel.url); // → https://random-words-here.trycloudflare.com
```

```ts
import { getSandbox } from "@cloudflare/sandbox";

const sandbox = getSandbox(env.Sandbox, "my-sandbox");
await sandbox.startProcess("python -m http.server 8080");

const tunnel = await sandbox.tunnels.get(8080);
console.log(tunnel.url); // → https://random-words-here.trycloudflare.com
```

#### Named tunnels

For more control you can create a named tunnel through `sandbox.tunnels.get(port, { name })`. A named tunnel binds a hostname (`<name>.<your-zone>`) backed by a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and a CNAME record on your zone resulting in something like [https://my-app-preview.example.com ↗︎](https://my-app-preview.example.com).

Unlike quick tunnels, which generate a new random URL each time, a named tunnel produces a persistent URL that survives container restarts. This makes named tunnels suitable for production use cases where you want control over the tunnel and it's origin.

```js
const tunnel = await sandbox.tunnels.get(8080, { name: "my-app-preview" });
console.log(tunnel.url); // → https://my-app-preview.example.com
```

```ts
const tunnel = await sandbox.tunnels.get(8080, { name: "my-app-preview" });
console.log(tunnel.url); // → https://my-app-preview.example.com
```

Calling `sandbox.destroy()` tears down the Cloudflare Tunnel and the associated DNS record alongside the container, so you do not leave dangling tunnels or records behind.

#### Upgrade

To update to the latest version:

npmyarnpnpmbun

```
npm i @cloudflare/sandbox@latest
```

```
yarn add @cloudflare/sandbox@latest
```

```
pnpm add @cloudflare/sandbox@latest
```

```
bun add @cloudflare/sandbox@latest
```

For full API details, refer to the [Sandbox tunnels reference](https://developers.cloudflare.com/sandbox/api/tunnels/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/#page","headline":"Share sandbox previews through Cloudflare Tunnel","description":"Expose Sandbox services on public preview URLs with sandbox.tunnels — zero-config quick tunnels on *.trycloudflare.com, plus named tunnels that bind a persistent custom hostname backed by a Cloudflare Tunnel.","url":"https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/og.png?v=21fe78533972fca4","dateModified":"2026-05-29","datePublished":"2026-05-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
