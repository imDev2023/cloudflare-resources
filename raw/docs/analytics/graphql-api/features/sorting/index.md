---
description: Sort GraphQL Analytics API query results.
title: Sorting
image: https://developers.cloudflare.com/analytics/graphql-api/features/sorting/og.png?v=e06e125bef11f500
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Sorting

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/sorting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can specify the order of the query result elements using the `orderBy` argument. By default, the results are sorted by the primary key of a dataset (table). If you specify another field to sort on, the primary key is also used in the sorting key, allowing results to remain consistent for pagination.

The default order for an aggregated dataset is by the fields on which the aggregated data is grouped. If you specify a different order, the aggregation group is appended to your specified ordering.

Note

Ordering within nested structures is not supported.

## Examples

### Raw data sorting

```graphql
firewallEventsAdaptive (orderBy: [clientCountryName_ASC]) {
    clientCountryName
}
```

### Raw data sorting using multiple fields

```graphql
firewallEventsAdaptive (orderBy: [clientCountryName_ASC, datetime_DESC]) {
    clientCountryName
    datetime
}
```

### Group sorting by aggregation function

```graphql
httpRequests1hGroups (orderBy: [sum_bytes_DESC]){
    sum {
        bytes
        requests
    }
    dimensions {
        datetime
    }
}
```
