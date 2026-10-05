---
description: Moondream 3.1, a fast and efficient vision language model with frontier-level visual reasoning, is now available on Workers AI.
title: Moondream 3.1 now available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/og.png?v=afde045e595e01a3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2026

## Moondream 3.1 now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Partnering with [Moondream ↗︎](https://moondream.ai/) to bring their latest model [`@cf/moondream/moondream3.1-9B-A2B`](https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/) to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.

Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.

#### Key capabilities

- **Query** — ask open-ended questions about an image, with an optional reasoning parameter
- **Caption** — generate short, normal, or long descriptions of an image
- **Point** — return coordinates for objects matching a target phrase
- **Detect** — return bounding boxes for objects matching a target phrase

#### Real-time vision at the edge

Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.

In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.

| Task | End-to-end (p50) |
| --- | --- |
| `query` | \~770 ms |
| `caption` | \~480 ms |
| `point` | \~145 ms |
| `detect` | \~160 ms |

At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.

#### Get started

Use Moondream 3.1 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Moondream 3.1 model page](https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/#page","headline":"Moondream 3.1 now available on Workers AI","description":"Moondream 3.1, a fast and efficient vision language model with frontier-level visual reasoning, is now available on Workers AI.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/og.png?v=afde045e595e01a3","dateModified":"2026-07-08","datePublished":"2026-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
