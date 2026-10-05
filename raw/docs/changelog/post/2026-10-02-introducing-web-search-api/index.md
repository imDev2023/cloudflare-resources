---
description: Search the web from your AI agents and applications through AI Gateway with Ceramic.ai, Exa, and Linkup.
title: Introducing Web Search API
image: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/og.png?v=1deaa8fb09156b56
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## Introducing Web Search API

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) [Web Search API](https://developers.cloudflare.com/web-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "query": "What are some fun things to do in Salt Lake City as fall approaches?",
    "provider": "ceramic",
    "limit": 5,
    "options": { "gateway": { "id": "default" } }
  }'
```

Or from a Worker with the AI binding:

```ts
const response = await env.AI.websearch({
	gatewayId: "default",
	query: "What are some fun things to do in Salt Lake City as fall approaches?",
	provider: "exa",
	limit: 5,
});

const results = await response.json();
```

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/#page","headline":"Introducing Web Search API","description":"Search the web from your AI agents and applications through AI Gateway with Ceramic.ai, Exa, and Linkup.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/og.png?v=1deaa8fb09156b56","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
