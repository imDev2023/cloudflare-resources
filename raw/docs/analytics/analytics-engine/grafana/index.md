---
description: Visualize Workers Analytics Engine data in Grafana.
title: Querying from Grafana
image: https://developers.cloudflare.com/analytics/analytics-engine/grafana/og.png?v=b6e63e39e7079f3c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Querying from Grafana

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/grafana/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Analytics Engine is optimized for powering time series analytics that can be visualized using tools like Grafana. Every event written from the runtime is automatically populated with a `timestamp` field.

## Grafana plugin setup

We recommend the use of the [Altinity plugin for Clickhouse ↗︎](https://grafana.com/grafana/plugins/vertamedia-clickhouse-datasource/) for querying Workers Analytics Engine from Grafana.

Configure the plugin as follows:

- URL: `https://api.cloudflare.com/client/v4/accounts/<account_id>/analytics_engine/sql`. Replace `<account_id>` with your 32 character account ID (available in the Cloudflare dashboard).
- Leave all auth settings off.
- Add a custom header with a name of `Authorization` and value set to `Bearer <token>`. Replace `<token>` with suitable API token string (refer to the [SQL API docs](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#authentication) for more information on this).
- No other options need to be set.

## Querying timeseries data

For use in a dashboard, you usually want to aggregate some metric per time interval. This can be achieved by rounding and then grouping by the `timestamp` field. The following query rounds and groups in this way, and then computes an average across each time interval whilst taking into account [sampling](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#sampling).

```sql
SELECT
    intDiv(toUInt32(timestamp), 60) * 60 AS t,
    blob1 AS label,
    SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric
FROM dataset_name
WHERE 
    timestamp <= NOW() 
    AND timestamp > NOW() - INTERVAL '1' DAY
GROUP BY blob1, t
ORDER BY t
```

The Altinity plugin provides some useful macros that can simplify writing queries of this type. The macros require setting `Column:DateTime` to `timestamp` in the query builder, then they can be used like this:

```sql
SELECT
    $timeSeries AS t,
    blob1 AS label,
    SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric
FROM dataset_name
WHERE $timeFilter
GROUP BY blob1, t
ORDER BY t
```

This query will automatically adjust the rounding time depending on the zoom level and filter to the correct time range that is currently being displayed.
