---
description: Deploy a static site by dragging a folder or ZIP file to Cloudflare, preview it for one hour, then claim it to keep the deployment.
title: Cloudflare Drop
image: https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/og.png?v=7a904b722e8b633b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 8, 2026

## Cloudflare Drop

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Drop ↗︎](https://cloudflare.com/drop) lets you deploy a static site to Cloudflare without requiring a Cloudflare account to get started.

![Cloudflare Drag and Drop upload screen for browsing folders or ZIP files](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2498,height=1294,format=webp/_astro/cloudflare-drag-and-drop-upload.KujM69eS.png)

Upload a folder or zip file of static assets (static HTML, CSS, JavaScript, images, and fonts) and get a temporary live preview that stays live for 1 hour. During that window, you can test the site, share the preview URL, or [claim the deployment](https://developers.cloudflare.com/workers/platform/claim-deployments/) to keep it.

![Cloudflare Drag and Drop temporary live preview screen with claim and copy claim link actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2936,height=1594,format=webp/_astro/cloudflare-drag-and-drop-preview.BQ1__XRX.png)

When you are ready to make the deployment permanent, click **Claim** to sign in or create a Cloudflare account. You can claim the site into an existing Cloudflare account or create a new account for the deployment.

Note

If you are creating a new account, you will need to verify your email address before continuing.

![Cloudflare Drag and Drop claim account screen with a countdown before the claim link expires](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1712,height=812,format=webp/_astro/cloudflare-drag-and-drop-claim.8Zv6px9B.png)

After claiming the site, you can:

- **Add a domain**: [Connect](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) an existing domain or purchase a new one for your site.
- **Enable [observability](https://developers.cloudflare.com/workers/observability/)**: Monitor your site's performance and usage.
- **Enable [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)**: Allow AI agents to access your site's content in Markdown.
- **Control access**: Make your site [private](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) and choose who can view it.

![Claimed Cloudflare Drag and Drop site setup screen showing options to add a domain, control access, enable observability, and enable Markdown for agents](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1812,height=1266,format=webp/_astro/cloudflare-drag-and-drop-post-claim.DvlaNmI7.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/#page","headline":"Cloudflare Drop","description":"Deploy a static site by dragging a folder or ZIP file to Cloudflare, preview it for one hour, then claim it to keep the deployment.","url":"https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/og.png?v=7a904b722e8b633b","dateModified":"2026-07-08","datePublished":"2026-07-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
