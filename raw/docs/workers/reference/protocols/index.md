---
description: Supported protocols on the Workers platform.
title: Protocols
image: https://developers.cloudflare.com/workers/reference/protocols/og.png?v=198e55cc958fd875
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Protocols

Last updated Jun 9, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/reference/protocols/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workers support the following protocols and interfaces:

| Protocol | Inbound | Outbound |
| --- | --- | --- |
| **HTTP / HTTPS** | Handle incoming HTTP requests using the [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) | Make HTTP subrequests using the [`fetch()` API](https://developers.cloudflare.com/workers/runtime-apis/fetch/) |
| **Direct TCP sockets** | Support for handling inbound TCP connections is [coming soon ↗︎](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) | Create outbound TCP connections using the [`connect()` API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) |
| **WebSockets** | Accept incoming WebSocket connections using the [`WebSocket` API](https://developers.cloudflare.com/workers/runtime-apis/websockets/) | |
| **HTTP/3 (QUIC)** | Accept inbound requests over [HTTP/3 ↗︎](https://www.cloudflare.com/learning/performance/what-is-http3/) by enabling it on your [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in **Speed** > **Settings** > **Protocol Optimization** area of the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). | |
| **SMTP** | Use [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) to process and forward email, without having to manage TCP connections to SMTP email servers | [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) |
