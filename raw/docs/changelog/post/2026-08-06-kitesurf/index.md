---
description: Kitesurf is a new stateless browser that runs entirely on Workers and is built for AI agents. It is available for free while in beta.
title: Introducing Kitesurf, an agent-first browser on Browser Run
image: https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/og.png?v=3985092c1aff85fa
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 6, 2026

## Introducing Kitesurf, an agent-first browser on Browser Run

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) is Cloudflare's new stateless, highly scalable browser that runs entirely on top of [Workers](https://developers.cloudflare.com/workers/) and is designed for AI agents. It is available for free while in beta.

Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.

Your existing clients already work. To opt in, add the `browser=kitesurf` parameter to any Browser Run [CDP](https://developers.cloudflare.com/browser-run/cdp/) or [Quick Action](https://developers.cloudflare.com/browser-run/quick-actions/) endpoint:

```sh
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/browser-run/screenshot?browser=kitesurf' \
  -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com"
  }' \
  --output "screenshot.png"
```

You can also explore Kitesurf without writing any code in the [public playground ↗︎](https://kitesurf.cloudflare.app/).

For more information, refer to the [Kitesurf documentation](https://developers.cloudflare.com/browser-run/kitesurf/) and the [blog announcement ↗︎](https://blog.cloudflare.com/kitesurf).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/#page","headline":"Introducing Kitesurf, an agent-first browser on Browser Run","description":"Kitesurf is a new stateless browser that runs entirely on Workers and is built for AI agents. It is available for free while in beta.","url":"https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/og.png?v=3985092c1aff85fa","dateModified":"2026-08-06","datePublished":"2026-08-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
