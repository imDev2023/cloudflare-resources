---
description: Custom Errors can now fetch and store fallback assets even if the origin returns a 4xx or 5xx status code.
title: More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes
image: https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/og.png?v=54f517ccb920c3ac
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 9, 2025

## More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) can now fetch and store [assets](https://developers.cloudflare.com/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard) and [error pages](https://developers.cloudflare.com/rules/custom-errors/#error-pages) from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.

**What’s new:**

- You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.
- These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.

This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.

Learn more in the [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/#page","headline":"More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes","description":"Custom Errors can now fetch and store fallback assets even if the origin returns a 4xx or 5xx status code.","url":"https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/og.png?v=54f517ccb920c3ac","dateModified":"2025-06-09","datePublished":"2025-06-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
