---
description: Manage sessions for MCP servers protected by portals, including reauthentication, server toggling, and automatic authorization prompts.
title: Session management for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/og.png?v=54bc2b649db42d25
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 2, 2026

## Session management for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.

To return to the server selection page, ask your AI agent with a prompt like "take me back to the server selection page." The portal responds with an authorization URL via [MCP elicitation ↗︎](https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation) that you open in your browser:

```txt
https://<subdomain>.<domain>/authorize?elicitationId=<ELICITATION_ID>
```

From the server selection page you can:

- **Enable or disable servers** — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.
- **Log out and reauthenticate** — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.

Users can also enable or disable a server inline by asking their AI agent directly, for example "enable the wiki server" or "disable my Jira server."

The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of [managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal).

For more information, refer to [Manage portal sessions](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/#page","headline":"Session management for MCP server portals","description":"Manage sessions for MCP servers protected by portals, including reauthentication, server toggling, and automatic authorization prompts.","url":"https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/og.png?v=54bc2b649db42d25","dateModified":"2026-04-02","datePublished":"2026-04-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
