---
description: Supported bindings per development mode
title: Supported bindings per development mode
image: https://developers.cloudflare.com/workers/local-development/bindings-per-env/og.png?v=2340d9abe6ad6ebf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Supported bindings per development mode

Last updated Jun 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/local-development/bindings-per-env/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Local development

**Local simulations**: During local development, your Worker code always executes locally and bindings connect to locally simulated resources [by default](https://developers.cloudflare.com/workers/local-development/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

**Remote binding connections:**: Allows you to connect to remote resources on a [per-binding basis](https://developers.cloudflare.com/workers/local-development/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

| Binding | Local simulations | Remote binding connections |
| --- | --- | --- |
| **AI** | ❌ | ✅ |
| **Assets** | ✅ | ❌ |
| **Analytics Engine** | ✅ | ❌ |
| **Browser Run** | ✅ | ✅ |
| **D1** | ✅ | ✅ |
| **Durable Objects** | ✅ | ❌ <sup>[1](#user-content-fn-1)</sup> |
| **Containers** | ✅ | ❌ |
| **Email Bindings** | ✅ | ✅ |
| **Hyperdrive** | ✅ | ❌ |
| **Images** | ✅ | ✅ |
| **KV** | ✅ | ✅ |
| **Media Transformations** | ❌ | ✅ |
| **mTLS** | ❌ | ✅ |
| **Queues** | ✅ | ✅ |
| **R2** | ✅ | ✅ |
| **Rate Limiting** | ✅ | ❌ |
| **Service Bindings (multiple Workers)** | ✅ | ✅ |
| **Vectorize** | ❌ | ✅ |
| **Workflows** | ✅ | ❌ |

## Remote development

During remote development, all of your Worker code is uploaded and executed on Cloudflare's infrastructure, and bindings always connect to remote resources. **We recommend using local development with remote binding connections instead** for faster iteration and debugging.

Supported only in [`wrangler dev --remote`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) - there is **no Vite plugin equivalent**.

| Binding | Remote development |
| --- | --- |
| **AI** | ✅ |
| **Assets** | ✅ |
| **Analytics Engine** | ✅ |
| **Browser Run** | ✅ |
| **D1** | ✅ |
| **Durable Objects** | ✅ |
| **Containers** | ❌ |
| **Email Bindings** | ✅ |
| **Hyperdrive** | ✅ |
| **Images** | ✅ |
| **KV** | ✅ |
| **Media Transformations** | ✅ |
| **mTLS** | ✅ |
| **Queues** | ❌ |
| **R2** | ✅ |
| **Rate Limiting** | ✅ |
| **Service Bindings (multiple Workers)** | ✅ |
| **Vectorize** | ✅ |
| **Workflows** | ❌ |

## Footnotes

1. Refer to [Using remote resources with Durable Objects and Workflows](https://developers.cloudflare.com/workers/local-development/#using-remote-resources-with-durable-objects-and-workflows) for recommended workarounds. [↩](#user-content-fnref-1)
