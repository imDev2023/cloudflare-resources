---
description: AI Gateway has added DeepSeek as a new provider.
title: AI Gateway adds DeepSeek as a Provider
image: https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/og.png?v=6f166910b334b623
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 2, 2025

## AI Gateway adds DeepSeek as a Provider

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**AI Gateway**](https://developers.cloudflare.com/ai-gateway/) now supports [**DeepSeek**](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/), including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or [Workers AI](https://developers.cloudflare.com/workers-ai/), AI Gateway empowers you to:

- **Monitor**: Gain actionable insights with analytics and logs.
- **Control**: Implement caching, rate limiting, and fallbacks.
- **Optimize**: Improve performance with feedback and evaluations.

![AI Gateway adds DeepSeek as a provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=131,format=webp/_astro/deepseek.hirkr3rv.png)

To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:

*Example fetch requestbash*

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
 --data '{
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

For detailed setup instructions, see our [DeepSeek provider documentation](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/#page","headline":"AI Gateway adds DeepSeek as a Provider","description":"AI Gateway has added DeepSeek as a new provider.","url":"https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/og.png?v=6f166910b334b623","dateModified":"2025-01-02","datePublished":"2025-01-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
