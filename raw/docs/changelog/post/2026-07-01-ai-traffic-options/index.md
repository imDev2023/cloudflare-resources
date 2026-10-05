---
description: All customers can now manage AI crawlers by behavior — Search, Agent, and Training — instead of a single Block AI bots toggle.
title: New options to manage AI traffic
image: https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/og.png?v=1fd27c1419d07cc8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## New options to manage AI traffic

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Not all AI traffic is the same. Now, all customers — including those on the Free plan — can manage AI crawlers based on what they actually do on your site. Cloudflare groups AI traffic into three behaviors you can control independently: [Search, Agent, and Training](https://developers.cloudflare.com/bots/concepts/bot/#ai-bots). This lets you keep the automated traffic that sends readers and revenue back to you, while blocking the traffic that only takes from your content.

Each behavior maps to a real use case. **Search** covers crawlers that index your content so they can answer questions about it later, where you should expect referral traffic or other equitable compensation in return. **Agent** covers automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents. **Training** covers crawlers that take your content to train or fine-tune a model. For each preset you can choose to block on all pages, block only on pages that display ads, or choose not to block.

![The Configure AI bot traffic policies screen, where Search, Agent, and Training can each be set to allow, block, or block only on pages with ads](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4720,height=2966,format=webp/_astro/ai-bot-traffic-policies.BqXU7Gmv.png)

Starting **September 15, 2026**, new domains onboarding to Cloudflare receive updated defaults: Bots classified as Training or as Agent are blocked on pages that display ads, while **Search** remains allowed. On that date, multi-purpose crawlers that combine Search and Training will be affected by the new defaults to block Training. All customers can [opt out of the new defaults ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/settings) at any time before September 15.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/#page","headline":"New options to manage AI traffic","description":"All customers can now manage AI crawlers by behavior — Search, Agent, and Training — instead of a single Block AI bots toggle.","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/og.png?v=1fd27c1419d07cc8","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
