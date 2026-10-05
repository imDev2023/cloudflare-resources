---
description: Review Cloudflare Tunnel connection events.
title: Tunnel audit logs
image: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs/og.png?v=f24175cb83c2ccff
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Tunnel audit logs

Last updated May 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) creates outbound-only connections between your infrastructure and Cloudflare. Tunnel audit logs record when these connections start, stop, or register new DNS records.

Audit logs for Tunnel are available in the [account section of the Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?account=audit-log), which you can find by selecting your name or email in the upper right-hand corner of the dashboard. For general audit log features such as filtering and retention, refer to [Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/). The following actions are logged:

| Action | Description |
| --- | --- |
| Registered | A tunnel connector (`cloudflared`) started and connected to Cloudflare's global network. |
| Unregistered | A tunnel connector disconnected from Cloudflare's global network. |
| CNAME add | A tunnel registered a new DNS record (CNAME or AAAA) to route traffic to an application behind the tunnel. |
