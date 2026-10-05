---
description: Scalar functions to implement conditional logic
title: Conditional functions
image: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/conditional/og.png?v=53555e8ae1c109ea
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-pipelines/llms.txt  
> Use this file to discover all available pages before exploring further.

# Conditional functions

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/conditional/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

*Basin Pipelines scalar function implementations are based on [Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `coalesce`

Returns the first of its arguments that is not *null*. Returns *null* if all arguments are *null*. This function is often used to substitute a default value for *null* values.

```plaintext
coalesce(expression1[, ..., expression_n])
```

**Arguments**

- **expression1, expression\_n**: Expression to use if previous expressions are *null*. Can be a constant, column, or function, and any combination of arithmetic operators. Pass as many expression arguments as necessary.

## `nullif`

Returns *null* if *expression1* equals *expression2*; otherwise it returns *expression1*. This can be used to perform the inverse operation of [`coalesce`](#coalesce).

```plaintext
nullif(expression1, expression2)
```

**Arguments**

- **expression1**: Expression to compare and return if equal to expression2. Can be a constant, column, or function, and any combination of arithmetic operators.
- **expression2**: Expression to compare to expression1. Can be a constant, column, or function, and any combination of arithmetic operators.

## `nvl`

Returns *expression2* if *expression1* is NULL; otherwise it returns *expression1*.

```plaintext
nvl(expression1, expression2)
```

**Arguments**

- **expression1**: return if expression1 not is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.
- **expression2**: return if expression1 is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.

## `nvl2`

Returns *expression2* if *expression1* is not NULL; otherwise it returns *expression3*.

```plaintext
nvl2(expression1, expression2, expression3)
```

**Arguments**

- **expression1**: conditional expression. Can be a constant, column, or function, and any combination of arithmetic operators.
- **expression2**: return if expression1 is not NULL. Can be a constant, column, or function, and any combination of arithmetic operators.
- **expression3**: return if expression1 is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.

## `ifnull`

*Alias of [nvl](#nvl).*
