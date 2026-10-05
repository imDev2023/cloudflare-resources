---
description: Troubleshoot Cloudflare 1014 error code.
title: Error 1014
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/og.png?v=de539b7f8a32a68d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1014

Last updated Sep 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1014: CNAME Cross-User Banned

This error indicates that a CNAME record between domains in different Cloudflare accounts is prohibited.

### Common cause

Common causes include:

- A DNS CNAME record points between domains in different Cloudflare accounts. Cloudflare permits CNAME records within a domain ( `www.example.com` CNAME to `api.example.com`), across zones within the same user account ( `www.example.com` CNAME to `www.example.net`), or when using [Cloudflare for SaaS ↗︎](https://www.cloudflare.com/saas/).
- A custom domain is connected to an R2 bucket, and its active zone has a [zone hold](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) or is banned.
- A custom domain is used to [create an MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#create-a-portal), and its active zone has a zone hold or is banned.

### Resolution

- To allow CNAME record resolution to a domain in a different Cloudflare account, the domain owner of the CNAME target must use [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/).
- To connect a custom domain to an R2 bucket, release the [zone hold](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) on the custom domain target zone.
- To create an MCP portal with a custom domain, release the [zone hold](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) on the selected zone and each parent zone. Then create the portal again.
- If the zone for the custom domain is banned:
  - First, check whether there is any [phishing report](https://developers.cloudflare.com/fundamentals/reference/report-abuse/complaint-types/) for the hostname (and request a review if there is one).
  - Second, make sure that you have no unpaid invoice(s), as you will not be able to enable any new services until [any outstanding balance](https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/) is addressed. If this does not resolve the issue, contact your account team.
