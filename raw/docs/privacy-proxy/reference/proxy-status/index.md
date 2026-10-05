---
description: All possible proxyStatus values for Privacy Proxy error classification in GraphQL Analytics and OpenTelemetry metrics.
title: Proxy status reference
image: https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/og.png?v=3275dc1ee16f27df
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/privacy-proxy/llms.txt  
> Use this file to discover all available pages before exploring further.

# Proxy status reference

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `proxyStatus` dimension provides proxy-level error classification. This field is available in both [GraphQL Analytics API](https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/) and [OpenTelemetry](https://developers.cloudflare.com/privacy-proxy/reference/metrics/opentelemetry/) metrics. The value is an empty string when no proxy-level error occurred.

---

## `proxyStatus` values

| Value | Description |
| --- | --- |
| `dns_error` | The proxy encountered a DNS error when resolving the next hop hostname. |
| `dns_timeout` | The proxy timed out while resolving the next hop hostname. |
| `destination_not_found` | The proxy cannot determine the appropriate next hop for this request. |
| `destination_unavailable` | The proxy considers the next hop unavailable (for example, recent failures or health check is down). |
| `destination_ip_prohibited` | The proxy is configured to prohibit connections to the next hop IP address. |
| `destination_ip_unroutable` | The proxy cannot find a route to the next hop IP address. |
| `connection_refused` | The proxy's connection to the next hop was refused. |
| `connection_terminated` | The proxy's connection to the next hop was closed before any response was received. |
| `connection_timeout` | The proxy's attempt to open a connection to the next hop timed out. |
| `connection_read_timeout` | The proxy was expecting data on a connection but received none within the configured time limit. |
| `connection_write_timeout` | The proxy was attempting to write data to a connection but was unable to. |
| `connection_limit_reached` | The proxy's configured connection limit to the next hop has been exceeded. |
| `source_addr_in_use` | The proxy cannot assign a source address when connecting to the next hop. |
| `source_addr_not_available` | The proxy cannot assign a source address (bind failure or source host resolution failure). |
| `tls_protocol_error` | The proxy encountered a TLS error when communicating with the next hop. |
| `tls_certificate_error` | The proxy encountered an error verifying the certificate presented by the next hop. |
| `http_request_error` | The proxy is generating a client (4xx) response on the origin's behalf. |
| `http_upgrade_failed` | The HTTP Upgrade between the proxy and the next hop failed. |
| `http_request_denied` | The proxy rejected the HTTP request based on its configuration or policy. |
| `proxy_internal_error` | The proxy encountered an internal error unrelated to the origin. |
| `proxy_loop_detected` | The proxy tried to forward the request to itself. |
| `http_protocol_error` | The proxy encountered an HTTP protocol error when communicating with the next hop. |
| `http_response_incomplete` | The proxy received an incomplete response from the next hop. |
| `rate_limited` | The client has reached the maximum number of connections per second to a single origin. |
