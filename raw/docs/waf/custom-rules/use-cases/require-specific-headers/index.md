---
description: Require specific HTTP headers in incoming requests.
title: Require specific HTTP headers
image: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/og.png?v=989b04b8e103a6c2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Require specific HTTP headers

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Many organizations qualify traffic based on the presence of specific HTTP request headers. Use the Rules language [HTTP request header fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/?field-category=Headers&search-term=http.request) to target requests with specific headers.

## Example 1: Require presence of HTTP header

This example custom rule uses the [`http.request.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/) field to look for the presence of an `X-CSRF-Token` header. The [`lower()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lower) transformation function converts the header name to lowercase so that the expression is case-insensitive.

When the `X-CSRF-Token` header is missing, Cloudflare blocks the request.

- **When incoming requests match**:

  Use the expression editor:  
  `not any(lower(http.request.headers.names[*])[*] eq "x-csrf-token") and (http.request.full_uri eq "https://www.example.com/somepath")`
- **Then take action**: *Block*

## Example 2: Require HTTP header with a specific value

This example custom rule uses the [`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/) field to look for the presence of the `X-Example-Header` header and to get its value (if any). When the `X-Example-Header` header is missing or it does not have the value `example-value`, Cloudflare blocks the request.

- **When incoming requests match**:

  Use the expression editor:  
  `not any(http.request.headers["x-example-header"][*] eq "example-value") and (http.request.uri.path eq "/somepath")`
- **Then take action**: *Block*

The keys in the `http.request.headers` field, corresponding to HTTP header names, are in lowercase.

In this example the header name is case-insensitive, but the header value is case-sensitive.
