---
description: The raw HTTP URI arguments associated with a request represented as a Map (associative array).
title: raw.http.request.uri.args
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# raw.http.request.uri.args

`raw.http.request.uri.args``Map<Array<String>>`

The raw HTTP URI arguments associated with a request represented as a Map (associative array).

This is the raw field version of the [`http.request.uri.args`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Categories:
- Request
- URI
- Raw fields
