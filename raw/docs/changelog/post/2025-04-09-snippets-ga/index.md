---
description: Snippets let you program HTTP traffic with lightweight JavaScript — now GA and ready for production.
title: Cloudflare Snippets are now Generally Available
image: https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/og.png?v=789769269fdf4eca
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 9, 2025

## Cloudflare Snippets are now Generally Available

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![Cloudflare Snippets are now GA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1126,format=webp/_astro/snippets-ga.BJr3csvv.png)

[Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/) are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.

You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.

What's new:

- **Snippets are now GA** – Available at no extra cost on all Pro, Business, and Enterprise plans.
- **Ready for production** – Snippets deliver a production-grade experience built for scale.
- **Part of the Cloudflare Rules platform** – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.
- **Trace integration** – Use [Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/) to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.![Snippets shown in Cloudflare Trace results](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=334,format=webp/_astro/snippets-ga-trace.WlCshaFo.gif)

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/snippets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/#page","headline":"Cloudflare Snippets are now Generally Available","description":"Snippets let you program HTTP traffic with lightweight JavaScript — now GA and ready for production.","url":"https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-09-snippets-ga/og.png?v=789769269fdf4eca","dateModified":"2025-04-09","datePublished":"2025-04-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
