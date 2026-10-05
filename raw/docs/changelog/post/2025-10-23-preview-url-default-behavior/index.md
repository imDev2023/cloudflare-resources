---
description: If a Workers Preview URL setting is not explicitly configured, its default behavior will now match the setting of the workers.dev subdomain.
title: Workers Preview URL default behavior now matches your workers.dev setting
image: https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/og.png?v=6f13e3ca838a1c0b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 23, 2025

## Workers Preview URL default behavior now matches your workers.dev setting

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have updated the default behavior for Cloudflare Workers [Preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/). **Going forward, if a preview URL setting is not [explicitly configured](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable) during deployment, its default behavior will automatically match the setting of your [`workers.dev` subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/).**

This change is intended to provide a more intuitive and secure experience by aligning your preview URL's default state with your `workers.dev` configuration to prevent cases where a preview URL might remain public even after you disabled your `workers.dev` route.

**What this means for you:**

- **If neither setting is configured:** both the workers.dev route and the preview URL will default to enabled
- **If your workers.dev route is enabled and you do not explicitly set Preview URLs to enabled or disabled:** Preview URLs will default to enabled
- **If your workers.dev route is disabled and you do not explicitly set Preview URLs to enabled or disabled:** Preview URLs will default to disabled

You can override the default setting by explicitly enabling or disabling the preview URL in your Worker's configuration through the [API](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/), [Dashboard](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#from-the-dashboard), or [Wrangler](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#from-the-wrangler-configuration-file).

**Wrangler Version Behavior**

The default behavior depends on the version of Wrangler you are using. This new logic applies to the latest version. Here is a summary of the behavior across different versions:

- **Before v4.34.0:** Preview URLs defaulted to enabled, regardless of the workers.dev setting.
- **v4.34.0 up to (but not including) v4.44.0:** Preview URLs defaulted to disabled, regardless of the workers.dev setting.
- **v4.44.0 or later:** Preview URLs now default to matching your workers.dev setting.

**Why we’re making this change**

In July, [we introduced preview URLs to Workers](https://developers.cloudflare.com/changelog/2025-07-23-workers-preview-urls/), which let you preview code changes before deploying to production. This made disabling your Worker’s workers.dev URL an ambiguous action — the preview URL, served as a subdomain of `workers.dev` (ex: `preview-id-worker-name.account-name.workers.dev`) would still be live even if you had disabled your Worker’s `workers.dev` route. If you misinterpreted what it meant to disable your `workers.dev` route, you might unintentionally leave preview URLs enabled when you didn’t mean to, and expose them to the public Internet.

To address this, we made a [one-time update](https://developers.cloudflare.com/changelog/2025-09-17-update-preview-url-setting/) to disable preview URLs on existing Workers that had their workers.dev route disabled and changed the default behavior to be disabled for all new deployments where a preview URL setting was not explicitly configured.

While this change helped secure many customers, it was disruptive for customers who keep their `workers.dev` route enabled and actively use the preview functionality, as it now required them to explicitly enable preview URLs on every redeployment.This new, more intuitive behavior ensures that your preview URL settings align with your `workers.dev` configuration by default, providing a more secure and predictable experience.

**Securing access to `workers.dev` and preview URL endpoints**

To further secure your `workers.dev` subdomain and preview URL, you can [enable Cloudflare Access with a single click](https://developers.cloudflare.com/changelog/2025-10-03-one-click-access-for-workers/) in your Worker's settings to limit access to specific users or groups.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/#page","headline":"Workers Preview URL default behavior now matches your workers.dev setting","description":"If a Workers Preview URL setting is not explicitly configured, its default behavior will now match the setting of the workers.dev subdomain.","url":"https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-23-preview-url-default-behavior/og.png?v=6f13e3ca838a1c0b","dateModified":"2025-10-23","datePublished":"2025-10-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
