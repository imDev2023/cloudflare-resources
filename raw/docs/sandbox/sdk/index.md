---
description: Documentation for existing applications on Sandbox SDK 0.x, the Sandbox class in @cloudflare/sandbox that runs commands, files, and services in a container.
title: Sandbox SDK 0.x
image: https://developers.cloudflare.com/sandbox/sdk/og.png?v=6d27845d4289e552
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/sandbox/llms.txt  
> Use this file to discover all available pages before exploring further.

# Sandbox SDK 0.x

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/sandbox/sdk/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Available on Workers Paid plan

Note

These pages document `@cloudflare/sandbox` 0.x for existing applications. Version 1.0 is a different library that works with a container you start from a Durable Object. To move an existing application to 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/). To start new work, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/).

Sandbox SDK 0.x gives your [Worker](https://developers.cloudflare.com/workers/) a `Sandbox` class built on [Containers](https://developers.cloudflare.com/containers/). A sandbox starts its container on first use, and its methods run commands, manage files, run background processes, and expose services in that container.

## Move to 1.0

### [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/)

Move a 0.12 application to a Durable Object that starts its own container.

### [API map](https://developers.cloudflare.com/sandbox/sdk/migrate/api-map/)

Find what replaces each 0.12 API in 1.0.

## Maintain a 0.x application

### [Getting started](https://developers.cloudflare.com/sandbox/sdk/get-started/)

Create a Worker that runs Python code in a 0.x sandbox.

### [How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)

Run commands, manage files, expose services, and deploy with Sandbox SDK 0.x.

### [API reference](https://developers.cloudflare.com/sandbox/sdk/api/)

Look up the methods of the 0.x `Sandbox` class.

### [Tutorials](https://developers.cloudflare.com/sandbox/sdk/tutorials/)

Build complete applications with Sandbox SDK 0.x.

## Coding agents

Install [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills) for your agent ([Agent setup](https://developers.cloudflare.com/agent-setup/)). Use **`sandbox-stable`** with these Sandbox SDK docs.
