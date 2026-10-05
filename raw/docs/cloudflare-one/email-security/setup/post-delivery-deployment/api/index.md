---
description: How API deployment works in Email Security.
title: API deployment
image: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/og.png?v=a71d1caa0fa20277
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# API deployment

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you choose an API deployment, email messages only reach Email security after they have already reached a user's inbox.

Then, through an integration with your email provider, Email security can [auto-move messages](https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/) based on your organization's policies.

![With API deployment, messages travel through Email security's email filter after reaching your users.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=585,height=492,format=webp/_astro/M365_API_Deployment_Graph.Czbz8tQF.png)

## Benefits

When you choose API deployment, you get the following benefits:

- Easy protection for complex email architectures, without requiring any change to mailflow operations.
- Agentless deployment for Microsoft 365.

## Limitations

However, API deployment also has the following disadvantages:

- Email security is dependent on Microsoft's Graph API, and outages will increase the message dwell time in the inbox.
- Your email provider may throttle API requests from Email security.
- Email security requires read and write access to mailboxes.
- Requires API support from your email provider (does not typically support on-premise providers).
- Detection rates may be lower if multiple solutions exist.
- Messages cannot be modified or quarantined.
