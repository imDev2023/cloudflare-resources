---
description: Supported header name and value formats for response header modifications.
title: Format of HTTP response header names and values
image: https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/og.png?v=74792821412d0972
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Format of HTTP response header names and values

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The **name** of the HTTP response header you want to set or remove can only contain:

- Alphanumeric characters: `a`- `z`, `A`- `Z`, and `0`- `9`
- The following special characters: `-` and `_`

The **value** of the HTTP response header you want to set can only contain:

- Alphanumeric characters: `a`- `z`, `A`- `Z`, and `0`- `9`
- The following special characters: ``_ :;.,\/"'?!(){}[]@<>=-+*#$&`|~^%``

The **length** of the HTTP response header can be a maximum of 4 KB (\~4,096 characters).
