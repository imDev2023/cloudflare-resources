---
description: Use models from different providers in AI Search (formerly AutoRAG)
title: AI Search (formerly AutoRAG) now with More Models To Choose From
image: https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/og.png?v=1772f83d3e5013e8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## AI Search (formerly AutoRAG) now with More Models To Choose From

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.

With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.

To use AI Search with other [model providers](https://developers.cloudflare.com/ai-search/configuration/models/):

1. **Add provider keys to AI Gateway**
   1. Go to AI > AI Gateway in the dashboard.
   2. Select or create an AI gateway.
   3. In Provider Keys, choose your provider, click Add, and enter the key.
2. **Connect a gateway to AI Search**: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.
3. **Select models**: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.

Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a `/ai-search` request:

```javascript
export default {
  async fetch(request, env) {
    
    // Query your AI Search instance with a natural language question to an OpenAI model
    const result = await env.AI.autorag("my-ai-search").aiSearch({
      query: "What's new for Cloudflare Birthday Week?",
      model: "openai/gpt-5"
    });

    // Return only the generated answer as plain text
    return new Response(result.response, {
      headers: { "Content-Type": "text/plain" },
    });
  },
};
```

In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the [AI Search Changelog](https://developers.cloudflare.com/changelog/product/ai-search/) and [Discord ↗︎](https://discord.cloudflare.com/) for more updates!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/#page","headline":"AI Search (formerly AutoRAG) now with More Models To Choose From","description":"Use models from different providers in AI Search (formerly AutoRAG)","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/og.png?v=1772f83d3e5013e8","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
