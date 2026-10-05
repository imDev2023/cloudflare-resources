---
description: After registering an application, use these endpoints to integrate your OAuth client with Cloudflare.
title: Integrate your OAuth client with Cloudflare
image: https://developers.cloudflare.com/fundamentals/oauth/integrate-with-cloudflare/og.png?v=26453964b3ee3799
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/fundamentals/llms.txt  
> Use this file to discover all available pages before exploring further.

# Integrate your OAuth client with Cloudflare

Last updated Jun 3, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/fundamentals/oauth/integrate-with-cloudflare/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

After [registering an application](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/), use these endpoints to integrate your OAuth client with Cloudflare.

- Jwks: `https://dash.cloudflare.com/.well-known/jwks.json`
- Open ID config: `https://dash.cloudflare.com/.well-known/openid-configuration`
- Authorization: `https://dash.cloudflare.com/oauth2/auth`
- Token: `https://dash.cloudflare.com/oauth2/token`
- Revoke: `https://dash.cloudflare.com/oauth2/revoke`
- Session logout: `https://dash.cloudflare.com/oauth2/logout`
- User info: `https://dash.cloudflare.com/oauth2/userinfo`
