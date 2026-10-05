---
description: RDP resources and guides for Zero Trust networking.
title: RDP
image: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/og.png?v=ec0d492f31136b7c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# RDP

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Remote Desktop Protocol (RDP) provides a graphical interface for users to connect to a computer remotely. RDP is most commonly used to facilitate simple remote access to machines or workstations which users cannot physically access. However, this also makes RDP connections the frequent subject of attacks, since a misconfiguration can inadvertently allow unauthorized access to the machine.

With Cloudflare Zero Trust, you can make your RDP server available over the Internet without the risk of opening any inbound ports on your local server.

Cloudflare offers three ways to secure RDP:

- [Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/)
- [RDP with Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/)
- [RDP with client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/)
