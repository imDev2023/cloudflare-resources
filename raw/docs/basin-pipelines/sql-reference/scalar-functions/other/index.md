---
description: Miscellaneous scalar functions
title: Other functions
image: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/og.png?v=ab99aa3e240bb0fe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-pipelines/llms.txt  
> Use this file to discover all available pages before exploring further.

# Other functions

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

*Basin Pipelines scalar function implementations are based on [Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `arrow_cast`

Casts a value to a specific Arrow data type:

```plaintext
arrow_cast(expression, datatype)
```

**Arguments**

- **expression**: Expression to cast. Can be a constant, column, or function, and any combination of arithmetic or string operators.
- **datatype**: [Arrow data type ↗︎](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) name to cast to, as a string. The format is the same as that returned by \[`arrow_typeof`]

**Example**

```plaintext
> select arrow_cast(-5, 'Int8') as a,
  arrow_cast('foo', 'Dictionary(Int32, Utf8)') as b,
  arrow_cast('bar', 'LargeUtf8') as c,
  arrow_cast('2023-01-02T12:53:02', 'Timestamp(Microsecond, Some("+08:00"))') as d
  ;
+----+-----+-----+---------------------------+
| a  | b   | c   | d                         |
+----+-----+-----+---------------------------+
| -5 | foo | bar | 2023-01-02T12:53:02+08:00 |
+----+-----+-----+---------------------------+
1 row in set. Query took 0.001 seconds.
```

## `arrow_typeof`

Returns the name of the underlying [Arrow data type ↗︎](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) of the expression:

```plaintext
arrow_typeof(expression)
```

**Arguments**

- **expression**: Expression to evaluate. Can be a constant, column, or function, and any combination of arithmetic or string operators.

**Example**

```plaintext
> select arrow_typeof('foo'), arrow_typeof(1);
+---------------------------+------------------------+
| arrow_typeof(Utf8("foo")) | arrow_typeof(Int64(1)) |
+---------------------------+------------------------+
| Utf8                      | Int64                  |
+---------------------------+------------------------+
1 row in set. Query took 0.001 seconds.
```
