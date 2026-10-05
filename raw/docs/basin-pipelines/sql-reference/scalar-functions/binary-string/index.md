---
description: Scalar functions for manipulating binary strings
title: Binary string functions
image: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/binary-string/og.png?v=960f6441cecb12ac
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-pipelines/llms.txt  
> Use this file to discover all available pages before exploring further.

# Binary string functions

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/binary-string/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

*Basin Pipelines scalar function implementations are based on [Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `encode`

Encode binary data into a textual representation.

```plaintext
encode(expression, format)
```

**Arguments**

- **expression**: Expression containing string or binary data
- **format**: Supported formats are: `base64`, `hex`

**Related functions**: [decode](#decode)

## `decode`

Decode binary data from textual representation in string.

```plaintext
decode(expression, format)
```

**Arguments**

- **expression**: Expression containing encoded string data
- **format**: Same arguments as [encode](#encode)

**Related functions**: [encode](#encode)
