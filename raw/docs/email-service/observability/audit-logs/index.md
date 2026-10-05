---
description: Track Email Service configuration changes such as rule edits and address additions in Cloudflare audit logs.
title: Audit logs
image: https://developers.cloudflare.com/email-service/observability/audit-logs/og.png?v=ade317ef1db125b8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/email-service/llms.txt  
> Use this file to discover all available pages before exploring further.

# Audit logs

Last updated Jun 9, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/email-service/observability/audit-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Email Service writes configuration changes to [Cloudflare audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/). Use audit logs to track who changed what and when.

## Email Routing actions

The following Email Routing actions are recorded:

- Add, edit, or delete a routing rule.
- Add or delete a destination address.
- Change the status of a destination address (for example, from pending to verified).
- Update the catch-all rule.
- Enable, disable, or unlock the zone for Email Routing.

## Email Sending actions

The following Email Sending actions are recorded:

- Onboard or remove a sending domain or subdomain.
- Add, edit, or delete entries on the suppression list.
- Enable or disable Email Sending on a domain.

To review audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).
