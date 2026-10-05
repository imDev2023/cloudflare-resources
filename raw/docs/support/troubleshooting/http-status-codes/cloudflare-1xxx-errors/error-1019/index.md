---
description: Troubleshoot Cloudflare 1019 error code.
title: Error 1019
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/og.png?v=236da4e1713b1dec
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1019

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1019: Compute server error

This error indicates a compute server error related to a Cloudflare Worker.

### Common cause

A Cloudflare Worker script recursively references itself.

### Resolution

Ensure your Cloudflare Worker does not access a URL that calls the same Workers script.
