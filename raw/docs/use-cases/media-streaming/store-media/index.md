---
description: Store media files with zero egress fees using R2.
title: Store media at scale
image: https://developers.cloudflare.com/use-cases/media-streaming/store-media/og.png?v=6d37260f5057ce82
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/use-cases/llms.txt  
> Use this file to discover all available pages before exploring further.

# Store media at scale

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/use-cases/media-streaming/store-media/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Media files are large, and egress fees from traditional cloud storage can be significant at scale. Cloudflare R2 provides S3-compatible object storage with zero egress fees, and Workers lets you build custom processing pipelines for validation, transformation, and routing.

## Solutions

### R2

S3-compatible object storage with zero egress fees. [Learn more about R2](https://developers.cloudflare.com/r2/).

- **Zero egress fees** - No charges for data transferred out, regardless of volume
- **S3 compatibility** - Use any S3-compatible tool, SDK, or library without code changes
- **Direct uploads** - Issue presigned URLs so clients upload directly to R2 without routing through your servers

### Workers

Build and deploy serverless applications on Cloudflare's global network. [Learn more about Workers](https://developers.cloudflare.com/workers/).

- **Custom processing pipelines** - Build media transformation, validation, and routing logic that runs at the edge

## Get started

1. [R2 get started](https://developers.cloudflare.com/r2/get-started/)
2. [Generate presigned URLs](https://developers.cloudflare.com/r2/api/s3/presigned-urls/)
3. [Workers get started](https://developers.cloudflare.com/workers/get-started/)
