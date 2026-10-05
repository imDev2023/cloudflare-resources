---
description: Wrangler now provides a better user experience when deploying a worker that was previously deployed via the Cloudflare dashboard.
title: Better local deployment flow for Cloudflare Workers
image: https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/og.png?v=716e9a9d206ffabc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 21, 2025

## Better local deployment flow for Cloudflare Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Until now, if a Worker had been previously deployed via the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com), a subsequent deployment done via the Cloudflare Workers CLI, [**Wrangler**](https://developers.cloudflare.com/workers/wrangler/) (through the [`deploy` command](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy)), would allow the user to override the Worker's dashboard settings without providing details on what dashboard settings would be lost.

Now instead, `wrangler deploy` presents a helpful representation of the differences between the [local configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) and the remote dashboard settings, and offers to update your local configuration file for you.

See example below showing a before and after for `wrangler deploy` when a local configuration is expected to override a Worker's dashboard settings:

### Before

![wrangler deploy run before the improved workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=785,height=257,format=webp/_astro/before.Bz-MOePT.png)

### After

![wrangler deploy run after the improved workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=788,height=492,format=webp/_astro/after.BrkkBaRL.png)

Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.

Update to [Wrangler](https://developers.cloudflare.com/workers/wrangler/) v4.50.0 or greater to take advantage of this improved deploy flow.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/#page","headline":"Better local deployment flow for Cloudflare Workers","description":"Wrangler now provides a better user experience when deploying a worker that was previously deployed via the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/og.png?v=716e9a9d206ffabc","dateModified":"2025-11-21","datePublished":"2025-11-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
