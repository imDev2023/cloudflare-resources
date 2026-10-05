---
description: Index a site without a complete sitemap, serve search from a hostname you own, restrict who can query it, and search several instances from one URL.
title: AI Search makes it easier to build a search engine for your data
image: https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/og.png?v=c98d735a10195bc9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 6, 2026

## AI Search makes it easier to build a search engine for your data

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.

Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.

#### Serve search from your own domain

A [public endpoint](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/) is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on `search.ai.cloudflare.com`. You can now serve the same endpoint from a [custom domain](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/), a hostname in a zone that you own:

```txt
https://search.example.com/search
```

#### Restrict who can query your content

Once your endpoint is on your own domain, you can put [Cloudflare Access](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/) in front of it. For example, you usually want to give `/mcp` to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.

#### Search several instances from one URL

A namespace can expose its own [public endpoint](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/) with `/search`, `/chat/completions`, and `/mcp` paths that fan out across the instances you choose:

```bash
curl https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search \
  --header "Content-Type: application/json" \
  --data '{
    "messages": [{ "content": "How do I configure AI Search?", "role": "user" }],
    "ai_search_options": { "instance_ids": ["docs", "support"] }
  }'
```

#### Index your sites without a sitemap

Website data sources support a new `discover` [parse type](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/). It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/instances" \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "my-ai-search",
    "type": "web-crawler",
    "source": "example.com",
    "source_params": {
      "web_crawler": {
        "parse_type": "discover",
        "discover_options": { "source": "links", "limit": 5000, "depth": 3 }
      }
    }
  }'
```

To learn more, refer to the [AI Search documentation](https://developers.cloudflare.com/ai-search/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/#page","headline":"AI Search makes it easier to build a search engine for your data","description":"Index a site without a complete sitemap, serve search from a hostname you own, restrict who can query it, and search several instances from one URL.","url":"https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/og.png?v=c98d735a10195bc9","dateModified":"2026-08-06","datePublished":"2026-08-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
