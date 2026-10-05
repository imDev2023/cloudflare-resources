---
description: Let your customers deploy their own code on your platform with isolated execution environments.
title: Enable customer code deployment
image: https://developers.cloudflare.com/use-cases/saas/code-deployment/og.png?v=805a9f87eba9d616
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/use-cases/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable customer code deployment

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/use-cases/saas/code-deployment/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

SaaS platforms often need to let customers run their own code — custom logic, integrations, webhooks — without compromising tenant isolation or platform stability. Cloudflare Workers for Platforms runs each customer's code in a separate V8 isolate with dispatch routing based on hostname, path, or header.

## Solutions

### Workers for Platforms

Deploy isolated Workers execution environments for your customers. [Learn more about Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/).

- **Tenant isolation** - Each customer's code runs in a separate V8 isolate with no shared memory between tenants
- **Custom logic** - Customers can deploy their own Workers to extend or customize your platform's behavior
- **Dispatch routing** - Route incoming requests to the correct customer Worker based on hostname, path, or header
- **Observability** - Tail Workers capture logs and errors across all tenant code from a single integration

## Get started

1. [Workers for Platforms get started](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/)
2. [Configure Dispatch Namespaces](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/)
