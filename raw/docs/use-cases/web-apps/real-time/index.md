---
description: Build interactive applications with WebSockets, real-time collaboration, and live updates.
title: Add real-time features
image: https://developers.cloudflare.com/use-cases/web-apps/real-time/og.png?v=b6cfac389bf6117a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/use-cases/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add real-time features

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/use-cases/web-apps/real-time/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Real-time features, such as live chat, collaborative editing, and multiplayer interactions, require persistent connections and strongly consistent state. Cloudflare Durable Objects maintain WebSocket connections and coordinate shared state, while Queues handle background event processing.

## Solutions

### Durable Objects

Stateful objects with strongly consistent storage and coordination. [Learn more about Durable Objects](https://developers.cloudflare.com/durable-objects/).

- **WebSocket support** - Maintain persistent connections and broadcast messages across clients in real time
- **Collaborative editing** - Build multiplayer and co-editing experiences with strongly consistent shared state
- **Strong consistency** - Coordinate state across many concurrent connections with transactional guarantees

### Queues

Reliable message queuing and background processing for Workers. [Learn more about Queues](https://developers.cloudflare.com/queues/).

- **Event processing** - Handle webhooks and background jobs reliably without blocking the main request path

## Get started

1. [Durable Objects get started](https://developers.cloudflare.com/durable-objects/get-started/)
2. [WebSocket connections with Durable Objects](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/)
3. [Queues get started](https://developers.cloudflare.com/queues/get-started/)
