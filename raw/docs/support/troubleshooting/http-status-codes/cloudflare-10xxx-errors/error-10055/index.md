---
description: Troubleshoot Cloudflare error 10055.
title: Error 10055
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10055/og.png?v=a3231ee04445ef36
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10055

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10055/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10055: Query string settings incompatible with redirect target URL

This error indicates a conflict between the **Preserve query string** option and the query string in the redirect target URL.

### Common causes

This error occurs when you enable the **Preserve query string** option of a URL redirect, but also provide a query string in the redirect target URL. In this case, the URL redirect would have conflicting configuration on how to handle the query string of incoming requests.

### Resolution

To resolve this issue, either disable the **Preserve query string** option in the URL redirect or remove the query string component from the redirect target URL to eliminate the conflict.
