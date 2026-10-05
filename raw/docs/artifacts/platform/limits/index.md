---
description: Review Artifacts platform limits.
title: Limits
image: https://developers.cloudflare.com/artifacts/platform/limits/og.png?v=83d5d7f227f0b27c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/artifacts/llms.txt  
> Use this file to discover all available pages before exploring further.

# Limits

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/artifacts/platform/limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Limits that apply to creating, importing, cloning, and pushing Artifacts are detailed below.

These limits cover naming rules, storage, and request rates for control-plane and Git operations.

| Feature | Limit |
| --- | --- |
| Control-plane request rate | 2,000 requests per 10 seconds per Artifacts namespace |
| Git request rate, per artifact | 2,000 requests per 10 seconds per artifact |
| Maximum storage per repository | 1 GB |
| Maximum individual file or blob size | 32 MB |
| Maximum storage per account | 1 TB (can be raised on request) |
| Maximum number of repositories | Unlimited |
| Maximum number of namespaces | Unlimited |
| Namespace name length | 2-63 characters |
| Namespace and repo names | Start with a letter or digit. Remaining characters may include letters, digits, `.`, `_`, and `-`. |
