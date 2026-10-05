---
description: Create a temporary URL for a local service without a Cloudflare account. Restrict access with email one-time PINs.
title: Quick Tunnels
image: https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/og.png?v=7213d8a3f76b97aa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/tunnel/llms.txt  
> Use this file to discover all available pages before exploring further.

# Quick Tunnels

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Quick Tunnels create a temporary `trycloudflare.com` URL for a local service. You do not need a Cloudflare account or domain.

Note

Quick Tunnels are for testing and development. For production, [create a Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/get-started/).

## Prerequisites

- [Install `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/).
- Start a local HTTP server. This example uses `http://localhost:8080`.

## Create a Quick Tunnel

1. In a terminal, start a Quick Tunnel:

   ```sh
   cloudflared tunnel --url http://localhost:8080
   ```


2. Open the `trycloudflare.com` URL printed by `cloudflared`.

Anyone with the URL can access your local service. The URL stops working when you stop the `cloudflared` process.

## Restrict access by email

Use `--allowed-mail` to require email authentication. Visitors receive a one-time PIN before they can access your service.

1. Start a Quick Tunnel with an allowed email address:

   ```sh
   cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com
   ```


2. Share the generated URL with the allowed visitor.
3. The visitor opens the URL and enters their email address.
4. The visitor enters the one-time PIN sent to their email.

The visitor does not need a Cloudflare account.

### Repeat the flag

Repeat `--allowed-mail` to allow multiple email addresses:

```sh
cloudflared tunnel --url http://localhost:8080 \
  --allowed-mail alice@example.com \
  --allowed-mail bob@example.com
```

### Use a comma-separated list

Separate multiple email addresses with commas:

```sh
cloudflared tunnel --url http://localhost:8080 \
  --allowed-mail 'alice@example.com,bob@example.com'
```

### Allow an email domain

Use `*@example.com` to allow every address from a domain. Enclose wildcard values in quotes to prevent shell expansion:

```sh
cloudflared tunnel --url http://localhost:8080 --allowed-mail '*@example.com'
```

To change who can access the service, stop `cloudflared` and start a new Quick Tunnel. Access ends for everyone when the process stops.

## Limitations

- Quick Tunnels have no uptime guarantee.
- Each Quick Tunnel supports up to 200 in-flight requests. Additional requests return a `429` response.
- Quick Tunnels do not support Server-Sent Events (SSE).
- Email authentication requires an interactive browser session. It does not support non-interactive clients.
- The hostname changes each time you create a Quick Tunnel.

For stable hostnames and production traffic, [create a Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/get-started/).
