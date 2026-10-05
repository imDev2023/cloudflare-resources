---
description: Conditional SQL functions for Analytics Engine queries.
title: Conditional functions
image: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/og.png?v=76c21573bf8cad4a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Conditional functions

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## if

Usage:

```sql
if(<condition>, <true_expression>, <false_expression>)
```

Returns `<true_expression>` if `<condition>` evaluates to true, else returns `<false_expression>`.

Example:

```sql
if(temp > 20, 'It is warm', 'Bring a jumper')
```
