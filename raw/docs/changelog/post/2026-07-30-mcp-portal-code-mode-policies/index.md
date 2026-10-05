---
description: New MCP portal policies let admins turn on Code Mode by default, drastically reducing token usage from large tool catalogs.
title: Admins can turn on Code Mode by default for MCP portal users
image: https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/og.png?v=0def9c1251912ecc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 30, 2026

## Admins can turn on Code Mode by default for MCP portal users

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now support four Code Mode policies: *Off*, *Opt-in*, *On by default*, and *Enforced*. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.

Existing portals retain their current behavior. Portals that previously allowed Code Mode use *Opt-in*, while portals that did not allow Code Mode use *Off*. New portals also use *Opt-in* by default.

Clients turn on Code Mode for an *Opt-in* portal with `?codemode=search_and_execute`. The *On by default* policy lets clients opt out with `?codemode=off`, which avoids nested code execution when a client runs its own Code Mode implementation. The *Off* and *Enforced* policies ignore client overrides.

The Cloudflare API exposes these policies through the `code_mode` field:

```json
{
	"code_mode": "default_on"
}
```

The supported values are `off`, `opt_in`, `default_on`, and `enforced`. The previous `allow_code_mode` boolean is deprecated.

For configuration details and client behavior, refer to [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/#page","headline":"Admins can turn on Code Mode by default for MCP portal users","description":"New MCP portal policies let admins turn on Code Mode by default, drastically reducing token usage from large tool catalogs.","url":"https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/og.png?v=0def9c1251912ecc","dateModified":"2026-07-30","datePublished":"2026-07-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
