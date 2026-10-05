---
description: A streamlined Support Portal featuring AI-driven ticket routing and a simplified interface for all Cloudflare customers.
title: Redesigned Support Portal for faster, personalized help
image: https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/og.png?v=270d848db6a3309a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2026

## Redesigned Support Portal for faster, personalized help

[Support](https://developers.cloudflare.com/support/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Redesigned "Get Help" Portal for faster, personalized help

Cloudflare has officially launched a redesigned "Get Help" Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.

The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as "Ask AI", "Chat with a human", or "Community" — without the manual triage.

#### What's New

- **One Page, Clear Choices**: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.
- **A Radically Simpler Support Form**: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.
- **AI-Driven Triage**: Using [Cloudflare Workers AI ↗︎](https://developers.cloudflare.com/workers-ai/) and [Vectorize ↗︎](https://developers.cloudflare.com/vectorize/), the portal now automatically generates case subjects and predicts product categories.

#### Moving complexity to the backend

Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.

By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.

To learn more, refer to the [Support documentation](https://developers.cloudflare.com/support/contacting-cloudflare-support/) or select **Get Help** directly in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/#page","headline":"Redesigned Support Portal for faster, personalized help","description":"A streamlined Support Portal featuring AI-driven ticket routing and a simplified interface for all Cloudflare customers.","url":"https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/og.png?v=270d848db6a3309a","dateModified":"2026-04-07","datePublished":"2026-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
