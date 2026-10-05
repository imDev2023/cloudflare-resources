---
description: RealtimeKit transcription supports 10 languages with regional variants powered by Deepgram Nova-3 running on Workers AI.
title: Real-time transcription in RealtimeKit now supports 10 languages with regional variants
image: https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/og.png?v=706d3de5ad41dcfa
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 6, 2026

## Real-time transcription in RealtimeKit now supports 10 languages with regional variants

[Workers AI](https://developers.cloudflare.com/workers-ai/) [Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) in RealtimeKit now supports 10 languages with regional variants, powered by [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) running on [Workers AI](https://developers.cloudflare.com/workers-ai/).

During a meeting, participant audio is routed through [AI Gateway](https://developers.cloudflare.com/ai-gateway/) to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.

Set the language when [creating a meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/) via `ai_config.transcription.language`:

```json
{
	"ai_config": {
		"transcription": {
			"language": "fr"
		}
	}
}
```

Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like `en-AU`, `en-GB`, `en-IN`, `en-NZ`, `es-419`, `fr-CA`, `de-CH`, `pt-BR`, and `pt-PT`. Use `multi` for automatic multilingual detection.

If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.

- [Transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
- [Nova-3 model page](https://developers.cloudflare.com/workers-ai/models/nova-3/)
- [Workers AI](https://developers.cloudflare.com/workers-ai/)
- [AI Gateway](https://developers.cloudflare.com/ai-gateway/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/#page","headline":"Real-time transcription in RealtimeKit now supports 10 languages with regional variants","description":"RealtimeKit transcription supports 10 languages with regional variants powered by Deepgram Nova-3 running on Workers AI.","url":"https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/og.png?v=706d3de5ad41dcfa","dateModified":"2026-03-06","datePublished":"2026-03-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
