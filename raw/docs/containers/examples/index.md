---
description: Code examples showing how to use Containers with Workers for stateless routing, cron jobs, WebSockets, and more.
title: Examples
image: https://developers.cloudflare.com/containers/examples/og.png?v=e9cf0d7d69da226c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/containers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Examples

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/containers/examples/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Build with Containers using the `durable_object` scheduling policy. Each example configures a named image and starts it from a Durable Object with the [Container API](https://developers.cloudflare.com/containers/api/durable-object-container/).

Start with [Stateless instances](https://developers.cloudflare.com/containers/examples/stateless/) for HTTP routing, or [Cron container](https://developers.cloudflare.com/containers/examples/cron/) for a scheduled task.

[**Static frontend, container backend** A simple frontend app with a containerized backend](https://developers.cloudflare.com/containers/examples/container-backend/)

[**Cron container** Running a container on a schedule using Cron Triggers](https://developers.cloudflare.com/containers/examples/cron/)

[**More examples** Various examples calling Containers directly from Durable Objects](https://developers.cloudflare.com/containers/examples/durable-object-interface/)

[**Environment variables and secrets** Pass in environment variables and secrets to your container](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/)

[**Mount R2 buckets with FUSE** Mount R2 buckets as filesystems using FUSE in Containers](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/)

[**Stateless instances** Run multiple instances across Cloudflare's network](https://developers.cloudflare.com/containers/examples/stateless/)

[**Monitor container lifecycle** Execute Workers code in reaction to Container status changes](https://developers.cloudflare.com/containers/examples/status-hooks/)

[**WebSocket to container** Forwarding a Websocket request to a Container](https://developers.cloudflare.com/containers/examples/websocket/)
