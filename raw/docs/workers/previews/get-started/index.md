---
description: Create a Worker Preview and configure preview-safe settings with Wrangler.
title: Get started
image: https://developers.cloudflare.com/workers/previews/get-started/og.png?v=2eb6967b7d478d0d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Get started

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/previews/get-started/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can create a Preview for a new or existing Worker. You do not need to deploy a Worker to production before creating its first Preview.

## Before you begin

Worker Previews requires `Wrangler 4.135.0` or later. Update the project dependency because project commands do not use a newer global installation.

npmyarnpnpmbun

```
npm i -D wrangler@latest
```

```
yarn add -D wrangler@latest
```

```
pnpm add -D wrangler@latest
```

```
bun add -d wrangler@latest
```

## Step 1: Configure Preview settings

Add a `previews` block to your Wrangler configuration file. Top-level settings define production, and the `previews` block defines Preview settings. The `previews` block can be empty if your Preview does not need separate settings.

```jsonc
{
  // ...
  "vars": {
    "ENVIRONMENT": "production"
  },
  // ...
  "previews": {
    // ...
    "vars": {
      "ENVIRONMENT": "preview"
    }
    // ...
  }
}
```

```toml
[vars]
ENVIRONMENT = "production"

[previews.vars]
ENVIRONMENT = "preview"
```

To determine which settings belong at the top level or in `previews`, refer to [What goes in the `previews` block](https://developers.cloudflare.com/workers/previews/configuration/#what-goes-in-the-previews-block).

Settings that you add or import in the dashboard must also be copied to your [Wrangler configuration file](https://developers.cloudflare.com/workers/previews/configuration/#dashboard-configuration).

## Step 2: Deploy a Preview

Run the same Preview command locally or in your existing CI workflow:

npmyarnpnpm

```
npx wrangler preview
```

```
yarn wrangler preview
```

```
pnpm wrangler preview
```

The Preview name defaults to your current Git branch. To choose a name, add `--name <PREVIEW_NAME>`.

To post Preview URLs automatically to pull requests or merge requests, [connect your Git repository](https://developers.cloudflare.com/workers/ci-cd/builds/#get-started) and use [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-preview-builds). New Workers use Worker Previews by default. If an existing Worker already uses Workers Builds, complete the [one-time setup](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#existing-workers-connected-to-builds).

A successful deployment returns a **Preview URL** that always points to the latest changes. It also returns a **Unique Deployment URL** for each deployment, so you can access earlier versions in the Preview's deployment history.

## Next steps

- [Configuration](https://developers.cloudflare.com/workers/previews/configuration/) - Configure variables, secrets, bindings, and Previews Base.
- [Resources and isolation](https://developers.cloudflare.com/workers/previews/resources/) - Decide which resources to share or isolate.
- [Limitations](https://developers.cloudflare.com/workers/previews/resources/#limitations) - Review current support gaps and workarounds.
- [Examples](https://developers.cloudflare.com/workers/previews/examples/) - Add Preview deployments to CI.
