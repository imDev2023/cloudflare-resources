---
description: Deployments on workers-rs are now more reliable with automatic panic recovery
title: Panic Recovery for Rust Workers
image: https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/og.png?v=c91c4f34f35ab91d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 19, 2025

## Panic Recovery for Rust Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In [workers-rs ↗︎](https://github.com/cloudflare/workers-rs), Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.

Now, when a panic occurs, in-flight requests will throw 500 errors, but the Worker will automatically and instantly recover for future requests.

This ensures more reliable deployments. Automatic panic recovery is enabled for all new workers-rs deployments as of version 0.6.5, with no configuration required.

#### Fixing Rust Panics with Wasm Bindgen

Rust Workers are built with Wasm Bindgen, which treats panics as non-recoverable. After a panic, the entire Wasm application is considered to be in an invalid state.

We now attach a default panic handler in Rust:

```rust
std::panic::set_hook(Box::new(move |panic_info| {
  hook_impl(panic_info);
}));
```

Which is registered by default in the JS initialization:

```js
import { setPanicHook } from "./index.js";
setPanicHook(function (err) {
	console.error("Panic handler!", err);
});
```

When a panic occurs, we reset the Wasm state to revert the Wasm application to how it was when the application started.

#### Resetting VM State in Wasm Bindgen

We worked upstream on the Wasm Bindgen project to implement a new [`--experimental-reset-state-function` compilation option ↗︎](https://github.com/wasm-bindgen/wasm-bindgen/pull/4644) which outputs a new `__wbg_reset_state` function.

This function clears all internal state related to the Wasm VM, and updates all function bindings in place to reference the new WebAssembly instance.

One other necessary change here was associating Wasm-created JS objects with an instance identity. If a JS object created by an earlier instance is then passed into a new instance later on, a new "stale object" error is specially thrown when using this feature.

#### Layered Solution

Building on this new Wasm Bindgen feature, layered with our new default panic handler, we also added a proxy wrapper to ensure all top-level exported class instantiations (such as for Rust Durable Objects) are tracked and fully reinitialized when resetting the Wasm instance. This was necessary because the workerd runtime will instantiate exported classes, which would then be associated with the Wasm instance.

This approach now provides full panic recovery for Rust Workers on subsequent requests.

Of course, we never want panics, but when they do happen they are isolated and can be investigated further from the error logs - avoiding broader service disruption.

#### WebAssembly Exception Handling

In the future, full support for recoverable panics could be implemented without needing reinitialization at all, utilizing the [WebAssembly Exception Handling ↗︎](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md) proposal, part of the newly announced [WebAssembly 3.0 ↗︎](https://webassembly.org/news/2025-09-17-wasm-3.0/) specification. This would allow unwinding panics as normal JS errors, and concurrent requests would no longer fail.

**We're making significant improvements to the reliability of [Rust Workers ↗︎](https://github.com/cloudflare/workers-rs). Join us in `#rust-on-workers` on the [Cloudflare Developers Discord ↗︎](https://discord.gg/cloudflaredev) to stay updated.**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/#page","headline":"Panic Recovery for Rust Workers","description":"Deployments on workers-rs are now more reliable with automatic panic recovery","url":"https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-19-workers-rs-panic-recovery/og.png?v=c91c4f34f35ab91d","dateModified":"2025-09-19","datePublished":"2025-09-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
