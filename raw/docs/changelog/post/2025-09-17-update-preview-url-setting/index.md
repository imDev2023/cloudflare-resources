---
description: We performed a one-time update to disable preview URLs on Workers with workers.dev disabled to require an explicit opt-in.
title: Preview URLs now default to opt-in
image: https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/og.png?v=9a622928d8bde8c3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 17, 2025

## Preview URLs now default to opt-in

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To prevent the accidental exposure of applications, we've updated how [Worker preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.

#### One-Time Update for Workers with workers.dev Disabled

We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) was also disabled.

Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.

If your Worker was affected, its preview URL (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) will now direct to an informational page explaining this change.

**How to Re-enable Your Preview URL**

If your preview URL was disabled, you can re-enable it [via the Cloudflare dashboard](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable) by navigating to your Worker's Settings page and toggling on the Preview URL.

Alternatively, you can use Wrangler by adding the `preview_urls = true` setting to your Wrangler file and redeploying the Worker.

```jsonc
{
  "preview_urls": true
}
```

```toml
preview_urls = true
```

**Note:** You can set `preview_urls = true` with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults `preview_urls` to false, ensuring preview URLs are always enabled by explicit choice.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/#page","headline":"Preview URLs now default to opt-in","description":"We performed a one-time update to disable preview URLs on Workers with workers.dev disabled to require an explicit opt-in.","url":"https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/og.png?v=9a622928d8bde8c3","dateModified":"2025-09-17","datePublished":"2025-09-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
