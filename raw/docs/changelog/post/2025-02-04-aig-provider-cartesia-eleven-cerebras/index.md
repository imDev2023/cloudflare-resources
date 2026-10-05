---
description: AI Gateway has added Cerebras, ElevenLabs, and Cartesia as new providers.
title: AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers
image: https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/og.png?v=0a6dd9646cfc786f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 5, 2025

## AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) has added three new providers: [Cartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/), [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/), and [ElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/), giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:

- [Cartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/) provides text-to-speech models that produce natural-sounding speech with low latency.
- [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/) delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.
- [ElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/) offers text-to-speech models with human-like voices in 32 languages.

![Example of Cerebras log in AI Gateway](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2278,height=1020,format=webp/_astro/cerebras2.qHYP0ZnF.png)

To get started with AI Gateway, just update the base URL. Here's how you can send a request to [Cerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/) using cURL:

*Example fetch requestbash*

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer CEREBRAS_TOKEN' \
 --data '{
    "model": "llama-3.3-70b",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/#page","headline":"AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers","description":"AI Gateway has added Cerebras, ElevenLabs, and Cartesia as new providers.","url":"https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/og.png?v=0a6dd9646cfc786f","dateModified":"2025-02-05","datePublished":"2025-02-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
