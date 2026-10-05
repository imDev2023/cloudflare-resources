---
description: Troubleshoot Cloudflare error 10028.
title: Error 10028
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10028/og.png?v=b016ea497f4e1846
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10028

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10028/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10028: The add list items operation contains duplicate items

This error indicates that the operation to add items to a list contains duplicate entries within the same request.

### Common causes

This error occurs when there are duplicate list items in a single operation to add items to a List (either an IP list or a Bulk Redirect List). This error can happen when you:

- Add a repeated IP address to an IP list
- Add a repeated source URL to a Bulk Redirect List

### Resolution

You need to remove the duplicate item and try again.
