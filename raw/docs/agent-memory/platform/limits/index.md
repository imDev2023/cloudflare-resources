---
description: Review Agent Memory platform limits, including message sizes, naming constraints, and API pagination limits.
title: Limits
image: https://developers.cloudflare.com/agent-memory/platform/limits/og.png?v=0c2b7a4aef988608
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/agent-memory/llms.txt  
> Use this file to discover all available pages before exploring further.

# Limits

Last updated Jun 3, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/agent-memory/platform/limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following limits apply to Agent Memory operations.

| Feature | Limit |
| --- | --- |
| Messages per `ingest()` call | 500 |
| Message content size | 32 KB (32,768 bytes UTF-8) |
| Recall query size | 1 KB (1,024 bytes UTF-8) |
| Session ID length | 64 characters |
| Profile name length | 100 characters |
| Namespace name length | 32 characters |
| List API page size | 1 to 1,000 (default: 20) |
