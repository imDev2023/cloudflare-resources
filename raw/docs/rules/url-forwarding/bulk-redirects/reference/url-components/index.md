---
description: URL components used in Bulk Redirect source and target URLs.
title: Supported URL components in Bulk Redirects
image: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/og.png?v=6904aa204ac210a7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Supported URL components in Bulk Redirects

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The source and target URLs of a URL redirect support different URL components.

The provided URL component examples in the reference table are based on the following URL:

```txt
https://user:password@www.example.com:443/search?q=term#results
```

| URL component | Supported in source URL <sup>[1](#user-content-fn-1)</sup> | Supported in target URL |
| --- | --- | --- |
| **Scheme**<br>For example:<br>`https` | Yes, `http` or `https` only<br>(optional) | Yes |
| **User information**<br>For example:<br>`user:password` | No | Yes (optional) |
| **Host**<br>For example:<br>`www.example.com` | Yes | Yes (optional) |
| **Port**<br>For example:<br>`443` | No | Yes (optional) |
| **Path**<br>For example:<br>`/search` | Yes | Yes |
| **Query string**<br>For example:<br>`q=term` | No | Yes, if [**Preserve query string**](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/#preserve-query-string) is `false` (optional)<br><br>You can only add a query string to the target URL if you do not keep the original query string (that is, if **Preserve query string** is `false`). If you set **Preserve query string** to `true`, the query string of the request will be passed along [when there is a match for the source URL](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/#matching-the-source-url-of-redirects). |
| **Fragment**<br>For example:<br>`results` | No | Yes (optional) |

Bulk Redirects also support target URLs without an authority component <sup>[2](#user-content-fn-2)</sup>, like the following URL:

```txt
magnet:?xt=urn:btih:2bd9d334e8d1e5bd7768755173222db5c6dea13b&dn=archlinux-2021.07.01-x86_64.iso
```

## Footnotes

1. **Supported in source URL** = **No** means that you cannot include the component in the source URL to match against the URL of incoming requests. [↩](#user-content-fnref-1)
2. The URL authority is the combination of user information, host, and port components. [↩](#user-content-fnref-2)
