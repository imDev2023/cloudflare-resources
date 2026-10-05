---
description: Configure data destinations in Basin Pipelines to write to R2 or Basin Catalog.
title: Sinks
image: https://developers.cloudflare.com/basin-pipelines/sinks/og.png?v=a13989b1139fd60a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-pipelines/llms.txt  
> Use this file to discover all available pages before exploring further.

# Sinks

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-pipelines/sinks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Sinks define destinations for your data in Basin Pipelines. They support writing to [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) as Apache Iceberg tables or to [R2](https://developers.cloudflare.com/r2/) as raw JSON or Parquet files.

Sinks provide exactly-once delivery guarantees, ensuring events are never duplicated or dropped. They can be configured to write files frequently for low-latency ingestion or to write larger, less frequent files for better query performance.

## Learn more

### [Manage sinks](https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/)

Create, configure, and delete sinks using Wrangler or the API.

### [Available sinks](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/)

Learn about supported sink destinations and their configuration options.
