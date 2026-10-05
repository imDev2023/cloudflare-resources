---
description: Control where your containers run with regional and jurisdictional constraints.
title: Placement
image: https://developers.cloudflare.com/containers/concepts/placement/og.png?v=4dec4faf359f60ac
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/containers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Placement

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/containers/concepts/placement/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, containers run in the location nearest to the incoming request with a pre-fetched image. Use placement constraints to restrict where your containers run for data residency, compliance, or latency requirements.

## Regional constraints

Use the `regions` constraint to limit container placement to specific geographic areas:

| Region | Description | Notes |
| --- | --- | --- |
| `ENAM` | Eastern North America | |
| `WNAM` | Western North America | |
| `EEUR` | Eastern Europe | |
| `WEUR` | Western Europe | |
| `APAC` | Asia Pacific | |
| `SAM` | South America | |
| `ME` | Middle East | Limited capacity |
| `OC` | Oceania | Limited capacity |
| `AFR` | Africa | Limited capacity |

Limited capacity regions (ME, OC, AFR) cannot be used exclusively. Include at least one other region, or contact support for dedicated access.

## Jurisdictional constraints

Use the `jurisdiction` constraint to restrict containers to compliance boundaries:

| Jurisdiction | Regions | Use case |
| --- | --- | --- |
| `eu` | EEUR, WEUR | EU data residency |
| `us` | ENAM, WNAM | US data residency |
| `fedramp` | ENAM, WNAM | FedRAMP regions |

When you specify both `jurisdiction` and `regions`, the regions must be valid for that jurisdiction. For example, specifying `jurisdiction: "eu"` with `regions: ["ENAM"]` is invalid.

## Configure placement

Set placement constraints in your Wrangler configuration:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "containers": [
    {
      "name": "my-container",
      "image": "docker.io/my-org/my-image:latest",
      "constraints": {
        "regions": [
          "ENAM",
          "WNAM"
        ],
        "jurisdiction": "fedramp"
      }
    }
  ]
}
```

```toml
[[containers]]
name = "my-container"
image = "docker.io/my-org/my-image:latest"

[containers.constraints]
regions = ["ENAM", "WNAM"]
jurisdiction = "fedramp"
```

Refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) for more details on how placement affects container startup and routing.
