---
description: Troubleshoot Cloudflare error 10056.
title: Error 10056
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10056/og.png?v=9507c97b1766f7b4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10056

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10056/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10056: The add list items operation contains different types of list items

This error indicates that different types of list items were combined in a single add operation.

### Common causes

This error occurs when different types of list items (such as IP addresses, hostnames, and URL redirects) are included in a single operation to add items to a list. It can occur with an IP list, a hostname list, or a Bulk Redirect List.

### Resolution

Remove the list items that do not apply to the list type. This means:

- Removing IP addresses from a request to add items to a Bulk Redirect List.
- Removing URL redirects from a request to add items to an IP list.
