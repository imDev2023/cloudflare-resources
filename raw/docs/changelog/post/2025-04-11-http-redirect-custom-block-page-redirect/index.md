---
description: Redirect traffic with a Gateway HTTP Redirect policy, or with the block page in an HTTP or DNS Block policy.
title: HTTP redirect and custom block page redirect
image: https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/og.png?v=2182b12707ce0c31
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 11, 2025

## HTTP redirect and custom block page redirect

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use more flexible redirect capabilities in Cloudflare One with Gateway.

- A new **Redirect** action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.
- For **Block** actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.

Learn more in our documentation for [HTTP Redirect](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#redirect) and [Block page redirect](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/#page","headline":"HTTP redirect and custom block page redirect","description":"Redirect traffic with a Gateway HTTP Redirect policy, or with the block page in an HTTP or DNS Block policy.","url":"https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/og.png?v=2182b12707ce0c31","dateModified":"2025-04-11","datePublished":"2025-04-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
