---
description: Configure automatic export of MCP server portal logs to third-party storage destinations or SIEM tools.
title: Export MCP server portal logs with Logpush
image: https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/og.png?v=b26052308fa5fc3a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 27, 2026

## Export MCP server portal logs with Logpush

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Only available on Enterprise plans.

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now supports [Logpush](https://developers.cloudflare.com/logs/logpush/) integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.

#### Available log fields

The MCP server portal logs dataset includes fields such as:

- `Datetime` — Timestamp of the request
- `PortalID` / `PortalAUD` — Portal identifiers
- `ServerID` / `ServerURL` — Upstream MCP server details
- `Method` — JSON-RPC method (for example, `tools/call`, `prompts/get`, `resources/read`)
- `ToolCallName` / `PromptGetName` / `ResourceReadURI` — Method-specific identifiers
- `UserID` / `UserEmail` — Authenticated user information
- `Success` / `Error` — Request outcome
- `ServerResponseDurationMs` — Response time from upstream server

For the complete field reference, refer to [MCP portal logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/).

#### Set up Logpush

To configure Logpush for MCP server portal logs, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

Note

MCP server portals is currently in beta.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/#page","headline":"Export MCP server portal logs with Logpush","description":"Configure automatic export of MCP server portal logs to third-party storage destinations or SIEM tools.","url":"https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/og.png?v=b26052308fa5fc3a","dateModified":"2026-02-27","datePublished":"2026-02-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
