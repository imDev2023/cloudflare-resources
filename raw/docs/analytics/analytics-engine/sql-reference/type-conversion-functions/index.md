---
description: Type conversion SQL functions for Analytics Engine.
title: Type conversion functions
image: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/og.png?v=8ed8bd1cc8f9eacf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Type conversion functions

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## toUInt8 New

Usage:

```sql
toUInt8(<expression>)
```

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer.

Behaviour for negative numbers is undefined.

## toUInt32

Usage:

```sql
toUInt32(<expression>)
```

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 32 bit integer.

Behaviour for negative numbers is undefined.
