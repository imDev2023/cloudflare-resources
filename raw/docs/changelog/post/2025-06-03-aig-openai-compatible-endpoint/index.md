---
description: AI Gateway has added OpenAI compatibility
title: AI Gateway adds OpenAI compatible endpoint
image: https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/og.png?v=6494453c20d9ce2b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 3, 2025

## AI Gateway adds OpenAI compatible endpoint

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Users can now use an [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.

To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the `model` and `apiKey` parameters.

*OpenAI SDK Examplejs*

```js
import OpenAI from "openai";
const client = new OpenAI({
	apiKey: "YOUR_PROVIDER_API_KEY", // Provider API key
	baseURL:
		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat",
});

const response = await client.chat.completions.create({
	model: "google-ai-studio/gemini-2.0-flash",
	messages: [{ role: "user", content: "What is Cloudflare?" }],
});

console.log(response.choices[0].message.content);
```

Additionally, the [OpenAI Compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) can be combined with our [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!

Learn more in the [OpenAI Compatibility](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/#page","headline":"AI Gateway adds OpenAI compatible endpoint","description":"AI Gateway has added OpenAI compatibility","url":"https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-03-aig-openai-compatible-endpoint/og.png?v=6494453c20d9ce2b","dateModified":"2025-06-03","datePublished":"2025-06-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
