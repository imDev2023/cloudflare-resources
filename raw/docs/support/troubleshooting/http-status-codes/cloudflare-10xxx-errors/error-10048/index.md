---
description: Troubleshoot Cloudflare error 10048.
title: Error 10048
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10048/og.png?v=2701f2aae1a095e5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10048

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10048/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10048: Preserve path suffix requires subpath matching enabled

This error indicates a configuration mismatch where the **Preserve path suffix** option is used without enabling **Subpath matching** in a URL redirect.

### Common causes

This error occurs when you enable the **Preserve path suffix** option in a redirect without enabling the **Subpath matching** option. The **Preserve path suffix** option of a URL redirect is only applicable when the **Subpath matching** option is also enabled.

### Resolution

Enable **Subpath matching** for the URL redirect with **Preserve path suffix** enabled.
