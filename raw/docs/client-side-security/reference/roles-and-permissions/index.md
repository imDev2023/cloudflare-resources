---
description: User roles and API token permissions required to access and configure client-side security.
title: Roles and permissions
image: https://developers.cloudflare.com/client-side-security/reference/roles-and-permissions/og.png?v=59a610dca693d753
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/client-side-security/llms.txt  
> Use this file to discover all available pages before exploring further.

# Roles and permissions

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/client-side-security/reference/roles-and-permissions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare users with the following [roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/) have access to client-side security in the Cloudflare dashboard:

- Administrator
- Super Administrator - All Privileges
- Page Shield
- Page Shield Read *(read-only access)*
- Domain Page Shield
- Domain Page Shield Read *(read-only access)*

The availability of specific features depends on your client-side security bundle. Refer to [Availability](https://developers.cloudflare.com/client-side-security/#availability) for more information.

## API token permissions

To interact with the [client-side security API](https://developers.cloudflare.com/client-side-security/reference/api/) you need an API token with one of the following [permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/):

- Client-side security > Edit
- Client-side security > Read *(read-only access)*

- Page Shield Write
- Page Shield Read *(read-only access)*
