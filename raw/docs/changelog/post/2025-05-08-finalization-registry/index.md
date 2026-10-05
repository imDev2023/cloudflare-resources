---
description: With the introduction of FinalizationRegistry in Workers Runtime, toolchains like Emscripten and wasm-bindgen can automatically reclaim unused WebAssembly heap and reduce memory leaks.
title: Improved memory efficiency for WebAssembly Workers
image: https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/og.png?v=64aba4c20c5a8cca
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 8, 2025

## Improved memory efficiency for WebAssembly Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[FinalizationRegistry ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry) is now available in Workers. You can opt-in using the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag.

This can reduce memory leaks when using WebAssembly-based Workers, which includes [Python Workers](https://developers.cloudflare.com/workers/languages/python/) and [Rust Workers](https://developers.cloudflare.com/workers/languages/rust/). The FinalizationRegistry works by enabling toolchains such as [Emscripten ↗︎](https://emscripten.org/) and [wasm-bindgen ↗︎](https://wasm-bindgen.github.io/wasm-bindgen/) to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using [memory profiling](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/), you may want to enable the FinalizationRegistry.

For more information refer to the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/#page","headline":"Improved memory efficiency for WebAssembly Workers","description":"With the introduction of FinalizationRegistry in Workers Runtime, toolchains like Emscripten and wasm-bindgen can automatically reclaim unused WebAssembly heap and reduce memory leaks.","url":"https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/og.png?v=64aba4c20c5a8cca","dateModified":"2025-05-08","datePublished":"2025-05-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
