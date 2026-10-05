---
description: Configure Web Analytics for single-page applications.
title: Web Analytics for SPAs
image: https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/og.png?v=18b4e75383359b63
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/web-analytics/llms.txt  
> Use this file to discover all available pages before exploring further.

# Web Analytics for SPAs

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Web Analytics automatically tracks user interactions on Single Page Applications (SPAs) via one of the following three methods, depending on which is supported:

1. Using the [Soft Navigations API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations)
2. Listening on `navigate` events via the [Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)
3. By patching the [History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API)'s `pushState` function and listening to the `onpopstate` event

## Disable SPA measurement

If you want to disable the automatic tracking for SPAs, you can do so by adding the `spa` option with a value of `false` in the data attribute of the script tag, as shown below:

```html
<script
  type="module"
  src="https://static.cloudflareinsights.com/beacon.min.js"
  data-cf-beacon='{"token": "...", "spa": false}'
></script>
```

Note: this requires using [the manual embedding approach](https://developers.cloudflare.com/web-analytics/get-started/#sites-not-proxied-through-cloudflare).

### Google Tag Manager (GTM)

If you are using Google Tag Manager (GTM), you can disable SPA tracking by passing the `spa=false` option via the query string in the script URL:

```html
<script
  type="module"
  src="https://static.cloudflareinsights.com/beacon.min.js?token=...&spa=false"
></script>
```
