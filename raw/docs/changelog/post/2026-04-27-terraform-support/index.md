---
description: Create and manage Pipelines and R2 Data Catalog resources using the Cloudflare Terraform provider v5.19.0.
title: Pipelines and R2 Data Catalog now supported in Terraform
image: https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/og.png?v=398d7bcdaa183cf8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 4, 2026

## Pipelines and R2 Data Catalog now supported in Terraform

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) ingests streaming data via [Workers](https://developers.cloudflare.com/workers/) or HTTP endpoints, transforms it with SQL, and writes it to [R2](https://developers.cloudflare.com/r2/) as Apache Iceberg tables. [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) manages those Iceberg tables, compaction, and compatibility with query engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), and [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/).

You can now create and manage both products using Terraform, supported in the [Cloudflare Terraform provider v5.19.0 ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

This adds four new resources that let you define your entire data pipeline as infrastructure-as-code: a data catalog, a stream for ingestion, a sink that writes to R2 Data Catalog or R2, and a pipeline that connects them with SQL.

The new Terraform resources are:

- [`cloudflare_r2_data_catalog` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog) — enable the data catalog on an R2 bucket
- [`cloudflare_pipeline_stream` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream) — create a stream that receives events via HTTP or Worker bindings
- [`cloudflare_pipeline_sink` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink) — create a sink that writes to R2 Data Catalog or R2
- [`cloudflare_pipeline` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline) — create a pipeline with SQL connecting a stream to a sink

Here is a minimal example that creates a stream, an R2 Data Catalog sink, and a pipeline:

```hcl
resource "cloudflare_pipeline_stream" "my_stream" {
  account_id = var.cloudflare_account_id
  name       = "my_stream"
  format     = { type = "json" }
  schema = {
    fields = [{
      name     = "value"
      type     = "json"
      required = true
    }]
  }
  http           = { enabled = true, authentication = false, cors = {} }
  worker_binding = { enabled = false }
}

resource "cloudflare_pipeline_sink" "my_sink" {
  account_id = var.cloudflare_account_id
  name       = "my_sink"
  type       = "r2_data_catalog"
  format     = { type = "parquet" }
  schema     = { fields = [] }
  config = {
    account_id = var.cloudflare_account_id
    bucket     = "my-pipeline-bucket"
    table_name = "my_table"
    token      = var.catalog_token
  }
}

resource "cloudflare_pipeline" "my_pipeline" {
  account_id = var.cloudflare_account_id
  name       = "my_pipeline"
  sql        = "INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}"
}
```

For a full end-to-end example that includes R2 bucket creation, data catalog setup, and scoped API token provisioning, refer to the [Pipelines Terraform documentation](https://developers.cloudflare.com/basin-pipelines/reference/terraform/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/#page","headline":"Pipelines and R2 Data Catalog now supported in Terraform","description":"Create and manage Pipelines and R2 Data Catalog resources using the Cloudflare Terraform provider v5.19.0.","url":"https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-27-terraform-support/og.png?v=398d7bcdaa183cf8","dateModified":"2026-05-04","datePublished":"2026-05-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
