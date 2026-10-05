---
description: Information about Cloudflare One Appliance's default password.
title: Default password
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/default-password/og.png?v=8f8bf3fd9f93595b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# Default password

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/default-password/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One Appliance (formerly Magic WAN Connector) ships to you with a default password that enables you to access the hardware box or the virtual machine. Cloudflare recommends that you change this password after the first boot.

## Default password to access hardware Cloudflare One Appliance

The default password for Cloudflare One Appliance is the serial number (also known as a Service Tag for Dell devices), all uppercase followed by an `!` (exclamation mark). For example, `A1B2C3D!`

## Default password to access Virtual Appliance

The default password for Virtual Appliance is the last seven characters of your license key, all uppercase, plus an `!` (exclamation mark).

For example, if your license key is `mconn-abcdefghijklmnopqrstuvwxyz`, your default password will be `TUVWXYZ!`.
