---
description: The pipeline field in Wrangler pipeline binding configuration has been renamed to stream. The old field is deprecated but still accepted.
title: Pipeline binding configuration field renamed to stream
image: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/og.png?v=24304b663b6a615d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 4, 2026

## Pipeline binding configuration field renamed to stream

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `pipeline` field inside the `pipelines` binding configuration in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) has been renamed to `stream`. The old field is deprecated but still accepted.

Update your configuration to use `stream` to avoid the deprecation warning.

**Before (deprecated):**

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "pipelines": [
    {
      "binding": "MY_PIPELINE",
      "pipeline": "<STREAM_ID>"
    }
  ]
}
```

```toml
[[pipelines]]
binding = "MY_PIPELINE"
pipeline = "<STREAM_ID>"
```

**After:**

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "pipelines": [
    {
      "binding": "MY_PIPELINE",
      "stream": "<STREAM_ID>"
    }
  ]
}
```

```toml
[[pipelines]]
binding = "MY_PIPELINE"
stream = "<STREAM_ID>"
```

No other changes are required. The binding name, TypeScript types, and runtime API (`env.MY_PIPELINE.send(...)`) remain the same.

For more information on configuring pipeline bindings, refer to [Writing to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#configure-pipeline-binding).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/#page","headline":"Pipeline binding configuration field renamed to stream","description":"The pipeline field in Wrangler pipeline binding configuration has been renamed to stream. The old field is deprecated but still accepted.","url":"https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/og.png?v=24304b663b6a615d","dateModified":"2026-06-04","datePublished":"2026-06-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
