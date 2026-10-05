---
description: Available Container instance types and limits for memory, vCPU, disk, image storage, and snapshots.
title: Limits and Instance Types
image: https://developers.cloudflare.com/containers/platform/limits/og.png?v=976edb39343c58ee
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/containers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Limits and Instance Types

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/containers/platform/limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Instance Types

The memory, vCPU, and disk space for Containers are set through instance types. You can use one of six predefined instance types or configure a [custom instance type](#custom-instance-types).

| Instance Type | vCPU | Memory | Disk |
| --- | --- | --- | --- |
| lite | 1/16 | 256 MiB | 2 GB |
| basic | 1/4 | 1 GiB | 4 GB |
| standard-1 | 1/2 | 4 GiB | 8 GB |
| standard-2 | 1 | 6 GiB | 12 GB |
| standard-3 | 2 | 8 GiB | 16 GB |
| standard-4 | 4 | 12 GiB | 20 GB |

For an application that uses the [`default` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/), specify the size with the [`instance_type` property](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) in your Worker's Wrangler configuration file. For the `durable_object` policy, pass the named size to `ctx.container.start()` with the runtime `instance` property.

Note

The `dev` and `standard` instance types are preserved for backward compatibility and are aliases for `lite` and `standard-1`, respectively.

### Custom Instance Types

In addition to the predefined instance types, you can configure custom instance types. Field names depend on where you configure the size. Wrangler configuration for the `default` policy uses `vcpu`, `memory_mib`, and `disk_mb`. A `ctx.container.start()` call for the `durable_object` policy uses `vcpu`, `memoryMib`, and `diskMb`.

Refer to the [Wrangler configuration documentation](https://developers.cloudflare.com/workers/wrangler/configuration/#custom-instance-types) or [scheduling policy documentation](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#choose-an-instance-size-at-runtime) for examples.

Custom instance types have the following constraints:

| Resource | Limit |
| --- | --- |
| Minimum vCPU | 1 |
| Maximum vCPU | 4 |
| Maximum Memory | 12 GiB |
| Maximum Disk | 20 GB |
| Memory to vCPU ratio | Minimum 3 GiB memory per vCPU |

For workloads requiring less than 1 vCPU, use the predefined instance types such as `lite` or `basic`.

If you need larger instance sizes or higher account-level limits, contact your account team, file a support ticket, or fill out [this form ↗︎](https://forms.gle/CscdaEGuw5Hb6H2s7).

## Account limits

The following limits apply per account:

| Resource | Limit |
| --- | --- |
| Concurrent memory | 6 TiB |
| Concurrent vCPU | 1,500 |
| Concurrent disk | 30 TB |
| Image size | Same as [instance disk space](#instance-types) |
| Total image storage per account | 50 GB <sup>[1](#user-content-fn-1)</sup> |

## Snapshot limits

The following limits apply to [Container snapshots](https://developers.cloudflare.com/containers/guides/snapshots/):

| Resource | Limit |
| --- | --- |
| Maximum snapshot size | 20 GB |
| Snapshot retention | 30 days from creation or the most recent restore |

Restoring a snapshot refreshes its 30-day time-to-live.

## Footnotes

1. Delete container images with `wrangler containers delete` to free up space. If you delete a container image and then [roll back](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) your Worker to a previous version, this version may no longer work. [↩](#user-content-fnref-1)
