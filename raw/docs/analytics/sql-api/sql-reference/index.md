---
description: Reference for the SQL syntax supported by the SQL API.
title: SQL language reference
image: https://developers.cloudflare.com/analytics/sql-api/sql-reference/og.png?v=8e7234eb8b0d8a77
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# SQL language reference

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/sql-api/sql-reference/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The SQL API supports a read-only subset of SQL for analytics queries. SQL keywords and function names are case-insensitive. Dataset and field names are case-sensitive.

Every query must read one schema-qualified dataset and must include an account or zone scope and a lower time bound. For HTTP API requests, you can provide scope and time bounds in SQL or through the JSON request fields. Workers binding queries are the exception: the binding supplies account scope automatically, so include only the time bound in SQL. For example:

```sql
SELECT
  clientRequestHttpHost AS host,
  COUNT(*) AS requests
FROM events.httpRequests
WHERE accountTag = '<ACCOUNT_TAG>'
  AND timestamp >= NOW() - INTERVAL '1' HOUR
GROUP BY clientRequestHttpHost
ORDER BY requests DESC
LIMIT 10
```

## Reference

- [Statements and clauses](https://developers.cloudflare.com/analytics/sql-api/sql-reference/statements/)
- [Operators](https://developers.cloudflare.com/analytics/sql-api/sql-reference/operators/)
- [Functions](https://developers.cloudflare.com/analytics/sql-api/sql-reference/functions/)
- [Data types and literals](https://developers.cloudflare.com/analytics/sql-api/sql-reference/data-types/)

## Unsupported features

The SQL API does not support arbitrary ClickHouse SQL. Unsupported features include:

- Data modification or definition statements, including `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, and `DROP`.
- Joins, unions, common table expressions, and general subqueries. One restricted derived-table projection is supported.
- Window functions.
- Row-level `SELECT DISTINCT`. `COUNT`, `SUM`, and `AVG` support `DISTINCT` on unsampled datasets and Workers Analytics Engine datasets.
- `FETCH`. ClickHouse-backed datasets support `OFFSET` with `LIMIT`.
- `EXPLAIN`, `ANALYZE`, `DESCRIBE`, `VALUES`, and `UNNEST`.
- `SIMILAR TO`, `LIKE ... ESCAPE`, and user-authored casts.
- Aggregate `FILTER` and aggregate-local `ORDER BY` clauses.

The API returns an HTTP `422` response when a statement contains unsupported syntax.
