---
description: Fix the 403 authentication error caused by incorrect zone data source indexing in Terraform.
title: 403 Authentication error when creating DNS records
image: https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/og.png?v=a5efb385efc627d6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/terraform/llms.txt  
> Use this file to discover all available pages before exploring further.

# 403 Authentication error when creating DNS records

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When creating DNS records using Terraform, the API returns the following error:

`Error: failed to create DNS record: HTTP status 403: Authentication error (10000)`

This is caused by an error in your code syntax, when you are not using index `[0]` for the zones. Find an example below and a more detailed thread on [GitHub ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/913).

Instead of this:

```txt
zone_id = data.cloudflare_zones.example_com.id
```

Use this:

```txt
zone_id = data.cloudflare_zones.example_com.zones[0].id`
```
