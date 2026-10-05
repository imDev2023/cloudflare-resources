---
description: Source maps are now Generally Available with a larger maximum size limit
title: Source Maps are Generally Available
image: https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/og.png?v=9705ddf09a95c3dd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 25, 2025

## Source Maps are Generally Available

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB. Previously, the maximum size limit was 15 MB uncompressed.

Source maps help map between the original source code and the transformed/minified code that gets deployed to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions onto the original source code making it easier to debug.

![Stack Trace without Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1908,height=198,format=webp/_astro/without-source-map.ByYR83oU.png)

With **no source maps uploaded**: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references `js` instead of `ts`.

![Stack Trace with Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=238,format=webp/_astro/with-source-map.PipytmVe.png)

With **source maps uploaded**: all methods reference the correct files and line numbers.

Uploading source maps and stack trace remapping happens out of band from the Worker execution, so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.

To enable source maps, add the following to your [Pages Function's](https://developers.cloudflare.com/pages/functions/source-maps/) or [Worker's](https://developers.cloudflare.com/workers/observability/source-maps/) wrangler configuration:

```jsonc
{
	"upload_source_maps": true
}
```

```toml
upload_source_maps = true
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/#page","headline":"Source Maps are Generally Available","description":"Source maps are now Generally Available with a larger maximum size limit","url":"https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/og.png?v=9705ddf09a95c3dd","dateModified":"2025-03-25","datePublished":"2025-03-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
