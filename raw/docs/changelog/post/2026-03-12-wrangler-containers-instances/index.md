---
description: A new Wrangler command to list all instances for a Container application.
title: List Container instances with `wrangler containers instances`
image: https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/og.png?v=54af7eb07fa82321
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 12, 2026

## List Container instances with \`wrangler containers instances\`

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [`wrangler containers instances`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances) command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.

The command displays each instance's ID, name, state, location, version, and creation time:

```sh
wrangler containers instances <APPLICATION_ID>
```

Use the `--json` flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.

For the full list of options, refer to the [`containers instances` command reference](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/#page","headline":"List Container instances with `wrangler containers instances`","description":"A new Wrangler command to list all instances for a Container application.","url":"https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/og.png?v=54af7eb07fa82321","dateModified":"2026-03-12","datePublished":"2026-03-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
