---
description: Embed AI Search components in your website and connect AI agents via MCP.
title: AI Search UI snippets and MCP support
image: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/og.png?v=5f62259a5ffca5b5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 23, 2026

## AI Search UI snippets and MCP support

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.

Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:

1. Go to **AI Search** in the Cloudflare dashboard. [Go to **AI Search** ↗](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
2. Select your instance, and turn on **Public Endpoint** in **Settings**. For more details, refer to [Public endpoint configuration](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/).

#### UI snippets

UI snippets are pre-built search and chat components you can embed in your website. Visit [search.ai.cloudflare.com ↗︎](https://search.ai.cloudflare.com/) to configure and preview components for your AI Search instance.

![Example of the search-modal-snippet component](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1842,height=806,format=webp/_astro/ui-snippet-search-modal.nSXbvcsi.png)

To add a search modal to your page:

```html
<script
	type="module"
	src="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js"
></script>

<search-modal-snippet
	api-url="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/"
	placeholder="Search..."
>
</search-modal-snippet>
```

For more details, refer to the [UI snippets documentation](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/).

#### MCP

The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:

```txt
https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/mcp
```

For more details, refer to the [MCP documentation](https://developers.cloudflare.com/ai-search/api/search/mcp/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/#page","headline":"AI Search UI snippets and MCP support","description":"Embed AI Search components in your website and connect AI agents via MCP.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/og.png?v=5f62259a5ffca5b5","dateModified":"2026-03-23","datePublished":"2026-03-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
