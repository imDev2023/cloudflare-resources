---
description: Troubleshoot Cloudflare error 10054.
title: Error 10054
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10054/og.png?v=829334f3723af6c8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10054

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10054/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10054: Invalid redirect source URL with fragment

This error indicates that the source URL includes an unsupported fragment component.

### Common causes

This error occurs when the source URL of a URL redirect includes a fragment component (for example, `https://example.com/search/#fragment`). Fragment components are not part of an HTTP request; they are an indication for the browser to scroll to a specific location once the page has loaded. Possible causes of this error include copying a URL with a fragment from a browser or external source, or inadvertently adding a fragment during URL configuration or editing.

### Resolution

Remove the fragment from the redirect source URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
