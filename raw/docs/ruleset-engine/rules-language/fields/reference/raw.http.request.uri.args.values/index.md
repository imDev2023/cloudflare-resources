---
description: The raw values of arguments in the HTTP URI query string.
title: raw.http.request.uri.args.values
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# raw.http.request.uri.args.values

`raw.http.request.uri.args.values``Array<String>`

The raw values of arguments in the HTTP URI query string.

This is the raw field version of the [`http.request.uri.args.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Categories:
- Request
- URI
- Raw fields
