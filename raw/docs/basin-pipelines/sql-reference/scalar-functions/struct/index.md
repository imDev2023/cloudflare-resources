---
description: Scalar functions for manipulating structs
title: Struct functions
image: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/og.png?v=0890e3f681e16c43
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-pipelines/llms.txt  
> Use this file to discover all available pages before exploring further.

# Struct functions

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

*Basin Pipelines scalar function implementations are based on [Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `struct`

Returns an Arrow struct using the specified input expressions. Fields in the returned struct use the `cN` naming convention. For example: `c0`, `c1`, `c2`, etc.

```plaintext
struct(expression1[, ..., expression_n])
```

For example, this query converts two columns `a` and `b` to a single column with a struct type of fields `c0` and `c1`:

```plaintext
select * from t;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+

select struct(a, b) from t;
+-----------------+
| struct(t.a,t.b) |
+-----------------+
| {c0: 1, c1: 2}  |
| {c0: 3, c1: 4}  |
+-----------------+
```

#### Arguments

- **expression\_n**: Expression to include in the output struct. Can be a constant, column, or function, and any combination of arithmetic or string operators.
