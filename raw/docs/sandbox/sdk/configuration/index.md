---
description: Configure Sandbox SDK 0.x deployments with Wrangler, Dockerfiles, environment variables, and transport modes.
title: Configuration
image: https://developers.cloudflare.com/sandbox/sdk/configuration/og.png?v=e954ba36141524b7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/sandbox/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configuration

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/sandbox/sdk/configuration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Configure your Sandbox SDK deployment with Wrangler, customize container images, and manage environment variables.

### [Wrangler configuration](https://developers.cloudflare.com/sandbox/sdk/configuration/wrangler/)

Configure Durable Objects bindings, container images, and Worker settings in wrangler.jsonc.

### [Dockerfile reference](https://developers.cloudflare.com/sandbox/sdk/configuration/dockerfile/)

Customize the sandbox container image with your own packages, tools, and configurations.

### [Environment variables](https://developers.cloudflare.com/sandbox/sdk/configuration/environment-variables/)

Pass configuration and secrets to your sandboxes using environment variables.

### [Transport modes](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/)

Configure HTTP or RPC transport to optimize communication and avoid subrequest limits.

### [Sandbox options](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/)

Configure sandbox behavior with options like `keepAlive` for long-running processes.

## Related resources

- [Get Started guide](https://developers.cloudflare.com/sandbox/sdk/get-started/) - Initial setup walkthrough
- [Wrangler documentation](https://developers.cloudflare.com/workers/wrangler/) - Complete Wrangler reference
- [Docker documentation ↗︎](https://docs.docker.com/engine/reference/builder/) - Dockerfile syntax
- [Security model](https://developers.cloudflare.com/sandbox/sdk/concepts/security/) - Understanding environment isolation
