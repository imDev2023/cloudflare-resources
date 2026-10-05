---
description: Create custom trace spans in your Workers code to instrument application-specific logic alongside automatic platform instrumentation.
title: Workers tracing now supports custom spans
image: https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/og.png?v=3201f0b53bc69c59
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2026

## Workers tracing now supports custom spans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create custom trace spans in your Workers code using `tracing.enterSpan()`. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.

The API is available via `import { tracing } from "cloudflare:workers"` or through the handler context as `ctx.tracing`:

```ts
import { tracing } from "cloudflare:workers";

export default {
  async fetch(request, env, ctx) {
    return tracing.enterSpan("handleRequest", async (span) => {
      span.setAttribute("url.path", new URL(request.url).pathname);
      const data = await env.MY_KV.get("key");
      return new Response(data);
    });
  },
};
```

Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The `Span` object provides `setAttribute(key, value)` for attaching metadata and an `isTraced` property to check whether the current request is being sampled.

![Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1988,height=670,format=webp/_astro/wobs_custom_spans_screenshot.B-hsHjyv.png)

[Tracing must be enabled](https://developers.cloudflare.com/workers/observability/traces/#how-to-enable-tracing) in your Wrangler configuration for spans to be recorded.

For full API details and examples, refer to [Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/#page","headline":"Workers tracing now supports custom spans","description":"Create custom trace spans in your Workers code to instrument application-specific logic alongside automatic platform instrumentation.","url":"https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/og.png?v=3201f0b53bc69c59","dateModified":"2026-06-16","datePublished":"2026-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
