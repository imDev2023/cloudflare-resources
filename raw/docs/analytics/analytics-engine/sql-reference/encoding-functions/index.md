---
description: Encoding SQL functions for Analytics Engine queries.
title: Encoding functions
image: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/og.png?v=118ae30c51b8339e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Encoding functions

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## bin New

Usage:

```sql
bin(<expression>)
```

`bin` returns a string containing the binary representation of its argument.

Examples:

```sql
-- get the binary representation of 1
bin(1)
-- get the binary representation of a string`
bin('abc')
```

## hex New

Usage:

```sql
hex(<expression>)
```

`hex` returns a string containing the hexadecimal representation of its argument.

Examples:

```sql
-- get the hexadecimal representation of 1
hex(1)
-- get the hexadecimal representation of a string`
hex('abc')
```
