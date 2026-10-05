---
description: Locally-managed tunnels resources and guides for Zero Trust networking.
title: Locally-managed tunnels
image: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/og.png?v=a5a793639d0fc215
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Locally-managed tunnels

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare recommends creating a [remotely-managed tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) for most use cases. Remotely-managed tunnels store their configuration on Cloudflare, which allows you to manage the tunnel from any machine using the dashboard, API, or Terraform.

As an alternative workflow, you can create a locally-managed tunnel by running `cloudflared tunnel create <NAME>` on the command line. Tunnel configuration is stored in your local `cloudflared` directory. Locally-managed tunnels are intended for specific scenarios such as local development, testing, or legacy configurations.

- [Create a locally-managed tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/)
- [Configuration file](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/)
- [Run as a service](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/)
- [Useful commands](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/tunnel-useful-commands/)
- [Tunnel permissions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/tunnel-permissions/)
- [Useful terms](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/)
