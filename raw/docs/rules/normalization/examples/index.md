---
description: Examples of the impact of different URL normalization settings in the URLs of incoming requests.
title: URL normalization examples
image: https://developers.cloudflare.com/rules/normalization/examples/og.png?v=f3179b19dc20a4c7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# URL normalization examples

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/normalization/examples/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following table shows how different [URL normalization settings](https://developers.cloudflare.com/rules/normalization/settings/) affect request URLs before they pass to other Cloudflare features and to the origin server:

| Incoming URL | Normalization type | Normalize incoming URLs | Normalize URLs to origin | URL at Cloudflare's network | URL passed to origin server |
| --- | --- | --- | --- | --- | --- |
| `www.example.com/hello` | (any) | *Off* | *Off* | `www.example.com/hello` | `www.example.com/hello` |
| `www.example.com/hello` | (any) | *On* | *Off* | `www.example.com/hello` | `www.example.com/hello` |
| `www.example.com/hello` | (any) | *On* | *On* | `www.example.com/hello` | `www.example.com/hello` |
| `example.com/%68ello` | (any) | *Off* | *Off* | `example.com/%68ello` | `example.com/%68ello` |
| `example.com/%68ello` | (any) | *On* | *Off* | `example.com/hello` | `example.com/%68ello` |
| `example.com/%68ello` | (any) | *On* | *On* | `example.com/hello` | `example.com/hello` |
| `example.com/%68ello//pa\th` | *RFC-3986* | *Off* | *Off* | `example.com/%68ello//pa\th` | `example.com/%68ello//pa\th` |
| `example.com/%68ello//pa\th` | *RFC-3986* | *On* | *Off* | `example.com/hello//pa%5Cth` | `example.com/%68ello//pa\th` |
| `example.com/%68ello//pa\th` | *RFC-3986* | *On* | *On* | `example.com/hello//pa%5Cth` | `example.com/hello//pa%5Cth` |
| `example.com/%68ello//pa\th` | *Cloudflare* | *Off* | *Off* | `example.com/%68ello//pa\th` | `example.com/%68ello//pa\th` |
| `example.com/%68ello//pa\th` | *Cloudflare* | *On* | *Off* | `example.com/hello/pa/th` | `example.com/%68ello//pa\th` |
| `example.com/%68ello//pa\th` | *Cloudflare* | *On* | *On* | `example.com/hello/pa/th` | `example.com/hello/pa/th` |
| `example.com/hello//../path` | *RFC-3986* | *On* | *On* | `example.com/hello/path` | `example.com/hello/path` |
| `example.com/hello//../path` | *Cloudflare* | *On* | *On* | `example.com/path` | `example.com/path` |
| `example.com/hello/\../path` | *RFC-3986* | *On* | *On* | `example.com/hello/%5C../path` | `example.com/hello/%5C../path` |
| `example.com/hello/\../path` | *Cloudflare* | *On* | *On* | `example.com/path` | `example.com/path` |
