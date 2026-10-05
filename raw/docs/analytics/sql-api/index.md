---
description: Query Cloudflare analytics data using SQL.
title: SQL API
image: https://developers.cloudflare.com/analytics/sql-api/og.png?v=eae470f8bdad1c3a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# SQL API

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/sql-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The SQL API lets you query Cloudflare analytics and observability datasets with SQL. Use the API to select fields, filter events, calculate aggregates, group results, and integrate analytics data with your applications.

The SQL API provides `GET` and `POST` query endpoints at:

```txt
https://api.cloudflare.com/client/v4/analytics/sql
```

Send one `SELECT` statement in each request. Use `POST` to send raw SQL or a JSON request with parameters, request-level scope, and a time range. Use `GET` for URL-encoded queries. The API validates the statement against the available datasets and supported SQL language before it executes the query.

Use the [introspection endpoint](https://developers.cloudflare.com/analytics/sql-api/datasets/#discover-datasets) to discover dataset names, categories, descriptions, kinds, columns, and data types. You can also run queries with [`cf sql query`](https://developers.cloudflare.com/analytics/sql-api/get-started/#use-the-cloudflare-cli) and list datasets with `cf sql datasets`.

The SQL API supports a deliberately limited SQL dialect. It does not pass arbitrary SQL through to the underlying data store. For the complete language surface, refer to the [SQL language reference](https://developers.cloudflare.com/analytics/sql-api/sql-reference/).

## Query scope

Every query must include:

- An account or zone scope, supplied in the SQL statement or request body, that identifies the data you are authorized to query.
- A lower time bound that limits how far back the query reads.
- One schema-qualified dataset, such as `events.httpRequests`.

Dataset and field availability depends on your Cloudflare plan and permissions. The API authorizes every account or zone named by a query.

## Get started

Refer to [Get started](https://developers.cloudflare.com/analytics/sql-api/get-started/) to create an API token and run your first query.

To query datasets from a Cloudflare Worker without managing an API token, use the [Workers binding](https://developers.cloudflare.com/analytics/sql-api/workers-binding/).
