---
description: Troubleshoot Cloudflare error 10050.
title: Error 10050
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10050/og.png?v=87599d4c13429cdb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10050

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10050/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10050: Invalid redirect source URL with user info

This error indicates that the source URL includes unsupported user information.

### Common causes

This error occurs when the source URL of a URL redirect includes a user info component (for example, `https://user:password@example.com`), which is not supported.

### Resolution

You need to remove the user information component from the redirect source URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
