---
description: Navigation redesign, improved onboarding, analytics fixes, and accessibility updates
title: AI dashboard experience improvements
image: https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/og.png?v=e846957c641c3bc8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 19, 2026

## AI dashboard experience improvements

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) [Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers AI](https://developers.cloudflare.com/workers-ai/) and [AI Gateway](https://developers.cloudflare.com/ai-gateway/) have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.

**Navigation and discoverability**

AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.

![AI sidebar navigation in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2328,height=1140,format=webp/_astro/sidebar-navigation.BQNFBmAk.png) *The new top-level AI section in the dashboard sidebar.*

**Onboarding and getting started**

[Getting started](https://developers.cloudflare.com/ai-gateway/get-started/) with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.

![AI Gateway onboarding flow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1232,format=webp/_astro/onboarding-flow.DZ7aMcHa.png) *The first-run setup experience for new gateways.*

We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.

**Dynamic Routing**

- The [route builder](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) is now more performant and responsive.
- You can now copy route names to your clipboard with a single click.
- Code examples use the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) format, making it easier to integrate routes into your application.

**Observability and analytics**

- Small monetary values now display correctly in [cost analytics](https://developers.cloudflare.com/ai-gateway/observability/costs/) charts, so you can accurately track spending at any scale.

**Accessibility**

- Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by [provider](https://developers.cloudflare.com/ai-gateway/usage/providers/).
- Improvements to sorting and filtering components on the [Workers AI](https://developers.cloudflare.com/workers-ai/models/) models page.

For more information, refer to the [AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/#page","headline":"AI dashboard experience improvements","description":"Navigation redesign, improved onboarding, analytics fixes, and accessibility updates","url":"https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/og.png?v=e846957c641c3bc8","dateModified":"2026-02-19","datePublished":"2026-02-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
