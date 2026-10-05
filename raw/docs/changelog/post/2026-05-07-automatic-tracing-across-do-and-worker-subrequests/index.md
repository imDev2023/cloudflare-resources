---
description: Traces now propagate across service binding and Durable Object calls, producing a single unified trace instead of separate disconnected traces.
title: Automatic tracing across Durable Object and Worker subrequests
image: https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/og.png?v=22f656068337f814
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## Automatic tracing across Durable Object and Worker subrequests

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, [automatic tracing](https://developers.cloudflare.com/workers/observability/traces/) produced disconnected traces when a Worker called another Worker through a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) or [Durable Object](https://developers.cloudflare.com/durable-objects/).

![Unified trace showing nested spans across a Durable Object subrequest and a service binding call](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1824,height=1156,format=webp/_astro/2026-04-28-worker-to-worker-context-prop.Db1qNQJL.png)

This means you can:

- Follow a request through your entire Worker architecture in one trace view
- See service binding and Durable Object calls as nested child spans instead of separate traces
- Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via [OpenTelemetry](https://developers.cloudflare.com/workers/observability/opentelemetry-export/)

[Tracing must be enabled](https://developers.cloudflare.com/workers/observability/traces/#how-to-enable-tracing) in your Wrangler configuration for traces to be recorded. Checkout [Workers tracing](https://developers.cloudflare.com/workers/observability/traces/) to get started.

Up next, we are working on external trace context propagation using [W3C Trace Context standards ↗︎](https://www.w3.org/TR/trace-context/), which will allow traces from your Workers to link with traces from services outside of Cloudflare.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/#page","headline":"Automatic tracing across Durable Object and Worker subrequests","description":"Traces now propagate across service binding and Durable Object calls, producing a single unified trace instead of separate disconnected traces.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/og.png?v=22f656068337f814","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
