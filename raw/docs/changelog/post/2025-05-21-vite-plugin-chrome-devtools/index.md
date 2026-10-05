---
description: The Cloudflare Vite plugin now supports debugging Cloudflare Workers using Chrome Devtools
title: Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/og.png?v=42f744c6289d9d55
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 30, 2025

## Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now [debug, profile, view logs, and analyze memory usage for your Worker ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/) using [Chrome Devtools ↗︎](https://developer.chrome.com/docs/devtools) when your Worker runs locally using the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/).

Previously, this was only possible if your Worker ran locally using the [Wrangler CLI ↗︎](https://developers.cloudflare.com/workers/wrangler/), and now you can do all the same things if your Worker uses [Vite ↗︎](https://vite.dev/).

When you run `vite`, you'll now see a debug URL in your console:

```plaintext
  VITE v6.3.5  ready in 461 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  Debug:   http://localhost:5173/__debug
  ➜  press h + enter to show help
```

Open the URL in Chrome, and an instance of Chrome Devtools will open and connect to your Worker running locally. You can then use Chrome Devtools to debug and introspect performance issues. For example, you can navigate to the Performance tab to understand where CPU time is spent in your Worker:

![CPU Profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2144,height=1134,format=webp/_astro/profile.Dz8PUp_K.png)

For more information on how to get the most out of Chrome Devtools, refer to the following docs:

- [Debug code by setting breakpoints](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/)
- [Profile CPU usage](https://developers.cloudflare.com/workers/observability/dev-tools/cpu-usage/)
- [Observe memory usage and debug memory leaks](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/#page","headline":"Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin","description":"The Cloudflare Vite plugin now supports debugging Cloudflare Workers using Chrome Devtools","url":"https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-21-vite-plugin-chrome-devtools/og.png?v=42f744c6289d9d55","dateModified":"2025-05-30","datePublished":"2025-05-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
